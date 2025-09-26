FROM ubuntu:24.04

SHELL ["/bin/bash", "-c"]
RUN useradd -ms /bin/bash ftsky

ENV HOME=/home/ftsky
ENV DEBIAN_FRONTEND=noninteractive

USER ftsky
WORKDIR $HOME
RUN mkdir software

USER root

RUN apt-get update && \
    apt-get install -y \
    git \
    wget \
    cmake \
    build-essential \
    g++ \
    pkg-config \
    casacore-data \
    casacore-dev \
    casacore-tools \
    libblas-dev \
    liblapack-dev \
    python3 \
    libpython3-dev \
    libboost-date-time-dev \
    libboost-test-dev \
    libboost-program-options-dev \
    libboost-system-dev \
    libboost-filesystem-dev \
    libcfitsio-dev \
    libfftw3-dev \
    libgsl-dev \
    libhdf5-dev \
    libopenmpi-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    python3-pytest \
    python3-sphinx \
    python3-casacore \
    python3-setuptools

WORKDIR $HOME/software
RUN git clone \
	--depth 1 \
        --branch v3.5 \
	https://gitlab.com/aroffringa/wsclean.git && \
    cd wsclean && \
    mkdir build && \
    cd build && \
    cmake $HOME/software/wsclean \
	-DPORTABLE=True \
    	-DCMAKE_PREFIX_PATH="/usr/local" && \
    make -j`nproc` && \
    make install -j`nproc`

WORKDIR $HOME/software
RUN wget --no-check-certificate https://casa.nrao.edu/download/distro/casa/release/rhel/casa-6.6.4-34-py3.10.el8.tar.xz && \
    tar xf casa-6.6.4-34-py3.10.el8.tar.xz && \
    rm -rf casa-6.6.4-34-py3.10.el8.tar.xz
ENV PATH=$HOME/software/casa-6.6.4-34-py3.10.el8/bin:$PATH

USER ftsky
WORKDIR $HOME

RUN mkdir ~/.casa
RUN mkdir ~/.casa/data
RUN casa --log2term -c "exit"
ENV CASASITECONFIG=$HOME/.casa/config.py
COPY --chown=ftsky:ftsky config.py $HOME/.casa/config.py

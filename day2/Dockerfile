FROM ubuntu:24.04

SHELL ["/bin/bash", "-c"]
RUN useradd -ms /bin/bash ftsky

ENV HOME=/home/ftsky
ENV DEBIAN_FRONTEND=noninteractive

USER root

RUN apt-get -qq update && \
    apt-get -qq install -y \
    git \
    cmake \
    build-essential \
    g++ \
    pkg-config \
    casacore-data \
    casacore-dev \
    casacore-tools \
    libblas-dev liblapack-dev \
    python3 \
    libpython3-dev \
    libboost-date-time-dev libboost-test-dev \
    libboost-program-options-dev libboost-system-dev libboost-filesystem-dev \
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
    python3-setuptools \
    wget \
    nvidia-cuda-toolkit

# Install EveryBeam
RUN mkdir /external && \
    cd /external && \
    git clone \
	--depth 1 \
	--branch v0.6.2 \
	--single-branch https://git.astron.nl/RD/EveryBeam.git && \
    mkdir /external/EveryBeam/build && \
    cd /external/EveryBeam/build && \
    cmake ../ && \
    make install -j`nproc`

# Install IDG
RUN cd /external && \
    git clone \
	--depth 1 \
	--branch 1.2.0 \
	--single-branch https://git.astron.nl/RD/idg.git && \
    mkdir /external/idg/build && \
    cd /external/idg/build && \
    cmake -DBUILD_LIB_CPU=ON \
          -DBUILD_LIB_CUDA=ON \
          -DBUILD_WITH_PYTHON=ON ../ && \
    make install -j`nproc`

# Install WSClean
RUN git clone --depth 1 --branch v3.5 https://gitlab.com/aroffringa/wsclean
WORKDIR /wsclean
RUN \
    mkdir /build && \
    cd /build && \
    cmake ../wsclean \
	-DPORTABLE=True \
    	-DCMAKE_PREFIX_PATH="/usr/local;/external/idg/build" \
	-DIDGAPI_VERSION=1.2.0 && \
    make -j`nproc` && \
    make install && \
    wsclean --version

# Download and install CASA.
RUN wget --no-check-certificate https://casa.nrao.edu/download/distro/casa/release/rhel/casa-6.6.4-34-py3.10.el8.tar.xz && \
    tar xf casa-6.6.4-34-py3.10.el8.tar.xz && \
    rm -rf casa-6.6.4-34-py3.10.el8.tar.xz

USER ftsky
WORKDIR $HOME

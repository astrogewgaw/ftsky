FROM ubuntu:24.04

SHELL ["/bin/bash", "-c"]
RUN useradd -ms /bin/bash ftsky

ENV HOME=/home/ftsky
ENV DEBIAN_FRONTEND=noninteractive

USER ftsky
WORKDIR $HOME
RUN mkdir software

USER root

RUN apt-get update && apt-get install -y \
    build-essential \
    casacore-data \
    casacore-dev \
    casacore-tools \
    cmake \
    g++ \
    git \
    libblas-dev \
    libboost-date-time-dev \
    libboost-filesystem-dev \
    libboost-program-options-dev \
    libboost-system-dev \
    libboost-test-dev \
    libcfitsio-dev \
    libfftw3-dev \
    libgsl-dev \
    libhdf5-dev \
    liblapack-dev \
    libopenmpi-dev \
    libpython3-dev \
    pkg-config \
    python3 \
    python3-casacore \
    python3-dev \
    python3-numpy \
    python3-pytest \
    python3-setuptools \
    python3-sphinx \
    software-properties-common \
    wget

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
RUN wget --no-check-certificate https://casa.nrao.edu/download/distro/casa/release/rhel/casa-6.7.0-31-py3.10.el8.tar.xz && \
  tar xf casa-6.7.0-31-py3.10.el8.tar.xz && \
  rm -rf casa-6.7.0-31-py3.10.el8.tar.xz && \
  mv casa-6.7.0-31-py3.10.el8 casa
ENV PATH=$HOME/software/casa/bin:$PATH

RUN add-apt-repository -y ppa:cartavis-team/carta \
    && apt-get update \
    && apt-get install -y carta

USER ftsky
WORKDIR $HOME

RUN mkdir $HOME/.casa
RUN mkdir $HOME/.casa/data
RUN casa --log2term -c "exit"
ENV CASASITECONFIG=$HOME/.casa/config.py
COPY --chown=ftsky:ftsky config.py $HOME/.casa/config.py

RUN echo "filetype plugin indent on" >> $HOME/.vimrc && \
    echo "set tabstop=4" >> $HOME/.vimrc && \
    echo "set shiftwidth=4" >> $HOME/.vimrc && \
    echo "set expandtab" >> $HOME/.vimrc && \
    echo "set pastetoggle=<F2>" >> $HOME/.vimrc && \
    echo "set hlsearch" >> $HOME/.vimrc && \
    echo "syntax on" >> $HOME/.vimrc

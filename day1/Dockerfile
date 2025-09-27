FROM mambaorg/micromamba:2.3.2 AS micromamba
FROM ubuntu:24.04

SHELL ["/bin/bash", "-c"] 
RUN useradd -ms /bin/bash ftsky

ENV HOME=/home/ftsky

ENV LD_LIBRARY_PATH=$HOME/software/lib:/usr/local/lib
ENV PATH=$PATH:$HOME/software/bin:$HOME/.local/bin
ENV DEBIAN_FRONTEND=noninteractive
ENV OMP_NUM_THREADS=1

ENV ONNX_HOME=$HOME/software/onnx_models
ENV TEMPO2=$HOME/software/tempo2/T2runtime
ENV YMW16_DIR=$HOME/software/XLibs/src/ymw16
ENV PSRCAT_FILE=$HOME/software/psrcat_tar/psrcat.db

RUN apt-get update && apt-get install -y --no-install-recommends \
	cmake \
	git \
	mpich \
  autoconf \
  g++ \
  gfortran \
  libblas-dev \
  libboost-log-dev \
  libboost-program-options-dev \
  libcfitsio-dev \
  libeigen3-dev \
  libfftw3-dev \
  liblapack-dev \
  libpng-dev \
  libtool \
  libx11-dev \
  make \
  pgplot5 \
  wget

USER ftsky
WORKDIR $HOME
RUN mkdir software

USER root

ARG MAMBA_USER=ftsky
ARG MAMBA_USER_ID=1001
ARG MAMBA_USER_GID=1001
ENV MAMBA_USER=$MAMBA_USER
ENV MAMBA_NO_LOW_SPEED_LIMIT=1
ENV MAMBA_ROOT_PREFIX=$HOME/software/conda
ENV MAMBA_EXE=$HOME/software/bin/micromamba

COPY --from=micromamba "/bin/micromamba" "$MAMBA_EXE"
COPY --from=micromamba 	/usr/local/bin/_activate_current_env.sh /usr/local/bin/_activate_current_env.sh
COPY --from=micromamba 	/usr/local/bin/_dockerfile_shell.sh /usr/local/bin/_dockerfile_shell.sh
COPY --from=micromamba 	/usr/local/bin/_entrypoint.sh /usr/local/bin/_entrypoint.sh
COPY --from=micromamba 	/usr/local/bin/_dockerfile_initialize_user_accounts.sh /usr/local/bin/_dockerfile_initialize_user_accounts.sh
COPY --from=micromamba 	/usr/local/bin/_dockerfile_setup_root_prefix.sh /usr/local/bin/_dockerfile_setup_root_prefix.sh

RUN /usr/local/bin/_dockerfile_initialize_user_accounts.sh && \
    /usr/local/bin/_dockerfile_setup_root_prefix.sh

USER ftsky

SHELL ["/usr/local/bin/_dockerfile_shell.sh"]
RUN micromamba install -y -n base --channel conda-forge python==3.10 && \
    micromamba clean --all --yes
ARG MAMBA_DOCKERFILE_ACTIVATE=1

WORKDIR $HOME/software
RUN git clone https://github.com/thepetabyteproject/your.git
WORKDIR $HOME/software/your
RUN python -m pip install -r requirements.txt
RUN python -m pip install .

WORKDIR $HOME/software
RUN git clone https://github.com/devanshkv/fetch
WORKDIR $HOME/software/fetch
RUN git checkout onnx
RUN python -m pip install .

WORKDIR $HOME/software
RUN git clone https://github.com/liberfa/erfa.git
WORKDIR $HOME/software/erfa
RUN ./bootstrap.sh
RUN ./configure --prefix=$HOME/software
RUN make -j 8 && make install

WORKDIR $HOME/software
RUN git clone https://bitbucket.org/psrsoft/tempo2.git
WORKDIR $HOME/software/tempo2
RUN rm -rf .git
RUN ./bootstrap
RUN ./configure --prefix=$HOME/software
RUN make -j 8 && make install
RUN make plugins-install
RUN make clean

WORKDIR $HOME/software
RUN wget https://www.atnf.csiro.au/research/pulsar/psrcat/downloads/psrcat_pkg.tar.gz && \
    tar -zxvf psrcat_pkg.tar.gz
WORKDIR $HOME/software/psrcat_tar
RUN source makeit && cp psrcat $HOME/software/bin

WORKDIR $HOME/software
RUN git clone https://github.com/ypmen/XLibs
RUN git clone https://github.com/ypmen/PlotX
RUN git clone https://github.com/ypmen/PulsarX
RUN git clone https://github.com/ypmen/TransientX

WORKDIR $HOME/software/XLibs
RUN ./bootstrap
RUN ./configure \
	--prefix=$HOME/software \
	CXXFLAGS="-std=c++11 -O3" \
	LDFLAGS="-L$HOME/software/lib" \
	CPPFLAGS="-I$HOME/software/include"
RUN make -j 8 && make install
RUN make clean

WORKDIR $HOME/software/PlotX
RUN ./bootstrap
RUN ./configure --prefix=$HOME/software
RUN make -j 8 && make install
RUN make clean

WORKDIR $HOME/software/PulsarX
RUN ./bootstrap
RUN ./configure \
	--prefix=$HOME/software \
	CXXFLAGS="-std=c++11 -O3" \
	LDFLAGS="-L$HOME/software/lib" \
	CPPFLAGS="-I$HOME/software/include"
RUN make -j 8 && make install
RUN make clean

WORKDIR $HOME/software/TransientX
RUN ./bootstrap
RUN ./configure \
	--prefix=$HOME/software \
	CXXFLAGS="-std=c++11 -O3" \
	LDFLAGS="-L$HOME/software/lib" \
	CPPFLAGS="-I$HOME/software/include"
RUN make -j 8 && make install
RUN make clean

RUN echo "filetype plugin indent on" >> $HOME/.vimrc && \
    echo "set tabstop=4" >> $HOME/.vimrc && \
    echo "set shiftwidth=4" >> $HOME/.vimrc && \
    echo "set expandtab" >> $HOME/.vimrc && \
    echo "set pastetoggle=<F2>" >> $HOME/.vimrc && \
    echo "set hlsearch" >> $HOME/.vimrc && \
    echo "syntax on" >> $HOME/.vimrc

WORKDIR $HOME
ENTRYPOINT [ "/bin/bash" ]

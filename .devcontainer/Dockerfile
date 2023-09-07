## Dockerfile for VSCode DevContainer environment
#  This project can be built on a host with Docker to install all
#  required dependencies.

# build stage
FROM python:3.11 AS base

## Environment
ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1 \
    ## Pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

## Python version to install with pyenv
ARG PYENV_GLOBAL_VER=3.11.4

## Install git & curl
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y \
    git \
    curl

## Install pyenv dependencies
RUN apt-get install -y --no-install-recommends \
    make \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    llvm \
    libncurses5-dev \
    xz-utils \
    tk-dev \
    libxml2-dev \
    libxmlsec1-dev \
    libffi-dev \
    liblzma-dev

RUN apt-get install -y mecab-ipadic-utf8


FROM base AS build
ARG PYENV_GLOBAL_VER

# install pyenv
ENV HOME="/root"

WORKDIR $HOME
RUN apt-get install -y git
RUN git clone --depth=1 https://github.com/pyenv/pyenv.git .pyenv

ENV PYENV_ROOT="$HOME/.pyenv"
ENV PATH="$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"

## Install pyenv
RUN pyenv install ${PYENV_GLOBAL_VER}
RUN pyenv global ${PYENV_GLOBAL_VER}

FROM python:3.11 AS build-pdm

# install PDM
RUN pip install -U pip setuptools wheel
RUN pip install pdm

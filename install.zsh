#!/bin/zsh

git clone --recursive https://github.com/cplee/prezto.git "${ZDOTDIR:-$HOME}/.zprezto"

${ZDOTDIR:-$HOME}/.zprezto/link.zsh

chsh -s /bin/sh

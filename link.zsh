#!/bin/zsh

setopt EXTENDED_GLOB
for rcfile in "${ZDOTDIR:-$HOME}"/.zprezto/runcoms/^README.md(N); do
  if [[ ! -a "${ZDOTDIR:-$HOME}/.${rcfile:t}" ]]; then
    echo ">> ${rcfile}"
    ln -s "$rcfile" "${ZDOTDIR:-$HOME}/.${rcfile:t}"
  fi
done

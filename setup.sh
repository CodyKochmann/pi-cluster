#!/bin/bash
# this is the original setup for a raspberry pi to set itself up on.

function install {
  sudo apt-get install -q -y @
}

function loadlist {
  cat $1 | grep -v "\#" | grep .
}

for i in `loadlist install.list`
do
  install $i
done


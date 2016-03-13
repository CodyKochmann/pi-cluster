#!/bin/bash
# this is the original setup for a raspberry pi to set itself up on.

function install {
  sudo apt-get install -q -y @
}

for i in `cat install.list`
do
  install $i
done


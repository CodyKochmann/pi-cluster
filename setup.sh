#!/bin/bash
# this is the original setup for a raspberry pi to set itself up on.

function install {
  sudo apt-get install -q -y $@
}

function pipinstall {
  sudo pip install -q $@
}

function loadlist {
  cat $1 | grep -v "\#" | grep .
}

function runinstallation { # 1=function_name 2=listname
  for i in `loadlist $2`
  do
    $1 $i
  done
}

# install the main list
runinstallation install.list install
# install pip's install list
runinstallation pipinstall pip-install.list

#!/bin/bash

# Installs peda from git to ~/.peda
git clone https://github.com/longld/peda.git ~/.peda

# Sources peda to .gdbinit
echo "source ~/.peda/peda.py" >> ~/.gdbinit

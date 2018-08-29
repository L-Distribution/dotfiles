#!/bin/bash

# Download & Install NVM
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash

# Export & setup NVM environment 
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# Source nvm to zsh
echo 'source ~/.nvm/nvm.sh' >> ~/.zshrc

# Install latest LTS version of Node.js
nvm install --lts

# Install latest version of Node.js
nvm install node

# Install letest version of npm
nvm install-latest-npm


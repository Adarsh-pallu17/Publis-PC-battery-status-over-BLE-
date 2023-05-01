#!/bin/bash

# Install Homebrew if not already installed
which -s brew
if [[ $? != 0 ]] ; then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Install Python 3 if not already installed
if ! command -v python3 &> /dev/null
then
    echo "Python 3 is not installed. Installing..."
    brew install python
fi

# Install bluepy library
echo "Installing bluepy library..."
brew install bluepy

# Install psutil library
echo "Installing psutil library..."
pip3 install psutil

# Done
echo "All libraries installed successfully!"

#!/bin/bash

# Install Python 3 if not already installed
if ! command -v python3 &> /dev/null
then
    echo "Python 3 is not installed. Installing..."
    sudo apt-get update
    sudo apt-get install -y python3
fi

# Install bluepy library
echo "Installing bluepy library..."
sudo apt-get update
sudo apt-get install -y python3-pip libglib2.0-dev
sudo pip3 install bluepy

# Install psutil library
echo "Installing psutil library..."
sudo pip3 install psutil

# Done
echo "All libraries installed successfully!"

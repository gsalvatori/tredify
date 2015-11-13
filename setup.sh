#!/bin/bash

echo Installing matplotlib...
sudo apt-get install python-matplotlib
echo Installing numpy...
sudo apt-get install python-numpy
echo Done.
echo "Check if pip is installed..."
echo "deb http://archive.ubuntu.com/ubuntu/ vivid universe" | sudo tee -a "/etc/apt/sources.list"
sudo apt-get install python-pip
echo "Installing geojson python module for GIS support..."
sudo pip install geojson


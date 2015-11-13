#!/bin/bash

echo Installing matplotlib...
sudo apt-get install python-matplotlib
echo Installing numpy...
sudo apt-get install python-numpy
echo Done.
echo Installing python-pip...
echo "deb http://archive.ubuntu.com/ubuntu/ vivid universe" | sudo tee -a "/etc/apt/sources.list"
sudo apt-get install python-pip
echo Installing python Basemap toolkit...








echo "Installing geojson python module for GIS support..."
sudo pip install geojson


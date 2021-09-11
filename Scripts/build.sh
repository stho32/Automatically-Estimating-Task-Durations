#!/bin/bash

# This is the build script for the project. It creates graphs and measurements from 
# the 2 datasets that I have available at the moment freshly everytime I run it.
# It helps to standardize all the images and other calculations. And helps with the
# division between the data that I am allowed to share and the rest.
# It is not necessary to create the pdf from the files contained within this repository.
# So if you are just looking to create the pdf or change some text you can do that
# without executing this.

# create a new fresh folder for the results
rm -rf output/
mkdir output

# execute measurements
./A001-execute.ps1


# analyse and build review + graphs

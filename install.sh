#!/usr/bin/bash

set -e

if [! -f ./setup.py ]; then
    echo ">> Cloning repo..."
    git clone https://github.com/RealOrangeOne/yoga-pal.git
    cd yoga-pal
fi

echo ">> Building Virtualenv..."
pyvenv env

echo ">> Building Application..."
env/bin/python3 setup.py develop

echo ">> Installing Application..."
sudo pip install -e .

echo ">> Installation Complete!"

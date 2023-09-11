#!/usr/bin/env bash

dest="../tmp"

# Load all files in target
mkdir $dest
cp -r * $dest
chmod +x $dest/_init.sh

# Run
cd $dest || exit 1
chmod +x _init.sh
./_init.sh
mv $dest/* ..

# Clean
cd ../.template || exit 2
rm -rf $dest
rm ../init.sh
rm ../_init.sh
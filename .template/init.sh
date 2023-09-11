#!/usr/bin/env bash

dest="../tmp"

# Load all files in target
mkdir $dest
cp -r * $dest
chmod +x $dest/_init.sh

# Run
#$dest/_init.sh
#mv $dest/* ..
#
## Clean
#rm -rf $dest
#rm ../init.sh
#rm ../_init.sh

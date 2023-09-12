#!/usr/bin/env bash

cd ../content/ || exit 1
git checkout .
git clean -f -d
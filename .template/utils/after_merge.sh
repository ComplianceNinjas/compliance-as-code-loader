#!/usr/bin/env bash

if [ -z "$PYTHONPATH" ]; then
    echo "It seems you forgot to call 'source .pyenv.sh'..."
    exit 1
fi

if [ ! -d build/CMakeFiles ]; then
  (cd build && cmake ..)
fi

./utils/rule_dir_json.py

for product_path in `find products -maxdepth 1 -mmin -5 | tail -n +2 | xargs` ; do
  for profile_file in `ls $product_path/profiles/` ; do
    profile=$(basename $profile_file .profile)
    product=$(basename $product_path)
    ./utils/autoprodtyper.py $product $profile
    ./utils/autoreftyper.py $product safran $profile
  done
done
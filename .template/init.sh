#!/usr/bin/env bash

declare -A patterns
patterns=(
    ["##PRODUCT_NAME##"]="parrot"
    ["##PRODUCT_NAME_FULL##"]="Parrot Linux"
    ["##BENCHMARK_ID##"]="PARROT"
    ["##PRODUCT_VERSION##"]="5.3"
    ["##PRODUCT_NAME_FULL_VERSION##"]="Parrot Linux 5.3"
)

# Replace patterns with their value
for pattern in "${!patterns[@]}"; do
  new_value="${patterns[$pattern]}"
  find . -type f -not -name "$(basename "$0")" \
       -exec sed -i "s,$pattern,$new_value,g" {} +
done

# Replace "newproduct" in filenames with the value of ##PRODUCT_NAME##
find . -depth -name "*newproduct*" \
  -execdir bash -c 'mv "$1" "$(echo "$1" | sed s/newproduct/'"${patterns["##PRODUCT_NAME##"]}"'/g)"' _ {} \;
#!/usr/bin/env bash

extract_json_value() {
    local json_file="../config.json"
    local key="$1"
    grep -Po "\"$key\":\s*\"\K[^\"]*" $json_file
}

declare -A patterns
patterns=(
    ["##PRODUCT_NAME##"]="$(extract_json_value "PRODUCT_NAME")"
    ["##PRODUCT_NAME_FULL##"]="$(extract_json_value "PRODUCT_NAME_FULL")"
    ["##BENCHMARK_ID##"]="$(extract_json_value "BENCHMARK_ID")"
    ["##PRODUCT_VERSION##"]="$(extract_json_value "PRODUCT_VERSION")"
    ["##PRODUCT_NAME_FULL_VERSION##"]="$(extract_json_value "PRODUCT_NAME_FULL_VERSION")"
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
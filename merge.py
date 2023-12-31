"""
Add a product to ComplianceAsCode
Merge changes.
"""
import fileinput
import os
import re
import shutil
import json

with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)

product_name = config_data["PRODUCT_NAME"]
product_name_upper = product_name.upper()
product_name_full = config_data["PRODUCT_NAME_FULL"]
benchmark_id = config_data["BENCHMARK_ID"]
product_version = config_data["PRODUCT_VERSION"]
platform_name_pretty = config_data["PLATFORM_NAME"]
platform_name = platform_name_pretty.lower()
package_manager = config_data.get("NEW_PACKAGE_MANAGER", "")
has_new_package_manager = package_manager != ""

# Editing CMakeLists.txt
for line in fileinput.input('../content/CMakeLists.txt', inplace=True):
    if re.match(r'option\(SSG_PRODUCT_FEDORA ', line.strip()):
        print(f'option(SSG_PRODUCT_{product_name_upper} "If enabled, the {product_name_full} SCAP content will be '
              f'built" ${{SSG_PRODUCT_DEFAULT}})')
    if re.match(r'message\(STATUS "Fedora', line.strip()):
        print(f'message(STATUS "{product_name_full}: ${{SSG_PRODUCT_{product_name_upper}}}")')
    if re.match(r'if\(SSG_PRODUCT_FEDORA\)', line.strip()):
        print(f'''if(SSG_PRODUCT_{product_name_upper})
    add_subdirectory("products/{product_name}" "{product_name}")
endif()''')

    print(line, end='')

# Editing profile_base.py
for line in fileinput.input('../content/ssg/entities/profile_base.py', inplace=True):
    print(line, end='')
    if re.match(r'msg = "Profile {0} ', line.strip()):
        print(f'            msg += "\\nDid you call \'./utils/after_merge.sh\'?\\nOr is your prodtype incorrect '
              f'for one of your rules?"')

# Editing constants.py
for line in fileinput.input('../content/ssg/constants.py', inplace=True):
    if re.match(r'\s*MULTI_PLATFORM_LIST\s*=', line):
        line = re.sub(r'\[', f'["{platform_name}", ', line)
    print(line, end='')
    if re.match(r'product_directories = \[', line.strip()):
        print(f"    '{product_name}',")
    if re.match(r'MULTI_PLATFORM_MAPPING = {', line.strip()):
        print(f'    "multi_platform_{platform_name}": ["{product_name}"],')
    if re.match(r'FULL_NAME_TO_PRODUCT_MAPPING = {', line.strip()):
        print(f'    "{product_name_full}": "{product_name}",')
    if re.match(r'MAKEFILE_ID_TO_PRODUCT_MAP = {', line.strip()):
        print(f"    '{platform_name}': '{platform_name_pretty}',")
    if has_new_package_manager and re.match(r'PKG_MANAGER_TO_SYSTEM = {', line.strip()):
        print(f"    '{package_manager[0]}': '{package_manager[1]}',")

# Editing build_product
for line in fileinput.input('../content/build_product', inplace=True):
    print(line, end='')
    if re.match(r'all_cmake_products=\(', line.strip()):
        print(f"  {product_name_upper}")

# Merge directory
current_script_filename = os.path.basename(__file__)
def merge_directories(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination_dir, filename)

        if filename == '.git':
            continue

        if filename == '.template':
            continue

        if filename == 'README.md' or filename == "LICENSE":
            continue

        if filename == 'config.json':
            continue

        if filename == current_script_filename:
            continue

        if os.path.isdir(source_file):
            merge_directories(source_file, destination_file)
        else:
            shutil.copy2(source_file, destination_file)


source_dir = os.path.dirname(os.path.abspath(__file__))
destination_dir = "../content"
merge_directories(source_dir, destination_dir)

"""
Add a product to ComplianceAsCode
Merge changes.
"""
import fileinput
import os
import re
import shutil

# Editing CMakeLists.txt
for line in fileinput.input('../content/CMakeLists.txt', inplace=True):
    if re.match(r'option\(SSG_PRODUCT_FEDORA ', line.strip()):
        print('option(SSG_PRODUCT_PARROT "If enabled, the PARROT SCAP content will be built" ${SSG_PRODUCT_DEFAULT})')
    if re.match(r'message\(STATUS "Fedora', line.strip()):
        print('message(STATUS "Parrot Linux: ${SSG_PRODUCT_PARROT}")')
    if re.match(r'if\(SSG_PRODUCT_FEDORA\)', line.strip()):
        print('''if(SSG_PRODUCT_PARROT)
    add_subdirectory("products/parrot" "parrot")
endif()''')

    print(line, end='')


# Editing constants.py
for line in fileinput.input('../content/ssg/constants.py', inplace=True):
    if re.match(r'\s*MULTI_PLATFORM_LIST\s*=', line):
        line = re.sub(r'\[', f'["parrot", ', line)
    print(line, end='')
    if re.match(r'product_directories = \[', line.strip()):
        print("    'parrot',")
    if re.match(r'FULL_NAME_TO_PRODUCT_MAPPING = {', line.strip()):
        print('    "Parrot Linux": "parrot",')
    if re.match(r'MULTI_PLATFORM_MAPPING = {', line.strip()):
        print('    "multi_platform_parrot": ["parrot"],')
    if re.match(r'MAKEFILE_ID_TO_PRODUCT_MAP = {', line.strip()):
        print("    'parrot': 'Parrot Linux',")

# Editing build_product
for line in fileinput.input('../content/build_product', inplace=True):
    print(line, end='')
    if re.match(r'all_cmake_products=\(', line.strip()):
        print("  PARROT")

# Editing sysctl_kernel_ipv6_disable.xml
for line in fileinput.input('../content/shared/checks/oval/sysctl_kernel_ipv6_disable.xml', inplace=True):
    if re.match(r'<platform>multi_platform_fedora</platform>', line.strip()):
        print("	<platform>multi_platform_parrot</platform>")
    print(line, end='')

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

        if filename == 'README.md':
            continue

        if filename == '.template':
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

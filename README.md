# ComplianceAsCode Loader

ComplianceAsCode Loader is a project designed to simplify the integration of custom compliance controls and products into [Compliance as Code](https://github.com/ComplianceAsCode/content) (CaC). It provides a straightforward process for initializing your project, making changes, and seamlessly merging those changes into the CaC project.

> A tool to seamlessly integrate your custom compliance controls into Compliance as Code (CaC) projects.

## Installation

To initialize the project with a new product, follow these steps:

1. Open the `config.json` file.
2. Replace the placeholder values with your product-specific information:

```json
{
    "PLATFORM_NAME": "The platform, such as 'Debian'",
    "PRODUCT_NAME": "The specific product, such as 'Debian 10'",
    "PRODUCT_NAME_FULL": "The full product name, for example, 'Debian Linux 10'",
    "BENCHMARK_ID": "An identifier, like 'DEBIAN-10'",
    "PRODUCT_VERSION": "The version number, e.g., '10'",
    "PRODUCT_OS_FILE": "The file to be checked, such as '/etc/debian_version'",
    "PRODUCT_OS_FILE_CONTENT": "The expected version pattern, which should match the installed version, for example, '^10\\.[0-9]+$'",
    // Only add the following line if your package manager is not already supported,
    // and be sure to update all necessary files accordingly.
    "NEW_PACKAGE_MANAGER": ["apt_get", "dpkg"]
}
```

3. Save the file.

Before you can use this tool, you need to make sure you have Python installed on your system. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/).

## Initialization

To initialize the current folder and set up a default product, follow these steps:

1. Open your terminal
2. Run the following command to initialize the folder with a configured product:

```bash
cd .template
chmod +x init.sh
./init.sh
```

This command will create the necessary files and folder structure for the configured product in the current directory.

## Usage

Assuming [ComplianceAsCode/content](https://github.com/ComplianceAsCode/content) is located in "../content," follow these steps to merge your changes into it:

1. Open a terminal or command prompt. 
2. If you see any uncommitted changes or files listed as modified in "../content", it's essential to either commit or discard these changes. To discard changes, use the following command:

```bash
./clean.sh
```

3. Run the "merge.py" Python script

```bash
python3 merge.py
```
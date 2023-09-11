# ComplianceAsCode Loader

ComplianceAsCode Loader is a project designed to simplify the integration of custom compliance controls and products into [Compliance as Code](https://github.com/ComplianceAsCode/content) (CaC). It provides a straightforward process for initializing your project, making changes, and seamlessly merging those changes into the CaC project.

> A tool to seamlessly integrate your custom compliance controls into Compliance as Code (CaC) projects.

## Installation

To initialize the project with a new product, follow these steps:

1. Open the `config.json` file.
2. Replace the placeholder values with your product-specific information:

```bash!
{
    "PRODUCT_NAME": "parrot",
    "PRODUCT_NAME_FULL": "Parrot Linux",
    "BENCHMARK_ID": "PARROT",
    "PRODUCT_VERSION": "5.3",
    "PRODUCT_NAME_FULL_VERSION": "Parrot Linux 5.3"
}
```

3. Save the file.

Before you can use this tool, you need to make sure you have Python installed on your system. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/).

## Initialization

To initialize the current folder and set up a default product, follow these steps:

1. Open your terminal
2. Run the following command to initialize the folder with a default product:

```bash
$ chmod +x ./template/init.sh
$ ./template/init.sh
```

This command will create the necessary files and folder structure for the default product in the current directory.

## Usage

Assuming [ComplianceAsCode/content](https://github.com/ComplianceAsCode/content) is located in "../content," follow these steps to merge your changes into it:

1. Open a terminal or command prompt. 
2. Navigate to the directory "../content".
3. If you see any uncommitted changes or files listed as modified, it's essential to either commit or discard these changes. To discard changes, use the following command:

```bash!
$ git checkout .
$ git clean -f -d
```

4. Run the "merge.py" Python script

```bash!
$ python merge.py
```
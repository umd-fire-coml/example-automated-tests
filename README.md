# Python Automated Testing Example

This package contains the following files:

```bash
├── src
│   ├── conftest.py
│   ├── hello.py
│   ├── goodbye.py
├── test
│   ├── test_sanity.py
│   ├── test_hello.py
│   ├── test_goodbye.py
├── .github
│   ├── .workflows
│       ├── main.yaml
├── requirements.txt
├── requirements-test.txt
└── .gitignore
```

## Source Directory

The src directory contains all the source code files for your project. In this example, there are two files - hello.py which contains the Hello class and goodbye.py which contains the Goodbye class. The conftest.py is an empty file that is created to allow pytest to find classes inside the src directory.

## Test Directory

The test directory contains all the unit tests for our source code files (test_hello.py, test_goodbye.py) as well as a test_sanity.py that just makes sure our tests work as expected. 

## .github Directory

The .github/workflows directory contains the different workflows that we want to run using GitHub Actions. The main.yaml file runs all of our tests as separate jobs any time we push, create a pull request, or manually run on GitHub.

## Requirements

The requirements.txt file and requirements-test.txt file contain the required packages for the code and tests respectively.

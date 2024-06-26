# Project File Copier

## Overview

Project File Copier is a Python-based command-line tool designed to aggregate the contents of all text files within a project structure into a single output file. This tool is particularly useful for preparing project contents for analysis by Large Language Models (LLMs) or for creating comprehensive project documentation.

## Features

- Recursively traverses project directories
- Copies content from text files into a single output file
- Ignores specified folders and files
- Concurrent processing for improved performance
- Logging support for better tracking and debugging
- MIME type checking to avoid issues with binary files
- Customizable logging levels and output

## Installation

1. Ensure you have Python 3.6 or higher installed on your system.
2. Clone this repository:
    git clone https://github.com/yourusername/project-file-copier.git
    cd project-file-copier
3. (Optional) Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
4. Install the required dependencies:
    pip install -r requirements.txt

## Usage

Run the script from the command line with the following syntax:
    python file_copier.py <root_dir> <output_file> [options]

### Arguments:

- `root_dir`: The root directory of the project structure to process
- `output_file`: The name of the output text file to store the aggregated contents

### Options:

- `--ignore-folders`: Space-separated list of folder names to ignore
- `--ignore-files`: Space-separated list of file names to ignore
- `--log-file`: Name of the log file (default: file_copier.log)
- `--log-level`: Logging level (choices: DEBUG, INFO, WARNING, ERROR, CRITICAL; default: INFO)
- `--max-workers`: Maximum number of worker threads for concurrent processing

### Example:
python file_copier.py /path/to/project output.txt --ignore-folders .git node_modules --ignore-files .gitignore README.md --log-file my_log.log --log-level DEBUG --max-workers 4

## Running Tests

To run the unit tests, execute the following command from the project root:
python -m unittest test_file_copier.py

## Contributing

Contributions to the Project File Copier are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Commit your changes
4. Push to your fork and submit a pull request

Please ensure your code adheres to the existing style and passes all tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions, issues, or suggestions, please open an issue on the GitHub repository or contact the maintainer at your.email@example.com.
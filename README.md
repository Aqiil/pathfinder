# Directory Traversal Tool

This script is a directory traversal tool designed to efficiently visualize complex file systems.

## Features
- Custom Directory Traversal: Traverse any specified directory, with the default being the current directory.
- Exclude Specific Folders and Files: Users can define folders and files that should be excluded from the traversal.
- Hide Hidden Files and Folders: An option to exclude hidden files and folders from the output.
- Intuitive Display: Presents the directory structure in an easy-to-read, tree-like format.

## Requirements
- Python 3.x

## Installation
1. Clone the repository

```bash
git clone https://github.com/Aqiil/pathfinder.git
```

2. Navigate to the project directory

```bash
cd pathfinder
```

## Usage
Run the script using Python from the command line. You can specify the directory to traverse and additional flags to customize the output.

### Basic Command
```bash
$ python pathfinder.py -h
usage: pathfinder.py [-x] [-h] [directory]

Directory traversal tool

positional arguments:
  directory             Directory path to traverse (default: current directory)

options:
  -x, --exclude-hidden  Exclude hidden folders/files from traversal
  -h, --help            Show this help message and exit.
```

### Example
```bash
python pathfinder.py "/path/to/directory" -x
```

## Contributing
Contributions, issues, and feature requests are welcome.

## License

This project is licensed under the [MIT License](./LICENSE).

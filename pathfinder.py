import os
import sys
import argparse

# List of folders to exclude
EXCLUDE_FOLDERS = ["__pycache__", "env"]

# List of files to exclude
EXCLUDE_FILES = ["__init__.py"]


def traverse_directory(path, exclude_hidden=False, exclude_folders=None, exclude_files=None, prefix=''):
    # Set default values for exclude_folders and exclude_files
    if exclude_folders is None:
        exclude_folders = []

    if exclude_files is None:
        exclude_files = []

    all_items = os.listdir(path)

    # Filter out excluded folders and files but include hidden files unless they are in the exclude list
    items = [item for item in all_items if item not in exclude_folders and item not in exclude_files
             and (not exclude_hidden or not os.path.isdir(os.path.join(path, item)) or not item.startswith("."))]
    num_items = len(items)

    for index, item in enumerate(items):
        item_path = os.path.join(path, item)

        # Set connector and new_prefix based on whether the item is the last item in the directory
        is_last_item = index == num_items - 1
        connector = "└── " if is_last_item else "├── "
        new_prefix = prefix + ("    " if is_last_item else "│   ")

        print(prefix + connector + item)

        # Traverse into sub-directory only if it's not a hidden directory (when exclude_hidden is True)
        if os.path.isdir(item_path) and not (exclude_hidden and item.startswith(".")):
            traverse_directory(item_path, exclude_hidden, exclude_folders, exclude_files, new_prefix)


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        add_help=False, description="Directory traversal tool")

    parser.add_argument("directory", nargs="?", default=os.getcwd(),
                        help="Directory path to traverse (default: current directory)")

    parser.add_argument("-x", "--exclude-hidden", action="store_true",
                        help="Exclude hidden folders from traversal")

    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help='Show this help message and exit.')

    args = parser.parse_args()

    try:
        # Check directory exists
        if not os.path.exists(args.directory):
            raise FileNotFoundError(f"Directory not found: {args.directory}")

        # Integrate EXCLUDE_FOLDERS and EXCLUDE_FILES into the traverse_directory function
        traverse_directory(args.directory, args.exclude_hidden, EXCLUDE_FOLDERS, EXCLUDE_FILES)
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)

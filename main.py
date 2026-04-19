import secrets

from pathlib import Path


def print_tree(directory, prefix="", level=-1):
    path = Path(directory)
    # Sort to show directories before files
    items = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    
    for i, item in enumerate(items):
        if item.name == "__pycache__":
            continue
        
        is_last = (i == len(items) - 1)
        connector = "└── " if is_last else "├── "
        
        print(f"{prefix}{connector}{item.name}")
        
        if level != 0 and item.is_dir():
            # Adjust prefix for nested levels
            extension = "    " if is_last else "│   "
            level = level if level == -1 else level - 1
            print_tree(item, prefix + extension, level)


def print_token():
    print(secrets.token_hex(32))

def main():
    print_tree(".", level=2)
    print_token()


if __name__ == "__main__":
    main()

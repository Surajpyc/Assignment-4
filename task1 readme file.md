
# File Reader with Exception Handling

This Python script attempts to read the contents of a text file named `sample.txt`. It demonstrates basic file operations and exception handling using `try` and `except`.

## Features

- Opens a file in read mode.
- Reads and prints the content.
- Handles the case where the file does not exist.

## Python Code

```python
try:
    file = open("sample.txt", "r")
    read = file.read()
    print("Reading file content:\n\n", read)
    file.close()
except FileNotFoundError:
    print("Error: the file sample.txt does not exist")
```

## How to Use

1. Make sure a file named `sample.txt` is present in the same directory as the script.
2. Run the script using Python 3:
   ```bash
   python filename.py
   ```
3. If the file exists, its contents will be printed.
4. If the file does not exist, an error message will be displayed.

## Requirements

- Python 3.x

## Author

Suraj Gupta


# Interactive File Writer and Reader

This Python script allows the user to write input into a file named `output.txt` and read its content. It repeats the process based on user preference.

## Features

- Reads and displays the current content of `output.txt`.
- Prompts the user to enter new content.
- Writes the new content to the file.
- Displays the updated content.
- Asks the user if they wish to continue writing to the file.

## Python Code

```python
def main():
    # First showing the text file is empty
    file = open("output.txt", "r+")
    read = file.read()
    print(read)
    file.close()

    # Writing the text file with user filled input
    user_input = input("enter: ")
    file1 = open("output.txt", "r+")
    write = file1.write(user_input)
    print(write)
    file1.close()

    file2 = open("output.txt", "r+")
    read1 = file2.read()
    print(read1)
    file2.close()

    repeat = input("do you want to write again in the output file [yes/no]?").lower()
    if repeat == "yes":
        main()
    else:
        exit("You do not want to write more in the file")

main()
```

## How to Use

1. Make sure `output.txt` exists in the same directory as this script. If not, create it manually.
2. Run the script using Python 3:
   ```bash
   python filename.py
   ```
3. Follow the prompt to enter content and choose whether to continue writing.

## Requirements

- Python 3.x

## Notes

- Content is overwritten when `file.write()` is used in `"r+"` mode. Use `"a"` for appending instead.

## Author

Suraj Gupta

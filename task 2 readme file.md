# File Input and Output with Repetition

This Python script allows users to read from and write to a text file named `output.txt`. It gives an interactive way for users to repeatedly update the file content.

## 📄 Description

- Initially reads and displays the content of `output.txt`.
- Prompts the user to enter new content.
- Overwrites the file with user input.
- Displays the updated content.
- Asks the user whether they want to write again.
- If the user types `yes`, the process repeats; otherwise, the program exits.

## 🧾 Code

```python
def main():
    # first showing the text file is empty
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

## ✅ Usage

1. Ensure `output.txt` exists in the same directory.
2. Run the script:
   ```bash
   python your_script_name.py
   ```
3. Follow on-screen prompts to add new content.

## 💡 Tips

- Using `r+` mode allows both reading and writing.
- Consider using `with open(...)` for safer file handling.
- Recursion is used for repeating the function; this is fine for small loops but can be replaced with a `while` loop for better performance and readability in production.


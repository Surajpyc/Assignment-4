# File Reader with Error Handling

This Python script demonstrates how to safely read the contents of a file using error handling to manage missing files.

## 📄 Description

The script attempts to read a file named `sample.txt`. If the file does not exist, it will catch the `FileNotFoundError` and display a user-friendly error message instead of crashing.

## 🧾 Code

```python
try:
    file = open("sample.txt", "r")
    read = file.read()
    print("Reading file content:\n\n", read)
    file.close()
except FileNotFoundError:
    print("Error the file sample.txt does not exist")
```

## ✅ Usage

1. Create a file named `sample.txt` in the same directory as this script, or leave it missing to test the error handling.
2. Run the script using:
   ```bash
   python your_script.py
   ```

3. Observe the output based on whether the file exists or not.

## 💡 Notes

- Always close files after opening to free system resources.
- You can use `with open(...) as file:` for cleaner syntax that automatically closes the file.

try:
    file=open("sample.txt","r")
    read=file.read()
    print("Reading file content:\n\n",read)
    file.close()
except FileNotFoundError:
    print("Error the file sample.txt does not exist")
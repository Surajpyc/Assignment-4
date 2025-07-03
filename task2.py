def main():
    #first showing the text file is empty
    file=open("output.txt","r+")
    read=file.read()
    print(read)
    file.close()

    #Writing the text file with user filled input
    user_input=input("enter: ")
    file1=open("output.txt","r+")
    write=file1.write(user_input)
    print(write)
    file1.close()

    file2=open("output.txt","r+")
    read1=file2.read()
    print(read1)
    file2.close()
    repeat=input("do you want to write again in the output file [yes/no]?").lower()
    if repeat=="yes":
        main()
    else:
        exit("You do not want to write more in the file")

main()
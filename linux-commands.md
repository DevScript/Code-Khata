<!-- This Tutorial is contributed by Gaurav Shukla(withgaurav) -->
# What is Linux?
### Linux is an open-source operating system (OS). An operating system is software that directly manages a system’s hardware and resources, like CPU, memory, and storage. Linux commands help us to go to any file or folder directly by writing code.

## List of all the commands

<summary>ls - This command helps us to list all the files/folders in the current directory. You can use the command given below

        ls

</summary>

<summary>cd - It is used to change the current working directory. You can use the command given below

        cd folder2

- If you want to go back to the parent directory of the current directory you can use the following command

        cd ..

</summary>

<summary>pwd - This command prints the Present Working Directory.


        pwd

</summary>        
<summary>cat - It is used to read the data from a file and gives its content as output. It also helps us to create, view, and concatenate(join) files.

Create a file command:


        cat > file1

To view a single file command:

        cat file1
To view multiple files

        cat file1 file2

Copy the content from one file to another file


        cat file1>file2
Append the contents of one file to the end of another file

        cat file1>>file2
</summary>

<summary>man - This is the command which will help you to know about the particular command. This command gives you detailed information about every command. For example, if you want to know about the command "echo" you can simply type


        man echo

</summary>

<summary>mkdir - make directory! This command helps us to create folders wherever we want to create a folder. For example, if you want to create a folder/directory named "hello" type the command given below. Your folder will be created successfully in the current directory in which you are.


        mkdir hello


- This command will help you to create a folder inside the current folder. For example, if you want to create a new file inside the test folder then you can use this command:-


        mkdir test/hello

- This command will create a file inside the hello file. When you go inside the second file there will be a new file which is named hello. But your hello folder which you have made in the previous command will remain as same as it was.


        mkdir -p test/second/hello
</summary>

<summary>cp - this command will help you to create a replica(copy) of any file. So the source file will be copied as same as the destination file.



        cp sourcefile destinationfile

</summary>

<summary>mv - from the name itself you can understand that this command will help you to move the file to another folder or file. 

- It is also used to rename a file or folder.

- rename the file - if you want to rename any file or directory you can just simply use the command, for example, if my file name is linux and I want to rename it I can write the command as


        mv linux set
        
- dot(.) represents the current directory if we want to move a file named "file1" to the current directory named "folder1" then we write the path of that file followed by a dot (.)


        mv filepath/file1 .
</summary>
<summary>Delete

- Deleting a file - This command is used for deleting a file command:


rm filename

- Deleting a directory- To remove an empty directory(folder), use either 'rmdir' or 'rm -d' followed by the directory name:


        rm -d foldername rmdir foldername

- To remove non-empty directories


        rm -r foldername

</summary>
<summary>df - This command displays the free disk space. As you can see in the image below it is showing in the Linux folder the amount of storage available and used.</summary>



<summary>head - It shows the first few text of the file. For example, if you have created a text file and you want to see some lines of that text file then you can type 'head file.txt'

tail - It shows the few lines from behind 'tail file.txt'

</summary>

<summary>diff - It compares files line by line. It will compare both files and list out all the files which are not there in both files.



        diff file.txt hello.txt
</summary>

<summary>find - This will help you to find the files which are there in the current directory for example you can use the command "find . -type f mtime -10" This command will help you to know all the files which have been created or modified in the particular directory within 10 days.</summary>


<summary>File permissions - There are three types of permission:- Read Write & Execute. You can change the permission by using the command


        chmod u =rwx,g=rx,o=r upper.txt

:>u - users, g - groups o - others

:>r - read, w - write x - execute

:> 4 stands for read, 2 stands for write 1 stands for execute & 0 stands for no permission. if you write a command in gitbash terminal:- chmod 777 upper.txt then you will get output as -rwxrwxrwx which means that users and groups&others all have permission to read, write and execute your file. Now the question that comes to your mind is how this 777 is coming this is 4+2+1 = 7. Users, groups and others have all the permissions to read, write and execute.
</summary>

</summary>Grep - global regular expression print. It allows searching for things written in the file. This is also case-sensitive. If you want to search for a particular word in your text file which you have saved earlier say for example if you have saved 'amazon' in your 'name.txt' you can use the command

- If you want to know the full name for example if you have saved "Amazon cart" in your text file then you can use this command


        grep -w "Amazon" name.txt

- If you wanna know the line number of any name Amazon then you type the command


        grep -n "Amazon" name.txt

- As I mentioned above grep is case sensitive and if you write the command 'grep -w "amazon" name.txt' then it will not give you the output. Instead of that, you can use the command


        grep -i "amazon" name.txt

- You can combine all three tags by using the command


        grep -win "amazon" name.txt
- You can count which all file matches these names by using the command


        grep -wirl "amazon" .
- You can count how many files there which contain 'amazon" by using the command


        grep -wirc "amazon" .
</summary>

<summary>History:- This command is used to view all the previously executed commands.


        history | grep "ls -l"
</summary>
<summary>Terminal Shortcuts
        
Suppose you write the code 'git push origin main' and from the code, you want to move to the beginning at the very first of your code then you can press "ctrl + a" on your keyboard. If you wanna move to the end then you can press 'ctrl + e' then you can move to the very end of your code. You can remove all the code written there by 'ctrl + u'. You can type 'history' in your terminal all the commands which you have run before will be shown as your output. If you want to run any command again then you can type '!189' Then your command will run again.

You can use multiple commands in the same line for example
        
   * git add . ; git commit -m "message"; git push they will be running successfully

   * sort -r:- This command is used to display the file in reverse order.
        
   * sort -n:- This command is used to display the file in numerical order.
        
   * ping:- this command is used to connect us to the server and grab all the information related to it

</summary>

<summary>
        
Benefits
        
   * It is free to use and lightweight.

   * It is open-source, and source codes are easily available.

   * The requirements for running Linux are much less than other operating systems.

   * Its security is most appreciated so it is used by many developers.

   * It provides high performance and is very flexible.</summary>



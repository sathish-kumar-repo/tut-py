# File Handling in Python

File handling is an important part of any web application. Python has several functions for creating, reading, updating, and deleting files.

## File handling is an important part of any web application. Python has several functions for creating, reading, updating, and deleting files.

### Binary file ( written in binary language, 0s, and 1s )

All binary files follow a specific format. We can open some binary files in the normal text editor but we can't read the content present inside the file.

### Text file

A text file exists stored as data within a computer file system. Text files don’t have any specific encoding and it can be opened in normal text editor itself.

## How to File Open

The key function for working with files in Python is the open() function. This function takes two parameters; filename, and mode.

### Syntax :

```python
file_object = open ( file_name , mode )
```

- file_name is a string that represents the name of the file you want to open
- mode is a string that represents how you want to open the file.

### Some Common Modes

- 'r': read-only mode (default)
- 'w': write mode (overwrites existing file or creates a new one)
- 'a': append mode (appends to an existing file or creates a new one)
- 'x': exclusive creation mode (creates a new file, fails if the file already exists)

> Once the file is opened, you can perform various operations on it, such as reading or writing to it. It is important to close the file once you are done with it, using the close() method.

## Delete a File in Python

Removing the files or a single file from a particular directory when it is no longer required is the basic concept of deleting a file. To delete a file, you must import the module os, then use the remove() function provided by the module to delete the file. It takes the file location as a parameter.

### Syntax :

```python
 os.remove ( file_location )
```

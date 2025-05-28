# Try Block

In Python, the try block is used to enclose code that might raise an exception. If an exception is raised within the try block, the code in the corresponding except block is executed. This allows you to handle errors and exceptions in a controlled way, rather than letting the program crash.

In Python, the try block is used to enclose code that might raise an exception. If an exception is raised within the try block, the code in the corresponding except block is executed. This allows you to handle errors and exceptions in a controlled way, rather than letting the program crash.

> Note: There are two types of errors
> 1.Run time error
> eg. 10/0
> 2.Compile Time Error
> eg. missing comma, quotation, bracket,..

## Syntax

```python
try:
    # code that might raise an exception
except ExceptionType1:
    # code to handle ExceptionType1
except ExceptionType2:
    # code to handle ExceptionType2
except:
    # code to handle any other exception
else:
    # code to run if no exception was raised
finally:
    # code that will always be executed, regardless of whether an exception was raised or not

```

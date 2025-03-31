# Q1. What is the purpose of the try block in Python error handling?

# a) To define the block of code where an exception may occur

# b) To catch and handle exceptions that occur within the block

# c) To ensure that the code executes without any errors

# d) To terminate the program if an exception occurs

# Answer: a

# Explanation: The try block defines a block of code in which exceptions may occur.

# Q2. Which keyword is used to handle exceptions in Python?

# a) try

# b) catch

# c) except

# d) handle

# Answer: c

# Explanation: The except keyword is used in Python to handle exceptions.

# Q3. What will happen if an exception is raised inside the try block and there is no corresponding except block to handle it?

# a) The program will terminate

# b) The exception will be ignored

# c) The program will enter an infinite loop

# d) The program will continue executing the code after the try-except block

# Answer: a

# Explanation: If an exception is raised inside a try block and there is no corresponding except block to handle it, the program will terminate.

# Q4. Which of the following statements about exceptions in Python is true?

# a) All exceptions are errors

# b) Exceptions can only be handled with try-except blocks

# c) Exceptions can be raised explicitly using the raise keyword

# d) Exceptions can only occur in the main block of code

# Answer: c

# Explanation: Exceptions can be raised explicitly using the raise keyword in Python.

# Q5. What is the purpose of the except block in Python exception handling?

# a) To define the block of code where an exception may occur

# b) To catch and handle exceptions that occur within the try block

# c) To ensure that the code executes without any errors

# d) To terminate the program if an exception occurs

# Answer: a

# Explanation: The except block catches and handles exceptions that occur within the try block.

# Q6. Which of the following is a built-in exception in Python?

# a) StopIteration

# b) ExceptionalError

# c) BreakException

# d) ProgramHalt

# Answer: a

# Explanation: StopIteration is a built-in exception in Python used with iterators.

# Q7. What will be the output of the following code?

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Divide by zero error")
except:
    print("Other error")

# a) “Divide by zero error”

# b) “Other error”

# c) Nothing will be printed

# d) Error: division by zero

# Answer: a

# Explanation: The code will output “Divide by zero error” because a ZeroDivisionError exception is raised.

# Q8. What is the purpose of the finally block in Python exception handling?

# a) To define the block of code where an exception may occur

# b) To catch and handle exceptions that occur within the try block

# c) To ensure that the code executes without any errors

# d) To execute cleanup code, whether an exception occurs or not

# Answer: d

# Explanation: The finally block in Python executes cleanup code, whether an exception occurs or not.

# Q9. What is the output of the following code?

try:
    raise NameError("Custom error")
except NameError as e:
    print(e)

# a) “Custom error”

# b) “NameError: Custom error”

# c) “Error: Custom error”

# d) NameError: Custom error

# Answer: a

# Explanation: The code will output “Custom error” because a NameError with the specified message is raised and caught.

# Q10. Which of the following is NOT a standard Python exception type?

# a) ValueError

# b) KeyError

# c) TypeMismatchError

# d) IndexError

# Answer: c

# Explanation: TypeMismatchError is not a standard Python exception type.

# Q11. What does the following code snippet do?

try:
    x = int("abc")
except ValueError:
    print("Invalid literal for int()")
finally:
    print("Finally block executed")

# a) Attempts to convert a string to an integer and prints an error message if it fails

# b) Prints “Finally block executed” regardless of the outcome

# c) Raises a ValueError exception

# d) Terminates the program

# Answer: b

# Explanation: The finally block is always executed, regardless of whether an exception is raised or caught.

# Q12. What will be the output of the following code?

try:
    raise IndexError("Index out of range")
except ValueError:
    print("ValueError")
except IndexError:
    print("IndexError")
except Exception:
    print("Exception")

# a) “ValueError”

# b) “IndexError”

# c) “Exception”

# d) “Index out of range”

# Answer: b

# Explanation: The code will output “IndexError” because an IndexError exception is raised and caught.

# Q13. What is the purpose of the raise statement in Python?

# a) To handle exceptions

# b) To terminate the program

# c) To define a new exception

# d) To print an error message

# Answer: d

# Explanation: The raise statement is used to explicitly raise exceptions in Python.

# Q14. What will happen if an exception is raised but not caught in a Python program?

# a) The program will continue executing normally

# b) The program will terminate with an error message

# c) The program will pause and wait for user input

# d) The program will enter an infinite loop

# Answer: b

# Explanation: If an exception is raised but not caught, the program will terminate with an error message.

# Q15. Which of the following keywords is used to catch all exceptions in Python?
# a) try

# b) catch

# c) except

# d) finally

# Answer: c

# Explanation: The except keyword is used to catch all exceptions in Python.

# Q16. What is the output of the following code?

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Divide by zero error")
finally:
    print("Finally block executed")

# a) “Divide by zero error”

# b) “Finally block executed”

# c) “Divide by zero error” followed by “Finally block executed”

# d) Nothing will be printed

# Answer: c

# Explanation: The code will output “Divide by zero error” because a ZeroDivisionError exception is raised and caught, followed by “Finally block executed”.

# Q17. What will be the output of the following code?

try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("You entered:", x)

# a) “Invalid input”

# b) “You entered: <number>”

# c) Nothing will be printed

# d) Error: invalid literal for int() with base 10: ‘<input>’

# Answer: b

# Explanation: If the input is successfully converted to an integer, it will print “You entered: <number>”. Otherwise, it will print “Invalid input”.

# Q18. Which of the following is true about the else block in Python exception handling?

# a) The else block is executed if an exception occurs

# b) The else block is always executed after the except block

# c) The else block is executed if no exceptions occur in the try block

# d) The else block is optional in exception handling

# Answer: c

# Explanation: The else block is executed if no exceptions occur in the try block.

# Q19. What does the following code snippet do?

try:
    assert 5 > 10, "AssertionError"
except AssertionError as e:
    print(e)
finally:
    print("Finally block executed")

# a) Raises an AssertionError and prints “AssertionError”, followed by “Finally block executed”

# b) Raises an AssertionError and prints “False”, followed by “Finally block executed”

# c) Raises an AssertionError and prints “5 > 10”, followed by “Finally block executed”

# d) Raises no error and prints “Finally block executed”

# Answer: a

# Explanation: The code will raise an AssertionError due to the failed assertion, and it will print the custom error message “AssertionError”, followed by “Finally block executed”.

# Q20. What is the output of the following code?

try:
    assert 2 + 2 == 5, "AssertionError"
except AssertionError as e:
    print(e)

# a) AssertionError

# b) AssertionError: 2 + 2 == 5

# c) 4

# d) Nothing will be printed

# Answer: a

# Explanation: The code will output “AssertionError” because the assert statement fails.

# Q21. Which of the following is a built-in exception type in Python?

# a) ProgramError

# b) SystemError

# c) ExecutionError

# d) LogicalError

# Answer: b

# Explanation: SystemError is a built-in exception type in Python.

# Q22. What will happen if an exception is raised but not caught within a function?

# a) The function will return None

# b) The function will return the exception object

# c) The program will terminate

# d) The program will enter an infinite loop

# Answer: c

# Explanation: If an exception is raised but not caught within a function, the program will terminate.

# Q23. What is the purpose of the traceback in Python exception handling?

# a) To display the error message

# b) To display the line number where the exception occurred

# c) To print the stack trace of the program

# d) To terminate the program

# Answer: c

# Explanation: The traceback in Python exception handling is used to print the stack trace of the program, showing the line numbers and functions involved.

# Q24. What is the output of the following code?

try:
    raise TypeError("Type error occurred")
except Exception as e:
    print(e.__class__.__name__)

# a) “TypeError”

# b) “Exception”

# c) “Error”

# d) “Python”

# Answer: a

# Explanation: The code will output “TypeError” because a TypeError exception is raised and caught, and e.__class__.__name__ retrieves the name of the exception class.

# Q25. Which of the following is NOT a standard Python exception type?

# a) OverflowError

# b) SyntaxError

# c) RangeError

# d) KeyError

# Answer: a

# Explanation: RangeError is not a standard Python exception type.

# Q26. What does the following code snippet do?

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result:", result)
finally:
    print("End of program")

# a) Asks the user to enter two numbers, divides them, and prints the result

# b) Asks the user to enter two numbers and prints their sum

# c) Prints “Invalid input” if the user enters a non-integer value

# d) Prints “Cannot divide by zero” if the user enters zero as the second number

# Answer: a

# Explanation: The code asks the user to enter two numbers, divides them, and prints the result. It also handles exceptions for invalid input and zero division.

# Q27. What will be the output of the following code?

try:
    x = 5 / 0
except:
    print("An error occurred")
else:
    print("No error")
finally:
    print("Finally block executed")

# a) “An error occurred” followed by “Finally block executed”

# b) “No error” followed by “Finally block executed”

# c) “An error occurred”

# d) “No error”

# Answer: a

# Explanation: The code will output “An error occurred” because a ZeroDivisionError exception is raised, followed by “Finally block executed”.

# Q28. What is the purpose of the assert statement in Python?

# a) To handle exceptions

# b) To terminate the program

# c) To define a new exception

# d) To check for conditions that should be true during program execution

# Answer: d

# Explanation: The assert statement is used to check for conditions that should be true during program execution. If the condition is false, an AssertionError is raised.

# Q29. What will be the output of the following code?

try:
    assert 3 < 2, "AssertionError"
except AssertionError as e:
    print(e)
finally:
    print("Finally block executed")

# a) “AssertionError”

# b) “AssertionError: AssertionError”

# c) “3 < 2”

# d) “Finally block executed”

# Answer: a

# Explanation: The code will output “AssertionError” because the assert statement fails, and the custom error message is printed.
print("If error ocurred then the finally statement is not executed")

# Q30. Which of the following is a valid reason to use custom exceptions in Python?

# a) To replace built-in exceptions

# b) To handle unexpected errors

# c) To confuse the programmer

# d) To reduce code readability

# Answer: 

# Explanation: A valid reason to use custom exceptions in Python is to handle unexpected errors and provide meaningful error messages.

# Q31. What will be the output of the following code?

try:
    x = int("abc")
except ValueError:
    print("Invalid input")
except Exception as e:
    print(e)
else:
    print("No error")
finally:
    print("Finally block executed")

# a) “Invalid input” followed by “Finally block executed”

# b) “invalid literal for int() with base 10: ‘abc'” followed by “Finally block executed”

# c) “No error” followed by “Finally block executed”

# d) “Finally block executed” only

# Answer: b

# Explanation: The code will output “invalid literal for int() with base 10: ‘abc'” because a ValueError occurs when trying to convert “abc” to an integer, followed by “Finally block executed”.

# Q32. What is the output of the following code?

try:
    raise KeyError("Key not found")
except ValueError:
    print("ValueError")
except KeyError as e:
    print(e)

# a) “ValueError”

# b) “KeyError: Key not found”

# c) “Key not found”

# d) Nothing will be printed

# Answer: 

# Explanation: The code will output “KeyError: Key not found” because a KeyError with the specified message is raised and caught.

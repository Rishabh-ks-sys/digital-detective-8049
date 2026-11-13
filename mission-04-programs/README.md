# Mission 4: How Programs Run

## 1. Task / Objective

The objective of this mission was to understand how programs run, execute a simple Python program using Python 3, and learn the difference between compilers and interpreters.

## 2. Work Completed

### Task 4.1: Create and Run a Python Program

Created a Python file named `hello.py` containing:

```python
print("Hello from Python")
```

Executed the program using:

```bash
python3 hello.py
```

**Output:**

```text
Hello from Python
```

This confirmed that the Python program executed successfully.

### Task 4.2: Compiler vs Interpreter

| Point | Compiler | Interpreter |
|---|---|---|
| Translation | Translates the entire source program before execution. | Translates and executes instructions during execution. |
| Execution | Executes the translated program. | Executes the program through the interpreter. |
| Example | C, C++ | Python |
| Advantage | Compiled programs can execute quickly. | Makes testing and interactive debugging easier. |

**Explanation:**

A compiler translates the entire source program before it is executed. An interpreter translates and executes instructions during program execution. Compiled programs can offer faster execution, while interpreted execution can make testing and debugging easier. Both help computers execute programs written by humans.

## 3. Commands / Tools Used

- `python3 hello.py` – Executes the Python program.
- Visual Studio Code – Used to create and edit the Python file.
- macOS Terminal – Used to execute the program.

## 4. My Understanding

Through this mission, I learned how to create and execute a Python program using Python 3. I understood that a compiler translates a complete program before execution, whereas an interpreter executes instructions during program execution.

## 5. Difficulties Faced

- Initially, the Terminal could not locate `hello.py` because it was in a different directory.

## 6. How I Resolved Them

- Navigated into the correct directory using the `cd` command.
- Executed the program again using `python3 hello.py`.

## 7. Evidence / Files

- `mission-04-programs/hello.py`
- `mission-04-programs/README.md`
- Successful Terminal output showing `Hello from Python`.

## 8. Commit Details

**Commit Message:** `Complete Mission 4 programs`

**GitHub Repository:** `digital-detective-8049`

**Branch:** `master`
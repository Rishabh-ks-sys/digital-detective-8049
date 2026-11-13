# Mission 5: Numbers and Data

## 1. Task / Objective

The objective of this mission was to understand how computers represent numbers and text using different number systems and character encodings.

## 2. Work Completed

### Task 5.1: Manual Number Conversions

Completed the following conversions manually:

| Conversion | Answer |
|---|---|
| Decimal 13 to Binary | 1101 |
| Decimal 25 to Binary | 11001 |
| Binary 1010 to Decimal | 10 |
| Binary 1101 to Decimal | 13 |
| Hexadecimal A to Decimal | 10 |
| Hexadecimal 1F to Decimal | 31 |
| Binary 1111 to Hexadecimal | F |

### Task 5.2: Verify Conversions Using Python

Used Python's built-in functions to verify the manual calculations.

| Python Expression | Result |
|---|---|
| `bin(13)` | `0b1101` |
| `bin(25)` | `0b11001` |
| `int("1010", 2)` | `10` |
| `int("1101", 2)` | `13` |
| `int("A", 16)` | `10` |
| `int("1F", 16)` | `31` |
| `hex(15)` | `0xf` |
| `hex(13)` | `0xd` |
| `int("D", 16)` | `13` |

The Python results matched the manual calculations.

### Task 5.3: Build a Number Converter

Created `number_converter.py` to convert decimal numbers into binary and hexadecimal.

**Program:**

```python
number = int(input("Enter a decimal number: "))

binary = bin(number)[2:]
hexadecimal = hex(number)[2:].upper()

print("Binary:", binary)
print("Hexadecimal:", hexadecimal)
```

**Test Results:**

| Input | Binary | Hexadecimal |
|---:|---|---|
| 13 | 1101 | D |
| 25 | 11001 | 19 |
| 255 | 11111111 | FF |

### Task 5.4: Understand Text Encoding

| Question | Answer |
|---|---|
| ASCII decimal code for uppercase A | 65 |
| ASCII decimal code for lowercase a | 97 |
| Why is encoding needed? | Computers store information as bits, so encoding standards represent characters using numerical values. |
| Example of a character outside basic ASCII | ₹ |

**ASCII and UTF-8:**

- ASCII represents a basic set of English letters, digits and symbols.
- UTF-8 supports a much wider range of characters, including different languages and emojis.

## 3. Commands / Tools Used

- `python3` – Starts the Python interpreter.
- `bin()` – Converts an integer into binary.
- `hex()` – Converts an integer into hexadecimal.
- `int()` – Converts a value into an integer using a specified base.
- `python3 number_converter.py` – Runs the number converter program.
- Visual Studio Code – Used to create and edit the Python file.
- macOS Terminal – Used to execute Python commands.

## 4. My Understanding

Through this mission, I learned how decimal, binary and hexadecimal number systems work. I practised converting numbers manually and verifying the results using Python. I also learned how computers represent text using character encoding standards such as ASCII and UTF-8.

## 5. Difficulties Faced

- Understanding repeated division for decimal-to-binary conversion.
- Understanding positional values in binary and hexadecimal.
- Remembering the Python conversion functions.

## 6. How I Resolved Them

- Practised repeated division and place-value calculations.
- Used Python's built-in conversion functions to verify results.
- Tested the number converter with three different inputs.

## 7. Evidence / Files

- `mission-05-numbers-data/README.md`
- `mission-05-numbers-data/number_converter.py`
- Manual conversion results and Python verification outputs.

## 8. Commit Details

**Commit Message:** `Complete Mission 5 numbers and data`

**GitHub Repository:** `digital-detective-8049`

**Branch:** `master`
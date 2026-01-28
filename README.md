# B211-Assignment_1
# Password Generator

## Overview
This project provides a Python-based password generator capable of producing two types of passwords:

1. **Memorable Passwords**
   - Constructed from random English nouns
   - Each word receives a random digit (0–9)
   - Words are joined with hyphens
   - Supports lower, upper, or title case formatting

2. **Random Passwords**
   - Generated from random characters
   - Supports lowercase, uppercase, digits, and optional punctuation
   - Allows exclusion of specific characters

The generator also logs every created password along with a timestamp into a file titled `Generated_Passwords.txt`.  
Each password type has its own directory:

- `Memorable/Generated_Passwords.txt`
- `Random/Generated_Passwords.txt`

If these directories do not exist, the program automatically creates them.

---

## How to Use
```python
password_generator()
Then run: python password_generator.py
You will be prompted to choose:
Memorable Password Options
- Number of words
- Case type (lower, upper, title)
-Word list is loaded from top_english_nouns_lower_100000.txt

Random Password Options
-Password length
-Whether punctuation is included
-Characters to exclude
-The generated password will be printed and logged.

To automatically generate 1000 passwords (randomly choosing between memorable and random), uncomment:
generate_1000_test()

## Output
Passwords are stored in:
Memorable/Generated_Passwords.txt
Random/Generated_Passwords.txt

Each entry includes:
password | Created: Wed Jan 28 09:56:00 2026

## Required Files
password_generator.py (main script)
top_english_nouns_lower_100000.txt (word list for memorable passwords)

## Modules Used
os — directory creation and file paths
os.path — path handling
random — random selection of words/characters
string — character sets for random passwords
time — timestamp generation
urllib.request — optional if downloading the word list

## Purpose
Use of Python standard modules
File handling and directory management
Randomization techniques
Practical password generation
Logging and timestamping
Modular program design


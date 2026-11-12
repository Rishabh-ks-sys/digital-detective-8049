## Task 2.1 — Explore Basic Terminal Operations

| Operation / Command Name | What it does | What I observed |
|---|---|---|
| Current-directory display — `pwd` | Displays the full path of the current working directory. | It displayed my assignment repository path. |
| Directory listing — `ls` | Lists files and folders in the current location. | It displayed the contents of my repository. |
| Detailed listing — `ls -l` | Displays files with permissions, owner, size and modification date. | I could see additional details about files and folders. |
| Change directory — `cd ..` | Moves to the parent directory. | My location changed from the repository to Desktop. |
| Create directory — `mkdir` | Creates a new folder. | I created a folder named terminal-practice. |
| Create empty file — `touch` | Creates an empty file. | I created sample.txt. |
| Copy file — `cp` | Creates a copy of an existing file. | I copied sample.txt to copy.txt. |
| Move / rename file — `mv` | Moves or renames a file. | I renamed copy.txt to moved.txt. |
| Display file contents — `cat` | Displays the contents of a text file. | It displayed the text stored in sample.txt. |



## Task 2.2 — Practise File Changes Safely

### 1. Difference between replacing and appending file contents

Replacing (`>`) removes the existing content and writes new content. Appending (`>>`) adds new content at the end without removing the existing content.

### 2. Difference between copying and moving a file

Copying (`cp`) creates another copy while keeping the original file. Moving (`mv`) transfers a file to another location or renames it.

### 3. What information does the current-directory display provide?

The `pwd` command displays the full path of the directory in which I am currently working.

### 4. Why is a directory-listing operation useful?

The `ls` command helps us view files and folders in the current directory and understand its contents.


## Task 2.3 — Understand Flags and Pipes

### 1. Difference Between Normal and Detailed Listings

The `ls` command displays files and folders in the current directory.

The `ls -lah` command displays a detailed listing, includes hidden files and shows file sizes in a human-readable format.

### 2. Understanding Pipes

The pipe symbol (`|`) sends the output of one command as input to another command.

Example:

`ls -l | head -n 5`

Here, `ls -l` generates a detailed directory listing, and `head -n 5` displays only the first five lines.

### 3. What I Learned

Flags modify how commands behave, while pipes allow multiple commands to work together by passing output from one command to another.

### 4. Pipe Command Output

Command used:

`ls -l | head -n 5`

Output:

total 8
-rw-r--r--@ 1 rksamal  staff  1225 Nov 12 11:31 README.md
drwxr-xr-x  2 rksamal  staff    64 Nov 12 11:22 evidence
drwxr-xr-x  3 rksamal  staff    96 Nov 12 11:23 mission-00-setup
drwxr-xr-x  3 rksamal  staff    96 Nov 12 11:23 mission-01-computer-basics

**Explanation:**
- `ls -l` generates a detailed directory listing.
- `|` passes the output to the next command.
- `head -n 5` displays only the first five lines.



## Task 2.4 — Understand Package Managers

### Package Manager: Homebrew

**Version:** 7.0.10

**Command used:**
- `brew --version` — Checks the installed Homebrew version.
- `brew list` — Displays packages managed by Homebrew.

### Why Package Managers Are Useful

A package manager helps users install, update and remove software easily. It manages software dependencies and makes software installation more convenient. Homebrew is a popular package manager for macOS.

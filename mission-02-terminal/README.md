
# Mission 2 — Become Comfortable with the Terminal

## 1. Task / Objective

The objective of this mission was to use the command-line interface to inspect folders, create and manage files, understand command options and pipes, and learn about package managers.

## 2. Work Completed

### Task 2.1 — Explore Basic Terminal Operations

| Operation / Command | What it does | What I observed |
|---|---|---|
| `pwd` | Displays the full path of the current directory. | It displayed my current working directory. |
| `ls` | Lists files and folders. | It displayed the contents of my repository. |
| `ls -l` | Displays a detailed directory listing. | It showed permissions, owner, size and modification date. |
| `cd ..` | Moves to the parent directory. | My location changed to Desktop. |
| `mkdir` | Creates a new directory. | I created terminal-practice. |
| `touch` | Creates an empty file. | I created sample.txt. |
| `cp` | Copies a file. | I created a copy of sample.txt. |
| `mv` | Moves or renames a file. | I renamed copy.txt to moved.txt. |
| `cat` | Displays file contents. | It displayed the text stored in sample.txt. |

### Task 2.2 — Practise File Changes Safely

I created a folder named terminal-practice and practised creating, editing, copying and renaming files.

**Commands used:**

- `touch sample.txt` — Created an empty file.
- `echo "Hello Terminal" > sample.txt` — Added the first line.
- `echo "Learning Linux commands" >> sample.txt` — Added a second line without removing the first.
- `cat sample.txt` — Displayed both lines.
- `cp sample.txt backup.txt` — Created a backup copy.
- `mv backup.txt renamed-backup.txt` — Renamed the backup.

**Answers to the questions:**

1. **Replacing vs appending:** The `>` operator replaces existing content, while `>>` adds content to the end of a file.

2. **Copying vs moving:** The `cp` command creates another copy while keeping the original. The `mv` command moves or renames a file.

3. **Current-directory display:** The `pwd` command displays the full path of the current working directory.

4. **Directory listing:** The `ls` command helps us view files and folders in the current directory.

### Task 2.3 — Understand Flags and Pipes

**Commands used:**

- `ls` — Displays a normal directory listing.
- `ls -lah` — Displays detailed information, includes hidden files and shows human-readable file sizes.
- `ls -l | head -n 5` — Displays the first five lines of a detailed directory listing.

**Explanation:**

Flags modify how a command behaves. The `-l` flag displays detailed information, `-a` includes hidden files and `-h` displays readable file sizes.

The pipe symbol (`|`) passes the output of one command as input to another command.

In `ls -l | head -n 5`, the first command generates a detailed listing, and the second displays only its first five lines.

-rw-r--r--@ 1 rksamal  staff  1225 Nov 12 11:31 README.md
drwxr-xr-x  2 rksamal  staff    64 Nov 12 11:22 evidence
drwxr-xr-x  3 rksamal  staff    96 Nov 12 11:23 mission-00-setup
drwxr-xr-x  3 rksamal  staff    96 Nov 12 11:23 mission-01-computer-basics

### Task 2.4 — Understand Package Managers

**Package Manager:** Homebrew

**Installed version:** 7.0.10
ca-certificates git             libunistring    openssl@4       sdl2-compat     x265
dav1d           json-c          libvmaf         opus            sdl3            xz
ffmpeg          lame            libvpx          pcre2           svt-av1
gettext         libpng          mpg123          qrencode        x264

**Commands used:**

- `brew --version` — Checks the installed Homebrew version.
- `brew list` — Displays packages managed by Homebrew.

**Why package managers are useful:**

A package manager helps users install, update and remove software easily. It also manages software dependencies and makes software installation more convenient. Homebrew is a commonly used package manager on macOS.

**My observation:**

Homebrew was already installed on my computer. I checked its version and listed its managed packages without installing or uninstalling anything.

**Packages displayed by `brew list`:**

Write the actual package names shown in your Terminal here.

## 3. Commands / Tools Used

| Command / Tool | Purpose |
|---|---|
| `pwd` | Displays the current directory path. |
| `ls` | Lists files and folders. |
| `ls -l` | Displays detailed file information. |
| `ls -lah` | Displays hidden files and readable file sizes in detailed format. |
| `cd` | Changes the current directory. |
| `mkdir` | Creates directories. |
| `touch` | Creates empty files. |
| `echo` | Prints or writes text. |
| `>` | Replaces file contents. |
| `>>` | Appends text to a file. |
| `cat` | Displays file contents. |
| `cp` | Copies files. |
| `mv` | Moves or renames files. |
| `head` | Displays the first lines of output. |
| `brew --version` | Checks the Homebrew version. |
| `brew list` | Lists Homebrew packages. |
| VS Code | Used to edit the README. |
| Git and GitHub | Used to manage and upload the project. |

## 4. My Understanding

I learned how to navigate directories and manage files using Terminal commands.

I understood the difference between copying and moving files, and between replacing and appending file contents.

I also learned that flags modify command behaviour, while pipes connect commands by passing output from one command to another.

Finally, I understood how package managers such as Homebrew help manage software on a computer.

## 5. Difficulties Faced

Initially, understanding the difference between the `>` and `>>` operators and the purpose of command flags was confusing.

## 6. How I Resolved Them

I practised the commands using sample files inside the terminal-practice folder and compared their outputs to understand their behaviour.

## 7. Evidence / Files

- README.md
- terminal-practice/sample.txt
- terminal-practice/moved.txt
- terminal-practice/renamed-backup.txt
- Terminal command outputs

## 8. Commit Details

**Commit message:** Complete Terminal and file management system.

The completed Mission 2 work was committed and pushed to the GitHub repository.




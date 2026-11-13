# Mission 3: Understand the Operating System

## 1. Task / Objective

The objective of this mission was to understand how an operating system works, explore macOS, identify running processes, understand file paths and permissions, and learn the major responsibilities of an operating system.

## 2. Work Completed

### Task 3.1: Explore Your Operating System

Explored my macOS system using Terminal commands.

| Information | Command | Observation |
|---|---|---|
| Operating System | `sw_vers` | macOS 27.2.1, Build 26B131 |
| Current User | `whoami` | Active account identified (username redacted for privacy) |
| Storage | `df -h /` | 926 GiB total, 13 GiB used, 835 GiB available |
| System Activity | `top -l 1 \| head -n 10` | 758 processes, 3 running, 755 sleeping, CPU 86.98% idle |

### Task 3.2: Understand Processes

Used process-related commands to identify running processes.

| Process | PID | Purpose |
|---|---:|---|
| launchd | 1 | Manages and starts system processes and services. |
| logd | 532 | Manages system logs. |
| Visual Studio Code | 2360 | Runs the code editor. |

**Answers:**

- A process is a program that is currently running on a computer.
- PID stands for Process ID. It is a unique numerical identifier assigned to each process.
- Examples of processes include `launchd`, `logd`, and Visual Studio Code.

### Task 3.3: Paths and Permissions

**Absolute Path:**

An absolute path specifies the complete location of a file or directory starting from the root directory.

Example:
`/Users/rksamal/Desktop/digital-detective-8049/mission-03-operating-system`

**Relative Path:**

A relative path specifies a location based on the current working directory.

Example:
`mission-03-operating-system`

**File Permissions:**

The `ls -l` command displayed the following permissions for README.md:

`-rw-r--r--`

- Owner: Read and write (`rw-`)
- Group: Read only (`r--`)
- Others: Read only (`r--`)

The directory permissions were:

`drwxr-xr-x`

- Owner: Read, write and execute (`rwx`)
- Group: Read and execute (`r-x`)
- Others: Read and execute (`r-x`)

**Meaning of permissions:**

- `r` = Read
- `w` = Write
- `x` = Execute (for directories, it allows traversal/access).

### Task 3.4: Responsibilities of an Operating System

| Responsibility | Explanation | Example |
|---|---|---|
| Process Management | Manages running programs and allocates CPU time. | Running VS Code while listening to music. |
| Memory Management | Allocates and manages RAM for programs. | Giving memory to a browser with multiple tabs open. |
| File Management | Organises, stores and retrieves files and folders. | Creating and renaming files in Finder. |
| Device Management | Controls and coordinates hardware devices. | Managing a keyboard, mouse and printer. |
| Security and Access Control | Protects data and controls access to system resources. | Logging into a Mac using a password. |
| User Interface | Provides a way for users to interact with the computer. | Using the macOS desktop, Finder and Terminal. |

## 3. Commands / Tools Used

- `sw_vers` – Displays macOS version information.
- `whoami` – Displays the current username.
- `df -h /` – Displays disk storage information.
- `top -l 1 | head -n 10` – Displays a system activity snapshot.
- `ps -axo pid,comm` – Displays process IDs and process names.
- `grep -i "code"` – Searches process output for matching text.
- `pwd` – Displays the current working directory.
- `cd` – Changes the current directory.
- `ls -l` – Displays detailed file information and permissions.
- `ls -ld .` – Displays permissions of the current directory.

**Tools:** macOS Terminal, Visual Studio Code.

## 4. My Understanding

Through this mission, I understood that an operating system manages the computer's hardware and software resources. I learned how to identify running processes, understand their PIDs, navigate using absolute and relative paths, and interpret file and directory permissions.

I also learned the six major responsibilities of an operating system and how they relate to everyday computer activities.

## 5. Difficulties Faced

- Understanding the difference between absolute and relative paths.
- Interpreting file and directory permission symbols.
- Identifying processes and understanding their PIDs.

## 6. How I Resolved Them

- Practised navigating directories using Terminal commands.
- Used `ls -l` and `ls -ld` to examine permissions.
- Used `ps` commands to identify running processes and their PIDs.
- Compared the command outputs to understand the concepts.

## 7. Evidence / Files

- `mission-03-operating-system/README.md`
- Terminal command outputs and observations from Tasks 3.1, 3.2 and 3.3.

## 8. Commit Details

**Commit Message:** `Complete Mission 3 operating system`

**GitHub Repository:** `digital-detective-8049`

**Branch:** `master`
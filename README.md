# SQL Search Tool

## Introduction

This is a Python tool for database querying, using MySQL Connector for database connections. The tool was created by BruceHanzi and developed at NewSight & Nac Studio.

The code is written on Mac.

But this tool is supported for every system including

`
Windows (Upper than XP)
`

`
MacOS (Upper than 10)
`

`
Linux (Suggest Ubuntu 14 and upper)
`

Little Tip:

Author BruceHanzi`s main environment is MacOS. He uses virtual Windows and Ubuntu Server to create Exe File and Linux File

## Copyright

Copyright © 2024 BruceHanzi

## How to Use This Tool

### First Things First
- Although it is written in Python, you don't need to install Python on your Mac.
- If you want, you can install Python 3.11 or later. I used Python 3.11 to write this program.
- I packed it into a Unix executable and Windows executable using PyInstaller.
- Thanks to PyInstaller and other libraries like `mysql-connector-python`, `os`, `sys`, `readline`, etc.
- You don't need to install Rosetta to run this program (For Mac with Apple Silicon).
- If you can, please contribute or subscribe to me on the websites listed below this file.

### Prerequisites
- Ensure you have the necessary permissions to access the database.
- Make sure the required MySQL server is running and accessible.
- This is an open-source project, you can read source code to find any questions and submit questions you have found.

## Installation

### Method for Mac And Linux

**Copy the Files**
- Copy the file (SQLSearchTool) to your desired location.

**Visibility of Hidden Files**
- If you cannot see the SQLSearchTool or _internal files, press `Shift + Command + .` (period) in Finder to show hidden files.

### Method for Windows

**Just move the exe to your desired location**

**Then double click it to run**

## Quick Start

### Run the Tool

**MacOS Or Linux**
- Open a terminal and navigate to the directory where you copied the files.
- Run the tool by executing the following command:

  ```sh
  ./SQLSearchTool
  ```

If you find that you cannot run it on your device, please run

```sh
chmod +x ./SQLSearchTool
```

If you want to make sure that you can use this tool with less premission denined, please run

```sh
sudo ./SQLSearchTool
```

Or just double-click the file to run it. (Windows Exe and unix executable file)

### Log into the Database

Follow the on-screen prompts to enter the database user, password, host, and database name when this program show the notebook application with a file named 'infos.txt'.
```
e.g.

Localhost
10004 # port, need provide in newer version
root
1234567 # provided, or write 'no' to let user provide password at anytime he(she) opens this program
BruceHanzi`s SQL Server
```

### Using the Tool

Once logged in, you can start using the tool to run SQL queries.
For help with available commands, type 'help' in the tool's console.
To view the logs, type 'log' or 'tail'.
You can also specify the number of log lines to display, 
`e.g. 'tail 10' to show the last 10 lines of the log file.`

## Why is the DMG File So Large?

The project includes all necessary dependencies and resources, which contribute to the size of the DMG file.
Don't worry; once you copy the files to your system, the actual space usage will be minimal.

## Useful Tools

### Autorun

By creating an autorun.txt file in the ./pymysqlconnector folder, you can auto-run the code when you open this console app.
You can choose to run it or not.

### Port Selection

**First Updated In Beta 24.10.3.23**

By writing port at line 2 in the infos.txt from ./pymysqlconnector folder, you can choose your port and server easier than ever.

## Troubleshooting

### Common Errors

If you encounter errors, try to read the error messages carefully.
Check online resources or forums for similar issues.
For system-related errors, you may be able to resolve them by following common troubleshooting steps.

### Program-Specific Errors

If the error is related to the program itself, please provide the error list or traceback to me.

## Additional Information

### Configuration File

You can create an infos.txt file in the same directory as the SQLSearchTool to store your database connection details. This will make it easier to log in each time you use the tool.
Example infos.txt content:

```
your_db_user
your_db_port
your_db_host
your_db_password (If you want to keep safe, you can write 'no' at this line)
your_db_name
```

### Beta Test
Beta Test Program will running until the program is stable and useful

I will release the pre-release stable version v1.24.1 in later October 2024.
Before the Release Version is released, you can use pre-beta version Pre-Beta 24.10.x.xx.b in early October 2024.
The last version of Beta is Beta (Pre-Beta) 24.10.3.25.
Then I will wait for you guys`s suggestions and bug report.
Later I will first send you pre-release stable version v1.24.b.
Finally I will send you stable version v1.24.1.

## The formula of versions:

### Beta

`24(year, only 2024).10(month, only 10).3(date, only 2, 3).specific version`

### pre-release

**beta**

`24(year, only 2024).10(month, only 10).3(date, only 2, 3).specific version.b(beta)`

**stable**

`v1(main version, change of it is add 1, like 1 to 2, when there are some big changes in my program, it will be changed).24(year).specific version.b(beta)`

### stable

`v1(main version, change of it is add 1, like 1 to 2, when there are some big changes in my program, it will be changed).24(year).specific version`



You can reach out to me or other helpers via the following channels:

GitHub: BruceCodeFarmer & BruceHanzi:https://github.com/BruceCodeFarmer

CSDN: BruceHanzi:https://blog.csdn.net/B20111003

Thank you for using this application! If you have any questions or need further assistance, feel free to contact me through the provided channels.🤗

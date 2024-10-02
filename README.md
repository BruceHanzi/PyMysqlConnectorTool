# SQL Search Tool

## Introduction

This is a Python tool for database querying, using MySQL Connector for database connections. The tool was created by BruceHanzi and developed at NewSight & Nac Studio.

## Copyright

Copyright © 2024 BruceHanzi

## How to Use This Tool

### First Things First
- Although it is written in Python, you don't need to install Python on your Mac.
- If you want, you can install Python 3.11 or later. I used Python 3.11 to write this program.
- I packed it into a Unix executable using PyInstaller.
- Thanks to PyInstaller and other libraries like `mysql-connector-python`, `os`, `sys`, `readline`, etc.
- You don't need to install Rosetta to run this program.
- If you can, please contribute or subscribe to me on the websites listed below this file.

### Prerequisites
- Ensure you have the necessary permissions to access the database.
- Make sure the required MySQL server is running and accessible.

## Installation

### Copy the Files
- Copy the file (SQLSearchTool) to your desired location.

### Visibility of Hidden Files
- If you cannot see the SQLSearchTool or _internal files, press `Shift + Command + .` (period) in Finder to show hidden files.

## Quick Start

### Run the Tool
- Open a terminal and navigate to the directory where you copied the files.
- Run the tool by executing the following command:

  ```sh
  ./SQLSearchTool
  ```

Or just double-click the file to run it.

### Log into the Database

Follow the on-screen prompts to enter the database user, password, host, and database name.
Using the Tool

Once logged in, you can start using the tool to run SQL queries.
For help with available commands, type help in the tool's console.
To view the logs, type log or tail.
You can also specify the number of log lines to display, e.g., tail 10 to show the last 10 lines of the log file.
Why is the DMG File So Large?

The project includes all necessary dependencies and resources, which contribute to the size of the DMG file.
Don't worry; once you copy the files to your system, the actual space usage will be minimal.
## Useful Tools

### Autorun

By creating an autorun.txt file in the ./pymysqlconnector folder, you can auto-run the code when you open this console app.
You can choose to run it or not.

## Troubleshooting

### Common Errors

If you encounter errors, try to read the error messages carefully.
Check online resources or forums for similar issues.
For system-related errors, you may be able to resolve them by following common troubleshooting steps.
Program-Specific Errors

If the error is related to the program itself, please provide the error list or traceback.

## Additional Information

### Configuration File

You can create an infos.txt file in the same directory as the SQLSearchTool to store your database connection details. This will make it easier to log in each time you use the tool.
Example infos.txt content:

```
your_db_user
your_db_host
your_db_password (If you want to keep safe, you can write 'no' at this line)
your_db_name
```

You can reach out to me or other helpers via the following channels:
GitHub: BruceCodeFarmer & BruceHanzi:https://github.com/BruceCodeFarmer
CSDN: BruceHanzi:https://blog.csdn.net/B20111003?spm=1000.2115.3001.5343
Thank you for using this application! If you have any questions or need further assistance, feel free to contact me through the provided channels.

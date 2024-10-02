from functools import partial
from time import sleep
import mysql.connector
import logging
import sys
import os
import getpass
import readline  # 用于命令历史
import schedule
# ANSI 转义序列用于控制终端文本颜色
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'
version = "beta 24.10.2.21"

def read_infos_file():
    try:
        with open('infos.txt', 'r') as file:
            lines = file.readlines()
            if len(lines) < 4:
                print("infos.txt does not contain enough information. It should have at least 3 lines: server address, username, and server name.")
                os.system('open -t infos.txt')
                logging.info(f"infos.txt does not contian enough information")
            server_address = lines[0].strip()
            username = lines[1].strip()
            password = lines[2].strip()
            server_name = lines[3].strip()
            return server_address, username, password, server_name
    except FileNotFoundError:
        print(RED + "infos.txt not found. Please create the file and add the necessary information at users/you/.pymysqlconnector" + RESET)
        print(RED + "if you cannot see the folder, please press command+shift+." + RESET)
        print(RED + "This program will help you open this txt, when you created and writed, you can run this program again")
        os.system('touch infos.txt')
        os.system('open -t infos.txt')
        sleep(10)
        logging.info(f"infos.txt not found, user will create or not")
        sys.exit(1)
    except Exception as e:
        print(RED + f"Error reading infos.txt: {e}" + RESET)
        logging.error(f"Error when reading infos.txt {e}")
        sys.exit(1)

def run_autorun_file(cursor):
    try:
        with open('autorun.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # 忽略空行
                    logging.info(f"Running command from autorun.txt: {line}")
                    print(f"Running command from autorun.txt: {line}")
                    cursor.execute(line)
                    result = cursor.fetchall()
                    if result:
                        print("Outputs:")
                        for row in result:
                            print(row)
                    else:
                        print("No output.")
                    logging.info(f"Command executed successfully: {line}")
    except FileNotFoundError:
        logging.error("autorun.txt not found")
        print(RED + "autorun.txt not found" + RESET)
    except mysql.connector.Error as e:
        logging.error(f"Database error while running autorun.txt: {e}")
        print(RED + f"Database error while running autorun.txt: {e}" + RESET)
        return False
    except Exception as e:
        logging.error(f"System error while running autorun.txt: {e}")
        print(RED + f"System error while running autorun.txt: {e}" + RESET)
        return False
    return True

def view_log(command, n_lines=None):
    try:
        with open('sql_search.log', 'r') as log_file:
            lines = log_file.readlines()
            if n_lines and n_lines > 0:
                lines = lines[-n_lines:]
            for line in lines:
                if 'INFO' in line and 'Connected to SQL Server' in line:
                    print(GREEN + line.strip() + RESET)
                elif 'ERROR' in line or 'CRITICAL' in line:
                    print(YELLOW + line.strip() + RESET)
                else:
                    print(line.strip())
    except FileNotFoundError:
        print(RED + "Log file not found." + RESET)
    except Exception as e:
        print(RED + f"Error reading log file: {e}" + RESET)

def main():
    try:
        os.system('clear')
        # 更改工作目录到主目录下的 .pymysqlconnector 文件夹
        home_dir = os.path.expanduser("~")  # 获取用户的主目录
        pymysqlconnector_dir = os.path.join(home_dir, '.pymysqlconnector')  # 构建 .pymysqlconnector 目录路径
        if not os.path.exists(pymysqlconnector_dir):  # 如果目录不存在
            os.makedirs(pymysqlconnector_dir)  # 创建目录load_scheduled_tasks(scheduled_file_path)
        os.chdir(pymysqlconnector_dir)  # 改变当前工作目录
        # 配置日志
        logging.basicConfig(filename='sql_search.log', level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            filemode='a')  # 'a' 模式表示追加写入，而不是覆盖
        logging.info("Starting Home SQL Server")
        print("Welcome to the SQL server connector with Python!")
        print(f"Program version: {version} for Mac with Apple Silicon or Intel Processor")

        # 读取 infos.txt 文件
        server_address, username, password, server_name = read_infos_file()

        # 使用 getpass 获取密码
        if password == 'no':
            password = getpass.getpass(GREEN + "Please provide Root's Password: " + RESET)

        try:
            # 连接到 MySQL 数据库
            mydb = mysql.connector.connect(
                host=server_address,
                user=username,
                passwd=password
            )

            logging.info("Connected to SQL Server")
            print(GREEN + f"Connected to SQL Server: {server_name}" + RESET)
            print(f"Host: {GREEN}{server_address}{RESET}")
            print(f"User: {GREEN}{username}{RESET}")
            print("Password: (Only you can know)")
            print("Welcome to the SQL Tool. Type your command or EXIT to quit.")
            logging.info(f"""Further Connection Info:
Host: {server_address}
User: {username}
Password: (Keep Safety, do not try it here)""")

            mycursor = mydb.cursor()

            # 检测是否存在 autorun.txt 文件
            if os.path.exists('autorun.txt'):
                response = input("autorun.txt is found. Do you want to automatically run its contents? (y/n): ").strip().lower()
                if response == 'y':
                    if not run_autorun_file(mycursor):
                        # 如果 autorun.txt 执行出错，询问用户下一步操作
                        while True:
                            action = input("An error occurred. Do you want to (c)ontinue, (e)xit, or (o)pen the txt file to edit? (c/e/o): ").strip().lower()
                            if action == 'c':
                                break
                            elif action == 'e':
                                logging.info("System exited due to user decision")
                                sys.exit()
                            elif action == 'o':
                                os.system('open -t autorun.txt')
                                break
                            else:
                                print("Invalid input, please choose (c)ontinue, (e)xit, or (o)pen the txt file to edit.")

            # 主循环
            history_file = os.path.expanduser("~/.pymysqlconnector/.sql_tool_history")
            if os.path.exists(history_file):
                readline.read_history_file(history_file)

            while True:
                try:
                    # 获取用户输入的命令
                    command = input("User Command: ")
                    readline.write_history_file(history_file)  # 保存命令历史
                    logging.info(f"User input: {command}")

                    if command.upper() == "EXIT":
                        logging.info("Exiting SQL Server Connector")
                        print("Exiting SQL Server Connector")
                        break

                    if command.upper() == "AUTORUN":
                        if os.path.exists('autorun.txt'):
                            response = input(
                                "autorun.txt is found. Do you want to automatically run its contents? (y/n): ").strip().lower()
                            if response == 'y':
                                if not run_autorun_file(mycursor):
                                    # 如果 autorun.txt 执行出错，询问用户下一步操作
                                    while True:
                                        action = input(
                                            "An error occurred. Do you want to (c)ontinue, (e)xit, or (o)pen the txt file to edit? (c/e/o): ").strip().lower()
                                        if action == 'c':
                                            break
                                        elif action == 'e':
                                            logging.info("System exited due to user decision")
                                            sys.exit()
                                        elif action == 'o':
                                            os.system('open -t autorun.txt')
                                            break
                                        else:
                                            print(
                                                "Invalid input, please choose (c)ontinue, (e)xit, or (o)pen the txt file to edit.")
                        continue

                    if command.upper() == "CLEAR":
                        os.system("clear")
                        continue

                    if command.upper() == "HELP":
                        print(f"""
Commands:
- AUTORUN: Run commands from autorun.txt
- CLEAR: Clear the terminal screen
- EXIT: Exit the program
- HELP: Show this help message
- TAIL [n]: View the last n lines of the log file
- LOG: View the entire log file
Version: {version}
""")
                        continue

                    if command.upper().startswith("TAIL"):
                        n_lines = int(command.split()[1]) if len(command.split()) > 1 else 10
                        view_log(command, n_lines)
                        continue

                    if command.upper() == "LOG":
                        view_log(command)
                        continue

                    # 执行 SQL 命令
                    mycursor.execute(command)
                    result = mycursor.fetchall()
                    if result:
                        print("Outputs:")
                        for row in result:
                            print(row)
                    else:
                        print("No output.")
                    logging.info(f"Command executed successfully: {command}")

                except mysql.connector.Error as e:
                    logging.error(f"Database error: {e}")
                    print(RED + f"Database error: {e}" + RESET)
                    run = input("Do you want to continue (y/n)? ").strip().lower()
                    if run == 'n':
                        logging.info("System exited due to user decision")
                        sys.exit()
                    else:
                        print("Invalid input, but continuing...")

                except Exception as e:
                    logging.error(f"System error: {e}")
                    print(RED + f"System error: {e}" + RESET)
                    run = input("Do you want to continue (y/n)? ").strip().lower()
                    if run == 'n':
                        logging.info("System exited due to exception")
                        sys.exit()

        except mysql.connector.Error as e:
            logging.error(f"Failed to connect to database: {e}")
            print(RED + f"Failed to connect to database: {e}" + RESET)
            logging.info("System exited due to connection error")
            sys.exit()

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(RED + f"Unexpected error: {e}" + RESET)
        logging.info("System exited due to unexpected error")
        sys.exit()

if __name__ == "__main__":
    main()
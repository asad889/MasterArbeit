import socket
import os
IP = socket.gethostbyname(socket.gethostname())				#to get the IPaddress
PORT = 4459									#to get the port number
ADDR = (IP, PORT)								#adress is tuple of ipaddress and port number
FORMAT = "utf-8"								#encoding format
SIZE = 1024									#buffer size	

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		#creating a socket for client
    client.connect(ADDR)							#client socket is connected with server socket

    while True:								#run forever
        data = client.recv(SIZE).decode(FORMAT)				#messaging recieving from server
        cmd, msg = data.split("@")
        if cmd == "OK":
            print(f"{msg}")

        data = input("< ")
        data = data.split(" ")
        cmd = data[0]
        if cmd == "HELP":
            client.send(cmd.encode(FORMAT))
        elif cmd == "LOGOUT":
            client.send(cmd.encode(FORMAT))
            break
        elif cmd == "UPLOAD":
            filename = data[1]
            filesize = os.path.getsize(filename)
            print(filesize)
            with open(filename, "rb") as f:
                while True:
                    bytes_read = f.read(SIZE)
                    if not bytes_read:
                        break
            data = f"{cmd}@{filename}@{bytes_read}"
            client.send(data.encode(FORMAT))


    print("Disconnected from the server.")
    client.close()

if __name__ == "__main__":
    main()

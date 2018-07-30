import socket
import time

def ex(args, message, client, invoke):

    args_out = ""
    if len(args) > 0:
        args_out = "\n\n*Attatched arguments %s*" % args.__str__()[1:-1].replace("'", "")
        argstr = str(args)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create InternetSocket for ipV4
#SOCK_STREAM - TCP SOCK_DGRAM - UDP
        server_addr = ('185.249.199.220', 1338)
        client_socket.connect(server_addr) #connect the socket | UDP does not need connect
        client_socket.send(bytes("tweetrequest", "utf8")) #send message (byte stream)
        time.sleep(4)
        client_socket.send(bytes("ilopylp", "utf8")) #send message (byte stream)
        song = client_socket.recv(1024)
        print(str(song, "utf8"))
        client_socket.close()

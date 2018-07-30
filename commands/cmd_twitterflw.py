import socket
import time

def ex(args, message, client, invoke):

    args_out = ""
    if len(args) > 0:
        args_out = "\n\n*Attatched arguments %s*" % args.__str__()[1:-1].replace("'", "")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_addr = ('185.249.199.220', 1338)
    client_socket.connect(server_addr)
    client_socket.send(bytes("tweetrequest", "utf8")
    time.sleep(1)
    argstr = str(args)
    client_socket.send(bytes(argstr, "utf8"))
    number = client_socket.recv(1024)
    number2 = str(number, "utf8")
    yield from client.send_message(message.channel, "The user  " + arg + "has " + number2 + " followers")

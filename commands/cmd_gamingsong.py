import socket
import langfile

def ex(args, message, client, invoke):

    args_out = ""
    if len(args) > 0:
        args_out = "\n\n*Attatched arguments %s*" % args.__str__()[1:-1].replace("'", "")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_addr = ('185.249.199.220', 1338)
    client_socket.connect(server_addr)
    client_socket.send(bytes("gamingsong", "utf8"))
    song = client_socket.recv(1024)
    yield from client.send_message(message.channel, langfile.lang_gamingsong + str(song, "utf8") + args_out)

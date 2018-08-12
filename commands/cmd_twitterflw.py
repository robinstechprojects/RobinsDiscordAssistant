import socket
import time
import langfile

def ex(args, message, client, invoke):

    args_out = ""
    if len(args) > 0:
        args_out = "\n\n*Attatched arguments %s*" % args.__str__()[1:-1].replace("'", "")
        argstr = args.__str__()[1:-1].replace("'", "")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create InternetSocket for ipV4
#SOCK_STREAM - TCP SOCK_DGRAM - UDP
        server_addr = ('185.249.199.220', 1338)
        client_socket.connect(server_addr) #connect the socket | UDP does not need connect
        client_socket.send(bytes("tweetrequest", "utf8")) #send message (byte stream)
        time.sleep(4)
        print(argstr)
        client_socket.send(bytes(argstr, "utf8")) #send message (byte stream)
        song = client_socket.recv(1024)
        print(str(song, "utf8"))
        yield from client.send_message(message.channel, langfile.lang_twitterflw + str(song, "utf8"))

        client_socket.close()

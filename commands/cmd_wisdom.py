import random


def ex(args, message, client, invoke):
    args_out = ""
    if len(args) > 0:
        args_out = "\n\n*Attatched arguments %s*" % args.__str__()[1:-1].replace("'", "")
        datei = open('wisdoms.txt', 'r')
        sammlung = datei.readlines()
        datei.close()
        zitat = random.choice(sammlung)
        yield from client.send_message(message.author, zitat + args_out)

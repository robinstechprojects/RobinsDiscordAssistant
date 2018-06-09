import random


def ex(args, message, client, invoke):

    args_out = ""
    if len(args) > 0:
        args_out = "\n\n*Attatched arguments %s*" % args.__str__()[1:-1].replace("'", "")
    file = open('wisdoms.txt', 'r')
    wisdoms = file.readlines()
    file.close()
    qoute = random.choice(wisdoms)
    yield from client.send_message(message.author, qoute + args_out)

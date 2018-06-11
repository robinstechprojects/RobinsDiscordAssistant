from random import randint


def ex(args, message, client, invoke):

    args_out = ""
    if len(args) > 0:
        args_out = "\n\n*Attatched arguments %s*" % args.__str__()[1:-1].replace("'", "")
    psolution = randint(1, 6)
    solution = str(psolution)
    yield from client.send_message(message.channel, solution + args_out)

from random import randint


def ex(args, message, client, invoke):

    args_out = ""
    if len(args) > 0:
        args_out = "\n\n*Attatched arguments %s*" % args.__str__()[1:-1].replace("'", "")
    solution = randint(1, 6)
    yield from client.send_message(message.author, solution + args_out)

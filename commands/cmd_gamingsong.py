import random


def ex(args, message, client, invoke):

    args_out = ""
    if len(args) > 0:
        args_out = "\n\n*Attatched arguments %s*" % args.__str__()[1:-1].replace("'", "")
    file = open('gamingsongs.txt', 'r')
    song = file.readlines()
    file.close()
    title = random.choice(song)
    yield from client.send_message(message.channel, "Your Gaming-Song suggestion is: " + title + args_out)

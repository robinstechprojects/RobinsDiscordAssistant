def ex(args, message, client, invoke):
    args_out = ""
    if len(args) > 0:
        args_out = "\n\n*Attatched arguments %s*" % args.__str__()[1:-1].replace("'", "")
    yield from client.send_message(message.author, "A few steps Backwards will keep you moving forward" + args_out)
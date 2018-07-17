

def ex(args, message, client, invoke):

    args_out = ""
    if len(args) > 0:
        args_out = "\n\n*Attatched arguments %s*" % args.__str__()[1:-1].replace("'", "")
        try:
            channel = message.author.voice.voice_channel
            voice = yield from client.join_voice_channel(channel)
            player = voice.create_ffmpeg_player('Sounds\h.mp3')
            player.start()
        except Exception as exc:
            yield from client.send_message(message.channel, "Es ist ein Fehler aufgetreten. ```{ttt}```".format(ttt=exc))
        voice_client = client.voice_client_in(message.server)
        yield from voice_client.disconnect()



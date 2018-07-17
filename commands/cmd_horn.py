

def ex(args, message, client, invoke):
        try:
            channel = message.author.voice.voice_channel
            voice = yield from client.join_voice_channel(channel)
            player = voice.create_ffmpeg_player('h.mp3')
            player.start()
        except Exception as exc:
            yield from client.send_message(message.channel, "Es ist ein Fehler aufgetreten. ```{ttt}```".format(ttt=exc))





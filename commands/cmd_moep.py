import time


def ex(args, message, client, invoke):
        try:
            channel = message.author.voice.voice_channel
            voice = yield from client.join_voice_channel(channel)
            player = voice.create_ffmpeg_player('moep.mp3')
            player.start()
        except Exception as exc:
            yield from client.send_message(message.channel, "Es ist ein Fehler aufgetreten. ```{ttt}```".format(ttt=exc))

        time.sleep(6)
        yield from client.send_message(message.channel, "I just horned !")
        voice_client = client.voice_client_in(message.server)
        yield from voice_client.disconnect()

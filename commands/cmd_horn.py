import time
import langfile


def ex(args, message, client, invoke):
        try:
            channel = message.author.voice.voice_channel
            voice = yield from client.join_voice_channel(channel)
            player = voice.create_ffmpeg_player('h.mp3')
            player.start()
        except Exception as exc:
            yield from client.send_message(message.channel, langfile.lang_hornerror + "```{ttt}```".format(ttt=exc))

        time.sleep(2)
        yield from client.send_message(message.channel, langfile.lang_horn)
        voice_client = client.voice_client_in(message.server)
        yield from voice_client.disconnect()

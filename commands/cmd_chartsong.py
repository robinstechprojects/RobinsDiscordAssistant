import random
import langfile

#execution def
def ex(args, message, client, invoke):

    args_out = ""
    if len(args) > 0:
        args_out = "\n\n*Attatched arguments %s*" % args.__str__()[1:-1].replace("'", "")
    file = open('chartsongs.txt', 'r') #open file with songs
    song = file.readlines() #save all lines to ram
    file.close() #close the file
    title = random.choice(song) #choose random song
    yield from client.send_message(message.channel, langfile.lang_chartsong + title + args_out) # send message with song

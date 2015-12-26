import sys
import random
import telepot
import subprocess
from time import sleep, localtime, strftime

adminid = /* ILTUOID */
apikey = /* LATUAKEYPERILBOT */
 
def handle(msg):
    content_type, chat_type, chat_id, msg_date, msg_id = telepot.glance2(msg, True)
    m = telepot.namedtuple(msg, 'Message')
    testo = msg['text']        
        
    print('Got command: %s (type %s from %s by %s)' % (testo, content_type, m.chat.id, m.from_))

    if testo[0][0] == '/':
        command = testo.split(None, 1)
        
        if command[0] == '/aiuto' or command[0] == '/aiuto@pitasibot':
            if m.from_.id == adminid :
                bot.sendMessage(chat_id, str("Ma tu sai già i miei comandi, padrone.\nD'altra parte, sei tu che li hai creati. \u263a"), reply_to_message_id=msg_id)
            else:
                bot.sendMessage(chat_id, "Fuck yourself baby. \U0001f618\n https://youtu.be/87D4SZ2tyC8?t=15", reply_to_message_id=msg_id)
            
        elif command[0] == '/lancia' or command[0] == '/lancia@pitasibot':
            if len(command) > 1:
                a = command[1].split()
                res = list(filter(lambda x: x.strip() != "", a))
                
                try:
                    par = int(res[0])
                except Exception:
                    par = -1
                    
                if par > 1 and par <= 50:
                    bot.sendMessage(chat_id, str("Ho lanciato un dado a %s facce per te.\nIl risultato è stato: %s" % (par, random.randint(1, par))), reply_to_message_id=msg_id)           
                else:
                    bot.sendMessage(chat_id, str("Per favore, utilizza come parametro un numero intero maggiore di 1 e minore o uguale di 50.\nNon vorrei dover fare calcoli tropppo complessi. Sono un po' pigro."), reply_to_message_id=msg_id)           
            else:
                bot.sendMessage(chat_id, str("Ho lanciato un dado a 6 facce per te dal momento che non hai specificato parametri.\nIl risultato è stato: %s" % random.randint(1, 6)), reply_to_message_id=msg_id)           

        elif command[0] == '/orario' or command[0] == '/orario@pitasibot':
            bot.sendMessage(chat_id, strftime("Sono le %H:%M del %d/%m/%Y.", localtime()), reply_to_message_id=msg_id)
        
        elif command[0] == '/salutami' or command[0] == '/salutami@pitasibot':
            if m.from_.id == adminid :
                bot.sendMessage(chat_id, str("Salve, mio creatore!\nGrazie per avermi donato la vita."), reply_to_message_id=msg_id)
            else:
                bot.sendMessage(chat_id, str("Ciao!\n\nchiunque tu sia..."), reply_to_message_id=msg_id)
                
        elif command[0] == '/scegli' or command[0] == '/scegli@pitasibot':
            if len(command) > 1:
                a = command[1].split(",")
                res = list(filter(lambda x: x.strip() != "", a))
                l = len(res)
                if l > 1:
                    id = random.randint(0,l-1)
                    bot.sendMessage(chat_id, str("La scelta ricade su: %s" % res[id].strip()), reply_to_message_id=msg_id)           
                else:
                    bot.sendMessage(chat_id, str("Parametri mancanti.\nUtilizzo: /scegli Andrea, Filippo, ..."), reply_to_message_id=msg_id)           
            else:
                bot.sendMessage(chat_id, str("Parametri mancanti.\nUtilizzo: /scegli Andrea, Filippo, ..."), reply_to_message_id=msg_id)           

        elif command[0] == '/say' or command[0] == '/say@pitasibot':
            if m.from_.id == adminid :
                a = command.split(None, 2)
                bot.sendMessage(int(a[1]), str(a[2]))           

        
bot = telepot.Bot(apikey)
bot.notifyOnMessage(handle)
print('I am listening ...')

while 1:
    sleep(10)


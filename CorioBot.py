
import telebot
from telebot import types
import time
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup

TOKEN = '349659410:AAGAkzfa2JeQIwD8Xf7uaZSbwKcv4QX_rvs'
bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
print (bot.get_me())
browser = RoboBrowser(history=True)
browser.open('https://www.forocoches.com/foro/forumdisplay.php?f=2')
#############################################
#Listener
def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        if m.content_type == 'text': # Filtramos mensajes que sean tipo texto.
           
            cid = m.chat.id
            if m.text == 'Jada Borroka!':
                la_lucha_es(cid)
            elif 'jada' in m.text.lower():
                jada(cid)
            # elif (' mano ' in m.text.lower() or
            #    ' manos ' in m.text.lower() or
            elif (' hand ' in m.text.lower() or
                ' hands ' in m.text.lower()):
                manos(cid)
            elif ('pirat' in m.text.lower()):
                pirata(cid)
            elif ('exam' in m.text.lower()):
                exam(cid)
            elif  m.text == 'temas':
                temas_fc(cid)
            elif ('bordillo.gif' in m.text.lower()):
                bordillo(cid)


        else:
            if m.photo != None:
                print (m.photo[1])
            elif m.video!= None:
                print (m.video[1])
            else:
                print (m)
bot.set_update_listener(listener) # Así, le decimos al bot que utilice 

def la_lucha_es(cid):
    bot.send_message( cid , 'La lucha es el unico camino')
    bot.send_photo( cid, 'AgADBAAD_6gxGzJT-FEeuDlNWk15TbqDpxkABLOi87UFqZek418CAAEC')

def jada(cid):
    bot.send_photo( cid, 'AgADBAAD_6gxGzJT-FEeuDlNWk15TbqDpxkABLOi87UFqZek418CAAEC')

def manos(cid):
    bot.send_photo( cid, 'AgADBAADBqkxGzJT-FFQ5s0HSybtRqg5nRkABIxdTew-TriSs44AAgI')

def pirata(cid):
    bot.send_photo( cid, 'AgADBAADB6kxGzJT-FFHo9k71oyyX1LKvBkABQkQzL8JBh718QEAAQI')

def exam(cid):
    bot.send_document( cid, 'CgADBAADiH0AAvcaZAcePk5H5-DINwI')

def bordillo(cid):
    bot.send_document( cid, 'CgADBAADziAAAm8bZAfltB6ywfOm_wI')
#def teclado(cid):
#    markup = types.InlineKeyboardMarkup()
#    btn1 = types.InlineKeyboardButton('Prueb1','http://www.forocoches.com/foro/showthread.php?t=5690143')
#    btn2 = types.InlineKeyboardButton('Prueb2','http://www.forocoches.com/foro/showthread.php?t=5690143')
#
#    markup.add(btn1)
#    markup.add(btn2)

#    bot.send_message(cid, 'temas', None, None, markup)
    # or use row method

def temas_fc(cid):
    browser.open('https://www.forocoches.com/foro/forumdisplay.php?f=2')
    fpage = browser.parsed
    soup = BeautifulSoup(str(fpage), 'html.parser')
    trs = soup.find_all("tr")
    links=[]
    for tr in trs:
        if 'class="alt1"' in str(tr):
            soup2 = BeautifulSoup(str(tr), 'html.parser')
            link = soup2.find("a")
            if 'href="showthread.php?t=' in str(link):
               print (link.text, '-',link['href'])
               links.append(Link(link.text,link['href']))
    markup = types.InlineKeyboardMarkup()
    for btn in links:
        btn =  types.InlineKeyboardButton(btn.text,btn.link)
        markup.add(btn)
    bot.send_message(cid, 'temas', None, None, markup)

    
class Link:
    def __init__(self, text, link):
        self.link = "http://www.forocoches.com/foro/%s"%(link)
        self.text = text



@bot.message_handler(commands=['lucha']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_miramacho(m): # Definimos una función que resuleva lo que necesitemos.
        cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
        bot.send_message( cid, 'Jada Borroka!') # Con la función 'send_message()' d
        bot.send_message( cid, 'Hasta la cosecha siempre!!')


bot.polling(none_stop=True)



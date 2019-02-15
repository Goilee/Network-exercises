# -*- coding: utf-8 -*-
import time
from sleekxmpp import ClientXMPP
from lxml import etree

DELAY = 5
username = 'goil@jabber.ru'
passwd = 'enterjb2'
to = ['monk@unboiled.info', 'goil@jabber.ru']

client = ClientXMPP(username, passwd)
client.connect()
client.process()

xml = etree.parse('http://weather.nsu.ru/weather.xml')
temp = xml.xpath( '/weather/current/text()')[0]
message = 'Current temperature: ' + temp + '°C'
for t in to:
    client.send_message(t, message)
print('Sent: \'' + message + '\'')

while True:
    xml = etree.parse('http://weather.nsu.ru/weather.xml')
    new_temp = xml.xpath( '/weather/current/text()')[0]
    if new_temp != temp:
        temp = new_temp
        message = 'Current temperature: ' + temp + '°C'
        for t in to:
            client.send_message(t, message)
        print('Sent: \'' + message + '\'')

client.disconnect()

import requests
import os

TOKEN = os.environ['TOKEN']
KEY = os.environ['KEY']
BACKLOG = os.environ['BACKLOG']

def create_card(card_name):
  url = "https://api.trello.com/1/cards"

  data = {
    'key': KEY,
    'token': TOKEN,
    'idList': BACKLOG,
    'name': card_name
  }
  r = requests.post(url, data=data)

  print('\n===== CARD {} CRIADO =====\n'.format(card_name))
  print(r)
  print(r.text)
  print('\n====================\n')


create_card('novo card')
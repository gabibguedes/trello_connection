import threading
import requests
import os
import logging

from issue import Issue
from database import *

WAIT_SECONDS = 60 * 15 # 15 minutes

TRELLO_TOKEN = os.environ['TRELLO_TOKEN']
TRELLO_KEY = os.environ['TRELLO_KEY']
TRELLO_CARD_LIST = os.environ['TRELLO_CARD_LIST']
REDMINE_KEY = os.environ['REDMINE_KEY']

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

def create_card(issue:Issue):
  logging.info('===> CREATING CARD FOR {}'.format(issue.id))
  url = "https://api.trello.com/1/cards"
  data = {
    'key': TRELLO_KEY,
    'token': TRELLO_TOKEN,
    'idList': TRELLO_CARD_LIST,
    'name': '[#{}] {}'.format(issue.id, issue.name),
    'desc': issue.description,
    'urlSource': issue.link
  }
  requests.post(url, data=data)

def get_issues():
  logging.info('===> GETTING ISSUES')
  issue_link = 'https://redmine.medipreco.com.br/issues/'
  url = 'https://redmine.medipreco.com.br/projects/silo-de-produto/issues.json?assigned_to_id=me'
  issues = []

  headers = {
      'Content-type': 'application/json',
      'X-Redmine-API-Key': REDMINE_KEY
  }
  r = requests.get(url, headers=headers)

  for issue in r.json()['issues']:
    id = issue['id']
    title = issue['subject']
    description = issue['description']
    link = issue_link + str(id)
    new_issue = Issue(id, title, description, link)
    issues.append(new_issue)
  
  return issues

def make_connection():
  logging.info('===> MAKING CONECTION')
  create_table()
  issues = get_issues()
  for issue in issues:
    if not issue_exists(issue):
      insert(issue)
      create_card(issue)


def timer_call():
    make_connection()
    threading.Timer(WAIT_SECONDS, timer_call).start()

if __name__ == '__main__':
  timer_call()

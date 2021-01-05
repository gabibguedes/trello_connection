import requests
import os
from issue import Issue
from database import *

TRELLO_TOKEN = os.environ['TRELLO_TOKEN']
TRELLO_KEY = os.environ['TRELLO_KEY']
TRELLO_CARD_LIST = os.environ['TRELLO_CARD_LIST']
REDMINE_KEY = os.environ['REDMINE_KEY']

def create_card(issue:Issue):
  print('===> CREATING CARD FOR {}'.format(issue.id))
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
  print('===> GETTING ISSUES')
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
  print('===> MAKING CONECTION')
  create_table()
  issues = get_issues()
  for issue in issues:
    if not issue_exists(issue):
      insert(issue)
      create_card(issue)

if __name__ == '__main__':
  make_connection()

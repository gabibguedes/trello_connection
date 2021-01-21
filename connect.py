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

SPRINT_FIELD_ID=4
POINTS_FIELD_ID=11

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
    'desc': issue.full_description,
    'urlSource': issue.link
  }
  requests.post(url, data=data)

def find_field(field, custom_fields):
  for f in custom_fields:
    if f['id'] is field:
      return f
  return None


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
    points = find_field(POINTS_FIELD_ID, issue['custom_fields'])['value']
    sprint = find_field(SPRINT_FIELD_ID, issue['custom_fields'])['value']
    link = issue_link + str(id)
    new_issue = Issue(id, title, description, link, points, sprint)

    # TODO: Add assignee

    issues.append(new_issue)
  
  return issues

def create_cards_from_issues():
  issues = get_issues()
  for issue in issues:
    if not issue_exists(issue):
      insert(issue)
      create_card(issue)

def update_issues_from_cards_on_doing():

  # TODO: update issues based on cards on the "Doing" list

  pass

def update_issues_from_cards_on_done():
  
  # TODO: update issues based on cards on the "Done" list
  
  pass

def timer_call():
    create_cards_from_issues()
    update_issues_from_cards_on_doing()
    update_issues_from_cards_on_done()

    threading.Timer(WAIT_SECONDS, timer_call).start()

if __name__ == '__main__':
  # erase_db()
  
  create_table()
  timer_call()

  # get_db_issues()

import psycopg2
import os

POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
POSTGRES_PORT = os.environ['POSTGRES_PORT']
POSTGRES_HOST = os.environ['POSTGRES_HOST']
POSTGRES_DB = os.environ['POSTGRES_DB']

def connect():
  return psycopg2.connect(host=POSTGRES_HOST,
                       database=POSTGRES_DB,
                       user=POSTGRES_USER,
                       password=POSTGRES_PASSWORD,
                       port=POSTGRES_PORT)


def run_db_command(command):
  con = connect()
  cur = con.cursor()
  cur.execute(command)
  con.commit()
  con.close()

def run_db_fetch_command(command):
  con = connect()
  cur = con.cursor()
  cur.execute(command)
  recset = cur.fetchall()
  con.close()
  return recset

def create_table():
  run_db_command(
      'CREATE TABLE IF NOT EXISTS issue (id serial primary key, name varchar(500));')

def insert(issue):
  run_db_command('INSERT INTO issue VALUES ({}, \'{}\');'.format(issue.id, issue.name))

def erase_db():
  run_db_command('DROP TABLE IF EXISTS issue;')

def get_issues():
  recset = run_db_fetch_command('SELECT * FROM issue;')
  for rec in recset:
    print(rec)

def issue_exists(issue):
  recset = run_db_fetch_command(
      'SELECT * FROM issue WHERE id={};'.format(issue.id))
  return len(recset) > 0

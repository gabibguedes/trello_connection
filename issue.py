class Issue(object):
  def __init__(self, id, name, description, link):
    self.id = id
    self.name = name
    self.description = description
    self.link = link
  
  def __str__(self) -> str:
      return 'ISSUE {}: {}'.format(self.id, self.name)

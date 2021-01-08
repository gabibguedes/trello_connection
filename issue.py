from enum import Enum
class Status(Enum):
  NEW_ISSUE = 0
  DOING = 1
  DONE = 2


class Issue(object):
  def __init__(
    self,
    id,
    name,
    description="",
    link="",
    points=None,
    sprint=None,
    assignee=None
  ):

    self.id = id
    self.name = name
    self.description = description
    self.link = link
    self.points = points
    self.sprint = sprint
    self.assignee = assignee
    self.structure_description()
  
  def __str__(self) -> str:
      return 'ISSUE {}: {}'.format(self.id, self.name)

  def structure_description(self):
    desc = "**Issue: {}**\n".format(self.id)
    if self.points: desc = desc + "**{} Pontos**\n".format(self.points)
    if self.sprint: desc = desc + "**{}**\n".format(self.sprint)
    desc = desc + "\n" + self.description

    self.full_description = desc

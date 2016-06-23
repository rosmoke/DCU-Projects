class Score(object):
    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points
    def __eq__(self, other):
        return((self.goals,self.points) > (other.goals,other.points))
    def __str__(self):
        return("{} goal(s) and {} point(s)".format(self.goals, self.points))
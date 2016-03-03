import sm
class River(sm.SM):
    river_db = []
    # blir kalt hver gang klassen blir instansiert
    def __init__(self, initialValue):
        self.startState = initialValue
        self.river_db = self.startState
        print type(self.river_db)
    
    def view(self):
        # Her implementeres logikken for "vakker" utskrift
        # ...
        print "** Here is the state of the river-world: "
        
        allAtLeft   = "** [chicken fox grain man ---\\ \_ _/ ___________ /---]"
        onlyBoatAtRight = "** [chicken fox grain man ---\\ ___________\_ _/ /---]"
        allAtLeftFinB = "** [chicken grain man ---\\ \_ fox _/ ___________ /---]"
    
    if self.river_db[0] == ['boat isat left']:
        print isAtLeft
    elif self.river_db.index(['boat isat right']):
        print onlyBoatAtRight
        
    def database(self):
        print self.river_db
    def add(self, item):
        self.river_db.append(item)
    def remove(self, item):
        self.river_db.remove(item)
    
    
# Test Cases
r = River((['boat isat left'],['chicken isat left'],['fox isat left'],['man isat left'],['grain isat left']))
r.start()
r.view()
r.database()
r.remove(['boat isat left'])
r.add(['boat isat right'])
r.database()
r.view()
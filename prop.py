

class Proposition(object):

    """
    A class for representing propositions. 
    Each proposition object has a name and a list of producers,
    that is the actions that have the proposition on their add list
    """

    def __init__(self, name):
        self.name = name  # the name of the proposition as string
        self.producers = []  # list of actions

    def getName(self):
        return self.name

    def getProducers(self):
        return self.producers

    def setProducers(self, producers):
        self.producers = producers

    def addProducer(self, producer):
        self.producers.append(producer)

    def __str__(self):
        return self.name
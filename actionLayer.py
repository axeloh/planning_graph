

class ActionLayer(object):

    """
    A class for an ActionLayer in a level of the graph.
    The layer contains a list of actions (action objects) and a list of mutex actions (Pair objects)
    """

    def __init__(self):
        self.actions = [] # list of all the actions in the layer
        self.mutexActions = [] # list of pairs of action that are mutex in the layer


    def addAction(self, action):
        if action not in self.actions:
            self.actions.append(action)

    def removeAction(self, action):
        if action in self.actions:
            self.actions.remove(action)

    def getActions(self):
        return self.actions

    def getMutexActions(self):
        return self.mutexActions

    def addMutexActionPair(self, a1, a2):
        if (a1, a2) not in self.mutexActions and (a2, a1) not in self.mutexActions:
            self.mutexActions.append((a1, a2))

    def isMutex(self, a1, a2):
        return (a1, a2) in self.mutexActions or (a2, a1) in self.mutexActions

class Action(object):

    """
      The action class is used to define operators.
      Each action has a list of preconditions, an "add list" of positive effects,
      a "delete list" for negative effects, and the name of the action.
      The lists for preconditions and effects are lists of Proposition objects.
    """

    def __init__(self, name, pre, add, delete):
        self.name = name
        self.pre = pre
        self.add = add
        self.delete = delete

    def getPre(self):
        return self.pre

    def getAdd(self):
        return self.add

    def getDelete(self):
        return self.delete

    def isPreCond(self, prop):
        return prop in self.pre

    def allPrecondsInList(self, props):
        """
        Returns true if all the precondition of the action
        are in the propositions list
        """
        return len(filter(lambda p: p in props, self.props)) > 0

    def __str__(self):
        return self.name
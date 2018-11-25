
class PropositionLayer(object):

    """
    A class for an PropositionLayer  in a level of the graph.
    The layer contains a list of propositions (Proposition objects) and a list of mutex propositions (Pair objects)
    """

    def __init__(self):
        self.propositions = []  # list of all the propositions in the layer
        self.mutexPropositions = []  # list of pairs of propositions that are mutex in the layer

    def addProposition(self, proposition):
        self.propositions.append(proposition)

    def removePropositions(self, proposition):
        self.propositions.remove(proposition)

    def getPropositions(self):
        return self.propositions

    def addMutexProp(self, p1, p2):
        if (p1, p2) not in self.mutexActions and (p2, p1) not in self.mutexActions:
            self.mutexActions.append((p1, p2))

    def isMutex(self, p1, p2):
        return (p1, p2) in self.mutexPropositions or (p2, p1) in self.mutexPropositions

    def getMutexProps(self):
        return self.mutexPropositions

    def allPrecondsInLayer(self, action):
        """
        returns true if all propositions that are preconditions of the
        action exist in this layer, and that none of those preconditions are mutex with each other 
        (i.e. the action can be applied)
        """
        preConds = action.getPre()
        for pre in preConds:
            if pre not in self.propositions:
                return False
        for pre1 in preConds:
            for pre2 in preConds:
                if (pre1, pre2) in self.mutexPropositions or (pre2, pre1) in self.mutexPropositions:
                    return False
        return True

    


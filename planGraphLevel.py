from actionLayer import ActionLayer
from propLayer import PropositionLayer


class PlanGraphLevel(object):
    """
    A class for representing a level in the plan graph.
    For each level i, the PlanGraphLevel consists of a propositionLayer and an actionLayer
    """

    def __init__(self):
        self.actionLayer = ActionLayer()
        self.propositionLayer = PropositionLayer()

    
    def updateActionLayer(self, prevPropLayer):
        """ 
        Updates the action layer given the previous proposition layer (see propositionLayer.py)
        allAction is the list of all the actions (include noOp in the domain)
        """
        for action in








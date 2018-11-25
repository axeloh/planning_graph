


class GraphPlan:

    """
    The class for initializing and running the graphplan algorithm
    """

    def __init__(self, initialState, goals, actions):
        self.initialState = initialState
        self.goals = goals
        self.actions = actions
        self.graph = []


    def graphPlan(self, initialState, goals, actions):
        """
        :param initialState: 
        :param goals: 
        :param actions: 
        :return: 
        """


    """
    A mutex relation holds between two actions at a given level if any of the following three conditions holds:
     - Inconsistent effects: one action negates an effect of the other
     - Interference one of the effects of one action is the negation of a precondition of the other
     - Competing needs: one of the preconditions of one action is mutually exclusive with a precondition of the other
    """


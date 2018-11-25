from action import Action
from prop import Proposition

class ProblemInfo:

    # Propositions
    brushClean = Proposition("BrushClean")
    brushDirty = Proposition("BrushDirty")
    rollerClean = Proposition("RollerClean")
    rollerDirty = Proposition("RollerDirty")
    mouldingsPainted = Proposition("MouldingsPainted")
    mouldingsNotPainted = Proposition("MouldingsNotPainted")
    wallPainted = Proposition("WallPainted")
    wallNotPainted = Proposition("WallNotPainted")
    picturesHanging = Proposition("PicturesHanging")
    picturesNotHanging = Proposition("PicturesNotHanging")
    propositions = [brushClean, brushDirty, rollerClean, rollerDirty,
                    mouldingsPainted, mouldingsNotPainted, wallPainted, wallNotPainted,
                    picturesHanging, picturesNotHanging]

    # Initial conditions
    iCond = [brushClean, rollerClean, mouldingsNotPainted, wallNotPainted, picturesHanging]

    # Goals
    goals = [mouldingsPainted, wallPainted, picturesHanging]

    # Actions
    actions = [
        Action(
            'BrushPaintMouldings',
            [brushClean],
            [brushDirty, mouldingsPainted],
            [brushClean]
        ),

        Action(
            'RollerPaintMouldings',
            [rollerClean],
            [rollerDirty, mouldingsPainted],
            [rollerClean]
        ),

        Action(
            'RollerPaintWall',
            [rollerClean, picturesNotHanging],
            [rollerDirty, wallPainted],
            [rollerClean]
        ),

        Action(
            'RemovePictures',
            [picturesHanging],
            [picturesNotHanging],
            [picturesHanging]
        ),

        Action(
            'RemovePictures',
            [picturesNotHanging],
            [picturesHanging],
            [picturesNotHanging]
        )
    ]

    @staticmethod
    def getAllActions():
        return ProblemInfo.actions

    @staticmethod
    def getAllPropositions():
        return ProblemInfo.propositions




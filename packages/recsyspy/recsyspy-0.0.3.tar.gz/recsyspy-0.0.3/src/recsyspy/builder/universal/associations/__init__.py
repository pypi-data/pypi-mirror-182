from recsyspy.builder import BaseRecoBuilder


class AssociationRules(BaseRecoBuilder):
    def __init__(self, msg: str):
        print(msg)
        print("Association Rules")

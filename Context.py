from Strategy import Strategy


##-- Strategy Pattern --##
class Context():
    """
    The Context provides Signin and Signup interfaces to the users.
    """

    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    @property
    def getStrategy(self):
        return self.strategy

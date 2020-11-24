from Strategy import Strategy


##-- Strategy Pattern --##
class Context():
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    @property
    def getStrategy(self):
        return self.strategy

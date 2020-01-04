class Coordinate:
    """
    Class for basepair coordinates objects

    """

    def __init__(self, coord):

        # convert to int
        coordinate = int(coord)

        self.coordinate = coordinate

        return(None)
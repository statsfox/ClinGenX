from Chr import Chr
from Coordinate import Coordinate

class Bedline:

    def __init__(self, chr, start, end):

        # split bedfile line
        chr = str(chr)
        start = int(start)
        end = int(end)

        # get chr object
        chr = Chr(chr)
        start = Coordinate(start)
        end = Coordinate(end)

        # check stop is after start
        assert (start.coordinate < end.coordinate), "the start coordinate is greater than the stop"

        self.chr = chr
        self.start = start
        self.end = end

        return(None)

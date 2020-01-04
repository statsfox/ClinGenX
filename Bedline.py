from Chr import Chr

class Bedline:

    def __init__(self, chr, start, stop):

        # split bedfile line
        chr = str(chr)
        start = int(start)
        stop = int(stop)

        # get chr object
        chr = Chr(chr)

        # check coordinates are int
        assert isinstance(start, int), "start is not an integer"
        assert isinstance(stop, int), "stop is not an integer"

        # check stop is after start
        assert (start < stop), "the start coordinate is greater than the stop"

        self.chr = chr
        self.start = start
        self.end = stop

        return(None)

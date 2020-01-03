import pybedtools

chr_list = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','X',
            'Y','MT']

class Bedline:

    def __init__(self, chr, start, stop):

        # split bedfile line
        chr = str(chr)
        start = int(start)
        stop = int(stop)

        # check chromosomes are sensible
        assert chr in chr_list, "chromosome is not valid"

        # check coordinates are int
        assert isinstance(start, int), "start is not an integer"
        assert isinstance(stop, int), "stop is not an integer"

        # check stop is after start
        assert (start < stop), "the start coordinate is greater than the stop"

        self.chr = chr
        self.start = start
        self.end = stop

        return(None)

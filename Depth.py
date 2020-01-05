import tabix

class Depth:
    """
    holds information on per-base depth for a given bed entry

    """

    def __init__(self, bedline, depthfile):

        try:
            tb = tabix.open(depthfile)
        except:
            print("could not open depthfile with tabix")
            quit()

        try:
            records = list(tb.query(bedline.chr.seq, bedline.start.coordinate, bedline.end.coordinate)) # to list as tb.query returns iterator which can only be accesses once
        except:
            print("unable to extract records using depthfile and given coordinates")
            quit()

        self.chr = bedline.chr.seq # inherited from bedline. Better way using inheritance?
        self.start = bedline.start.coordinate  # inherited from bedline. Better way using inheritance?
        self.end = bedline.end.coordinate  # inherited from bedline. Better way using inheritance?
        # self.meta will be needed - this will have to be its own class

        self.records = records


        return None


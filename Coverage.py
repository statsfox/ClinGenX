
class Coverage:
    """
    holds information on coverage

    """

    def __init__(self, depth, mindepth):

        try:
            mindepth = int(mindepth)
        except:
            print("given mindepth %r must be an integer" % mindepth)
            quit()

        # calculate average depth

        ## interval size
        length = (depth.end - depth.start) + 1 # plus 1 because it is inclusive

        total_coverage = 0
        meets_mindepth = 0

        for rec in depth.records:
            try:
                depth_at_base = int(rec[2])
            except:
                print("expected integer in depthfile but got: %r" % rec[2])
            total_coverage = (total_coverage + depth_at_base)
            if (depth_at_base >= mindepth):
                meets_mindepth += 1

        avg_coverage = total_coverage / length
        perc_mindepth = (meets_mindepth / length) * 100

        self.chr = depth.chr
        self.start = depth.start
        self.end = depth.end
        self.mindepth = mindepth
        self.avg_coverage = avg_coverage
        self.perc_mindepth = perc_mindepth

        return None
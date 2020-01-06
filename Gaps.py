class Gaps:
    """
    holds information on gaps (either due to positions with fewer reads than defined in mindepth or
    positions missing from depth file)

    """

    def __init__(self, depth, mindepth):

        try:
            mindepth = int(mindepth)
        except:
            print("given mindepth %r must be an integer" % mindepth)
            quit()

        # list of position in depth file that do not meet mindepth
        meets_mindepth = {}
        depth_bp = []
        current_pos = 0
        depth_at_base= 0

        for rec in depth.records:

            # check coordinate is coercible to integer
            try:
                current_pos = int(rec[1])
            except:
                print("expected integer coordinate in depthfile but got: %r" % rec[2])
                quit()

            depth_bp.append(current_pos)

            # check depth is coercible to integer
            try:
                depth_at_base = int(rec[2])
            except:
                print("expected integer depth in depthfile but got: %r" % rec[2])
                quit()

            if (depth_at_base < mindepth):
                meets_mindepth[current_pos] = False
            elif (depth_at_base >= mindepth):
                meets_mindepth[current_pos] = True
            else:
                quit()

        # list of intevals in bedline that are not available in depth file (missing)
        bed_bp = []
        for bp in range(depth.start, depth.end):
            bed_bp.append(bp)

        print(list(set(bed_bp) - set(depth_bp)))
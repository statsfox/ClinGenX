
chr_list = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','X',
            'Y','MT']

class Chr:
    """
    Class for chromosome objects

    """

    def __init__(self, chr):

        # convert to string
        chr = str(chr)

        # exit if chr contains white space
        if ' ' in chr:
            exit(1)

        # check chromosome format and remove prefix if found
        if chr.startswith(("chr","Chr","CHR")):
            chr = chr[3:]

        # deal with sex and mt chromosomes
        if chr == "23": chr = "X"
        elif chr == "24": chr = "Y"
        elif chr == "25": chr = "MT"

        # check chromosomes are as expected
        assert chr in chr_list, "chromosome %r is not valid. Expected chromosomes are: %r" % (chr,chr_list)

        self.seq = chr

        return(None)

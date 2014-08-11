#!/usr/bin/env python

from math import exp

def main():

    """Generates the simple two Helium test case

    It shall generate 90 files according to the syntax of the configurations of
    the morsefit program. The system is just a two Helium atoms interacting via
    a toy set of Morse parameters.

    """

    de = 0.35
    a = 1.2
    r0 = 0.8
    
    for i in xrange(0, 90):

        r = 0.4 + 0.1 * i 
        en = de * ((
                1.0 - exp(-a * (r - r0))
                ) ** 2 - 1.0)

        fn = "conf-%2.2d" % i
        out = open(fn, 'w')
        print >> out, "%25.7f" % en
        print >> out, "%10.2f" % r
        print >> out, ""
        print >> out, " He 0.0 0.0 0.0 "
        print >> out, ""
        print >> out, " He %10.2f 0.0 0.0 " % r
        print >> out, ""

        print " %10.2f  %25.8f " % (r, en)

        continue

    return 0

if __name__ == '__main__':
    main()




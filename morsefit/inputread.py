"""Defines the subroutines for reading the input files"""

import sys

from .configuration import Configuration


def read_morse_inp(inp_file):
    
    """Reads the input file for the guesses of Morse potential

    It parses the input file and returns a list of the Morse potentials to
    be fitted. The input file has got one line for each Morse potential to be
    fitted and skips the blank and lines started with the hash sign. For each
    Morse potential, the element signs of the two atoms needs to be given along
    with the initial guesses for the De, a, and r_0 parameters. 

    The returned list contains pairs of the sorted pair of the element symbol
    and the initial guess values.

    """

    morse_params = []

    for i_line in inp_file:

        line_stripped = i_line.strip()
        if len(line_stripped) == 0 or line_stripped[0] == '#':
            continue

        fields = line_stripped.split()
        try:
            elem = tuple(sorted(fields[0:2]))
            init_guess = tuple(float(i) for i in fields[2:5])
        except IndexError:
            print "Incorrect number of fields on the line: "
            print i_line
            sys.exit(1)
        except ValueError:
            print "Incorrect format of numbers on the line: "
            print i_line
            sys.exit(1)
        morse_params.append(
                        (elem, init_guess) )

        continue

    return morse_params



def read_configuration(file_name, cut_off):

    """Read the configuration from a file

    :param file_name: The file name for the configuration file, which should be
      a string that can be used in the :py:func:`open` function.
    :param cut_off: The cut-off for the pairwise interactions.

    """

    try:
        f = open(file_name)
    except IOError:
        print " File %s cannot be opened! " % file_name
        sys.exit(1)

    sections = []
    cur_section = []
    for line in f:
        stripped = line.strip()
        if len(stripped) != 0:
            cur_section.append(stripped)
            continue
        else:
            sections.append(cur_section)
            cur_section = []
            continue

    try:
        ab_initio_e = float(sections[0][0])
    except ValueError:
        print "Incorrect ab-initio energy in %s" % file_name
        sys.exit(1)

    molecules = []
    for i_mol in sections[1:]:
        cur_mol = []
        for i_atm in i_mol:
            fields = i_mol.split()
            try:
                symb = fields[0]
                coord = np.array( [float(i) for i in fields[1:4] ] )
                cur_mol.append( (symb, coord) )
            except (IndexError, ValueError):
                print "In file %s, corrupt line: " % file_name
                print i_atm
                sys.exit(1)
            continue
        molecules.append(cur_mol)
        continue

    conf = Configuration(file_name)
    conf.ab_initio_e = ab_initio_e
    for i in molecules:
        conf.add_molecule(i)
        continue
    conf.calc_interactions(cut_off)

    return conf





        conf.add_molecule(















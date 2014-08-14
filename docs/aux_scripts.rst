Auxiliary scripts
-----------------

In order to make the process of converting the output from quantum mechanical
codes to the input format required by the ``morsefit`` code without much
difficulty, auxiliary scripts are written to facilitate the process. Currently
just one ``readPES`` script has been finished, which is based on the cclib_
python library and should be able to work with a lot of computational chemistry
codes.

readPES
^^^^^^^

Due to the large number of configurations that is needed for this script, the
configurations are not taken from the command line arguments but rather from
the file given as the first command line argument in JSON format. It is based
on the cclib library and should be able to support all the output format that
is supported there. The options include:

input_globs
    A glob string whose expansion is able to give all the input files.

input_format
    The format of the input files, should be given in compatible with the
    supported format options of cclib_. Its default value is to use the default
    format deduction of the ``ccopen`` function of cclib.

ref_energy
    The reference energy which is going to be subtracted to get the interaction
    energy. It should be given in the unit of eV.

output_pattern, output_repl
    The pattern to be matched against the input file names and the replacement
    to get the file name of the output file. It follows the conventions used in
    the built-in ``re.subs`` function in the regular expression module of
    python.

tag_pattern, tag_repl
    The pattern and replacement to get the tag file for each input file. It can
    be absent to given blank tags.

element_symbols
    A list of element symbols to substitute the ones in the input file. It
    should be given as a list or it can be absent to use the original symbols in
    the input file.

first_molecule_natoms, last_molecule_natoms
    The number of molecules in the first or the last molecule. By this the
    system is going to be divided into two molecules. These two options are
    mutually exclusive. At lease one should be specified.

An example of the input file will be:
::

    {
            "input_globs": "../*/res/pyrene.out",
            "ref_energy": -17502.34385822885,
            "output_pattern": ".*/(\\d*)/.*",
            "output_repl": "conf-\\1",
            "tag_pattern": "(.*)/res/pyrene.out",
            "tag_repl": "\\1/len",
            "last_molecule_natoms": 2,
            "element_symbols": [ 
                    "H1", "H1", "H1", "H1", "H1", "B1", "H1", "B1", "H1", "B1", 
                    "B1", "B1", "H1", "B1", "B1", "H1", "B1", "H1", "N1", "N1", 
                    "N1", "N1", "N1", "N1", "N1", "N1", "H99", "H99"] 
    }

.. _cclib: http://cclib.github.io 


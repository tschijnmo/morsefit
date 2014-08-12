Using the morsefit code
-----------------------

The code can be invoked by the ``morsefit`` driver script. The configurations on
which the fitting is based should be specified by the files whose names are
given in the command line argument. One file for each configuration. The files
have got a very simple format comprised of sections separated by blank lines.
The first section gives the ab-initio energy, and an optional tag for the
configuration can be given in the next line. Additional lines in the first
section are going to be ignored. The following sections are going to be the
Cartesian coordinates of the atoms in the molecules of the system. Only the
interaction between molecules are going to be considered, with all the
intra-molecular interactions ignored. 

The code also accepts optional arguments for the distance cut-off and the input
file for the initial guesses of the Morse potentials. The cut-off defaults to
``None``, which leads to no distance cut-off. And the default file name for the
Morse potential parameter initial guess input is ``morse.inp``. The file should
consists of lines for the initial guesses for the Morse interaction between the
atoms, with the first two fields being the atomic symbols for the interacting
pairs and the remaining three fields being the :math:`D_e`, :math:`a`, and
:math:`r_0` parameters for the Morse potential. All the interacting pairs in the
configurations should be given here. And here the blank lines and lines starting
with the hash sign are going to be skipped.



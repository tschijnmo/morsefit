Using the morsefit code
-----------------------

The code can be invoked by the ``morsefit`` driver script. The configurations on
which the fitting is based should be specified by files whose names are given in
the command line argument. One file for each configuration. The files have got a
very simple format comprised of sections separated by blank lines.  The first
section gives the ab-initio energy, and an optional tag for the configuration
can be given in the next line. Additional lines in the first section are going
to be ignored. The following sections are going to be the Cartesian coordinates
of the atoms in the molecules of the system. Only the interaction between
molecules are going to be considered, with all the intra-molecular interactions
ignored. Most of the times the number of input files is going to be larger than
what is manually manageable, so globbing by shell can be helpful here.

The code also needs the initial guesses for all the Morse interactions in the
system. And the default file name for the Morse potential parameter initial
guess input is ``morse.inp``, which can be changed by command line argument. The
file should consists of lines for the initial guesses for the Morse interactions
between the atoms, with the first two fields being the atomic symbols for the
interacting pairs and the next three fields being the :math:`D_e`, :math:`a`,
and :math:`r_0` parameters for the Morse potential. All the interacting pairs in
the configurations should be given here. And here the blank lines and lines
starting with the hash sign are going to be skipped. Optionally, the lower and
upper bound for the parameters can be given for all the three parameters
following the initial guesses. They can be given as ``None`` to indicate no
bound. Note that some solvers does not support the usage of bounds.

The code also accepts several optional arguments,

-g, --guess       The file name for the initial guess file, default to
                  ``morse.inp``.
-m, --method      The optimization method, default to ``LMA`` for
                  Levenberg-Marquardt algorithm. Besides this, all the methods in
                  the ``scipy.optimize.minimize`` function are supported. Note
                  that not all of the methods are able to handle bounds.
-j, --no-jacobian  Disable the computation of the analytic Jacobian. This can be
                   tried when you are really desperate.
-t, --tolerance   The stopping criterion for the minimization solvers.
-i, --trunk-size  The size of one trunk of optimization steps. The parameters are
                  going to be printed for every trunk.
-s, --steps       The maximum number of trunks of steps.
-c, --cutoff      The distance cut-off for the interactions.
-f, --factor      The scaling factor for the initial step of the
                  Levenberg-Marquardt solver.
-d, --diagonal    The diag argument for the Levenberg-Marquardt solver, it can be
                  a single number or a list of numbers for each of the
                  parameters.

As an example, ::

  morsefit -m TNC -t 1.0E-5 conf-*

would start the optimization with the ``TNC`` solver to a tolerance of
:math:`1.0\times10^{-5}` for the input files matching the glob pattern
``conf-*``.


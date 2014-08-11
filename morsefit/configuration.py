"""Defines the class for an atomic configuration"""

import itertools

import numpy as np
from numpy import linalg


class Configuration(object):

    """Defines an configuration of atoms

    All the information about the atomic configurations are tried to be stored
    and manipulated here.

    .. py:attribute:: molecules

      The molecules in the configuration, which is a list of lists of
      coordinates of atoms, given as a pair of element symbol and an numpy array
      for its Cartesian coordinate.

    .. py:attribute:: file_name

      The file name for the input file for this configuration.

    .. py:attribute:: tag
     
      A tag for the configuration, which can be specified after the ab-initio
      energy in the input file for the configuration.

    .. py:attribute:: ab_initio_e

      The ab-initio energy.

    .. py:attribute:: cutoff

      The distance cut-off for the interactions.

    .. py:attribute:: interactions

      A list of interacting atomic pairs in the configuration. Given as a triple
      and atomic symbols and the distance.

    """

    __slots__ = [
            "molecules",
            "file_name",
            "tag",
            "ab_initio_e",
            "cut_off",
            "interactions"
            ]

    def __init__(self, file_name, tag, ab_e):

        """Initializes the configuration object

        It just initializes the basic properties like the file name, the tag,
        and the ab-initio energy, with the actual molecules have to be added by
        :py:method:`add_molecule`.

        :param file_name: The file name for the input file of the configuration.
        :param tag: A string for a tag of the configuration.
        :param ab_e: The ab-initio energy.

        """

        self.file_name = file_name
        self.tag = tag
        self.ab_initio_e = ab_e
        self.molecules = []
        self.cut_off = None
        self.interactions = []

    def add_molecule(self, mol):

        """Add a molecule to the configuration

        The molecule has to be specified by a list of pairs of element symbols
        and numpy 1-D array for the Cartesian coordinate.

        """

        self.molecules.append(mol)
        return None

    def calc_interactions(self, cut_off):

        """Calculate the interactions from the molecules that has been added

        .. warning::

          This method has to be invoked after the :py:method:`add_molecule` has
          been invoked for all the molecules in the system.

        :param cut_off: The cut-off for calculating the interactions. It can be
                        set to ``None`` to set no cut-off.
        :return: The number of interactions that has been recognized.


        """

        for mol1, mol2 in itertools.combinations(self.molecules, 2):
            for atm1 in mol1:
                for atm2 in mol2:
                    dist = linalg.norm(atm1[1] - atm2[1])
                    if cut_off and dist > cut_off:
                        continue
                    else:
                        self.interactions.append(
                                ((atm1[0], atm2[0]), dist) )
                        continue

        self.cut_off = cut_off

        return len(self.interactions)







# -*- coding: utf-8 -*-
"""
YALTApy
Copyright (C) 2022 Inria

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


from collections import OrderedDict

LANG = 'ENG'
#LANG = 'FR'


class Fields(object):
    """Generic class settings all the possible key-words for our mathematical
    object with the language specified by LANG."""

    def __init__(self):

        # Language set
        self.lang = LANG
        # Our data structure, an ordered dictionnary so that we can handle
        # the order our fields are printed/displayed to user.
        self.struct = OrderedDict()

        if self.lang == 'FR':
            self.type = u'Type'
            self.asymp_stab = u'StabilitéAsymp'
            self.roots_no_delay = u'RacinesSansRetard'
            self.roots_chain = u'ChainesPôles'
            self.crossing_tab = u'TableauCroisements'
            self.imag_roots = u'RacinesImaginaires'
            self.stab_win = u'FenêtresStabilité'
            self.nb_unstab_poles = u'NbPôlesInstables'
            self.unstable_poles = u'PôlesInstables'
            self.error = 'ErreurPôles'
            self.root_loci = 'LieuRacines'
        elif self.lang == 'ENG':
            self.type = u'Type'
            self.asymp_stab = u'AsympStability'
            self.roots_no_delay = u'RootsNoDelay'
            self.roots_chain = u'RootsChain'
            self.crossing_tab = u'CrossingTable'
            self.imag_roots = u'ImaginaryRoots'
            self.stab_win = u'StabilityWindows'
            self.nb_unstab_poles = u'NbUnstablePoles'
            self.unstable_poles = u'UnstablePoles'
            self.error = 'PolesError'
            self.root_loci = 'RootLocus'
        else:
            raise NotImplementedError

    def get_fields_and_dict(self):
        """Return the object to manipulate easily the fields and the
        ordered dictionnary itself."""
        return self, self.struct

class FieldsAnalysis(Fields):
    """Class describing the fields of the outuput structure after the call
    of function thread_analysis()"""

    def __init__(self):

        Fields.__init__(self)
        # The fields we want to be available.
        self.struct[self.type] = None
        self.struct[self.asymp_stab] = None
        self.struct[self.roots_no_delay] = None
        self.struct[self.roots_chain] = None
        self.struct[self.crossing_tab] = None
        self.struct[self.imag_roots] = None


class FieldsStabilityWindows(Fields):
    """Class describing the fields of the outuput structure after the call
    of function thread_stability_windows()"""

    def __init__(self):

        Fields.__init__(self)
        # The fields we want to be available.
        self.struct[self.type] = None
        self.struct[self.roots_no_delay] = None
        self.struct[self.roots_chain] = None
        self.struct[self.crossing_tab] = None
        self.struct[self.stab_win] = None
        self.struct[self.nb_unstab_poles] = None


class FieldsRootLocus(Fields):
    """Class describing the fields of the outuput structure after the call
    of function thread_root_locus()"""

    def __init__(self):

        Fields.__init__(self)
        # The fields we want to be available.
        self.struct[self.roots_no_delay] = None
        self.struct[self.crossing_tab] = None
        self.struct[self.imag_roots] = None
        self.struct[self.unstable_poles] = None
        self.struct[self.error] = None
        self.struct[self.root_loci] = None


class Messages(object):
    """Class describing messages that are played back to the user during Yalta
    GUI execution."""

    def __init__(self):

        self.lang = LANG

        if self.lang == 'FR':
            self.types = [u"Retardé", u"Avancé", u"Neutre"]
            self.asymp = [u"Nombre infini de pôles instables dans le "\
                          u"demi-plan droit",
                          u"Impossible de vérifier la position des chaînes de "\
                          u"pôles sur l'axe imaginaire",
                          u"Il n'y a pas de pôles instables",
                          u"Il y a %d pôle(s) instable(s) dans le demi-plan "\
                          u"droit",
                          u"Nous ne traitons pas les systèmes avancés: "\
                          "infinité de pôles instables",
                          u"Il y a une chaîne de pôles asymptotique à l'axe "\
                          "imaginaire par la gauche. Impossible de calculer les "\
                          "pôles de petit module."]
            self.roots = u"Les chaînes de pôles sont calculées seulement pour "\
                         u"les systèmes neutres"
            self.cross = u"Pas de croisements"
            self.xlabel = u"Retard (s)"
            self.ylabel = u"Nombre de pôles instables"
            self.stablabel = u"Stabilité"
            self.rootlocilabel = u"Lieu des racines"
            self.degAproxToLow = u"Le degré de l'approximation doit être "\
                                 u"supérieur au degré du quasi-polynôme."
            self.errorModePade = u"iMode doit être soit 'ORDER' (valeur "\
                                 u"par défaut) ou 'NORM'"
            self.optNotSelected = u"Option non sélectionnée"
            self.cant_compute_root_loc = u"Impossible de déterminer le lieu des racines : ";
            self.cant_compute_pade = u"Impossible de trouver une approximation Padé-2 du système : "
            self.cant_compute_stabwin = u"Impossible de calculer les fenêtres de stabilité: "
            self.asymp_imag_by_left = u"il y a une chaîne de pôles asymptotique à l'axe imaginaire par la gauche."
            self.matrix_required = u"Matrice 2D exigée"
        elif self.lang == 'ENG':
            self.types = [u"Retarded", u"Avanced", u"Neutral"]
            self.asymp = [u"Infinite number of unstable poles in the right half-plane",
                          u"Impossible to check position of chains of poles at "\
                          u"imaginary axis",
                          u"There is no unstable pole",
                          u"There is (are) %d unstable pole(s) in the right half-"\
                          u"plane",
                          u"We are not dealing with advanced systems: infinite "\
                          u"number of unstable poles.",
                          u"There is a chain of poles clustering the imaginary "\
                          u"axis by the left. Impossible to compute poles of "\
                          u"small modulus."]
            self.roots = u"Roots chains only computed for neutral systems"
            self.cross = u"No crossing"
            self.xlabel = u"Delay (s)"
            self.ylabel = u"Number of unstable poles"
            self.stablabel = u"Stability"
            self.rootlocilabel = u"Root Locus"
            self.degAproxToLow = u"Degree of the approximation must be higher "\
                                 u"than the degree of the quasi polynomial."
            self.errorModePade = u"iMode needs to be either 'ORDER' (default "\
                                 u"value) or 'NORM'"
            self.optNotSelected = u"Option not selected"
            self.cant_compute_root_loc = u"Root locus cannot be computed: "
            self.cant_compute_pade = u"Cannot compute Pade-2 approximation: "
            self.cant_compute_stabwin = u"Stability windows cannot be computed: "
            self.asymp_imag_by_left = u"there is a chain of poles clustering the imaginary axis by the left."
            self.matrix_required = u"2D Matrix required"
        else:
            raise NotImplementedError

MSG = Messages()

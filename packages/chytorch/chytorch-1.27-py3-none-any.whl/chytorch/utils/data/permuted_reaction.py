# -*- coding: utf-8 -*-
#
#  Copyright 2022 Ramil Nugmanov <nougmanoff@protonmail.com>
#  This file is part of chytorch.
#
#  chytorch is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, see <https://www.gnu.org/licenses/>.
#
from chython import ReactionContainer
from chython.periodictable import Element
from random import random, choice
from torch import LongTensor, cat
from torch.utils.data import Dataset
from torchtyping import TensorType
from typing import Sequence, Tuple, Union
from .reaction import *


# isometric atoms
# sorted neighbors bonds, atom symbol > atom symbol, hydrogens count

isosteres = {
    (): [('B', 3), ('C', 4), ('N', 3), ('O', 2), ('F', 1),
                   ('Si', 4), ('P', 3), ('S', 2), ('Cl', 1),
                              ('As', 3), ('Se', 2), ('Br', 1),
                                         ('Te', 2), ('I', 1),
         # [BH4-] [NH4+] [OH-] [X-]
         ('B', 4), ('N', 4), ('O', 1), ('F', 0), ('Cl', 0), ('Br', 0), ('I', 0)],

    (1,): [('B', 2), ('C', 3), ('N', 2), ('O', 1), ('F', 0),
                     ('Si', 3), ('P', 2), ('S', 1), ('Cl', 0),
                                ('As', 2), ('Se', 1), ('Br', 0),
                                           ('Te', 1), ('I', 0),
           ('B', 3), ('N', 3), ('N', 1), ('O', 0), ('S', 0)],  # R[BH3-] R[NH3+] R[NH-] R[OS-]

    (2,): [('B', 1), ('C', 2), ('N', 1), ('O', 0), ('P', 1), ('S', 0), ('As', 1), ('Se', 0),
           ('N', 2), ('N', 0)],  # R=[NH2+], =[N-]
    (1, 1): [('B', 1), ('C', 2), ('N', 1), ('O', 0), ('Si', 2), ('P', 1), ('S', 0), ('As', 1), ('Se', 0), ('Te', 0),
             ('B', 2), ('N', 2), ('N', 0)],  # R2[BH2-] R2[NH2+] R2[N-]

    (3,): [('C', 1), ('N', 0), ('P', 0),
           ('C', 0), ('O', 0)],  # [C-]#[O+]
    (1, 2): [('B', 0), ('C', 1), ('N', 0), ('P', 0), ('As', 0), ('Cl', 0), ('Br', 0), ('I', 0),
             ('N', 1), ('O', 0), ('S', 0)],  # =[NH+]- =[O+]- =[S+]-
    (1, 1, 1): [('B', 0), ('C', 1), ('N', 0), ('Si', 1), ('P', 0), ('As', 0), ('Cl', 0), ('Br', 0), ('I', 0),
                ('B', 1), ('N', 1), ('S', 0)],  # R3[BH-] R3[NH+] R3[S+]

    (1, 3): [('C', 0), ('N', 0)],  # #[N+]-
    (2, 2): [('C', 0), ('Si', 0), ('S', 0), ('Se', 0), ('Te', 0), ('N', 0)],  # =[N+]=
    (1, 1, 2): [('C', 0), ('Si', 0), ('S', 0), ('Se', 0), ('Te', 0), ('B', 0), ('N', 0)],  # R2[B+]= =[N+]R2
    (1, 1, 1, 1): [('C', 0), ('Si', 0), ('S', 0), ('Se', 0), ('Te', 0), ('B', 0), ('N', 0), ('P', 0)],  # R4[B-] R4[NP+]

    (1, 2, 2): [('P', 0), ('As', 0), ('Cl', 0), ('Br', 0), ('I', 0)],
    (1, 1, 1, 2): [('P', 0), ('As', 0), ('Cl', 0), ('Br', 0), ('I', 0)],
    (1, 1, 1, 1, 1): [('P', 0), ('As', 0), ('Cl', 0), ('Br', 0), ('I', 0)],

    (2, 2, 2): [('S', 0), ('Se', 0), ('Te', 0)],
    (1, 1, 2, 2): [('S', 0), ('Se', 0), ('Te', 0)],
    (1, 1, 1, 1, 1, 1): [('S', 0), ('Se', 0), ('Te', 0), ('P', 0)],  # [PF6-]

    (1, 2, 2, 2): [('Cl', 0), ('Br', 0), ('I', 0)],
    (1, 1, 1, 2, 2): [('Cl', 0), ('Br', 0), ('I', 0)],
    (1, 1, 1, 1, 1, 2): [('Cl', 0), ('Br', 0), ('I', 0)],
    (1, 1, 1, 1, 1, 1, 1): [('Cl', 0), ('Br', 0), ('I', 0)]
}
isosteres = {(*bs, rp): [x for x in rps if x[0] != rp] for bs, rps in isosteres.items() for rp, _ in rps}


def collate_permuted_reactions(batch) -> Tuple[TensorType['batch', 'atoms', int],
                                               TensorType['batch', 'atoms', int],
                                               TensorType['batch', 'atoms', 'atoms', int],
                                               TensorType['batch', 'atoms', int],
                                               TensorType['batch*atoms', int]]:
    """
    Prepares batches of permuted reactions.

    :return: atoms, neighbors, distances, atoms roles, and atoms replacement legend.

    Note: cls and padding not included into legend.
    """
    return *collate_reactions([x[:4] for x in batch]), cat([x[-1] for x in batch])


class PermutedReactionDataset(Dataset):
    def __init__(self, reactions: Sequence[Union[ReactionContainer, bytes]], *, rate: float = .15,
                 only_product: bool = False, distance_cutoff: int = 10, add_cls: bool = True,
                 add_molecule_cls: bool = True, symmetric_cls: bool = True,
                 disable_components_interaction: bool = False, hide_molecule_cls: bool = True, unpack: bool = False):
        """
        Prepare reactions with permuted atoms.
        Organic atoms with valence <= 4 can be randomly replaced by carbon.
        Carbons with valence 1,2 and methane can be replaced by oxygen, with valence 3,4 by nitrogen.
        5-valent atoms replaced by P, P(V) > Cl
        6-valent by S, S > Se
        7-valent by Cl, Cl > I.

        :param rate: probability of replacement
        :param only_product: replace only product atoms

        See ReactionDataset for other params description.
        """
        self.rate = rate
        self.only_product = only_product
        self.reactions = reactions
        self.distance_cutoff = distance_cutoff
        self.add_cls = add_cls
        self.add_molecule_cls = add_molecule_cls
        self.symmetric_cls = symmetric_cls
        self.disable_components_interaction = disable_components_interaction
        self.hide_molecule_cls = hide_molecule_cls
        self.unpack = unpack

    def __len__(self):
        return len(self.reactions)

    def __getitem__(self, item: int) -> Tuple[TensorType['atoms', int], TensorType['atoms', int],
                                              TensorType['atoms', 'atoms', int], TensorType['atoms', int],
                                              TensorType['atoms', int]]:
        r = ReactionContainer.unpack(self.reactions[item]) if self.unpack else self.reactions[item].copy()

        labels = []
        for m in (r.products if self.only_product else r.molecules()):
            bonds = m._bonds
            hgs = m._hydrogens
            for n, a in m.atoms():
                k = sorted(x.order for x in bonds[n].values())
                k.append(a.atomic_symbol)
                if (p := isosteres.get(tuple(k))) and random() < self.rate:
                    s, h = choice(p)
                    a.__class__ = Element.from_symbol(s)
                    hgs[n] = h
                    labels.append(0)  # Fake atom
                else:
                    labels.append(1)  # True atom
        return *ReactionDataset((r,), distance_cutoff=self.distance_cutoff, add_cls=self.add_cls,
                                add_molecule_cls=self.add_molecule_cls, symmetric_cls=self.symmetric_cls,
                                disable_components_interaction=self.disable_components_interaction,
                                hide_molecule_cls=self.hide_molecule_cls)[0], LongTensor(labels)


__all__ = ['PermutedReactionDataset', 'collate_permuted_reactions']

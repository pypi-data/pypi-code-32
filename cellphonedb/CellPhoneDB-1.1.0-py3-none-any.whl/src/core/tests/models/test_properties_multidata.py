from unittest import TestCase

import pandas as pd

from src.core.models.multidata import multidata_properties


class TestPropertiesMultidata(TestCase):
    def test_can_be_ligand(self):
        multidatas = pd.DataFrame(multidatas_fixtures)

        for index, multidata in multidatas.iterrows():
            self.assertEqual(multidata_properties.can_be_ligand(multidata), multidata['can_be_ligand'],
                             'Multidata {} cant be ligand didnt match'.format(multidata['id']))

    def test_can_be_receptor(self):
        multidatas = pd.DataFrame(multidatas_fixtures)
        for index, multidata in multidatas.iterrows():
            self.assertEqual(multidata_properties.can_be_receptor(multidata), multidata['can_be_receptor'],
                             'Multidata {} can be receptor didnt match')


multidatas_fixtures = [
    {
        'id': 1,
        'receptor': True,
        'secretion': True,
        'other': False,
        'transmembrane': False,
        'extracellular': False,
        'cytoplasm': False,
        'transporter': False,
        'is_receptor': False,
        'secreted_highlight': True,
        'can_be_ligand': True,
        'can_be_receptor': True

    },
    {
        'id': 2,
        'receptor': True,
        'secretion': False,
        'other': True,
        'transmembrane': True,
        'extracellular': True,
        'cytoplasm': False,
        'transporter': False,
        'is_receptor': True,
        'secreted_highlight': False,
        'can_be_ligand': False,
        'can_be_receptor': False

    },
    {
        'id': 3,
        'receptor': True,
        'secretion': False,
        'other': False,
        'transmembrane': False,
        'extracellular': False,
        'cytoplasm': False,
        'transporter': True,
        'is_receptor': False,
        'secreted_highlight': False,
        'can_be_ligand': False,
        'can_be_receptor': False
    },
    {
        'id': 4,
        'receptor': False,
        'secretion': False,
        'other': False,
        'transmembrane': True,
        'extracellular': False,
        'cytoplasm': False,
        'transporter': False,
        'is_receptor': False,
        'secreted_highlight': False,
        'can_be_ligand': False,
        'can_be_receptor': False
    },
]

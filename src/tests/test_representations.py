from representations.numerical import nncr
from compression_distances.cdm import CDM
from compression_algos.custom_impasse import Impasse
import matplotlib.pyplot as plt
import unittest

METRIC = CDM()
COMPRESSOR = Impasse

class TestNaturalNumberCompressionRepresentation(unittest.TestCase):
    def test_functionnality(self):
        self.assertEqual(len(nncr(25)), 25)
        self.assertEqual(len(nncr(-15)),30)
        self.assertEqual(len(nncr(0)), 0)

    def test_different_compression_length(self):
        self.assertLess(METRIC.dist(COMPRESSOR, nncr(3), nncr(4), break_string=True), METRIC.dist(COMPRESSOR, nncr(3), nncr(50), break_string=True))
        #self.assertLess(METRIC.dist(COMPRESSOR, nncr(5), nncr(5), break_string=True), METRIC.dist(COMPRESSOR, nncr(4), nncr(-14), break_string=True))
        #self.assertLess(METRIC.dist(COMPRESSOR, nncr(3), nncr(4), break_string=True), METRIC.dist(COMPRESSOR, nncr(3), nncr(5), break_string=True))
        

    def test_compression_deltas(self):
        deltas = []
        x = range(100)
        for i in x:
            deltas.append(METRIC.dist(COMPRESSOR,nncr(i),nncr(i+1), True))
        fig, ax = plt.subplots()

        ax.plot(x, deltas)

        ax.set(xlabel='Chiffre', ylabel='Delta distance au prochain chiffre',
        title='Calcul des "dérivées" de distance de compression des représentations numériques')
        ax.grid()

        #fig.savefig("./tests/plots/compression_deltas.png")

    def test_compression_distances(self):
            number = 50
            deltas = []
            x = range(100)
            for i in x:
                deltas.append(METRIC.dist(COMPRESSOR,nncr(number),nncr(i), True))
            fig, ax = plt.subplots()
    
            ax.plot(x, deltas)
    
            ax.set(xlabel='Chiffre', ylabel='Distance de ' + str(number),
            title='Distance entre valeurs numériques et ' + str(number))
            ax.grid()
    
            fig.savefig("./tests/plots/compression_distance_to" + str(number) + ".png")


def run_tests():
    unittest.main()
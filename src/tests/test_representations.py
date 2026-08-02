from representations.numerical import nncr
from compression_distances.cdm import CDM
from compression_algos.custom_impasse import Impasse
from compression_algos.legacy_lzw import LZW
import matplotlib.pyplot as plt
import unittest


class TestNaturalNumberCompressionRepresentationImpasse(unittest.TestCase):

    def __init__(self, methodName = "runTest"):
        self.METRIC = CDM()
        self.COMPRESSOR = Impasse
        super().__init__(methodName)
        
    def test_functionnality(self):
        self.assertEqual(len(nncr(25)), 25)
        self.assertEqual(len(nncr(-15)),30)
        self.assertEqual(len(nncr(0)), 0)

    def test_different_compression_length(self):
        self.assertLess(self.METRIC.dist(self.COMPRESSOR, nncr(3), nncr(4), break_string=True), self.METRIC.dist(self.COMPRESSOR, nncr(3), nncr(50), break_string=True))
        #self.assertLess(METRIC.dist(COMPRESSOR, nncr(5), nncr(5), break_string=True), METRIC.dist(COMPRESSOR, nncr(4), nncr(-14), break_string=True))
        #self.assertLess(METRIC.dist(COMPRESSOR, nncr(3), nncr(4), break_string=True), METRIC.dist(COMPRESSOR, nncr(3), nncr(5), break_string=True))
        

    def test_compression_deltas(self):
        deltas = []
        x = range(100)
        for i in x:
            deltas.append(self.METRIC.dist(self.COMPRESSOR,nncr(i),nncr(i+1), True))
        fig, ax = plt.subplots()

        ax.plot(x, deltas)

        ax.set(xlabel='Chiffre', ylabel='Delta distance au prochain chiffre',
        title='Calcul des "dérivées" de distance de compression des représentations numériques')
        ax.grid()

        #fig.savefig("./tests/plots/compression_deltas_lzw.png")

    def test_compression_distances(self):
            number = 50
            deltas = []
            x = range(100)
            for i in x:
                deltas.append(self.METRIC.dist(self.COMPRESSOR,nncr(number),nncr(i), True))
            fig, ax = plt.subplots()
    
            ax.plot(x, deltas)
    
            ax.set(xlabel='Chiffre', ylabel='Distance de ' + str(number),
            title='Distance entre valeurs numériques et ' + str(number))
            ax.grid()
    
            fig.savefig("./tests/plots/compression_distance_to" + str(number) + "_impasse.png")

class TestNaturalNumberCompressionRepresentationLZW(unittest.TestCase):

    def __init__(self, methodName = "runTest"):
        self.METRIC = CDM()
        self.COMPRESSOR = LZW()
        super().__init__(methodName)
        
    def test_compression_deltas(self):
        deltas = []
        x = range(-1000,1000)
        for i in x:
            deltas.append(self.METRIC.d(self.COMPRESSOR,x=nncr(i),y=nncr(i+1), break_string=True))
        fig, ax = plt.subplots()

        ax.plot(x, deltas)

        ax.set(xlabel='Chiffre', ylabel='Delta distance au prochain chiffre',
        title='Deltas de compression des représentations numériques LZW')
        ax.grid()

        fig.savefig("./tests/plots/compression_deltas_lzw.png")

    def test_compression_distances(self):
            for number in [1,50,100]:
                deltas = []
                x = range(-100,100)
                for i in x:
                    deltas.append(self.METRIC.d(self.COMPRESSOR,x=nncr(number),y=nncr(i), break_string=True))
                fig, ax = plt.subplots()

                ax.plot(x, deltas)

                ax.set(xlabel='Chiffre', ylabel='Distance de ' + str(number),
                title='Distance entre valeurs numériques et ' + str(number))
                ax.grid()

                fig.savefig("./tests/plots/compression_distance_to" + str(number) + "_lzw.png")



def run_tests():
    unittest.main()
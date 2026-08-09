from representations.numerical import nncr, progress_bar
from compression_distances.cdm import CDM
from compression_distances.unproven_cd import UNPROVEN_CD
from compression_algos.custom_impasse import Impasse
from compression_algos.legacy_lzw import LZW
from compression_algos.legacy_lz78_worst_case import LZ78_WORST_CASE
import matplotlib.pyplot as plt
import unittest


class TestNaturalNumberCompressionRepresentationImpasse(unittest.TestCase):

    def __init__(self, methodName = "runTest"):
        self.METRIC = CDM()
        self.COMPRESSOR = LZ78_WORST_CASE
        super().__init__(methodName)
        
    def test_functionnality(self):
        self.assertEqual(len(nncr(25)), 25)
        self.assertEqual(len(nncr(-15)),30)
        self.assertEqual(len(nncr(0)), 0)

    def test_different_compression_length(self):
        self.assertLess(self.METRIC.dist(self.COMPRESSOR, nncr(3), nncr(4), break_string=True), self.METRIC.dist(self.COMPRESSOR, '3', '13', break_string=True))
        self.assertLess(self.METRIC.dist(self.COMPRESSOR, nncr(4), nncr(8), break_string=True), self.METRIC.dist(self.COMPRESSOR, '300', '-118', break_string=True))
        self.assertLess(self.METRIC.dist(self.COMPRESSOR, nncr(15), nncr(20), break_string=True), self.METRIC.dist(self.COMPRESSOR, '10', '16', break_string=True))
        

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
        self.METRIC = UNPROVEN_CD() #CDM()
        self.COMPRESSOR = LZW()
        self.REPRESENTATION = progress_bar
        self.algo = 'LZW'
        self.metric = 'UNPROVEN_CD'
        self.representation = 'progress_bar'
        super().__init__(methodName)
        
    def test_compression_deltas(self):
        deltas = []
        x = range(-1000,1000)
        for i in x:
            deltas.append(self.METRIC.d(self.COMPRESSOR,x=self.REPRESENTATION(i),y=self.REPRESENTATION(i+1), break_string=True))
        fig, ax = plt.subplots()

        ax.plot(x, deltas)

        ax.set(xlabel='Valeur', ylabel='Delta prochaine valeur',
        title='Deltas nncr, {algo}, {metric}, {representation}'.format(algo=self.algo, metric = self.metric,representation=self.representation))
        ax.grid()

        fig.savefig("./tests/plots/{algo}_{metric}_{representation}_compression_deltas.png".format(algo=self.algo,metric=self.metric,representation=self.representation))

    def test_compression_distances(self):
            for number in [1,50,100]:
                deltas = []
                x = range(-100,100)
                for i in x:
                    deltas.append(self.METRIC.d(self.COMPRESSOR,x=self.REPRESENTATION(number),y=self.REPRESENTATION(i), break_string=True))
                fig, ax = plt.subplots()

                ax.plot(x, deltas)

                ax.set(xlabel='Chiffre', ylabel='Distance de ' + str(number),
                title='D( x, ' + str(number) + '): {algo}, {metric}, {representation}'.format(algo=self.algo,metric=self.metric,representation=self.representation))
                ax.grid()

                fig.savefig("./tests/plots/{algo}_{metric}_{representation}_compression_distance_to".format(algo=self.algo,metric=self.metric,representation=self.representation) + str(number) + ".png")


class TestNaturalNumberCompressionRepresentationLZ78_WORST_CASE(unittest.TestCase):

    def __init__(self, methodName = "runTest"):
        self.METRIC = UNPROVEN_CD() #CDM()
        self.COMPRESSOR = LZ78_WORST_CASE()
        self.REPRESENTATION = nncr
        self.algo = 'LZ78_WORST_CASE'
        self.metric = 'UNPROVEN_CD'
        self.representation = 'nncr'
        super().__init__(methodName)
        
    def test_compression_deltas(self):
        deltas = []
        x = range(-1000,1000)
        for i in x:
            deltas.append(self.METRIC.d(self.COMPRESSOR,x=self.REPRESENTATION(i),y=self.REPRESENTATION(i+1), break_string=True))
        fig, ax = plt.subplots()

        ax.plot(x, deltas)

        ax.set(xlabel='Valeur', ylabel='Delta prochaine valeur',
        title='Deltas nncr, {algo}, {metric}, {representation}'.format(algo=self.algo, metric = self.metric, representation=self.representation))
        ax.grid()

        fig.savefig("./tests/plots/{algo}_{metric}_{representation}_compression_deltas.png".format(algo=self.algo,metric=self.metric,representation=self.representation))

    def test_compression_distances(self):
            for number in [1,50,100]:
                deltas = []
                x = range(-100,100)
                for i in x:
                    deltas.append(self.METRIC.d(self.COMPRESSOR,x=self.REPRESENTATION(number),y=self.REPRESENTATION(i), break_string=True))
                fig, ax = plt.subplots()

                ax.plot(x, deltas)

                ax.set(xlabel='Chiffre', ylabel='Distance de ' + str(number),
                title='D( x, ' + str(number) + '): {algo}, {metric}, {representation}'.format(algo=self.algo,metric=self.metric, representation=self.representation))
                ax.grid()

                fig.savefig("./tests/plots/{algo}_{metric}_{representation}_compression_distance_to".format(algo=self.algo,metric=self.metric,representation=self.representation) + str(number) + ".png")



def run_tests():
    unittest.main()
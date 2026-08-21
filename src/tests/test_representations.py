from representations.numerical import nncr, progress_bar
from compression_distances.cdm import CDM
from compression_distances.ncd import NCD
from compression_distances.clm import CLM
from compression_distances.unproven_cd import UNPROVEN_CD
from compression_algos.custom_impasse import Impasse
from compression_algos.legacy_lzw import LZW
from compression_algos.legacy_lz78_worst_case import LZ78_WORST_CASE
import matplotlib.pyplot as plt
import unittest


class TestNaturalNumberCompressionRepresentationImpasse(unittest.TestCase):

    def __init__(self, methodName = "runTest"):
        self.METRIC = CDM()
        self.COMPRESSOR = LZ78_WORST_CASE()
        super().__init__(methodName)
        
    def test_functionnality(self):
        self.assertEqual(len(nncr(25)), 25)
        self.assertEqual(len(nncr(-15)),30)
        self.assertEqual(len(nncr(0)), 0)

    def test_different_compression_length(self):
        pass
        #self.assertLess(self.METRIC.dist(self.COMPRESSOR, nncr(3), nncr(4), break_string=True), self.METRIC.dist(self.COMPRESSOR, '3', '13', break_string=True))
        #self.assertLess(self.METRIC.dist(self.COMPRESSOR, nncr(4), nncr(8), break_string=True), self.METRIC.dist(self.COMPRESSOR, '300', '-118', break_string=True))
        #self.assertLess(self.METRIC.dist(self.COMPRESSOR, nncr(15), nncr(20), break_string=True), self.METRIC.dist(self.COMPRESSOR, '10', '16', break_string=True))
        

class TestNaturalNumberCompressionRepresentationLZW(unittest.TestCase):

    def __init__(self, methodName = "runTest"):
        self.METRICS = [(NCD(), 'NCD'), (CDM(), 'CDM'), (CLM(), 'CLM')]#, (UNPROVEN_CD(), 'UnprovenCD')]
        self.COMPRESSORS = [(LZW(), 'LZW'), (LZ78_WORST_CASE(), 'LZ78_Pire_Cas')]#, (Impasse(), 'Impasse')]
        self.REPRESENTATIONS = [(progress_bar, 'Progress Bar'), (nncr, 'NNCR')]
        super().__init__(methodName)
        
    def test_compression_deltas(self):
        range_min = -1000
        range_max = 1000
        range_str = '[' + str(range_min) + ', ' + str(range_max) + ')'

        for compressor, compressor_name in self.COMPRESSORS:
            for representation, rep_name in self.REPRESENTATIONS:
                fig, ax = plt.subplots()
                for metric, metric_name in self.METRICS:
                    deltas = []
                    x = range(range_min,range_max)
                    for i in x:
                        if (representation == progress_bar):
                            deltas.append(metric.d(compressor,x=representation(i,max=range_max,min=range_min),y=representation(i+1,max=range_max,min=range_min), break_string=True))
                        else:
                            deltas.append(metric.d(compressor,x=representation(i),y=representation(i+1), break_string=True))
                    ax.plot(x, deltas, label=metric_name, alpha=0.8)

                ax.set(xlabel='Valeur', ylabel='Delta successeur',
                title='Deltas, {algo}, {representation} {range_str}'.format(algo=compressor_name,representation=rep_name, range_str=range_str))
                ax.legend(loc='best')
                ax.grid()

                fig.savefig("./tests/plots/combined/{algo}_{representation}_{range_str}_compression_deltas.png".format(algo=compressor_name,representation=rep_name, range_str=range_str))

    def test_compression_distances(self):
        range_min = -100
        range_max = 100
        range_str = '[' + str(range_min) + ', ' + str(range_max) + ')'
        numbers = [range_min, -50, 1, 50, range_max]

        for compressor, compressor_name in self.COMPRESSORS:

            for representation, rep_name in self.REPRESENTATIONS:

                for metric, metric_name in self.METRICS:
                    fig, ax = plt.subplots()
                    for number in numbers:
                        deltas = []
                        x = range(range_min,range_max)
                        for i in x:
                            if (representation == progress_bar):
                                deltas.append(metric.d(compressor,x=representation(i,max=range_max,min=range_min),y=representation(number,max=range_max,min=range_min), break_string=True))
                            else:
                                deltas.append(metric.d(compressor,x=representation(i),y=representation(number), break_string=True))


                        ax.plot(x, deltas, label=metric_name+'(x,'+str(number)+')', alpha=0.5)

                    ax.set(xlabel='x', ylabel='D(x, ' + str(number) + ')',
                    title='D( x, y): {algo}, {metric}, {representation}, {range_str}'.format(algo=compressor_name,representation=rep_name, metric=metric_name,range_str=range_str))
                    ax.grid()
                    ax.legend(loc='best')

                    fig.savefig("./tests/plots/combined/{algo}_{representation}_{metric}_compression_distance_to".format(algo=compressor_name,metric=metric_name,representation=rep_name) + ".png")



def run_tests():
    unittest.main()
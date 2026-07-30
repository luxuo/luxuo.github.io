from representations.numerical import nncr
from compression_distances.clm import CLM
from compression_algos.custom_impasse import Impasse
import unittest

class TestNaturalNumberCompressionRepresentation(unittest.TestCase):
    def test_functionnality(self):
        self.assertEqual(len(nncr(25)), 25)
        self.assertEqual(len(nncr(-15)),30)
        self.assertEqual(len(nncr(0)), 0)

    def test_different_compression_length(self):
        compressor = Impasse
        metric = CLM()
        self.assertLess(metric.dist(compressor, nncr(3), nncr(14), break_string=True), metric.dist(compressor, nncr(3), nncr(50), break_string=True))
        self.assertLess(metric.dist(compressor, nncr(3), nncr(3), break_string=True), metric.dist(compressor, nncr(3), nncr(-3), break_string=True))
        #self.assertLess(metric.dist(compressor, nncr(3), nncr(4), break_string=True), metric.dist(compressor, nncr(3), nncr(5), break_string=True))
        deltas = []
        for i in range(14):
            deltas.append(metric.dist(compressor,nncr(i),nncr(i+1), True))
        print(deltas)
        deltas = []
        for i in range(14):
            deltas.append(metric.dist(compressor,nncr(3),nncr(i), True))
        print(deltas)

def run_tests():
    unittest.main()
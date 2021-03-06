from Hilbert import Hilbert
import unittest
import os

class HilbertTest(unittest.TestCase):

    def setUp(self):
        refDir = os.path.dirname(os.getcwd())
        refNumStr = '103'
        refInFileDir = os.path.join(refDir, refNumStr, 'Input.csv')
        refOutFileDir = os.path.join(refDir, refNumStr, 'HilbertOutput.csv')
        resOutFileDir = os.path.join(refDir, refNumStr, 'HilbertResultsPython.csv')

        self.samplingFreq = 360.0

        self.refInFile = open(refInFileDir, 'r')
        self.refOutFile = open(refOutFileDir, 'r')
        self.resultFile = open(resOutFileDir, 'w')
        self.refInVector = []
        self.refOutVector = []
        self.resultVector = []
        self.refIntSignalVector = []
        self.refMarksVector = []

    def tearDown(self):
        self.refInFile.close()
        self.refOutFile.close()
        self.resultFile.close()

    def loadReferenceData(self):
        refInVectorStr = self.refInFile.readline().split(',')
        del refInVectorStr[-1]
        for item in refInVectorStr:
            val = float(item)
            self.refInVector.append(val)

        refOutVectorStr = self.refOutFile.readline().split(',')
        del refOutVectorStr[-1]
        for item in refOutVectorStr:
            val = int(float(item))
            self.refOutVector.append(val)

    def runAlgorithm(self):
        self.alg = Hilbert(self.refInVector, samplingFrequency=self.samplingFreq)
        self.resultVector = self.alg.process()
        for val in self.resultVector or []:
            self.resultFile.write('%d\n' % val)

    def isResultIdentical(self):
        result = True

        for ref, res in zip(self.refOutVector, self.resultVector):
            print '{} {}'.format(ref, res)
            if ref != res:
                print 'reference ({}) and result ({}) are not equal'.format(ref, res)
                result = False

        return result

    def testAlgorithm(self):
        self.loadReferenceData()
        self.runAlgorithm()

        self.assertTrue(self.isResultIdentical(), 'Reference vector and result vector are not identical')

if __name__ == '__main__':
    unittest.main()

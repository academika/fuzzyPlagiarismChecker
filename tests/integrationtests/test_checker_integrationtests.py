from checker.main import calculateResult
from pytest import mark


@mark.integration
class IntegrationTests:
    def test_cmpFile2Dir_expectOneSimilarFile(self):
        result = calculateResult(['--usecase', 'cmpFile2Dir', '--file1', './resources/copyOfSimpleFile.html', '--dir', './resources'])
        assert '/simpleFile.html' in result

    def test_cmpFile2Dir_expectNoSimilarFiles(self):
        assert calculateResult(['--usecase', 'cmpFile2Dir', '--file1', './pytest.ini', '--dir', './resources']) == []

    def test_cmpTwoFiles_expect100Similarity(self):
        assert calculateResult(['--usecase', 'cmpTwoFiles', '--file1', './resources/copyOfSimpleFile.html', '--file2', './resources/simpleFile.html']) == 100

    def test_cmpTwoFiles_expect0Similarity(self):
        assert calculateResult(['--usecase', 'cmpTwoFiles', '--file1', './resources/copyOfSimpleFile.html', '--file2', './resources/textFile.txt']) == 0

    def test_checkStructure_expectTrue(self):
        assert calculateResult(['--usecase', 'checkStructure', '--file1', './resources/simpleFile.html', '--structureFile', './resources/simpleStructure.txt'])

    def test_checkStructure_expectFalse(self):
        assert calculateResult(['--usecase', 'checkStructure', '--file1', './resources/simpleFile.html', '--structureFile', './resources/complicatedStructure.txt']) == (False, 0)

    def test_checkStructureDir_expectTrue(self):
        assert calculateResult(['--usecase', 'checkStructureDir', '--dir', './resources/toTestDirStructureTheSame', '--structureFile', './resources/simpleStructure.txt'])

    def test_checkStructureDir_expectFileToNotConformTheStructure(self):
        result = calculateResult(['--usecase', 'checkStructureDir', '--dir', './resources/toTestDirStructureTheSame', '--structureFile', './resources/complicatedStructure.txt'])
        expectedFile = 'simpleFile.html'
        assert expectedFile in result

    def test_cmpFilesInDir_expectTwoFIlesSame(self):
        result = calculateResult(['--usecase', 'cmpFilesInDir', '--dir', './resources'])
        expectedFile = '/simpleFile.html'
        expectedFile2 = '/copyOfSimpleFile.html'
        assert expectedFile in result or expectedFile2 in result

    def test_cmpFilesInDir_expectNoSameFiles(self):
        result = calculateResult(['--usecase', 'cmpFilesInDir', '--dir', './resources/toTestRestrictedFiles'])
        assert result == {}

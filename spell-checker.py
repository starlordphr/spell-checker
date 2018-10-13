import sys
import jamspell

class FileStats:
    def __init__(self, location):
        self.fileLocation = location
        self.fileContent = ""

    def readFile(self):
        fileObject = open(self.fileLocation, 'r')
        self.fileContent = fileObject.read()

    def spellCorrect(self):
        corrector = jamspell.TSpellCorrector()
        corrector.LoadLangModel('en.bin')

        output = corrector.FixFragment(self.fileContent)
        return output


if __name__ == "__main__":

    fileObject = FileStats(sys.argv[1])
    fileObject.readFile()

    corrected = fileObject.spellCorrect()

    print "##### ORIGINAL TEXT #####"
    print fileObject.fileContent

    print "\n\n##### CORRECTED TEXT #####"
    print corrected

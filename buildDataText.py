import os
import settings
from sklearn.model_selection import train_test_split
import glob


class FileReader(object):
    def __init__(self, filePath, encoder=None):
        self.filePath = filePath
        self.encoder = encoder if encoder != None else 'utf-16le'

    def read(self):
        with open(self.filePath) as f:
            s = f.read()
        return s

    def content(self):
        s = self.read()
        return s


class FileStore(object):
    def __init__(self, filePath=None, data=None):
        self.filePath = filePath
        self.data = data

    def StoreTextUnit(self, list):
        for index, value in enumerate(list):
            name_file = self.filePath + '/NH_(' + str(index) + ').txt'
            with open(name_file, 'w') as output:
                output.write(value)


if __name__ == '__main__':
    print('Reading Data Raw')
    json_train = FileReader(filePath=settings.DATA_SPLIT_PATH).content()
    X_train, X_test = train_test_split(json_train.split('\n'), test_size=0.3)
    train_files = glob.glob(settings.DATA_TRAIN_LABEL + '/*')
    for f in train_files:
        os.remove(f)
    test_files = glob.glob(settings.DATA_TEST_LABEL + '/*')
    for f in test_files:
        os.remove(f)
    FileStore(filePath=settings.DATA_TRAIN_LABEL).StoreTextUnit(X_train)
    FileStore(filePath=settings.DATA_TEST_LABEL).StoreTextUnit(X_test)

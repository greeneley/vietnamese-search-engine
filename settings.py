import os
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_TRAIN_PATH = os.path.join(DIR_PATH, 'data/Viettel/train/')
DATA_TEST_PATH = os.path.join(DIR_PATH, 'data/Viettel/test/')
DATA_TRAIN_JSON = os.path.join(DIR_PATH, 'processed_data/data_train.json')
DATA_TEST_JSON = os.path.join(DIR_PATH, 'processed_data/data_test.json')
FEATURES_TEST = os.path.join(DIR_PATH, 'feature_extraction/feature_test_full.pkl')
FEATURES_TRAIN = os.path.join(DIR_PATH, 'feature_extraction/feature_train_full.pkl')
VECTOR_EMBEDDING = os.path.join(DIR_PATH, 'vector_embedding/vector_embedding_full.pkl')
STOP_WORDS = os.path.join(DIR_PATH, 'stopwords-nlp-vi.txt')
SPECIAL_CHARACTER = '0123456789%@$.,=+-!;/()*"&^:#|\n\t\''
DICTIONARY_PATH = 'dictionary.txt'
TOKEN = 'f68f98d802ba6c0a60ee9dc44c47f48c'
THRESHOLD = 0.7
# ======= Khách Sạn =======
# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/khachsan.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Khach San')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Khách Sạn')

# ======= NHA HANG ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/nhahang.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Nhà Hàng')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Nhà Hàng')

# ======= Quán Cà Phê ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/quancaphe.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Quán Cà Phê')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Quán Cà Phê')

# ======= ATM ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/atm.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/ATM')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/ATM')

# ======= Siêu thị ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/sieuthi.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Siêu Thị')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Siêu Thị')

# ======= Ăn vặt, vỉa hè ========

DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/anvat.txt')
DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/An Vat Via He')
DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/An Vat Via He')

# ======= Ngân hàng ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/nganhang.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Ngân Hàng')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Ngân Hàng')

# ======= Bưu điện ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/buudien.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Buu Dien')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Buu Dien')
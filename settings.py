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

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/anvat.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/An Vat Via He')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/An Vat Via He')

# ======= Ngân hàng ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/nganhang.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Ngân Hàng')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Ngân Hàng')

# ======= Bưu điện ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/buudien.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Buu Dien')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Buu Dien')

# # ======= Tòa nhà  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/toanha.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Tòa Nhà')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Tòa Nhà')

# ======= Chung cư  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/chungcu.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Chung cư')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Chung cư')

# # ======= Nhà thờ  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/nhatho.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Nhà Thờ')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Nhà Thờ')

# # ======= Nghĩa trang  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/nghiatrang.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Nghĩa Trang')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Nghĩa Trang')

# # ======= Đài Tưởng Niệm Liệt Sĩ  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/lietsy.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Đài Tưởng Niệm Liệt Sĩ')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Đài Tưởng Niệm Liệt Sĩ')

# # ======= Rừng Quốc Gia  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/rungquocgia.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Rừng Quốc Gia')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Rừng Quốc Gia')


# ======= Chùa  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/chua.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Chùa')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Chùa')

# # ======= Khu bảo tồn  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/khubaoton.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Khu Bảo Tồn')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Khu Bảo Tồn')

# ======= Khu du lich  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/khudulich.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Khu Du Lịch')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Khu Du Lịch')


# # ======= Điểm đỗ xe  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/diemdauxe.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Điểm Đỗ Xe')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Điểm Đỗ Xe')

# # ======= Showroom oto  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/showroom.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/showroom ô tô')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/showroom ô tô')


# # ======= Dịch Vụ Thuê Xe  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/dichvuthuexe.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Dịch Vụ Thuê Xe')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Dịch Vụ Thuê Xe')

# # ======= Tiệm Rửa Sửa Xe  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/tiemruasuaxe.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Tiệm Rửa Sửa Xe')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Tiệm Rửa Sửa Xe')


# # ======= Garage  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/garage.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Garage')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Garage')


# ======= Garage  ========

DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/tramxang.txt')
DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Trạm Xăng')
DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Trạm Xăng')

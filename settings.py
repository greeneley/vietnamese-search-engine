import os
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_TRAIN_PATH = os.path.join(DIR_PATH, 'data/Viettel/train/')
DATA_TEST_PATH = os.path.join(DIR_PATH, 'data/Viettel/test/')
DATA_TRAIN_JSON = os.path.join(DIR_PATH, 'processed_data/data_train.json')
DATA_TEST_JSON = os.path.join(DIR_PATH, 'processed_data/data_test.json')
FEATURES_TEST = os.path.join(
    DIR_PATH, 'feature_extraction/feature_test_full.pkl')
FEATURES_TRAIN = os.path.join(
    DIR_PATH, 'feature_extraction/feature_train_full.pkl')
VECTOR_EMBEDDING = os.path.join(
    DIR_PATH, 'vector_embedding/vector_embedding_full.pkl')
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


# # ======= Trạm Xăng  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/tramxang.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Trạm Xăng')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Trạm Xăng')


# # ======= DV Quảng Cáo  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/dvquangcao.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Dịch Vụ Quảng Cáo')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Dịch Vụ Quảng Cáo')

# # ======= Thẩm Mỹ Viện  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/thammyvien.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Thẩm Mỹ Viện')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Thẩm Mỹ Viện')

# # ======= Nhà May  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/nhamay.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Nhà May')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Nhà May')

# # ======= Tiệm Mỹ Phẩm  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/tiemmypham.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Tiệm Mỹ Phẩm')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Tiệm Mỹ Phẩm')

# # ======= Đồ Nội Thất  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/donoithat.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Đồ Nội Thất')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Đồ Nội Thất')

# # ======= Cửa hàng mắt kính  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/matkinh.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Cửa Hàng Mắt Kính')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Cửa Hàng Mắt Kính')

# # ======= Cắt tóc  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/cattoc.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Cắt Tóc')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Cắt Tóc')

# # ======= Massage  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/massage.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Massage')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Massage')

# # ======= Spa  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/spa.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Spa')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Spa')

# # ======= Ảnh Viện Áo Cưới  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/anhvienaocuoi.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Ảnh Viện Áo Cưới')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Ảnh Viện Áo Cưới')

# # ======= Cafe  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/cafe.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Cafe')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Cafe')


# # ======= Khu Công Nghiệp  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/khucongnghiep.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Khu Công Nghiệp')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Khu Công Nghiệp')

# # ======= Công Ty Luật  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/congtyluat.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Công Ty Luật')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Công Ty Luật')

# # ======= Dịch Vu Cầm Đồ  ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/dichvucamdo.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Dịch Vụ Cầm Đồ')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Dịch Vụ Cầm Đồ')

# # ======= Trung Tâm Bảo Hành ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/trungtambaohanh.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Trung Tâm Bảo Hành')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Trung Tâm Bảo Hành')

# # ======= Trường Cao Đẳng ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/caodang.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Trường Cao Đẳng')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Trường Cao Đẳng')

# # ======= Trường THPT ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/thpt.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Trường THPT')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Trường THPT')

# # ======= Trường mầm non ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/mamnon.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Trường Mầm Non')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Trường Mầm Non')

# # ======= Trường Tiểu Học ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/tieuhoc.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Tiểu Học')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Tiểu Học')

# # ======= Trường THCS ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/thcs.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/THCS')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/THCS')

# # ======= Trường Đại Học ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/daihoc.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Đại Học')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Đại Học')

# # ======= Cửa Hàng Băng Đĩa ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/cuahangbangdia.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Cửa Hàng Băng Đĩa')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Cửa Hàng Băng Đĩa')

# # ======= Rạp chiếu phim ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/rapchieuphim.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Rạp Chiếu Phim')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Rạp Chiếu Phim')

# # ======= Cửa Hàng Tranh ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/cuahangtranh.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Cửa Hàng Tranh')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Cửa Hàng Tranh')

# # ======= Tiệm Internet ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/tieminternet.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Tiệm Internet')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Tiệm Internet')
# # ======= Quán Karaoke ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/karaoke.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Quán Karaoke')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Quán Karaoke')

# # ======= Xổ số ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/xoso.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Xổ Số')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Xổ Số')


# # ======= Bảo tàng ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/baotang.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Bảo Tàng')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Bảo Tàng')

# # ======= Bar Pub ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/barpub.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Bar Pub')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Bar Pub')

# # =======Nhà Hát ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/nhahat.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Nhà Hát')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Nhà Hát')

# # ======= Múa Rối ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/muaroi.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Múa Rối')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Múa Rối')

# # ======= Đài Truyền Hình ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/daitruyenhinh.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Đài Truyền Hình')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Đài Truyền Hình')

# # ======= Đài Phát Thanh ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/daiphatthanh.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Đài Phát Thanh')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Đài Phát Thanh')

# # ======= Công Viên ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/congvien.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Công Viên')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Công Viên')

# # ======= Bảo Hiểm ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/baohiem.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Bảo Hiểm')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Bảo Hiểm')

# # ======= Đại Sứ Quán ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/daisuquan.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Đại Sứ Quán')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Đại Sứ Quán')

# # ======= Báo Chí ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/bao.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Báo Chí')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Báo Chí')

# # ======= Công An ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/congan.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Công An')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Công An')

# # ======= Doanh Trại Quân Đội ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/doanhtrai.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Doanh Trại Quân Đội')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Doanh Trại Quân Đội')

# # ======= Bệnh Viện ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/benhvien.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Bệnh Viện')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Bệnh Viện')

# # ======= Trung Tâm Y Tế ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/trungtamyte.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Trung Tâm Y Tế')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Trung Tâm Y Tế')

# # ======= Hiệu Thuốc ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/hieuthuoc.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Hiệu Thuốc')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Hiệu Thuốc')

# # ======= Phòng Khám Thú Y ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/phongkhamthuy.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Phòng Khám Thú Y')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Phòng Khám Thú Y')

# # ======= Quán Nhậu ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/quannhau.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Quán Nhậu')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Quán Nhậu')

# # ======= Tiệm Bánh ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/tiembanh.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Tiệm Bánh')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Tiệm Bánh')

# # ======= Thư Viện ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/thuvien.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Thư Viện')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Thư Viện')

# # ======= Nhà sách ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/nhasach.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Nhà Sách')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Nhà Sách')

# # ======= Chợ ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/cho.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Chợ')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Chợ')

# # ======= Trung Tâm Thương Mại ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/trungtamthuongmai.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Trung Tâm Thương Mại')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Trung Tâm Thương Mại')

# # ======= Tạp Hóa ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/taphoa.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Tạp Hóa')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Tạp Hóa')

# # ======= Bãi Biển ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/baibien.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Bãi Biển')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Bãi Biển')

# # ======= Sân Golf ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/golf.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Sân Golf')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Sân Golf')

# # ======= Vườn Hoa ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/vuonhoa.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Vườn Hoa')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Vườn Hoa')

# # ======= Bể Bơi ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/beboi.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Bể Bơi')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Bể Bơi')

# # ======= Trung Tâm Thể Thao ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/trungtamthethao.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Trung Tâm Thể Thao')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Trung Tâm Thể Thao')

# # ======= Sân Vận Động ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/sanvandong.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Sân Vận Động')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Sân Vận Động')

# # ======= Sân Bay ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/sanbay.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Sân Bay')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Sân Bay')

# # ======= Cửa Khẩu ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/cuakhau.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Cửa Khẩu')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Cửa Khẩu')

# # ======= Trạm Thu Phí ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/tramthuphi.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Trạm Thu Phí')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Trạm Thu Phí')

# # ======= Trạm Xe Buýt ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/tramxebuyt.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Trạm Xe Buýt')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Trạm Xe Buýt')

# # ======= Bến Xe ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/benxe.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Bến Xe')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Bến Xe')

# # # ======= Camera Giao Thông ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/camera.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Camera Giao Thông')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Camera Giao Thông')

# # ======= Cảng ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/cang.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Cảng')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Cảng')

# # ======= Bến Phà ========

# DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/benpha.txt')
# DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Bến Phà')
# DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Bến Phà')

# ======= Ga Tàu Hỏa ========

DATA_SPLIT_PATH = os.path.join(DIR_PATH, 'data/raw/gatauhoa.txt')
DATA_TRAIN_LABEL = os.path.join(DIR_PATH, './data/Viettel/train/Ga Tàu Hỏa')
DATA_TEST_LABEL = os.path.join(DIR_PATH, './data/Viettel/test/Ga Tàu Hỏa')

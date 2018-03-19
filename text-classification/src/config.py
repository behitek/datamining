# -*- coding: utf8 -*-
"""
Đường dẫn đến thư mục chứa dữ liệu, mỗi nhãn là một file riêng
Mỗi news là một dòng có cú pháp: <content>,<label>
"""
MASTER_DATA_DIR = "../res/master_data/"


"""
Số lượng news cần lấy cho cả train + test, nếu không đủ thì lấy tất cả news đang có
"""
NUMBER_OF_NEWS = 2000

"""
Tỷ lệ train data/ tổng số
"""
TRAIN_PERCENT = 0.8

"""
Đường dẫn lưu tệp dữ liệu train, file
"""
TRAIN_PATH = "../res/train/train.txt"

"""
Đường dẫn lưu tệp dữ liệu test, file
"""
TEST_PATH = "../res/test/test.txt"

"""
Đường dẫn lưu log chương trình
"""
LOG_MAKE_DATA = "../log/log_make_data"
LOG_TRAIN = "../log/train"

"""
Danh sách các nhãn dùng trong bài toán
"""
TARGET_NAMES = ['Giáo dục', 'Khoa học', 'Kinh doanh', 'Pháp luật', 'Sức khỏe', 'Thể Thao']

"""
Nơi lưu model sau khi train của hai thuật toán
"""
SAVE_NB_PATH = "../model/nb.pkl"
SAVE_SVM_PATH = "../model/svm.pkl"

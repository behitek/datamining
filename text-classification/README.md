# Cài đặt các package sau:
- python 3.6 x64 
```angular2html
https://www.python.org/ftp/python/3.6.4/python-3.6.4-amd64.exe
```
- Numpy, scipy, sklean
```angular2html
python -m pip install --user numpy scipy scikit-learn
```

# Các chức năng của chương trình
- Tách dữ liệu
```angular2html
Input: Đường dẫn tới thư mục chứa dữ liệu (Tạm gọi là masterdata) 
Dữ liệu đã chia mỗi nhãn thành một file. Mỗi tin tức trong file là một dòng. Không có dòng trắng. Mỗi dòng có cấu trúc: <content>,<label>
Các file ở trong cùng 1 thư mục.
Sửa MASTER_DATA_DIR, NUMBER_OF_NEWS, TRAIN_PERCENT, TRAIN_PATH, TEST_PATH ở config.py
Sau đó chạy lệnh:
python make_data.py
Output: Tách train, test thành 2 file dữ liệu riêng chia đúng theo tỷ lệ ở config.
```
- Train model + save model:
```angular2html
file load_data.py để đọc dữ liệu train và test từ 2 file train, test đã tách ở trên
file news.py - class mô tả cấu trúc dữ liệu
file train.py train model và save lại model
```

- Đọc model và test kết quả:
```angular2html
Xem guess.py
```
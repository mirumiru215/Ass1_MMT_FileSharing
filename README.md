# Assignment_1_ComputerNetwork

Phía Client(A)
-  Tải project của dự án về máy từ link Github.
-  Chạy file GUI.py
-  Nhập IP và đặt tên cho hostname của mình và nhấn "Connect".
-  Tải file (fetch): nhâp tên file muốn tải vào frame "Fetch file" và nhấn nút "FETCH".
-  Upload file (publish) nhấn nút Publish ở phía dưới danh sách các file và chọn file muốn upload.
-  Xóa file (delete) nhập tên file muốn xóa vào frame "Delete file" và nhấn nút "DELETE"
-  Thoát khỏi hệ thống (disconnect) nhấn nút "DISCONNECT" để thoát khỏi hệ thống.

Phía Server (B)
- Tải project của dự án về máy từ link Github.
- Chạy file serverFE.py
- Nhấn nút "START SERVER" để bắt đầu ứng dụng.
- Kiểm tra trạng thái của client (ping): nhập tên hostname muốn kiểm tra và nhấn nút "PING"
- Xem danh sách các file mà 1 client đang có (discover): nhập tên hostname muốn xem và nhấn nút "DISCOVER"
- Xem danh sách các client đã tham gia vào hệ thống: nhấn nút F5 để làm mới danh sách các client đã tham gia vào hệ thống.


**Note**: Khi publish file, cần copy đường dẫn từ file muốn publish. 
Ví dụ: Muốn publish file tên _test.pdf_ có đường dẫn _C:/User/Document/test.pdf_ thì gõ lệnh publish C:/User/Document test.pdf

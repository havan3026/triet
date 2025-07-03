CHƯƠNG I: CƠ SỞ DỮ LIỆU VÀ MỘT SỐ MÔ HÌNH CƠ SỞ DỮ LIỆU
I. TỔNG QUAN VỀ CƠ SỞ DỮ LIỆU
1) Tầm quan trọng của cơ sở dữ liệu
- Dư thừa và tính không nhất quán dữ liệu
- Khó khăn trong việc truy nhập dữ liệu
- Cô lập và hạn chế chia sẻ dữ liệu
- Vấn đề về an toàn
- Vấn đề về độ tin cậy
- Vấn đề về toàn vẹn
- Dị thường truy nhập dữ liệu
- Sự phục thuộc dữ liệu của chương trình ứng dụng

2) Lịch sử phát triển của cơ sở dữ liệu
-Những năm 60: mô hình dữ liệu phân cấp: cây -cha con,mỗi nút 1 cha,1 csdl=1 tập=1 rừng (Hierarchical) + mô hình dạng mạng: bdien đồ thị có hướng, sơ đồ thực thể liên kết với các liên kết hạn chế là lket hai ngôi nhiều-một, bản ghi logic(Network)
-Năm 1970: hệ cơ sở dữ liệu quan hệ (Relational) Codd, dạng bảng, thuật ngữ toán học + hướng dữ liệu
-Năm 1976: mô hình thực thể - liên kết (Entity-Relationship): bdien dữ liệu trogn tgioi thực, 3 kn: tập thực thể-hcn, tập liên kết-thoi và thuộc tính-tròn
-Những năm 1980: hướng đối tượng không tích hợp (Object-oriented DBMS)
-Những năm 1990: mô hình cơ sở tri thức giá trị có tích hợp: Oracle Database, DB2 Universal Database, SQL Server, Sybase Adaptive Server, MySQL, PostgreSQL, SQLite.
-Đầu thế kỷ 21: mô hình cơ sở dữ liệu web giá trị có tích hợp: MongoDB (NoSQL - not only SQL)

3) Các khái niệm cơ bản về cơ sở dữ liệu
- Cơ sở dữ liệu: là một bộ sưu tập các dữ liệu tác nghiệp được lưu trữ lại và được các hệ ứng dụng của một xí nghiệp cụ thể nào đó sử dụng (là sự tập hợp có tổ chức các dữ liệu có quan hệ logic với nhau)
- Một tập hợp có cấu trúc của những dữ liệu có liên quan với nhau được lưu trữ trong máy tính
+)Danh sách sinh viên, Niên giám điện thoại, Danh mục các đề án
- Một CSDL biểu diễn một phần của thế giới thực (thế giới thu nhỏ)
- CSDL được thiết kế, xây dựng, và lưu trữ với một mục đích xác định, phục vụ cho một số ứng dụng và người dùng
- Tập ngẫu nhiên của các dữ liệu không thể xem là một CSDL
- Đặc tính của CSDL: Tính tự mô tả, Tính độc lập giữa chương trình và dữ liệu, Tính trừu tượng dữ liệu, Tính nhất quán, Các cách nhìn dữ liệu

- Hệ quản trị cơ sở dữ liệu(DBMS): là một hệ thống phần mềm cho phép tạo lập cơ sở dữ liệu và điều khiển mọi truy nhập đối với cơ sở dữ liệu đó (M.Access, DB2, Informix, SQL Server, Sybase, Oracle …..) gồm 6 thành phần: Ngôn ngữ giao tiếp, từ điển dữ liệu, biện pháp bảo mật, cơ chế giải quyết tranh chấp, cơ chế sao lưu phục hồi, đảm bảo tính độc lập
-Ngôn ngữ giao tiếp giữa người sử dụng và CSDL: Ngôn ngữ định nghĩa dữ liệu (DDL), Ngôn ngữ thao tác dữ liệu (DML), Ngôn ngữ truy vấn có cấu trúc (SQL), Ngôn ngữ quản lý dữ liệu (DCL)

- Hệ cơ sở dữ liệu: là một hệ thống dữ liệu gồm 4 thành phần:
+) Cơ sở dữ liệu hợp nhất: có 2 tính chất: tối thiểu hóa dư thừa + được chia sẻ
+) Người sử dụng: NGƯỜI SD CUỐI (Người ít sử dụng: Ít khi truy cập CSDL, nhưng cần những thông tin khác nhau trong mỗi lần truy cập và dùng những câu truy vấn phức tạp=> Người quản lý; Người sử dụng thường xuyên :Thường xuyên truy vấn và cập nhật CSDL nhờ vào một số các chức năng đã được xây dựng sẳn =>Nhân viên; Người sử dụng đặc biệt: Thông thạo về HQT CSDL, tự xây dựng những truy vấn phức tạp cho công việc => Kỹ sư, nhà khoa học, người phân tích,…) + NG VIẾT CTRINH ỨD (Chịu trách nhiệm về Lựa chọn cấu trúc phù hợp để lưu trữ dữ liệu+ Quyết định những dữ liệu nào cần được lưu trữ, Liên hệ với người dùng để nắm bắt được những yêu cầu và đưa ra một thiết kế CSDL thỏa yêu cầu này, Có thể là 1 nhóm các DBA quản lý các CSDL sau khi việc thiết kế hoàn tất) + NGƯỜI QTRI CSDL( người đk toàn bộ hệ thống: Cấp quyền truy cập CSDL, Điều phối và giám sát việc sử dụng CSDL) 
+) Phần mềm hệ qtri CSDL
+) Phần cứng: thiết bị nhớ thứ cấp được sử dụng để lưu trữ CSDL

4) Phân loại các hệ CSDL
- Theo mô hình dữ liệu: Mạng - Phân cấp - Quan hệ - Hướng đối tượng,.
-Theo số người sử dụng: Một người dùng - Nhiều người dùng
-Theo tính phân tán của CSDL: Tập trung - Phân tán
+)Hệ CSDL tập trung: Hệ CSDL cá nhân + trung tâm + khách/chủ
+) Hệ CSDL phân tán: Hệ CSDL phân tán thuần nhất + phân tán không thuần nhất
- Theo tính thống nhất của dữ liệu: Đồng nhất - Không đồng nhất

II. CÁC MỨC BIỂU DIỄN CỦA MỘT CƠ SỞ DỮ LIỆU
1. Mức vật lý: mức thấp nhất của sự trừu tượng mta DL đc lưu trữ tsu ntn. Các cấu trúc DL mức thấp phức tạp được mô tả chi tiết.
-Nó tồn tại trong các thiết bị lưu trữ
- Mức lưu trữ CSDL – mức trong
- Vấn đề cần giải quyết: Dữ liệu gì, được lưu trữ thế nào? Ở đâu? (đĩa từ, băng từ, track, sector,…. nào?) + Cần các chỉ mục gì? + Truy xuất tuần tự hay ngẫu nhiên?
– Dành cho NGƯỜI QTRỊ và NGƯỜI SD CHUYÊN MÔN
- Ví dụ: Một bản ghi khach_hang được mô tả như một khối nhớ, chương trình dịch che dấu các chi tiết mức này đối với người lập trình  

2. Mức quan niệm (mức logic, mức khái niệm)
- Định nghĩa cấu trúc logic của dữ liệu, dữ liệu nào được lưu trữ & mối quan hệ giữa các dữ liệu
- Biểu diễn trừu tượng của CSDL mức vật lý
-Trả lời câu hỏi: Cần phải lưu trữ bao nhiêu loại dữ liệu? Dữ liệu gì? + Mối quan hệ?
- Dành cho: chuyên viên tin học khảo sát và phân tích, quản trị CSDL
- Ví dụ: mỗi bản ghi được mô tả bởi một định nghĩa kiểu, người lập trình sử dụng ngôn ngữ lập trình làm việc tại mức trừu tượng này

3. Mức khung nhìn (mức ngoài/lược đồ con)
Mô tả cách mà người sử dụng có thể nhìn thấy dữ liệu(mức cao nhất sự trừu tượng chỉ mô tả 1 phần CSDL)
- Mức người sử dụng và chương trình ứng dụng
- Có thể nhìn thấy toàn bộ hoặc 1 phần CSDL theo góc độ khác nhau
- Có thể không biết về cấu trúc tổ chức lưu trữ thông tin trong CSDL
- Chỉ có thể làm việc với 1 phần CSDL

**CÁC THỂ HIỆN VÀ CÁC SƠ ĐỒ**
-Một thể hiện CSDL: tập hợp các ttin đc lưu trữ (.) CSDL tại 1 thời điểm đbiệt.
-Sơ đồ CSDL: 1 thiết kế tổng thể của CSDL

**TÍNH ĐỘC LẬP DỮ LIỆU**
- Tính độc lập DL: khả năng thay đổi 1 định nghĩa sơ đồ (.) 1 mức mà 0 ảnh hưởng đến định nghĩa sơ đồ (.) mức cao hơn tiếp theo.
- Có 2 mức độc lập:
+) Mức vật lý: khả năng thay đổi sơ đồ vly mà kh dẫn đến các ctrinh UWSD phải viết lại
+) Mức logic: khả năng thay đổi sơ đồ logic mà kh dẫn đến các ctrinh UWSD phải viết lại 
=> Mức logic KHÓ ĐẠT ĐƯỢC do ctrinh ỨD phụ thuộc nhiều vào ctruc logic của dữ liệu mà họ đg truy nhập

**CÁC NGÔN NGỮ CSDL**
- 2 kiểu ngôn ngữ: đặc tả sơ đồ dữ liệu + bdien các truy vấn và các cập nhật CSDL
-Ngôn ngữ định nghĩa dữ liệu (DDL-Data Definition Language): một sơ đồ CSDL đặc tả bởi 1 tập các định nghĩa đc bdien bởi 1 ngôn ngữ đbiệt.
=> Kết quả của vc dịch các lệnh của ngôn ngữ này là một tập các băng đc lưu trữ (.) 1 tệp đbiệt gọi là từ điển dữ liệu/thư mục dữ liệu.
+) Từ điển dữ liệu: một tệp chứa các siêu dữ liệu có nghĩa là các dữ liệu về dữ liệu. Được tra cứu trc khi DL tsu đc đọc/đc sửa đổi (.) hệ CSDL.
+) Chức năng: tạo, sửa xóa cấu trúc quan hệ, bảo mật và quyền truy nhập
+) Ngôn ngữ định ngữ định nghĩa và lưu trữ dữ liệu: cấu trúc lưu trữ và các phương pháp truy nhập được SD bởi 1 hệ CSDL đc đặc tả bởi 1 tập các định nghĩa (.) 1 kiểu đbiệt của DDL
=> Kết quả dịch định nghĩa này là một tập các chỉ thị đặc tả các chi tiết cài đặt của  CSDL, các chi tiết này thường được che dấu đvs ng SD
- Ngôn ngữ thao tác dữ liệu (DML-Data Manipulation Language)
+) Các yêu cầu thao tác dữ liệu gồm: Tìm kiếm ttin đc lưu trữ (.) CSDL, Thêm thông tin mới vào CSDL, Xóa ttin từ CSDL, Thay đổi ttin đc lưu trữ (.) CSDL
+) DML: là ngôn ngữ cho phép nhg ng SD truy nhập/thao tác dữ liệu đc tổ chức bởi mô hình dữ liệu thích hợp.
=> 2 kiểu ngôn ngữ thao tác:
	+) DML thủ tục đòi hỏi 1 ng SD phải đặc tả dữ liệu nào cần tkiem và tkiem nhg dữ liệu này ntn
	+) DML phi thủ tục đòi hỏi 1 ng SD đặc tả dữ liệu nào cần tkiem mà khphai đặc tả tìm kiếm nhg dữ liệu này ntn
=> DML phi thủ tục DỄ ĐỌC+DỄ SỬ DỤNG HƠN
+) Một truy vấn: một chỉ thị ycau tkiem ttin
+) Ngôn ngữu truy vấn: Các lệnh của DML kéo theo tkiem ttin

**XỬ LÝ CÂU HỎI**
- Công việc của bộ xử lý câu hỏi là bđổi 1 truy vấn/1 thao tác CSDL có thể đc bdien tại 1 mức rất cao thành 1 dãy các yêu cầu đối với các dlieu đc lưu trữ (.) CSDL.
- Phần khó nhất của xử lý câu hỏi là tối ưu hóa câu hỏi, có nghĩa là lựa chọn 1 kế hoạch thực hiện tốt nhất hay lựa chọn 1 dãy các yêu cầu đvs hệ thống lưu trữ để trl truy vấn này nhanh nhất
- Các truy vấn phức tạp thường cho phép sắp xếp lại trình tự các phép toán và có thể có 1 số lớn các kế hoạch thực hiện có thể, thg có thể số kế hoạch là hàm số mũ đvs kthuoc của câu hỏi

**QUẢN TRỊ GIAO DỊCH**
- Một giao dịch trong cơ sở dữ liệu là một đơn vị công việc logic gồm nhiều thao tác, được xử lý như một khối không thể tách rời: hoặc tất cả thao tác được thực hiện, hoặc không thao tác nào được thực hiện.
- Hệ quản trị cơ sở dữ liệu đảm bảo tính nhất quán, an toàn, đồng thời, và khả năng phục hồi khi có lỗi hệ thống.
- Giao dịch phải đảm bảo:Tính nguyên vẹn + Tính đồng thời + Khả năng phục hồi
- Các hệ quản trị cơ sở dữ liệu lớn có đầy đủ cơ chế quản trị giao dịch, điều khiển tương tranh và phục hồi.
- Hệ nhỏ (như máy cá nhân) có thể không có đầy đủ các tính năng này và thường chỉ cho phép một người truy cập tại một thời điểm.

**QUẢN LÝ LƯU TRỮ**
- Cơ sở dữ liệu thường đòi hỏi lưu trữ khối lượng lớn thông tin.
- Dữ liệu có thể chiếm từ vài gigabytes đến hàng terabytes.
- Hệ thống quản trị cơ sở dữ liệu cần sử dụng hiệu quả các thiết bị lưu trữ, đảm bảo dữ liệu được lưu an toàn, dễ truy xuất và tối ưu hiệu suất hệ thống.
- Dữ liệu được lưu trữ trên các thiết bị như đĩa từ, băng từ và có thể được chuyển sang bộ nhớ chính để xử lý nhưng chậm so với tốc độ xử lý bộ trung tâm
- Việc lưu trữ và truy xuất dữ liệu hiệu quả cần thiết kế hợp lý để giảm thời gian và chi phí truy cập.
- Cấu trúc lưu trữ ảnh hưởng trực tiếp đến hiệu năng của hệ thống.
- Bộ quản lý lưu trữ là mô-đun chương trình cung cấp giao diện giữa các dữ liệu đc lưu trữ (.) CSDL mức thấp và các ctrinh UWSD hay các truy vấn đc đẹ trình đối với hệ thống và có trách nhiệm:
+) Tương tác với bộ quản lý tệp
+) Bộ quản lý lưu trữ dịch các lệnh của ngôn ngữ DML khác nhau thành các hệ thống xử lý tệp mức thấp
=> Trách nhiệm: Lưu trữ, tìm kiếm và cập nhật dữ liệu trong CSDL

III. Kiến trúc tổng quát của hệ qtri CSDL 
1. Bộ xử lý câu hỏi
- Yêu cầu: Tìm kiếm dữ liệu trả lời cho một yêu cầu truy vấn.
- Thực hiện: Biến đổi truy vấn ở mức cao thành các yêu cầu có thể hiểu được bởi hệ CSDL, Lựa chọn một kế hoạch tốt nhất để trả lời truy vấn này

2. Bộ quản lý lưu trữ
-Yêu cầu: lưu trữ và truy xuất dữ liệu trên các thiết bị nhớ
- Thực hiện: Tổ chức tối ưu dữ liệu trên thiết bị nhớ, Tương tác hiệu quả với bộ quản lý tệp

3. Bộ quản trị giao dịch
-Yêu cầu
+)Định nghĩa giao dịch: một tập các thao tác được xử lý như một đơn vị không chia cắt được
+) Đảm bảo tính đúng đắn và tính nhất quán của dữ liệu + tính toàn vẹn
- Thực hiện: Quản lý điều khiển tương tranh + Phát hiện lỗi và phục hồi CSDL

-  3 kiểu thao tác đối với hệ qtri cơ sở dữ liệu:
+) các truy vấn: các thao tác hỏi đáp về dữ liệu được lưu trữ trong CSDL. Được sinh ra theo 2 cách gồm thông qua 1 giao diện truy vấn chung + thông qua các giao diện ctrinh ỨD
+) cập nhật dữ liệu
+) các thay đổi sơ đồ: ng qtri cơ sở dl là chủ

**NGƯỜI QUẢN TRỊ CƠ SỞ DỮ LIỆU**
- là ng có trách nhiệm ddkhien 1 cách tập trung toàn bộ hệ thống
- Nvu: định nghĩa sơ đồ + xác định cấu trúc lưu trữ và pp truy nhập + tuyên bố ủy quyền truy nhập dữ liệu + đặc tả các ràng buộc toàn vẹn

**NGƯỜI SỬ DỤNG CƠ SỞ DỮ LIỆU**: 3 nhóm người
- Người lập trình ứng dụng
- Người phân tích dữ liệu
- Người sử dụng cuối

IV. Phân loại các hệ cơ sở dữ liệu
- Có 2 loại kiến trúc CSDL: phân tán và tập trung
1. Hệ cơ sở dữ liệu tập trung: 3 kiểu
a. Hệ CSDL cá nhân: 
+) ứng dụng chung nhất là cviec kinh doanh nhỏ
+) ứng dụng điển hình: quản lý thanh toán, kiểm kê hàng hóa, quản lý khách hàng
=> Rủi ro tạo ra “các hòn đảo tự trị”
b. Hệ CSDL trung tâm:
+) lưu trữ trên 1 máy tính trung tâm, người sử dụng từ xa có thể truy nhập CSDL thông qua các thiết bị đầu cuối và các máy móc truyền thông DL
+) lưu trữ các CSDL tích hợp rất lớn và dc nhiều ng SD truy nhập (trăm giao dịch/s)
+) ứng dụng điển hình:hệ thống đăng ký giữ chỗ máy báy, httt cơ quan tài chính và cty phát triển nhanh
c. Hệ CSDL khách/chủ
+) Máy tính được móc nối vs nhau trong 1 mạng cục bộ, đc thiết kế với sự phân tải cv trên mạng mtinh trong đó các máy khách có thể chia sẻ các dịch vụ của một máy chủ đơn lẻ
+) Một máy chủ: một ứng dụng phần mềm cung cấp các dịch vụ quản lý tệp/CSDL,qly truyền thông đvs các máy khách đg ycau
+) Một máy khách: một ứng dụng phần mềm yêu cầu các dvu từ 1 hay nhiều máy chủ. Thường được định vị trên một máy tính riêng trong mạng cục bộ đó
+) Mục đích: cho phép ứng dụng máy khách truy nhập dữ liệu đc quản lý bởi máy chủ. Giao diện ng sử dụng và logic của ứng dụng kinh doanh đc xử lý trên máy khách, trong khi xử lý cơ sở dữ liệu đc thực hiện trên máy chủ cơ sở dữ liệu
+) Sử dụng để hỗ trợ tính toán theo 1 nhóm công việc (sdung các tài nguyên tính toán để hỗ trợ quyết định và các ứng dụng khác bởi 1 nhóm ng sdung)

2. Hệ cơ sở dữ liệu phân tán: 2 kiểu
- là một cơ sở dữ liệu logic đơn lẻ mà dc trải ra về mặt vật lý trên nhiều máy tính ở nhiều vị trí địa lý khác nhau
a. Hệ CSDL phân tán thuần nhất
- là công nghệ CSDL là như nhau (hay ít nhất là có thể tương thích) tại 1 vị trí địa lý và dữ liệu tại các vị trí địa lý khác nhau cũng có thể tương thích
- Điều kiện:
+) Các hệ điều hành mtinh tại mỗi vị trí là như nhau/có khả năng tương thích cao
+) Các mô hình dữ liệu đc sdung tại mỗi vị trí là như nhau 
+) Các hệ qtri CSDL đước sử dụng tại mỗi vị trí địa lý là như nhau/khả năng tương thích cao
+) Dữ liệu tại các vtri khác nhau có các định nghĩa và khuôn dạng chung
b. Hệ CSDL phân tán không thuần nhất
- Các tổ chức thường có nhiều cơ sở dữ liệu đặt tại các vị trí khác nhau và không được lập kế hoạch đồng bộ từ đầu.
- Mỗi vị trí có thể sử dụng hệ điều hành, mô hình dữ liệu, phần mềm quản trị khác nhau → dẫn đến sự không tương thích giữa các hệ thống.
- Dữ liệu ở các vị trí khác nhau có thể khác nhau về: Cú pháp (cách biểu diễn khác nhau) + Ngữ nghĩa (ý nghĩa khác nhau cho cùng một dữ liệu).
- Việc xây dựng một hệ cơ sở dữ liệu thống nhất là khó khăn, tốn kém và thường không khả thi về kỹ thuật lẫn kinh tế.
- Cơ sở dữ liệu đc móc nối với nhau tạo ra tập các cơ sở dữ liệu kh thuần nhất (cơ sở dữ liệu liên hiệp)
- Thường chỉ có thể đọc dữ liệu giữa các vị trí, nhưng không cập nhật được đồng bộ
 
Một quan hệ dạng chuẩn 1NF có thể chuyển đổi về nhóm các quan hệ 3NF bằng cách :a. Loại bỏ các phụ thuộc không đầy đủ vào khoá và bắc cầu vào khoá.
Phép tính vị từ biến bộ sử dụng các biến đại diện cho: các bộ trong quan hệ
Xác thực đa yếu tố: sử dụng hai/nhiều yếu tố để xác thực
Nhược điểm chính của tổ chức tệp đống: tìm kiếm dữ liệu chậm do kh có cấu trúc sắp xếp
Quy tắc Amstrong đbảo tập F và tập suy ra từ F là tương đương: quy tắc bao đóng, phản xạ, hợp
View trong SQL: một bảng ảo trong csdl có ndung đc định nghĩa thông qua 1 câu lệnh SQL nào đó
Biểu thức không hợp lệ trong đại số quan hệ: chọn_{A>B}(R kết nối tự nhiên S)
+) Đc: R hợp (S-T); chiếu_{A}(R) kntn chọn_{B>10}(S); chiếu_{A}(R hợp S)
4 KIỂU PHÂN BIỆT CÔNG CỤ KHUNG NHÌN
Câu lệnh phát sinh lỗi khi thực thi: IF NOT EXISTS CREATE DATABASE STUDNETS
Khóa thay thế: khóa có thể dung như khóa chính nếu cần thiết
Dsach hhoa trong kho chứ IP14: Select*from hanghoa where makho in (select makho from hanghoa where ten_hh = N’IP14’)
Quan hệ N:N chuyển sang quan hệ: tạo 1 bảng riêng cho mối quan hệ
Quan hệ 1:1 chuyển sang qhe: hợp nhất 2 thực thể thành 1 bảng/thêm khóa ngoại
Trong kiến trúc ba mức, nếu lược đồ ngoài thay đổi, điều gì sẽ xảy ra: Các ứng dụng sử dụng lược đồ ngoài đó bị ảnh hưởng
Khóa phức hợp: tạo thành từ nhiều thuộc tính
Quan hệ 3NF: có mỗi phụ thuộc X->a, X là siêu khóa hoạc A là thuộc tính không khóa
Phép xóa: xóa 1 bộ hay xóa 1 nhóm các bộ
Phép kết nối bằng nhau: tích đề các + chọn
Hai bảng qhe liên kết với nhau thông qua: thuộc tính các trường đc chọn
Để đưa ra tất cả các tên hàng trong bảng HANGHOA có tên bắt đầu là
“TIVI” thì câu lệnh nào sau đây sẽ thực hiện được: Select TENHANG From HANGHOA WHERE TENHANG LIKE ‘TIVI%’
Mỗi bảng trong CSDL phải có ít nhất một cột
Phép chọn được thực hiện sau FROM, tại mệnh đề WHERE
Phép chiếu được thực hiện sau mệnh đề WHERE
Các bước thực hiện đúng câu lệnh SELECT: Tích Đề các, phép toán chọn, theo nhóm, sắp xếp và phép chiếu
Quan hệ 3NF có thể chấp nhận đc trong quá trình tìm kiếm: vì kh xuất hiện dị thường thông tin khi thực hiện các phép lưu trữ
Quan hệ 2NF không thể chấp nhận vì có thể k chèn thêm ttin
Tích quan hệ from, chọn theo biểu thức sau where và chiếu trên các thuộc tính sau select
Các dòng trong một bảng có thể nạp vào theo thứ tự tùy ý
Không thể chèn thêm thông tin 1 loại cáp khi chứ đc lắp đặt vì gtri khóa 0 xác định
Quan hệ gồm mã số, họ tên, địa chỉ là dạng chuẩn 3NF
Sau khi chuẩnhóa đến 3NF chúng ta có 4 quan hệ sau: R11 với U11 = {SoHD, MaKH,NgayDathang}; R12 với U12 = {MaKH, TenKH, DiaChiKH}; R21 với U21 ={SoHoadon, Mahang,SoLuong}; R22 với U22 = {Mahang, Tenhang, DonGia}
Nguyên tắc đánh giá tối ưu hóa biểu thức quan hệ: Ưu tiên thực hiện các phép chiếu và chọn
Kết quả chúng ta có có 3 quan hệ: R1 với U1= {ABCD}; R21 với U21= {AEFGH} và R22 với U22= {FIJ}
Quá trình tách không làm tổn thất thông tin theo nghĩa: : Quan hệ gốc được
khôi phục từ các quan hệ chiếu.bằng phép kết nối tự nhiên
“Lệnh SQL được sử dụng để thêm và đưa dữ liệu vào bảng với các giá trị tương ứng với các cột là lệnh…” INSERT
Mệnh đề AS được sử dụng để thay đổi tên một cột trong tập kết quả hoặc để gán tên cho một cột dẫn xuất
BETWEEN trong SQL được sử dụng để...? : Chỉ định một phạm vi để kiểm tra
Cách tiếp cận vật chất hóa được thực hiện như thế nào? ghi kết quả vào đĩa thông qua các quan hệ tạm thời
Các bước chính để tạo CSDL: Tạo bảng; Chọn khóa chính cho bảng; Đặt tên
bảng và lưu cấu trúc bảng; Tạo liên kết bảng


CHƯƠNG II. NNGỮ ĐỊNH NGHĨA VÀ TTÁC DL DVS MÔ HÌNH QHE + LÝ THUYẾT THIẾT KẾ CSDL
- ngôn ngữ đại số + ngôn ngữ tính toán vị từ
- khả hợp nếu chúng đc xác định trên cùng 1 tập thuộc tính và các thuộc tính cùng tên có cùng miền gtri
- phép hợp: tất cả các bộ thuộc r hoặc s hoặc thuộc cả hai qhe
- phép giao: tất cả các bộ thuộc cả hai quan hệ r và s
- phép trừ: tất cả các bộ thuộc r nhưng không thuộc s
- phép chiếu: loại bỏ đi 1 số thuộc tính và giữ lại nhg thuộc tính còn lại của qhe
- phép chọn: lọc ra 1 tập con các bộ quan hệ đã cho tm 1 điều kiện xđinh->đk chọn/bthuc chọn
- Chuẩn 2NF: 1NF + mọi thuộc tính kh khóa phụ thuộc đầy đủ vào khóa chính
- Chuẩn 3NF: 2NF + mọi thuộc tính kh khóa 0 phục thuộc bắc cầu khóa chính

*TỔ CHỨC DỮ LIỆU VẬT LÝ*
- Bộ nhớ ngoài: thứ cấp lưu trữ đĩa từ, bằng từ,..
- đĩa từ chia thành khối vật lí kích thước giống nhau. Mỗi khối 512-4096 bytes đc đánh địa chỉ tuyệt đối
- mỗi tệp dl lưu trên đĩa từ chiếm 1/nhiều khối, mỗi khối chứa 1/nhiều bản ghi.
1.Tổ chức tệp đống
-đơn giản nhất, lưu trữ kế tiếp nhau k theo tuần tự,k tổ chức
- Thao tác: tìm kiếm, thêm sau bản ghi cuối cùng, xóa, sửa đổi
2. Tổ chức tệp băm
-phân chia thành các cụm.mỗi cụm gồm một hoặc nhiều khối(block),mỗi khối chứa số lg bản ghi cố định
- thao tác: tkiem, thêm vào khối đầu tiên,xóa,sửa đổi
3. tệp chỉ dẫn
- các cặp (k,d) k là gtri khóa, d địa chỉ khối
- thêm bản ghi: nếu k có chỗ thì đẩy cái cuối sang mới để thế vào chỗ cuối
4. B-cây
-B cây cân bằng tổ chwuc theo cấp m, tính chất:
+) Gốc là 1 nút lá/ít nhất 2 con
+) mỗi nút (trừ nút gốc và nút lá) có từ [m/2] đến m con
- mỗi khối chứa tối đa 3 bản ghi, mỗi khối ứng vs nút chứa 1 con trỏ và 2 bản chỉ dẫn. Các nút thực chất là tệp chỉ dẫn

*TỐI ƯU HÓA CÂU HỎI*
- Bước lquan xử lý truy vấn: phân tích và dịch, tối ưu hóa, đánh giá
- tối ưu bằng biểu thức quan hệ: 6 chiến lược
+) phép chọn và chiếu sớm nhất có thể
+) tổ hợp phép chọn xđ với phép tích đề các thành phép kết nối
+) tổ hợp dãy các phép toán 1 ngôi như các phép chọn và phép chiếu
+) xác định các biểu thức con chung trong 1 bthuc
+) xử lý tệp trc khi tính toán phép kết nối/tương đương với nó là 1 phép tích đề các đi theo sau 1 phép chọn
+) ước lượng chi phí và lựa chọn thứ tự thực hiện thích hợp
- pphap tối ưu hóa chiến lược: áp dụng phép chọn/chiếu đơn giản -> áp dụng phép chọn và phép chiếu,hoặc -> áp dụng phép tích đề các, phép hợp/phép hiệu tập hợp cho 2 hạng thức mà trc đó các phép chọn/phép chiếu đã đc áp dụng cho 1/cả 2 hạng thức
- ánh xạ cuốn: là ánh xạ từ các hàng của bảng này lên các hàng cảu 1 bảng khác mà báo toàn biến pbiet và các hằng số nhg kh ánh xạ một ký hiệu lên 2 ký hiệu pbiet

*AN TOÀN VÀ TOÀN VẸN DỮ LIỆU*
- hệ qtri csdl dbao 0 cho phép ng sd thực hiện bất cứ ttac nào nếu 0 đc hco phép
- quyền truy cập: đọc dữ liệu + cập nhật dữ liệu + bổ sung dữ liệu + xóa dữ liệu
- quyền sửa đổi sơ đồ csdl: tạo chỉ dẫn, qly tài nguyên, thay đổi, loại bỏ
-cung cấp ptein cho ng sd để hệ thống nhận bt 
- sơ đồ đơn giản nhất và chung nhất để xác minh ng sd là dùng mkhau
1. các khung nhìn như cơ chế bảo vệ
- cho phép xd ctr ứng dụng
- định nghĩlaij csdl mức logic
- tăng cường tính độc lập dữ liệu mức logic
-công cụ: “chỉ đọc” ISBL+QBE và cả đọc và ghi
2. Lệnh
-tạo khung nhìn CREATE VIEW<tên view>[(<dstencot>)] AS <câu truy vấn?
-tuyên bố và kiểm tra: GRANT<DSTTAC> ON <DDOITUONG> TO <NGUOI> [WITH GRANT OPTION]
+) read, select, write, insert, update, delete, create, run
+) tên bảng, khung nhìn,ctrnh ud
+) tên ng sd, nhóm ng
+) tiếp tục lan truyền
- hủy bỏ: REVOKE <DS> ON <DOITUONG> FROM <NGUOI>
3. Toàn vẹn dữ liệu
- mất do: hỏng về phần cứng ở 1 chỗ trong hệ thống, sai sót về phía ng ttac mtinh/ng sd đầu cuối, về lập trình trong hệ qtri csdl/hđh cơ sở, lập trình ở 1 trong nhg uwsd csdl
4. Ràng buộc toàn vẹn
- miền : cơ bản nhất 
CONSTRAINT<TÊN RÀNG BUỘC> CHECK(<TÊN CỘT>){IN/NOT IN}(TẬP GTRI)
CONSTRAINT [PRIMARY KEY ]/[UNIQUE KEY] / [FOREIGN KEY]
5. khẳng định
- Các khẳng định: Một khẳng định là một vị từ biểu thị điều kiện muốn cơ sở dữ liệu luôn thỏa mãn
CREATE ASSERTION <tên khẳng định> CHECK <vị từ>
- Khi một khẳng định được tạo lập, hệ thống sẽ kiểm tra tính hiệu lực.Khi khẳng định có hiệu lực thì sau đó một sự thay đổi sẽ chỉ được thực hiện nếu khẳng định không bị vi phạm
6. Các kích hoạt: Một kích hoạt là một chỉ thị được thực hiện một cách tự động bởi hệ thống như một tác động phụ của một thay đổi. Để thiết kế kích hoạt cần đáp ứng: Đặc tả các điều kiện + Đặc tả các hành động
- Được dùng để báo động hay thực hiện nhiệm vụ nhất định một cách tự động khi các điều kiện được đáp ứng còn đc gọi là các luật sự kiên-đk-hđ hay luật ECA
- Một số nguyên tắc:  Chỉ được kiểm tra khi các sự kiện, các đặc tả xuất hiện + Ngăn chặn lập tức sự kiện vừa phát sinh bằng một kích hoạt kiểm tra điều kiện + Khi điều kiện của kích hoạt được thỏa mãn, hành động kết hợp với kích hoạt được thực hiện bởi hệ quản trị cơ sở dữ liệu
7. Các phụ thuộc hàm:  Một kiểu ràng buộc đặc biệt được gọi là phụ thuộc hàm, xác định ràng buộc trên tập các quan hệ, cho phép biểu diễn các sự kiện được mô hình hóa trong cơ sở dữ liệu 
- Phụ thuộc hàm là sự tổng quát hóa khái niệm khóa, nó có thể cho phép biểu diễn các ràng buộc không biểu diễn được qua các ràng buộc về khóa

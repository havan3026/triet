DANH SÁCH CÁC HÀM

Tần suất:   FREQUENCY(data_array, bins_array) – Ctrl+shift+enter
Data_array : tập hợp các giá trị cần đếm tần suất
Bins_array : nhu cầu nhóm các giá trị

Xếp hạng: RANK(number, ref, order))
Number: số cần xếp hạng
Ref: tập hợp danh sách các số.
Order: chỉ định cách xếp

Hàm:  IF(logical_test, value_if_true, value_if_false)

Tìm một giá trị trong cột tận cùng bên trái của 1 bảng  xong cho ra 1 giá trị ở cùng hàng với giá trị tìm được từ cột được chỉ thị
VLOOKUP(lookup_value, table_array, col_index_num, range_lookup)
Lookup_value: giá trị phải được tra cứu ở cột tận cùng bên trái
Table_array: bẳng tra cứu ( địa chỉ tuyệt đối)
Col_index_num: số thứ tự cột trong bảng tra cứu
Range_lookup: tím liên kết tương đương(true), lien kết chính xác(false)

Tìm kiếm 1 giá trị trong hàng thứ nhất của 1 bảng rồi cho 1 giá trị trong cùng cột tính từ hàng đã xác định
HLOOK(lookup_value, table_array, row_inder_num,range_lookup)

Cộng các ô được chỉ định theo tiêu chuẩn cho trước
SUMIF(range,criteria,sum_range)
Range: dãy các ô muốn lượng giá
Criteria: tiêu chuẩn nhằm xác dịnh loại ô nào được cộng
Sum_range: các ô thực tế phải tính tổng

Đếm số lượng các ô trong 1 vùng thỏa mãn criteria
COUNTIF(range,criteria)

Tìm giá trị trung bình trong điều kiện cho trước
DAVERAGE(database,field,criteria)
Database: Vùng dữ liệu
Field: tên trường(cột)

Số các ô chứa giá trị cho trước thỏa mãn criteria
DCOUNT(database,field,criteria)

 Tìm giá trị Max thỏa mãn criteria
DMAX(database,field,criteria)

Tích các giá trị thỏa mãn criteria
DPRODUCT(database,field,criteria)

 Tổng các giá trị thỏa mãn criteria
DSUM(database,field,criteria)

 Tổng khấu hao theo tổng các năm trong 1 chu kì xác định
SYD(cost,salvage,life,per)
Cost: giá trị ban đầu of tài sản
Salvage: giá trị còn lại tại thời điểm cuối của đời hữu dụng
Life: chủ kì sử dụng
Per: chu kì tình khấu hao (cùng đơn vị với life)

 Tính khấu hao = phương pháp kết số giảm đều cố định
DB(cost,salvage,life,per,month)
Month: số tháng sử dụng tài sản trong năm đầu tiên

 Tính khấu hao = p.p kết toán giảm nhanh kép (theo tỷ lệ xác định)
DDB(cost,salvage,life,per,factor)
Factor: tỷ suất khấu hao

 Tính khấu hao = p.p kế toán kép (hay chỉ định)
VDB(cost,salvage,life,start_per,end_per,factor,no_switch)
No_switch: giá trị logic ( .T. là không,  .F. là có)

 Tính giá trị còn lại of tại sản
Salvage=cost*(1-rate)^life
Rate: tỷ lệ khấu hao mỗi chu kì

 Tính khấu hao vs tỷ lệ khấu hao trải đều cho 1 khoảng thời gian
SLN(cost,salvage,life)

Tính giá trị tương lai của 1 khoản đầu tư dựa vào tổng số chu kì, tiển trả và lãi suất cố định
FV(Rate,Nper,Pmt,Pv,Type)
Nper: tổng số kì chi trả
Pmt: số tiền chi trả trong mỗi kì (cố định)
Pv: giá trị đầu tư ban đầu
Type: bằng 1 nếu số tiền trả đầu kì, bằng 0 nếu cuối kì

 Tính lãi gộp
FV = Pv*(1+Rate)^life

 Tính giá trị tương lai of đầu tư vs lãi suất thay đổi
FVSCHEDUELE(princripal,Scheduele)
Princripal: vốn chính
Scheduele: dãy tỷ lệ lãi suất được áp dụng

 Tính lãi suất thực tế hàng năm
EFFECT(Nominal_rate,Npery)
Nominal_rate: lãi suất danh nghĩa
Npery: số lần tính lãi trong năm

Tính giá trị hiện tại dòng
NPV(Rate, Value 1,Value 2,….)
Value 1: giá trị vốn bỏ ra ban đầu (âm)
Value 2,…: giá trị tiền dự đoán thu về (dương) or phải bỏ ra mỗi kì (âm)

 Tính tỷ lệ hoàn vốn (khi NPV = 0)
IRR(Value,Guess)
Value: vùng dữ liệu muốn tính tỷ lệ
Guess: số ta kì vọng (để trống là 10%)

 Tính giá trị hiện tại của khoản đầu tư
PV(Rate,Nper,Pmt,Fv,Type)

Tính số tiền trả định kì dựa trên tiền trả và lãi suất cố định
PMT(Rate,Nper,Fv,Type)

 Tính số tiền lãi phải trả trong 1 kì hạn
IPMT(Rate,Per,Nper,Pv,Fv,Type)

 Tính mức lãi suất theo chu kì
RATE(Nper,Pmt,Pv,Type,Guess)

 Tính lãi gộp cho 1 trái phiếu trả vào ngày tới hạn
ACCRINTM(Issue,Maturity,Rate,Par,Basis)
Issue: ngày phát hành trái phiếu
Maturity: ngày tới hạn
Rate: lãi suất of trái phiếu
Par: mệnh giá mỗi trái phiếu
Basis: cơ sở tính ngày

 Tính lãi suất của chứng khoán được đầu tư hết
INTRATE(Settlement,Maturity,Investment,Redemption,Basis)
Settlement: ngày giao dịch nhà đầu tư thanh toán tiền cho nhà phát hành và nhận chứng khoán
Investment: khoản đầu tư đã trả cho nhà phát hành
Redemption: khoản tiền thu được of nhà đầu tư vào ngày tới hạn

 Tính số tiền thu được of chứng khoán vào ngày tới hạn (đầu tư hết)
RECEIVED(Settlement,Maturity,Investment,Discount,Basis)
Discount: tỷ lệ chiếu khấu

 Tính tỷ suất chiết khấu of 1 chứng khoán
DISC(Settlement,Maturity,Pr,Redemption,Basis)
Pr: giá trị mỗi mệnh giá 100 đôla of chứng khoán

 Tính giá trị cho mỗi mệnh giá 100 đôla of CK vào ngày tới hạn
PRICEMAT(Settlement,Maturity,Issue,Rate,Yld,Basis)
Yld: lợi tức hàng năm

 Dự đoán trên cơ sở mô hình tuyến tính
FORECAST(X,known_y,known_x)
X: giá trị để dự đoán
Known_x: các đại lượng đã biết of X
Known_y: các đại lượng đã biêt of Y

Câu 1:  Các yếu tố cần đánh giá khi mua sắm phần cứng không bao gồm 
Năng lực hoạt động
Công nghệ
Tính thân thiện với môi trường (ĐA) 
Khả năng kết nối
Câu 2: Các yếu tố cần đánh giá khi mua sắm phần cứng không bao gồm
Tốc độ
Công nghệ
Khả năng bảo mật   (ĐA).
Khả năng hỗ trợ	
Câu 3: Thiết bị nào là bộ nhớ của máy tính
Vi phim máy tính
Dữ liệu ký tự, âm thanh, hình ảnh
Băng từ . (ĐA)
Bộ xử lý trung tâm
Câu 4: Thành phần nào sau đây của HTTT là yếu tố phi công nghệ
Phần cứng
Phần mềm
Dữ liệu
Thủ tục . (ĐA)
Câu 5: Một… tương đương 1024 GB
Gigabyte
Terabyte. (ĐA)
Kilobyte
Megabyte
Câu 6: Hãy chọn phương án trả lời đúng nhất: 
Phần cứng của máy tính điện tử là:
Là toàn bộ thiết bị…
Là toàn bộ ..chức năng xử lý thông tin
Là toàn bộ trang thiết bị máy móc thực hiện chức năng truyền thông tin (ĐA)
Là toàn bộ các chương trình thực hiện chức năng truyền thông tin
Câu 7: Sự giống nhau cơ bản giữa bộ nhớ ngoài và bộ nhớ RAM là:
Đều mất thông tin khi mất điện/ tắt máy
Đều không mất thông tin khi mất điện hoặc tắt máy
Đều có thể ghi và đọc thông tin (ĐA)
Đều lưu trữ bảo quản thông tin lâu bền
Câu 8: Màn hình cảm ứng là ví dụ về một loại thiết bị nào ?
Chỉ là thiết bị lưu trữ
Chỉ là 1 thiết bị ra
Một phần mềm hỗ trợ ra quyết định
Vừa là thiết bị ra, vừa là thiết bị lưu trữ (ĐA)
Câu 9: Lý do nào sau đây cho thấy bộ nhớ trong được coi là bộ nhớ chính 
Không có bộ nhớ trong thì máy tính không lưu được chương trình
Không có bộ nhớ trong thì máy tính không thể hoạt động được (ĐA)
Không có bộ nhớ trong thì máy tính không lưu được dữ liệu
Không có bộ nhớ trong thì máy tính không xử lý được các lệnh

Câu 10: Để chạy một chương trình hay xử lý các dữ liệu, trước tiên máy tính cần phải chuyển chương trình hay dữ liệu cần xử lý từ đĩa vào …
Bộ nhớ
Bộ nhớ chính (ĐA)
Đĩa cứng
Thiết bị đầu vào
Câu 11: Tất cả các máy tính đều cấu thành từ các bộ phận giống nhau, trong số đó có:
Bytes, đầu vào và đầu ra
Bộ vào, bộ nhớ và bộ kiểm soát DAS
Đường truyền thông tin, bộ nhớ và modem
Bộ vào, bộ ra, bộ nhớ và bộ làm tính (ĐA)
Câu 12: ALU là viết tắt của:
Arithmetic Logic Unit (ĐA)
Array Logic Unit
Application Logic Unit
None of above
Câu 13: Tất cả các thiết bị sau đây đều cùng chỉ một loại máy tính, trừ
Máy tính cá nhân
Máy vi tính
Máy tính mini (ĐA)
Máy pc
Câu 14: Linh kiện chính của máy tính điện tử ở thế hệ thứ hai là ?
Bóng bán dẫn
Bóng đèn điện tử (ĐA)
Mạch tích hợp cỡ lớn
Mạch tích hợp
Câu 15: Máy tính cá nhân ra đời ở thế hệ nào của máy tính điện tử
Thế hệ thứ hai
Thế hệ thứ nhất
Thế hệ thứ tư (ĐA)
Thế hệ thứ ba 

Câu 11.01: Chế độ đa chương trình là gì, chế độ ấy có tác dụng gì
Là quá trình đưa vào bộ nhớ trong nhiều chương trình cùng một lúc rồi dùng hệ điều hành để điều phối CPU luân phiên thực hiện các chương trình ấy….,làm việc không hết công suất (ĐA)
Là quá trình kết hợp nhiều chương trình vào một hệ thống chương trình…
Là quá trình thực hiện song song nhiều chương trình khác nhau bởi nhiều CPU…
Là quá trình liên kết nhiều máy tính vào cùng một mạng…
Câu 11.02: Phần mềm máy tính là các chương trình giúp máy tính vận hành và thực hiện được các chức năng đáp ứng nhu cầu của con người ?
Đúng (ĐA)
Sai
Câu 11.03: Phần mềm có tốc độ thay đổi nhanh hơn phần cứng máy tính ?
Đúng (ĐA)
Sai
Câu 11.04: Phần mềm nhóm công tác là phần mềm 
Mạng xã hội
Phần mềm chatting
Chia sẻ tài nguyên
Các phương án trên  (ĐA)
Câu 11.05: Hệ điều hành là phần mềm ứng dụng luôn được cài đặt đầu tiên sau khi mua máy tính
Đúng
Sai (ĐA)
Câu 11.06: Hệ điều hành giúp tạo ra môi trường phù hợp cho các phần mềm ứng dụng hoạt động, khai thác tối ưu các tài nguyên của máy tính ?
Đúng (ĐA)
Sai
Câu 11.07: Các yếu tố cần đánh giá khi mua sắm phần mềm không bao gồm
Khả năng hoạt động
Dung lượng bộ nhớ (ĐA)
Khả năng kết nối
Tài liệu hướng dẫn đầy đủ
Câu 11.08: Các yếu tố cần đánh giá khi mua sắm phần mềm không bao gồm
Tốc độ hoạt động
Tính linh hoạt
Tính thân thiện 
Dung lượng bộ nhớ (ĐA)
Câu 11.09: Khái niệm nào về phần mềm là đúng ?
Phần mềm là tập hợp của các thiết bị lưu trữ như ổ cứng, đĩa mềm, USB,..
Phần mềm là tập hợp của các thiết bị xuất như màn hình, máy in máy chiếu,...
Phần mềm là một tập hợp những câu lệnh được viết bằng một hoặc nhiều ngôn ngữ lập trình và các dữ liệu hay tài liệu liên quan nhằm tự động thực hiện một số nhiệm vụ hay chức năng (ĐA)
Phần mềm là tập hợp các thiết bị nhập như máy scan, bàn phím, chuột,..
Câu 11.10: Chức năng nào trong số sau đây là một trong số các chức năng của một phần mềm ứng dụng
Phân chia bộ nhớ chính
Thực hiện thao tác đổi bộ nhớ
Truy vấn tin từ cơ sở dữ liệu khách hàng (ĐA)
Phản hồi khi có lỗi
Câu 11.11: Phần mềm nào trong số sau đây không là phần mềm ứng dụng 
Phần mềm hệ điều hành (ĐA)
Chương trình quản lý tồn kho
Gói phần mềm bảng tính
Phần mềm xử lý văn bản
Câu 11.12: ………. Có chức năng như một bản hướng dẫn đối với phần cứng trong một HTTT
Phần mềm (ĐA)
Chính sách
Cơ sở dữ liệu
Thủ tục
Câu 11.13: Phần mềm nào sau đây không phải là một phần mềm ứng dụng ?
Phần mềm điều khiển thiết bị  (ĐA)
Chương trình quản lý tồn kho
Gói phần mềm bảng tính
Chương trình xử lý văn bản
Câu 11.14: phát biểu nào sau đây là đúng
Phần mềm mã nguồn mở không có bản quyền
Phần mềm mã nguồn mở không có bảo hành  (ĐA)
Phần mềm mã nguồn mở gây hại cho người sử dụng
Phần mềm mã nguồn mở không cho phép phân phối lại
Câu 11.15: Phần mềm nào sau đây là phần mềm ứng dụng
Phần mềm điều khiển thiết bị
Hệ điều hành
Gói phần mềm bảng tính (ĐA)
Chương trình dịch

7.42.01.Trong hàm quy hồi, biến nào là biến phụ thuộc
Biến giải thích
Biến đầu vào
Biến kết quả (ĐA)
Biến thích ứng-
7.42.02: Trong hàm hồi quy, biến nào là biến độc lập ?
A.Biến giải thích  (ĐA)
B. Biến đầu vào
C.Biến kết quả
D. Biến thích ứng
7.42.03: Để hiển thị phương trình đường xu thế trên biểu đồ trong Excel, ta chọn ô kiểm nào trong hộp thoại Format Trendline:  
Display equation on chart (ĐA)
Display R-squared value on chart
Display both equation and R-squared value on chart
Display R’ on chart
7.42.04: Để đổi kiểu đường xu thế trong Excel, ta click chuột phải vào đường xu thế và chọn:
Edit Trendline
Format Trendline (ĐA)
Remove Trendline
Add Trendline
7.42.05: Mục nào trong công cụ Excel Solver phải đặt giới hạn hoặc yêu cầu được đặt giá trị ô được sử dụng:
Set Objective
Subject to the Constraints
Parameters  (ĐA)
By changing variable cells
7.42.06: Công ty A đang xem xét 4 hoạt động khả thi và sẽ chấp nhận chúng nếu tỷ lệ hoàn vốn nội bộ IRR từ 10% trở lên, như xuất hiện trong ô E2, công thức được sử dụng trong ô C2, công thức này cũng có thể được sao chép xuống ô C3 đến C5, để tạo ra kết quả cần thiết là gì ?      

=IF(B2>=F2, “Chấp nhận”, “Hủy bỏ”)
=IF(B2>=SES2, “Chấp nhận”, “Hủy bỏ”)  (ĐA)
=IF(B2>=SE2,“Chấp nhận”, “Hủy bỏ”)
=IF(B2>=ES2, “Chấp nhận”, “Hủy bỏ”)
7.42.07: Công cụ nào sau đây có thể được sử dụng cho Phân tích What-if trong Excel ?
Goal seek
Scenario Manager
Cả A và B (ĐA)
Data Validation
7.42.08: Mục đích của Tìm kiếm Mục tiêu (Goal Seek) trong phân tích What-if là gì ?
Để tìm giá trị lớn nhất trong một tập dữ liệu
Để tìm ra giá trị nhỏ nhất trong một tập dữ liệu
Để tìm ra giá trị đầu vào cụ thể tạo ra giá trị đầu ra mong muốn  (ĐA)
Để tìm ra giá trị đầu ra mong muốn với giá trị đầu vào cụ thể
7.42.09: Cho bảng dữ liệu tổng hợp hàng hóa như sau: 
Để phục vụ nhu cầu quản lý, có thể tạo ra từ bảng dữ liệu này các thông tin, trừ:

Tổng doanh thu mỗi nhân viên đạt được  (ĐA)
Tổng doanh thu mỗi năm
Tổng doanh thu từ mỗi nhóm hàng
Dùng PivotTable với tham số Column là “Năm”, Values là “Doanh thu” và Summarize Value By là “SUM”
7.42.10: Cho bảng dữ liệu tổng hợp hàng bán như sau:
Để tính tổng doanh thu mỗi năm, có thể dùng cách nào sau đây:

Dùng Private Table với tham số Row là “Năm”, Values là “Doanh thu” và Summarize Value By là “SUM”
Dùng Subtotal với tham số At each change là “Năm”, Use Function là “SUM” và Add Subtotal To là “Doanh thu” (sau khi đã sắp xếp bảng tăng dần theo năm)
Dùng Private Table với tham số Column là “Năm”, Values là “Doanh thu” và Summarize Value By là “SUM” (ĐA)
Cả A,B,C

43.01: Phân tích hồi quy bội bao gồm:
Một biến phụ thuộc và một biến độc lập
Một biến phụ thuộc và nhiều biến độc lập (ĐA)
Nhiều biến phụ thuộc và một biến độc lập
Nhiều biến phụ thuộc và nhiều biến độc lập
43.02: Cho bảng dữ liệu quản lý nhân sự như sau:
Sử dụng hàm nào để tính tổng tiền lương của các nhân viên làm việc ở phòng Tài chính ?

SUMIFS
SUM
SUMIF (ĐA)
SUMI
43.03: Cho bảng dữ liệu quản lý nhân sự như sau:
Sử dụng hàm nào để tính tổng tiền lương của các nhân viên Nữ làm việc ở phòng Tài chính?

SUMIF()
SUM()
SUMPRODUCT()
SUMIFS() (ĐA)
Note: ĐỐI VỚI ĐỀ BÀI LỚN HƠN 2 YÊU CẦU -> CHỌN HÀM SUMIFS
43.05: Trong SOLVER, để giải quyết bài toán tối ưu hóa, người dùng cần thiết phải thiết lập các thành phần nào ?
Hàm mục tiêu, biến và ràng buộc (ĐA)
Hàm mục tiêu và biến
Hàm mục tiêu và ràng buộc
Biến và ràng buộc
43.06: Một khách hàng mua theo hình thức trả góp một xe ô tô trị giá 600tr đồng trong vòng 4 năm. Biết lãi suất nhà cung cấp đưa ra là 9%/năm và khách hàng phải thực hiện trả góp định kì vào cuối mỗi tháng. Để tính số tiền trả góp hàng tháng bằng hàm PMT, cần sử dụng các đối số RATE và NPER với các giá trị lần lượt như sau:
9%, 4
0,75%, 48 (ĐA)
9%,48
0,75%, 4
43.07: Một người lập kế hoạch tiết kiệm chuẩn bị cho cuộc sống sau khi nghỉ hưu như sau: cuối mỗi năm trong 40 năm tới gửi vào tiết kiệm $2000 với lãi suất 8%/năm. Hãy sử dụng hàm FV để tính giá trị tương lai của dòng tiền đầu tư với các đối số cụ thể như sau:
=FV(8%,40,-2000,0,0) (ĐA)
=FV(8%,40,-2000,0,1)
=FV(8%,40*12,-2000,0,1)
=FV(8%,40*12,-2000,0,0)
43.08: Một Công ty dự kiến thu nhập của họ sẽ là $180,000 cho năm 2014-2018. Hàm nào phải được nhập vào ô E6 để hiển thị thu nhập trong năm 2016 nếu nó vượt quá ngân sách, nếu không nó sẽ hiển thị 0 ?
=IF(E2<SBS6,E2,0)
=IF(E2<SBS6,0,E2)
=IF(E2>SBS6,E2,0) (ĐA)
=IF(E2>SBS6,0,E2)
43.09: Cho bảng dữ liệu quản lý nhân sự như sau:
Sử dụng hàm nào để đếm số nhân viên Nam làm việc ở phòng Marketing ?

COUNTIF
COUNTIFS (ĐA)
COUNTA
COUNTBLANK
43.10: Một khách hàng muốn thực hiện một khoản vay ngân hàng trong vòng 15 năm với lãi suất 6%/năm. Ngân hàng cho phép khách hàng có thể trả góp $2.000.000 vào cuối kỳ mỗi năm. Để xác định..
Cả B và D (ĐA)
Công cụ Goal Seek
Công cụ Regression
Công cụ Solver


4.34.1: B2C là:
Xử lý các giao dịch mua bán hàng hóa giữa công ty và khách lẻ (ĐA)
Xử lý các giao dịch mua bán hàng hóa giữa các công ty
Xử lý các giao dịch mua bán hàng hóa giữa công ty và chính phủ
Xử lý các giao dịch mua bán hàng hóa giữa các chính phủ
4.34.2: Trong mô hình Thương mại điện tử B2G, công ty bán hàng hóa cho:
Một nhóm các công ty
Một nhóm khách lẻ
Chính phủ (ĐA)
Các công ty khác
4.34.3: 

4.34.4: C2G là?
A.Giao dịch thương mại điện tử giữa người tiêu dùng với cơ quan công quyền nhà nước (ĐA)
B.Giao diện thương mại điện tử giữa 2 cơ quan nhà nước với nhau
C.Giao diện thương mại điện tử giữa nhà nước với doanh nghiệp
D.Giao diện thương mại điện tử giữa doanh nghiệp với người tiêu dùng
4.34.5: G2G là:
A.Giao dịch thương mại điện tử giữa người tiêu dùng với cơ quan công quyền nhà nước
B.Giao diện thương mại điện tử giữa 2 cơ quan nhà nước với nhau (ĐA)
C.Giao diện thương mại điện tử giữa nhà nước với doanh nghiệp
D.Giao diện thương mại điện tử giữa doanh nghiệp với người tiêu dùng
4.34.6:: Tất cả các thuật ngữ sau đều tương đương với thuật ngữ Thương mại điện tử, trừ:
A.Thương mại trực tuyến
B.Thương mại điều khiển học
C.Kinh doanh các mặt hàng điện tự (ĐA)
D.Thương mại không giấy tờ
4.34.7:: Trình tự các công đoạn chính của Thương mại điện tử: 
A.Đặt hàng, thanh toán, thông tin, giao hàng, hỗ trợ sau bán hàng
B.Thông tin, đặt hàng, thanh toán, giao hàng, hỗ trợ sau bán hàng  (ĐA)
C.Thông tin, đặt hàng, thanh toán, giao hàng, kiểm tra mức tồn kho
D.Đặt hàng, giao hàng, thanh toán, thông tin, hỗ trợ sau bán hàng
4.34.8: Hoạt động mua bán hàng hóa qua mạng Internet được gọi là:
A.E-commerce (ĐA)
B.E-business 
C. Intranet
D. Extranet 
4.34.9: Việc sử dụng công nghệ kỹ thuật số và Internet để thực hiện các quy trình kinh doanh chính trong doanh nghiệp được gọi là
A. E-commerce 
B. E-business (ĐA)
C. Enterprise applications
D. MIS

4.34.10: Mạng ___ dùng cho Thương mại điện tự giữa các Doanh nghiệp với nhau
A.Mạng Intranet 
B. Mạng Extranet (ĐA)
C. Mạng LAN
D. Cả A và B 



Câu 1: Tội phạm điện tử ( E-Crimes) là gì?
A.Là dạng tội phạm nhắm đến đối tượng là các thiết bị điện tử 
B.Là dạng tội phạm nhắm đến đối tượng là các thẻ tín dụng điện tử
C.Là dạng tội phạm có sử dụng máy tính hoặc một phương tiện điện tử trong quá trình thực hiện tội phạm  (ĐA)
D. Là dạng tội phạm nhắm đến các máy ATM rút tiền 
Câu 2: Tội phạm Internet (cybercrimes ) là gì?
A.Là dạng tội phạm có sử dụng máy tính và mạng, đặc biệt là mạng Internet để thực hiện các hành vi tấn công các máy tính 
B. Là dạng tội phạm có sử dụng máy tính và mạng, đặc biệt là mạng Internet để thực hiện các hành vi tấn công các cơ quan cơ sở dữ liệu
C. Là dạng tội phạm có sử dụng máy tính và mạng, đặc biệt là mạng Internet để thực hiện các hành vi tấn công các tổ chức tài chính 
D. Tất cả phương án trên  (ĐA)
Câu 3: Phương án nào không phải là hành vi của tội phạm điện tử?
A.Xâm nhập hệ thống, cảnh cáo về lỗ hổng bảo mật cho người quản trị (ĐA)
B. Đánh cắp mật khẩu, giả mạo để truy nhập thông tin
C. Xâm nhập hệ thống để lấy cắp, sửa đổi thông tin
D. Dùng Virus làm hỏng dữ liệu hoặc làm tê liệt hoạt động của hệ thống 
Câu 4: Tội phạm tấn công dữ liệu là gì? 
A.Là tội phạm dùng các kỹ thuật lập trình để thay đổi chương trình máy tính một cách trực tiếp hoặc gián tiếp 
B. Là tội phạm làm cho dữ liệu nhập không chính xác vào máy tính hoặc làm sai lệch, sửa xóa các dữ liệu hiện thời (ĐA)
C. Là tội phạm làm cho dữ liệu không thể nhập lên máy tính
D. Là tội phạm thực hiện hành vi dùng kỹ thuật lập trình để mở các tủ tài liệu lưu trữ 
Câu 5: Tội phạm tấn công chương trình là gì?
A.Là tội phạm dùng các kỹ thuật lập trình để thay đổi chương trình máy tính một cách trực tiếp hoặc gián tiếp  (ĐA)
B. Là tội phạm làm cho dữ liệu nhập không chính xác vào máy tính hoặc làm sai lệch, sửa xóa các dữ liệu hiện thời
C. Là tội phạm làm cho dữ liệu không thể nhập lên máy tính 
D. Là tội phạm thực hiện hành vi dùng kỹ thuật lập trình để mở các tủ tài liệu lưu trữ 
Câu 6: Phương án nào là công nghệ hỗ trợ đảm bảo an toàn thông tin hiện nay?
A.Tường lửa ( FIREWALL ) và máy chủ PROXY ( Proxy Server )
B. Mã hóa và mạng riêng tư 
C. Xác thực định danh và hệ thống quản trị truy cập 
D. Tất cả các phương án trên  (ĐA)
Câu 7: Các hoạt động mức kiểm soát tổng thể của HTTT?
A. Kiểm soát quá trình triển khai hệ thống; Kiểm soát phần mềm; Kiểm soát phần cứng; Kiểm soát an toàn dữ liệu; Kiểm soát xử lý 
B. Kiểm soát quá trình triển khai hệ thống; Kiểm soát phần mềm; Kiểm soát phần cứng; Kiểm soát an toàn dữ liệu; Kiểm soát hành chính  (ĐA)
C. Kiểm soát quá trình triển khai hệ thống; Kiểm soát phần mềm; Kiểm soát phần cứng; Kiểm soát đầu vào; Kiểm soát hành chính 
D. Kiểm soát quá trình triển khai hệ thống; Kiểm soát phần mềm; Kiểm soát phần cứng; Kiểm soát đầu ra; Kiểm soát hành chính 
Câu 8: Các hoạt động mức kiểm soát ứng dụng của HTTT?
A.Kiểm soát đầu vào, kiểm soát an toàn dữ liệu; Kiểm soát đầu ra
B. Kiểm soát đầu vào; Kiểm soát xử lý; Kiểm soát hành chính 
C.Kiểm soát an toàn dữ liệu; Kiểm soát xử lý; Kiểm soát đầu ra
D. Kiểm soát đầu vào; Kiểm soát xử lí; kiểm soát đầu ra  (ĐA)
Câu 9: Chính sách an toàn thông tin ( Information Security Policy ) là gì ?
A. Là văn bản trong đó quy định rõ những gì được phép đối với việc sử dụng thông tin trong tổ chức 
B. Là văn bản trong đó quy định rõ những gì không được phép đối với việc sử dụng thông tin trong tổ chức 
C. Là văn bản trong đó quy định rõ những hình thức xử lý các vi phạm tương ứng trong việc sử dụng thông tin 
D. Tất cả các phương án trên  (ĐA)
Câu 10: Công việc của Phó giám đốc an toàn thông tin ( Chief Information Security Officer ) là gì?
A.Xác định các rủi ro liên quan đến an toàn thông tin của tổ chức  (ĐA)
B.Xây dựng và triển khai các biện pháp đối phó hiệu quả với các rủi ro 
C.Loại trừ tất cả các rủi ro 
D. Cả A và B 


Câu 1: Khi lập kế hoạch các HTTT trong tổ chức doanh nghiệp, để xác định các tiến trình nghiệp vụ đặc thù,người ta sử dụng
Mô hình năm lực lượng cạnh tranh
Chuỗi giá trị Value Chain (ĐA)
Phân tích chi phí và lợi ích (Benefit and Cost Analysis)
Cả A và C
Câu 2: HTTT gia tăng giá trị cho hoạt động chính “Sản xuất ” trong chuỗi giá trị là:
HTTT thiết kế sản phẩm có trợ giúp của máy tính - CAD (Computer-Aided- Design)
HTTT sản xuất có trợ giúp của máy tính - CAM ( Computer - Aided- Manufacturing) (ĐA)
Hệ thống trao đổi dữ liệu điện tử - EDI ( Electronic Dât Interchange)
Cả A và C
Câu 3: Các hoạt động chính của giai đoạn thiết kế HTTT bao gồm:
Thiết kế giao diện vào/ra, thiết kế CSDL và thiết kế tài liệu hướng dẫn sử dụng
Thiết kế giao diện vào/ ra, thiết kế CSDL và thiết kế logic xử lí (ĐA)
Thiết kế CSDL, thiết kế logic xử lí và thiết kế biểu mẫu nhập liệu
Thiết kế logic xử lí, thiết kế báo cáo đầu ra và thiết kế CSDL
Câu 4: Tái thiết kế quy trình nghiệp vụ trong các tổ chức doanh nghiệp là cần thiết vì những lý do:
Nhu cầu nâng cao hiệu quả chuỗi cung cập, nâng cao chất lượng dịch vụ khách hàng và quản trị quan hệ khách hàng
Nhu cầu tham gia kinh doanh- thương mại điện tử và Marketing trực tuyến
Nhu cầu quản lý chuyên nghiệp các quy trình nghiệp vụ trong tổ chức doanh nghiệp
Cả A và B  (ĐA)
Câu 5: Để đảm bảo ứng dụng thành công CNTT trong tổ chức doanh nghiệp, cần có:
Sự đồng thuận và hỗ trợ của cấp lãnh đạo, sự tham gia hiệu quả của người sử dụng
Sự tham gia hiệu quả của người sử dụng và sự hỗ trợ mang tính chuyên nghiệp của các nhà cung ứng giải pháp CNTT
Có mô tả yêu cầu hệ thống rõ ràng, có kế hoạch triển khai mang tính khả thi
Cả A và C (ĐA)
Câu 6: Cải tiến giao diện của HTTT nhằm làm tăng tính thân thiện của hệ thống với người sử dụng là một ví dụ về:
Bảo trì hiệu chính
Bảo trì thích nghi
Bảo trì hoàn thiện (ĐA)
Bảo trì phòng ngừa
Câu 7: Mức độ ứng dụng CNTT theo trình tự từ thấp đến cao là:
Tự động hóa, tái thiết kế các tiến trình nghiệp vụ, hợp lý hóa các thủ tục, đổi mới toàn diện tổ chức 
Tự động hóa, đổi mới toàn diện, hợp lý hóa các thủ tục, tái thiết kế các tiến trình nghiệp vụ
Hợp lí hóa các thủ tục, tự động hóa, tái thiết kế các tiến trình nghiệp vụ, đổi mới toàn diện tổ chức
Tự động hóa, hợp lý hóa các thủ tục, tái thiết kế các tiến trình nghiệp vụ, đổi mới toàn diện tổ chức (ĐA)
Câu 8: Các chiến lược chuyển đổi HTTT bao gồm:
Chuyển đổi trực tiếp, chuyển đổi song song, chuyển đổi một lần và chuyển đổi theo pha
Chuyển đổi trực tiếp, chuyển đổi song song, chuyển đổi theo pha và chuyển đổi thí điểm (ĐA)
Chuyển đổi theo pha, chuyển đổi thí điểm, chuyển đổi trực tiếp và chuyển đối nhiều lần
Chuyển đổi song song, chuyển đổi trực tiếp, chuyển đổi thí điểm và chuyển đổi tạm thời 
Câu 9: Giai đoạn phân tích hê thống thông tin bao gồm:
Xác định yêu cầu hệ thống và lập trình thực hiện các yêu cầu đó.
Mô hình hoá các yêu cầu hệ thống cà thiết kế logic xử lý các yêu cầu đó
Xác định và mô hình các yêu cầu hệ thống (ĐA)
Không có lựa chọn nào đúng
Câu 10: Giai đoạn phân tích hệ thống thông tin bao gồm:
Xác định yêu cầu hệ thống và lập trình thực hiện các yêu cầu đó
Mô hình hóa các yêu cầu hệ thống
Xác định và mô hình hóa các yêu cầu hệ thống (ĐA)
Không có lựa chọn nào đúng



Câu 1: Tất cả đều là hoạt động cơ bản trong chuỗi giá trị, trừ:
Hậu cần đầu vào
Quản trị nguồn nhân lực (ĐA)
sản xuất tác nghiệp
Dịch vụ say bán hàng

Câu 2:___ là một ví dụ về hoả động chính trong chuỗi giá trị
Xử lý đơn hàng tự động (ĐA)
Thiết kế có sự trợ giúp của máy tính
Lập kế hoạch nhân sự tự động 
Mua sắm phụ tùng trực tuyến

Câu 3: Tất cả đều là phần mềm hỗ trợ hoạt động Marketing, trừ:
Phần mềm trợ giúp nhân viên bán hàng
Phần mềm trợ giúp quản lý các nhân viên bán hàng
Phần mềm trợ giúp quản lý chương trình bán hàng qua điện thoại
Phần mềm MRP  (ĐA)
Câu 4: Hệ chuyên gia tài chính sử dụng dữ liệu do….. Cung cấp
Các hệ chuyên gia chuyên biệt khác
HTTT quản lý tài chính (ĐA)
Các HTTT xử lý giao dịch liên quan
HTTT kế toán
Câu 5: Mô hình EOD hỗ trợ các nhà quản lý
Mức lãnh đạo
Mức tác nghiệp
Mức chiến thuật
Cả A,B và C (ĐA)
Câu 6: Các giai đoạn của quản trị quan hệ khách hàng bao gồm:
Khai thác khách hàng mới, duy trì khách hàng, giữ mối quan hệ khách hàng
Khai thác khách hàng mới, nâng cao chất lượng dịch vụ khách hàng, duy trì khách hàng (ĐA)
Duy trì khách hàng, nâng cao chất lượng dịch vụ khách hàng, chăm sóc khách hàng
Khai thác khách hàng mới, nâng cao chất lượng dịch vụ khách hàng, tìm kiếm khách hàng tiềm năng trong xã hội
Câu 7: Trong quản lý sản xuất, MRP là viết tắt của:
Material Request Plan
Material Requirement Production
Material Requirement Planning (ĐA)
Material Requirement Production
Câu 8: Hệ thống nào sau đây không thuộc mức tác nghiệp
Hệ thống mua hàng
Hệ thống kiểm tra chất lượng sản phẩm
Hệ thống JIT (ĐA)
Hệ thống kế toán chi phí giá thành
Câu 9: Chu trình xử lý tài liệu văn bản bao gồm các hoạt động:
Nhập và xử lý tài liệu
Lưu trữ và đưa ra tài liệu
Nhân bản và phân phối tài liệu
Tất cả A,B,C đều đúng (ĐA)
Câu 10: Quản trị quan hệ khách hàng cho phép tổ chức
Xác định và nhắm tới các khách hàng tiềm năng nhất
Tùy chỉnh và cá nhân hóa sản phẩm theo nhu cầu của khách hàng
Áp dụng kinh nghiệm chăm sóc và dịch vụ khách hàng có chất lượng cao cho mọi điểm giao dịch
Tất cả A,B,C đều đúng (ĐA)



Câu 1: Trong ngữ cảnh ra quyết định, yếu tố nào sau đây là quan trọng nhất, ảnh hưởng đến chất lượng của các quyết định
Khả năng phần cứng HTTT để xử lý lượng dữ liệu khổng lồ với tốc độ mong muốn
Các chương trình phần mềm và các thuật toán có khả năng tạo ra các kết quả chính xác
Quá trình tư duy và diễn giải thông tin của người ra quyết định (ĐA)
Các thủ tục có ảnh hưởng đến việc thực thi các quyết định
Câu 2: Tìm giá trị trung bình của một bộ các giá trị đơn lẻ là một ví dụ về kết xuất….từ…..:
Tập con, tập lớn
Thông tin, dữ liệu (ĐA)
Tri thức, thông tin
Dữ liệu, thông tin
Câu 3: Thông tin có tính kinh tế có nghĩa là:
Thông tin có được với chi phí thấp nhất
Giữa chi phí bỏ ra để có được thông tin và giá trị mà thông tin mang lại có quan hệ hợp lý (ĐA)
Thông tin mang lại giá trị lớn nhất
Thông tin đem lại lợi ích cho nhiều người nhất với chi phí thấp nhất
Câu 4: HTTT dưới góc độ kỹ thuật có thể được hiểu là một hệ thống các thành phần có quan hệ tương tác, nhằm thực hiện các chức năng thu thập, xử lý, lưu trữ và truyền đạt thông tin hỗ trợ
Hoạt động ra quyết định và kiểm soát trong một tổ chức (ĐA)
Truyền thông và luồng dữ liệu
Các cán bộ quản lý phân tích các dữ liệu thô của tổ chức
Quá trình tạo ra các sản phẩm và dịch vụ mới
Câu 5: Quyết định có thể xác định được theo một trình tự thủ tục gọi là quyết định….
Có cấu trúc (ĐA)
Không có cấu trúc
Không có tài liệu
Bán cấu trúc
Câu 6: Tính lương cho công nhân được xếp vào phạm trù ra quyết định
Có cấu trúc (ĐA)
      B .Không có cấu trúc
      C. Không có tài liệu
      D. Bán cấu trúc
Câu 7: HTTT quản lý, HTTT hỗ trợ ra quyết định và HTTT hỗ trợ lãnh đạo đều sử dụng dữ liệu do…..cung cấp:
Hệ chuyên gia ES
Hệ quản lý tri thức KMS
Hệ thống thông tin xử lý giao dịch TPS (ĐA)
Cả A,B,C
Câu 8: Bài toán tìm kiếm giải pháp tối ưu cho các bài toán phân bổ các nguồn lực (nhân lực, tài lực,..) vốn dĩ hạn hẹp trong các tổ chức doanh nghiệp có thể được giải bằng
HTTT hỗ trợ ra quyết định DSS (ĐA)
HTTT nhân lực
HTTT tài chính
Cả B và C
Câu 9: Dữ liệu đầu vào của HTTT hỗ trợ lãnh đạo có nguồn gốc:
Từ bên ngoài môi trường kinh doanh
Từ bên trong doanh nghiệp phản ánh các hoạt động tác nghiệp hàng ngày


Cả A và B Đáp án
Câu 10: Một trong số các mục tiêu của HTTT xử lý giao dịch TPS là:
Thu thập, xử lý, lưu trữ và tạo ra các tài liệu nghiệp vụ

Câu 1: Một ứng dụng xử lý dữ liệu sau đó phân phối thông tin tới người sử dụng hợp lệ và tập trung vào việc tạo ra các thông tin hữu ích từ các nguồn dữ liệu có ích được gọi là:
Ứng dụng phân tích và trình bày dữ liệu
Câu 2: Các CSDL quản lý thường là một tập con hoặc là tích hợp của các


CSDL tác nghiệp
Câu 3: Hoạt động nào sau đây là thử thách nhất với một tổ chức:


Thay đổi các quy trình thủ tục, đòi hỏi con người thay đổi phương thức làm việc


Câu 4: HTTT dưới góc độ kỹ thuật có thể được hiểu là một hệ thống các thành phần có quan hệ tương tác, nhằm thực hiện các chức năng thu thập, xử lý, lưu trữ và truyền đạt thông tin hỗ trợ
A.Hoạt động ra quyết định và kiểm soát trong một tổ chức

Câu 5: Một…tương đương 1024G
Terabyte


Câu 6: Hoạt động nào sau đây không liên quan đến máy chủ ?
Xử lý văn bản

Câu 7: Yếu tố nào sau đây là thành phần của HTTT nhưng không được xem là yếu tố công nghệ ?

Thủ tục

Câu 8: Ứng dụng nào sau đây thường sử dụng các tệp tuần tự
Ứng dụng xử lý lương theo lô
Câu 9: Chương trình ứng dụng nào sau đấy gần như phải được tổ chức xây dựng thay vì 
Hệ hỗ trợ ra quyết định


Câu 10: Lựa chọn nào là một trong năm lý do chính của việc kết nối mạng các máy tính và các thiết bị liên quan ?
Tất cả các lựa chọn trên



01: Phân tích hồi quy bội bao gồm:

Một biến phụ thuộc và nhiều biến độc lập

02: Trong phương pháp dự báo bằng đường xu thế, ta sử dụng đường xu thế để:
Dự báo giá trị tương lai của biến phụ thuộc dựa trên giá trị hiện tại của biến độc lập
03: Kiểu biểu đồ nào được sử dụng để so sánh một cách trực quan Doanh thu của 10 cửa hàng trong một hệ thống bán lẻ ?

Bar Chart

04: Trong công cụ Data Analysis của MS Excel, phân tích hồi quy tuyến tính đơn được sử dụng để làm gì:
Tìm ra mối quan hệ giữa hai biến trong một tập dữ liệu

05: Cho bảng dữ liệu theo dõi thanh toán tiền phòng của một khách sạn như sau:
Để xác định tiền phòng của một khách hàng căn cứ trên mã của người đó, có thể dùng hàm:
DGET ()
06. Thành phần nào của phân tích hồi quy tuyến tính đơn được sử dụng để đánh giá mức độ đánh giá mức độ chính xác của mô hình hồi quy ?
Hệ số xác định R’’
07. Cho bảng dữ liệu quản lý nhân sự như sau:
Sử dụng hàm nào để tính tổng tiền lương của các nhân viên Nữ làm việc ở phòng Tài chính?

D. SUMIFS()
08: Trong SOLVER, hàm mục tiêu được định nghĩa như thế nào?
Cả A,B,C đều đúng
09: Cho biết nhà máy sản xuất 4 loại sản phẩm. Biết lợi nhuận đơn vị, chi phí nhân công đơn vị, chi phí giờ máy đơn vị, nhu cầu về số lượng mỗi loại sản phẩm, biết giới hạn giờ công lao động và giới hạn giờ máy. Để xác định gói sản phẩm tối ưu, sao cho tổng lợi nhuận thu được từ các sản phẩm sản xuất được là lớn nhất có thể dùng công cụ nào sau đây ?
Solver
10: Một cửa hàng dự kiến đưa vào kinh doanh một loại nước giải khát mới. Biết chi phí đơn vị, chi phí cố định cho hoạt động kinh doanh và cầu thị trường trong tháng đầu tiên. Để định giá bán cho sản phẩm mới này sao cho lợi nhuận tháng đầu tiên đạt $45,000, có thể dùng công cụ nào ?
Cả B và C

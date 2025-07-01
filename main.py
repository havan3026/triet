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




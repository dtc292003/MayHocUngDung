s1 =''' anh chị tư vấn giúp nếu em chọn hai ngành tài chính marketing có hợp lý và dễ xin việc khi ra trường không . ngành human resources quản trị nhân lực thì nên học kết hợp với ngành nào và công việc sau này là gì . với marketing em nên học chuyên ngành nào để phù hợp với sở thích làm thương mại . trường quốc tế phân chuyên ngành rất sâu khác với các đh việt nam . em lo nếu chọn không đúng sau này về nước sẽ khó xin việc đúng chuyên môn . mọi người cho em lời khuyên nên chọn học ngành gì để phù hợp với môi trường tuyển dụng của việt nam hiện nay . cảm ơn mọi người . nguyễn đăng thiện độc giả đặt câu hỏi tư vấn tại đây .'''
s2 = ''' trong đề toán chung dành cho tất cả thí sinh thi vào phổ thông năng khiếu của kỳ thi tuyển sinh vào lớp 10 vừa qua có một bài toán gây bất ngờ cho thí sinh phụ huynh và cả thầy cô giáo về cách đặt câu hỏi… không giống ai . dù vậy đa số chuyên gia đánh giá đây là bài toán hay cách đặt vấn đề thú vị và bất ngờ học sinh tỉnh táo một chút có thể xử lý tốt . mời bạn đọc cùng thử sức . đề bài lớp 9a có 27 học sinh nam và 18 học sinh nữ . nhân dịp sinh nhật bạn x là một thành viên của lớp các bạn trong lớp có rất nhiều món quà tặng x ngoài ra mỗi bạn nam của lớp làm 3 tấm thiệp và mỗi bạn nữ xếp 2 hoặc 5 con hạc để tặng bạn x biết số tấm thiệp và số con hạc bằng nhau hỏi bạn x là nam hay nữ . ts trần nam dũng đh khoa học tự nhiên đh quốc gia tp hcm .'''
vocab = []
# Xóa các kí tự xuống dòng . tách thành các từ theo khoảng trắng
s1_slipted = s1.replace('\n', '').split() 
s2_slipted = s2.replace('\n', '').split()
for word in s1.split(): # Duyệt các từ trong biến s1.split lưu vào word
    word = word.strip() # Xóa khoảng trắng đầu và cuối
    if word not in vocab: # Kiểm tra xem từ có trong vocab chưa
        vocab.append(word) # Chưa thì thêm vào vocab

for word in s2.split():
    word = word.strip()
    if word not in vocab:
        vocab.append(word)
print(len(vocab))
print(vocab)


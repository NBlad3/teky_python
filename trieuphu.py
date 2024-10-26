import time
import random

question_list = [
    ["Đâu là một loại hình chợ tạm tự phát thường xuất hiện trong các khu dân cư?", "A: Ếch", "B: Cóc", "C: Thằn lằn", "D: Nhái", "B"],
    ["Đâu là tên một bãi biển ở Quảng Bình?", "A: Đá Lăn", "B: Đá Nhảy", "C: Đá Chạy", "D: Đá Bò", "B"],
    ["Haiku là thể thơ truyền thống của nước nào?", "A: Nhật Bản", "B: Mông Cổ", "C: Trung Quốc", "D: Hàn Quốc", "A"],
    ["Đâu là tên một loại bánh Huế?", "A: Khoái", "B: Sướng", "C: Thích", "D: Vui", "A"],
    ["Tượng đài Chiến thắng Điện Biên Phủ tại chiến trường xưa được dựng trên ngọn đồi nào?", "A: Đồi Him Lam", "B: Đồi A1", "C: Đồi C1", "D: Đồi D1", "D"],
    ["Màu chủ đạo của tờ tiền Polymer mệnh giá 500.000 đồng là gì?", "A: Đỏ", "B: Xanh", "C: Vàng", "D: Tím", "B"],
    ["Chiến trường Đắk Tô - Tân Cảnh, nơi diễn ra chiến thắng vang dội năm 1972, nay thuộc địa bàn tỉnh nào ở Tây Nguyên?", "A: Kon Tum", "B: Đắk Lắk", "C: Gia Lai", "D: Đắk Nông", "A"],
    ["Bảo tàng Hồ Chí Minh được thiết kế theo dáng một loài hoa nào?", "A: Hoa sen", "B: Hoa hướng dương", "C: Hoa hồng", "D: Hoa đào", "A"],
    ["Tháng âm lịch nào còn được gọi là 'Tháng cô hồn'?", "A: Tháng bảy", "B: Tháng tám", "C: Tháng chín", "D: Tháng mười", "A"],
    ["Có câu thành ngữ: 'Đi mây về ...' gì?", "A: Mây", "B: Núi", "C: Biển", "D: Gió", "D"],
    ["Đâu là một cách nói ví von về những trường hợp hay gặp vận hạn, rủi ro?", "A: Sao quả cân", "B: Sao quả yến", "C: Sao quả tạ", "D: Sao quả tấn", "C"],
    ["Gỗ mun có màu gì?", "A: Vàng", "B: Nâu", "C: Đen", "D: Xanh", "C"],
    ["Tân Tổng thống Ukraine Volodymyr Zelensky làm nghề gì trước khi nhậm chức?", "A: Võ sĩ quyền anh", "B: Diễn viên hài", "C: Bác sĩ phẫu thuật", "D: Doanh nhân", "B"],
    ["Tình cảnh đơn độc, yếu thế không có chỗ dựa là nghĩa của câu nào?", "A: Thân lừa ưa nặng", "B: Thân tàn ma dại", "C: Thân cô thế cô", "D: Thân làm tội đời", "C"],
    ["Vườn quốc gia nào hiện không nằm trong danh sách Vườn di sản ASEAN?", "A: Vườn quốc gia Kon Ka Kinh", "B: Vườn quốc gia Tam Đảo", "C: Vườn quốc gia Chư Mom Ray", "D: Vườn quốc gia Bái Tử Long", "B"]
]

def goi_ban(i):
    temp_list = ["A", "B", "C", "D"]
    if random.randint(1, 100) <= 70:
        print(f"\nTôi nghĩ là {question_list[i][5]}\n")
    else:
        temp_list.remove(question_list[i][5])
        print(f"\nTôi nghĩ là {random.choice(temp_list)}\n")

def fifty_fifty(i):
    temp_list = ["A", "B", "C", "D"]
    temp_list.remove(question_list[i][5])
    ff_list = [question_list[i][5], random.choice(temp_list)]
    ff_list.sort()
    print(f"\n{ff_list[0]} hoặc {ff_list[1]}\n")

def hoi_moi_nguoi(i):
    perm_list = ["A", "B", "C", "D"]
    hmn_list = [0, 0, 0, 0]
    index = perm_list.index(question_list[i][5])
    for k in range(100):
        temp_list = ["A", "B", "C", "D"]
        if random.randint(1, 100) <= 70:
            hmn_list[index] += 1
        else:
            temp_list.remove(question_list[i][5])
            wrong_letter = random.choice(temp_list)
            wrong_index = perm_list.index(wrong_letter)
            hmn_list[wrong_index] += 1
    print(f"\nA = {hmn_list[0]}%, B = {hmn_list[1]}%, C = {hmn_list[2]}%, D = {hmn_list[3]}%\n")

def play_quiz():
    print("\nHướng dẫn: Bạn chọn một trong 4 câu trả lời của câu hỏi.\n")
    time.sleep(5)

    complete = False
    gb, ff, hmn = True, True, True

    for i in range(len(question_list)):
        for j in range(5):
            print(f"{question_list[i][j]}")

        l = input("\nBạn có muốn ai giúp không? (y/n): ")
        if l.lower() == "y":
            if gb or ff or hmn:
                while True:
                    if gb:
                        print("- Gọi bạn")
                    if ff:
                        print("- 50/50")
                    if hmn:
                        print("- Hỏi mọi người")
                    m = input("Bạn muốn dùng cái gì: ")
                    if m.upper() == "GOI BAN":
                        goi_ban(i)
                        gb = False
                        for j in range(5):
                            print(f"{question_list[i][j]}")
                        user_choice = input("\nChọn: ").upper()
                        break
                    elif m == "50/50":
                        fifty_fifty(i)
                        ff = False
                        for j in range(5):
                            print(f"{question_list[i][j]}")
                        user_choice = input("\nChọn: ").upper()
                        break
                    elif m.upper() == "HOI MOI NGUOI":
                        hoi_moi_nguoi(i)
                        hmn = False
                        for j in range(5):
                            print(f"{question_list[i][j]}")
                        user_choice = input("\nChọn: ").upper()
                        break
                    else:
                        print("Bạn nhập sai")
            else:
                print("Bạn không còn ai để giúp nữa.")
                for j in range(5):
                    print(f"{question_list[i][j]}")
                user_choice = input("\nChọn: ").upper()
        else:
            for j in range(5):
                print(f"{question_list[i][j]}")
            user_choice = input("\nChọn: ").upper()

        if user_choice == question_list[i][5]:
            print("Đúng\n\n")
            if i == len(question_list) - 1:
                complete = True
                break
            if i == 4 or i == 9:
                user_input = input("Bạn muốn tiếp tục hay dừng lại\n- Tiếp tục\n- Dừng lại\nChọn: ")
                if user_input.upper() == "DUNG LAI":
                    if i == 4:
                        print("Bạn đã thắng 5,000 USD.")
                    elif i == 9:
                        print("Bạn đã thắng 50,000 USD.")
                    break
                else:
                    print("\n")
        else:
            print(f"\nSai. Bạn đã trả lời {i} câu hỏi đúng \nBye")
            break

    if complete:
        print("Chúc mừng, bạn đã thắng 1,000,000 USD.")

x = input("Ai là triệu phú?\n\n- Play\n- Exit\nChọn: ")

if x.upper() == "PLAY":
    play_quiz()
else:
    print("Bye")
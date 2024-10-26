def tinh_luong_net(luong_gross, so_nguoi_phu_thuoc):
  # Tính các khoản bảo hiểm (10.5% của lương Gross)
  bao_hiem = luong_gross * 0.105

  # Các khoản giảm trừ
  giam_tru_ban_than = 11_000_000  # Giảm trừ gia cảnh cho bản thân
  giam_tru_nguoi_phu_thuoc = 4_400_000  # Giảm trừ gia cảnh cho mỗi người phụ thuộc

  # Tính thu nhập chịu thuế
  thu_nhap_chiu_thue = luong_gross - bao_hiem - giam_tru_ban_than - (giam_tru_nguoi_phu_thuoc * so_nguoi_phu_thuoc)

  # Nếu thu nhập chịu thuế <= 0, không phải đóng thuế TNCN
  if thu_nhap_chiu_thue <= 0:
      thue_thu_nhap_ca_nhan = 0
  else:
      # Tính thuế thu nhập cá nhân dựa trên các bậc thuế
      if thu_nhap_chiu_thue <= 5_000_000:
          thue_thu_nhap_ca_nhan = thu_nhap_chiu_thue * 0.05
      elif thu_nhap_chiu_thue <= 10_000_000:
          thue_thu_nhap_ca_nhan = 5_000_000 * 0.05 + (thu_nhap_chiu_thue - 5_000_000) * 0.10
      elif thu_nhap_chiu_thue <= 18_000_000:
          thue_thu_nhap_ca_nhan = 5_000_000 * 0.05 + 5_000_000 * 0.10 + (thu_nhap_chiu_thue - 10_000_000) * 0.15
      else:
          thue_thu_nhap_ca_nhan = 5_000_000 * 0.05 + 5_000_000 * 0.10 + 8_000_000 * 0.15 + (thu_nhap_chiu_thue - 18_000_000) * 0.20

  # Tính lương Net
  luong_net = luong_gross - bao_hiem - thue_thu_nhap_ca_nhan

  return luong_net, thue_thu_nhap_ca_nhan

def main():
  # Nhập lương gross và số người phụ thuộc từ người dùng
  luong_gross = int(input("Nhập lương Gross: "))
  so_nguoi_phu_thuoc = int(input("Nhập số người phụ thuộc: "))

  # Tính lương net và thuế TNCN
  luong_net, thue_thu_nhap_ca_nhan = tinh_luong_net(luong_gross, so_nguoi_phu_thuoc)

  # Hiển thị kết quả
  if thue_thu_nhap_ca_nhan > 0:
      print(f"Thuế TNCN của bạn là: {thue_thu_nhap_ca_nhan:,.0f} VND")
  else:
      print("Bạn không phải đóng thuế TNCN")

  print(f"Lương Net của bạn là: {luong_net:,.0f} VND")

# Chạy chương trình chính
if __name__ == "__main__":
  main()
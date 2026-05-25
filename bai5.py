raw_batch = " LAP-VN-23-001 ; mou-us-24-012 ; KEY-vn-23-abc ; lap-JP-22-045 ; MOn-vn-24-099 "

# hàm xử lý và chuẩn hóa dữ liệu
def process_batch(raw_batch):
    products = raw_batch.split(";")
    result = []
    valid_count = 0

    for p in products:
        code = p.strip().upper()

        parts = code.split("-")

        if len(parts) != 4:
            continue

        product_type = parts[0]
        country = parts[1]
        year = "20" + parts[2]
        serial = parts[3]

        # kiểm tra serial
        if serial.isdigit():
            status = "Pass"
            valid_count += 1
        else:
            status = "Lỗi Serial - Reject"

        result.append([product_type, country, year, serial, status])

    return result, valid_count, len(products)


while True:
    print("\n===== HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO HÀNG =====")
    print("1. Hiển thị chuỗi mã vạch gốc")
    print("2. Giải mã, làm sạch và in báo cáo kiểm kê")
    print("3. Tra cứu nhanh theo đuôi Serial")
    print("4. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn (1-4): ")

    if choice == "1":
        print("Dữ liệu gốc:")
        print(raw_batch)

    elif choice == "2":
        data, valid_count, total = process_batch(raw_batch)

        print("\n{:<10} {:<10} {:<10} {:<10} {:<25}".format(
            "MÃ SP", "XUẤT XỨ", "NĂM SX", "SERIAL", "TRẠNG THÁI"
        ))
        print("-" * 65)

        for item in data:
            print("{:<10} {:<10} {:<10} {:<10} {:<25}".format(
                item[0], item[1], item[2], item[3], item[4]
            ))

        print(f"\nĐã giải mã thành công {valid_count} sản phẩm hợp lệ / Tổng số {total} sản phẩm.")

    elif choice == "3":
        key = input("Nhập 2 số cuối của Serial: ").strip()

        data, _, _ = process_batch(raw_batch)
        found = False

        for item in data:
            if item[3][-2:] == key:
                print("\nSản phẩm tìm thấy:")
                print("Mã:", item[0])
                print("Xuất xứ:", item[1])
                print("Năm:", item[2])
                print("Serial:", item[3])
                print("Trạng thái:", item[4])
                found = True

        if not found:
            print("Không tìm thấy sản phẩm phù hợp")

    elif choice == "4":
        print("Đóng ca kiểm kho. Chào tạm biệt!")
        break

    else:
        print("Chức năng không tồn tại, vui lòng nhập số từ 1-4!")
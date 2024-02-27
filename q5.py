def dem_so_lan_xuat_hien(duong_chuoi)
    dem = {}
    for ki_tu in duong_chuoi: 
        if ki_tu != ' ':
            dem[ki_tu] = dem.get(ki_tu, 0) + 1

    for ki_tu, so_lan in dem.items():
        print(f"{ki_tu}: {so_lan} lần")

dong_chuoi = input("Nhập dòng chữ: ")

dem_so_lan_xuat_hien(dong_chuoi)

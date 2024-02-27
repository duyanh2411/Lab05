def dem_so_lan_xuat_hien(dong_chu)
    dem = {}
    for ki_tu in dong_chu: 
        if ki_tu != ' ':
            dem[ki_tu] = dem.get(ki_tu, 0) + 1

    for ki_tu, so_lan in dem.items():
        print(f"{ki_tu}: {so_lan} lần")

dong_chu = input("Nhập dòng chữ: ")

dem_so_lan_xuat_hien(dong_chu)

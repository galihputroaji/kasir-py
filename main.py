import json
import os
import platform
import time


class Belanja:

    def __init__(self, menus):
        self.menus = menus
        self.total_harga = 0
        self.daftar_pesanan = []
        self.dipesan = []

    def rupiah(self, angka):
        rp = "{:,.0f}".format(angka)
        rp = rp.replace(",", ".")
        rp = "Rp " + str(rp)
        return rp

    def cl(self):
        system = platform.system()
        if system == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def main(self):
        while True:
            self.cl()
            print(30 * "=")
            print("Daftar Produk:")
            print(30 * "=")
            for i, menu in enumerate(self.menus):
                print(f"{i+1}. {menu['nama']}\t\t{menu['harga']}")
            print(30 * "=")

            # User Pilih Menu
            if len(self.daftar_pesanan) > 0:
                self.dipesan = []
                jml_dipesans = {}
                # Tambah pesanan ke dalam list
                for menu in self.daftar_pesanan:
                    if menu['nama'] in jml_dipesans:
                        jml_dipesans[menu['nama']] = (jml_dipesans[menu['nama']][0] + 1,
                                                      jml_dipesans[menu['nama']][1])
                    else:
                        jml_dipesans[menu['nama']] = (1, menu['harga'])

                # Daftar Menu Yang Dipilih
                print("Daftar Belanja:")
                for menu, jml_dipesan in jml_dipesans.items():
                    harga = int(jml_dipesan[0]) * int(jml_dipesan[1])
                    print(f"- {menu} x{jml_dipesan[0]} = {self.rupiah(harga)}")
            for menu in self.daftar_pesanan:
                # Cek apa pilihan udan ada di list
                exists = False
                for p in self.dipesan:
                    if p['nama'] == menu['nama']:
                        # Jika sudah ada, update jumlahnya
                        p['jumlah'] += 1
                        exists = True
                        break
                # Jika belum ada, tambah ke list
                if not exists:
                    self.dipesan.append({
                        'nama': menu['nama'],
                        'harga': menu['harga'],
                        'jumlah': 1
                    })

            dipilih = int(
                input("Pilih Menu Atau Masukan 0 Untuk Selesai Memesan: "))
            # Jika user memasukan 0, selesai
            if dipilih == 0:
                break
            if dipilih > len(self.menus):
                print("Maaf, Menu Tidak Tersedia")
                time.sleep(1)
                continue

            # Menambahkan menu yang dipilih ke daftar pesanan
            self.daftar_pesanan.append(self.menus[dipilih - 1])

            # Menambahkan harga makanan ke total pesanan
            self.total_harga += int(self.menus[dipilih - 1]['harga'])

        self.cl()
        print(40 * "=")
        print("\tStruk Belanja")
        print(40 * "=")
        for menu in self.dipesan:
            hrg = int(menu['jumlah'] * menu['harga'])
            print(f"{menu['nama']}\t{menu['jumlah']}\t{self.rupiah(hrg)}")
        print("")
        print(f"Total Belanja: {self.rupiah(self.total_harga)}")
        print(40 * "=")


# Ambil data dari json
with open('makanan.json') as f:
    menus = json.load(f)

# Membuat objek belanja
belanja = Belanja(menus)

# Gassss...
belanja.main()

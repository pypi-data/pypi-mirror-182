import requests
from bs4 import BeautifulSoup

"""
Class GempaTerkini. Class merupakan cetak biru dari sebuah objek GempaTerkini.
GempaTerkini nantinya adalah sebuah objek.
Objek GempaTerkini memiliki 3 identitas berupa description, result, url.
Objek GempaTerkini memiliki “kemampuan” untuk ekstraksi_data(), tampilkan_data() dan run().
Dieksekusi di dalam konstruktor __init__ dan __main__
Dibuat objek gempa_di_indonesia dan gempa_di_dunia dari Class GempaTerkini.
dan dijalankan sehingga tampil data gempa terkini.

Constructor = metode yang dipanggil pertama kali saat object diciptakan.
Gunakan untuk mendeklarasikan semua variabel/field pada Class ini.
"""


class Bencana:
    def __init__(self, url, description):
        self.description = description
        self.result = None
        self.url = url

    def tampilkan_keterangan(self):
        print(self.description)

    def ekstraksi_data(self):
        print('ekstraksi_data not yet implemented')

    def tampilkan_data(self):
        print('tampilkan_data not yet implemented')

    def run(self):
        self.ekstraksi_data()
        self.tampilkan_data()


class BanjirTerkini(Bencana):
    def __init__(self, url):
        super(BanjirTerkini, self).__init__(url, 'NOT YET IMPLEMENTED, but it should return last flood in Indonesia')

    def tampilkan_keterangan(self):
        print(f'UNDER CONSTRUCTION {self.description}')


class GempaTerkini(Bencana):
    def __init__(self, url):
        super(GempaTerkini, self).__init__(url, 'To get the latest EarthQuake in Indonesia from BMKG.go.id')

    def ekstraksi_data(self):
        """
        Tanggal: 24 November 2022
        Waktu: 11:51:32 WIB
        Magnitudo: 3.8
        Kedalaman: 10 km
        Lokasi: LS=3.80 BT=128.50
        Pusat gempa: Pusat gempa berada di laut 30 km barat daya Maluku Tengah
        Dirasakan: Dirasakan (Skala MMI): I-II Ambon
        :return:
        """
        # mengambil data/konten halaman dari halaman situs bmkg.go.id
        # dan jika alamat salah/server mati maka munculkan pesan error
        try:
            content = requests.get(self.url)
        except (Exception,):
            return None

        # dan jika statusnya berhasil (kode 200)
        # maka tampilkan datanya menggunakan BeautifulSoup
        if content.status_code == 200:
            soup = BeautifulSoup(content.text, 'html.parser')

            # mengambil item waktu dari situs bmkg
            # dan menggunakan split itu memisahkan format
            result = soup.find('span', {'class': 'waktu'})
            result = result.text.split(', ')
            tanggal = result[0]
            waktu = result[1]

            # mengambil item lainnya dibawah class gempabumi-detail dan dibawah li (list item)
            result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
            result = result.findChildren('li')
            # hasil dari findChildren berupa array
            """
            i = 0
            for res in result:
                print(i, res)
                i = i + 1
            """
            # siapkan variabel untuk mengambil data lainnya
            i = 0
            magnitudo = None
            kedalaman = None
            ls = None
            bt = None
            lokasi = None
            dirasakan = None

            # looping data untuk membaca hasil dari scraping
            for res in result:
                if i == 1:
                    magnitudo = res.text
                elif i == 2:
                    kedalaman = res.text
                elif i == 3:
                    koordinat = res.text.split(' - ')
                    ls = koordinat[0]
                    bt = koordinat[1]
                elif i == 4:
                    lokasi = res.text
                elif i == 5:
                    dirasakan = res.text

                i = i + 1

            # masukan datanya dalam variabel hasil
            hasil = dict()
            hasil['tanggal'] = tanggal
            hasil['waktu'] = waktu
            hasil['magnitudo'] = magnitudo
            hasil['kedalaman'] = kedalaman
            hasil['koordinat'] = {'ls': ls, 'bt': bt}
            hasil['lokasi'] = lokasi
            hasil['dirasakan'] = dirasakan
            self.result = hasil
        else:
            return None

    def tampilkan_data(self):
        # jika situs bmkg down, maka cetak pesan error
        if self.result is None:
            print("Tidak bisa menemukan data gempa terkini!")
            return

        # cetak hasilnya di aplikasi
        print('Gempa Terakhir berdasarkan BMKG')
        print(f"Tanggal {self.result['tanggal']}")
        print(f"Waktu {self.result['waktu']}")
        print(f"Magnitudo {self.result['magnitudo']}")
        print(f"Kedalaman {self.result['kedalaman']}")
        print(f"Koordinat LS={self.result['koordinat']['ls']}, BT={self.result['koordinat']['bt']}")
        print(f"Lokasi {self.result['lokasi']}")
        print(f"Dirasakan {self.result['dirasakan']}")


if __name__ == '__main__':
    gempa_di_indonesia = GempaTerkini('https://www.bmkg.go.id/')
    gempa_di_indonesia.tampilkan_keterangan()
    gempa_di_indonesia.run()

    print('\n')
    banjir_di_indonesia = BanjirTerkini('NOT YET')
    banjir_di_indonesia.tampilkan_keterangan()
    banjir_di_indonesia.run()

    # Polymorphism
    daftar_bencana = [gempa_di_indonesia, banjir_di_indonesia]
    print('\nSemua bencana yang ada')
    for bencana in daftar_bencana:
        bencana.tampilkan_keterangan()

    # gempa_di_dunia = GempaTerkini('https://climate.com//')
    # print("Deskripsi class GempaTerkini", gempa_di_dunia.description)
    # gempa_di_dunia.run()

    # gempa_di_indonesia.ekstraksi_data()
    # gempa_di_indonesia.tampilkan_data()

# Latest Indonesia EarthQuake
This package will get the latest earthquake from BMKG | Meteorology, Climatology, and Geophysical Agency

## HOW IT WORK?
This package will scrape from [BMKG](https://bmkg.go.id) to get latest quake happened in Indonesia.

This package will use BeautifulSoup4 and Request, to produce output in the form of JSON that is ready to be used in web or mobile application.

## HOW TO USE
```
import gempaterkini

if __name__ == '__main__':
    gempa_di_indonesia = gempaterkini.GempaTerkini('https://www.bmkg.go.id/')
    print(f'Aplikasi utama menggunakan package yang memiliki deskripsi {gempa_di_indonesia.description}')
    gempa_di_indonesia.tampilkan_keterangan()
    gempa_di_indonesia.run()
```

# Author
Erwin Zulfikar
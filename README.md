# Çölyak Karar Destek Sistemi

## Proje Hakkında

Bu proje, bireylerin çölyak hastalığı açısından risk durumlarını değerlendirmek amacıyla geliştirilmiş web tabanlı bir karar destek sistemidir.

Kullanıcı tarafından girilen klinik bilgiler ve semptomlar değerlendirilerek çölyak hastalığı için bir risk oranı hesaplanmaktadır. Hesaplanan risk oranına göre sistem kullanıcıya öneriler sunmaktadır.

Ayrıca yapılan analizler SQLite veritabanında saklanmakta ve yönetici paneli üzerinden görüntülenebilmektedir.

---

## Proje Amacı

Çölyak hastalığına ait belirtileri ve laboratuvar verilerini kullanarak:

* Risk analizi yapmak
* Kullanıcıya öneriler sunmak
* Analiz geçmişini saklamak
* Yönetici paneli üzerinden kayıtları görüntülemek

amaçlanmıştır.

---

## Kullanılan Teknolojiler

* Python
* Flask
* SQLite
* HTML5
* CSS3
* Git
* GitHub
* Pandas
* OpenPyXL

---

## Kullanılan Veriler

Sistemde aşağıdaki bilgiler kullanılmaktadır:

* Yaş
* Cinsiyet
* Karın Ağrısı
* Diyare (İshal)
* Kilo Kaybı
* IgA Seviyesi
* tTG-IgA
* EMA-IgA
* HLA-DQ2/DQ8
* Anemi Durumu

---

## Risk Hesaplama Mantığı

Sistem belirtilere ve laboratuvar sonuçlarına göre puanlama yapmaktadır.

Örnek olarak:

* Karın ağrısı varsa risk artar.
* Diyare varsa risk artar.
* Kilo kaybı varsa risk artar.
* tTG-IgA yüksekse risk artar.
* EMA-IgA pozitifse risk artar.
* HLA-DQ2/DQ8 pozitifse risk artar.
* Anemi varsa risk artar.

Toplam puan üzerinden yüzde risk değeri oluşturulmaktadır.

---

## Sistem Özellikleri

### Kullanıcı Paneli

* Risk analizi yapma
* Sonuç görüntüleme
* Otomatik öneri alma

### Yönetici Paneli

* Tüm analizleri görüntüleme
* Toplam kayıt sayısını görüntüleme
* Veritabanı kayıtlarını inceleme

---

## Veritabanı

Proje içerisinde SQLite veritabanı kullanılmaktadır.

Tablo adı:

analizler_v2

Veriler sistem tarafından otomatik olarak kaydedilmektedir.

---

## Kurulum

Projeyi çalıştırmak için:

```bash
pip install flask
pip install pandas
pip install openpyxl
```

Daha sonra:

```bash
python app.py
```

Tarayıcıdan:

```text
http://127.0.0.1:5000
```

adresine gidilir.

---

## GitHub

Proje GitHub üzerinden yönetilmektedir.

---

## Geliştirici


Emine  NUR Akhan




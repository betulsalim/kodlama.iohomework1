#şart blokları

#sistem üyeliği var mı yok mu????
print("sistem üyeliği var mı yok mu???")
print("\n")

kullaniciadi1 = "Betül"
kullaniciSoyadi1 = "Salim"

sifre1 = "123456"
email1 = "betulsalim6@gmail.com"

kullaniciGenel1 = [kullaniciadi1, kullaniciSoyadi1, sifre1, email1]

kullaniciadi2 = "Nesrin"
kullaniciSoyadi2 = "Salim"

sifre2 = "654321"
email2 = "nesrin09@gmail.com"

kullaniciGenel2 = [kullaniciadi2, kullaniciSoyadi2, sifre2, email2]

ad = "Burak"
soyad = "Salim"
email = "betulsalim6@gmail.com"
sifre = "123456"

kullaniciGenel3 = [ad, soyad, sifre, email]

if kullaniciGenel1 == kullaniciGenel3 or kullaniciGenel3 == kullaniciGenel2:
  print("Sisteme giriş yapıldı")
else:
  print("Başarısız")

print("\n")
print("\n")

print("Sisteme giriş yapıldı mı???")
print("\n")
#sisteme giriş yapıldı mı yapılmadı mı???
kullanici1 = "Yasin"
kullanici2 = "Yunus"
kullanici3 = "Burak"

kullaniciGiris1 = True
kullaniciGiris2 = False
kullaniciGiris3 = True

if kullaniciGiris1:
  print(kullanici1 + " Aramıza hoş geldin")
  print("\n")
else:
  print("Sisteme Giriş yapamadınız")
  print("\n")

if kullaniciGiris2:
  print(kullanici2 + " Aramıza hoş geldin")
  print("\n")
else:
  print("Sisteme Giriş yapamadınız   " + kullanici2)
  print("\n")

if kullaniciGiris3:
  print(kullanici3 + " Aramıza hoş geldin")
  print("\n")
else:
  print("Sisteme Giriş yapamadınız")
  print("\n")

#DÖNGÜLER
#eğitim kısmında çıkan kategori ve eğitmen filtreleri

kategoriTuru1 = "Programlama"
kategoriTuru2 = "Tümü"

egitmen1 = "Engin DEMİROĞ"
egitmen2 = "Halit Enes KALAYCI"
egitmen3 = "Tümü"

kategoriler = [kategoriTuru1, kategoriTuru2]
egitmenler = [egitmen1, egitmen2, egitmen3]
print("Kategori Türleri: ")
for i in range(len(kategoriler)):
  print("\n")
  print(str(i + 1) + " " + kategoriler[i])
print("\n")
print("Eğitmenler: ")

for j in range(len(egitmenler)):
  print("\n")
  print(str(j + 1) + " " + egitmenler[j])

#METODLAR
#sayfa çağırıldığında...


def sayfaDegistir():
  print("Dersleri listele: ")
  print("\n")
  ders1 = "C# dersi"
  ders2 = "Java dersi"
  ders3 = "JavaScript dersi"
  ders4 = "C dersi"
  dersler = [ders1, ders2, ders3, ders4]
  for i in range(len(dersler)):
    print(str(i + 1) + " . " + dersler[i])
    print("\n")


def kartBilgisiGir():
  print("kart bilgilerini gir: ")
  print("\n")
  kartBilgisi1 = "Iban"
  kartBilgisi2 = "Hesap Numarası"
  kartBilgisi3 = "CVV numatrası"
  kartBilgisi4 = "Son kullanma tarihi"
  kartBilgileri = [kartBilgisi1, kartBilgisi2, kartBilgisi3, kartBilgisi4]
  for i in range(len(kartBilgileri)):
    print(str(i + 1) + " . " + kartBilgileri[i])


if kullaniciGiris1:
  kartBilgisiGir()
  print("\n")
  sayfaDegistir()

print("\n")

if kullaniciGiris2:
  print("lütfen üye olunuz")

print("\n")
if kullaniciGiris3:
  kartBilgisiGir()
  print("\n")
  sayfaDegistir()

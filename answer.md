## Boolean İkili Mantığı

### Boolean İkili Mantığı
Boolean ikili mantığı, yalnızca iki olası değere sahip olan bir veri türüdür: True (Doğru) ve False (Yanlış). Bu mantık, bilgisayar bilimi ve programlamada önemli bir rol oynar ve genellikle mantıksal işlemler, koşullu ifadeler ve döngülerde kullanılır.

### Boolean Kullanım Alanları
- **Koşullu İfadeler:** `if`, `elif` ve `else` ifadelerinde kullanılır.
- **Döngüler:** `while` döngüsünde döngünün devam edip etmeyeceğini belirlemek için kullanılır.
- **Mantıksal Operatörler:** `and`, `or`, `not` gibi operatörlerle kombinasyon halinde kullanılır.

```python
is_raining = True

if is_raining:
    print("Şemsiyeni al!")
else:
    print("Bugün hava güzel.")
```

## Matematiksel Fonksiyonlar: `round`, `floor`, `ceil`

Matematiksel fonksiyonlar, sayısal verilerle çalışırken sıkça kullanılır. Python, bu tür işlemleri gerçekleştirmek için çeşitli yerleşik fonksiyonlar sağlar. Bu kılavuzda, `round`, `floor`, ve `ceil` fonksiyonlarını detaylı olarak ele alacağız.

### `round` Fonksiyonu

`round` fonksiyonu, verilen bir sayıyı en yakın tam sayıya yuvarlar. Eğer ondalık basamak belirtilirse, sayı belirtilen basamak sayısına göre yuvarlanır.

#### Kullanımı

```python
round(number, ndigits)
```

- `number`: Yuvarlanacak sayı.
- `ndigits`: (Opsiyonel) Yuvarlamanın kaç ondalık basamağa kadar yapılacağını belirtir. Eğer belirtilmezse, tam sayıya yuvarlama yapılır.

#### Örnekler

```python
print(round(3.14))  # Çıktı: 3
print(round(3.14159, 2))  # Çıktı: 3.14
print(round(2.675, 2))  # Çıktı: 2.67 (Bazı Python sürümlerinde 2.68 olabilir, bu sayının ikili sistemdeki temsilinden kaynaklanır)
print(round(5.5))  # Çıktı: 6 (Eğer sayı tam ortadaysa, en yakın çift sayıya yuvarlar)
```

### `floor` Fonksiyonu

`floor` fonksiyonu, verilen bir sayıyı aşağıya doğru en yakın tam sayıya yuvarlar. Bu fonksiyon `math` modülü altında bulunur.

#### Kullanımı

```python
import math

math.floor(x)
```

- `x`: Aşağıya doğru yuvarlanacak sayı.

#### Örnekler

```python
print(math.floor(3.99))  # Çıktı: 3
print(math.floor(-3.99))  # Çıktı: -4
print(math.floor(3.0))  # Çıktı: 3 (Zaten tam sayı olduğu için değişmez)
```

### `ceil` Fonksiyonu

`ceil` fonksiyonu, verilen bir sayıyı yukarıya doğru en yakın tam sayıya yuvarlar. Bu fonksiyon da `math` modülü altında bulunur.

#### Kullanımı

```python
import math

math.ceil(x)
```

- `x`: Yukarıya doğru yuvarlanacak sayı.

#### Örnekler

```python
print(math.ceil(3.01))  # Çıktı: 4
print(math.ceil(-3.01))  # Çıktı: -3
print(math.ceil(3.0))  # Çıktı: 3 (Zaten tam sayı olduğu için değişmez)
```

### `floor` ve `ceil` Fonksiyonlarının Karşılaştırması

`floor` ve `ceil` fonksiyonları, bir sayının tam sayı kısmına yuvarlanması için kullanılır. Aralarındaki fark, `floor` fonksiyonunun sayıyı aşağıya doğru, `ceil` fonksiyonunun ise yukarıya doğru yuvarlamasıdır. Bu fark, özellikle negatif sayılarla çalışırken önemlidir.

#### Örnek Karşılaştırma

```python
print(math.floor(-3.7))  # Çıktı: -4
print(math.ceil(-3.7))  # Çıktı: -3
```

### Uygulama Alanları

Bu fonksiyonlar, finansal hesaplamalar, grafiksel işlemler, yuvarlama hatalarının minimize edilmesi gereken mühendislik uygulamaları gibi birçok alanda kullanılır. Örneğin:

- `round` fonksiyonu, kullanıcıya gösterilecek değerlerin belirli bir hassasiyette olmasını sağlamak için kullanılabilir.
- `floor` fonksiyonu, indirim hesaplamalarında veya stok yönetiminde kullanılabilir.
- `ceil` fonksiyonu, gerektiğinde daha fazla miktarda rezervasyon yapmayı veya kapasite planlamasını sağlamak için kullanılabilir.

Bu fonksiyonları kullanarak, sayısal veriler üzerinde hassas ve kontrollü yuvarlama işlemleri gerçekleştirebilirsiniz.

## Hata Yönetimi: `try` ve `except`

### `try` ve `except` Kullanımı
Python'da hataların ele alınması için `try` ve `except` blokları kullanılır. `try` bloğunda hataya neden olabilecek kodlar yer alır ve eğer bu kodlar bir hata oluşturursa, kontrol `except` bloğuna geçer.

Python'da hataların yönetimi ve ele alınması oldukça önemli bir konudur. Hataların doğru şekilde ele alınmaması, programın beklenmedik şekilde sonlanmasına ve kullanıcı deneyiminin olumsuz etkilenmesine neden olabilir. Python, hataları yönetmek ve programın kararlılığını artırmak için `try` ve `except` bloklarını sağlar. Bu bloklar, potansiyel hata durumlarını yakalayarak uygun şekilde işlem yapmayı mümkün kılar.

### `try` ve `except` Kullanımı

`try` ve `except` blokları, hata yönetiminin temelini oluşturur. `try` bloğu içinde, hataya neden olabilecek kodlar yer alır. Eğer bu kodlar bir hata üretirse, kontrol `except` bloğuna geçer ve ilgili hata türüne göre işlem yapılır. Bu sayede, programın beklenmedik şekilde sonlanması engellenir ve kullanıcıya uygun bir geri bildirim sağlanır.

#### Örnek: Sıfıra Bölme Hatası

Aşağıdaki örnekte, `ZeroDivisionError` hatası ele alınmaktadır. Bu hata, bir sayının sıfıra bölünmesi durumunda meydana gelir.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Sıfıra bölme hatası oluştu.")
```

Bu kod çalıştırıldığında, `10 / 0` ifadesi `ZeroDivisionError` hatası oluşturur ve kontrol `except` bloğuna geçer. Bu blok içinde, kullanıcıya hatanın nedeni hakkında bilgi verilir.

### `except` Blokları ile Belirli Hataların Yakalanması

Her hata türü için ayrı `except` blokları tanımlanabilir. Bu sayede, belirli hata türlerine özel işlem yapılabilir. Örneğin, `ValueError` hatası, geçersiz bir değerin işlendiği durumlarda meydana gelir. Bu hata, genellikle bir string'in integer'a dönüştürülmeye çalışılması gibi durumlarda oluşur.

#### Örnek: Geçersiz Değer Hatası

Aşağıdaki örnekte, `ValueError` hatası ele alınmaktadır. Bu hata, `int` fonksiyonunun geçersiz bir string değeri işlemeye çalışması durumunda oluşur.

```python
try:
    number = int("abc")
except ValueError:
    print("Geçersiz değer hatası oluştu.")
```

Bu kod çalıştırıldığında, `int("abc")` ifadesi `ValueError` hatası oluşturur ve kontrol `except` bloğuna geçer. Bu blok içinde, kullanıcıya hatanın nedeni hakkında bilgi verilir.

### Birden Fazla `except` Bloğu

Bir `try` bloğu, birden fazla `except` bloğu ile birlikte kullanılabilir. Bu sayede, farklı hata türleri ayrı ayrı ele alınabilir ve her hata türüne özel işlem yapılabilir.

#### Örnek: Birden Fazla Hata Türünü Ele Alma

Aşağıdaki örnekte, hem `ZeroDivisionError` hem de `ValueError` hataları ele alınmaktadır.

```python
try:
    result = 10 / 0
    number = int("abc")
except ZeroDivisionError:
    print("Sıfıra bölme hatası oluştu.")
except ValueError:
    print("Geçersiz değer hatası oluştu.")
```

Bu kod çalıştırıldığında, `10 / 0` ifadesi `ZeroDivisionError` hatası oluşturur ve kontrol ilgili `except` bloğuna geçer. İkinci `except` bloğu, `ValueError` hatası için ayrılmıştır, ancak bu örnekte ilk hata `ZeroDivisionError` olduğu için bu blok çalışmaz.

### `else` ve `finally` Blokları

Hata yönetimi yaparken `try` ve `except` bloklarına ek olarak `else` ve `finally` blokları da kullanılabilir. `else` bloğu, `try` bloğunda hata oluşmadığında çalıştırılır. `finally` bloğu ise hata oluşup oluşmadığına bakılmaksızın her zaman çalıştırılır.

#### Örnek: `else` ve `finally` Kullanımı

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Sıfıra bölme hatası oluştu.")
else:
    print("İşlem başarılı: Sonuç =", result)
finally:
    print("İşlem tamamlandı.")
```

Bu kod çalıştırıldığında, `10 / 2` ifadesi hatasız çalışır ve sonuç `else` bloğunda yazdırılır. `finally` bloğu ise her durumda çalışarak, işlem tamamlandığını belirtir.

### Sonuç

Hata yönetimi, Python programlarının kararlılığını ve kullanıcı deneyimini artırmak için kritik bir öneme sahiptir. `try` ve `except` blokları, hataların ele alınmasını ve uygun şekilde işlem yapılmasını sağlar. Ayrıca, `else` ve `finally` blokları ile hata yönetimi daha esnek ve kapsamlı hale getirilebilir. Bu yapılar sayesinde, programlar beklenmedik durumlarla başa çıkabilir ve kullanıcıya daha güvenli bir deneyim sunabilir.

## `__name__ '__main__' Kullanımı`
Python programlama dilinde `__name__` ve `__main__` özel değişkenleri, bir Python dosyasının doğrudan çalıştırılıp çalıştırılmadığını veya bir modül olarak ithal edilip edilmediğini belirlemek için kullanılır. Bu, kodun farklı senaryolarda nasıl davranması gerektiğini kontrol etmek için önemli bir tekniktir. Aşağıda bu konunun gelişmiş ve detaylı bir açıklamasını bulabilirsiniz.

### `__name__` Değişkeni

Her Python dosyası çalıştırıldığında, Python yorumlayıcısı dosyanın bazı özel değişkenlerini tanımlar. Bunlardan biri de `__name__` değişkenidir. Bu değişken, dosyanın çalıştırılma bağlamına bağlı olarak farklı değerler alır:

- Bir Python dosyası doğrudan çalıştırıldığında, `__name__` değişkeni `"__main__"` değerini alır.
- Aynı dosya bir başka Python dosyasından modül olarak ithal edildiğinde, `__name__` değişkeni o dosyanın adıyla (uzantısız) tanımlanır.

### `if __name__ == "__main__"` Yapısı

Bu yapı, bir Python dosyasının doğrudan çalıştırıldığında belirli bir kod bloğunun çalıştırılmasını sağlamak için kullanılır. Böylece, bir dosya hem bağımsız bir program olarak çalıştırılabilir hem de başka bir dosyada modül olarak kullanılabilir.

Aşağıda bu yapının nasıl kullanıldığını gösteren bir örnek bulunmaktadır:

```python
# my_module.py

def main():
    print("Ana fonksiyon çalışıyor.")

if __name__ == "__main__":
    main()
```

Bu örnekte, `main()` fonksiyonu sadece `my_module.py` dosyası doğrudan çalıştırıldığında çalışacaktır. Eğer bu dosya başka bir dosyadan modül olarak ithal edilirse, `main()` fonksiyonu çalıştırılmayacaktır.

### Örnek Senaryolar

#### Doğrudan Çalıştırma

`my_module.py` dosyasını doğrudan çalıştırdığınızda:

```bash
python my_module.py
```

Çıktı şu şekilde olacaktır:

```
Ana fonksiyon çalışıyor.
```

Bu durumda, Python yorumlayıcısı `my_module.py` dosyasını doğrudan çalıştırdığı için `__name__` değişkeni `"__main__"` değerini alır ve `if` bloğunun içindeki `main()` fonksiyonu çalıştırılır.

#### Modül Olarak İthal Etme

Eğer `my_module.py` dosyasını başka bir dosyadan ithal ederseniz:

```python
# another_module.py

import my_module
```

Bu durumda `main()` fonksiyonu çalıştırılmaz çünkü `my_module.py` dosyası doğrudan çalıştırılmamıştır, sadece modül olarak ithal edilmiştir. Bu senaryoda `__name__` değişkeni `"my_module"` değerini alır ve `if` bloğunun içindeki kod çalıştırılmaz.

### Neden Kullanılır?

1. **Kodun Yeniden Kullanılabilirliği:** `if __name__ == "__main__"` yapısı sayesinde bir dosya hem bağımsız bir program olarak çalıştırılabilir hem de modül olarak yeniden kullanılabilir. Bu, kodun daha modüler ve yeniden kullanılabilir olmasını sağlar.
2. **Test ve Geliştirme Kolaylığı:** Geliştirme sırasında bir dosyanın belirli kısımlarını test etmek için kullanışlıdır. Bir dosyanın doğrudan çalıştırıldığında belirli test fonksiyonlarının veya kod parçalarının çalıştırılmasını sağlayabilirsiniz.
3. **Kod Düzenleme ve Organizasyon:** Bu yapı, kodun daha okunabilir ve düzenli olmasını sağlar. Ana programın mantığını ve modül fonksiyonlarını ayırarak kodun organizasyonunu iyileştirir.

### Sonuç

`__name__` ve `__main__` yapısı, Python'da sıkça kullanılan ve önemli bir konudur. Bu yapı sayesinde Python dosyalarının farklı bağlamlarda nasıl çalıştırılacağını kontrol edebilir, kodunuzu daha modüler, yeniden kullanılabilir ve test edilebilir hale getirebilirsiniz. Bu teknik, özellikle büyük projelerde ve çoklu dosya yapılarında oldukça faydalıdır.


## Adımlarla Dilimleme

### Dilimleme (Slicing)
Python'da dilimleme, bir dizinin belirli bir bölümünü elde etmek için kullanılan bir yöntemdir. Bu yöntem, bir liste, dize veya başka bir dizilebilir veri yapısının bir alt kümesini seçmeye yarar. Dilimleme işlemi `[başlangıç:bitiş:adım]` şeklinde yazılır. `başlangıç` ve `bitiş` indeksleri belirli aralıktaki elemanları seçmek için kullanılır ve `adım`, bu aralıktaki elemanları hangi aralıklarla seçeceğimizi belirler.

#### Genel Dilimleme Yapısı
```python
dizi[başlangıç:bitiş:adım]
```
- `başlangıç`: Dilimlemeye başlanan indeks. Bu indeks dahilidir.
- `bitiş`: Dilimlemenin bittiği indeks. Bu indeks dahil değildir.
- `adım`: Dilimleme sırasında elemanların hangi aralıklarla seçileceğini belirler. Varsayılan değeri 1'dir.

Örnek:
```python
string = "Python"
print(string[1:5])  # Çıktı: ytho
print(string[::2])  # Çıktı: Pto
```
Yukarıdaki örneklerde:
- `string[1:5]` ifadesi, `string` dizisinin 1. indeksinden başlayarak (dahil) 5. indeksine kadar (hariç) olan elemanlarını seçer.
- `string[::2]` ifadesi, `string` dizisinin ilk elemanından başlayarak her iki elemanda bir seçer.

## String Öğeleri Dilimleme

### String Dilimleme
Stringlerde dilimleme, belirli karakterleri veya karakter dizilerini elde etmek için kullanılır. Stringlerde indeksleme 0'dan başlar. Bu nedenle, dilimleme işlemi yaparken indeks numaralarına dikkat edilmelidir.

#### Başlangıç ve Bitiş İndeksleri ile Dilimleme
Başlangıç ve bitiş indeksleri kullanarak bir stringin belirli bir bölümünü seçebiliriz.

Örnek:
```python
string = "Merhaba Dünya"
print(string[:7])  # Çıktı: Merhaba
print(string[8:])  # Çıktı: Dünya
```
Yukarıdaki örneklerde:
- `string[:7]` ifadesi, `string` dizisinin başından (0. indeks) 7. indekse kadar olan (hariç) elemanları seçer.
- `string[8:]` ifadesi, `string` dizisinin 8. indeksinden başlayarak dizinin sonuna kadar olan elemanları seçer.

##  Adım Değeri ile Dilimleme
Adım değeri belirterek dilimleme yaparken, belirli aralıklarla elemanları seçebiliriz.

Örnek:
```python
string = "Dilimleme"
print(string[::2])  # Çıktı: Dlilee
print(string[1::2])  # Çıktı: iimme
```
Yukarıdaki örneklerde:
- `string[::2]` ifadesi, `string` dizisinin ilk elemanından başlayarak her iki elemanda bir seçer.
- `string[1::2]` ifadesi, `string` dizisinin 1. indeksinden başlayarak her iki elemanda bir seçer.

### Negatif İndeksler ile Dilimleme
Negatif indeksler kullanarak dilimleme yaparken diziyi tersten seçebiliriz.

Örnek:
```python
string = "Dilimleme"
print(string[::-1])  # Çıktı: ememliliD
print(string[-1:-5:-1])  # Çıktı: emel
```
Yukarıdaki örneklerde:
- `string[::-1]` ifadesi, `string` dizisini ters çevirir.
- `string[-1:-5:-1]` ifadesi, `string` dizisinin son elemanından (ters yön) başlayarak -5. indekse kadar olan (hariç) elemanları seçer.

### Dilimleme ile Alt String Elde Etme
Bir stringin belirli bir alt kümesini elde etmek için dilimleme işlemi oldukça kullanışlıdır. Bu sayede, string içinden belirli bölümleri kolayca seçebiliriz.

Örnek:
```python
string = "Python Programlama Dili"
alt_string = string[7:18]
print(alt_string)  # Çıktı: Programlama
```
Yukarıdaki örnekte:
- `string[7:18]` ifadesi, `string` dizisinin 7. indeksinden başlayarak 18. indekse kadar olan (hariç) elemanları seçer ve bu alt stringi `alt_string` değişkenine atar.

Dilimleme işlemleri Python'da oldukça güçlü ve esnektir. Bu sayede diziler ve stringler üzerinde hızlı ve etkili manipülasyonlar gerçekleştirebiliriz.

## Ondalık Kesir, Dolar İşareti ve Biçim Belirteçleri

### Ondalık Kesir Ekleme
Python'da `format()` fonksiyonu veya f-stringler kullanarak sayıları belirli bir ondalık hassasiyetiyle yazdırabilirsiniz.

```python
value = 123.456
print(f"{value:.2f}")  # Çıktı: 123.46
```

### Dolar İşareti Ekleme
Değerleri dolar işaretiyle formatlamak için de `format()` veya f-string kullanılabilir.

```python
price = 49.99
print(f"${price:.2f}")  # Çıktı: $49.99
```

## `while` Döngüsü Kullanımı

### `while` Döngüsü
`while` döngüsü, belirli bir koşul True olduğu sürece kod bloğunu tekrarlar. 

```python
counter = 0
while counter < 5:
    print(counter)
    counter += 1
```

Bu Python öğreticisi, Boolean ikili mantığından hata yönetimine, matematiksel fonksiyonlardan string dilimlemeye kadar geniş bir yelpazeyi kapsamaktadır. Kod parçacıkları, her konunun nasıl uygulanabileceğini gösterir ve Python programlama dilinin temel ve ileri düzey kavramlarını anlamak için gerekli bilgileri sağlar.


### `while True` Kullanımı

#### `while True` Döngüsü
`while True`, koşul her zaman `True` olduğu için sonsuz bir döngü oluşturur. Bu tür döngüler genellikle belirli bir koşul sağlandığında `break` ifadesi ile sonlandırılır. `while True` döngüsü, özellikle kullanıcıdan sürekli veri almak, belirli bir olayın gerçekleşmesini beklemek veya belirli bir işlem sonsuza kadar devam ettirilmek istendiğinde kullanılır.

Aşağıda, kullanıcıdan sürekli veri alıp, kullanıcı 'q' tuşuna bastığında döngüden çıkılmasını sağlayan bir örnek bulunmaktadır:

```python
while True:
    user_input = input("Çıkmak için 'q' ya basın: ")
    if user_input == 'q':
        break
    print(f"Girilen değer: {user_input}")
```

Bu örnekte, `while True` döngüsü ile kullanıcıdan sürekli veri alınıyor. Kullanıcı 'q' tuşuna bastığında `if user_input == 'q':` koşulu sağlanır ve `break` ifadesi ile döngü sonlandırılır. Aksi halde, girilen değer ekrana yazdırılır ve döngü devam eder.

#### `while True` Döngüsünün Kullanım Alanları

1. **Kullanıcıdan Sürekli Veri Almak:**
   - Bir form veya giriş işlemi gibi kullanıcıdan sürekli veri alınması gereken durumlarda kullanılabilir.
   
   ```python
   while True:
       command = input("Komut girin ('exit' ile çık): ")
       if command == 'exit':
           break
       else:
           print(f"Komut: {command}")
   ```

2. **Belirli Bir Olayı Beklemek:**
   - Bir olayın gerçekleşmesini beklerken kullanılabilir. Örneğin, bir sunucuya bağlanma girişimleri veya bir sensör verisi bekleme durumu.
   
   ```python
   import time

   while True:
       event_happened = check_event()  # Olayın gerçekleşip gerçekleşmediğini kontrol eden bir fonksiyon
       if event_happened:
           break
       time.sleep(1)  # Olayı beklerken 1 saniye ara ver
   print("Olay gerçekleşti!")
   ```

3. **Sonsuz Döngüler:**
   - Bir programın sonsuza kadar çalışması gereken durumlarda kullanılabilir. Örneğin, bir web sunucusu veya bir arka plan hizmeti.

   ```python
   while True:
       process_requests()  # Gelen istekleri işleyen bir fonksiyon
       if should_shutdown():  # Programın kapatılıp kapatılmaması gerektiğini kontrol eden bir fonksiyon
           break
   ```

#### `while True` Döngüsünde Dikkat Edilmesi Gerekenler

- **Sonsuz Döngüler:**
  - Yanlış kullanıldığında, `while True` döngüleri programın sonsuza kadar çalışmasına ve CPU kaynaklarını tüketmesine neden olabilir. Bu nedenle, döngüden çıkış koşullarının doğru ve mantıklı bir şekilde belirlenmesi önemlidir.

- **Kullanıcı Deneyimi:**
  - Kullanıcıdan sürekli veri alınan durumlarda, kullanıcıya döngüden nasıl çıkılacağı açık bir şekilde belirtilmelidir.

- **Kaynak Yönetimi:**
  - Sistem kaynaklarının verimli bir şekilde kullanılması için döngü içerisinde gereksiz işlemlerden kaçınılmalı ve gerekirse bekleme süreleri (`time.sleep()`) eklenmelidir.

Yukarıdaki örnekler ve açıklamalar, `while True` döngüsünün nasıl kullanılacağını ve nerelerde faydalı olabileceğini detaylı bir şekilde göstermektedir. Bu sayede, belirli bir koşul gerçekleşene kadar döngünün devam etmesi gereken durumlarda etkili bir şekilde kullanılabilir.

## `for` Döngüsü Kullanımı

### `for` Döngüsü
`for` döngüsü, iterable (tekrarlanabilir) bir nesne üzerinde yineleme yapar. Python'da liste, tuple, string gibi veri yapıları üzerinde kullanılarak her bir elemanın sırayla işlenmesini sağlar. Bu döngü, özellikle tekrar eden işlemler için oldukça kullanışlıdır.

#### Temel Kullanım
Aşağıdaki örnekte, bir liste üzerindeki her bir eleman `for` döngüsü kullanılarak yazdırılır:

```python
# Bir liste üzerinde for döngüsü kullanımı
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
```

Bu kod parçasında `numbers` listesi üzerinde yineleme yapılarak, her bir `number` elemanı sırayla ekrana yazdırılır.

## `for` Döngüsünün Kullanım Alanları
`for` döngüsü, çeşitli veri yapıları ve senaryolar üzerinde kullanılabilir. İşte bazı yaygın kullanım alanları:

#### Liste, Tuple, Set veya String Üzerinde Yineleme
Liste, tuple, set veya string gibi veri yapıları üzerinde yineleme yapmak için `for` döngüsü kullanılır:

```python
# Bir string üzerinde for döngüsü kullanımı
text = "Python"
for char in text:
    print(char)
```

Bu örnekte, `text` stringi üzerindeki her bir karakter `char` değişkenine atanarak ekrana yazdırılır.

#### Belirli Bir Aralıkta Sayılar Üzerinde Yineleme
`range()` fonksiyonu ile belirli bir aralıkta sayı üretip, bu sayılar üzerinde `for` döngüsü ile yineleme yapılabilir:

```python
# Belirli bir aralıkta sayılar üzerinde yineleme
for i in range(5):
    print(i)
```

Bu kod, 0'dan başlayarak 4'e kadar (5 hariç) olan sayıları ekrana yazdırır.

#### Dosya Satırları Üzerinde Yineleme
Bir dosyanın her bir satırını okumak ve işlemek için `for` döngüsü kullanılabilir:

```python
# Bir dosyanın satırları üzerinde for döngüsü kullanımı
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

Bu kod, `example.txt` dosyasını açar ve her bir satırını `line` değişkenine atayarak ekrana yazdırır. `strip()` metodu, satır sonundaki gereksiz boşlukları ve yeni satır karakterlerini temizler.

### `enumerate()` Fonksiyonu ile İterasyon
`enumerate()` fonksiyonu, bir iterable üzerinde yineleme yaparken, aynı zamanda her bir elemanın indeksini de sağlar:

```python
# enumerate() fonksiyonu kullanımı
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

Bu kod, her bir meyvenin indeksini ve adını ekrana yazdırır.

### `zip()` Fonksiyonu ile İterasyon
`zip()` fonksiyonu, birden fazla iterable üzerinde paralel yineleme yapmayı sağlar:

```python
# zip() fonksiyonu kullanımı
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

Bu örnekte, `names` ve `ages` listeleri üzerinde paralel olarak yineleme yapılır ve her bir isme karşılık gelen yaş ekrana yazdırılır.

### Sonuç
`for` döngüsü, Python programlamada yineleme işlemleri için vazgeçilmez bir araçtır. Listelerden dosya satırlarına kadar geniş bir yelpazede kullanım alanı bulunur. `enumerate()` ve `zip()` gibi yardımcı fonksiyonlarla birlikte kullanıldığında, daha karmaşık ve güçlü yineleme işlemleri gerçekleştirilebilir.

## Değişkenlere Değer Atama

### `running = True` veya `None`

Bir değişkenin `True` veya `None` olarak atanması, programın akışını kontrol etmek veya belirli bir durum belirtmek için kullanılan yaygın bir yaklaşımdır. Bu, özellikle koşullu ifadeler ve döngülerde önemli bir rol oynar. İşte bu iki durumun ayrıntılı bir incelemesi:

### `True`

Bir değişkenin `True` olarak atanması, genellikle bir işlemin veya döngünün devam etmesi gerektiğini belirtir. Bu tür bir atama, programın belirli bir durumda çalışmaya devam etmesini sağlamak için kullanılır.

Örnek:
```python
running = True
while running:
    print("Program çalışıyor.")
    # Koşullu ifadeyle 'running' değişkenini False yaparak döngüyü sonlandırabilirsiniz.
    if bazı_koşul:
        running = False
```
Bu örnekte, `running` değişkeni `True` olarak ayarlandığında, `while` döngüsü çalışmaya devam eder. `running` değişkeni `False` olduğunda ise döngü sonlanır.

### `None`

Bir değişkenin `None` olarak atanması, o değişkenin henüz bir değere sahip olmadığını veya geçici olarak boş olduğunu belirtir. `None`, Python'da "değer yok" anlamına gelir ve genellikle başlangıçta bir değişkenin atanmış bir değeri olmadığını ifade etmek için kullanılır.

Örnek:
```python
result = None
if result is None:
    print("Sonuç henüz belirlenmedi.")
    # Daha sonra 'result' değişkenine bir değer atanabilir.
    result = hesaplama_fonksiyonu()
```
Bu örnekte, `result` değişkeni başlangıçta `None` olarak ayarlanır. Daha sonra, belirli bir işlem veya hesaplama sonucunda bu değişkene bir değer atanabilir.

### Uygulama Örneği

Bir programda `True` ve `None` kullanımını birleştiren daha kapsamlı bir örnek:

```python
# Değişkenlerin başlangıç değerleri
running = True
result = None

# Program döngüsü
while running:
    # Kullanıcıdan girdi alma
    user_input = input("Bir sayı girin veya 'exit' yazın: ")

    if user_input.lower() == 'exit':
        # Döngüyü sonlandırmak için 'running' değişkenini False yap
        running = False
    else:
        try:
            # Kullanıcı girdisini sayıya çevir ve hesaplama yap
            number = int(user_input)
            result = number ** 2
            print(f"Girdiğiniz sayının karesi: {result}")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

# Program sona erdiğinde bir mesaj göster
print("Program sonlandı.")
```

Bu örnekte, `running` değişkeni `True` olarak ayarlandığında döngü çalışmaya devam eder. Kullanıcı "exit" komutunu girdiğinde, `running` değişkeni `False` yapılarak döngü sonlandırılır. `result` değişkeni ise kullanıcının girdiği sayının karesi olarak hesaplanır ve başlangıçta `None` olarak atanmıştır.

Bu şekilde, `True` ve `None` değerlerinin atanması, program akışını ve değişkenlerin durumunu etkin bir şekilde kontrol etmek için kullanılabilir.

## Fonksiyonlar

Python'da fonksiyonlar, belirli bir işlemi gerçekleştiren kod bloklarıdır. Fonksiyonlar, kodu daha organize, okunabilir ve tekrar kullanılabilir hale getirir. Bu bölümde, fonksiyonların nasıl yazıldığını ve anahtar sözcüklerin kullanımını detaylı olarak ele alacağız.

### Fonksiyon Yazımı ve Anahtar Sözcükler

Python'da bir fonksiyon, `def` anahtar sözcüğü ile tanımlanır. `def` anahtar sözcüğünden sonra fonksiyonun adı ve ardından parantezler içinde parametreler gelir. Fonksiyon gövdesi, girintili bir blok içinde yer alır.

Örnek bir fonksiyon tanımı şu şekildedir:

```python
def greet(name):
    return f"Merhaba, {name}!"
```

Bu fonksiyon, `name` adlı bir parametre alır ve bir selamlama mesajı döner. `return` anahtar sözcüğü, fonksiyonun sonucunu belirlemek için kullanılır.

#### `return` Anahtar Sözcüğü

Bir fonksiyon, `return` anahtar sözcüğünü kullanarak bir değer dönebilir. `return` anahtar sözcüğü kullanıldığında, fonksiyonun çalışması durur ve belirtilen değer döner.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Çıktı: 8
```

Yukarıdaki örnekte, `add` fonksiyonu iki parametre alır ve bu parametrelerin toplamını döner.

### `return` Anahtar Sözcüğü Olmadan Fonksiyon

Bir fonksiyon, `return` anahtar sözcüğü olmadan da tanımlanabilir ve çalıştırılabilir. Bu durumda, fonksiyon `None` döner. Bu tür fonksiyonlar genellikle sadece bir işlem gerçekleştirmek için kullanılır ve bir değer döndürmeleri gerekmez.

```python
def greet(name):
    print(f"Merhaba, {name}!")

result = greet("Ahmet")
print(result)  # Çıktı: None
```

Yukarıdaki örnekte, `greet` fonksiyonu bir selamlama mesajı yazdırır ancak `return` ifadesi içermez, dolayısıyla `None` döner.

### Parametreler ve Argümanlar

Fonksiyonlar, belirli işlemleri gerçekleştirmek için parametreler alabilir. Parametreler, fonksiyon tanımında belirtilir ve fonksiyon çağrıldığında argümanlar olarak değerler alır.

```python
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)  # Çıktı: 20
```

Yukarıdaki `multiply` fonksiyonu, iki parametre alır ve bu parametrelerin çarpımını döner. Fonksiyon çağrıldığında, `4` ve `5` argümanları, `a` ve `b` parametrelerine atanır.

### Varsayılan Parametre Değerleri

Fonksiyonlara, varsayılan değerler atanabilir. Bu, fonksiyonun bazı parametrelerinin opsiyonel olduğu durumlarda kullanışlıdır.

```python
def greet(name, greeting="Merhaba"):
    return f"{greeting}, {name}!"

print(greet("Ahmet"))  # Çıktı: Merhaba, Ahmet!
print(greet("Ayşe", "Selam"))  # Çıktı: Selam, Ayşe!
```

Yukarıdaki `greet` fonksiyonu, iki parametre alır: `name` ve `greeting`. `greeting` parametresine varsayılan olarak "Merhaba" değeri atanmıştır. Fonksiyon çağrıldığında, `greeting` parametresi verilmezse, varsayılan değer kullanılır.

### Anahtar Sözcük Argümanlar

Fonksiyon çağrılırken, parametre isimleri belirtilerek anahtar sözcük argümanlar kullanılabilir. Bu, argümanların sırasının önemli olmadığı durumlarda kullanışlıdır.

```python
def divide(a, b):
    return a / b

print(divide(a=10, b=2))  # Çıktı: 5.0
print(divide(b=2, a=10))  # Çıktı: 5.0
```

## Gelişmiş ve Detaylı Anlatım: `*args` Kullanımı

Python'da fonksiyonların dinamik sayıda argüman alabilmesi için kullanılan bazı özel sözdizimleri vardır. Bu özel sözdizimlerinden biri olan `*args`, fonksiyonların herhangi bir sayıda pozisyonel argüman almasına olanak tanır. Bu özellik, fonksiyonların esnekliğini artırır ve daha genel amaçlı fonksiyonlar yazmayı mümkün kılar.

#### `*args` Nedir ve Nasıl Çalışır?

`*args`, bir fonksiyona gönderilen pozisyonel argümanların tek bir tuple içinde toplanmasını sağlar. Fonksiyon tanımında `*args` ifadesi yer alıyorsa, bu fonksiyon çağrıldığında tüm pozisyonel argümanlar `args` adında bir tuple'a dönüştürülür.

```python
def örnek_fonksiyon(*args):
    print(args)

örnek_fonksiyon(1, 2, 3)
# Çıktı: (1, 2, 3)
```

Yukarıdaki örnekte, `örnek_fonksiyon` fonksiyonuna gönderilen 1, 2 ve 3 argümanları `args` tuple'ında toplanır.

#### `*args` Kullanımının Yaygın Örnekleri

1. **Toplama Fonksiyonu**

Birden fazla sayının toplamını hesaplayan bir fonksiyon yazalım. Bu fonksiyon, kaç tane sayı verildiğine bakmaksızın hepsinin toplamını döndürebilir.

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))  # Çıktı: 6
print(sum_all(4, 5, 6, 7, 8))  # Çıktı: 30
```

2. **String Birleştirme**

Birden fazla string argümanı birleştiren bir fonksiyon yazalım.

```python
def birlestir(*args):
    return ' '.join(args)

print(birlestir('Merhaba', 'Dünya!'))  # Çıktı: Merhaba Dünya!
print(birlestir('Python', 'çok', 'eğlenceli!'))  # Çıktı: Python çok eğlenceli!
```

3. **Arbitrary Argümanların İşlenmesi**

Bir fonksiyon, kendisine verilen argümanları işleyebilir ve her bir argümanı ayrı ayrı kullanabilir.

```python
def argumanlari_yazdir(*args):
    for arg in args:
        print(arg)

argumanlari_yazdir(1, 'a', [1, 2, 3], {'key': 'value'})
# Çıktı:
# 1
# a
# [1, 2, 3]
# {'key': 'value'}
```

#### `*args` ile Diğer Parametrelerin Birlikte Kullanımı

Bir fonksiyon, `*args` ile birlikte normal pozisyonel ve anahtar kelime argümanları da alabilir. Ancak, `*args` her zaman diğer pozisyonel argümanlardan sonra tanımlanmalıdır.

```python
def karma_fonksiyon(normal_param, *args, **kwargs):
    print(f"Normal Parametre: {normal_param}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

karma_fonksiyon(1, 2, 3, 4, isim='Ahmet', yas=30)
# Çıktı:
# Normal Parametre: 1
# Args: (2, 3, 4)
# Kwargs: {'isim': 'Ahmet', 'yas': 30}
```

#### Özet

`*args`, Python'da fonksiyonların daha esnek ve dinamik hale gelmesini sağlar. Bir fonksiyonun belirli sayıda değil, herhangi bir sayıda pozisyonel argüman almasına izin verir. Bu özellik, özellikle değişken sayıda argümanla çalışmanın gerektiği durumlarda çok kullanışlıdır. `*args` ile fonksiyonlarınızı daha genel ve yeniden kullanılabilir hale getirebilirsiniz.

## **kwargs Kullanımı

Python'da fonksiyonların esnek bir şekilde çeşitli sayıda argüman alabilmesi için özel parametreler bulunmaktadır. Bu parametrelerden biri de `**kwargs`'tır. `**kwargs`, fonksiyonun herhangi bir sayıda anahtar sözcük argüman (keyword arguments) almasına olanak tanır. Bu sayede, fonksiyon çağrıldığında, isimlendirilmiş argümanlar bir sözlük olarak fonksiyonun içine geçer.

#### `**kwargs` Parametresinin Temel Kullanımı

`**kwargs`, fonksiyon tanımında çift yıldız (`**`) ile birlikte kullanılır. Bu parametre, fonksiyonun içerisine bir sözlük olarak gelir ve bu sözlükte her bir anahtar, fonksiyon çağrılırken geçilen isimlendirilmiş argümanları temsil eder.

Örneğin, aşağıdaki `print_info` fonksiyonu, herhangi bir sayıda isimlendirilmiş argümanı kabul edebilir ve bu argümanları anahtar-değer çiftleri olarak yazdırır:

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Ahmet", age=30, city="İstanbul")
# Çıktı:
# name: Ahmet
# age: 30
# city: İstanbul
```

Yukarıdaki örnekte, `print_info` fonksiyonu çağrıldığında `name`, `age` ve `city` argümanları fonksiyona anahtar-değer çiftleri olarak geçer. `kwargs` parametresi bu anahtar-değer çiftlerini bir sözlük olarak saklar ve `kwargs.items()` yöntemi kullanılarak bu çiftler üzerinde dolaşılır.

#### `**kwargs` ile Varsayılan Parametreler Kullanımı

`**kwargs` parametresi ile birlikte, fonksiyonun belirli parametreleri için varsayılan değerler belirlemek mümkündür. Böylece, fonksiyon çağrılırken bu parametreler atlanabilir ve varsayılan değerler kullanılır.

```python
def greet(**kwargs):
    greeting = kwargs.get("greeting", "Merhaba")
    name = kwargs.get("name", "Dünya")
    print(f"{greeting}, {name}!")

greet()
# Çıktı: Merhaba, Dünya!

greet(greeting="Selam", name="Ahmet")
# Çıktı: Selam, Ahmet!
```

Bu örnekte, `greet` fonksiyonu `greeting` ve `name` isimli iki opsiyonel parametre alır. Eğer bu parametreler belirtilmezse, `kwargs.get` yöntemi kullanılarak varsayılan değerler atanır.

#### `**kwargs` ve Diğer Parametrelerin Birlikte Kullanımı

`**kwargs`, diğer pozisyonel ve isimlendirilmiş parametrelerle birlikte kullanılabilir. Bu durumda, `**kwargs` her zaman fonksiyon tanımında en sonda yer almalıdır.

```python
def user_info(username, age, **kwargs):
    print(f"Username: {username}")
    print(f"Age: {age}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

user_info("ahmet123", 30, city="İstanbul", occupation="Developer")
# Çıktı:
# Username: ahmet123
# Age: 30
# city: İstanbul
# occupation: Developer
```

Bu örnekte, `user_info` fonksiyonu `username` ve `age` isimli iki zorunlu parametre alır. Ek olarak, `city` ve `occupation` isimli opsiyonel parametreler de `**kwargs` ile geçilebilir.

#### `**kwargs` Kullanımının Avantajları

1. **Esneklik**: Fonksiyonlar herhangi bir sayıda isimlendirilmiş argüman alabilir, bu da fonksiyonların daha esnek ve yeniden kullanılabilir olmasını sağlar.
2. **Genişletilebilirlik**: Mevcut fonksiyonlara yeni argümanlar eklemek, mevcut fonksiyon tanımını değiştirmeden mümkündür.
3. **Okunabilirlik**: İsimlendirilmiş argümanlar, fonksiyon çağrılarında daha anlamlı ve okunabilir kod yazmayı teşvik eder.

#### Sonuç

`**kwargs`, Python fonksiyonlarının daha esnek ve dinamik bir şekilde çalışmasını sağlar. İsimlendirilmiş argümanları fonksiyonlara geçirirken, `**kwargs` kullanımı ile kodunuzu daha esnek, genişletilebilir ve okunabilir hale getirebilirsiniz. Bu özellik, özellikle birçok opsiyonel argümanı olan fonksiyonlarda büyük bir avantaj sağlar.

### Lambda Fonksiyonları

Lambda fonksiyonları, kısa ve basit fonksiyonlar tanımlamak için kullanılır. `lambda` anahtar sözcüğü ile tanımlanır ve genellikle bir satırlık ifadeler içerir.

```python
square = lambda x: x ** 2
print(square(5))  # Çıktı: 25

add = lambda a, b: a + b
print(add(3, 7))  # Çıktı: 10
```

Lambda fonksiyonları, özellikle yüksek derecede anonim fonksiyonlar gerektiren durumlarda kullanışlıdır.

### Sonuç

Fonksiyonlar, Python programlamada önemli bir rol oynar. Fonksiyonların nasıl tanımlandığını, `return` anahtar sözcüğünün nasıl kullanıldığını, parametre ve argümanlarla nasıl çalışıldığını ve lambda fonksiyonlarının nasıl yazıldığını öğrenmek, daha verimli ve okunabilir kod yazmanıza yardımcı olacaktır. Bu bilgileri kullanarak, karmaşık işlemleri basit ve modüler hale getirebilirsiniz.

## `*args` ve `**kwargs` Kullanımı

### `*args`
`*args`, fonksiyona değişken sayıda konumsal argüman geçirmeyi sağlar. Bu argümanlar bir tuple olarak paketlenir.

```python
def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1, 2, 3, 4)
```

### `**kwargs`
`**kwargs`, fonksiyona değişken sayıda anahtar kelime argümanı geçirmeyi sağlar. Bu argümanlar bir sözlük olarak paketlenir.

```python
def print_key_values(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_key_values(name="Ahmet", age=30, city="Ankara")
```

### `*args` ve `**kwargs` Birlikte Kullanımı
Bir fonksiyonda hem `*args` hem de `**kwargs` kullanılabilir.

```python
def example_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

example_function(1, 2, 3, name="Ahmet", age=30)
```

## Modül ve Fonksiyon İthal Etme

### Modüllerin İthal Edilmesi
Python'da bir modülden veya dosyadan diğerine fonksiyonları veya sınıfları ithal etmek için `import` ifadesi kullanılır. Modülün tamamı veya belirli parçaları ithal edilebilir.

```python
# math modülünün tamamının ithal edilmesi
import math

print(math.sqrt(16))

# math modülünden belirli fonksiyonun ithal edilmesi
from math import sqrt

print(sqrt(16))
```

### Sayfadan Sayfaya Aktarım
Bir Python dosyasındaki fonksiyon veya sınıfları başka bir dosyaya ithal edebilirsiniz.

```python
# module.py dosyasında bir fonksiyon
def greet(name):
    return f"Merhaba, {name}!"

# main.py dosyasından module.py dosyasındaki fonksiyonun ithal edilmesi
from module import greet

print(greet("Ahmet"))
```

Bu Python öğreticisi, `while` ve `for` döngülerinden fonksiyonlara, hata yönetiminden modüllerin ithal edilmesine kadar geniş bir yelpazeyi kapsamaktadır. Kod parçacıkları, her konunun nasıl uygulanabileceğini gösterir ve Python programlama dilinin temel ve ileri düzey kavramlarını anlamak için gerekli bilgileri sağlar.



Bu rehber, Python programlama dilinin çeşitli önemli kavramlarını ele alır. Bilimsel ve ciddi bir dil kullanılarak kapsamlı ve ayrıntılı açıklamalar sunulmuştur.

### `from` Anahtar Kelimesi

#### `from` Kullanımı
`from` anahtar kelimesi, bir modülden belirli ögeleri ithal etmek için kullanılır. Bu yöntem, sadece ihtiyacımız olan fonksiyonları veya sınıfları ithal ederek belleği daha verimli kullanmamızı sağlar.

```python
from math import sqrt, pi

print(sqrt(16))  # Çıktı: 4.0
print(pi)  # Çıktı: 3.141592653589793
```

## Fonksiyon İçinde Fonksiyon Tanımlama

Fonksiyon içinde fonksiyon tanımlama, yazılım geliştirmede kodun yapılandırılmasını ve kapsama alanlarının kontrol edilmesini sağlayan önemli bir tekniktir. Bu yaklaşım, özellikle belirli bir işlevi yerine getiren yardımcı fonksiyonların sadece belirli bir bağlamda kullanılmasını istediğinizde kullanışlıdır.

#### İç İçe Fonksiyonlar (Nested Functions)

İç içe fonksiyonlar, bir fonksiyonun tanımı içinde başka bir fonksiyon tanımlanması durumudur. Bu iç içe fonksiyonlar, genellikle dış fonksiyonun işlevselliğini desteklemek için kullanılır ve sadece dış fonksiyonun içinde çağrılabilirler. Bu durum, iç fonksiyonun kapsama alanını sınırlandırarak dış dünyadan gizlenmesini sağlar.

##### Örnek Kullanım

Aşağıdaki örnekte, `outer_function` adında bir dış fonksiyon ve içinde tanımlanan `inner_function` adında bir iç fonksiyon bulunmaktadır. `inner_function`, `outer_function` içinde tanımlandığı için sadece `outer_function` tarafından çağrılabilir.

```python
def outer_function(text):
    def inner_function():
        print(text)
    inner_function()

outer_function("Merhaba")
```

Bu örnekte:

1. `outer_function` fonksiyonu `text` adında bir parametre alır.
2. `inner_function` fonksiyonu, `text` parametresini kullanarak ekrana bir mesaj yazdırır.
3. `inner_function`, `outer_function` içinde tanımlandığı için sadece `outer_function` tarafından çağrılabilir.
4. `outer_function`, çağrıldığında `inner_function`'ı çağırır ve `text` parametresini ekrana yazdırır.

#### İç İçe Fonksiyonların Avantajları

1. **Kapsama Alanı Kontrolü**: İç fonksiyonlar, dış fonksiyonun kapsama alanı içinde tanımlandıkları için sadece bu bağlamda kullanılabilirler. Bu, fonksiyonların yanlışlıkla başka yerlerde kullanılmasını önler.
2. **Kodun Yapılandırılması**: İç fonksiyonlar, dış fonksiyonun işlevselliğini desteklemek için belirli görevleri modüler hale getirebilir. Bu, kodun daha okunabilir ve sürdürülebilir olmasını sağlar.
3. **Kapsamdan Yararlanma**: İç fonksiyonlar, dış fonksiyonun yerel değişkenlerine erişebilirler. Bu, fonksiyonlar arasında veri paylaşımını kolaylaştırır.

##### Daha İleri Bir Örnek

Aşağıdaki örnekte, bir dış fonksiyon ve birden fazla iç fonksiyon tanımlanarak daha karmaşık bir yapı oluşturulmuştur:

```python
def process_data(data):
    def clean_data():
        return [item.strip() for item in data if isinstance(item, str)]
    
    def transform_data(cleaned_data):
        return [item.upper() for item in cleaned_data]
    
    cleaned_data = clean_data()
    transformed_data = transform_data(cleaned_data)
    
    return transformed_data

data = ["  apple  ", "  banana  ", "  cherry  "]
result = process_data(data)
print(result)
```

Bu örnekte:

1. `process_data` fonksiyonu, `data` adlı bir liste alır.
2. `clean_data` iç fonksiyonu, `data` listesindeki metinleri temizler ve sadece metin olan öğeleri döner.
3. `transform_data` iç fonksiyonu, temizlenmiş metinleri büyük harfe dönüştürür.
4. `process_data` fonksiyonu, temizlenmiş veriyi ve dönüştürülmüş veriyi sırasıyla işler ve sonucu döner.

İç içe fonksiyonlar, karmaşık işlemleri daha basit ve yönetilebilir adımlara bölerek kodun anlaşılmasını ve bakımını kolaylaştırır. Bu yapı, özellikle büyük ve karmaşık projelerde kodun modülerliğini artırmak için sıklıkla kullanılır.



### Dosya ve Dizin İşlemleri

#### `os.path.exists`
Belirtilen bir yolun var olup olmadığını kontrol etmek için kullanılır.

```python
import os

if os.path.exists('example.txt'):
    print("Dosya mevcut.")
else:
    print("Dosya mevcut değil.")
```

#### `os.path.isfile`
Belirtilen bir yolun bir dosya olup olmadığını kontrol eder.

```python
import os

if os.path.isfile('example.txt'):
    print("Bu bir dosyadır.")
else:
    print("Bu bir dosya değildir.")
```

#### `os.path.isdir`
Belirtilen bir yolun bir dizin olup olmadığını kontrol eder.

```python
import os

if os.path.isdir('/home/user'):
    print("Bu bir dizindir.")
else:
    print("Bu bir dizin değildir.")
```

### Dosya Açma ve Okuma

#### `open('test.txt', 'r')`
Belirtilen dosyayı okuma modunda (`r`) açar.

```python
with open('test.txt', 'r') as file:
    content = file.read()
    print(content)
```

#### Dosya Modları

- **`'r'`**: Okuma modu. Varsayılan moddur. Dosyayı okumak için açar.
- **`'w'`**: Yazma modu. Dosyayı yazmak için açar. Dosya mevcut değilse yeni bir dosya oluşturur; mevcutsa içeriğini siler.

```python
# Okuma modu
with open('test.txt', 'r') as file:
    content = file.read()
    print(content)

# Yazma modu
with open('test.txt', 'w') as file:
    file.write("Yeni içerik.")
```

### `*args` ve `**kwargs` Kullanımı

#### `*args`
Değişken sayıda konumsal argümanları kabul eder. Bu argümanlar bir tuple olarak fonksiyona iletilir.

```python
def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1, 2, 3, 4)  # Çıktı: 1 2 3 4
```

#### `**kwargs`
Değişken sayıda anahtar kelime argümanlarını kabul eder. Bu argümanlar bir sözlük olarak fonksiyona iletilir.

```python
def print_key_values(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_key_values(name="Ahmet", age=30, city="Ankara")  # Çıktı: name: Ahmet age: 30 city: Ankara
```

#### `*args` ve `**kwargs` Birlikte Kullanımı

```python
def example_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

example_function(1, 2, 3, name="Ahmet", age=30)  
# Çıktı: Positional arguments: (1, 2, 3)
#       Keyword arguments: {'name': 'Ahmet', 'age': 30}
```

### Modül ve Fonksiyon İthal Etme

#### Modüllerin İthal Edilmesi

```python
# math modülünün tamamının ithal edilmesi
import math

print(math.sqrt(16))  # Çıktı: 4.0

# math modülünden belirli fonksiyonun ithal edilmesi
from math import sqrt

print(sqrt(16))  # Çıktı: 4.0
```

#### Sayfadan Sayfaya Aktarım

```python
# module.py dosyasında bir fonksiyon
def greet(name):
    return f"Merhaba, {name}!"

# main.py dosyasından module.py dosyasındaki fonksiyonun ithal edilmesi
from module import greet

print(greet("Ahmet"))  # Çıktı: Merhaba, Ahmet!
```

Bu Python öğreticisi, programlama dilinin temel ve ileri düzey kavramlarını ele alarak kapsamlı ve ayrıntılı açıklamalar sunar. Her konunun nasıl uygulanabileceğini gösteren kod parçacıkları ile Python dilinin kullanımı hakkında derinlemesine bilgi sağlar.



Bu rehber, Python programlama dilinin çeşitli önemli kavramlarını ele alır. Bilimsel ve ciddi bir dil kullanılarak kapsamlı ve ayrıntılı açıklamalar sunulmuştur.

### Dosya Açma Modları

#### `'a'`: Ekleme Modu
`'a'` modu, bir dosyayı ekleme (append) modunda açar. Dosya mevcut değilse, yeni bir dosya oluşturur. Dosya mevcutsa, mevcut içeriği silmeden yeni verileri dosyanın sonuna ekler.

```python
with open('example.txt', 'a') as file:
    file.write("Yeni satır\n")
```

#### `'b'`: İkili Mod
`'b'` modu, dosyaları ikili (binary) formatta açmak için kullanılır ve diğer modlarla birlikte kullanılır.

```python
with open('example.bin', 'wb') as file:
    file.write(b'Binary data')
```

#### `'t'`: Metin Modu
`'t'` modu, dosyaları metin (text) formatında açmak için kullanılır ve varsayılan moddur.

```python
with open('example.txt', 'rt') as file:
    content = file.read()
    print(content)
```

#### `'+'`: Güncelleme Modu
`'+'` modu, bir dosyayı hem okuma hem de yazma için açar.

```python
with open('example.txt', 'r+') as file:
    content = file.read()
    file.write("Yeni veri")
```

### `with open` Kullanımı

#### `with open` Nedir?
`with open` ifadesi, dosya işlemleri sırasında kaynak yönetimini otomatik olarak sağlar. Dosya açılır ve işlemler tamamlandığında otomatik olarak kapanır, böylece dosyanın kapatılmasını unutma gibi hataların önüne geçilir.

```python
with open('test.txt', 'w') as file:
    file.write("Merhaba Dünya")
```

### `shutil` Nedir?

`shutil` modülü, Python'da yüksek seviyeli dosya ve dizin işlemleri yapmak için kullanılan bir standart kütüphanedir. Bu modül, dosya ve dizin kopyalama, taşıma, kaldırma gibi işlemleri kolayca gerçekleştirmemizi sağlar. `shutil` modülü, bu tür işlemleri gerçekleştiren fonksiyonlar sunarak, bu işlemleri yaparken manuel olarak kod yazma gereksinimini ortadan kaldırır ve hata yapma olasılığını azaltır.

### `shutil` Modülünün Kullanım Alanları

`shutil` modülü, özellikle dosya sistemleri ile yoğun olarak çalışan programlarda, yedekleme işlemlerinde, dosya ve dizin yapılarını yönetme gereksinimi duyulan projelerde kullanılır. Başlıca kullanım alanları şunlardır:

- **Dosya ve Dizin Kopyalama**: Dosya veya dizinleri başka bir konuma kopyalamak.
- **Dosya ve Dizin Taşıma**: Dosya veya dizinleri bir konumdan başka bir konuma taşımak.
- **Dosya ve Dizin Silme**: Dosya veya dizinleri silmek.
- **Disk Kullanım Bilgisi Alma**: Disk alanı hakkında bilgi almak.

### `shutil` Modülündeki Temel Fonksiyonlar

#### 1. `shutil.copy(src, dst)`
Bu fonksiyon, `src` yolundaki dosyayı `dst` yoluna kopyalar. `dst` bir dizin ise, `src` dosyası bu dizine kopyalanır.

```python
import shutil

shutil.copy('kaynak_dosya.txt', 'hedef_dizin/')
```

#### 2. `shutil.copy2(src, dst)`
Bu fonksiyon, `copy` fonksiyonuna benzer ancak kopyalama sırasında dosya meta verilerini (oluşturma zamanı, değişiklik zamanı gibi) de kopyalar.

```python
import shutil

shutil.copy2('kaynak_dosya.txt', 'hedef_dizin/')
```

#### 3. `shutil.copytree(src, dst)`
Bu fonksiyon, `src` yolundaki dizini ve altındaki tüm dosya ve dizinleri `dst` yoluna kopyalar.

```python
import shutil

shutil.copytree('kaynak_dizin', 'hedef_dizin')
```

#### 4. `shutil.move(src, dst)`
Bu fonksiyon, `src` yolundaki dosya veya dizini `dst` yoluna taşır.

```python
import shutil

shutil.move('kaynak_dosya.txt', 'hedef_dizin/')
```

#### 5. `shutil.rmtree(path)`
Bu fonksiyon, `path` yolundaki dizini ve altındaki tüm dosya ve dizinleri siler.

```python
import shutil

shutil.rmtree('silinecek_dizin')
```

#### 6. `shutil.disk_usage(path)`
Bu fonksiyon, belirtilen `path` yolundaki disk kullanım bilgilerini döner. Dönen değer, toplam, kullanılan ve boş alanı bayt cinsinden içerir.

```python
import shutil

disk_kullanimi = shutil.disk_usage('/')
print(f'Toplam: {disk_kullanimi.total} bayt')
print(f'Kullanılan: {disk_kullanimi.used} bayt')
print(f'Boş: {disk_kullanimi.free} bayt')
```

### Örnek Uygulamalar

#### Dosya Kopyalama

```python
import shutil

# Bir dosyayı kopyalama 
shutil.copy('ornek.txt', 'yedek_ornek.txt')
```

#### Dizin Kopyalama

```python
import shutil

# Bir dizini ve altındaki tüm dosya ve dizinleri kopyalama
shutil.copytree('ornek_dizin', 'yedek_ornek_dizin')
```

#### Dosya Taşıma

```python
import shutil

# Bir dosyayı taşıma
shutil.move('ornek.txt', 'yeni_konum/ornek.txt')
```

#### Dizin Silme

```python
import shutil

# Bir dizini ve altındaki tüm dosya ve dizinleri silme
shutil.rmtree('silinecek_dizin')
``

### `raise` Anahtar Sözcüğü

#### `raise` Nedir?
`raise`, özel durum (exception) fırlatmak için kullanılır. Hata koşullarında programcı tarafından manuel olarak hata oluşturulmasını sağlar.

```python
def check_positive(number):
    if number < 0:
        raise ValueError("Sayı negatif olamaz")
    return True

try:
    check_positive(-10)
except ValueError as e:
    print(e)
```


### `os` Modülü Nedir?

`os` modülü, Python'un standart kütüphanelerinden biri olup, işletim sistemi ile etkileşim kurmamızı sağlayan çeşitli fonksiyonlar içerir. Bu modül, dosya ve dizin işlemleri, çevresel değişkenlerin yönetimi, süreç ve işlem bilgilerine erişim gibi geniş bir yelpazede işlevler sunar. Bu modül sayesinde Python programları, platform bağımsız bir şekilde, farklı işletim sistemlerinde aynı kodla çalışabilir.

#### `os` Modülünün Temel Kullanım Alanları

1. **Dosya ve Dizin İşlemleri**:
   - Dosya ve dizinlerin varlığını kontrol etme
   - Yeni dizinler oluşturma
   - Dosya ve dizinleri silme veya yeniden adlandırma

2. **Çevresel Değişkenler**:
   - Çevresel değişkenleri okuma
   - Çevresel değişkenleri ayarlama

3. **Sistem Bilgilerine Erişim**:
   - İşletim sistemi hakkında bilgi edinme
   - Mevcut çalışma dizinini öğrenme ve değiştirme

4. **Süreç Yönetimi**:
   - Yeni süreçler başlatma
   - Süreç kimlik bilgilerini alma

#### Örnek Kullanımlar

Aşağıda, `os` modülünün bazı temel işlevleri nasıl kullanıldığını gösteren örnekler bulunmaktadır:

##### 1. Dosya veya Dizin Varlığını Kontrol Etme

Belirtilen bir dosyanın veya dizinin mevcut olup olmadığını kontrol etmek için `os.path.exists()` fonksiyonu kullanılır.

```python
import os

if os.path.exists('example.txt'):
    print("Dosya mevcut.")
else:
    print("Dosya mevcut değil.")
```

##### 2. Yeni Bir Dizin Oluşturma

Yeni bir dizin oluşturmak için `os.makedirs()` fonksiyonu kullanılır. Bu fonksiyon, belirtilen yol boyunca gerekli tüm ara dizinleri de oluşturur.

```python
import os

# 'new_directory' adlı yeni bir dizin oluşturur
os.makedirs('new_directory')
```

##### 3. Çevresel Değişken Okuma

Bir çevresel değişkenin değerini okumak için `os.getenv()` fonksiyonu kullanılır. Bu örnekte, `PATH` çevresel değişkeninin değeri okunarak ekrana yazdırılmaktadır.

```python
import os

# 'PATH' çevresel değişkeninin değeri okunur
path = os.getenv('PATH')
print(path)
```

#### Diğer Önemli `os` Modülü Fonksiyonları

- **`os.remove(path)`**: Belirtilen dosyayı siler.
- **`os.rmdir(path)`**: Boş bir dizini siler.
- **`os.rename(src, dst)`**: Bir dosya veya dizini yeniden adlandırır.
- **`os.listdir(path)`**: Belirtilen dizindeki dosya ve dizinlerin bir listesini döner.
- **`os.getcwd()`**: Mevcut çalışma dizinini döner.
- **`os.chdir(path)`**: Mevcut çalışma dizinini değiştirir.
- **`os.system(command)`**: Belirtilen komutu işletim sistemi kabuğunda çalıştırır.

#### Özet

`os` modülü, Python ile işletim sistemi arasındaki etkileşimi sağlayan güçlü bir araçtır. Dosya ve dizin yönetiminden, çevresel değişkenlere erişime kadar geniş bir yelpazede işlevler sunar. Bu modül sayesinde Python programları, farklı işletim sistemlerinde uyumlu bir şekilde çalışabilir. `os` modülünün sunduğu zengin işlevselliği kullanarak, işletim sistemi ile ilgili pek çok işlemi kolayca gerçekleştirebilirsiniz.

### Hata Türleri

#### `FileNotFoundError`
Dosya bulunamadığında oluşur.

```python
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError as e:
    print(e)
```

#### `PermissionError`
İzin hatası oluştuğunda meydana gelir.

```python
try:
    with open('/protected_file.txt', 'w') as file:
        file.write("Veri")
except PermissionError as e:
    print(e)
```

#### `OSError`
Genel işletim sistemi hatasıdır. Dosya sistemleriyle ilgili çeşitli hatalar için kullanılır.

```python
try:
    os.remove('non_existent_file.txt')
except OSError as e:
    print(e)
```

### Fonksiyonların Kullanımı ve Önemi

#### Fonksiyonlar Nedir?
Fonksiyonlar, belirli bir görevi yerine getiren, yeniden kullanılabilir kod bloklarıdır. Modülerliği artırır, kod tekrarını önler ve kodun okunabilirliğini artırır.

```python
def greet(name):
    return f"Merhaba, {name}!"

print(greet("Ahmet"))
```

#### Fonksiyonların Önemi
- **Kodun Yeniden Kullanılabilirliği:** Fonksiyonlar, kodun farklı yerlerinde tekrar kullanılabilir.
- **Modülerlik:** Kodun daha küçük, yönetilebilir parçalara bölünmesini sağlar.
- **Okunabilirlik:** Fonksiyonlar, kodun anlamlı bloklara ayrılmasını sağlar ve okunabilirliği artırır.

### Kapsamlı Fonksiyon Kullanımı

#### Fonksiyon İçinde Fonksiyon Tanımlama
İç içe fonksiyonlar, fonksiyon içinde tanımlanan diğer fonksiyonlardır. Bu yapı, dış fonksiyonun işlevini desteklemek için kullanılır ve sadece dış fonksiyonun içinden çağrılabilir.

```python
def outer_function(text):
    def inner_function():
        print(text)
    inner_function()

outer_function("Merhaba")
```

#### `*args` ve `**kwargs` Kullanımı
- **`*args`**: Değişken sayıda konumsal argüman kabul eder ve bu argümanlar bir tuple olarak fonksiyona iletilir.
- **`**kwargs`**: Değişken sayıda anahtar kelime argümanı kabul eder ve bu argümanlar bir sözlük olarak fonksiyona iletilir.

```python
def example_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

example_function(1, 2, 3, name="Ahmet", age=30)
```

Bu Python öğreticisi, programlama dilinin temel ve ileri düzey kavramlarını ele alarak kapsamlı ve ayrıntılı açıklamalar sunar. Her konunun nasıl uygulanabileceğini gösteren kod parçacıkları ile Python dilinin kullanımı hakkında derinlemesine bilgi sağlar.
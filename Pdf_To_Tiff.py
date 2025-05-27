# Gerekli Kütüphaneleri kuralım.
# pip install pdf2image, Image

from pdf2image import convert_from_path
from PIL import Image
import paths as ph # Dizin bilgilerimi import ediyorum. 
import os
import pandas as pd
import openpyxl

Image.MAX_IMAGE_PIXELS = None # Max pixels sınırı defaultta var. Eğer bu sınırı geçen pdf leriniz varsa, Tiff formatına dönüşemeyecek. Bu sebep ile bu sınırı kaldırıyoruz.

# pdf_path değişkenine, pdflerinizin bulunduğu dizini verin.
# output_path değişkenine, tiff formatında kaydedilecek dizini verin.

# for döngüsündeki range değerlerini, pdf dosyalarınızın isimlendirilmesine göre ayarlayın. İsimlendirmeniz sayılarlaysa çok daha rahat olur.
# Pdflerinizin bulunduğu dizinin öğe sayısınıda verebilirsiniz. Tamamen sizin pdflerinizin isimlendirilmesine bağlı.

for i in range(20230000091494, 20230000098798):
    pdf_path = f"{ph.pdf_dir}/{i + 1}.pdf"
    output_path = f"{ph.output}/{i + 1}.tiff"
    try:
        images = convert_from_path(pdf_path, dpi=300, poppler_path="C:/poppler-24.08.0/Library/bin") # popper_path bilgisini kendi bilgisayarınıza göre ayarlayın.
        # PDF dosyasını TIFF formatında kaydet
        images[0].save(output_path, save_all=True, append_images=images[1:], compression="tiff_deflate") # TIFF dosyasını sıkıştırarak kaydet
        print(f"{output_path} dosyası başarıyla oluşturuldu.")
    except Exception as e:
        print(f"{pdf_path} dosyası işlenemedi: {e}")
        continue

# Bu kod, belirtilen dizindeki PDF dosyalarını TIFF formatına dönüştürür.
# Her PDF dosyası için, TIFF dosyası belirtilen dizine kaydedilir.
# Kodun sonunda, her bir PDF dosyasının başarıyla dönüştürüldüğünü veya hata mesajını yazdırır.
# Range aralığında belirtilen sayılar, PDF dosyalarının isimlendirilmesine göre ayarlanmalıdır.
# Range aralığında olmayan belgelerim olduğu için, hata verecek pdf isimlerinde, try-except bloğu ile hata alındığında devam edilmesini sağlıyorum.
# Not: Kodun çalışabilmesi için pdf2image ve Pillow kütüphanelerinin kurulu olması gerekmektedir.
# Not: Kodun çalışabilmesi için poppler kütüphanesinin bilgisayarınızda kurulu olması gerekmektedir.


# Klasördeki belgelerin isimlerini yazdırma
klasor_yolu = ph.dosya # veya "./" gibi göreli bir yol da olabilir

for dosya in os.listdir(klasor_yolu):
    if dosya.lower().endswith(('.tiff', '.pdf')):
        print(dosya)

tiffler = pd.DataFrame(os.listdir(klasor_yolu))
tiffler.to_excel("tiff_2023.xlsx")
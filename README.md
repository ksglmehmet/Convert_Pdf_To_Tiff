# Pdf_To_Tiff
Convert Pdf to Tiff

PDF veya PDF'lerinizi Tiff dokümanına çevirmek için 20 satırlık kod işinizi görecektir.

İlk olarak "poppler" uygulamasını bilgisayarınıza indirmeniz gerekmektedir. Sebebi, gerekli kütüphaneler arka planda poppler'e ihtiyaç duymaktadır.

indirmek için : https://github.com/oschwartz10612/poppler-windows/releases/tag/v24.08.0-0

Release 24.08.0-0 indirebilir, dışarıya aktarıp, C veya herhangi bir dizine yerleştirebilirsiniz.

Bu kod, belirtilen dizindeki PDF dosyalarını TIFF formatına dönüştürür.
Her PDF dosyası için, TIFF dosyası belirtilen dizine kaydedilir.
Kodun sonunda, her bir PDF dosyasının başarıyla dönüştürüldüğünü veya hata mesajını yazdırır.
Not: Kodun çalışabilmesi için pdf2image ve Pillow kütüphanelerinin kurulu olması gerekmektedir.
 Not: Kodun çalışabilmesi için poppler kütüphanesinin bilgisayarınızda kurulu olması gerekmektedir.
import cv2

# Görüntüyü oku
image = cv2.imread('C:/Users/Emre/Desktop/task1/ArcaneJinx.jpeg')  # Resim adı ve uzantısını değiştirin

# Görüntünün doğru bir şekilde yüklenip yüklenmediğini kontrol et
if image is None:
    print("Görüntü yüklenemedi.")
else:
    # Görüntüyü ekranda göster
    cv2.imshow('Görüntü', image)

    # Bekleme süresi (mili saniye cinsinden), 0: Sonsuz bekler, belirli bir süre için beklemek istiyorsanız, örneğin 1000 (1 saniye)
    cv2.waitKey(0)

    # Pencereyi kapat
    cv2.destroyAllWindows()
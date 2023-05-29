
## Nasıl Kullanılır

1. `neural_network.py` adlı Python dosyasını çalıştırın.
2. Kod, önceden tanımlanmış giriş ve çıkış verilerini kullanarak sinir ağını eğitecektir.
3. Eğitim tamamlandıktan sonra, sinir ağı yeni bir giriş verisiyle tahmin yapabilecektir.
4. Yeni bir giriş verisi için tahmin yapmak için `new_inputs` değişkenini düzenleyin ve kodu yeniden çalıştırın.
5. Tahmin sonucu ekrana yazdırılacaktır.

## Sinir Ağı Modeli

Bu kod, basit bir sinir ağı modeli oluşturur. Sinir ağı modeli, iki giriş özelliğiyle (0 veya 1 değerleri) bir çıkış tahmini yapar. Sinir ağı, geri yayılım algoritmasını kullanarak eğitilir ve ağırlıklarını günceller.

Sinir ağının aktivasyon fonksiyonu, binary step fonksiyonudur. Binary step fonksiyonu, girdinin eşik değerine göre 0 veya 1 döndürür.

## Örnek

Aşağıdaki örnek, sinir ağı modelinin nasıl kullanıldığını göstermektedir:

```python
import numpy as np

# Giriş ve çıkış verilerini tanımlar
inputs = np.array([[0, 0], [1, 1], [1, 0], [0, 1]])
outputs = np.array([[0, 1, 0, 0]]).T

# Sinir ağı modelini eğitir
neural_network = NeuralNetwork()
neural_network.train(inputs, outputs, 10000)

# Yeni bir girişle tahmin yap
new_inputs = np.array([1, 0])
prediction = neural_network.predict(new_inputs)
print(prediction)
```

Bu örnek, sinir ağı modelinin eğitilmesini ve yeni bir giriş verisi için tahmin yapılmasını göstermektedir. Önceden tanımlanmış giriş ve çıkış verileri kullanılarak sinir ağı eğitilir ve new_inputs değişkeniyle belirtilen yeni bir giriş için tahmin yapılır. Tahmin sonucu ekrana yazdırılır.
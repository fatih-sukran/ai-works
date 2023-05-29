import numpy as np

class NeuralNetwork:
    def __init__(self):
        np.random.seed(1)
        self.weights = 2 * np.random.random((2, 1)) - 1

    def binary_step(self, x):
        """
        Binary step fonksiyonu, girdinin eşik değerine göre 0 veya 1 döndürür.

        Args:
            x (numpy.ndarray): Girdi verisi.

        Returns:
            numpy.ndarray: Girdinin eşik değerine göre 0 veya 1 içeren dizi.
        """
        return np.where(x >= 1, 1, 0)

    def train(self, inputs, outputs, iterations):
        """
        Sinir ağını eğitmek için geri yayılım algoritmasını kullanır.

        Args:
            inputs (numpy.ndarray): Giriş verileri.
            outputs (numpy.ndarray): Çıkış verileri.
            iterations (int): İterasyon sayısı.

        Returns:
            None
        """
        for i in range(iterations):
            output = self.predict(inputs)
            error = outputs - output
            adjustment = np.dot(inputs.T, error)
            self.weights += adjustment

    def predict(self, inputs):
        """
        Verilen girişe göre tahmin yapar.

        Args:
            inputs (numpy.ndarray): Giriş verisi.

        Returns:
            numpy.ndarray: Tahmin sonucu.
        """
        return self.binary_step(np.dot(inputs, self.weights))

# Giriş ve çıkış verilerini tanımlar
inputs = np.array([[0, 0], [1, 1], [1, 0], [0, 1]])
outputs = np.array([[0, 1, 0, 0]]).T

# Sinir ağı modelini eğitir
neural_network = NeuralNetwork()
neural_network.train(inputs, outputs, 10000)

# Yeni bir girişle tahmin yap
print(neural_network.predict(np.array([0, 0]))) # output: 0
print(neural_network.predict(np.array([0, 1]))) # output: 0
print(neural_network.predict(np.array([1, 0]))) # output: 0
print(neural_network.predict(np.array([1, 1]))) # output: 1
 
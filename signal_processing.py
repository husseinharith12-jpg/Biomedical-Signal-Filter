import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# Filtre Tasarımı (Butterworth Band-pass)
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

# Test Verisi Oluşturma (Gürültülü EKG Simülasyonu)
fs = 500.0
t = np.linspace(0, 1, int(fs), endpoint=False)
clean_signal = np.sin(2 * np.pi * 1.2 * t) 
noise = 0.5 * np.random.normal(size=t.shape)
noisy_signal = clean_signal + noise

# Filtreleme Uygulaması
filtered_signal = bandpass_filter(noisy_signal, 0.5, 50.0, fs, order=6)

# Sonuçları Kaydetme
plt.figure(figsize=(10, 6))
plt.plot(t, noisy_signal, label='Gürültülü Sinyal (Raw Data)')
plt.plot(t, filtered_signal, label='Filtrelenmiş Sinyal (Cleaned)', linewidth=2)
plt.title('Biyomedikal Sinyal İşleme: EKG Gürültü Azaltma')
plt.legend()
plt.savefig('result.png') # Sonucu görsel olarak kaydeder
print("İşlem tamamlandı. Filtrelenmiş sinyal oluşturuldu.")

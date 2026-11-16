import os

from kompresi import kompresi_jpeg, kompresi_kuantisasi
from segmentasi import segmentasi_kmeans, segmentasi_otsu

def main():
    path_input = "gambar.jpg"

    if not os.path.exists(path_input):
        print(f"File tidak ditemukan: {path_input}")
        print(f"Letakkan gambar bernama 'gambar.jpg' di folder ini, lalu jalankan ulang.")
        return

    os.makedirs("hasil", exist_ok=True)

    print("=== Kompresi ===")
    kompresi_jpeg(path_input, "hasil/kompresi_jpeg.jpg", kualitas=40)
    kompresi_kuantisasi(path_input, "hasil/kompresi_kuantisasi.png", jumlah_warna=16)

    print("\n=== Segmentasi ===")
    segmentasi_otsu(path_input, "hasil/segmentasi_otsu.png")
    segmentasi_kmeans(path_input, "hasil/segmentasi_kmeans.png", k=4)

    print("Selesai! cek folder 'hasil' unutk melihat hasilnya.")
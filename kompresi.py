import os
from os import path
import cv2
from PIL import Image

def kompresi_jpeg(path_input, path_output, kualitas=40):
    os.makedirs(os.path.dirname(path_output) or ".", exist_ok=True)
    img = Image.open(path_input).convert("RGB")
    img.save(path_output,"JPEG", quality=kualitas, optimaze=True)
    print(f"JPEG tersimpan di {path_output}")

def kompresi_kuantisasi(path_input, path_output, jumlah_warna=16):
    os.makedirs(os.path.dirname(path_output) or ".", exist_ok=True)
    img = cv2.imread(path_input)
    if img is None:
        print(f"File tidak ditemukan: {path_input}")
        return

    data=img.reshape((-1,3)).float32() if hasattr(img, "float32") else img.reshape((-1,3)).astype("float32")
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
    _, labels, centers = cv2.kmeans(data, jumlah_warna, None, criteria, 10, cv2.KMEANS_PP_CENTERS) 

    center = centers.astype("uint8")
    hasil = center[labels.flatten()].reshape(img.shape)
    cv2.imwrite(path_output, hasil)
    print(f"Kuantisasi tersimpan di: {path_output}")
import cv2

def upscaling_image(path_input, path_output, scale=2, method="linear"):
    img = cv2.imread(path_input)
    if img is None:
        print (f"Gagal membaca gambar: {path_input}")
        return

    methods = {
        "nearest": cv2.INTER_NEAREST,
        "linear": cv2.INTER_LINEAR,
        "cubic": cv2.INTER_CUBIC,
        "lanczos": cv2.INTER_LANCZOS4
    }
    interp = methods.get(method.lower(), cv2.INTER_LINEAR)

    height, width = img.shape[:2]
    new_size = (width * scale, height * scale)

    upscaled_img = cv2.resize(img, new_size, interpolation=interp)
    cv2.imwrite(path_output, upscaled_img)
    print(f"Gambar berhasil di-upscale dan disimpan di: {path_output}")
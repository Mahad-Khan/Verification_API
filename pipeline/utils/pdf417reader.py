import zxing
import os
from PIL import Image
import sys

# get barcode directory full path
test_barcode_dir = os.path.join(os.path.dirname(__file__), "barcodes")
# get actual barcodereader
test_reader = zxing.BarCodeReader()

# filenames = ["vert_rev", "vert_norm", "horz_right", "horz_left"]

filenames = ["free_bottom", "free_mid", "free_top"]

# we have jpg filenames, now iterate and create bmps in barcodes
test_barcodes = []
for name in filenames:
    temp = name + ".bmp"
    try:
        dl_img = Image.open(os.path.join(test_barcode_dir, name + ".jpg"))
    except IOError:
        print("unable to load image")
        sys.exit(1)

    dl_img.save("barcodes/" + temp, "bmp")
    test_barcodes.append([(temp, "PDF_417", "This should be PDF_417")])

    dl_img.close()

print(test_barcodes)


def try_barcode(obj):
    global test_reader
    for filename, expected_format, expected_raw in obj:
        path = os.path.join(test_barcode_dir, filename)
        print("trying ", filename)
        try:
            dec = test_reader.decode(
                path, possible_formats=expected_format, try_harder=True
            )
            if dec.parsed != "":
                print("it worked!")
                print(dec.parsed)
            else:
                print("no!")
        except zxing.BarCodeReaderException:
            print("no scan!")


for barcode in test_barcodes:
    try_barcode(barcode)

import qrcode
url = input("Enter the URL to generate QR Code: ")

filename = input("Enter the filename u want to save it as: ")
if not(filename.endswith(".png")):
    filename = filename + ".png"

img = qrcode.make(url)
img.save(filename)
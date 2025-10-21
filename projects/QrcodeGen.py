import qrcode
img = qrcode.make('http://www.google.com/')
img.save("text_file.png")
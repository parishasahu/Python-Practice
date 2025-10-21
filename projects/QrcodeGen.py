import qrcode
img = qrcode.make('upi://pay?pa=8950633977@pthdfc')
img.save("text_file.png")
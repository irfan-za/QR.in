import qrcode
from qrcode.image.styledpil import StyledPilImage

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,  
    border=2,  
)
url=input('Insert URL or text : ')
user_have_logo = input("Want to add a logo to your QR Code? (Y/N): ").strip().lower()
qr.add_data(url)
qr.make(fit=True)
if(user_have_logo== 'y'):
  logo = input("Insert your logo file name : ")
  qr_img = qr.make_image(image_factory=StyledPilImage, embeded_image_path=logo)
else:
  custom_color = input("Want to custom color on your QR Code? (Y/N): ").strip().lower()
  if(custom_color == 'y'):
    foreground = input("foreground color : ")
    background = input("background color : ")
    qr_img = qr.make_image(fill_color=foreground, back_color=background)
  else:
    qr_img = qr.make_image(fill_color="black", back_color="white")
qr_img.save('qrcode.png')

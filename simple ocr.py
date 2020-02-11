from PIL import Image
import pytesseract

im = Image.open("image name.jpg")

text = pytesseract.image_to_string(im, lang = 'eng')

print(text)
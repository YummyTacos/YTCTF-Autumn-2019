from PIL import Image

im = Image.open('pic.png')

print(len(set(im.getdata())))

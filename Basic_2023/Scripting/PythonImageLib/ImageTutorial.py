from PIL import Image, ImageFilter

img = Image.open('KarekarSir.jpg')
print(img.format)
#print(dir(img))

filter_img= img.filter(ImageFilter.BoxBlur(10))
filter_img.save("blur.png", "png")
#img.show()   # To open the image in image viewer

print(img.size)

img.thumbnail((400,400))        # compesses image to new aspect ration without any noticible difference
img.show()
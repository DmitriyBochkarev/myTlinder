from PIL import Image, ImageFilter

monastery = "default.jpg"
with Image.open(monastery) as img_monastery:
    img_monastery.load()
logo = "default2.jpg"
with Image.open(logo) as img_logo:
    img_logo.load()

img_logo = img_logo.convert("L")
threshold = 50
img_logo = img_logo.point(lambda x: 255 if x > threshold else 0)
img_logo = img_logo.resize(
    (img_logo.width // 5, img_logo.height // 5)
)
img_logo = img_logo.filter(ImageFilter.CONTOUR)
img_logo = img_logo.point(lambda x: 0 if x == 255 else 255)

img_monastery.paste(img_logo, (0, 0), img_logo)
img_monastery.save()


img.load()
        logo = "media/default2.jpg"
        with Image.open(logo) as img_logo:
            img_logo.load()

        img_logo = img_logo.convert("L")
        threshold = 50
        img_logo = img_logo.point(lambda x: 255 if x > threshold else 0)
        img_logo = img_logo.resize(
            (img_logo.width // 5, img_logo.height // 5)
        )
        img_logo = img_logo.filter(ImageFilter.CONTOUR)
        img_logo = img_logo.point(lambda x: 0 if x == 255 else 255)

        img.paste(img_logo, (0, 0), img_logo)
        img.save()
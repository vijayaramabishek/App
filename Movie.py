print("Emter the text:")
image=input()
img_file = Image.open(image)
img = img_file.load()

# (2) Get image width & height in pixels
[xs, ys] = img_file.size
max_intensity = 100
hues = {}

# (3) Examine each pixel in the image file
for x in xrange(0, xs):
  for y in xrange(0, ys):
    # (4)  Get the RGB color of the pixel
    [r, g, b] = img[x, y]

    # (5)  Normalize pixel color values
    r /= 255.0
    g /= 255.0
    b /= 255.0

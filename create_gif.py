import imageio.v3 as iio

image_paths = ['goku1.png', 'goku2.png']
images = []

for path in image_paths:
    images.append(iio.imread(path))

iio.imwrite('goku.gif', images, loop=0, duration=500)
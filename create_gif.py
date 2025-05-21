import imageio.v3 as iio
from pygifsicle import optimize

filenames = ["srcs/nyan-cat1.png", "srcs/nyan-cat2.png", "srcs/nyan-cat3.png"]
images = []

for filename in filenames:
    images.append(iio.imread(filename))
    
# Creating GIFi
# "nyan_cat.gif" - Name I want to call my gif
# images - The list containing the image data
# duration - How long in each milli seconds
# loop = 0 - Infinite loop
iio.imwrite("nyan_cat.gif", images, duration = 100, loop = 0)

# Optimized the GIF
# Option 1: Save as a new optimizef file
optimize("nyan_cat.gif", "nyan_cat_optimized.gif")

# Option 2: Overwrite the original with optimized version
#optimize("nyan_cat.gif")

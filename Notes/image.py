import numpy as np
import skimage.data as skdata
import matplotlib.pyplot as mplt

image = skdata.camera()
mplt.gray()
mplt.imshow(image)
mplt.show()
print(image)

L = [image[image == i] for i in range(256)]
print(L)


# for i in range(256):
#   A = image_array == i
# - initialize 
# - loop through 255
# - relations to make another array of bools
# - logical indexing to make array
# - do size
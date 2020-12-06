import matplotlib.pyplot as plt
import matplotlib.image as mpimg


"""
This program prints a pumpkin I drew with the scariest thing I could think of.....2020!
"""

img = mpimg.imread('Pumpkin.png') #tells where to look
print(img)

imgplot = plt.imshow(img)



plt.show() #plot the graph with the image


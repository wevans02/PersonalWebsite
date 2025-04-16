import matplotlib.pyplot
import numpy
import sys

def main(argv):
    photoName = argv[1]
    myImage = matplotlib.pyplot.imread(photoName)

    height=myImage.shape[0]
    width=myImage.shape[1]


    for x in range(0, height-1):
        for y in range(0,width-1):
            average = (myImage[x, y, 0] + myImage[x, y, 1] + myImage[x, y, 2])/3
            myImage[x, y, 0] = average
            myImage[x, y, 1] =  average
            myImage[x, y, 2] = average
            

    imgplot = matplotlib.pyplot.imshow(myImage)
    matplotlib.pyplot.show()

main(sys.argv)

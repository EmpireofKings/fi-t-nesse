import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib.image as mpimg

def show_images(images, cols , titles , title):
    
    assert((titles is None)or (len(images) == len(titles)))
    n_images = len(images)
    if titles is None: titles = ['Image (%d)' % i for i in range(1,n_images + 1)]
    fig = plt.figure()
    fig.suptitle(title)
    for n, (image, title) in enumerate(zip(images, titles)):
        a = fig.add_subplot(2,2, n + 1)
        f=plt.imshow(mpimg.imread(image), aspect= 'auto')
        plt.axis('off')
        f.axes.get_xaxis().set_visible(False)
        f.axes.get_yaxis().set_visible(False)
        a.set_title(title)
        
    fig.set_size_inches(np.array(fig.get_size_inches()) * n_images)
    plt.show()

def main(sideUpText, sideDownText, frontUpText, frontDownText, finalScore):
    script_dir = os.path.dirname('home/mayankj/technique/') 
    frontDown = "FinalFrontDOWN.png"
    frontUp = "FinalFrontUp.png"
    sideDown = "FinalSideDown.png"
    sideUp = "FinalSideUp.png"
    show_images([frontDown, frontUp, sideDown, sideUp],4 ,[frontDownText, frontUpText, sideDownText,sideUpText], finalScore)

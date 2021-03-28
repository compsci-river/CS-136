#
#River Sheppard
#
#

from PIL import Image

if __name__ == "__main__":
    scale = 768
   
    # creating the new image in RGB mode
    bitmap = Image.new("RGB", (scale, scale), "white")
  
    # Allocating the storage for the image and
    # loading the pixel data.
    pix = bitmap.load()
     
    # setting up the variables according to 
    # the equation to  create the fractal
    c = complex(-0.585, 0.85)
    move = 0.0
    maxIter = 255
   
    for x in range(scale):
        for y in range(scale):
            zx = 1.5*(x - scale/2)/(0.5*scale) + move
            zy = 1.0*(y - scale/2)/(0.5*scale) + move
            z = complex(zx,zy)
            i = maxIter
            while abs(z*z) < 4 and i > 1:
                z = z**2 + c
                i -= 1
  
            # convert byte to RGB (3 bytes), kinda 
            # magic to get nice colors
            pix[x,y] = (i << 21) + (i << 10) + i*8
  
    # to display the created fractal
    bitmap.show()
        
        

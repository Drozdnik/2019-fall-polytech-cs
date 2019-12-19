

def setup():
    global img
    background(100)
    smooth()
    size(1600,1200)
    img = loadImage("data/popugay.jpg")
    
    
def draw():
    global img
    background(100)
    image(img, mouseX, mouseY)

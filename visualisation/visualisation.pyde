
add_library("sound")
amount = 20
num=20
scale = 1.5
bands = 64
sum = [0.0] * bands
smooth_factor = 0.2
r_width = 0


def setup():
    global song , img0
    size(700,873)
    smooth()
    stroke(247,25,25,255)
    img0 = loadImage("visual.jpg")
    
    global r_width
    r_width = width / float(bands)
    song = SoundFile(this, "opening.mp3")
    song.play()
    
    global fft
    fft = FFT(this, bands)
    fft.input(song)
    
def draw():
    image(img0,0,0)
    global num, amount
    fill(0,40)
    fft.analyze()
    
    rect(-1,-1,width+1,height+1)
   
    
    translate(width/2,height/2)
    for i, v in enumerate(sum):
        sum[i] += (fft.spectrum[i] - v) * smooth_factor
        maxX = map(-sum[i] * height * scale, 0, width, 1, 250)
        for i in range(0,360, amount):
            x = sin(radians(i+num))*maxX
            y = cos(radians(i+num))*maxX
        
            x2 = sin(radians(i+amount - num))*maxX
            y2 = cos(radians(i+amount - num))*maxX
        
            noFill()
            bezier(x,y,x-x2,y-y2,x2-x,y2-y,x2,y2)
            bezier(x,y,x+x2,y+y2,x2+x,y2+y,x2,y2)
            fill(0,150,255)
            ellipse(x,y,5,5)
            ellipse(x2,y2,5,5)
        num +=0.5

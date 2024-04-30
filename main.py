def encode(text,name="image"):
    from PIL import Image

    img = Image.new("RGB", 
        (
            len(text)+1, # size X
            len(text)+1    # size Y
        )
    )

    bg = Image.open('bg.png')
    bg = bg.resize((len(text)+1,len(text)+1))
    pixels = bg.load() 
    width, height = bg.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            img.putpixel(
                (x,y),
                (r,g,b)
            )
    
    img.putpixel(
        (0,0),
        (len(text),0,0)
    )

    for v in range(len(text)+1):
        if v == 0: continue
        i = ord(text[v-1])+10
        if i>=255: i=0
        b = i%3 == 0 # and i%2 !=0
        g = i%2 == 0 # and i%3 !=0
        r = i%3 != 0 and i%2 != 0
        if b==True: 
            b=i
        else:
            b=0
        if g==True: 
            g=i
        else:
            g=0
        if r==True:
            r=i
        else:
            r=0

        img.putpixel(
            (
                v, # x
                0  # Y
            ),
            ((
                r, # R
                g, # G
                b  # B
            ))
        )
    for v in range(len(text)+1):
        if v == 0: continue
        i = ord(text[v-1])+len(text)
        if i>=255: i=0
        b = i%3 == 0 # and i%2 !=0
        g = i%2 == 0 # and i%3 !=0
        r = i%3 != 0 and i%2 != 0
        if b==True: 
            b=i
        else:
            b=0
        if g==True: 
            g=i
        else:
            g=0
        if r==True:
            r=i
        else:
            r=0

        img.putpixel(
            (
                0, # x
                v  # Y
            ),
            ((
                r, # R
                g, # G
                b  # B
            ))
        )
    for v in range(len(text)+1):
        if v == 0: continue
        i = ord(text[v-1])+len(text)
        if i>=255: i=0
        b = i%3 == 0 # and i%2 !=0
        g = i%2 == 0 # and i%3 !=0
        r = i%3 != 0 and i%2 != 0
        if b==True: 
            b=i
        else:
            b=0
        if g==True: 
            g=i
        else:
            g=0
        if r==True:
            r=i
        else:
            r=0

        img.putpixel(
            (
                v, # x
                len(text)  # Y
            ),
            ((
                r, # R
                g, # G
                b  # B
            ))
        )
    for v in range(len(text)+1):
        if v == 0: continue
        i = ord(text[v-1])+len(text)
        # if i>=255: i=0
        b = i%3 == 0 # and i%2 !=0
        g = i%2 == 0 # and i%3 !=0
        r = i%3 != 0 and i%2 != 0
        if b==True: 
            b=i
        else:
            b=0
        if g==True: 
            g=i
        else:
            g=0
        if r==True:
            r=i
        else:
            r=0

        img.putpixel(
            (
                len(text), # x
                v  # Y
            ),
            ((
                r, # R
                g, # G
                b  # B
            ))
        )

    img.save(name+".png")

    return name+".png"
def decode(path="image.png"):
    from PIL import Image

    img = Image.open(path)

    textlen = img.getpixel((0,0))[0]+1

    img = Image.open(path)

    toreturn = ""

    k = 0

    for k in range(textlen):
        x,y,z = img.getpixel((k,0))
        if k == 0: continue
        if y==z: z=0
        temp = x+y+z
        toreturn += chr(temp-10)
        k += 1
    return toreturn

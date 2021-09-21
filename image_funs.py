from PIL import Image


def rmBlack(img):  # Changes the black pixels to transparent
    img = img.convert('RGBA')
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)
    return img


def reColor(img, color):  # Changes the white pixels to the defined color
    img = img.convert('RGBA')
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255 and item[3] == 255:
            newData.append(color)
        else:
            newData.append(item)
    img.putdata(newData)
    return img


def closeCrop(img):  # Crops to the closest white pixels (Non-functioning)
    img = img.convert('RGBA')
    datas = img.getdata()
    dim = img.size
    cropBox = [dim[0], dim[1], 0, 0]
    pos = [0, 0]
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            if pos[0] < cropBox[0]:
                cropBox[0] = pos[0]
            if pos[0] > cropBox[2]:
                cropBox[2] = pos[0]
            if pos[1] < cropBox[1]:
                cropBox[1] = pos[1]
            if pos[1] > cropBox[3]:
                cropBox[3] = pos[1]
        if pos[0] == dim[0] - 1:
            pos[0] = 0
            pos[1] = pos[1] + 1
        else:
            pos[0] = pos[0] + 1
    img = img.crop(cropBox)
    return img


def squareCrop(img):  # Crops to the closes white pixels in the wider dimension, evenly crops the shorter dimensio to make the final result a square (Non functioning)
    img = img.convert('RGBA')
    datas = img.getdata()
    dim = img.size
    cropBox = [dim[0], dim[1], 0, 0]
    pos = [0, 0]
    for item in datas:  # Loops through all the pixels and tracks the left-most, top-most, right-most, bottom-most
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            if pos[0] < cropBox[0]:
                cropBox[0] = pos[0]
            if pos[0] > cropBox[2]:
                cropBox[2] = pos[0]
            if pos[1] < cropBox[1]:
                cropBox[1] = pos[1]
            if pos[1] > cropBox[3]:
                cropBox[3] = pos[1]
        if pos[0] == dim[0] - 1:
            pos[0] = 0
            pos[1] = pos[1] + 1
        else:
            pos[0] = pos[0] + 1

    cropDim = [cropBox[2] - cropBox[0], cropBox[3] - cropBox[1]]

    if cropDim[0] > cropDim[1]:  # Adjusts for squareness
        adjU = int((cropDim[0] - cropDim[1]) / 2) + ((cropDim[0] - cropDim[1]) % 2 > 0)  # Rounds up to make sure a half pixel will get shifted to one side
        adjD = int((cropDim[0] - cropDim[1]) / 2)  # Rounds down
        cropBox[1] = cropBox[1] - adjU
        cropBox[3] = cropBox[3] + adjD
    else:
        adjU = int((cropDim[1] - cropDim[0]) / 2) + ((cropDim[1] - cropDim[0]) % 2 > 0)
        adjD = int((cropDim[1] - cropDim[0]) / 2)
        cropBox[0] = cropBox[0] - adjU
        cropBox[2] = cropBox[2] + adjD

    #add padding
    padding = max(cropDim)*0.2
    cropBox[0] = cropBox[0] - padding
    cropBox[1] = cropBox[1] - padding
    cropBox[2] = cropBox[2] + padding
    cropBox[3] = cropBox[3] + padding
    
    img = img.crop(cropBox)
    return img

def compPaste(img, base, box):  # Takes in an image, a background, and pastes with transparency proprely
    temp = Image.new('RGBA', base.size, (255, 255, 255, 0))
    temp.paste(img, box)
    composite = Image.alpha_composite(base, temp)
    return composite

def advPaste(img, background, centerPos, scale, rotation, color):
    img = squareCrop(img)
    img = rmBlack(img)
    img = reColor(img, color)
    newSize = (int(background.size[1] * scale), int(background.size[1] * scale))

    img = img.resize(newSize, resample=Image.NEAREST)
    img = img.rotate(rotation)
    xsize, ysize = img.size

    pastePos = (int(round(centerPos[0] - (xsize / 2))), int(round(centerPos[1] - (ysize / 2))))

    comp = compPaste(img, background, pastePos)
    return comp

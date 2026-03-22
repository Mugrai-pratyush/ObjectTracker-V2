def histograminit(num):
    """
    initializes histogram with 0 initial values and an indexarr and also returns them
    """
    histValues=[]
    for i in range(0,num):
        histValues.append(0)
    return histValues
def PixelDictinit(num):
    """
    initializes Dict key 0 to num and values [] and also returns it
    """
    PixelDict={}
    for i in range(0,num):
        PixelDict[i]=[]
    return PixelDict
def histogramCreater(histogramArr,height,width,D2pixelarr):
    """
    Loops over D2pixelarr visiting each pixel once and recording the pixel value in an 0 initiated histogram array for that perticualr pixel
    pixels are b/w 0,255 ig we will check 
    inputs: height of the D2pixelarr
            width of the D2pixelarr
            D2pixelarr
            histogramArr
    returns: updated histogramArr
    """
    for i in range(0,height):
        for j in range(0,width):
            val=D2pixelarr[i][j]#between 0,255
            histogramArr[val]+=1
    return histogramArr
def dictCreator(PixelDict,height,width,D2pixelarr):
    """
    Loops over D2pixelarr visiting each pixel once and recording the pixel value in an 0 initiated dict val to key setup 
    where key is 0-255 and val is [x,y]
    input: height of the D2pixelarr
            width of the D2pixelarr
            D2pixelarr
            PixelDict
    returns: updated PixelDict
    """
    for i in range(0,height):
        for j in range(0,width):
            key=D2pixelarr[i][j]
            pixelPoseArr=[i,j]
            PixelDict[key].append(pixelPoseArr)
    return PixelDict
def squarefinder(dict, side):
    """
    Calulates points using pixeldict
    returns:Pointsarray
    """
    probable_pixel = None
    for key in dict:
        if len(dict[key]) >= side * side:
            probable_pixel = key
            break

    if probable_pixel is None:
        raise ValueError("Square not found")

    pointsarray =dict[probable_pixel]
    min_row = min(p[0] for p in pointsarray)
    max_row = max(p[0] for p in pointsarray)
    min_col = min(p[1] for p in pointsarray)
    max_col = max(p[1] for p in pointsarray)

    A = [min_row, min_col]
    B = [min_row, max_col]
    C = [max_row, min_col]
    D = [max_row, max_col]

    return [A, B, C, D]
from CreateBackgroundandSquare import *
from HistogramAndDict import *
def Sim(runs,height,width,side,SquarePixelVal):
    """
    Runs the simulator for given runs and creates the Patharr depending on Square Position
    return:PathArr
    """
    PathArr=[]
    inirun=0
    while inirun<runs:
        bg=CreateBackground(height,width)
        Bg_square=CreateSquare(height,width,side,bg,SquarePixelVal) #build the background and place Square
        Histogram=histograminit(256)
        Pixeldict=PixelDictinit(256)
        histogramCreater(Histogram,height,width,Bg_square)
        dictCreator(Pixeldict,height,width,Bg_square)
        ####Now we find the Square from the dict
        SquarePos = squarefinder(Pixeldict, side)
        PathArr.append(SquarePos)
        inirun+=1
    return PathArr

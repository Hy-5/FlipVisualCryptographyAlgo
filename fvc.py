#CS6359 Project

import sys, getopt, os, random
import tkinter as tk
from tkinter.filedialog import askopenfilename as loadimage
from PIL import Image


def oneSplit():

    #Creating a matrix to hold picture binary values


    imgName=loadimage()
    print(imgName)
    with Image.open(imgName) as pic:
        print("pic size =",pic.size)
        pic = pic.convert("RGBA")
        pixel=pic.load()
    matrixMapping=[[0]*(pic.size[1]) for _ in range(pic.size[0])]
    tcy1=[[0]*(pic.size[1]*2) for _ in range(pic.size[0]*2)]
    tcy2=[[0]*(pic.size[1]*2) for _ in range(pic.size[0]*2)]
    """print("tcy1 =", tcy1)
    print("tcy2 =", tcy2)"""
    """for i in range (matrixMapping):
        for j in range (matrixMapping):
            print(matrixMapping[i,j])"""
    for i in range (pic.size[0]):
        for j in range(pic.size[1]):
            a=bool(random.getrandbits(1))
            if pixel[i,j]<=(200,200,200,200):
                matrixMapping[j][i]=1
                if (a):
                    tcy1[(j*2)][(i*2)]=1
                    """tcy1[(j*2)][(i*2)+1]=0
                    tcy1[(j*2)+1][(i*2)]=0"""
                    tcy1[(j*2)+1][(i*2)+1]=1
                    
                    """tcy2[(j*2)][(i*2)]=0"""
                    tcy2[(j*2)][(i*2)+1]=1
                    tcy2[(j*2)+1][(i*2)]=1
                    """tcy2[(j*2)+1][(i*2)+1]=0"""
                else:
                    """tcy1[(j*2)][(i*2)]=0"""
                    tcy1[(j*2)][(i*2)+1]=1
                    tcy1[(j*2)+1][(i*2)]=1
                    """tcy1[(j*2)+1][(i*2)+1]=0"""
                    
                    tcy2[(j*2)][(i*2)]=1
                    """tcy2[(j*2)][(i*2)+1]=0
                    tcy2[(j*2)+1][(i*2)]=0"""
                    tcy2[(j*2)+1][(i*2)+1]=1
            else:
                if (a):
                    tcy1[(j*2)][(i*2)]=1
                    """tcy1[(j*2)][(i*2)+1]=0
                    tcy1[(j*2)+1][(i*2)]=0"""
                    tcy1[(j*2)+1][(i*2)+1]=1
                    
                    tcy2[(j*2)][(i*2)]=1
                    """tcy2[(j*2)][(i*2)+1]=0
                    tcy2[(j*2)+1][(i*2)]=0"""
                    tcy2[(j*2)+1][(i*2)+1]=1
                else:
                    """tcy1[(j*2)][(i*2)]=0"""
                    tcy1[(j*2)][(i*2)+1]=1
                    tcy1[(j*2)+1][(i*2)]=1
                    """tcy1[(j*2)+1][(i*2)+1]=0"""
                    
                    """tcy2[(j*2)][(i*2)]=0"""
                    tcy2[(j*2)][(i*2)+1]=1
                    tcy2[(j*2)+1][(i*2)]=1
                    """tcy2[(j*2)+1][(i*2)+1]=0"""
    """print("\nReading transparencies\n")
    print("tcy1=")
    for i in range(len(tcy1)):
        print(tcy1[i])
    print("\ntcy2=")
    for i in range(len(tcy2)):
        print(tcy2[i])"""
    tcyGen(tcy1, tcy2)
    
    #read mapped matrix
    #print("test ",matrixMapping[2][6])
    """for i in range (pic.size[0]):
        for j in range (pic.size[1]):
            print(matrixMapping[i][j], end=" ")
        print("\n")"""
    
    return

#Colors specified in hex code, #000000 for opaque black, #ffffff for opaque white
#Transparencies are last 2 chars and written as hex value of transparency percentage
#fully transparent=> alpha=0 in decimal =0/255 => 00 in hex
#fully opaque=> alpha=1 in decimal =255/255 => ff in hex
#Thus full white but 100% transparent is #ffffff00

def tcyGen(tcy1, tcy2):
    tcy1Out=Image.new("RGBA",(len(tcy1),len(tcy1)),color="#000000")
    tcy2Out=Image.new("RGBA",(len(tcy2),len(tcy2)),color="#000000")
    
    pix1=tcy1Out.load()
    pix2=tcy2Out.load()
    
    for i in range (len(tcy1)):
        for j in range (len(tcy1)):
            if tcy1[i][j]==0:
                pix1[j,i]=(255,255,255,0)
            if tcy2[i][j]==0:
                pix2[j,i]=(255,255,255,0)
    
    tcy1Out.save("layer1.png")
    tcy2Out.save("layer2.png")
    return

def imgCreate():

    return

def encryption():
    opt=input("\nChoose an option:\n1.Split a loaded image\n2.Create an encrypted image\n\n")
    if (int(opt)==1):
        oneSplit()
    elif (int(opt)==2):
        imgCreate()
    return

def decryption():
    print("Please choose the 1st layer")
    layer1=loadimage()
    print("Now choose the 2nd layer")
    layer2=loadimage()
    
    
    with Image.open(layer1) as lay1:
        pix1=lay1.load()
    with Image.open(layer2) as lay2:
        pix2=lay2.load()
        
    imgOut=Image.new("RGBA", lay1.size, color="#00000000")
    pixFinal=imgOut.load()
    for i in range (lay1.size[0]):
        for j in range (lay1.size[1]):
            pixFinal[i,j]=pix1[i,j] or pix2[i,j]
            """print("pix1 values=", pix1[i,j])
            print("pix2 values=", pix2[i,j])
            print("pixFinal values=", pixFinal[i,j])"""
            
    imgOut.save("decryptedImage.png")
    
    
    return


def main(argv):
    inputImage1=""
    inputImage2=""

    try:
        opts, args = getopt.getopt(argv, "i:t:", ["image1=","image2="])
    except:
        print("python3 <projectname.py> -i <image1_relative_path> -t <image2_relative_path>\n")
        exit(1)
    for opt, arg in opts:
        if opt in ("-i", "--image1"):
            inputImage1=arg
        elif opt in ("-t", "--image2"):
            inputImage2=arg


    #print("Input file name of 1st image:\n", os.path.abspath(inputImage1))
    #print("\nInput file name of 2nd image:\n", os.path.abspath(inputImage2))
    select=input("\nSelect one option of the Two.\n1.Encryption\n2.Decryption\n\n")

    if (int(select)==1):
        encryption()
    elif (int(select)==2):
        decryption()
    



if __name__=='__main__':
    main(sys.argv[1:])

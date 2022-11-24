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
                    tcy1[j][i]=1
                    tcy1[j][i+1]=0
                    tcy1[j+1][i]=0
                    tcy1[j+1][i+1]=1
                    
                    tcy2[j][i]=0
                    tcy2[j][i+1]=1
                    tcy2[j+1][i]=1
                    tcy2[j+1][i+1]=0
                else:
                    tcy1[j][i]=0
                    tcy1[j][i+1]=1
                    tcy1[j+1][i]=1
                    tcy1[j+1][i+1]=0
                    
                    tcy2[j][i]=1
                    tcy2[j][i+1]=0
                    tcy2[j+1][i]=0
                    tcy2[j+1][i+1]=1
            else:
                if (a):
                    tcy1[j][i]=1
                    tcy1[j][i+1]=0
                    tcy1[j+1][i]=0
                    tcy1[j+1][i+1]=1
                    
                    tcy2[j][i]=1
                    tcy2[j][i+1]=0
                    tcy2[j+1][i]=0
                    tcy2[j+1][i+1]=1
                else:
                    tcy1[j][i]=0
                    tcy1[j][i+1]=1
                    tcy1[j+1][i]=1
                    tcy1[j+1][i+1]=0
                    
                    tcy2[j][i]=0
                    tcy2[j][i+1]=1
                    tcy2[j+1][i]=1
                    tcy2[j+1][i+1]=0
    print("\nReading transparencies\n")
    print("tcy1=\n", tcy1 )
    print("tcy2=\n", tcy2 )
    #read mapped matrix
    #print("test ",matrixMapping[2][6])
    for i in range (pic.size[0]):
        for j in range (pic.size[1]):
            print(matrixMapping[i][j], end=" ")
        print("\n")
    
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


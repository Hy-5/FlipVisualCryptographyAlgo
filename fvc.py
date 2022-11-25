#Implementing both Visual Cryptography and Flip Visual Cryptography schemes to evaluate
#security and expansion size

import sys, getopt, os, random
import tkinter as tk
from tkinter.filedialog import askopenfilename as loadimage
from PIL import Image


def encryption():

    #initializing matrix holding picture's binary values (white pxl=0, black pxl=1)

    imgName=loadimage()
    print(imgName)
    with Image.open(imgName) as pic:
        print("pic size =",pic.size, end="\n")
        pic = pic.convert("RGBA")
        pixel=pic.load()
    matrixMapping=[[0]*(pic.size[1]) for _ in range(pic.size[0])]
    tcy1=[[0]*(pic.size[1]*2) for _ in range(pic.size[0]*2)]
    tcy2=[[0]*(pic.size[1]*2) for _ in range(pic.size[0]*2)]
    for i in range (pic.size[0]):
        for j in range(pic.size[1]):
            a=bool(random.getrandbits(1))
            if pixel[i,j]<=(200,200,200,200):
                matrixMapping[j][i]=1
                if (a):
                    tcy1[(j*2)][(i*2)]=1
                    tcy1[(j*2)+1][(i*2)+1]=1
                    
                    tcy2[(j*2)][(i*2)+1]=1
                    tcy2[(j*2)+1][(i*2)]=1
                else:
                    tcy1[(j*2)][(i*2)+1]=1
                    tcy1[(j*2)+1][(i*2)]=1
                    
                    tcy2[(j*2)][(i*2)]=1
                    tcy2[(j*2)+1][(i*2)+1]=1
            else:
                if (a):
                    tcy1[(j*2)][(i*2)]=1
                    tcy1[(j*2)+1][(i*2)+1]=1
                    
                    tcy2[(j*2)][(i*2)]=1
                    tcy2[(j*2)+1][(i*2)+1]=1
                else:
                    tcy1[(j*2)][(i*2)+1]=1
                    tcy1[(j*2)+1][(i*2)]=1
                    
                    tcy2[(j*2)][(i*2)+1]=1
                    tcy2[(j*2)+1][(i*2)]=1

    tcyGen(tcy1, tcy2) 
    return


#generates 2 transparency images from input matrices tcy1 and tcy2
def tcyGen(tcy1, tcy2):
    #colors are hex codes with (optional) 2 last characters for transparency
    #Fully opaque = 255 in dec => ff in hex || Fully transparent = 0 in dec => 00 in hex
    tcy1Out=Image.new("RGBA",(len(tcy1),len(tcy1)),color="#000000")
    tcy2Out=Image.new("RGBA",(len(tcy2),len(tcy2)),color="#000000")
    
    pix1=tcy1Out.load()
    pix2=tcy2Out.load()
    
    for i in range (len(tcy1)):
        for j in range (len(tcy1)):
            if tcy1[i][j]==0:
                pix1[j,i]=(0,0,0,0)
            if tcy2[i][j]==0:
                pix2[j,i]=(0,0,0,0)
    
    tcy1Out.save("layer1.png")
    tcy2Out.save("layer2.png")
    return


#Lin et al. FVC algo (2010)
#doi:10.1016/j.jvcir.2010.08.006
def fvcEncrypt():
    print("Select the 1st secret image")
    secret1=loadimage()
    print("Select the 2nd secret image")
    secret2=loadimage()
    
    with Image.open(secret1) as sc1:
        print("Secret pic1 size =",sc1.size, end="\n")
        sc1 = sc1.convert("RGBA")
        pixel1=sc1.load()
    
    with Image.open(secret2) as sc2:
        print("Secret pic2 size =",sc2.size, end="\n")
        sc2 = sc2.convert("RGBA")
        pixel2=sc2.load()
    
    #creating identical size transparency matrices
    tcy1=[[0]*(sc1.size[1]) for _ in range(sc1.size[0])]
    tcy2=[[0]*(sc2.size[1]) for _ in range(sc2.size[0])]
    
    #creating the basis matrices
    b1=[[0,0,1,1,1,1],[0,1,0,1,1,1],[0,1,1,1,0,1],[0,1,1,1,1,0]]
    rb1=[[b1[j][i] for j in range(len(b1))] for i in range(len(b1[0])-1,-1,-1)]
    """for i in range (len(rb1)):
        print(rb1[i])"""
    print("b1:")
    for i in range (len(rb1)):
        print(rb1[i])
    print("\n")
    b2=[[0,0,1,1,1,1],[0,1,0,1,1,1],[0,1,1,1,1,0],[1,1,0,1,1,0]]
    rb2=[[b2[j][i] for j in range(len(b2))] for i in range(len(b2[0])-1,-1,-1)]
    print("b2:")
    for i in range (len(rb2)):
        print(rb2[i])
    print("\n")
    b3=[[0,0,1,1,1,1],[0,1,0,1,1,1],[1,0,1,1,0,1],[0,1,1,1,1,0]]
    rb3=[[b3[j][i] for j in range(len(b3))] for i in range(len(b3[0])-1,-1,-1)]
    print("b3:")
    for i in range (len(rb3)):
        print(rb3[i])
    print("\n")
    b4=[[0,0,1,1,1,1],[0,1,0,1,1,1],[1,0,1,1,0,1],[1,1,0,1,1,0]]
    rb4=[[b4[j][i] for j in range(len(b4))] for i in range(len(b4[0])-1,-1,-1)]
    print("b4:")
    for i in range (len(rb4)):
        print(rb4[i])
    print("\n")
    b5=[[0,0,1,1,1,1],[0,1,0,1,1,1],[0,1,1,1,1,0],[1,0,1,1,1,0]]
    rb5=[[b5[j][i] for j in range(len(b5))] for i in range(len(b5[0])-1,-1,-1)]
    print("b5:")
    for i in range (len(rb5)):
        print(rb5[i])
    print("\n")
    b6=[[0,0,1,1,1,1],[0,1,0,1,1,1],[0,1,1,1,0,1],[1,1,1,1,0,0]]
    rb6=[[b6[j][i] for j in range(len(b6))] for i in range(len(b6[0])-1,-1,-1)]
    print("b6:")
    for i in range (len(rb6)):
        print(rb6[i])
    print("\n")
    b7=[[0,0,1,1,1,1],[0,1,0,1,1,1],[1,0,1,0,1,1],[1,0,1,1,0,1]]
    rb7=[[b7[j][i] for j in range(len(b7))] for i in range(len(b7[0])-1,-1,-1)]
    print("b7:")
    for i in range (len(rb7)):
        print(rb7[i])
    print("\n")
    b8=[[0,0,1,1,1,1],[0,1,0,1,1,1],[1,0,1,1,0,1],[1,1,1,0,1,0]]
    rb8=[[b8[j][i] for j in range(len(b8))] for i in range(len(b8[0])-1,-1,-1)]
    print("b8:")
    for i in range (len(rb8)):
        print(rb8[i])
    print("\n")
    b9=[[0,0,1,1,1,1],[0,1,0,1,1,1],[1,1,0,0,1,1],[0,1,1,0,1,1]]
    rb9=[[b9[j][i] for j in range(len(b9))] for i in range(len(b9[0])-1,-1,-1)]
    print("b9:")
    for i in range (len(rb9)):
        print(rb9[i])
    print("\n")
    b10=[[0,0,1,1,1,1],[0,1,0,1,1,1],[1,1,0,1,0,1],[1,1,0,1,1,0]]
    rb10=[[b10[j][i] for j in range(len(b10))] for i in range(len(b10[0])-1,-1,-1)]
    print("b10:")
    for i in range (len(rb10)):
        print(rb10[i])
    print("\n")
    b11=[[0,0,1,1,1,1],[0,1,0,1,1,1],[1,1,1,1,0,0],[0,1,1,1,1,0]]
    rb11=[[b11[j][i] for j in range(len(b11))] for i in range(len(b11[0])-1,-1,-1)]
    print("b11:")
    for i in range (len(rb11)):
        print(rb11[i])
    print("\n")
    b12=[[0,0,1,1,1,1],[0,1,0,1,1,1],[1,1,1,1,0,0],[1,1,0,1,1,0]]
    rb12=[[b12[j][i] for j in range(len(b12))] for i in range(len(b12[0])-1,-1,-1)]
    print("b12:")
    for i in range (len(rb12)):
        print(rb12[i])
    print("\n")
    b13=[[0,0,1,1,1,1],[0,1,0,1,1,1],[1,1,0,0,1,1],[1,0,1,0,1,1]]
    rb13=[[b13[j][i] for j in range(len(b13))] for i in range(len(b13[0])-1,-1,-1)]
    print("b13:")
    for i in range (len(rb13)):
        print(rb13[i])
    print("\n")
    b14=[[0,0,1,1,1,1],[0,1,0,1,1,1],[1,1,0,0,1,1],[1,1,1,0,1,0]]
    rb14=[[b14[j][i] for j in range(len(b14))] for i in range(len(b14[0])-1,-1,-1)]
    print("b14:")
    for i in range (len(rb14)):
        print(rb14[i])
    print("\n")
    b15=[[0,0,1,1,1,1],[0,1,0,1,1,1],[1,1,1,0,0,1],[1,0,1,0,1,1]]
    rb15=[[b15[j][i] for j in range(len(b15))] for i in range(len(b15[0])-1,-1,-1)]
    print("b5:")
    for i in range (len(rb15)):
        print(rb15[i])
    print("\n")
    b16=[[0,0,1,1,1,1],[0,1,0,1,1,1],[1,1,1,0,0,1],[1,1,1,0,1,0]]
    rb16=[[b16[j][i] for j in range(len(b16))] for i in range(len(b16[0])-1,-1,-1)]
    print("b16:")
    for i in range (len(rb16)):
        print(rb16[i])
    
    #checking the quadruples
    quad=""
    index1=""
    index2=""
    index3=""
    index4=""
    for i in range(sc1.size[0]):
        for j in range(sc1.size[1]):
            randomCol=""
            print(i,j)
            if pixel1[j,i]<(200,200,200,200):
                index1="B"
            else:
                index1="W"
            if pixel1[(sc1.size[1]-1-j),i]<(200,200,200,200):
                index2="B"
            else:
                index2="W"
            if pixel2[j,i]<(200,200,200,200):
                index3="B"
            else:
                index3="W"
            if pixel2[(sc2.size[1]-1-j),i]<(200,200,200,200):
                index4="B"
            else:
                index4="W"
            quad=index1+index2+index3+index4
            """print("supposed p1 is", pixel1[i,j])
            print("supposed p2 is", pixel2[i,j])"""
            print("For",i,j,"Value of quad is",quad)
            
            a=random.randint(0,5)
    
            if quad=="WWWW":
                for iter in range(len(b1)):
                    randomCol+=str(rb1[a][iter])
                print("randomCol is",randomCol)
            elif quad=="WWWB":
                for iter in range(len(b1)):
                    randomCol+=str(rb2[a][iter])
                print("randomCol is",randomCol)
            elif quad=="WWBW":
                for iter in range(len(b1)):
                    randomCol+=str(rb3[a][iter])
                print("randomCol is",randomCol)
            elif quad=="WWBB":
                for iter in range(len(b1)):
                    randomCol+=str(rb4[a][iter])
                print("randomCol is",randomCol)
            elif quad=="WBWW":
                for iter in range(len(b1)):
                    randomCol+=str(rb5[a][iter])
                print("randomCol is",randomCol)
            elif quad=="WBWB":
                for iter in range(len(b1)):
                    randomCol+=str(rb6[a][iter])
                print("randomCol is",randomCol)
            elif quad=="WBBW":
                for iter in range(len(b1)):
                    randomCol+=str(rb7[a][iter])
                print("randomCol is",randomCol)
            elif quad=="WBBB":
                for iter in range(len(b1)):
                    randomCol+=str(rb8[a][iter])
                print("randomCol is",randomCol)
            elif quad=="BWWW":
                for iter in range(len(b1)):
                    randomCol+=str(rb9[a][iter])
                print("randomCol is",randomCol)
            elif quad=="BWWB":
                for iter in range(len(b1)):
                    randomCol+=str(rb10[a][iter])
                print("randomCol is",randomCol)
            elif quad=="BWBW":
                for iter in range(len(b1)):
                    randomCol+=str(rb11[a][iter])
                print("randomCol is",randomCol)
            elif quad=="BWBB":
                for iter in range(len(b1)):
                    randomCol+=str(rb12[a][iter])
                print("randomCol is",randomCol)
            elif quad=="BBWW":
                for iter in range(len(b1)):
                    randomCol+=str(rb13[a][iter])
                print("randomCol is",randomCol)
            elif quad=="BBWB":
                for iter in range(len(b1)):
                    randomCol+=str(rb14[a][iter])
                print("randomCol is",randomCol)
            elif quad=="BBBW":
                for iter in range(len(b1)):
                    randomCol+=str(rb15[a][iter])
                print("randomCol is",randomCol)
            elif quad=="BBBB":
                for iter in range(len(b1)):
                    randomCol+=str(rb16[a][iter])
                print("randomCol is",randomCol)
            
    return


#adds up 2 secret images and outputs secret message in decryptedImage.png
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
            if (pix1[i,j])==(pix2[i,j]):
                #print("same")
                pixFinal[i,j]=pix1[i,j]
            else:
                #print("not same")
                pixFinal[i,j]=max(pix1[i,j],pix2[i,j])
            
    imgOut.save("decryptedImage.png")
    return


def main(argv):
    #command line args 
    """inputImage1=""
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
            inputImage2=arg"""

    #absolute path of args
    #print("Input file name of 1st image:\n", os.path.abspath(inputImage1))
    #print("\nInput file name of 2nd image:\n", os.path.abspath(inputImage2))
    
    select=input("\nSelect one option:\n1.Visual Cryptography Encryption\n2.Flip Visual Cryptography Encryption\n3.Decryption\n\n")
    if (int(select)==1):
        encryption()
    elif (int(select)==2):
        fvcEncrypt()
    elif (int(select)==3):
        decryption()
    

if __name__=='__main__':
    main(sys.argv[1:])

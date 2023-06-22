import time 
import re 
import subprocess 
import datetime 
import shutil 
import os 
import random 
import math

iterationCounter=0
FlexPDEdirectory='c:\FlexPDE6student\FlexPDE6s.exe'

f6=open("dB_data.csv","w")
f6.write("Alpha4"+","+
"Alpha3" +","+
"Alpha2" +","+
"Alpha6" +","+
"Bmax" +","+
"Bmin" +","+
"dB" +","+
"Alignment" +","+
 "\n")
f6.close()

while(1):
	
     DecAlpha4 = (random.randrange(5, 35, 3))
     DecAlpha3 = (random.randrange(5, (40 - DecAlpha4), 3))
     DecAlpha2 = (random.randrange(5, (45 - DecAlpha4 - DecAlpha3), 3))
     DecAlpha6 = (random.randrange(0, 45, 3))
     
     Alpha4 = (3.14 / 180) * DecAlpha4
     Alpha3 = (3.14 / 180) * DecAlpha3
     Alpha2 = (3.14 / 180) * DecAlpha2
     Alpha6 = (3.14 / 180) * DecAlpha6
	
     f1=open ("input.pde","w") 
     f1.write(
     "Alpha4="+str(Alpha4)+"\nAlpha3="+str(Alpha3)+"\nAlpha2="+str(Alpha2)+
     "\nAlpha6="+str(Alpha6)
     )
     f1.close()
	
	
     subprocess.call([FlexPDEdirectory,'Mini_Project_Model.pde','-S'])
	
     f2=open ('Output.txt',"r")
     val=f2.read()
     Bmax=re.search('(Bmax= )(.*)',val).group(2)
     Bmin=re.search('(Bmin= )(.*)',val).group(2)
     dB=re.search('(dB= )(.*)',val).group(2)
     Alignment=re.search('(Alignment= )(.*)',val).group(2)
     f2.close()
	
	
     f6=open("dB_data.csv","a")
     f6.write(str(Alpha4)+","+str(Alpha3)+","+str(Alpha2)+","+str(Alpha6)+","+str(Bmax)+","+str(Bmin)+","+str(dB)+","+str(Alignment)+
     "\n")
	
	
	
     f6.close()
	
     iterationCounter = iterationCounter + 1
     print "simulation ", iterationCounter
	

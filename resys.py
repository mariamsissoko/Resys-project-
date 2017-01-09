# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 10:14:58 2016

@author: Mariam
"""

def readFile(fileName):
    matr=[]
    f=open(fileName,'r')
    line=f.readline()
    while len(line)>0:
        line=line.split('\t')
        line[len(line)-1]=line[len(line)-1][0:len(line[len(line)-1])-1]
        matr.append(line)
        line=f.readline()
    return matr
    
def dicProfils(mat):
    dicProf={}
    for i in range(1,len(mat)):
        cell=mat[i][0]
        del(mat[i][0])
        profil=mat[i]
        profil=','.join(profil)
        try:
            dicProf[profil].append(cell)
        except  KeyError:
            dicProf[profil]=[cell]
    return dicProf

def singleCellTransition(matProf):
    print matProf[0]
    change=0
    l=0
    for i in range(1,len(matProf)):
        for j in range(i+1,len(matProf)): 
            count=0
            for k in range(1,len(matProf[i])): 
                if matProf[i][k]!=matProf[j][k]:
                    count+=1
            print count  
            print l
            if count==1:
                change+=1
            l+=1
   
    print change
    return 

matProf=readFile("hemato_embryo.tsv")  
#ingleCellTransition(matProf)
dico=dicProfils(matProf)
count=0
for i in dico.keys():
    if len(dico[i])>2:
        count+=1
print count
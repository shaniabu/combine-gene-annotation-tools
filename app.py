# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 19:36:07 2020

@author: Q56074043
"""

import app_interface
import sys
import os
import numpy as np
import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QLineEdit
import FATHMN_web, MSC_web, Mutation_Assessor_web, PROVEAN_web



main_window = app_interface.Ui_MainWindow

class CoperQt(QtWidgets.QMainWindow,main_window):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)  
        main_window.__init__(self)
        self.setupUi(self)  
        self.cwd = os.getcwd()
#                
        self.Download.clicked.connect(self.download_file)
        self.FATHMN.clicked.connect(self.fathmn)
        self.MSC.clicked.connect(self.msc)
        self.PROVEAN.clicked.connect(self.provean)
        self.Mutation.clicked.connect(self.mutation)
        
        
    def download_file(self):
        ans = []
        F = open('./web_result/Fathmn_result.txt', 'r')
        while True:
            line = F.readline()
            if not line:
                break
            fathmn = list(line.split("\t"))
            count = len(ans)
            temp = 0
            while count>0:
                if fathmn[1] == ans[count-1][1]:
                    temp=1
                    break
                else:
                    count = count -1
                    temp=0
            if temp==0:
                f = [fathmn[0:4] + fathmn[6:8]]
                ans.extend(f)
        F.close()
        
        temp = 0
        msc_temp = []
        with open('./web_result/MSC_result.csv', 'r', newline='') as csvfile: 
            msc = csv.reader(csvfile)
            for i in msc:
                count = len(msc_temp)
                while count >0:
                    if i[1] == msc_temp[count-1][1]:
                        temp=1
                        break
                    else:
                        count = count -1 
                        temp=0
                if temp ==0:
                    m = [i[0:2]+i[3:5]+['','']+i[6:7]+i[8:9]+i[10:12]+i[15:17]]
                    msc_temp.extend(m)
            for i in range(1,len(msc_temp)):
                count = len(ans)
                temp=0
                while count>0:
                    if msc_temp[i][1] == ans[count-1][1]:
                        ans[count-1] = ans[count-1] + msc_temp[i][6:12]
                        temp = 1
                        break
                    else:
                        count  = count-1
                        temp = 0
                if temp == 0:
                    ans.extend([msc_temp[i]])
        
        temp = 0
        mutation_temp = []    
        with open('./web_result/MutationAssessor.output.csv', 'r', newline='') as csvfile: 
            mutation = csv.reader(csvfile) 
            for i in mutation:
                count = len(mutation_temp)
                while count >0:
                    if i[1].split(',')[2] == mutation_temp[count-1][1]:
                        temp=1
                        break
                    else:
                        count = count -1 
                        temp=0
                if temp ==0:
                    mu = [i[1].split(',')[1:]+['','','','','','','','']+i[7:9]+i[11:12]]
                    mutation_temp.extend(mu)
            for i in range(1,len(mutation_temp)):
                count = len(ans)
                temp=0
                while count>0:
                    if mutation_temp[i][1] == ans[count-1][1]:
                        ans[count-1] = ans[count-1] + mutation_temp[i][12:15]
                        temp = 1
                        break
                    else:
                        count  = count-1
                        temp = 0
                if temp == 0:
                    ans.extend([mutation_temp[i]])
        temp = 0
        provean_temp = []      
        with open('./web_result/Provean_result.csv', 'r', newline='',encoding="utf-8") as csvfile: 
            provean = csv.reader(csvfile)
            for i in provean:
                count = len(provean_temp)
                while count >0:
                    if i[1].split(',')[1] == provean_temp[count-1][1]:
                        temp=1
                        break
                    else:
                        count = count -1 
                        temp=0
                if temp ==0:
                    p = [i[1].split(',')+['','','','','','','','','','','']+i[10:12]+i[14:16]]
                    provean_temp.extend(p)
            for i in range(1,len(provean_temp)):
                count = len(ans)
                temp=0
                while count>0:
                    if provean_temp[i][1] == ans[count-1][1]:
                        ans[count-1] = ans[count-1] + provean_temp[i][15:19]
                        temp = 1
                        break
                    else:
                        count  = count-1
                        temp = 0
                if temp == 0:
                    ans.extend([provean_temp[i]])
        
        with open('result.csv', 'w', newline='') as csvfile: 
            writer = csv.writer(csvfile)
            writer.writerow(['Chromosome','Position', 'Reference', 'Allele', 'Fathmn_Coding Score', 'Fathmn_Coding Groups','CADD_Score','MSC-CADD_Impact_Pred','PolyPhen2_Score','hvar_prediction','SIFT_Score','SIFT_Pred','mutation_Func. Impact','mutation_FI score','mutation_MSA height','Provean_SCORE','Provean_PREDICTION (cutoff=-2.5)','Provean_SCORE','Provean_PREDICTION (cutoff=0.05)',])
            for i in range(len(ans)):
                writer.writerow(ans[i])
        print('finish!!')
        
    def fathmn(self): 
        path = self.file_path.text()
        path = path.replace('\\','//')
        path = path + '.xlsx'
        FATHMN_web.catchData(path)
        
    def msc(self):
        path = self.file_path.text()
        path = path.replace('\\','//')
        path = path + '.xlsx'
        MSC_web.catchData(path)
    
    def provean(self):
        path = self.file_path.text()
        path = path.replace('\\','//')
        path = path + '.xlsx'
        PROVEAN_web.catchData(path)
        
    def mutation(self):
        path = self.file_path.text()
        path = path.replace('\\','//')
        path = path + '.xlsx'
        Mutation_Assessor_web.catchData(path)
       
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CoperQt()
    window.show()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 18:56:10 2020

@author: Q56074043
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 23:33:31 2019

@author: Q56074043
"""

import requests
import urllib.parse
import csv
import pandas as pd
import xlrd
import math
from selenium import webdriver
# FATHMN format : chromosome,Region,Reference,Allele



def catchData(path):
    book = xlrd.open_workbook(path)
    sheet1 = book.sheets()[0]
    variantTextArea = "\n"
    ans = []
    num=10   #筆數
    for j in range(math.ceil(sheet1.nrows/num)):#math.ceil(sheet1.nrows/num)
    #    variantTextArea = "\n"
        for i in range(j*num,(j+1)*num):#sheet1.nrows
            if i<sheet1.nrows:
                row3_values = sheet1.row_values(i)
                if row3_values[5]=='SNV':
                    one = str(int(row3_values[1]))
                    two = str(row3_values[2])
                    two = two.split('.')[0]
                    three = row3_values[3]
                    four = row3_values[4]
        
                    string = one + ',' + two + ',' + three + ',' + four + '\n'
                    variantTextArea = variantTextArea+ string
    
    
    
    url = 'http://fathmm.biocompute.org.uk/fathmmMKL.htm'
    
    
    #f = open('FATHMN_data.txt', "r")
    
    driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\chromedriver.exe')
    driver.get(url)
    driver.maximize_window()
    
    driver.find_element_by_id('batch').send_keys(variantTextArea)
    # 手動點擊submit 以及download
    # 複製網頁內容


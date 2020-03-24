# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 18:57:21 2020

@author: Q56074043
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 23:04:29 2019

@author: Q56074043
"""
import requests
import urllib.parse
import csv
import pandas as pd
import xlrd
import math
from selenium import webdriver
# Mutation Assessor format : hg19,chromosome,Region,Reference,Allele

def catchData(path):
    
    book = xlrd.open_workbook(path)
    sheet1 = book.sheets()[0]
    variantTextArea = "\n"
    ans = []
    num=10   #筆數
    for j in range(math.ceil(sheet1.nrows/num)):#
    #    variantTextArea = "\n"
        for i in range(j*num,(j+1)*num):#sheet1.nrows
            if i<sheet1.nrows:
                row3_values = sheet1.row_values(i)
                one = 'hg19'
                two = str(int(row3_values[1]))
                three = str(row3_values[2])
                if three.find('..')!=-1:
                    three_1 = three.split('..')
                    for k in range(int(three_1[1])-int(three_1[0])+1):
                        three = str(int(three_1[0])+k)
                        four_1 = row3_values[3]
                        if len(four_1)!=1:
                            four = four_1[k] 
                        else:
                            four = four_1
                            if four == '-':
                                  four = '_'
                        five_1 = row3_values[4]
                        if len(five_1)!=1:
                            five = five_1[k]
                        else:
                            five = five_1
                            if five == '-':
                                five = '_'
    
                        string = one + ',' + two + ',' + three + ',' + four + ',' + five + '\n'
                        variantTextArea = variantTextArea+ string
    
                elif three.find('^')!=-1:
                    three_1 = three.split('^')
                    four_1 = row3_values[3]
                    five_1 = row3_values[4]
                    for k in range(len(five_1)):
                        three = str(int(three_1[1])+k)
                        if four_1 == '-':
                            four = '_'
                        five = five_1[k]
                        string = one + ',' + two + ',' + three + ',' + four + ',' + five + '\n'
                        variantTextArea = variantTextArea+ string
    
                else:
                    three = three.split('.')[0]
                    four = row3_values[3]
                    five = row3_values[4]
                    
                    if four == '-':
                        four = '_'
                    if five == '-':
                        five = '_'
                    
                    string = one + ',' + two + ',' + three + ',' + four + ',' + five + '\n'
                    variantTextArea = variantTextArea+ string
    
    url = 'http://mutationassessor.org/r3/'
    
    driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\chromedriver.exe')
    driver.get('http://mutationassessor.org/r3/')
    driver.maximize_window()
    
    driver.find_element_by_id('vars').send_keys(variantTextArea)
    driver.find_element_by_name('tableQ').click()
    """ 自己按送出 """
    #driver.find_element_by_xpath("//input[@value=' submit ']").click()
    

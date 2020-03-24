# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 18:58:54 2020

@author: Q56074043
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 00:18:15 2019

@author: Q56074043
"""

import time
import requests
import urllib.parse
import csv
import pandas as pd
import xlrd
import math
from selenium import webdriver
# PROVEAN format : chromosome,Region,Reference,Allele

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
                one = str(int(row3_values[1]))
                two = str(row3_values[2])
                if two.find('..')!=-1:
                    two_1 = two.split('..')
                    for k in range(int(two_1[1])-int(two_1[0])+1):
                        two = str(int(two_1[0])+k)
                        three_1 = row3_values[3]
                        four_1 = row3_values[4]
                        if len(four_1)!=1:
                            four = four_1[k] 
                        else:
                            four = four_1
                            if four == '-':
                                  four = '.'
                     
                        if len(three_1)!=1:
                            three = three_1[k]
                        else:
                            three = three_1
                            if three == '-':
                                three = '.'
                        string = one + ',' + two + ',' + three + ',' + four + '\n'
                        variantTextArea = variantTextArea+ string
    
                elif two.find('^')!=-1:
                    two_1 = two.split('^')
                    three_1 = row3_values[3]
                    four_1 = row3_values[4]
                    for k in range(len(four_1)):
                        two = str(int(two_1[1])+k)
                        if three_1 == '-':
                            three = '.'
                        four = four_1[k]
                        string = one + ',' + two + ',' + three + ',' + four + '\n'
                        variantTextArea = variantTextArea+ string
    
                else:
                    two = two.split('.')[0]
                    three = row3_values[3]
                    four = row3_values[4]
                    
                    if four == '-':
                        four = '.'
                    if three == '-':
                        three = '.'
                    
                    string = one + ',' + two + ',' + three + ',' + four + '\n'
                    variantTextArea = variantTextArea+ string
    
    
    
    url = 'http://provean.jcvi.org/genome_submit_2.php?species=human&fbclid=IwAR2kfnydOI6wsWab0CAfNw0zIeaRVeTJsCrSmdWvM1Cwm8NoUo8IAHdQ_JQ'
    
    
    driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\chromedriver.exe')
    driver.get(url)
    driver.maximize_window()
    
    driver.find_element_by_id('CHR').send_keys(variantTextArea)
    
    driver.find_element_by_xpath("//input[@value='gene_id']").click()
    driver.find_element_by_xpath("//input[@value='gene_name']").click()
    driver.find_element_by_xpath("//input[@value='transcript_id']").click()
    driver.find_element_by_xpath("//input[@value='transcript_status']").click()
    driver.find_element_by_xpath("//input[@value='description']").click()
    driver.find_element_by_xpath("//input[@value='gc_content']").click()
    driver.find_element_by_xpath("//input[@value='chr_band']").click()
    driver.find_element_by_xpath("//input[@value='family_id']").click()
    driver.find_element_by_xpath("//input[@value='family_desc']").click()
    driver.find_element_by_xpath("//input[@value='uniprot_id']").click()
    driver.find_element_by_xpath("//input[@value='refseq_protein_id']").click()
    driver.find_element_by_xpath("//input[@value='mim_accession']").click()
    driver.find_element_by_xpath("//input[@value='pfam_id']").click()
    driver.find_element_by_xpath("//input[@value='tigrfam_id']").click()
    driver.find_element_by_xpath("//input[@value='interpro_id']").click()
    driver.find_element_by_xpath("//input[@value='go_term_accession']").click()
    driver.find_element_by_xpath("//input[@value='go_slim_goa_accession']").click()
    
    
    driver.find_element_by_xpath("//input[@type='submit']").click()
    
    
    
    # 手動點擊download
    # 用excel開啟，把編碼設為utf-8，並且設定以tab鍵分隔
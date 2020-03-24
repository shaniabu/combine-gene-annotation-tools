# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 18:46:12 2020

@author: Q56074043
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 18:28:27 2019

@author: Q56074043
"""

import requests
import urllib.parse
import csv
import pandas as pd
import xlrd
import math

# MSC format : chromosome    Region    ID    Reference    Allele    Homo_sapines_refseq 
def catchData(path):
    
    book = xlrd.open_workbook('input_data.xlsx')
    sheet1 = book.sheets()[0]
    variantTextArea = "\n"
    ans = []
    num=10   #筆數
    for j in range(math.ceil(sheet1.nrows/num)):#math.ceil(sheet1.nrows/num)
        variantTextArea = "\n"
        for i in range(j*num,(j+1)*num):#sheet1.nrows
            if i<sheet1.nrows:
                row3_values = sheet1.row_values(i)
                one = str(int(row3_values[1]))
                two = str(row3_values[2])
                if two.find('..')!=-1:
                    two_1 = two.split('..')
                    for k in range(int(two_1[1])-int(two_1[0])+1):
                        two = str(int(two_1[0])+k)
                        three = row3_values[0]
                        four_1 = row3_values[3]
                        if len(four_1)!=1:
                            four = four_1[k] 
                        else:
                            four = four_1
                            if four == '-':
                                  four = '.'
                        five_1 = row3_values[4]
                        if len(five_1)!=1:
                            five = five_1[k]
                        else:
                            five = five_1
                            if five == '-':
                                five = '.'
                        six = row3_values[6]
                        string = one + '\t' + two + '\t' + three + '\t' + four + '\t' + five + '\t' + six + '\n'
                        variantTextArea = variantTextArea+ string
    
                elif two.find('^')!=-1:
                    two_1 = two.split('^')
                    three = row3_values[0]
                    four_1 = row3_values[3]
                    five_1 = row3_values[4]
                    six = row3_values[6]
                    for k in range(len(five_1)):
                        two = str(int(two_1[1])+k)
                        if four_1 == '-':
                            four = '.'
                        five = five_1[k]
                        string = one + '\t' + two + '\t' + three + '\t' + four + '\t' + five + '\t' + six + '\n'
                        variantTextArea = variantTextArea+ string
    
                else:
                    two = two.split('.')[0]
                    three = row3_values[0]
                    four = row3_values[3]
                    five = row3_values[4]
                    six = row3_values[6]
                    
                    if four == '-':
                        four = '.'
                    if five == '-':
                        five = '.'
                    
                    string = one + '\t' + two + '\t' + three + '\t' + four + '\t' + five + '\t' + six + '\n'
                    variantTextArea = variantTextArea+ string
    
        url = 'http://pec630.rockefeller.edu:8080/MSC/'
        
        # pretend as a real browser
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
        
        # request the website for cookie
        req = requests.get(url, headers=headers)
        
        cookie = req.headers['Set-Cookie']
        print(cookie)
        cookie = cookie[:cookie.index(';')]
        headers['Cookie'] = cookie
        
        # put the query info such as "Confidence Interval", "Apply MSC to" and  "variants" into the url, and needs to be encoded for url, see https://www.w3school.com.cn/tags/html_ref_urlencode.html
        variantTextArea = urllib.parse.quote(variantTextArea)
        url = 'http://pec630.rockefeller.edu:8080/MSC/VariantTextServlet?measure0=CADD&measure0=PolyPhen2&measure0=SIFT&confidenceInterval0=ci99&dbSource0=HGMD&displayDataSource0=YES&variantTextArea=' + variantTextArea
        
        # this action is like pressing the "Submit" button
        req = requests.get(url, headers=headers)
        
        # getting the "Download Result", this needs the cookie from above
        url = 'http://pec630.rockefeller.edu:8080/MSC/DownloadServlet'
        req = requests.post(url, headers=headers)
        
        temp = req.text.split('\n')
        if j!=0:
            temp = temp[1:-1]
            ans.extend(temp)
        else:
            temp = temp[:-1]
            ans.extend(temp)

    """ 需要先自行新增MSC_result.csv這個檔案喔 """
    with open('MSC_result.csv', 'w', newline='') as csvfile: 
        writer = csv.writer(csvfile)
        
        for i in range(len(ans)): 
            writer.writerow(ans[i].split("\t"))
    print("finish!")
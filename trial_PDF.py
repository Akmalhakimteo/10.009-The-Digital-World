# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 10:48:45 2019

@author: akmal
"""

import PyPDF2 as p2

PDFfile = open("file:///C:/Users/akmal/Downloads/Khutbah.pdf","rb")
pdfread = p2.PdfFileReader(PDFfile)

firstpage = pdfread.getPage(0)
print(firstpage.extractText())
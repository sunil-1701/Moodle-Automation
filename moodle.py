# -*- coding: utf-8 -*-
"""

@author: SUNIL

"""
#---------------- IMPORTING MODULES ----------------

import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()        #Create an instance of Chrome
browser.maximize_window()           #Maximize window


def login():
    userName="2021cs36su"
    Password="Mahadev@1701#"
    
    browser.get(('http://moodle.mitsgwalior.in/login/index.php'))

    username = browser.find_element('id','username')
    username.send_keys(userName)


    passW= browser.find_element('id','password')
    passW.send_keys(Password)
 
    signInButton = browser.find_element('id','loginbtn')
    signInButton.click()

def mark():
    
    try:
        browser.find_element(By.LINK_TEXT,"Submit attendance").click()
        browser.find_element(By.NAME,"status").click()
        browser.find_element(By.NAME,"submitbutton").click()
        browser.find_element(By.LINK_TEXT,"0901CS211121 SUNIL KUSHWAHA").click()
        browser.find_element(By.XPATH,"//a[@data-title='logout,moodle']").click()
    except:
        pass
    
def mark_pass():
    
    try:
        browser.find_element(By.LINK_TEXT,"Submit attendance").click()
        attendance_pass=input("Enter the password: ")
        browser.find_element('id','id_studentpassword').send_keys(attendance_pass)
        browser.find_element(By.NAME,"status").click()
        browser.find_element(By.NAME,"submitbutton").click()
        browser.find_element(By.LINK_TEXT,"0901CS211121 SUNIL KUSHWAHA").click()
        browser.find_element(By.XPATH,"//a[@data-title='logout,moodle']").click()
    except:
        pass
    
def dkm():
    browser.get(('http://moodle.mitsgwalior.in/mod/attendance/view.php?id=78740'))
    mark()

def rrm():
    browser.get(('http://moodle.mitsgwalior.in/mod/attendance/view.php?id=78452'))
    mark_pass()
    
def knt():
    browser.get(('http://moodle.mitsgwalior.in/mod/attendance/view.php?id=78506'))
    mark()
    
def mp():
    browser.get(('http://moodle.mitsgwalior.in/mod/attendance/view.php?id=78436'))
    mark()
    
def gk():
    browser.get(('http://moodle.mitsgwalior.in/mod/attendance/view.php?id=78302'))
    mark()

def cn_lab():
    browser.get(('http://moodle.mitsgwalior.in/mod/attendance/view.php?id=78743'))
    mark_pass()
def py_lab():
    browser.get(('http://moodle.mitsgwalior.in/mod/attendance/view.php?id=78341'))
    mark_pass()

def dbms_lab():
    browser.get(('http://moodle.mitsgwalior.in/mod/attendance/view.php?id=78601'))
    mark()


Time= datetime.datetime.now().strftime("%X")
login()
current_day=datetime.datetime.now().strftime("%a")

#-----------------------------------------------------
if current_day=="Fri":
    if "11:00:00">Time >"09:00:00":
        py_lab()
    
    elif "12:00:00">Time >"11:00:00":
        rrm()
    if "13:00:00">Time >"12:00:00":
        knt()

#-----------------------------------------------------
elif current_day=="Thu":
    if "11:00:00">Time >"10:00:00":
        mp()
    
    elif "12:00:00">Time >"11:00:00":
        dkm()

    elif "13:00:00">Time >"12:00:00":
        gk()
    
    elif "15:00:00">Time >"14:00:00":
        knt()
    
#-----------------------------------------------------
elif current_day=="Wed":
    if "11:00:00">Time >"10:00:00":
        gk()
    
    elif "12:00:00">Time >"11:00:00":
        rrm()

    elif "13:00:00">Time >"12:00:00":
        dkm()
    
#-----------------------------------------------------
elif current_day=="Tue":
    if "11:00:00">Time >"10:00:00":
        mp()

    elif "13:00:00">Time >"11:00:00":
        py_lab()
    
    elif "16:00:00">Time >"14:00:00":
        dbms_lab()
    
#-----------------------------------------------------
elif current_day=="Mon":
    if "11:00:00">Time>"10:00:00":
        dkm()
        
    elif "12:00:00">Time>"11:00:00":
        rrm()
    
    elif "13:00:00">Time>"12:00:00":
        knt()
    
    elif "15:00:00">Time>"14:00:00":
        mp()
        
    elif "16:00:00">Time>"15:00:00":
        gk()
    elif "18:00:00">Time>"16:00:00":
        cn_lab()
    
#-----------------------------------------------------

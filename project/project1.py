#Import Statements

import speech_recognition
from urllib.request import urlopen
from bs4 import BeautifulSoup
from newsplease import NewsPlease
import os
import random
import tkinter as tk
from tkinter import font as f
from tkinter import Text
from tkinter import *
from PIL import Image,ImageTk
import threading
import re
import json
import time
import webbrowser

#Functions

def IndiaToday(keyword):
    keyword = keyword.replace(' ','-').lower()
    html = urlopen(f'https://www.indiatoday.in/topic/crime')
    bs = BeautifulSoup(html, 'html.parser')
    lst = bs.find('div',{'class':'view-content'}).find_all('div',{'class':'search-pic'})
    for each in lst:
        file.write((str(each.find('a',href=True)['href']))+'\n')
        
def urlIndiaTV(keyword):
    keyword = keyword.replace(' ','-').lower()
    html = urlopen(f"https://www.indiatvnews.com/topic/{keyword}")
    bs = BeautifulSoup(html,'html.parser')
    try:
        lst = bs.find('ul',{'class':'newsListfull'}).find_all('li')
        for x in lst:
            file.write(str(x.find('a',href = True)['href'])+'\n')
    except:
        pass
    
def urlOneIndia(keyword):
    keyword = keyword.replace(' ','%20').lower()
    html = urlopen(f"https://www.oneindia.com/search/results.html?q=={keyword}")
    bs = BeautifulSoup(html,'html.parser')
    url_ini = "https://www.oneindia.com/"
    try:
        lst = bs.find('div',{'class':'search-results-list'}).find_all('li')
        for x in lst:
            file.write(url_ini + str(x.find('div',{'class':'image'}).find('a',href = True)['href'])+'\n')
    except:
        pass
    
def urlTheIndExp(keyword):
    keyword = keyword.replace(' ','-').lower()
    html = urlopen(f"https://indianexpress.com/?s={keyword}")
    bs = BeautifulSoup(html,'html.parser')
    try:
        lst = bs.find('div',{'class':'search-result'}).find_all('div',{'class':'details'})
        for x in lst:
            file.write(str(x.find('h3').find('a',href = True)['href'])+'\n')
    except:
        pass
    
def urlTOI(keyword):
    keyword = keyword.replace(' ','-').lower()
    html = urlopen(f"https://timesofindia.indiatimes.com/topic/{keyword}")
    bs = BeautifulSoup(html,'html.parser')
    url_ini = "https://timesofindia.indiatimes.com/topic"
    try:
        lst = bs.find('div',{'class':'tab_content'}).find_all('li')
        for x in lst:
            file.write(url_ini + str(x.find('div',{'class':'content'}).find('a',href = True)['href'])+'\n')
    except:
        pass
    
def Aajtak(keyword):
    keyword = keyword.replace(' ','-').lower()
    html = urlopen(f"https://aajtak.intoday.in/topic/{keyword}.html")
    bs = BeautifulSoup(html,'html.parser')
    try:
        lst = bs.find('div',{'class':'leftTopSearchSec'}).find_all('div',{'class':'scc_s'})
        for x in lst:
            file.write(str(x.find('a',href = True)['href'])+'\n')
    except:
        pass
    
def Khashkhabar(keyword):
    keyword = keyword.replace(' ','-').lower()
    html = urlopen(f"https://www.khaskhabar.com/tags/{keyword}")
    bs = BeautifulSoup(html,'html.parser')
    try:
        lst = bs.find('div',{'class':'grid_16 alpha'}).find_all('li')
        for x in lst:
            file.write(str(x.find('a',href = True)['href'])+'\n')
    except:
        pass

def FakingNews(keyword):
    keyword=keyword.replace(' ','%20').lower()
    url_ini = "http://www.fakingnews.com/?s="
    html=urlopen(f"http://www.fakingnews.com/?s={keyword}")
    bs= BeautifulSoup(html,'html.parser')
    lst = bs.find('div',{'class':'tab-pane fade in active'}).find_all('li')
    for x in lst:
        try:
            file.write(str(x.find('a',href=True)['href'])+'\n')
        except:
             pass

def LiveMint(keyword):
    keyword=keyword.replace(' ','%20').lower()
    url_ini="https://www.livemint.com/Search/Link/Keyword/"
    html=urlopen(f"https://www.livemint.com/Search/Link/Keyword/{keyword}")
    bs= BeautifulSoup(html,'html.parser')
    lst = bs.find('div',{'class':'mySearchView'}).find_all('div',{'class':'listing clearfix'})
    for x in lst:
        try:
            file.write(url_ini+str(x.find('a',href=True)['href'])+'\n')
        except:
             pass

def AsianAge(keyword):
    keyword=keyword.replace(' ','%20').lower()
    url_ini="http://www.asianage.com/search?page=search&srh=news&search="
    html=urlopen(f"http://www.asianage.com/search?page=search&srh=news&search={keyword}")
    bs= BeautifulSoup(html,'html.parser')
    lst = bs.find('div',{'class':'col-sm-12 col-xs-12 single_left_coloum_wrapper india-news noPadding'}).find_all('div',{'class':'singlesunday'})
    for x in lst:
        try:
            file.write(url_ini+str(x.find('a',href=True)['href'])+'\n')
        except:
             pass

def BBCUrl(keyword):
    keyword=keyword.replace(' ','+').lower()
    html=urlopen(f"https://www.bbc.co.uk/search?q={keyword}") 
    bs = BeautifulSoup(html,'html.parser')
    lst = bs.find('ol',{'class':"search-results results"}).find_all('li')
    for x in lst:
        try:
            file.write(str(x.find('a')['href'])+'\n')
        except:
            pass
    
def errorFilter(lst,n,count):
    n = 0
    cate_var = cat_variable.get()
    #webbrowser.open("output.html")
    try:
        for i in range(n,10):
            n = i
            windowResult.update()
            article = NewsPlease.from_url(lst[i])
            if article.title not in title:
                if cate_var == 'Select a Category':
                    windowResult.update()
                    html_out = f'''<html>
                                    <p><a href = {article.url}>{article.title}</a>&#13;&#10;</p>
                                    <p>Time:{article.date_publish}</a>&#13;&#10;</p>
                                    <p>{article.text}</a>&#13;&#10;</p>

                                </html>'''
                    html_file.write(html_out)
                    title.add(article.title)
                elif (cate_var!='Select a Category') and (cate_var in article.title):
                        windowResult.update()
                        html_out = f'''<html>
                                        <p><a href = {article.url}>{article.title}</a>&#13;&#10;</p>
                                        <p>Time:{article.date_publish}</a>&#13;&#10;</p>
                                        <p>{article.text}</a>&#13;&#10;</p>

                                    </html>'''
                        html_file.write(html_out)
                        title.add(article.title)

        windowResult.destroy()
    except:
        del lst[n]
        return n,count

def main(keyword):
    #keyword = str(input("Enter keyword to search: "))
    global file
    global html_file
    html_file = open("output.html",'w')
    count = 0
    global title
    title = set()
    n = 0
    file = open('output.txt','w+')
    #Aajtak(keyword)
    IndiaToday(keyword)
    #th1 = threading.Thread(target = IndiaToday,args = (keyword,))
    ##urlOneIndia(keyword)
    th2 = threading.Thread(target = urlOneIndia,args = (keyword,))
    ##Khashkhabar(keyword)
    #th3 = threading.Thread(target = Khashkhabar,args = (keyword,))
    #urlTheIndExp(keyword)
    ##LiveMint(keyword)
    th4 = threading.Thread(target = LiveMint,args = (keyword,))
    ##FakingNews(keyword)
    th5 = threading.Thread(target = FakingNews,args = (keyword,))
    ##AsianAge(keyword)
    #th6 = threading.Thread(target = AsianAge,args = (keyword,))
    ##urlTOI(keyword)
    th7 = threading.Thread(target = urlTOI,args = (keyword,))
    th8 = threading.Thread(target = BBCUrl, args = (keyword,))
    #th1.start()
    th2.start()
    #th3.start()
    th4.start()
    th5.start()
    #th6.start()
    th7.start()
    th8.start()
    #th1.join()
    th2.join()
    #th3.join()
    th4.join()
    th5.join()
    #th6.join()
    th7.join()
    th8.join()
    file.close()
    file = open('output.txt','r')
    lst = file.readlines()
    resultBox.insert(END,f"Total {len(lst)} results generating for {keyword}.\nPlease Wait!")
    resultBox.itemconfig(END, fg = "#00FF44",bg="black")
    resultBox.insert(END,'\n')
    random.shuffle(lst)
    try:
        n,count = errorFilter(lst,0,count)
        while n<len(lst):
                n = errorFilter(lst,n+1,count)
    except:
        pass
    html_file.close()
def main_Popularity(keyword):
    #keyword = str(input("Enter keyword to search: "))
    global file
    count = 0
    global html_file
    html_file = open("output.html",'w')
    global title
    title = set()
    n = 0
    file = open('output.txt','w+')
    #Aajtak(keyword)
    BBCUrl(keyword)
    IndiaToday(keyword)
    urlTOI(keyword)
    urlOneIndia(keyword)
    LiveMint(keyword)
    #AsianAge(keyword)
    FakingNews(keyword)
    Khashkhabar(keyword)
    file.close()
    file = open('output.txt','r')
    lst = file.readlines()
    resultBox.insert(END,f"Total {len(lst)} results generating for {keyword}.\nPlease Wait!")
    resultBox.itemconfig(END, fg = "#00FF44",bg="black")
    resultBox.insert(END,'\n')
    
    #random.shuffle(lst)
    try:
        n,count = errorFilter(lst,0,count)
        while n<len(lst):
                n = errorFilter(lst,n+1,count)
    except:
        pass   
    html_file.close()



#*************************************************************GUI******************************************************

def location():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)
    region = data['region']
    return region

def search(keyword):
    window.destroy()
    windowResult.geometry("1100x600")
    windowResult.title("SEARCH RESULT")
    windowResult.configure(bg="white")
    if popu_var.get()==1:
        if loc_var.get()==1:
            region = location()
            keyword = keyword + ' ' + region
            main_Popularity(keyword)
        else:
            main_Popularity(keyword)
    else:
        if loc_var.get()==1:
            region = location()
            keyword = keyword + ' ' + region
            main(keyword)
        else:
            main(keyword)
    #main(keyword)
    window.mainloop()
    

def textsearch():
    search(searchKeyword.get())

def voiceSearch():

    mic = speech_recognition.Microphone()
    R = speech_recognition.Recognizer()
    #messagebox.showinfo("Title", "Speak Keyword")
    try:
        with mic as source:
            R.adjust_for_ambient_noise(source)
            audio = R.listen(source)
        keyword = (R.recognize_google(audio, language='en-GB'))
        if loc_var.get()==1:
            region = location()
            keyword = keyword + ' ' + region
            search(keyword)  
        else:
            search(keyword)
    except:
        return "Please try again!"
    
url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)
region = data['region']


window = Tk()
window.geometry("1100x600")
window.title("dAtA cRaWlEr")
window.resizable(0,0)

mainLabel = Label(window, text="WELCOME TO DATA CRAWLER", fg="#00FF44",bg="black",relief=RAISED,font=("Scary",16,"bold"))
mainLabel.pack(fill = BOTH, padx = 2, pady = 2)

topFrame = Frame(window)
topFrame.pack(expand = True, fill = BOTH)
topFrame.configure(background = "#EFF0F1")
logo = Image.open("spider2.png")
image = logo.resize((250, 250), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
lab = Label(topFrame, image=photo)
lab.place(x=425,y=10)

searchKeyword = StringVar()
bottomFrame = Frame(window)
bottomFrame.pack(side = BOTTOM, expand = True, fill = BOTH)
searchEntry = Entry(bottomFrame, width = 35, font=10, textvariable = searchKeyword, bg = "#b3ffff", bd = 5)
searchEntry.place(x = 400, y = 30)
searchLabel = Label(bottomFrame, text = "Enter Keyword", font=("arial",13,"bold"))
searchLabel.place(x = 270,y = 27)
searchButton = Button(bottomFrame,text="Search",bg="#00FF44",relief=GROOVE,font=("Scary",13,"bold"), command = textsearch)
searchButton.place(x = 740,y = 25)

#Voice Search
voice_image = PhotoImage(file = "microphone.png")
voice_button = Button(bottomFrame, image = voice_image, width = 30, height = 30, relief=GROOVE, command = voiceSearch)
voice_button.place(x = 830, y = 23)

loc_var = IntVar()
loc_checkBox = Checkbutton(bottomFrame, text = "Search in my Location", variable = loc_var)
loc_checkBox.place(x = 500, y = 65)

popu_var = IntVar()
popu_checkBox = Checkbutton(bottomFrame, text = "Sort by Popularity", variable = popu_var)
popu_checkBox.place(x = 500, y = 100)

global cat_variable
cat_variable = StringVar(window)
cat_variable.set("Select a Category") # default value

dropDMenu = OptionMenu(bottomFrame, cat_variable, "Accident", "Robbery", "Rape", "Murder")
dropDMenu.place(x = 500,y = 140)

#Result Window

#windowResult = Tk()

fot = f.Font(size=3,family="cursive",slant="italic")

windowResult = Tk()

lower_frame = Frame(windowResult, bg="#80c1ff",bd=8)
lower_frame.place(x=10,y=10,height=580,width=1080)

#lower_frame = Frame(window2,bg="#80c1ff",bd=5)
#lower_frame.place(x=10,y=10,width=1890,height=1050)

resultBox = Listbox(lower_frame,font=fot,bg="#bf8040")
resultBox.pack(fill=BOTH,expand=True)

locationLabel = Label(bottomFrame, text = f"Your current location: {data['city']}, {data['region']}, {data['country']}", font=("Scary",11,"bold"), fg = "blue")
locationLabel.place(x = 350, y = 200)

time1 = ''
clock = Label(bottomFrame, font=('times', 20, 'bold'), bg='#EFF0F1', fg = 'blue')
clock.place(x = 485,y = 225)
def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(100, tick)
tick()


window.mainloop()

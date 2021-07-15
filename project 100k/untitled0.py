import tkinter as tk
from tkinter import*
from PIL import Image,ImageTk
from urllib.request import urlopen
from bs4 import BeautifulSoup
import random

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
    
def TeluguG(keyword):
    keyword = keyword.replace(' ','+').lower()
    html = urlopen(f"http://www.teluguglobal.in/?s={keyword}")
    bs = BeautifulSoup(html, 'html.parser')
    try:
        lst = bs.find('div',{'class':'td-ss-main-content'}).find_all('h3',{'class':'entry-title td-module-title'})
        for x in lst:
            file.write(str(x.a['href'])+'\n')
    except:
        pass

def TeluguGProp(url):
    prop = dict()
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.h1.get_text()
    img_src = bs.find('div',{'class':'td-post-content'}).a['href']
    text = bs.p.get_text()
    date = None
    prop = {"url":url,"title":title,"text":text,"img_src":img_src,"date":date}
    return prop

def DCProp(url):
    prop = dict()
    html = urlopen(url)
    bs = BeautifulSoup(html,'html.parser')
    title = bs.find('h1',{'class':'headline'}).get_text().strip()
    text = bs.find('div',{'class':'strap'}).get_text().strip()
    img_src = bs.find('div',{'class':'cover'}).find('img')['src']
    date = bs.find('div',{'class':'col-sm-6 col-xs-12 noPadding noMargin'}).get_text().strip()
    prop = {"url":url,"title":title,"text":text,"img_src":img_src,"date":date}
    return prop

def TIEProp(url):
    prop = dict()
    html = urlopen(url)
    bs = BeautifulSoup(html,'html.parser')
    title = bs.find('h1',{'itemprop':'headline'}).get_text()
    text = bs.find('h2',{'itemprop':'description'}).get_text().strip()
    img_src = bs.find('span',{'class':'custom-caption'}).find('img')['src']
    date = bs.find('meta',{'itemprop':'datePublished'})['content']
    prop = {"url":url,"title":title,"text":text,"img_src":img_src,"date":date}
    return prop

def TOIProp(url):
    prop = dict()
    html = urlopen(url)
    bs = BeautifulSoup(html,'html.parser')
    title = bs.find('title').get_text().strip()
    text = bs.find('head').find('meta',{'name':'description'})['content']
    img_src = bs.find('head').find('meta',{'property':'og:image'})['content']
    date = "None"#bs.find('div',{'class':'col-sm-6 col-xs-12 noPadding noMargin'}).get_text().strip()
    prop = {"url":url,"title":title,"text":text,"img_src":img_src,"date":date}
    return prop

def AajTakProp(url):
    prop = dict()
    html = urlopen(url)
    bs = BeautifulSoup(html,'html.parser')
    title = bs.find('h1',{'class':'secArticleTitle'}).get_text().strip()
    text = bs.find('div',{'class':'detailTxtContainer storyBody middle_s'}).get_text().strip()
    img_src = bs.find('div',{'class':'tabData'}).find('img')['src']
    date = bs.find('div',{'class':'editorRightPart'}).find('p').get_text()
    prop = {"url":url,"title":title,"text":text,"img_src":img_src,"date":date}
    return prop

def urlOneIndiaProp(url):
    html = urlopen(url)
    bs = BeautifulSoup(html,'html.parser')
    title = bs.find('div',{'class':'oi-article-lt'}).h1.get_text()
    date = bs.find('div',{'class':'oi-article-lt'}).time.get_text().replace('Published: ','').replace('Updated: ','').strip()
    text = bs.find('div',{'class':'oi-article-lt'}).p.get_text()
    img_src = bs.find('div',{'class':'big_center_img'})['data-gal-src']
    prop = {"url":url,"title":title,"text":text,"img_src":img_src,"date":date}
    return prop

def IndiaTodayProp(url):
    prop = dict()
    html = urlopen(url)
    bs = BeautifulSoup(html,'html.parser')
    title = bs.find('div',{'class':'node node-story view-mode-full'}).find('h1',{'itemprop':'headline'}).get_text().strip()
    text = bs.find('div',{'class':'story-kicker'}).find('h2').get_text()
    img_src = bs.find('div',{'class':'stryimg'}).find('img')['src']
    date = bs.find('dt',{'class':'pubdata'}).get_text()
    prop = {"url":url,"title":title,"text":text,"img_src":img_src,"date":date}
    return prop

def webIdentify(url):
    dic = dict()
    if 'deccanchronicle' in url:
        dic =  DCProp(url)
        return dic
    elif 'timesofindia' in url:
        dic = TOIProp(url)
    
    elif 'indianexpress' in url:
        dic =  TIEProp(url)
        return dic

    elif 'aajtak' in url:
        dic =  AajTakProp(url)
        return dic
    elif 'oneindia' in url:
        dic =  urlOneIndiaProp(url)
        return dic
    elif 'indiatoday' in url:
        dic =  IndiaTodayProp(url)
        return dic
    elif 'teluguglobal' in url:
        dic = TeluguGProp(url)
        return dic
    else:
        return None
    
def errorFilter(lst,n,count):
    n = 0
    try:
        for i in range(n,len(lst)):
            n = i
            article = webIdentify(lst[i])
            if article==None:
                print(f"Match not found for {lst[i]}")
            if article['title'] not in title:
                count += 1
                resultBox.insert(END,f"Count: {count}")
                resultBox.insert(END,f"URL: {article['url']}")
                resultBox.insert(END,f"Title: {article['title']}")
                resultBox.insert(END,f"Time: {article['date']}")
                resultBox.insert(END,f"Image Source: {article['img_src']}"+'\n')
                title.add(article['title'])
    except:
        del lst[n]
       # pdb.set_trace()
        return n,count
                      
def main(keyword):
    #keyword = str(input("Enter keyword to search: "))
    global file
    count = 0
    global title
    title = set()
    n = 0
    file = open('output.txt','w+')
    #Aajtak(keyword)
    #IndiaToday(keyword)
    urlOneIndia(keyword)
    TeluguG(keyword)
    #Khashkhabar(keyword)
    urlTheIndExp(keyword)
    #urlTOI(keyword)
    file.close()
    file = open('output.txt','r')
    lst = file.readlines()
    #print(f"Total {len(lst)} results found for {keyword}")
    random.shuffle(lst)
    try:
        n,count = errorFilter(lst,0,count)
        while n<len(lst):
                n = errorFilter(lst,n+1,count)
    except:
        pass  

HEIGHT = 500
WIDTH = 600

root = tk.Tk()
canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

def result():
    resultBox.delete(0,END)
img=Image.open("rt.jpg")
photo=ImageTk.PhotoImage(img)
lab=tk.Label(image=photo)
lab.place(relheight=1,relwidth=1)

frame = tk.Frame(root,bg='#80c1ff',bd=5)
frame.place(relx=0.5,rely=0.1,relheight=0.1,relwidth=0.75,anchor='n')

button =  tk.Button(frame, text="Search",command=result)
button.place(relx=0.7,relwidth=0.3,relheight=1)

entry = tk.Entry(frame,font=40)
entry.place(relwidth=0.65,relheight=1)

lower_frame = tk.Frame(root,bg="#80c1ff",bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

resultBox = tk.Listbox(lower_frame)
resultBox.pack(fill=BOTH,expand=True)
resultBox.insert(END,"hello")


root.mainloop()
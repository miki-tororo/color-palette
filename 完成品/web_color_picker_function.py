
#requestとBeautifulSoupのインポート➡URL抽出のため
import requests
from bs4 import BeautifulSoup


#reをインポート➡正規表現パターンによる文字列の抽出や置換、分割などができる。
import re


#動作のメソッド化
def color_pick(url): 
  


    
    #URLからhtmlデータを抽出する
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    #print (soup)


    #soupから、linkと記載のある行を抜き出して、linkに代入。
    url = soup.find_all('link')

    
    #配列の作成
    col_c=[]
    cc=[]

    #後処理のために、「x」という変数に「.css」を代入
    x = ".css"

    #ccc=1

    #抽出結果を全て一行ずつ羅列する（print指示なし、実際に表示はされない）
    for e in url:     
        url_css=str(e)    
                                   
        #条件文：
        #抽出済みURLが「.css」を含む場合(一行ずつ確認)
        if x in url_css:

            text=url_css

            #パターンの意味：
            #href="で始まり、任意の一文字を0回以上繰り返し、.cssで終わるもの        
            pattern="href=\".*\.css"
            

            #reを使用し、パターンを含む文字列の抽出を行う
            #res　結果表示一例：['href="https://www.nagoyajo.city.nagoya.jp/css/global/import.css']
            res=re.findall(pattern, text)
            #print(res)
            
            
            #stripを使用し、不要な文字をresの結果から取り除く
            #意味➡resのインデックス0➡0文字目から「href=」を取り除いて、ｒへ代入
            r=res[0].strip("href=")

            #rのインデックス1から後ろ全てをｒに代入    
            r=r[1:]
            
            #r の結果表示一例：https://www.nagoyajo.city.nagoya.jp/css/global/import.css
            #print(r)


            """
            やりたいこと
            https://www.nagoyajo.city.nagoya.jp/css/global/import.css
            抽出済み.cssを含むURLにアクセスし、中に書かれている色情報のみを取得する。
            方法➡正規表現#後にa～fと数字の0～9が6個続くものを抽出する➡色番号
            """

            #抽出済み.cssを含むURLにアクセスし、中身を取得          
                
            url = r
            css_url = requests.get(url)

            iro = BeautifulSoup(css_url.text, 'lxml')

            #print(iro)

                   
            #取り出した.cssのURL情報を文字列型に変換
        
            col=str(iro)
           

            """
            正規表現を使い
            「#」の後にa～fと数字の0～9が6個続くものを抽出する➡抽出結果：色番号
            """

            pattern1='\#[a-fA-F0-9_]{6}'
                
            c=re.findall(pattern1, col)

            #print(c)


            #複数配列を一つの配列にまとめる

            for item in c:
                col_c.append(item)                   
                
                
                #print(col_c)
                
         
    return col_c



    





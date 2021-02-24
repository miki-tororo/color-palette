#.cssを含むURLから色情報のみを抜き出しすメソッドの実行

import web_color_picker_function as color


#メソッド実行結果の出力
#メソッドは戻り値に置き換わる➡の引数は与えるもの、戻り値は、結果に置き換わるprintの結果
list1=color.color_pick("https://en-hyouban.com/company/10200093320/")
#list1=color.color_pick("https://www.nagoyajo.city.nagoya.jp/")

#メソッド実行結果のカラーナンバーを1つずつ改行表示
for i in list1:
        
        print(i)

        #aa=int("bb", 16)
        #print(aa)
        #print(2)

#抽出済み全カラーナンバーの重複を削除
#例：iterable=["apple", "apple", "pain", "bike", "bike", "it"]
#例：uniqued = set(iterable)
#例：print(uniqued)
list2=set(list1)

#重複削除後のカラーナンバーを表示
#print(list2)



list3=sorted(list2)


"""
以下、GUI作成コード
tkinterをインポートする➡GUIを作成するため
"""

import tkinter as tk


"""山田さん側で作成してくれる、選択済みカラーを受け取る関数
def addcolor(color):
        label=tk.Label(bg=color)
"""        

#選択済みの色番は配列に入っているので、1つずつ取り出し
#別ページに渡せるよう、決められた変数に代入しておく関数
def add_colorlist(slected_colors):

        for e in slected_colors:

                color = e
                
        



#選択済みフォント色表示ラベル

"""
selected2 = tkinter.Label(width=8, background="blue",relief="ridge")
selected2.place(x=285,y=68)               

selected3 = tkinter.Label(width=8, background="green",relief="ridge")
selected3.place(x=370,y=68)               
"""    

"""
def btn_click():

        i=1
        while i>5:
                btn(i)["text"]=""
                i += 1


def btn_click():
        btn1["text"]="〇"

"""

#ウィンドウの基礎を作る(ウィンドウのオブジェクトを生成）
root = tk.Tk()

v_size=round(len(list3)/11*100)

print(v_size)


x=500
y=600

if(v_size < 500):

        #画面サイズ
        root.geometry(str(x) + 'x' + str(y))
        # 500x600
else:
           
        #画面サイズ
        root.geometry(str(v_size)+'x600')
              

#画面背景色
#root.configure(bg='oldlace')
root.configure(bg='oldlace')

#画面タイトル
root.title('Web_color _picker')


#ラベルは「tkinter.Label」で作成します。ラベルに表示する文字列は「text」で指定します。
#ラベルを表示する座標は「place」でX座標、Y座標を指定します。

#root>tkinter.Lableという階層 ラベル部品を生成
lbl_a = tk.Label(text='使用したい色を選択してください。（□をクリック）',font=('Meiryo',13,'bold'),bg='oldlace')
#配置を決めている
lbl_a.place(x=40, y=8)

# 選択済みフォント見出し
lbl_b = tk.Label(text='Selected_Colors:',font=('Times',15),bg='oldlace')
lbl_b.place(x=45, y=50)

# フォント選択メッセージ
lbl_c = tk.Button(text='Color送信ボタン',font=('Meiryo',11,'bold'),bg='#FFB6C1')
#lbl_c = tk.Button(text='Color送信ボタン',font=('Meiryo',11,'bold'),bg='#ffb8b8')
lbl_c.place(x=45, y=90)


#抽出済み色情報を入れた配列の要素数をカウント
print(len(list3))


checklist=[]

#選択済みの色を入れる配列を作成
slected_colors=[]

def check_clicked():

        #すべての要素を削除: clear()
        slected_colors.clear()
        
        
        #今何周目かのカウント
        cnt=0
  

        """
        色番号のチェックボックスにチェックが入っているものを探す
        入っていたら、selectedのところにラベルを作って、その色番号を取得し入れる
        で、それを最後まで繰り返す。
        """
        xx=200
        yy=52

        
        for e in bln_list:
                #print(e.get())
                #print(7)
                
                
                if e.get():
                #if check["variable"].get():
                        num=checklist[cnt]["bg"]
                        print(num)
                        
                        slected_color = tk.Label(width=3, background=num,relief="ridge")
                        slected_color.place(x=xx,y=yy)

                        
                        slected_colors.append(num)

                        xx += 40

                cnt+=1

                                
        print(slected_colors)
        
                        
#要素数を変数として設定
n=0
#print(n)

#x軸の配置に関する変数設定
yy=0
xx=0


#今何周目かのカウント
counter=0


xs=20
xl=75

ys=148
yl=150

bln_list=[]

                       

for i in list3:
        
        
        k=str(i)                    
                

        #フォント選択ボタン
        #btn = tkinter.Button(width=2,relief="ridge",command=btn_click)
        #btn.place(x=xs+xx,y=ys+yy)              

              
        #色塗りつぶしラベル
        #iro = tkinter.Label(width=4,background=k,relief="ridge")
        #iro.place(x=xl+xx,y=yl+yy)

        
        bln_var=tk.BooleanVar()
        bln_list.append(bln_var)


        #チェックリスト
        check= tk.BooleanVar(value = True)
        
        #check=tk.Checkbutton(root,width=6,background=k,relief="ridge", variable=bln_list[counter],command=check_clicked)
        #check=tk.Checkbutton(root,width=6,background=k,relief="ridge", command=check_clicked)
        check=tk.Checkbutton(root,width=6,background=k,relief="ridge", variable=bln_var,command=check_clicked)
        check.place(x=xs+xx,y=ys+yy)
        checklist.append(check)

        

        o=bln_var.get()
        print(o)
        print(44)

        #print(bln_list[counter].get())
        #print(checklist)
        

        n+=1
        yy+=40

        counter+=1
        

        print(n)


        if counter%11==0:                 

                yy=0
                xx+=90






                

        
        





              


#イロナンバー非表示➡選んだ3つとかだけ表示させる➡〇を付けたものを➡送信？
#画面サイズに合わせて表示➡表示が縮む
#ダサい
#他の画面との連携はどうやってやる➡色をドラッグ＆ドロップして他のページへとか
#色のソート➡カーラーソート/アルゴリズム
#メソッド化➡メソッドの中身もメソッド化➡def






#色かぶりを消す➡一つ目のボックスラインに入っている色を基準に➡同じ色は追加しない
#ボタンのリストを作る
#whileなどで処理を囲む


root.mainloop()

#チェックされている色をリスト化➡それを基に動的にラベルを作る
#リストから



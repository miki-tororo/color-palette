import tkinter as tk

ColorHolder = tk.Tk()
ColorHolder.title("Color_holder")
ColorHolder.geometry("1000x750")

a=100                           #位置の変数a、bと初期値
b=50

var=tk.IntVar()                 #ラジオボタンのチェックの有無の変数var
var.set(0)                      #ラジオボタンのチェックの初期値　valure=0(一つ目)に設定

color="#ffffff"                 #色指定の変数
colorList = []

radioList=[]
entryList=[]
labelList=[]
delList=[]
varList=[]







#画面遷移ボタン(Sellection)の処理
def transition_button1(home):
    test=tk.Toplevel()
    
    
#画面遷移ボタン(Web)の処理
def transition_button2(home):
    test=tk.Toplevel()

       




#削除ボタンの処理
def DelBtn_click():
    
    radioList[num].destroy()  #delボタンが押されたところのnumのradioボタンを消す
    entryList[num].destroy()  #delボタンが押されたところの配列のindexを取得したい
    labelList[num].destroy()
    delList[num].destroy()
    
    radioList.pop()     #pop() 配列の要素を一つ消すメソッド
    entryList.pop()     #配列の数を減らすと、AddCollor()でradioList[num]が範囲外となる。
    labelList.pop()
    delList.pop()

    #num -=1             #numもマイナス1する
                        #すでに設置済のカラーホルダーをなくなったところに移動させる必要がある。
                        #AddCollorをしても、すでに設置済みのものにかぶってしまうから。
                     
    print(len(radioList))
    print(num)





#エンターキーを押したときに実行する処理
#       処理①ラベル3個の色をEntに入力されたカラーコードに変更する。
#       処理②プレビュー画面２つの色をEntに入力されたカラーコードに変更する。
#       処理③例外処理

#変数i:エンターキーが押されたエントリーボックスのインデックス番号

def colorChangeNum(event):
    num=0
    try:
        labelList[num].config(bg= entryList[num].get())
        
        canvas1.configure(id0,fg = entryList[num].get())
        #canvas2.configure(id0,fg = entryList[num].get())
        
    except tk.TclError:
        error=0


  



#カラー1色を追加するメソッド
def AddColor(color):         #カラーホルダーの生成（①ラジオボタン、②エントリーボックス、③ラベル）
    print(1)
    
    #ラジオボタンをつくる
    radio =tk.Radiobutton(ColorHolder, variable=var)
    radioList.append(radio)
    #変数numの設定：ラジオボタンの長さ = インデックス番号
    print(len(radioList))
    num=len(radioList)-1

    
       
    #エントリーボックス
    entry = tk.Entry(ColorHolder,width = 13,background = '#ffffff',foreground = '#000000')
    entryList.append(entry)
    entry.insert(0,color)  
    
    
    #ラベルをつくる
    label=tk.Label(ColorHolder,width = 4,height = 2,relief = "groove",background =color)
    labelList.append(label)

    #削除ボタンをつくる
    delBtn = tk.Button(ColorHolder, text="Delet", command=DelBtn_click)
    delList.append(delBtn)
  
    #各位置設定　(ラジオ、エントリー、ラベル、削除ボタン)
    
    radioList[num].place(x=a,y=b*(num+1))
    entryList[num].place(x=a*1.8, y=b*(num+1))
    entryList[num].bind("<Return>",colorChangeNum)
    labelList[num].place(x=a*2.8, y=b*(num+1))
    delList[num].place(x=a*3.3, y=b*(num+1))

    
    """  
    #色を登録する
    colorList.append()
    """
def CreateHoler():
    AddColor("#ffffff")





    




"""
#☆②イベントの処理の設定
#    エンターキーが押されたときにラベルの色を変更

#入力されたエントリーボックスのインデックス「i」を探す
i=0 #仮に設定　event？.entryで設定する

for index in range (num):
    if entryList[i].get() != entryList[index].get():
        print(index)
        i=index
        print(entryList[i].get())
        entryList[i].bind("<Return>",colorChange)
        print("ラベルの色変更")

    else:
        print(index)
        print(entryList[index].get())
        print("変更なし")
"""


    

#削除ボタンの処理
def DelBtn_click():
    
    radioList[num].destroy()  #delボタンが押されたところのnumのradioボタンを消す
    entryList[num].destroy()  #delボタンが押されたところの配列のindexを取得したい
    labelList[num].destroy()
    delList[num].destroy()
    
    radioList.pop()     #pop() 配列の要素を一つ消すメソッド
    entryList.pop()     #配列の数を減らすと、AddCollor()でradioList[num]が範囲外となる。
    labelList.pop()
    delList.pop()

    #num -=1             #numもマイナス1する
                        #すでに設置済のカラーホルダーをなくなったところに移動させる必要がある。
                        #AddCollorをしても、すでに設置済みのものにかぶってしまうから。
                    
    
    print(len(radioList))
    print(num)








#プレビュー画面を載せるためのキャンバス画面(#canvas1の設定)
canvas1=tk.Canvas(width=500,height=300,bg="#000")          
canvas1.place(x=a*4.5, y=1.2*b)



#ホーム画面のボタン
selectionBtn = tk.Button(ColorHolder, text="Selection Color",
                       command=lambda:transition_button1(canvas1))  #セレクション画面に遷移するボタン           
selectionBtn.place(x=a*4.5, y=0.2*b)


webBtn = tk.Button(ColorHolder, text="Web Color Picker",
                       command=lambda:transition_button2(canvas1))  #Web画面に遷移するボタン
webBtn.place(x=a*5.5, y=0.2*b)

WebEntry = tk.Entry(width = 35)                                     #URL入力エントリーボックス
WebEntry.insert(0,"http://www.shido.info/py/tkinter2.html")         #エントリーボックスの初期値設定
WebEntry.place(x=a*5.5, y=0.8*b)


#カラーを追加するボタンの設定
addBtn = tk.Button(ColorHolder, text="Add Color", command=CreateHoler)           
addBtn.place(x=a*3.5, y=b*0.2)


#プレビュー画面(ホーム画面canvas1に追加する)
id1=canvas1.create_rectangle(0,0,250,300, fill="#ffffff")
id2=canvas1.create_rectangle(250,0,500,300, fill="#ffffff")
id0=canvas1.create_text(100,50,text="Sample", fill= "red",
                     font=("MSゴシック", "40", "bold"))


#canvas1.itemconfigure(id0,fill = "orange")
#canvas1.itemconfigure(id1,fill = "red")

    
ColorHolder.mainloop()

 

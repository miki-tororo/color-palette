import pyautogui as ag
import pyperclip

import tkinter as tk
import tkinter.font as font

#GUI左上のアイコンの変更
iconfile = 'iro.ico'

ColorHolder = tk.Tk()
ColorHolder.title("Color_holder")
ColorHolder.geometry("1000x750")
ColorHolder.iconbitmap(default=iconfile)

x0=10
y0=0
a=100                           #位置の変数a、bと初期値
b=70


color="#ffffff"                 #色指定の変数


entryList=[]
labelList=[]
delList=[]

#font
my_font = font.Font(family="游ゴシック",size=10,weight="bold")

#微調整実行関数
def adjustColor():
    global switch, cc, r, g, b
    code = Color(txt1.get())        #自作のクラスColorのインスタンスを生成
    cc = code.adjustColor(r, g, b)  #Colorクラスのメソッドを使用
    changeColor()
    #トリガー変数switch==1の間0.05秒ごとにadjustColor()を再読み込み
    if switch == 1:
        root.after(50, adjustColor)


#コピー＆ペースト関数
def release_action(event):
    pyperclip.copy(event.widget["bg"])
    click_paste()

def click_paste():
        
    #マウスをドロップした場所のポジションを取得
    x, y = ag.position()
    #マウスをドロップした場所をクリックさせる
    ag.click(x, y, clicks=1)
    #テキストボックス内の全消去(コード入力時に使用する場合は要コメントアウト)
    ag.hotkey("ctrl", "a", "del")
    #カラーコードのペースト
    ag.hotkey("ctrl", "v")

#画面遷移ボタン(Sellection)の処理
def transition_button1(home):
    #####
    ###for ColorSelection
    #####
    import functools
    from ColorClass import Color   #自作クラスのインポート


    def submit():
        print(txt1.get())
        AddColor(txt1.get())

    #カラーコード読み取り・反映関数
    def colorGet():
        try:
            window.config(bg=txt1.get())
        except Exception as error:
            error = 0
        finally:
            after = ColorHolder.after(1000, colorGet)  #1秒後にcolorGet()を再読み込み
            

    #カラー表示ラベル変更関数(カラーコードも変更)
    def changeColor():
        global cc
        txt1.delete(0, tk.END)
        txt1.insert(tk.END, cc)
        try:
            window.config(bg=cc)
        except tk.TclError:
            error = 0


    #ベースカラー読込み関数
    def setColor(event, param):
        global cc
        cc = param
        changeColor()


    #微調整トリガー関数
    def setTrigger(event, params, paramr, paramg, paramb):
        global switch, r, g, b
        switch = params
        r = paramr
        g = paramg
        b = paramb
        adjustColor()



    #カラーコード格納用変数
    cc = '#ffffff'            #初期値は白

    #微調整関数ON/OFFトリガー変数
    switch = 0                #関数持続トリガー
    r = 0                     #赤変更トリガー
    g = 0                     #緑変更トリガー
    b = 0                     #青変更トリガー

    #サイズ及び位置用変数
    fw0 = 200                 #column=0のwidth変数
    fw1 = 500                 #column=1のwidth変数
    fw2 = 800 - (fw0 + fw1)   #column=2のwidth変数(rootサイズ変更時数値部分変更する)
    fh0 = 70                  #row=0,1,2,4のheight変数
    fh1 = 270                 #row=3のheight変数
    #ラベルのheight値はフレームのheight値の14倍?
    #ラベルのwidth値はフレームのwidth値の7倍?

    bh = 2  #ベースカラーのheight変数

    ww = 50                   #カラー表示用ラベルのwidth変数
    wh = 17                   #カラー表示用ラベルのheight変数
    wx = (fw1 - ww * 7) / 2   #カラー表示用、赤、白ラベルの位置座標変数(x軸)
    wy = 10                   #カラー表示用、赤、緑、青ラベルの位置座標変数(y軸)

    tx = (fw1 / 2) - (bh * 15)   #カラーコード表示ボックスの位置座標変数(x軸)
    ty = 20                      #カラーコード表示ボックスの位置座標変数(y軸)
    btx = (fw1 / 2) + (bh * 30)  #カラーコード送信ボタンの位置座標変数(x軸)
    bty = 15                     #カラーコード送信ボタンの位置座標変数(y軸)

    cx = (fw1 / 2) - (bh * 7)     #緑ラベルの位置座標変数(x軸)
    ex = (wx + ww * 7) - (bh * 14)  #青、黒ラベルの位置座標変数(x軸)
    sh = (wy + wh * 14) - (bh * 7)  #白、黒ラベルの位置座標変数(y軸)
    
    
    root = tk.Toplevel(ColorHolder)
    root.geometry('1000x600')
    root.title('Color_selection')

    #フレーム作成
    base0_0 = tk.Frame(root, width=fw0, height=fh0)
    base0_1 = tk.Frame(root, width=fw0, height=fh0)
    base0_2 = tk.Frame(root, width=fw0, height=fh0)
    base0_3 = tk.Frame(root, width=fw0, height=fh1)
    base1_1 = tk.Frame(root, width=fw1, height=fh0, bd=1, relief="ridge", bg="#cccccc")
    base1_3 = tk.Frame(root, width=fw1, height=fh1)
    base1_4 = tk.Frame(root, width=fw1, height=fh0)
    base1_5 = tk.Frame(root, width=fw1, height=fh0)
    base2_4 = tk.Frame(root, width=fw2, height=fh0)


    #フレーム配置
    base0_0.grid(column=0, row=0)
    base0_1.grid(column=0, row=1)
    base0_2.grid(column=0, row=2)
    base0_3.grid(column=0, row=3)
    base1_1.grid(column=1, row=1)
    base1_3.grid(column=1, row=3)
    base1_4.grid(column=1, row=4)
    base1_5.grid(column=1, row=5)
    base2_4.grid(column=2, row=4)


    #カラー表示用ラベル
    window = tk.Label(base1_3, width=ww, height=wh, bd=1, relief="ridge", bg=cc)
    window.place(x=wx, y=wy)
    window.bind("<ButtonRelease>", release_action)


    #カラーコード表示ボックス
    txt1 = tk.Entry(base1_4, width=bh*5, bd=1, relief="ridge")
    txt1.insert(0, cc)
    txt1.place(x=tx, y=ty)


    #カラーコード送信ボタン(カラーホルダーへ)
    btn = tk.Button(base1_4, text="送信",command=submit)
    btn.place(x=btx, y=bty)


    #ここからベースカラー
    colors = ['#ffffff', '#000000', '#795548', '#ff0000',  #白、黒、茶、赤
              '#ff6f00', '#ffff00', '#76ff03', '#00ff00',  #橙、黄、黄緑、緑
              '#18ffff', '#0000ff', '#1a237e', '#6200ea']  #水色、青、紺、紫

    bclist = []  #各ラベルを格納するリスト
    bclp = 0     #for文用リスト位置変数

    for i in colors:
        bclist.append(tk.Label(base1_1, width=bh*2, height=bh, bd=1, relief="ridge", bg=i))
        bclist[bclp].pack(side=tk.LEFT, padx=5, pady=10)
        bclist[bclp].bind("<Double-ButtonPress-1>", functools.partial(setColor, param=i))
        bclp += 1
    #ここまでベースカラー


    #微調整用ラベル作成(赤、緑、青、白、黒)
    aka = tk.Label(base1_3, width=bh*2, height=bh, bd=1, relief="ridge", bg="#ff0000")
    midori = tk.Label(base1_3, width=bh*2, height=bh, bd=1, relief="ridge", bg="#00ff00")
    ao = tk.Label(base1_3, width=bh*2, height=bh, bd=1, relief="ridge", bg="#0000ff")
    siro = tk.Label(base1_3, width=bh*2, height=bh, bd=1, relief="ridge", bg="#ffffff")
    kuro = tk.Label(base1_3, width=bh*2, height=bh, bd=1, relief="ridge", bg="#000000")


    #微調整用ラベル配置
    aka.place(x=wx, y=wy)
    midori.place(x=cx, y=wy)
    ao.place(x=ex, y=wy)
    siro.place(x=wx, y=sh)
    kuro.place(x=ex, y=sh)


    #微調整機能実装
    aka.bind("<ButtonPress-1>", functools.partial(setTrigger, params=1, paramr=1, paramg=0, paramb=0))
    aka.bind("<ButtonPress-3>", functools.partial(setTrigger, params=1, paramr=-1, paramg=0, paramb=0))
    aka.bind("<ButtonRelease>", functools.partial(setTrigger, params=0, paramr=0, paramg=0, paramb=0))
    midori.bind("<ButtonPress-1>", functools.partial(setTrigger, params=1, paramr=0, paramg=1, paramb=0))
    midori.bind("<ButtonPress-3>", functools.partial(setTrigger, params=1, paramr=0, paramg=-1, paramb=0))
    midori.bind("<ButtonRelease>", functools.partial(setTrigger, params=0, paramr=0, paramg=0, paramb=0))
    ao.bind("<ButtonPress-1>", functools.partial(setTrigger, params=1, paramr=0, paramg=0, paramb=1))
    ao.bind("<ButtonPress-3>", functools.partial(setTrigger, params=1, paramr=0, paramg=0, paramb=-1))
    ao.bind("<ButtonRelease>", functools.partial(setTrigger, params=0, paramr=0, paramg=0, paramb=0))
    siro.bind("<ButtonPress-1>", functools.partial(setTrigger, params=1, paramr=1, paramg=1, paramb=1))
    siro.bind("<ButtonPress-3>", functools.partial(setTrigger, params=1, paramr=-1, paramg=-1, paramb=-1))
    siro.bind("<ButtonRelease>", functools.partial(setTrigger, params=0, paramr=0, paramg=0, paramb=0))
    kuro.bind("<ButtonPress-1>", functools.partial(setTrigger, params=1, paramr=-1, paramg=-1, paramb=-1))
    kuro.bind("<ButtonPress-3>", functools.partial(setTrigger, params=1, paramr=1, paramg=1, paramb=1))
    kuro.bind("<ButtonRelease>", functools.partial(setTrigger, params=0, paramr=0, paramg=0, paramb=0))

    print(txt1.get())

    #colorGet()関数起動
    colorGet()
    #####
    ###/for ColorSelection
    #####



         
#画面遷移ボタン(Web)の処理
def transition_button2(home):
    #####
    ###for ColorPicker
    #####
    import web_color_picker_function as color

        #メソッド実行結果の出力
    #メソッドは戻り値に置き換わる➡の引数は与えるもの、戻り値は、結果に置き換わるprintの結果
    list1=color.color_pick("https://en-hyouban.com/company/10200093320/")
    #list1=color.color_pick("https://www.nagoyajo.city.nagoya.jp/")
    
    #抽出済み全カラーナンバーの重複を削除
    list2=set(list1)
    list3=sorted(list2)

    """
    以下、GUI作成コード
    tkinterをインポートする➡GUIを作成するため
    """

    import tkinter as tk


    
        

    #選択済みの色番は配列に入っているので、1つずつ取り出し
    #別ページに渡せるよう、決められた変数に代入しておく関数
    def add_colorlist(slected_colors):
            for e in slected_colors:
                    color = e
    #add colors to ColorHolder
    def AddColors():
        for i in slected_colors:
            AddColor(i)

    #ウィンドウの基礎を作る(ウィンドウのオブジェクトを生成）
    root = tk.Toplevel()
    #左上アイコンの配置
    root.iconbitmap(default=iconfile)

    v_size=round(len(list3)/11*100)


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

    #root>tkinter.Lableという階層 ラベル部品を生成
    lbl_a = tk.Label(root,text='使用したい色を選択してください。（□をクリック）',font=('Meiryo',13,'bold'),bg='oldlace')
    #配置を決めている
    lbl_a.place(x=40, y=8)

    # 選択済みフォント見出し
    lbl_b = tk.Label(root,text='Selected_Colors:',font=('Times',15),bg='oldlace')
    lbl_b.place(x=45, y=50)

    # フォント選択メッセージ
    lbl_c = tk.Button(root,text='Color送信ボタン',font=('Meiryo',11,'bold'),bg='#FFB6C1',command=AddColors)
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
            """
            xx=200
            yy=52

            
            for e in bln_list:
                    #print(e.get())
                    #print(7)
                    
                    
                    if e.get():
                    #if check["variable"].get():
                            num=checklist[cnt]["bg"]
                            
                            slected_color = tk.Label(root,width=3, background=num,relief="ridge")
                            slected_color.place(x=xx,y=yy)

                            
                            slected_colors.append(num)

                            xx += 40

                    cnt+=1

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
            
            bln_var=tk.BooleanVar()
            bln_list.append(bln_var)


            #チェックリスト
            check= tk.BooleanVar(value = True)
            
            check=tk.Checkbutton(root,width=6,background=k,relief="ridge", variable=bln_var,command=check_clicked)
            check.place(x=xs+xx,y=ys+yy)
            checklist.append(check)

            

            o=bln_var.get()            

            n+=1
            yy+=40

            counter+=1
            
            if counter%11==0:                 

                    yy=0
                    xx+=90
    
    #####
    ###/for ColorPicker
    #####
       

#エンターキーを押したときに実行する処理
#       処理①ラベル3個の色をEntに入力されたカラーコードに変更する。
#       処理②プレビュー画面２つの色をEntに入力されたカラーコードに変更する。
#       処理③例外処理

#変数i:エンターキーが押されたエントリーボックスのインデックス番号

def colorChange(event):

    #event.widget=entryList[i]
    #print(i) 
    

    #エンターキーが押されたエントリーボックスを探す
    for i in range(len(labelList)):             
        if event.widget==entryList[i]:
            
            try:
                labelList[i].config(bg= entryList[i].get())
                #canvas1.configureitem(id0,fg = entryList[i].get())
        
                #canvas1.configure(id1,fg = entryList[i+1].get())
        
            except tk.TclError:
                error=0

#カラー1色を追加するメソッド
def AddColor(color):         #カラーホルダーの生成（①ラジオボタン、②エントリーボックス、③ラベル）

 
    #ラジオボタンをつくる
    #radio =tk.Radiobutton(ColorHolder,font=my_font, value=int(len(radioList)), variable=var)    
    #radioList.append(radio)
       
    #エントリーボックス
    entry = tk.Entry(ColorHolder,font=my_font,width = 13,background = '#ffffff',foreground = '#000000')
    entry.bind("<Return>",colorChange)
    entryList.append(entry)
    entry.insert(0,color)
 
    #ラベルをつくる
    label=tk.Label(ColorHolder,width = 4,height = 2,relief = "groove",background =color)
    label.bind("<ButtonRelease>",release_action)
    labelList.append(label)

    #削除ボタンをつくる
    delBtn = tk.Button(ColorHolder, text="Delete")
    delBtn.bind("<Button>", DelBtn_click)
    delList.append(delBtn)

    Update_create()
    
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
def DelBtn_click(event):

    #エンターキーが押されたDelボタンを探す
    #delボタンが押されたところの配列のindexを取得したい
    for i in range(len(delList)):             
        if event.widget==delList[i]:
            print(i)
    
            #del radioList[i]  #delボタンが押されたところのindexを消す
            del entryList[i]  
            del labelList[i]
            del delList[i]
            Update_create()
            break
    print(labelList)

def allDelete():
    print("aaa")
    i=len(labelList)
    for j in range(i):             
        del entryList[0]  
        del labelList[0]
        del delList[0]
    Update_create()
    print(labelList)

def Update_create():

    for i in range(len(labelList)):
          
        #各位置再設定　(ラジオ、エントリー、ラベル、削除ボタン)
        #radioList[i].place(x=x0,y=b*(i+1))
        labelList[i].place(x=x0, y=y0+b*(i))
        entryList[i].place(x=x0+0.7*a, y=y0+b*(i)+15)
        delList[i].place(x=x0+a*2.7, y=y0+b*(i))
        print(i)


#プレビュー画面を載せるためのキャンバス画面(#canvas1の設定)
canvas1=tk.Canvas(width=500,height=300,bg="#000")          
canvas1.place(x=a*4.5, y=1.2*b)

#AddCollor部分のウェジェットを


#ホーム画面のボタン
selectionBtn = tk.Button(ColorHolder, text="Selection Color",
                       command=lambda:transition_button1(canvas1))  #セレクション画面に遷移するボタン           
selectionBtn.place(x=a*4.5, y=6.5*b)


webBtn = tk.Button(ColorHolder, text="Web Color Picker",
                       command=lambda:transition_button2(canvas1))  #Web画面に遷移するボタン
webBtn.place(x=a*4.5, y=8*b)

WebEntry = tk.Entry(width = 35)                                     #URL入力エントリーボックス
WebEntry.insert(0,"http://www.shido.info/py/tkinter2.html")         #エントリーボックスの初期値設定
WebEntry.place(x=a*4.5, y=9*b)



#カラーを追加するボタンの設定
#addBtn = tk.Button(ColorHolder, text="Add Color", command=CreateHoler)           
addBtn = tk.Button(ColorHolder, text="Add Color", command=allDelete)           

addBtn.place(x=a*4.5, y=b*0.2)

#プレビュー画面(ホーム画面canvas1に追加する)
id0=canvas1.create_rectangle(0,0,250,300, fill="blue")
id1=canvas1.create_rectangle(250,0,500,300, fill="yellow")
id2=canvas1.create_text(250,150,text="Sample", fill= "red",
                     font=("MSゴシック", "40", "bold"))


#canvas1.itemconfigure(id0,fill = "orange")
#canvas1.itemconfigure(id1,fill = "red")


    
ColorHolder.mainloop()



 

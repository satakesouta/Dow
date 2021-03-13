#ダウ平均アプリ（mac用）
#ダウ平均の株価及びその情報を簡単にブラウザ（Chrome専用）検索できる
#write.txtにダウ平均関連の調べたい単語を保存できる
#ChromeアプリのUNIX実行ファイルのパス及びwrite.txt、write1.txtのパスを指定する必要あり
#アプリ化は任意で

import tkinter
from tkinter import ttk
import subprocess
from time import sleep


class NotebookSample(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.read()
        self.read1()
        self.note0(data)
        self.note1()
        self.note2()
        self.pack()

    def create_widgets(self):
        # ウィンドウタブのデザイン
        tabstyle = ttk.Style()
        tabstyle.configure(
            "example.TNotebook",
        )
        tabstyle.configure(
            "example.TNotebook.Tab",
            font=("游ゴシック",20,"bold"),
            foreground="blue"
        )
        tabstyle.map(
            "example.TNotebook.Tab",
            foreground=[
                ('active', 'black'),
                ('disabled', 'gray'),
                ('selected', 'blue'),
            ],

        )
        width = 290
        # タブの配置
        note = ttk.Notebook(self,width=290,style="example.TNotebook")
        global note0,note1,note2
        note0 = ttk.Frame(note,takefocus = 3)
        note1 = ttk.Frame(note,takefocus = 3)
        note2 = ttk.Frame(note,takefocus = 3)
        note.add(note0,text="株情報",padding=5)
        note.add(note1,text="株価",padding=5)
        note.add(note2,text="メモ",padding=5)
        note.pack(expand=1, fill='both',anchor='center')
        
    
    def read(self):
        # テキスト（write.txt）内のデータ読み取り
        f = open('write.txtのパスを記入', 'r', encoding='utf-8')
        global data
        data = f.readlines()
        f.close()
        data = list(map(lambda x:x.strip(), data))


    def write(self):
        # テキスト内にデータ上書き
        S = {}
        f = open('write.txtのパスを記入', 'w', encoding='utf-8')
        for i in range(len(EditBox)):
            if not EditBox[i].get() == '':
                S[i] = EditBox[i].get() + "\n"
                f.write(S[i])
        f.close()

    def search(self):
        # ブラウザ起動及び自動検索
        # グーグル
        V1 = "https://www.google.com/search?q="
        V2 = "&rlz=1C1EJFC_enJP888JP888&tbas=0&tbs=sbd:1&tbm=nws&sxsrf=ALeKk03vvQqjy4kpVZcCZuSKRyorbMwmKg:1613270790800&tbas=0&source=lnt&sa=X&ved=0ahUKEwi6raWDrujuAhXGdd4KHV7EC1wQpwUIKQ&biw=1280&bih=578&dpr=1.5"
        V = {}        
        for i in range(len(EditBox)):
            if not EditBox[i].get() == '':                
                V[i] = V1 + EditBox[i].get() + V2    
                # ChromeアプリのUNIX実行ファイルのパス        
                subprocess.Popen(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',V[i]])
                
        
        self.write()

    def note0(self,data):
        # 「株情報」タブのデザイン
        label0 = ttk.Label(note0,text="【検索ワード】",font=("",30),foreground="#ff0000")
        label0.pack(pady=20,side='top')
        global EditBox
        EditBox = {}
        for i in range(8):
            EditBox[i] = ttk.Entry(note0,width = 18,font=("",18))
        for i in range(len(data)):
            EditBox[i].insert(tkinter.END,data[i])
        for i in range(8):
            EditBox[i].pack(pady=5,side='top')
        buttonstyle = ttk.Style()
        #buttonstyle.theme_use('alt')
        buttonstyle.configure("office.TButton", font=("",20), anchor="center",fg = "red",background="hotpink")
        text = ["検索", "保存"]
        def button(i):
            button = ttk.Button(note0,text=text[i],style="office.TButton",padding=[1],width=3)            
            if i == 0:
                button.configure(command=self.search)
            else:
                button.configure(command=self.write)
            button.pack(pady=15,side='right',expand=True)
        for i in range(len(text)):
            button(i)


    def X1(self):
        # ダウ平均
        N1 = "https://www.sbisec.co.jp/ETGate/?_ControlID=WPLETmgR001Control&_PageID=WPLETmgR001Mdtl20&_DataStoreID=DSWPLETmgR001Control&_ActionID=DefaultAID&burl=iris_indexDetail&cat1=market&cat2=index&dir=tl1-idxdtl%7Ctl2-.DJI%7Ctl5-jpn&file=index.html&getFlg=on"
        subprocess.Popen(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',N1])
        
    
    def X2(self):
        # ダウ先物
        N1 = "https://www.sbisec.co.jp/ETGate/?_ControlID=WPLETmgR001Control&_PageID=WPLETmgR001Mdtl20&_DataStoreID=DSWPLETmgR001Control&_ActionID=DefaultAID&burl=iris_indexDetail&cat1=market&cat2=index&dir=tl1-idxdtl%7Ctl2-JDIc1%7Ctl5-jpn&file=index.html&getFlg=on"
        subprocess.Popen(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',N1])

    def X3(self):
        # 日経平均
        N1 = "https://www.sbisec.co.jp/ETGate/?_ControlID=WPLETmgR001Control&_PageID=WPLETmgR001Mdtl20&_DataStoreID=DSWPLETmgR001Control&_ActionID=DefaultAID&burl=iris_indexDetail&cat1=market&cat2=index&dir=tl1-idxdtl%7Ctl2-.N225%7Ctl5-jpn&file=index.html&getFlg=on"
        subprocess.Popen(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',N1])
    

    def note1(self):
        label = ttk.Label(note1,text="【ダウ平均株価】",font=("",30))
        label.place(x=26, y=20)
        text = ["平均株価", "先物株価"]        
        def button(i):
            button = ttk.Button(note1,text=text[i],style="office.TButton",padding=[1],width=6)
            if i == 0:
                button.configure(command=self.X1)
            else:
                button.configure(command=self.X2)
            button.place(x = 10+140*i,y = 70)

        for i in range(len(text)):
            button(i)

        text = ["【日経平均株価】"]
        xaxis = [26,0,18]
        def labelbutton(i):
            label = ttk.Label(note1,text=text[i],font=("",30))
            label.place(x=xaxis[i],y=130+110*i)
            button = ttk.Button(note1,text="検索",style="office.TButton",padding=[1],width=3)
            button.configure(command=self.X3)
            button.place(x=100,y=180+110*i)
        for i in range(len(text)):
            labelbutton(i)
    
    def read1(self):
        # テキスト（write1.txt）内のデータ読み取り
        # 「メモ」タブのテキスト欄にwrite1.txtの記入内容を反映
        f = open('write1.txtのパス', 'r', encoding='utf-8')
        global data1
        data1 = f.read()
        f.close()
        # data = list(map(lambda x:x.strip(), data))

    def write1(self):
        # テキスト内にメモ内容上書き
        # 「メモ」タブの記入内容をwrite1.txtに記入
        f = open('write1.txtのパス', 'w', encoding='utf-8')
        S = txt.get('1.0', 'end -1c')
        f.write(S)
        f.close()


    def note2(self):
        # メモ帳
        label = ttk.Label(note2,text="【メモ帳】",font=("",30), foreground = 'blue')
        label.pack()
        global txt
        txt = tkinter.Text(note2,width = 200, height = 19,font=("",18))
        txt.insert(tkinter.END,data1)
        scroll = tkinter.Scrollbar(note2, orient=tkinter.VERTICAL, command=txt.yview)
        scroll.pack(side=tkinter.RIGHT, fill="y")
        #動きをスクロールバーに反映
        txt["yscrollcommand"] = scroll.set
        txt.pack()
        button = ttk.Button(note2,text="保存",style="office.TButton",padding=[1],width=3)
        button.configure(command=self.write1)   
        button.pack()



if __name__ == '__main__':
    # ウィンドウ表示
    root = tkinter.Tk()
    root.title("Dow Jones")
    root.geometry("356x567")
    root.configure(bg = 'white')
    # 最大化ボタン非表示
    root.resizable(0,0)
    NotebookSample(master = root)
    root.mainloop()

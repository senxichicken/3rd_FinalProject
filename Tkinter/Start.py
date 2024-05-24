import tkinter as tk
from PIL import Image, ImageTk
import threading
import Role
from character import tk_img

img = Image.open('D:/Homework/specialsubject/project/Tkinter/picture/KP.png')


def start(root,btnStart,btnAbout,btnExit,his,background_label):
    global tk_img#必須宣告為全域變數，否則當label更改完畢後回到MainWindows時則tk_img會丟失。
    background_label.destroy()
    btnStart.destroy()
    btnAbout.destroy()
    btnExit.destroy()

    tk_img = ImageTk.PhotoImage(img)
    imglabel = tk.Label(root,
                        image=tk_img,
                        bg = '#000000',
                        padx = 10,
                        pady = 10,
                        )
    imglabel.pack()
    #print(imglabel)
    #print(img)
    horizontal_btn = tk.Frame(root)
    btnNext = tk.Button(horizontal_btn,
                        text = ("下一頁"),
                        width= 5,height= 1 , #btn的大小是看字元數
                        font = ('Arial',15,'bold'),
                        fg = '#000000',
                        bg = '#808080',
                        command=  lambda:chat_Next(chat,btnNext,btnAns,his,imglabel)
                        )
    btnNext.pack(side = 'right')
    btnAns = tk.Button(horizontal_btn,
                        text = ("輸入"),
                        width= 5,height= 1 , #btn的大小是看字元數
                        font = ('Arial',15,'bold'),
                        fg = '#000000',
                        bg = '#808080',
                        command = None
                        )
    #btnAns.pack(side = 'right') 後面有需要再pack
    horizontal_btn.pack(fill = 'x')
    chat =tk.Text(root,
                  wrap = tk.WORD,
                  width = 20,
                  height = 5,
                  font = ('Arial', 20, 'bold'), 
                  fg='#000000', 
                  bg='#808080', 
                  pady=30)
    chat.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
    chat.insert(tk.END,"接下來將由我帶您進入TPRG的世界")
    '''chat = tk.Label(root,
                    width= 1280,height= 150 ,
                    text = "接下來將由我帶您進入TPRG的世界",
                    font = ('Arial',20,'bold'),
                    wraplength = 1000,
                    fg = '#000000',
                    bg = '#808080',
                    pady = 30,
                    justify = 'left'
                    )
    chat.pack(anchor= 's')
    '''


def background_task():
    print(Role.player_data)
    
    timer = threading.Timer(2, background_task)
    timer.start()   
    if Role.player_data:
        #print("gg")
        timer.cancel()



#聊天室窗控制
def chat_Next(chat, btnNext,btnAns,his,imglabel):
    
    #print("Button Text:", btnNext.cget("text"))

    if btnNext.cget("text") == "下一頁":
        btnNext.config(text="創建")
        chat.delete(1.0, tk.END)
        chat.insert(tk.END,"請建立一張屬於您自己的角色卡!")
        background_task()
        btnNext.config(command=lambda: Role.Card(chat, btnNext,btnAns,his,imglabel))
        
        


 
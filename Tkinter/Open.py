import tkinter as tk
import Start
import webbrowser
from PIL import Image, ImageTk


root = tk.Tk()
root.title('TRPG in to COC')
root.resizable(False, False)

window_width = root.winfo_screenwidth()    # 取得螢幕寬度
window_height = root.winfo_screenheight()  # 取得螢幕高度

width = 1280 
height = 800
left = int((window_width - width)/2)       # 計算左上 x 座標
top = int((window_height - height)/2) 
root.geometry(f'{width}x{height}+{left}+{top}')  # 定義視窗的尺寸和位置

frame_his = tk.Frame(root)
frame_his.pack(side="top", fill="both", expand=True)

file_path = "D:/Homework/specialsubject/project/Tkinter/picture/cover.jpg"
image = Image.open(file_path)
image = image.resize((1280, 800), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

root.config(bg="white")  # 設置一個基本的背景色，以防圖片不完全填滿整個視窗
background_label = tk.Label(root, image=photo)
background_label.image = photo
background_label.place(relwidth=1, relheight=1)

def About():
    url = "https://yuukotrpg.weebly.com/247362337630340trpg308623086221816/trpg" 
    webbrowser.open(url)

his = tk.Button(frame_his,
                width = 8 , height = 1,
                text = ("歷史紀錄"),
                font = ('Arial',15,'bold'),
                fg = '#000000',
                bg = '#808080',
                command = None)



btnStart = tk.Button(
                     root,
                     width = 8 , height = 1,
                     text = ("開始遊戲"),
                     font = ('Arial',15,'bold'),
                     fg = '#000000',
                     bg = '#D3D3D3',
                     command= lambda:Start.start(root,btnStart,btnAbout,btnExit,his,background_label)
                     )
btnAbout = tk.Button(root,
                     width = 8 , height = 1,
                     text = ("關於TRPG"),
                     font = ('Arial',15,'bold'),
                     fg = '#000000',
                     bg = '#D3D3D3',
                     command = lambda:About())
btnExit = tk.Button(root,
                     width = 8 , height = 1,
                     text = ("離開遊戲"),
                     font = ('Arial',15,'bold'),
                     fg = '#000000',
                     bg = '#D3D3D3',)



btnStart.pack()
btnAbout.pack()
btnExit.pack()

root.mainloop()


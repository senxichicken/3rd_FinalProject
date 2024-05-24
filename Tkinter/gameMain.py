import tkinter as tk
from tkinter import ttk
from character import tk_img
from tkinter import Entry, Button, Text, Scrollbar,ttk
import time
import text
import threading
import his_insert
import imageCreate
from character import tk_img
from PIL import Image,ImageTk
import os
from character import player_data
from datetime import datetime
image_changed = False


def box_update(chat,btnAns,btnNext,his,imglabel):

    btnNext.pack_forget()
    chat.delete(1.0, tk.END)
    chat.insert(tk.END, "首先，請先輸入「開始」測試!")

    btnAns.config(command = lambda:dialog(chat,imglabel))
    btnAns.pack(side = 'right')

    his.config(command = lambda: his_insert.his_show())
    his.pack(side = 'left')


def dialog(chat,imglabel):
    
    diabox = tk.Toplevel()
    diabox.resizable(False, False)

    window_width = diabox.winfo_screenwidth()    # 取得螢幕寬度
    window_height = diabox.winfo_screenheight() 
    width = 300
    height = 100
    left = int((window_width - width)/2)       # 計算左上 x 座標
    top = int((window_height - height)/2) 
    diabox.geometry(f'{width}x{height}+{left}+{top}') 

    diabox.title("輸入您的行動")

    entry = Entry(diabox, width=50)
    entry.pack(pady=10)

    btn_inpu = Button(diabox, text="確定!",command=lambda:check(entry,chat,diabox,imglabel))
    btn_inpu.pack(pady=10)
    diabox.wait_window()
  

def check(entry,chat,diabox,imglabel):
    
    #output = text.context(entry)
    #chat.delete(1.0, tk.END)
    #chat.insert(tk.END, output)
    #diabox.destroy()  # 關閉回覆視窗
    #return output
    thread = threading.Thread(target=run_text, args=(entry, chat, diabox,imglabel))
    thread.start()
def run_text(entry, chat, diabox,imglabel):
    global tk_img,image_changed

    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{player_data['姓名']}.txt"
    # 進度條
    progress_bar = ttk.Progressbar(diabox, length=200, mode="indeterminate")
    progress_bar.pack(side="bottom")
    progress_bar.start()

    # 獲取爬蟲結果
    input,output = text.context(entry)
    #背景生成
    his_insert.mes_save(input,output)
    
    # 更新 chat
    chat.delete(1.0, tk.END)
    chat.insert(tk.END, output)

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            old_text = file.read()
        chat.insert(tk.END, old_text + '\n---分隔符---\n')
    except FileNotFoundError:
        pass  #

    new_text = f"你: {input}\n劇情: {output}\n"
    
    custom_logs_folder = "D:/Homework/specialsubject/project/Tkinter"  
    save_folder = os.path.join(custom_logs_folder, 'logs')

    # 確保保存的文件夾存在
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    
    text_save(new_text, folder=save_folder, file_name=file_name)
    #圖片生成，先暫停 不然生一張圖好花錢QQ
    '''if not image_changed:
        imageCreate.Delle(output)
        image_path = "image.png"
        img = Image.open(image_path)
        tk_img = ImageTk.PhotoImage(img)
        imglabel.config(image=tk_img)

        
        image_changed = True
    '''
    progress_bar.stop()
    progress_bar.destroy()
    

    # 關閉視窗
    diabox.destroy()
def text_save(text_content, folder=".", file_name="output_log.txt"):
    file_path = os.path.join(folder, file_name)
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(text_content)
        print(f"文本已成功附加到本地文件 {file_path}")
    except Exception as e:
        print(f"保存文本時發生錯誤: {e}")
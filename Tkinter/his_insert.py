import tkinter as tk
from tkinter.ttk import *

history_in = ""
history_out = ""
history_list = []




'''def his_flag():
    global flag
    flag = 1
    print("hisfalg")
    '''
def his_close(his_win):
    his_win.withdraw()


def mes_save(input,output): 
    global history_in , history_out    
    history_in = input
    history_out = output
    #print("1_1" + history_in)
    #print("1_2" + history_out)


def insert_text(history):
        global flag

        history.tag_configure('right_align', justify='right', foreground='#FF0000')
        history.tag_configure('left_align', justify='left', foreground='#000000')

        history_list.append((history_in, history_out))
        if not history.get("1.0", tk.END).strip():
            history.delete(1.0, tk.END)
        
        # 重新構建整個文本
        for in_text, out_text in history_list:

            history.insert(tk.END, '\n' + in_text, 'right_align')


            history.insert(tk.END, '\n' + out_text, 'left_align')
        

    #print("2_1" + history_in)
    #print("2_2" + history_out)
def his_show():

    his_win=tk.Tk()
    his_win.attributes('-alpha',0.85)
    his_win.resizable(False, False)

    window_width = his_win.winfo_screenwidth()    # 取得螢幕寬度
    window_height = his_win.winfo_screenheight()  # 取得螢幕高度

    width = 1200
    height = 750
    left = int((window_width - width)/2)       # 計算左上 x 座標
    top = int((window_height - height)/2) 
    his_win.geometry(f'{width}x{height}+{left}+{top}')  # 定義視窗的尺寸和位置
    his_win.overrideredirect(True)


    frame1 = tk.Frame(his_win)

    frame1.pack(side="top", fill="both", expand=True) 
    btn = tk.Button(frame1,
                    width = 2 , height = 1,
                    text = ("X"),
                    font = ('Arial',15,'bold'),
                    fg = '#000000',
                    bg = '#808080',
                    command= lambda : his_close(his_win)

        )   
    btn.pack(anchor = "ne")

    frame2 = tk.Frame(his_win)   # 建立 Frame
    frame2.pack()
    scrollbar = tk.Scrollbar(frame2)               
    scrollbar.pack(side='right', fill='y')

    history =tk.Text(frame2,
                    wrap = tk.WORD,
                    width = 80,
                    height = 20,
                    font = ('Arial', 20, 'bold'), 
                    fg='#000000', 
                    bg='#808080', 
                    pady=30,
                    yscrollcommand=scrollbar.set)

    history.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
    scrollbar.config(command=history.yview)
    
    insert_text(history)



    

    


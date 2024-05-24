import tkinter as tk
from tkinter import StringVar
import random
import openai
from collections import defaultdict
import gameMain
from character import player_data

with open('D:/Homework/specialsubject/project/secretkey.txt','r') as file:
    apikey = file.read().rstrip()

openai.api_key = apikey

#player_data = {}

def Card(chat, btnNext,btnAns,his,imglabel):

    card = tk.Toplevel()
    card.title('TRPG into COC')
    card.resizable(False, False)

    window_width = card.winfo_screenwidth()
    window_height = card.winfo_screenheight()

    width = 800
    height = 900
    left = int((window_width - width) / 2)
    top = int((window_height - height) / 2)
    card.geometry(f'{width}x{height}+{left}+{top}')

    card.configure(bg='#ccc')

    top_frame = tk.Frame(card)
    top_frame.pack(side="top", fill="both", expand=True)

 
    left_top_frame = tk.Frame(top_frame)
    left_top_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

    local = tk.Label(left_top_frame, text='基本資料', background='#ccc', font=('Arial', 20))
    local.pack()

    

    frame1 = tk.Frame(left_top_frame)
    frame1.pack(pady=5)

    labels = ['姓名', '職業', '學歷', '背景年代', '性別', '年齡', '出生地', '居住地']
    entries = []

    for i, label_text in enumerate(labels):
        label = tk.Label(frame1, text=label_text, background='#f90', font=('Arial', 16))
        entry = tk.Entry(frame1)

        label.grid(column=0, row=i + 1, sticky='w', padx=10, pady=5)
        entry.grid(column=1, row=i + 1, sticky='e', padx=10, pady=5)

        entries.append(entry)

    buttonTOP = tk.Button(left_top_frame, text="自動生成角色", command=lambda: card.after(0, lambda: Top_action(labels, entries)))
    buttonTOP.pack()
    

    # Right part of the top frame (newly added)
    right_top_frame = tk.Frame(top_frame)
    right_top_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

    ability = tk.Label(right_top_frame, text='能力值', background='#ccc', font=('Arial', 20))
    ability.pack()

    frame2 = tk.Frame(right_top_frame)
    frame2.pack(pady=5)

    

    labels2 = ['力量', '體質', '敏捷', '外貌', '意志', '智力', '體型', '教育', '幸運']
    label_vars = [StringVar(card) for _ in labels2]

    for i, label_text in enumerate(labels2):
        label = tk.Label(frame2, text=label_text, background='#f90', font=('Arial', 18))
        label_var = label_vars[i]
        label_var.set("一般")  # 初始值

        label.grid(row=i + 1, column=0, sticky='w', padx=10, pady=5)

        label_display = tk.Label(frame2, textvariable=label_var, font=('Arial', 14))
        label_display.grid(row=i + 1, column=1, sticky='e', padx=10, pady=5)

    buttonB = tk.Button(frame2, text='自動投骰', command=lambda: B_action(label_vars))
    buttonB.grid(row=len(labels2) + 2, column=1, pady=10)

    # Bottom frame (newly added)
    bottom_frame = tk.Frame(card)
    bottom_frame.pack(side="bottom", fill="both", expand=True)

    # Label for the bottom frame (newly added)
    bottom_label = tk.Label(bottom_frame, text='你可以依據自己的喜好建構你的角色，或使用自動生成按鈕!\
                            完成輸入後請按自動投骰決定你的調查員數值，之後你將會以這些數值來判定事件是否成功!', background='#ccc', font=('Arial', 20),wraplength=800, justify='left')
    bottom_label.pack(side="top", fill="both", expand=True)

    # Button inside the new frame (newly added)
    confirm_button = tk.Button(bottom_frame, text='確定', command=lambda: confirm_button_function(card,labels, entries, labels2, label_vars,chat, btnNext,btnAns,his,imglabel))
    confirm_button.pack()

    card.mainloop() 

def B_action(label_vars):
    attributes_3d6 = [sum(random.randint(1, 6) for _ in range(3)) * 5 for _ in range(5)]
    attributes_2d6_plus_6 = [sum(random.randint(1, 6) for _ in range(2)) + 6 for _ in range(3)]
    LUK = sum(random.randint(1, 6) for _ in range(3)) * 5

    for i, value in enumerate(attributes_3d6 + attributes_2d6_plus_6 + [LUK]):
        label_vars[i].set(value)

def PL_autoCreate():

    prompt = "產生一個故事的主角，這個主角可能來自世界各地，只生成包含姓名,職業, 學歷, 背景年代, 性別, 年齡, 出生地, 居住地的一位虛擬角色。\
              最後以下列格式總結你生成的內容，且不需要贅述。 姓名: 職業: 學歷: 背景年代: 性別: 年齡: 出生地: 居住地:  "

    # 提供一個提示（prompt）並生成文本
    OPENA_AI_MODEL = "gpt-3.5-turbo-instruct"
    DEFAULT_TEMPERATURE = 0.7

    response = openai.Completion.create(
    model=OPENA_AI_MODEL,
    prompt=prompt,
    temperature=DEFAULT_TEMPERATURE,
    max_tokens=200,
    n=1,
    stop=None,
    presence_penalty=0,
    frequency_penalty=0.1,
    )   

    #print(type(response["choices"][0]["text"]))

    #print(response['choices'][0]['message']['content'])

    feature = response["choices"][0]["text"]

    return feature

def Top_action(labels, entries):
    featuretext = PL_autoCreate()
    generated_content = defaultdict(lambda: "未知")
    for line  in featuretext.split("\n"):
        if line and ": " in line:
            key, value = line.split(": ", 1)
            generated_content[key] = value
    
    for label_text, entry in zip(labels, entries):
        entry_value = generated_content[label_text]  # 如果找不到對應的鍵，默認為 "未知"
        entry.delete(0, tk.END)  # 清空 Entry
        entry.insert(tk.END, entry_value)  # 插入新的值
    #print(type(label_text))
    #print(entry_value)
    #print(entry_key)
    #print(generated_content)
    #print(generated_content[label_text])
def confirm_button_function(card,labels, entries, labels2, label_vars,chat, btnNext,btnAns,his,imglabel):
    # 創建一個新的字典
    
    global  player_data 

    # 處理基本資料
    for label, entry in zip(labels, entries):
        entry_value = entry.get()
        player_data[label] = entry_value

    # 處理能力值
    for label, label_var in zip(labels2, label_vars):
        value = label_var.get()
        player_data[label] = value
    #print(type(player_data))
    chat.delete(1.0, tk.END)
    chat.insert(tk.END, "您好!"+ player_data['姓名'] + "," + "\n" + "接下來我們將開始進行遊戲!")
    
    btnNext.config(text = "開始" ,command=lambda: gameMain.box_update(chat,btnAns,btnNext,his,imglabel))
    card.destroy()

    
    

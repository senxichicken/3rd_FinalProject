import openai
from character import player_data
import his_insert

openai.api_key = apikey


def chatGPT_api(list_msg, list_ans, message):
    
    global player_data
    Name = player_data['姓名']
    Job = player_data['職業']
    Sch = player_data['學歷']
    Era = player_data['背景年代']
    Sex = player_data['性別']
    Age = player_data['年齡']
    Born = player_data['出生地']
    Live = player_data['居住地']
    STR = player_data['力量']
    CON = player_data['體質']
    DEX = player_data['敏捷']
    APP = player_data['外貌']
    POW = player_data['意志']
    INT = player_data['智力']
    SIZ = player_data['體型']
    EDU = player_data['教育']
    LUK = player_data['幸運']

    system_role = 'You are a Tabletop Role Playing Game expert player\
                  當玩家輸入 開始 後，你需要生成一段約30個字左右起始劇情。\
                   劇情為玩家遇到什麼事情或遇到什麼人、需要前往哪個目的地、做什麼，這三件事情，關於目的地的風景敘述越完整越好，請使用繁體中文。\
                   並且在劇情結尾提供三個選項讓玩家繼續進行遊戲，須注意這三個選項格式為劇情末端先換行後條列 1.選項一2.選項二3.選項三 ，且每個選項皆須於末端換行'
    
    user_role = '當玩家回覆非 開始 的內容即為行動，判斷行動是否需要使用'+f"力量{STR}、體質{CON}、敏捷{DEX}、外貌{APP}、意志力{POW}、智力{INT}、身材{SIZ}、學歷{EDU}、運氣{LUK}"+\
                    '其中一個最有關連的能力進行大小判定，如果行動與能力關聯不大則不需要，而如果有密切關聯，請從1~99中隨機生成一個數字並與該能力進行比較，若數字比能力值大則行動成功，否則失敗。\
                    在判定過程輸出格式為 [能力判定 能力名字 原能力值 / 隨機生成數值 成功或失敗]。' 
    send_msg = [  
        {'role': 'system', 'content': system_role},
        {'role': 'user', 'content': user_role}
        ]

    # 讀取歷史訊息
    for i in range(len(list_msg)):
        _msg = {'role': 'user', 'content': list_msg[i]}
        send_msg.append(_msg)
        _ans = {'role': 'assistant', 'content': list_ans[i]}
        send_msg.append(_ans)

    # 玩家新回覆
    _msg = {'role': 'user', 'content': message}
    send_msg.append(_msg)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=send_msg
    )
        
    # 直接返回 API 返回的助手回應
    return response["choices"][0]["message"]["content"]
history_list_msg = []
history_list_ans = []


def context(entry):    
    message = entry.get()
    #print(message)
    answer = chatGPT_api(history_list_msg, history_list_ans, message)
    history_list_msg.append(message)
    history_list_ans.append(answer)
    #print(":回答")
    #print(answer)
    #print("\n")
    #print(history_list_ans)
    return message, answer

if __name__ == "__main__":
    context()

'''
f"我將以以下敘述的角色遊玩這次的角色扮演，\
                  姓名{Name}，職業{Job}，教育背景{Sch}，背景{Era}年代，性別{Sex}，年齡{Age}，出生地{Born}，居住地{Live}，\
                  "
'''
import openai
import requests
from io import BytesIO
from PIL import Image


openai.api_key = apikey
openai.Model.list()

def image_textedit(output):
    system_role = "將故事劇情更改為對風景的特寫"
    user_role = output + "\n" + "請參考以上的敘述，敘述中包含了人物、地點、事件，\
        忽略敘述中關於角色的所有描述，僅針對地點的敘述，重新產生一個約20~30個字，且只描述地點的風景的敘述。"
    imageEdit = [
        {'role': 'system', 'content': system_role},
        {'role': 'user', 'content': user_role}
        ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = imageEdit
        )
    return response["choices"][0]["message"]["content"]

def Delle(output):
    image_role = image_textedit(output)
    print(image_role)
    response = openai.Image.create(
        model="dall-e-2",
    # 使用 DALL-E 2 模型的名稱
        prompt=image_role,
        size="512x512",
        n=1,
    )
    image_url = response.data[0].url
    save_path = "image.png"
    download_image(image_url,save_path)
    #print(image_url)

def download_image(url,save_path):
    try:
        response = requests.get(url)   
        if response.status_code == 200:
            image_data = BytesIO(response.content)
            with Image.open(image_data) as img:
                img.save(save_path)
            print(f"Image downloaded and saved to {save_path}")
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")


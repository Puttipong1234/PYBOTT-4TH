from linebot.models import *

text = TextSendMessage(text="hello").as_json_dict()
print(type(text))

image = ImageSendMessage(original_content_url="https://www.w3schools.com/w3css/img_lights.jpg",
                        preview_image_url="https://www.w3schools.com/w3css/img_lights.jpg"
)

print(image)

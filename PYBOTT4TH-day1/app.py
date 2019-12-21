from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from config import channel_access_token , channel_secret
from exam import car_timer


app = Flask(__name__)
user_database = {} #initial database
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


import time

def isTimeFormat(input):
    try:
        time.strptime(input, '%H:%M')
        return True
    except ValueError:
        return False



@app.route("/callback", methods=['GET','POST'])
def callback():
    if request.method == "POST":
        # get X-Line-Signature header value
        signature = request.headers['X-Line-Signature']

        # get request body as text
        body = request.get_data(as_text=True)
        app.logger.info("Request body: " + body)

        # handle webhook body
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            print("Invalid signature. Please check your channel access token/channel secret.")
            abort(400)

        return 'OK'
    
    elif request.method == "GET":
        return "This is Get Method หน้าเว็บสำหรับรับ Request"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    text_from_user = event.message.text  #get msg from user #สมมุติ user พิม "7 10 8 30".split(" ") => [7,10,8,30]
    reply_token = event.reply_token  #get reply token
    userid = event.source.user_id # get userid 

    if userid not in user_database.keys(): # if no this user in database
        user_database[userid] = {
            "เวลาเข้า":None,
            "เวลาออก":None
        }
    
    if isTimeFormat(text_from_user): #7:30 
        if user_database[userid]["เวลาเข้า"] is None:
            user_database[userid]["เวลาเข้า"] = text_from_user

            text_to_send = TextSendMessage(text="กรอกเวลาเข้าเรียบร้อยคะ")
            line_bot_api.reply_message(reply_token=reply_token,
                                messages = text_to_send )
            return '200'
        
        else :
            user_database[userid]["เวลาออก"] = text_from_user
    
    if user_database[userid]["เวลาเข้า"] is None:

        text_to_send = TextSendMessage(text="ท่านยังไม่ได้กรอกเวลาเข้าจอด")
        text_to_send_2 = TextSendMessage(text="กรุณาพิมพ์เวลาที่รถเข้าจอดด้วยคะ")

        line_bot_api.reply_message(reply_token=reply_token,
                                messages = [text_to_send,text_to_send_2] )
        return '200'
    
    elif user_database[userid]["เวลาออก"] is None:
        text_to_send = TextSendMessage(text="ท่านยังไม่ได้กรอกเวลาออก")
        text_to_send_2 = TextSendMessage(text="กรุณาพิมพ์เวลาที่รถออกด้วยคะ")

        line_bot_api.reply_message(reply_token=reply_token,
                                messages = [text_to_send,text_to_send_2] )
        return '200'

    in_hr , in_min = user_database[userid]["เวลาเข้า"].split(":")  # 7:30
    out_hr , out_min = user_database[userid]["เวลาออก"].split(":")  # 8:30 

    จำนวนเงินที่ต้องจ่าย = car_timer(in_hr=in_hr,
                                in_min=in_min,
                                out_hr=out_hr,
                                out_min=out_min)

    message_to_reply = "จำนวนเงินที่ต้องจ่าย : {} บาท".format(จำนวนเงินที่ต้องจ่าย) 

    text_to_send = TextSendMessage(text=message_to_reply)

    image = ImageSendMessage(original_content_url="https://www.w3schools.com/w3css/img_lights.jpg",
                        preview_image_url="https://www.w3schools.com/w3css/img_lights.jpg"
)

    line_bot_api.reply_message(reply_token=reply_token,
                                messages = [text_to_send,image] )
    
    user_database[userid] = {
            "เวลาเข้า":None,
            "เวลาออก":None
        }

if __name__ == "__main__":
    app.run(debug=True)
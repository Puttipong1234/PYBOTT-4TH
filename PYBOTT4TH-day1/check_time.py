import time

def isTimeFormat(input):
    try:
        time.strptime(input, '%H:%M')
        return True
    except ValueError:
        return False

print(isTimeFormat("สวัสดีค่ะ"))
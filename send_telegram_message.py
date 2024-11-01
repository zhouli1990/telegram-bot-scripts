# @1

import requests

# 机器人API Token
bot_token = 'YOUR_BOT_TOKEN'
# 要发送消息的用户ID
user_id = 'TARGET_USER_ID'
# 日志文件的路径
log_file_path = '/root/result.log'

# 读取文件最后两行的内容
def get_last_two_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # 返回最后两行内容
        return ''.join(lines[-2:])

# 获取要发送的消息内容
message = get_last_two_lines(log_file_path)

# 发送消息的URL
url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

# 发送请求
response = requests.post(url, data={
    'chat_id': user_id,
    'text': message
})

# 检查发送结果
if response.status_code == 200:
    print("Message sent successfully!")
else:
    print("Failed to send message:", response.json())

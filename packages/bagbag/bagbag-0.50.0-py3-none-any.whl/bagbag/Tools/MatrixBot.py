from __future__ import annotations

# 需要配合以下服务食用
# 
# version: '3'
# services:
#   matrix_bot:
#     image: darren2046/matrix-bot:0.0.1
#     container_name: matrix-bot
#     restart: always
#     #ports:
#     #   - "8888:8888" 
#     environment:
#       MATRIX_SERVER: "https://your.homeserver.com"
#       MATRIX_USER: account_username 
#       MATRIX_PASS: account_password
#       API_PASS: password_for_call_this_api_server # can be empty
#     dns:
#       - 8.8.8.8
#       - 4.4.4.4
#     volumes:
#       - /data/cr-volumes/matrix-bot/data:/data
# 备注:
# 版本0.0.1
#     arm64的可以调用http api发送消息, 也可以收消息(发送id给bot返回房间号)
#     amd64的可以调用http api发送消息, 但是不能收消息, 一脸蒙逼
#     

try:
    from .. import Http
    from .. import Base64
except:
    import sys
    sys.path.append("..")
    import Http 
    import Base64

class MatrixBot():
    def __init__(self, apiserver:str, password:str="") -> None:
        self.apiserver = apiserver.rstrip('/')
        self.password = password 
    
    def SetRoom(self, room:str) -> MatrixBot:
        """
        如果room的id是 !abcdefghiljkmn:example.com, 那么room可以是abcdefghiljkmn, 默认取homeserver的域名
        
        :param room: The room you want to join
        :type room: str
        """
        self.room = room

        return self
    
    def Send(self, message:str):
        Http.PostForm(
            self.apiserver + "/send/text", 
            {
                "room": self.room, 
                'text': message,
                'password': self.password,
            })
    
    def SendImage(self, path:str):
        Http.PostForm(
            self.apiserver + "/send/image", 
            {
                "room": self.room, 
                'image': Base64.Encode(open(path, 'rb').read()),
                'password': self.password,
            })

if __name__ == "__main__":
    mb = MatrixBot("https://example.com", 'password').SetRoom("xQIjxlkLqVdVKJaxwF")
    mb.Send("Hello World!")
import requests
import json

#输入歌曲ID
ID=input("歌曲ID:")

#根据歌曲ID获取网页原址
url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token=568cec564ccadb5f1b29311ece2288f1".format(ID)
#制作标头信息
headers = {
   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
   'Referer':'http://music.163.com/song?id=551816010',
   'Origin':'http://music.163.com',
   'Host':'music.163.com'
}
#加密数据，直接拿过来用
user_data = {
   'params': 'vRlMDmFsdQgApSPW3Fuh93jGTi/ZN2hZ2MhdqMB503TZaIWYWujKWM4hAJnKoPdV7vMXi5GZX6iOa1aljfQwxnKsNT+5/uJKuxosmdhdBQxvX/uwXSOVdT+0RFcnSPtv',
   'encSecKey': '46fddcef9ca665289ff5a8888aa2d3b0490e94ccffe48332eca2d2a775ee932624afea7e95f321d8565fd9101a8fbc5a9cadbe07daa61a27d18e4eb214ff83ad301255722b154f3c1dd1364570c60e3f003e15515de7c6ede0ca6ca255e8e39788c2f72877f64bc68d29fac51d33103c181cad6b0a297fe13cd55aa67333e3e5'
}

response = requests.post(url,headers=headers,data=user_data)

data = json.loads(response.text)
hotcomments = []
for hotcommment in data['hotComments']:
   item = {
       'nickname':hotcommment['user']['nickname'],
       'content':hotcommment['content'],
       'likedCount':hotcommment['likedCount']
   }
   hotcomments.append(item)

#获取评论用户名，内容，以及对应的获赞数
content_list = [content['content'] for content in hotcomments]
nickname = [content['nickname'] for content in hotcomments]
liked_count = [content['likedCount'] for content in hotcomments]

index = len(nickname)
for i in range(index):
    print ("ID:",nickname[i]," 赞数",liked_count[i],"-----",content_list[i])

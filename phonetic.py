import requests
import re
import random
from bs4 import BeautifulSoup

def learn(voca):
    url = "https://tw.amazingtalker.com/blog/zh-tw/zh-eng/3747/"
    
    html = requests.get(url)
    bs = BeautifulSoup(html.text, 'lxml')
    words = bs.find_all("td")
    num = random.randint(1, 1200)
    
    try:
        for word in words:
            text = word.text
            # 使用正则表达式检测并删除包含 "-" 的部分
            mod_text = re.sub(r'\(.*?-.*?\)', '', text).strip()
            # 仅在 modified_text 不为空时打印
            if mod_text:
                part = mod_text.split('.')
                if int(part[0]) == num:
                    # print(num)
                    return (part[1])
    except:
        return '錯誤，請稍候再試'


# import requests
# from bs4 import BeautifulSoup
# # word = input( '請輸入中文字:' )
# def read(word):
#     url = f'https://dict.revised.moe.edu.tw/search.jsp?md=1&word={word}#searchL'

#     html = requests.get( url )
#     bs = BeautifulSoup(html.text,'lxml')
#     data = bs.find('table', id='searchL')
#     try:
#         row = data.find_all('tr')[2]
#         chinese = row.find('cr').text
#         phones = row.find_all('code')
#         phone = [e.text for e in phones]
#         s = " ".join( phone )
#         # s = row.find('sub')
#         return chinese +  ' => ' + s 
#     except:
#         return '查無此字'
    
# # read('國小')

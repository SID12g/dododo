import requests
from bs4 import BeautifulSoup

def color(color):
    match color:
        case 'fc1cad':
            return "LG"
        case '86001f':
            return "키움"
        case 'f37321':
            return '한화'
        case '042071':
            return '두산'
        case '0061AA':
            return '삼성'
        case '002b69':
            return 'NC'
        case 'cf152d':
            return 'SSG'
        case '000000':
            return 'KT'
        case 'ed1c24':
            return 'KIA'
        case '888888':
            return '롯데'
        case _:
            return color

cnt = 0
file = input('파일명을 입력하세요.\n')
href = input('주소를 입력하세요.\n')
person = int(input('선수 명 수를 입력하세요.\n'))
data = requests.get(href)
soup = BeautifulSoup(data.content, 'html.parser')
File = open(f'{file}.csv', 'w') 

for j in range(person):
    print(f'{j+1} / {person}')
    File.write(color(soup.select('tr td div.teams span')[3*cnt]['style'][12:18]))
    for i in range(31):
        if(i == 2):
            File.write(', '+soup.select('td')[i+cnt*31].text[4:6])
        else:
            File.write(', '+soup.select('td')[i+cnt*31].text)
        
    File.write('\n')
    cnt+=1
File.close()


"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #
        tags = soup.find_all('td')
        total = []
        for tag in tags:
            number = tag.text
            # 因為td裡有含'排名'、'男嬰姓名'、'女嬰姓名'及'資料來源'需要先排除這些不要的Data
            if not number.isdigit() and not number.isalpha() and 1 < len(number) < 50:
                new_number = ''
                # 抓出嬰兒總數後，因為是tuple所以要先轉換成數值
                for ch in number:
                    if ch.isdigit():
                        new_number += ch
                # 將轉成數值的男女嬰總數裝進list裡
                total.append(int(new_number))
        males = females = 0
        for i in range(len(total)):
            # 從網站裡可以看到都是先呈現男嬰數目在呈現女嬰，因此list裡中index是偶數的值等於男嬰；基數等於女嬰
            if i % 2 == 0:
                males += total[i]
            else:
                females += total[i]
        print(f'Male Number: {males}')
        print(f'Female Number: {females}')


if __name__ == '__main__':
    main()

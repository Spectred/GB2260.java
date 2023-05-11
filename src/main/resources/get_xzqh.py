import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    dict = {'2022': 'https://www.mca.gov.cn/article/sj/xzqh/2022/202201xzqh.html',
            # '2021': '',
            '2020': 'https://www.mca.gov.cn/article/sj/xzqh/2020/20201201.html',
            '2019': 'https://www.mca.gov.cn/article/sj/xzqh/1980/2019/202002281436.html',
            '2018': 'https://www.mca.gov.cn/article/sj/xzqh/1980/201903/201903011447.html',
            '2017': 'https://www.mca.gov.cn/article/sj/xzqh/1980/201803/201803131454.html',
            '2016': 'https://www.mca.gov.cn/article/sj/xzqh/1980/201705/201705311652.html',
            '2015': 'https://www.mca.gov.cn/article/sj/tjbz/a/2015/201706011127.html',
            '2014': 'https://files2.mca.gov.cn/cws/201502/20150225163817214.html',
            '2013': 'https://files2.mca.gov.cn/cws/201404/20140404125552372.htm',
            '2012': 'https://www.mca.gov.cn/article/sj/tjbz/a/201713/201707271556.html',
            '2011': 'https://www.mca.gov.cn/article/sj/tjbz/a/201713/201707271552.html',
            '2010': 'https://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220946.html',
            '2009': 'https://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220943.html',
            '2008': 'https://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220941.html',
            '2007': 'https://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220939.html',
            '2006': 'https://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220936.html',
            '2005': 'https://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220935.html',
            '2004': 'https://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220930.html',
            '2003': 'https://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220928.html',
            '2002': 'https://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220927.html',
            '2001': 'https://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220925.html',
            '2000': 'https://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220923.html',
            }
    for year, url in dict.items():
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        tds = soup.find_all('td')
        with open(year + '.txt', 'w') as f:
            for i in range(0, len(tds)):
                code = tds[i].text.strip()
                if len(code) == 0:
                    continue
                if not code.isdigit():
                    continue
                name = tds[i + 1].text.strip()
                f.write(f'{code}\t{name}\n')
        print(year, "✅")

import requests
import json

headers = {
    'Host': 'www.zhihu.com',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    # 'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
}


def getcontent(url):
    ans_all_url = 'https://www.zhihu.com/question/xxxx/answer/'
    resp = requests.get(url, headers=headers)
    object = json.loads(resp.text).get('data')

    for attr in object:
        ans_id = 0
        for k, v in attr.items():
            ans = ''
            if k == 'id':
                ans_id = v

            if k == "content":
                if v.find('xxx') >= 1:
                    print(ans_all_url + str(ans_id))

    json_res = json.loads(resp.text).get('paging')
    for k, v in json_res.items():

        if k == 'next':
            nex_turl = v
        if k == 'is_end':
            if v:
                return
        if k == 'next':
            nex_turl = v
            getcontent(nex_turl)


if __name__ == '__main__':
    # url 根据全部回答的update时间来取
    url = '¬'
    getcontent(url)

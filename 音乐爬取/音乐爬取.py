import re
from concurrent.futures import ThreadPoolExecutor

from Functions.file_save import *
from Functions.get_ajax_json import get_json
from Functions.get_now_date import get_date


def run_get_json():
    url = "https://re.bluepoch.com/activity/official/websites/music/query"
    header = {
        # "POST": "/activity/official/websites/picture/query HTTP/1.1",
        #
        # "Host": "re.bluepoch.com",

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
        #
        # "Accept": "application/json, text/javascript, */*; q=0.01",
        #
        # "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",

        # "Accept-Encoding": "gzip, deflate, br",

        "Content-Type": "application/json; charset=utf-8",

        # "X-Requested-With": "XMLHttpRequest",
        #
        # "Content-Length": "54",
        #
        # "Origin": "https://re.bluepoch.com",
        #
        # "Connection": "keep-alive",
        #
        # "Referer": "https://re.bluepoch.com/home/detail.html",
        #
        # "Sec-Fetch-Dest": "empty",
        #
        # "Sec-Fetch-Mode": "cors",
        #
        # "Sec-Fetch-Site": "same-origin"

    }
    data = {"id": "", "collectionId": "", "current": 1, "pageSize": 999}
    get_json(url, header, data, '音乐/query文件', get_date() + 'query.json')


def save_dict(_data_dict):
    path = '音乐'
    title = str(_data_dict['_info_dict']['title']).replace('|', '-')
    date = get_date()
    _urls_dict = _data_dict['_urls_dict']
    for _url_name in _urls_dict:
        save_file(_urls_dict[_url_name], f'{path}/单独音乐{date}/{title}', _url_name)
        _tail_name = re.match('.*(\..*)', _url_name).group(1)
        if _tail_name == '.wav' or _tail_name == '.mp3':
            save_file(_urls_dict[_url_name], f'{path}/总音乐', _url_name)

    _json_dict = _data_dict['_info_dict']['all_json_data']
    save_json(_json_dict, f'{path}/单独音乐{date}/{title}', 'info.json')


def deal_datas_dict(_datas_dict):
    def _get_tail_name(_str_name):
        return re.match('.*/(.*)', _str_name).group(1)

    musicUrl = _datas_dict['musicUrl']
    bigCoverUrl = _datas_dict['bigCoverUrl']
    smallCoverUrl = _datas_dict['smallCoverUrl']

    _urls_dict = {
        _get_tail_name(musicUrl): musicUrl,
        _get_tail_name(bigCoverUrl): bigCoverUrl,
        _get_tail_name(smallCoverUrl): smallCoverUrl
    }
    _info_dict = {
        'title': _datas_dict['title'],
        'all_json_data': _datas_dict,
    }
    dealed_data_dict = {
        '_info_dict': _info_dict,
        '_urls_dict': _urls_dict,

    }
    return dealed_data_dict


run_get_json()
datas_dict = json_to_dict(f'音乐/query文件/{get_date()}query.json')
total_num = datas_dict['data']['total']
datas_list = datas_dict['data']['pageData']


def run_single(_datas_dict):
    dealed_data_dict = deal_datas_dict(_datas_dict)
    save_dict(dealed_data_dict)


total_num = 3
with ThreadPoolExecutor(max_workers=total_num) as executor:
    # 使用map方法将访问网页的任务提交给线程池
    results = executor.map(run_single, datas_list)

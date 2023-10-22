from bs4 import BeautifulSoup
import requests
import re
from concurrent.futures import ThreadPoolExecutor
from 重返未来1999.file_save import save_file, save_txt
from 重返未来1999.get_now_date import get_date
from 重返未来1999.tail import get_tail_type


def get_part_url():
    url = 'https://re.bluepoch.com/home/'

    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    _img_dict = soup.select('div .backstory-left .swiper-slide img.backstory-img')
    _picture_url = _img_dict[0].attrs['src']
    _part_url = re.match('(.*/).*', _picture_url).group(1)
    return _part_url, len(_img_dict)


def produce_urls(_base_url='https://re.bluepoch.com/home/', _part_url='img/backstory/', _img_num=8):
    _urls_list = []
    _url_dict = {}
    _info_dict = {}
    _data_dict = {}
    for _num in range(1, _img_num + 1):
        _url_dict = {
            f'p{_num}.png': f'{_base_url + _part_url}p{_num}.png',
            f'p{_num}c.png': f'{_base_url + _part_url}p{_num}c.png',
            f'p{_num}d.jpg': f'{_base_url + _part_url}p{_num}d.jpg',
            f't{_num}.png': f'{_base_url + _part_url}t{_num}.png',
        }
        _info_dict = {
            'num': _num,
            '描述.txt': backstoryStr_list[_num - 1]
        }
        _data_dict = {
            '_url_dict': _url_dict,
            '_info_dict': _info_dict,
        }
        _urls_list.append(_data_dict)
    return _urls_list


def run_save_dict(_data_dict):
    path = '世界/'
    date = get_date()
    _url_dict = _data_dict['_url_dict']
    _info_dict = _data_dict['_info_dict']
    for name in _url_dict:
        # save_path = path + '单独世界' + date + '/p' + str(_info_dict["num"])
        save_path = f"{path}/单独世界{date}/p{_info_dict['num']}"
        save_file(_url_dict[name], save_path, name)
        save_txt(_info_dict['描述.txt'], save_path, '描述.txt')
        if get_tail_type(name) == '.jpg':
            save_file(_url_dict[name], path + '总世界', name)


backstoryStr_list = [
    "1999年12月31日，23点59分。世纪之交的缝隙中，一场“暴雨”往天空倾泻。所有派对、彩灯、末班巴士都在下一刻消逝。世界回到了一个崭新的旧时代。<br>",
    "每个时代都有它的标志性城市，60年代属于伦敦，而20年代毫无疑问属于纽约。<br>1920年代的纽约，现代科学也在化一切为可能。福特汽车、无线电的使用，将世界推向乐观浪潮的更远处。爵士乐响彻通宵，人们在查尔斯顿舞步中奔赴下一场宴会。<br>没有人能拒绝加入这场狂欢。<br>",
    "20世纪60年代的一切都很好。波普艺术和嬉皮士风格开始在年轻人中流行起来，伦敦成为了“酷的中心”（Capital of Cool）。<br>更重要的是，海盗电台和摇滚乐在此兴起了。<br>",
    "一场不可思议的天方夜谭：第一滴雨滴坠入天空时，诡谲的异变随即伴生而来。<br>60年代的波普与色彩，20年代的铂金与爵士……随时代更迭，异变的体征亦有所不同。它就像是某种幻象，或者时代的海市蜃楼。<br>",
    "数千年来，人类第一防线学校接收了无数失去归所的神秘学家孩子，并为其提供系统的神秘学训练。<br>由此毕业的学生往往被视为人才模范，进入圣洛夫基金会、拉普拉斯科算中心、芝诺军备学院等世界前列组织。<br>但无论身处何处，这些白与灰菱格之下长大的孩子们从未忘却他们的准则与训诫——为了人类，为了和平。<br>",
    "万物皆有因果，世界衔于一蛇。<br>拉普拉斯科学计算中心在几次工业革命中声名鹊起，依凭着新锐技术与时代强风，发展成为世界上规模最为庞大的科研机构。<br>他们旨在研究科技与神秘术的结合，并推动第四次工业革命的到来。<br>在“暴雨”到来后，其主张以因果律为核心理论依据，由此演算、推导出回溯的原因与人类到达未来的可能性。<br>",
    "纺车。辅以湿润的雾气与流淌的河。它充满了神秘气息，总有人在其呼唤中欣然到访。<br>而你所需要做的，仅仅是——转动它。<br>",
    "一只深紫色菱格纹的手提箱。比羽毛重一些，较金锭轻一些。由一道不算复杂的咒语开启，通往一处开阔的居所。<br>其中罗列的门与窗数不胜数，各自通往不同的光景。这里不受“暴雨”的侵扰，可留存时代的印记。可预见的，将有许多神秘学家在此立足存身。<br>"
]
m_part_url, m_num = get_part_url()
m_urls_list = produce_urls(_part_url=m_part_url, _img_num=m_num)
with ThreadPoolExecutor(max_workers=8) as executor:
    # 使用map方法将访问网页的任务提交给线程池
    executor.map(run_save_dict, m_urls_list)

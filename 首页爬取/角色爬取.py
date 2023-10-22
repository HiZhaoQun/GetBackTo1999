import re
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup

from Functions.file_save import *
from datetime import datetime


#
#
# def get_character():
#     # host_url = 'https://re.bluepoch.com/home/'
#     response = requests.get(host_url)
#     html = response.text
#     # print(html.text)
#     return html
#
#
# def beautiful_soup(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     characters_list = soup.select('div #slide3.swiper-slide .swiper-slide img')
#     print(characters_list)
#     src_attrs = []
#     for character in characters_list:
#         print(character['src'])
#         src_attrs.append(character['src'])
#     return src_attrs
#
#
# def get_num_url(src_attr):
#     return re.match(".*?\d", src_attr).group(1)
#
#
# def produce_url():
#     html = get_character()
#     src_sttrs = beautiful_soup(html)
#     total_urls = []
#     for src_sttr in src_sttrs:
#         part_url = get_num_url(src_sttr)
#         total_url_dict = {}
#         names_dict = {
#             '灰色图像': str(part_url) + '.png',
#             '彩色人物图像': str(part_url) + 'c.png',
#             '人物签名': str(part_url) + 't.png',
#             '背景图像1': str(part_url) + 'bg.png',
#             '背景图像2': str(part_url) + 'false.webp',
#             '人物语音': str(part_url) + '.mp3',
#             '人物动画': str(part_url) + '.webm',
#             '人物特写图':
#
#         }
#         total_urls.append(total_url_dict)
#     return total_urls
#

bg = '背景图像'
role = '短角色视频'
rolem = '角色特写图像'
gif = '角色视频'
gifm = '纯角色视频'
nocheck = '纯角色特写图像'
check = ''
title = '人物签名图像'
str_sign = ''
voice = '人物语音'

characterMsg = [
    {
        bg: "5bg.png",
        role: "5s.webm",
        rolem: "5m.png",
        gif: "5.webm",
        gifm: "5m.gif",
        nocheck: "5.png",
        check: "5c.png",
        title: "5t.png",
        str_sign: "愿和平与我们同在。",
        voice: "./mp3/role/5.mp3"
    },
    {
        bg: "9bg.png",
        role: "9s.webm",
        rolem: "9m.png",
        gif: "9.webm",
        gifm: "9m.gif",
        nocheck: "9.png",
        check: "9c.png",
        title: "9t.png",
        str_sign: "在海上漂流，在电台狂欢，<br>向所有的新玩意儿发起进攻，直到永远！",
        voice: "./mp3/role/9.mp3"
    },
    {
        bg: "3bg.png",
        role: "3s.webm",
        rolem: "3m.png",
        gif: "3.webm",
        gifm: "3m.gif",
        nocheck: "3.png",
        check: "3c.png",
        title: "3t.png",
        str_sign: "太阳升起，野兽们噤声不吠。<br>而后，我听见第一只离林之鸟振翅的声响。",
        voice: "./mp3/role/3.mp3"
    },
    {
        bg: "1bg.png",
        role: "1s.webm",
        rolem: "1m.png",
        gif: "1.webm",
        gifm: "1m.gif",
        nocheck: "1.png",
        check: "1c.png",
        title: "1t.png",
        str_sign: "别辜负我的期望，各位同僚。",
        voice: "./mp3/role/1.mp3"
    },
    {
        bg: "6bg.png",
        role: "6s.webm",
        rolem: "6m.png",
        gif: "6.webm",
        gifm: "6m.gif",
        nocheck: "6.png",
        check: "6c.png",
        title: "6t.png",
        str_sign: "你好！我是苏芙比，如你所见是一个优秀而博学的淑女！<br>话说回来，刚刚那个农夫居然拥有一整群双角兽啊！",
        voice: "./mp3/role/6.mp3"
    },
    {
        bg: "8bg.png",
        role: "8s.webm",
        rolem: "8m.png",
        gif: "8.webm",
        gifm: "8m.gif",
        nocheck: "8.png",
        check: "8c.png",
        title: "8t.png",
        str_sign: "某人的剑，还没有生锈。",
        voice: "./mp3/role/8.mp3"
    },
    {
        bg: "4bg.png",
        role: "4s.webm",
        rolem: "4m.png",
        gif: "4.webm",
        gifm: "4m.gif",
        nocheck: "4.png",
        check: "4c.png",
        title: "4t.png",
        str_sign: "这单就由我接下喽，多谢老板～我是泥鯭的士，<br>当然你叫我安安是更好的啦，有空喊我一起发财啦～",
        voice: "./mp3/role/4.mp3"
    },
    {
        bg: "7bg.png",
        role: "7s.webm",
        rolem: "7m.png",
        gif: "7.webm",
        gifm: "7m.gif",
        nocheck: "7.png",
        check: "7c.png",
        title: "7t.png",
        str_sign: "别总盯着推荐剂量瞻前顾后的，好的实验效果需要大胆尝试——<br>我的建议是：直接拉满。",
        voice: "./mp3/role/7.mp3"
    },
    {
        bg: "2bg.png",
        role: "2s.webm",
        rolem: "2m.png",
        gif: "2.webm",
        gifm: "2m.gif",
        nocheck: "2.png",
        check: "2c.png",
        title: "2t.png",
        str_sign: "你会是个勇敢的发声者吗？<br>你看上去长得像——嗯，声音听起来也像。",
        voice: "./mp3/role/2.mp3"
    },
    {
        bg: "10bg.png",
        role: "10s.webm",
        rolem: "10m.png",
        gif: "10.webm",
        gifm: "10m.gif",
        nocheck: "10.png",
        check: "10c.png",
        title: "10t.png",
        str_sign: "嗨，嗨，我在这里。<br>我是星之眼，一名热爱和平的域外访客。",
        voice: "./mp3/role/10.mp3"
    }
]


def produce_url():
    host_url = 'https://re.bluepoch.com/home/'
    part_url = 'img/role/'
    character_part_url = 'img/character/'
    _urls_list = []

    sign_text = ''
    for i in range(0, len(characterMsg)):
        url_dict = {}
        data_dict = {}
        num = -1
        for name in characterMsg[i]:
            tail_url = characterMsg[i][name]
            sign_text = characterMsg[i][str_sign]
            if name == '人物语音':
                tail_name = re.match('.*?(\d+.mp3)', characterMsg[i][name]).group(1)
                url_dict[name + tail_name] = host_url + tail_url

            elif name:
                url_dict[name + characterMsg[i][name]] = host_url + part_url + tail_url

            num = get_num(characterMsg[i][bg])

        url_dict['人物灰色头像'] = host_url + character_part_url + num + '.png'
        url_dict['人物彩色头像'] = host_url + character_part_url + num + 'c.png'

        data_dict['str_sign'] = sign_text
        data_dict['urls_dict'] = url_dict

        logging.info(data_dict)
        _urls_list.append(data_dict)
    logging.info(_urls_list)
    return _urls_list


def get_num(str_text):
    return re.match('.*?(\d+).*?', str_text).group(1)


def save_dict(data_dict):
    save_path = f'角色/单独{date_time}/'
    logging.info('在读取url字典')
    url_dict = data_dict['urls_dict']
    sgin_text = data_dict['str_sign']

    for name in url_dict:
        url = url_dict[name]
        i = get_num(name)
        save_file(url, save_path + '人物' + str(i), name)
        save_txt(sgin_text, save_path + '人物' + str(i), 'sign.txt')

    logging.info('读取完成')


urls_list = produce_url()
date_time = datetime.now().date().strftime("%Y年%m月%d日")
max_work = len(urls_list)
with ThreadPoolExecutor(max_workers=10) as executor:
    # 使用map方法将访问网页的任务提交给线程池
    results = executor.map(save_dict, urls_list)

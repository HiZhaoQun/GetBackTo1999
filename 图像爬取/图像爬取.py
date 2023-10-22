from io import BytesIO
from os import makedirs
from os.path import exists
import requests
import logging
import json
from PIL import Image
from 重返未来1999.get_ajax_json import get_json
from 重返未来1999.get_now_date import get_date


def save_json():
    url = 'https://re.bluepoch.com/activity/official/websites/picture/query'
    header = {

        "POST": "/activity/official/websites/picture/query HTTP/1.1",

        "Host": "re.bluepoch.com",

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",

        "Accept": "application/json, text/javascript, */*; q=0.01",

        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",

        "Accept-Encoding": "gzip, deflate, br",

        "Content-Type": "application/json; charset=utf-8",

        "X-Requested-With": "XMLHttpRequest",

        "Content-Length": "54",

        "Origin": "https://re.bluepoch.com",

        "Connection": "keep-alive",

        "Referer": "https://re.bluepoch.com/home/detail.html",

        "Sec-Fetch-Dest": "empty",

        "Sec-Fetch-Mode": "cors",

        "Sec-Fetch-Site": "same-origin",

    }
    data = {"id": "", "collectionId": "", "current": 1, "pageSize": 999}
    save_path = 'query文件'
    detail_name = get_date() + "query" + '.json'
    get_json(url, header, data, save_path, detail_name)
    return save_path + '/' + detail_name


def read_json(file_name):
    """
    读取json文件，并转化为字典
    :param file_name:
    :return:
    """
    logging.info('正在读取文件 %s', file_name)
    json_dict = {}
    with open(file_name, 'r', encoding='UTF-8') as file:
        json_dict = json.load(file)
    logging.info('读取json文件完成，已经转为字典文件%s', str(json_dict))
    return json_dict


def read_dict(json_dict):
    """
    转字典为列表
    :param json_dict:
    :return:
    """
    logging.info('读取字典文件中')
    json_list = [json_dict['data']['pageData'][m]['pictureUrl'] for m in range(0, 42)]
    name_list = [json_dict['data']['pageData'][m]['title'] for m in range(0, 42)]
    logging.info('字典文件读取完成，已经提取url为列表%s, title为列表%s', str(json_list), str(name_list))
    return json_list, name_list


def save_img(url_list, name_list, output_path='result'):
    """
    将列表中的链接下载并保存为图像
    :param url_list:
    :return:
    """
    exists(output_path) or makedirs(output_path)
    for url, name in zip(url_list, name_list):
        logging.info(f'正在访问图像{url}')
        response = requests.get(url, stream=True)
        picture_name = f"{output_path}{name}.jpg"
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            image.save(picture_name)
            logging.info(f'保存{picture_name}图像成功')
        else:
            logging.info(f"Unable to retrieve the image. Status code: {response.status_code}")



save_path = "picture/"
json_name = save_json()
json_dict = read_json(json_name)
json_list, name_list = read_dict(json_dict)
save_img(json_list, name_list, save_path)

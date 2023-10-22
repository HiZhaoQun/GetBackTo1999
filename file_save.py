import json
import logging
import os
import requests

logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(levelname)s: %(message)s')


def json_to_dict(json_file):
    logging.info(f"正在打开文件{json_file}")
    with open(json_file, 'r', encoding='utf-8') as file:
        data_dict = json.load(file)
    logging.info(f"读取文件{json_file}成功，已经转换为{str(data_dict)[:50]}...")
    return data_dict


def save_image(url, save_path, detail_name):
    os.path.exists(save_path) or os.makedirs(save_path)
    logging.info(f"正在访问{url}中")
    response = requests.get(url=url)
    with open(f"{save_path}/{detail_name}", "wb", encoding='UTF-8') as file:
        file.write(response.content)
    logging.info(f"访问{url}成功，已保存{detail_name}文件")


def save_video(url, save_path, detail_name):
    os.path.exists(save_path) or os.makedirs(save_path)
    logging.info(f"正在访问{url}中")
    response = requests.get(url, stream=True)
    with open(f"{save_path}/{detail_name}", "wb", encoding='UTF-8') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
    logging.info(f"访问{url}成功，已保存{detail_name}文件")


def save_music(url, save_path, detail_name):
    os.path.exists(save_path) or os.makedirs(save_path)
    logging.info(f"正在访问{url}中")
    response = requests.get(url)
    with open(f"{save_path}/{detail_name}", "wb", encoding='UTF-8') as file:
        file.write(response.content)
    logging.info(f"访问成功，已保存{detail_name}文件")


def save_json(data_dict, save_path, detail_name):
    os.path.exists(save_path) or os.makedirs(save_path)
    with open(f'{save_path}/{detail_name}', 'w', encoding='utf-8') as file:
        json_str = json.dumps(data_dict, indent=4, ensure_ascii=False)
        file.write(json_str)
    logging.info(f'json文件{detail_name}保存成功')


def save_file(url, save_path, detail_name):
    os.path.exists(save_path) or os.makedirs(save_path)
    logging.info(f"正在访问{url}中")
    response = requests.get(url, stream=True)
    with open(f"{save_path}/{detail_name}", "wb") as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
    logging.info(f"访问{url}成功，已保存{detail_name}文件")


def save_txt(string, save_path, detail_name):
    os.path.exists(save_path) or os.makedirs(save_path)
    logging.info(f"正在保存{detail_name}中")
    with open(f"{save_path}/{detail_name}", "w", encoding='utf-8') as file:
        file.write(string)
    logging.info(f'保存{detail_name}成功')


logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(levelname)s: %(message)s')

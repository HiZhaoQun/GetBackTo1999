import logging
import requests
import json
from Functions import file_save


def get_json(url, header, data, save_path, detail_name):
    json_data = json.dumps(data)
    logging.info(f'正在访问{url}中')
    response = requests.post(url=url, headers=header, data=json_data)
    logging.info(response.text)
    dic = eval(response.text.replace('null', '''\"null\"'''))
    logging.info(dic)
    file_save.save_json(dic, save_path, detail_name=detail_name)
    logging.info(f'文件{detail_name}保存成功')


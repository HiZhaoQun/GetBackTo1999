from concurrent.futures import ThreadPoolExecutor
from Functions.file_save import *
from Functions.get_ajax_json import get_json
from Functions.get_now_date import get_date
from Functions.tail import get_url_tail_name, get_tail_type


# def save_dict(data_dict):
#     """
#     解析字典元素，调用相关函数
#     :param data_dict:
#     :return:
#     """
#     picture_form = '.jpg'
#     video_form = '.mp4'
#     title = data_dict['title']
#     video_name = title + '_video' + video_form
#     bigcover_name = title + '_bigcover' + picture_form
#     smallcover_name = title + '_smallcover' + picture_form
#     mobilethumbnail_name = title + '_mobilethumbnail' + picture_form
#     _date = get_date()
#     single_save_path = f'视频/单独视频{_date}/' + title
#     total_path = '视频/总视频/'
#     save_video(data_dict['videoUrl'], single_save_path, video_name)
#     save_video(data_dict['videoUrl'], total_path, video_name)
#     save_image(data_dict['bigCoverUrl'], single_save_path, bigcover_name)
#     save_image(data_dict['smallCoverUrl'], single_save_path, smallcover_name)
#     save_image(data_dict['mobileThumbnailUrl'], single_save_path, mobilethumbnail_name)


def run_get_json():
    _url = 'https://re.bluepoch.com/activity/official/websites/video/query'
    _data = {"id": "", "collectionId": "", "current": 1, "pageSize": 999}
    _header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
        "Content-Type": "application/json; charset=utf-8",

    }
    _path = 'json文件'
    _date = get_date()
    get_json(_url, header=_header, data=_data, save_path=_path, detail_name=_date + 'query.json')
    return _path + '/' + _date + 'query.json'


def deal_json_dict(_json_dict):
    """
    将传入的单个json数据提取其中的url并命名url为文件名
    :param _json_dict: 传入的json文件
    :return:
    """
    videoUrl = _json_dict['videoUrl']
    bigCoverUrl = _json_dict['bigCoverUrl']
    smallCoverUrl = _json_dict['smallCoverUrl']
    mobileThumbnailUrl = _json_dict['mobileThumbnailUrl']

    _urls_dict = {
        get_url_tail_name(videoUrl): videoUrl,
        get_url_tail_name(bigCoverUrl): bigCoverUrl,
        get_url_tail_name(smallCoverUrl): smallCoverUrl,
        get_url_tail_name(mobileThumbnailUrl): mobileThumbnailUrl,
    }

    _info_dict = {
        'title': _json_dict['title'],
        'desc': _json_dict['desc'],
        'json': _json_dict,
    }
    dealed_dict = {
        '_info_dict': _json_dict,
        '_urls_dict': _urls_dict,
    }
    return dealed_dict


def save_dict(_data_dict):
    """
    save dict url and other information
    :param _data_dict: need save dict
    :return:
    """
    _urls_dict = _data_dict['_urls_dict']
    _info_dict = _data_dict['_info_dict']
    path = '视频'
    title = _info_dict['title']
    date = get_date()
    for name in _urls_dict:
        save_file(_urls_dict[name], save_path=f'{path}/单独视频{date}/{title}', detail_name=name)
        if get_tail_type(name) == '.mp4':
            save_file(_urls_dict[name], save_path=f'{path}/总视频', detail_name=name)

    save_json(_info_dict['json'], f'{path}/单独视频{date}/{title}', 'info.json')
    save_txt(_info_dict['desc'], f'{path}/单独视频{date}/{title}', 'desc.txt')


def run_single(_datas_dict):
    dealed_dict = deal_json_dict(_datas_dict)
    save_dict(dealed_dict)

m_json_name = run_get_json()
json_dicts = json_to_dict(m_json_name)
data_dicts = json_dicts['data']['pageData']
total = json_dicts['data']['total']

# 创建一个线程池，最大线程数为10

with ThreadPoolExecutor(max_workers=total) as executor:
    # 使用map方法将访问网页的任务提交给线程池
    results = executor.map(run_single, data_dicts)

logging.info('运行完成')

import re


def get_url_tail_name(_url):
    """
    get url tail name and return file name
    :param _url: string type
    :return:
    """
    _tail_name = re.match('.*/(.*)', _url).group(1)
    return _tail_name


def get_tail_type(_tail_str):
    """
    get file type
    :param _tail_str:string type
    :return: file type
    """
    _tail_type = re.match('.*(\..*)', _tail_str).group(1)
    return _tail_type

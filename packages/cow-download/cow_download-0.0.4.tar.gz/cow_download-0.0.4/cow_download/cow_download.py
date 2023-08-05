# Created by Xiyou at 2022/7/19
# https://gitee.com/txbhandsome/DownloadKit
from DownloadKit import DownloadKit
import os

dirname = os.path.dirname(__file__)
attrs = ['_block_size', '_connect', '_download', '_file_exists',
 '_get_usable_thread', '_goal_path', '_interval', '_lock',
  '_log_mode', '_logger', '_missions', '_missions_num',
   '_page', '_print_mode', '_retry', '_roads', '_run',
    '_run_or_wait', '_session', '_show', '_stop_printing',
     '_stop_show', '_threads', '_timeout', '_waiting_list',
      '_when_mission_done', 'add', 'block_size', 'cancel',
       'file_exists', 'get_failed_missions', 'get_mission',
        'goal_path', 'interval', 'is_running', 'retry', 'roads',
         'session', 'set_log', 'set_print', 'set_proxies', 'show',
          'show_errmsg', 'timeout', 'wait', 'waiting_list']
# 创建下载器对象
d = DownloadKit()
# 线程数
d.roads = 20
# 大文件分块大小，默认 20MB
d.block_size = '50M'
# 设置文件保存路径
d.global_path = dirname
# 设置重试次数
d.retry = 5
# 设置失败重试间隔，初始 5
d.interval = 5
# 设置存在文件名冲突时的处理方式 skip overwrite rename
d.file_exists = 'rename'

"""
add(file_url, goal_path, rename, file_exists, post_data, split, kwargs)
file_url：文件网址
goal_path：保存路径
rename：重命名的文件名
file_exists：遇到同名文件时的处理方式，可选'skip','overwrite','rename'，默认跟随实例属性
post_data：post 方式使用的数据
split：是否允许多线分块下载
kwargs：连接参数，与 requests 的参数使用方法一致
# get 方式
mission = d.add(url)
# post 方式
d.add(url, json=data)
d.add(url, data=data)
"""

"""
d = DownloadKit(r'.\files', size=3)
url = 'https://example.com/file/abc.zip'
mission = d.add(url)
d.show()
"""


import os
import re
import sys
import time

import requests

HOST = 'https://cowtransfer.com'
SUCCESS_CODE = '0000'


def get_unique_url(download_code):
    url = f"{HOST}/core/api/transfer/share/precheck?downloadCode={download_code}"
    response = requests.get(url).json()
    if response['code'] != SUCCESS_CODE:
        raise BaseException("获取uniqueUrl失败")
    return response['data']['uniqueUrl']


def get_permission_info(unique_url):
    url = f"{HOST}/core/api/transfer/share/precheck?uniqueUrl={unique_url}"
    response = requests.get(url).json()
    if response['code'] != SUCCESS_CODE:
        raise BaseException("获取权限信息失败")
    if response['data']['needPassword']:
        raise BaseException("不支持加密文件下载")
    return response


def get_file_details(unique_url):
    url = f"{HOST}/core/api/transfer/share?uniqueUrl={unique_url}"
    response = requests.get(url).json()
    if response['code'] != SUCCESS_CODE:
        raise BaseException("获取文件详情失败")
    file_details = response['data']['firstFile']
    return {
        'title': file_details['file_info']['title'],
        'format': file_details['file_info']['format'],
        'size': file_details['file_info']['size'],
        'file_id': file_details['id'],
        'guid': response['data']['guid']
    }


def get_download_url(file_details):
    url = f"{HOST}/core/api/transfer/share/download?transferGuid={file_details['guid']}&title={file_details['title']}&fileId={file_details['file_id']}"
    response = requests.get(url).json()
    if response['code'] != SUCCESS_CODE:
        raise BaseException("获取下载URL失败")
    return response['data']['downloadUrl']


def get_file_name(file_details):
    return file_details['title'] + "." + file_details['format']


def process_bar(num, total):
    rate = float(num) / total
    rate_num = int(100 * rate)
    r = '\r[{}{}]{}%'.format('*' * rate_num, ' ' * (100 - rate_num), rate_num)
    sys.stdout.write(r)
    sys.stdout.flush()


def download_file(unique_url, target=None):
    # unique_url = get_unique_url(download_code)
    get_permission_info(unique_url)
    file_details = get_file_details(unique_url)
    file_size = file_details['size']
    download_url = get_download_url(file_details)
    if target is None:
        # 保存在当前目录
        target = get_file_name(file_details)
    else:
        if os.path.exists(target) and os.path.isdir(target):
            if target.endswith(os.sep):
                target = target + get_file_name(file_details)
            else:
                target = target + os.sep + get_file_name(file_details)
        else:
            raise BaseException("saveDirectory 需要是一个已存在的目录")

    # 流式下载
    chunk_size = 2048
    download_size = 0
    progress_total = 100
    # response = requests.get(download_url, stream=True)
    d.add(download_url, stream=True)
    d.show()
    # with open(target, "wb") as target_file:
    #     for chunk in response.iter_content(chunk_size=chunk_size):
    #         if chunk:
    #             download_size += chunk_size
    #             target_file.write(chunk)
    #             if int(time.time()) % 2 == 0:
    #                 process_bar(int((download_size * 1.0 / file_size) * 100), progress_total)
    # process_bar(100, progress_total)
    # print(f"\ncomplete download, save to {target}")


def show_help():
    sys.stdout.write(
        'download file : python3 cowtransfer_download_helper_py3.py download ${downloadUniqueUrl} [saveDirectory]')
    sys.stdout.flush()


if __name__ == "__main__"
    """
    python3 download_cow.py download 380c74eaf66f46
    """
    arg_len = len(sys.argv)
    if arg_len <= 1:
        raise SyntaxError("不合法的参数，help显示帮助，download下载文件")
    command = sys.argv[1]
    if command == 'download':
        unique_url = None
        save_target = None
        if arg_len == 3:
            unique_url = sys.argv[2]
        elif arg_len == 4:
            unique_url = sys.argv[2]
            save_target = sys.argv[3]
        else:
            raise SyntaxError("不合法的参数个数")
        download_file(unique_url, save_target)
    elif command == 'help':
        show_help()
    else:
        raise SyntaxError("不合法的命令")

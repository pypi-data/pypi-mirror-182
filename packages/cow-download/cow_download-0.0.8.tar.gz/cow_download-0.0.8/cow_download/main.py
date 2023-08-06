import sys
from cow_download.cow_download import (
    show_help,
    download_file
)


def main():
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
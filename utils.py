import argparse
import os
import sys


def get_variable(params):
    result = []

    for param in params:
        local_value = os.environ.get(param)
        if local_value is not None:
            result.append(local_value)

    if len(result) == len(params):
        return result

    parser = argparse.ArgumentParser(description='这是一个命令行参数解析示例')
    for param in params:
        parser.add_argument(f'--{param}')
    args = parser.parse_args()
    for param in params:
        result.append(getattr(args, param))
    return result

    # local_name = os.environ.get(key)
    #
    # # 如果环境变量不存在，则从命令行参数中获取
    # if local_name is None:
    #     local_args = sys.argv
    #     if index != 0 and len(local_args) > index:
    #         local_name = local_args[index]
    #
    # if local_name is None:
    #     local_name = default
    #
    # return local_name


def filter_image_file(folder_dir):
    suffixes = ('.png', '.jpg', '.jpeg')
    return [f for f in folder_dir if f.endswith(suffixes)]

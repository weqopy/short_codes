# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'weqopy'
__datetime__ = '2018-02-28 21:10:58'


"""
从通过 'pip freeze > requirements.txt' 命令生成的 requiremens 文件中删除版本信息
delete versions of 'requiremens' file created by 'pip freeze > requirements.txt'
"""


results = []


def main():
    get_pure_requirements()
    remove_old_requirements()
    create_new_requirements()


def get_pure_requirements():
    with open('requirements.txt', 'r') as requirements_file:
        lines = requirements_file.readlines()
        for line in lines:
            index = line.index('=')
            result = line[:index]
            results.append(result)


def remove_old_requirements():
    import os
    os.remove('requirements.txt')


def create_new_requirements():
    with open('requirements.txt', 'w') as requirements_file:
        for result in results:
            requirements_file.write(result + '\n')


if __name__ == '__main__':
    main()

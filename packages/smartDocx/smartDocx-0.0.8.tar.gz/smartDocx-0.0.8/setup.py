"""
@File  : setup.py
@IDE   : PyCharm
@Author: Sanbom
@Date  : 2021/10/3
@Desc  : 
"""
# -*- coding: utf-8 -*-

# encoding: utf-8

from setuptools import setup, find_packages

"""
# 1.编译

python setup.py sdist bdist_wheel

# 2.上传
pip install twine(如未安装twine)
测试环境:python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
生产环境:python -m twine upload dist/*
"""
setup(
    name="smartDocx",  # egg包名
    version="0.0.8",
    description="smart docx",
    author="sanbom",
    author_email="sanbomsu1993@outlook.com",
    zip_safe=False,
    license='MIT',
    # 依赖包
    install_requires=[
        "xlrd>=1.2.0, <2",
        "numpy>=1.21.2",
        "openpyxl>=3.0.9",
        "pandas>=1.3.3",
        "pyecharts>=1.9.0",
        "pyecharts-snapshot>=0.2.0",
        "snapshot-phantomjs>=0.0.3",
        "python-docx>=0.8.11"
    ],
    # 包含src中所有的包,并排除一些特定的包
    packages=find_packages("src",
                           exclude=["*.tests", "*.tests.*"]),
    package_dir={"": "src"},  # 告诉setuptools在src目录下找包
    package_data={
        "": ["*.txt"],  # 任何包中含有txt的文件
        # "smartDocx": ["template/*.docx", "README.md"],  # demo包中data目录下的dat文件
        "smartDocx": [],  # demo包中data目录下的dat文件
    }
)

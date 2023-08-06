from distutils.core import setup
import setuptools
packages = ['txdpy']# 唯一的包名
setup(name='txdpy',
    version='4.5.1',
    author='唐旭东',
    packages=packages,
    package_dir={'requests': 'requests'},
    install_requires=[
        "lxml","mmh3","loguru","redis","requests","tqdm","lxpy","colorama","xlrd","pymysql","undetected_chromedriver","selenium"
    ])
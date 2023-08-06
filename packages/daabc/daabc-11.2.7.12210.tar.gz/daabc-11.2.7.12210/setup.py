from setuptools import setup

setup(
    name = 'daabc', 
    version = '11.2.7.12210', 
    description = 'DA2B C/CXX', 
    author = 'Little Deer Travel Copyright 2000-2022', 
    author_email = 'jzheng130@gmail.com',
    url = 'https://da2bc.org', 
    packages = ['pkgs'], 
    data_files = [('lib', ['/usr/local/lib/libdaabc.so.11.2.7', '/usr/local/lib/libdaabcxx.so.11.2.7']), ('include', ['/usr/local/include/daab_c_api.h', '/usr/local/include/daab_cxx_api.h'])]
)
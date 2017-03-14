#coding: utf-8
from setuptools import setup

setup(
    name = 'tickets',
    py_modules = ['tickets', 'stations', 'get_check_stations_data','format_data'],
    install_requires = ['requests', 'docopt', 'prettytable', 'colorama','pprint' ],
    entry_points = {
        'console_scripts':['tickets = tickets:cli']    
    }
)

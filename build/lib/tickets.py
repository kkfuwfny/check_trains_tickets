#coding: utf-8

#Original author:protream
#Reconstruction of the author:lv zengchuan
#Time:2017-03-14

"""命令行火车票查看器

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets 北京 上海 2016-10-10
    tickets -dg 成都 南京 2016-10-10
"""


from docopt import docopt
import requests
import get_check_stations_data #获取火车战查询数据
from stations import stations #导入车站和车站的字母代码
from pprint import pprint
#pprint(available_trains, indent = 10)
  
import format_data   #导入格式化程序

"""

cli()函数任务有三个：
1、读入用户输入的参数数据，并且分析
2、用户输入的参数合法之后，调用get_check_stations_data.get_check_stations_data(date , from_station, to_station)
   爬取数据，返回josn数据
3、调用return format_data.Format_trains_data(available_trains, options).pretty_print(),返回的是格式化的数据

"""

def cli():
    """command-line interface""" 
    arguments = docopt(__doc__)
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments['<date>']
    
    #获取参数
    options = ''.join([
        key for key, value in arguments.items() if value is True
    ])
    
    #获取火车站查询返回的数据
    get_data = get_check_stations_data.Get_check_stations_data(date, from_station, to_station)
    r = get_data.get_requests()
    available_trains = r.json()['data']

    print("您输入的时间、出发地和目的地分别是：") 
    pprint((date, arguments['<from>'], arguments['<to>']), indent = 10)
    return format_data.Format_trains_data(available_trains, options).pretty_print()
    
if __name__ == '__main__':
    print(cli())

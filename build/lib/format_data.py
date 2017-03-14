#coding: utf-8
"""
格式化并返回数据
"""
from prettytable import PrettyTable
from colorama import init,Fore
init()

class Format_trains_data:

    header = '车次 车站 时间 历时 一等 二等 软卧 硬卧 硬座 无座'.split()

    def __init__(self, available_trains, options):
        """查询到的火车班次集合

        :param available_trains: 一个列表, 包含可获得的火车班次, 每个
                                 火车班次是一个字典
        :param options: 查询的选项, 如高铁, 动车, etc...
        """
        self.available_trains = available_trains
        self.options = options

    def _get_duration(self, raw_train):
        duration = raw_train.get('lishi').replace(':', '小时') + '分'
        if duration.startswith('00'):
            return duration[4:]
        if duration.startswith('0'):
            return duration[1:]
        return duration

    @property
    def trains(self):
        for fraw_train in self.available_trains:
            raw_train =fraw_train.get('queryLeftNewDTO')
            if raw_train is not None and raw_train != '':
                train_no = raw_train['station_train_code']
                initial = train_no[0].lower()
                if not self.options or initial in self.options:
                #如果用户没有输入车次类型 或 initial是用户要查的车次类型，就执行。
                #用户没输入，默认查全部的。
                    train = [
                        train_no,        
                        '\n'.join( [Fore.GREEN + raw_train['from_station_name'] + Fore.RESET,
                                  Fore.RED + raw_train['to_station_name'] + Fore.RESET]),
                        '\n'.join([Fore.GREEN + raw_train['start_time'] + Fore.RESET,
                                  Fore.RED + raw_train['arrive_time'] + Fore.RESET]),
                        self._get_duration(raw_train),
                        raw_train['zy_num'],
                        raw_train['ze_num'],
                        raw_train['rw_num'],
                        raw_train['yw_num'],
                        raw_train['yz_num'],
                        raw_train['wz_num'],
                    ]
                    yield train

    def pretty_print(self):
        pt = PrettyTable()
        pt._set_field_names(self.header)
        for train in self.trains:
            pt.add_row(train)
        #print(pt)
        return pt


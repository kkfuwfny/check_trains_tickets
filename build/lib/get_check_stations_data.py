#coding: utf-8

"""
查询站点之后，把返回的车站信息返回来
"""

import requests


class Get_check_stations_data(object):
    def __init__(self, date, from_station, to_station):
        self.from_station = from_station
        self.to_station = to_station
        self.date = date
        
    def get_requests(self):
        url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(self.date, self.from_station, self.to_station)
        #verify=false 参数不带验证书
        r = requests.get(url, verify = False)
        return r

if __name__ == '__main__':
    test_req = Get_check_stations_data("2017-03-15","GLZ","GZQ")
    res = test_req.get_requests()
    print (res)


一、使用方法两种，一个是:python3 ticket.py 广州 桂林 2017-03-15
另外一种是用setuptools安装过之后的，直接：ticket 广州 桂林 2017-03-15
详细看图片即可。


二、文件结构
1、ticket.py 是主要函数文件
2、get_check_stations_data.py 爬取数据的
3、format_data.py 格式化查询火车返回的信息，加颜色，边框等等
4、stations.py  这个保存的是火车的车站和对应的单词代表
5、search.py 这个是爬取数据的json格式
6、build，dist，ticksetsegg-info 三个文件夹是用python3 setup.py install产生的
7、__pycache__是python3执行产生的
8、parse_staion.py是爬取火车站和其对应的缩写字母.

9、setup.py 是用来打包的。python3 setup.py install



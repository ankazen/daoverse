import hashlib
import time
import datetime
import re
import calendar
import random
import json

def getMonthFirstDayAndLastDay(year=None, month=None):
    """
    :param year: 年份，默认是本年，可传int或str类型
    :param month: 月份，默认是本月，可传int或str类型
    :return: firstDay: 当月的第一天，datetime.date类型
              lastDay: 当月的最后一天，datetime.date类型
    """
    if year:
        year = int(year)
    else:
        year = datetime.date.today().year

    if month:
        month = int(month)
    else:
        month = datetime.date.today().month

    # 获取当月第一天的星期和当月的总天数
    firstDayWeekDay, monthRange = calendar.monthrange(year, month)

    # 获取当月的第一天
    firstDay = datetime.date(year=year, month=month, day=1)
    lastDay = datetime.date(year=year, month=month, day=monthRange)

    return firstDay, lastDay



def COL_desc(name, text, show=True):
    dic = {}
    dic['value'] = name
    dic['text'] = text
    dic['show'] = show
    return dic


def dt2tmp(dt):
    if not dt:
        return 0
    return time.mktime(dt.timetuple())


def datetimetoday():
    timestr = time.strftime("%Y-%m-%d 00:00:00", time.localtime())
    ts = time.mktime(time.strptime(timestr,"%Y-%m-%d %H:%M:%S"))
    dt = datetime.datetime.fromtimestamp(ts)
    return dt


def datetimetoday_str():
    timestr = time.strftime("%Y-%m-%d 00:00:00", time.localtime())
    return timestr

def jsDate_to_dt(jsdatestr):
    # /Date(1579054825636+0800)/ -》
    try:
        ts = jsdatestr.split('(')[1].split('+')[0]
    except:
        return None

    ts = int(ts)/1000
    dt = datetime.datetime.fromtimestamp(ts)
    return dt


def jsDate_to_dtstr(jsdatestr, fmt='time'):
    # /Date(1579054825636+0800)/ -》
    try:
        ts = jsdatestr.split('(')[1].split('+')[0]
    except:
        return None

    ts = int(ts)/1000
    dt = datetime.datetime.fromtimestamp(ts)
    if fmt == 'date':
        return dt.strftime("%Y-%m-%d")
    return dt.strftime("%Y-%m-%d %H:%M:%S")


P_TSP_Str = re.compile(r'/Date\(([0-9+]+)\)/')

def tspstr2dt(tspst):
    '''
    /Date(1568532913810)/ => datetime
    '''
    m = P_TSP_Str.match(tspst)
    if not m:
        return None
    tsp = m.groups()[0].split('+')[0]
    tsp = float(tsp)/1000

    dt = datetime.datetime.fromtimestamp(int(tsp))
    return dt


def tsp2dt(tsp):
    '''
    1568532913810 => datetime
    '''

    dt = datetime.datetime.fromtimestamp(int(tsp))
    return dt


def tsp2day(tsp):
    '''
    1568532913810 => datetime
    '''

    dt = datetime.datetime.fromtimestamp(int(tsp))
    return dt.isoformat()

def datetimesplit(datetimestr):
    spliter = '/'
    if '/' in datetimestr:
        spliter = '/'
    if '-' in datetimestr:
        spliter = '-'
    datestr, timestr = datetimestr.rsplit()
    yearstr, datestr = datestr.split(spliter, 1)
    yearstr = yearstr
    monthstr, datestr = datestr.split(spliter, 1)
    datestr = datestr
    return yearstr, monthstr, datestr, timestr


def datetimesplit2(datetimestr):
    spliter = '/'
    if '/' in datetimestr:
        spliter = '/'
    if '-' in datetimestr:
        spliter = '-'
    yearstr, monthstr, datestr = datetimestr.split(spliter)
    return yearstr, monthstr, datestr

def uuid():
    t = time.time()
    s = '%f.%02d' % (t, random.randint(1, 99))
    return s.replace('.', '-')

def make_token(data):
    # 把自动trans成md5
    # {'email':'ankazen@qq.com'} => xxxxxxxxxx
    kvs = []
    s = ''
    for k in data:
        kvs.append('%s=%s' % (k, data[k]))
    s += '&'.join(kvs)
    token = hashlib.sha224(s.encode('utf-8')).hexdigest()
    return token

def obj_to_dic(obj, attrs):
    dic = {}
    for attr in attrs:
        dic[attr] = getattr(obj, attr)
    return dic

class obj(object):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
               setattr(self, a, [obj(x) if isinstance(x, dict) else x for x in b])
            else:
               setattr(self, a, obj(b) if isinstance(b, dict) else b)


def str2json(s):
    s = s.replace('\t', '')
    s = s.replace('\n', '')
    s = s.replace(',}','}')
    s = s.replace(',]',']')
    s = s.replace('\'','\"')
    s = s.replace('False','false')
    s = s.replace('True','true')
    s = s.replace('None','null')
    data = json.loads(s)
    return data


def pager(lis, page, count):
    result = lis
    total_count = len(lis)
    if count != -1:
        result = lis[(page-1)*count:page*count]

    extend_dic = {
        'total': total_count,
        'page': page,
    }

    return result, extend_dic


if __name__ == '__main__':
    txt = '''
{'orderId': 13217040603, 'uid': '_M18922804999', 'distributionChannel': '', 'receiveTime': '2020-08-01 16:54:48', 'orderCreateTime': '2020-08-01 16:54:48', 'score': 43, 'travelNature': 'P', 'departure': '', 'destinations': '三亚', 'departureDate': '2099-12-31', 'returnDate': '2099-12-31', 'avgBudget': -1.0, 'budget': '无明确预算', 'personsDesc': '0成人，0儿童', 'adultNum': 0, 'childNum': 0, 'minPersons': 0, 'maxPersons': 0, 'contactor': '', 'contactorTel': '1895pbf4999', 'encryptMobile': '186519190', 'hostNum': '02180276688', 'orderType': 1, 'orderStatus': 2, 'originalOrderStatus': 20, 'orderStatusName': '待确认方案', 'processStatus': 2, 'provider': {'platformProviderID': 34117, 'platformUserID': '7cf7ae04-999d-4eee-bbaf-f5d499c7f0fc', 'providerName': '绿野国际旅行社（北京）有限公司 李骁驹', 'mobilePhone': '18201145003'}, 'inquiryID': 0, 'inquirySupplyID': 5906827, 'requireDetailID': 0, 'actualPrice': 0.0, 'receiveAmount': 0.0, 'orderVersion': '201710', 'orderTags': [], 'isSpecify': False, 'isMyOrder': False, 'schemeId': 23569455, 'cancelApplyType': 0, 'advisorId': 157323, 'productType': 0, 'productId': '', 'bizType': '', 'countryArea': 86, 'saleMode': 'R', 'schemeAuditStatus': 0, 'schemeAuditType': 0, 'timeZone': '', 'locale': '', 'site': 'CTRIP', 'userFirstCallTime': '/Date(1596275688141+0800)/', 'schemeOfferTime': '/Date(1596283050095+0800)/', 'budgetCurrency': '', 'splitType': 0, 'advisorPermissionId': 'DZXY002587'}
    '''
    print(str2json(txt))

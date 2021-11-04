import datetime
import sys


class Lunar(object):
    tg = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
    dz = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

    def __init__(self, dt=None):
        """ 初始化：参数为datetime.datetime类实例，默认当前时间  """
        self.localtime = dt if dt else datetime.datetime.today()
        self.year_gz = ''
        self.month_gz = ''

    def gz_year(self):  # 返回干支纪年

        year_g = self.g_year()
        n = self.localtime.year % 12

        year_z = ''
        if n > 3:
            year_z = self.dz[(n - 3) - 1]
        else:
            year_z = self.dz[(n - 3 + 12) - 1]
        self.year_gz = year_g + year_z
        return self.year_gz

    def g_year(self):
        n = self.localtime.year % 10
        year_g = ''
        if n > 3:
            year_g = self.tg[(n - 3) - 1]
        else:
            year_g = self.tg[(n - 3 + 10) - 1]
        return year_g

    def gz_month(self):  # 返回干支纪月
        month_gs = {
            '甲': ['丙', '丁', '戊', '己', '庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁'],
            '己': ['丙', '丁', '戊', '己', '庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁'],

            '乙': ['戊', '己', '庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁', '戊', '己'],
            '庚': ['戊', '己', '庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁', '戊', '己'],

            '丙': ['庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁', '戊', '己', '庚', '辛'],
            '辛': ['庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁', '戊', '己', '庚', '辛'],

            '丁': ['壬', '癸', '甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸'],
            '壬': ['壬', '癸', '甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸'],

            '戊': ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸', '甲', '乙', ],
            '癸': ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸', '甲', '乙', ],
        }
        month = self.localtime.month
        month_g = month_gs.get(self.g_year())[month - 1]
        month_z = self.dz[(month + 1) % 12]
        self.month_gz = month_g + month_z
        return self.month_gz

    def gz_day(self):  # 返回干支纪月
        month_gs = {
            '甲': ['丙', '丁', '戊', '己', '庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁'],
            '己': ['丙', '丁', '戊', '己', '庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁'],

            '乙': ['戊', '己', '庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁', '戊', '己'],
            '庚': ['戊', '己', '庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁', '戊', '己'],

            '丙': ['庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁', '戊', '己', '庚', '辛'],
            '辛': ['庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁', '戊', '己', '庚', '辛'],

            '丁': ['壬', '癸', '甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸'],
            '壬': ['壬', '癸', '甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸'],

            '戊': ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸', '甲', '乙', ],
            '癸': ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸', '甲', '乙', ],
        }
        month = self.localtime.month
        month_g = month_gs[self.g_year()][month - 1]
        month_z = self.dz[(month + 1) % 12]
        self.month_gz = month_g + month_z
        return self.month_gz

    def gz_day(self):
        ''''''
        # 月基数
        month_cn = {
            1: 0,
            2: 31,
            3: -1,
            4: 30,
            5: 0,
            6: 31,
            7: 1,
            8: 32,
            0: 3,
            10: 33,
            11: 4,
            12: 34

        }
        year = self.localtime.year
        month = self.localtime.month
        day = self.localtime.day
        s = (year % 100) - 1
        m = month_cn[month]
        if month == 2 and self.year_is_run(year):
            m += 1
        d = day
        x =
        r = (s // 4) * 6 + 5 * ((s // 4) * 3 + (s % 4)) + m + d + x

    def year_is_run(self, year):
        '''
        是否为闰年
        :param year:
        :return:
        '''
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

 庚申
金金



if __name__ == '__main__':
    ct0 = datetime.datetime(1993, 12, 1, 20, 50, 15)
    # ct1 = datetime.datetime(1988, 12, 26, 23, 6, 15)
    # ct2 = datetime.datetime(2019, 3, 2, 19, 6, 15)
    lunr = Lunar(ct0)
    print(lunr.gz_year())
    print(lunr.gz_month())
    # ba_zi(ct1)
    # ba_zi(ct2)

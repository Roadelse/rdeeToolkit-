#coding=utf-8

# ................. standard lib
import os
import os.path
import logging

import unittest
import inspect
from collections import OrderedDict

from rdee import rmrf


# ................. project lib
# ................. 3rd libs



class ISetup:
    """
    Interface class implementing general setUpClass & setUp methods for the belowing TestCases
    """
    @classmethod
    def setUpClass(cls) -> None:
        from rdee import rmrf
        os.chdir(utest_dir)
        cls.testDir: str = os.path.abspath(cls.__name__[5:])

        os.makedirs(cls.testDir)
        os.chdir(cls.testDir)

        print(f"\n***************************************************")
        print(f"TestCase: {cls.__name__[5:]}")
        print(f"***************************************************")

    def setUp(self) -> None:
        """
        print start information via puer print()
        &
        prepare test directory and enter it
        """
        from .. import rmrf

        # mid = '.'.join(self.id().split(".")[-2:])
        mid = self.id().split(".")[-1]

        print(f">>>>> test method: {mid} <<<<<")
        
        #@sk <get-path/>
        os.chdir(self.__class__.testDir)
        _, funcname = self.id().split(".")[-2:]
        self.testDir: str = f"{funcname[5:]}"

        #@sk <os-operation desc="mkdir -> rm -rf -> cd, and store the current working directory"/>
        os.makedirs(self.testDir)
        os.chdir(self.testDir)


# class TestPrior(unittest.TestCase):
#     def setUp(self):
#         print(f"\nRunning test: {self.id()}")

#     def test_dim_xxx_label_n(self):
#         # test : dim_xxx_label_n, dim_xxx_n, get_unique_values_1d_stable
#         import numpy as np

#         data1 = np.array([1,2,3,4,5,6,7,8,9,10])
#         labels1 = [0,0,0,1,1,1,2,2,3,4]
#         labels1B = np.array([4, 0,0,0,1,1,1,2,2,3])

#         res1 = rdee.dim_xxx_label_n(data1, labels1B, 0, "sum")
#         print(res1)

#         # data2 = data1.reshape(2, 5)
#         # labels2 = ["a", "b", "b", "c", "d"]
#         # res2 = rdee.dim_xxx_label_n(data2, labels2, 1, "sum")
#         # print(data2)
#         # print(res2)

#         # data3 = np.arange(16).reshape(4,2,2)
#         # labels3 = ["a", "b", "b", "c"]
#         # res3 = rdee.dim_xxx_label_n(data3, labels3, 0, "sum")
#         # print(data3)
#         # print(res3)


#     def test_month2season(self):
#         import numpy as np

#         ms = [1,2,3,4,5,6,7,8,9,10,11,12]

#         res = rdee.month2season(ms, {'outMode' : "str"})

#         print(res)

#     def test_dim_xxx_m2s_n(self):
#         yms = ["201701", "201702", "201703", "201704", "201705", "201706", "201707", "201708", "201709", "201710", "201711", "201712"]
#         data = [1,2,3,4,5,6,7,8,9,10,11,12]

#         res = rdee.dim_xxx_m2s_n(data, 0, yms, "sum")
#         print(res)


#     def test_write_nc_var(self):
#         import netCDF4 as nc4
#         import numpy as np

#         ncf = nc4.Dataset('test/test_write_nc_var.nc', 'w')
#         rdee.write_nc_var(ncf, "test1", [1,2,3,4]) # (ncf, var, varName)
#         rdee.write_nc_var(ncf, "test3", ["q","a"]) 
#         rdee.write_nc_var(ncf, "test2", np.arange(16).reshape(2, 4, 2))


#         ncf.close()


#     def test_ind_eq_map(self):
#         import numpy as np
#         arrP = [1,2,3,4,5,6,7,8,9,10]
#         arrC = [2,4,7]

#         res = rdee.ind_eq_map(arrP, arrC)

#         print(type(res))
#         print(res)

#         res2 = rdee.ind_eq_map(arrP, np.array(arrC))
#         print(type(res2))
#         print(res2)


#     def test_dim_xxx_cate_n(self):
#         # test : test_dim_xxx_cate_n, createSlice
#         import numpy as np

#         data1 = np.array([1,2,3,4,5,6,7,8,9,10,11])
#         labels1 = [0,0,0,1,1,1,2,2,3,4,1]
#         cates1 = [0, 1, 2, 3, 4]

#         res1 = rdee.dim_xxx_cate_n(data1, labels1, cates1, 0, "sum")
#         print(res1)

#         data2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
#         labels2 = [0,1,0,2,1]
#         cates2 = [0,1,2]
#         res2 = rdee.dim_xxx_cate_n(data2, labels2, cates2, 1, "sum")
#         print(res2)



#     def test_transform_time_reso_rtc(self):
#         import configPCS
#         import netCDF4 as nc4
#         import numpy as np

#         config = configPCS.GC({'case' : 'hist', 'tc' : 8})

#         f1 = nc4.Dataset(config['WRF_L1_DAILY_DATA'])
#         f2 = nc4.Dataset(config['WRF_L1_MONTHLY_DATA'])
#         f3 = nc4.Dataset(config['WRF_L1_SEASONAL_DATA'])
#         f4 = nc4.Dataset(config['WRF_L1_OMONTHLY_DATA'])
#         f5 = nc4.Dataset(config['WRF_L1_OSEASONAL_DATA'])

#         T2_f1 = f1.variables['T2'][:].filled(np.nan)
#         days = f1.variables['days'][:]
#         T2_f2 = f2.variables['T2'][:].filled(np.nan)
#         T2_f3 = f3.variables['T2'][:].filled(np.nan)
#         T2_f4 = f4.variables['T2'][:].filled(np.nan)
#         T2_f5 = f5.variables['T2'][:].filled(np.nan)

#         opt_ttrr = {}
#         opt_ttrr['method'] = "avg"
#         opt_ttrr['time_reso_dst'] = "monthly"
#         opt_ttrr['time_fmt_src'] = "%Y%m%d"

#         T2_f1_MONTHLY = rdee.transform_time_reso_rtc(T2_f1, 0, days, opt_ttrr)
#         print(np.sum(np.abs(T2_f1_MONTHLY['data'] - T2_f2)))

#         opt_ttrr['time_reso_dst'] = "seasonal"
#         T2_f1_SEASONAL = rdee.transform_time_reso_rtc(T2_f1, 0, days, opt_ttrr)
#         print(np.sum(np.abs(T2_f1_SEASONAL['data'] - T2_f3)))

#         opt_ttrr['time_reso_dst'] = "Omonthly"
#         T2_f1_OMONTHLY = rdee.transform_time_reso_rtc(T2_f1, 0, days, opt_ttrr)
#         print(np.sum(np.abs(T2_f1_OMONTHLY['data'] - T2_f4)))

#         opt_ttrr['time_reso_dst'] = "Oseasonal"
#         T2_f1_OSEASONAL = rdee.transform_time_reso_rtc(T2_f1, 0, days, opt_ttrr)
#         print(np.sum(np.abs(T2_f1_OSEASONAL['data'] - T2_f5)))


#     def test_xxx_inte(self):
#         import rdee
#         import numpy as np

#         data = np.array([1,2,3,4,5,6,7,8,9,10])
#         values = np.array([1,2,3,4,5,6,7,8,9,10])
#         method = "sum"
#         intervals = [[0, 3], [3, 6]]

#         print(rdee.xxx_inte(data, values, intervals, method))

#         intervals2 = [[0, 3], [[3, 6], [9, 10]]]

#         print(rdee.xxx_inte(data, values, intervals2, method))


#     def test_splitAsciiDef_singleTS(self):
#         print(rdee.splitAsciiDef_singleTS('A-C,G,Q-Z', '-', ','))


#     def test_split_by_true_sep(self):
#         s = "a,b,(c,d),e"

#         print(rdee.split_by_true_sep(s, ','))

        
# class TestArray(unittest.TestCase):
#     def setUp(self):
#         print(f"\nRunning test: {self.id()}")

#     def test_asplit(self):
#         a1 = list(range(10))
#         s1, s2 = _array.asplit(a1, (0.8, 0.2))
#         assert s1 == list(range(8))
#         assert s2 == list(range(8, 10))
#         s1, s2 = _array.asplit(a1, (0.8, 0.2), random=True)
#         assert s1 != list(range(8))


# class TestCode(unittest.TestCase):
#     def setUp(self):
#         print(f"\nRunning test: {self.id()}")

#     def test_get_submodules(self):
#         import numpy as np
#         sms = get_submodules(np)
#         self.assertTrue(len(sms) > 30)

#     def test_search_api(self):
#         import numpy as np
#         r = search_api(np, 'random')
#         self.assertTrue(len(r) == 3)

#     def test_reformat_comments(self):
#         """
#         Aims to test function:reformat_comments, mainly focusing on its runnability rather than correctness

#         @2024-01-06     init
#         """
        
#         content = """#!/bin/bash
# # <L1> l1 comments
# # <L2> l2 comments
# echo hello u
#     # <L3> l3 comments
# """
#         ctt_rc_lines = reformat_comments(content).splitlines()
#         self.assertEqual(len(ctt_rc_lines), 5)
#         self.assertTrue(ctt_rc_lines[-1].startswith('    #'))
#         self.assertGreater(len(ctt_rc_lines[1]), 40)
#         self.assertGreater(len(ctt_rc_lines[2]), 15)


class Test_Logging(ISetup, unittest.TestCase):
    """
    This class contains several test functions in relation with logging
    """
    # def tearDown(self) -> None:
    #     """
    #     Go back to original workding directory
    #     """
    #     print("\n\n\n")

    def test_getLogger(self):
        """
        This function aims to test getLogger in _x_logging module, which should first resolve selcted/default local logging config then return corresponding logger, and, if not matchable, return a new logger with default settings (but can also controlled a bit via argument)
        This function trying 3 loggers, the "root" and "test1" are defined in local logging.config, and "test2" are not. The consolve should print all information from the 3 loggers, and test1.log & test2.log would be written. While, the latter is checked using self.assert..., but the prior feature needs eyes to see.
        """

        #@sk import
        from .. import getLogger, getAllHandlers 

        #@sk prepare write a local logging.config
        with open("logging.config", "w") as f:
            f.write("""
[loggers]
keys=root,test1

[handlers]
keys=console1,file1

[formatters]
keys=fmtfile,fmtcsl

[filters]
keys=ft1

[logger_root]
level=INFO
handlers=console1
qualname=root

[logger_test1]
level=DEBUG
handlers=file1
qualname=test1
; if set to 0, test1 logger will not trigger root logger handlers
propagate=1

[handler_console1]
class=StreamHandler
level=DEBUG
formatter=fmtcsl
args=(sys.stdout,)

[handler_file1]
class=logging.handlers.RotatingFileHandler
level=DEBUG
formatter=fmtfile
args=('test1.log', 'a', 20000, 5)

[formatter_fmtfile]
format=%(asctime)s  (%(name)s)  [%(levelname)s]  %(message)s
datefmt=%Y-%m-%d %H:%M:%S

[formatter_fmtcsl]
format=\033[4m%(asctime)s \033[0m (\033[33m%(funcName)s\033[0m)  [\033[32m%(levelname)s\033[0m]  %(message)s
datefmt=%Y-%m-%d %H:%M:%S

""")

        #@sk prepare remove the getLogger.configured so it can load the created local config file
        delattr(getLogger, "configured")  #@sk because python -m package will still run the __init__.py statements, while the `logger = getLogger("rdee")` statement will try to load local config file (doesn't exist at that time) and marks it "configured" then.

        #@sk <do desc="do the core statements">
        #@sk <basic desc="test basic functionality" />
        logger = getLogger("root")
        logger1 = getLogger("test1")
        logger2 = getLogger("test2", fpath="test2.log")
        logger.info("info from root")
        logger1.info("info from test1")
        logger2.info("info from test2")
        #@sk <envfilter desc="test envfilter" />
        logger1.info("2nd info from test1")
        os.environ["reDebugTargets"] = "whoru"
        logger3 = getLogger("test3", fpath="test3.log")
        logger2.info("2nd info from test2")
        logger3.info("info from test3")
        #@sk </do>
    

        #@sk check
        self.assertTrue(os.path.exists("test1.log"))
        self.assertTrue(os.path.exists("test2.log"))
        self.assertTrue(os.path.exists("test3.log"))  #@sk log file will be created even no message passed

        self.assertEqual(2, len(open("test1.log").readlines()))
        self.assertEqual(2, len(open("test2.log").readlines()))
        self.assertEqual("", open("test3.log").read())

    def test_logFilter(self):
        from .._o_globalstate import logger

        def f1():
            logger.info("in f1")
        
        def f2():
            logger.info("in f2")

        os.environ["reDebugTargets"] = "f1"

        logger.addHandler(logging.FileHandler("test_logFilter.log"))
        f1()
        f2()
        self.assertEqual("in f1\n", open("test_logFilter.log").read())




class Test_basicfunc(unittest.TestCase):
    def setUp(self) -> None:
        print(f"\n***************************************************")
        print(f"Running test: {self.id()}")
        print(f"***************************************************")
        return super().setUp()
    
    def test_singleton(self):
        """
        This function aims to test usage of singleton decorator
        """
        import random
        from .. import singleton

        @singleton
        class cc:
            def __init__(self):
                self.rvalue = random.random()

        ins1 = cc()
        ins2 = cc()
        self.assertEqual(ins1.rvalue, ins2.rvalue)


class Test_string(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_TrimSuffix(self):
        from .. import String

        ss = ["20240201105000", "20240201105100"]
        ssTrim = String.trim_suffix(ss)
        self.assertListEqual(["202402011050", "202402011051"], ssTrim)


class Test_time(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_get_time_str_and_scale(self) -> None:
        from datetime import datetime
        from .._x_time import Time
        ts1 = (
            datetime(2024, 2, 1, 11, 8, 14, 602249),
            datetime(2024, 2, 1, 11, 8, 15, 135897)
        )
        ts2 = (
            datetime(2024, 2, 1, 11),
            datetime(2021, 2, 1, 13)
        )

        ts1_str = Time.get_time_str_and_scale(ts1)
        self.assertListEqual(["20240201110814", "20240201110815"], ts1_str)
        ts2_str = Time.get_time_str_and_scale(ts2)
        self.assertListEqual(["2024020111", "2021020113"], ts2_str)

    def test_get_days_from_ym(self) -> None:
        from .._x_time import Time
        self.assertEqual(29, Time.get_days_from_ym("2016", "02"))
        self.assertEqual(31, Time.get_days_from_ym("2018", 12))
        with self.assertRaises(Exception):
            Time.get_days_from_ym("2018", 13)
    
    def test_countLeap(self) -> None:
        from .._x_time import Time

        self.assertEqual(0, Time.countLeap(1, 1))
        self.assertEqual(24, Time.countLeap(1, 100))
        self.assertEqual(1, Time.countLeap(100, 104))
        self.assertEqual(1, Time.countLeap(-104, -100))
        self.assertEqual(48, Time.countLeap(-100, 100))
        self.assertEqual(97, Time.countLeap(1, 400))
        self.assertEqual(121, Time.countLeap(-400, 100))
        self.assertEqual(121, Time.countLeap(-100, 400))
        self.assertEqual(122, Time.countLeap(-104, 400))
        self.assertEqual(121, Time.countLeap(-104, 400, False))
        self.assertEqual(122, Time.countLeap(-104, 402))
        self.assertEqual(122, Time.countLeap(-105, 401, False, False))

    def test_get_jdays(self) -> None:
        from .._x_time import Time

        self.assertEqual(1, Time.get_jdays(1,1,2014))


class Test_redtime(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_init(self) -> None:
        from .._xx_redtime import freetime

        ft1: freetime = freetime(1, 3, 5, 7, 9)
        self.assertEqual(1, ft1.year)

    def test_freetime_sim(self) -> None:
        from .._xx_redtime import freetime

        ft1: freetime = freetime(0, 0)
        ft1.sim()
        self.assertEqual(0, ft1.year)
        self.assertEqual(0, ft1.month)

        ft2: freetime = freetime(-1, -1)
        ft2.sim()
        self.assertEqual("-2/11/0 0:0:0", str(ft2))

        ft3: freetime = freetime(-1, 24, 796, 61, 59, 61)
        ft3.sim()
        self.assertEqual("1/0/798 14:0:1", str(ft3))

        ft4: freetime = freetime(0, -12, 1, -1, 1, -3661)
        ft4.sim()
        self.assertEqual("-1/0/0 21:59:59", str(ft4))

    def test_freetime_count(self) -> None:
        from .._xx_redtime import freetime
        ft1 = freetime(-1, -1, -1, -1, -1, -1)
        self.assertEqual(-13, ft1.months)
        self.assertEqual(-2, ft1.years)
        self.assertEqual(-2, ft1.days)
        self.assertEqual(-26, ft1.hours)
        self.assertEqual("-1/-1/-1 -1:-1:-1", str(ft1))
        ft1.sim()
        self.assertEqual("-2/11/-2 22:58:59", str(ft1))

    def test_freetime_add_sub(self) -> None:
        from .._xx_redtime import freetime

        ft1: freetime = freetime(-1, 1, -1, 1, -1, 1) + freetime(1, -1, 1, -1, 1, -1)
        self.assertEqual("0/0/0 0:0:0", str(ft1))
        self.assertEqual("1/1/1 2:2:2", str(ft1.add(freetime(1,1,1,2,2,2))))
        self.assertEqual("-1/0/0 1:1:1", str(ft1.sub(freetime(2,1,1,1,1,1))))

    def test_realtime_basic(self) -> None:
        from .._xx_redtime import realtime, realevel

        rt1 = realtime(2024, 2, 5, 11, 4, 59)
        self.assertEqual(realevel.SECOND, rt1.timescale)

        rt2 = realtime(2024, 2, 5)
        self.assertEqual(realevel.DAY, rt2.timescale)
        self.assertEqual(realevel.HOUR, rt2.set_hour(11).timescale)
        with self.assertRaises(Exception):
            rt2.set_second(58)
        
        rt3 = realtime(2024)
        self.assertEqual(realevel.YEAR, rt3.timescale)
        self.assertEqual("2024", str(rt3))
        rt3.set_month(2).set_day(28).set_hour(11).set_minute(58)
        self.assertEqual("2024/2/28 11:58", str(rt3))


        rt4 = realtime(2024, 2, 4, 14, 45, 59)
        rt4.sim()  #@ exp | redundant operation
        self.assertEqual("2024/2/4 14:45:59", str(rt4))
        
        with self.assertRaises(Exception):
            rtx = realtime(2024, 2, 4, 14, 45, 60)

    def test_realtime_stamp(self) -> None:
        from .._xx_redtime import freetime, realtime, realevel

        rt1 = realtime(1, 1, 1, 1, 1, 1)
        self.assertEqual(1, rt1.years)
        self.assertEqual(1, rt1.months)
        self.assertEqual(1, rt1.days)
        self.assertEqual(3661, rt1.stamp)
        self.assertEqual(62135596800, realtime(1970, 1, 1, 00, 00, 00).stamp)
        self.assertEqual(63554975914, realtime(2014, 12, 23, 23, 58, 34).stamp)

        self.assertEqual(2014, realtime(2014).stamp)
        self.assertEqual(36, realtime(3, 12).stamp)
        self.assertEqual(1068, realtime(3, 12, 4).stamp)
        self.assertEqual(1067 * 24 + 10, realtime(3, 12, 4, 10).stamp)

    def test_realtime_op(self) -> None:
        from .._xx_redtime import freetime, realtime, realevel

        rt1 = realtime(2024, 2, 4, 14, 45, 59)
        rt2 = rt1 + freetime(month=-20)
        self.assertEqual("2022/6/4 14:45:59", str(rt2))

        rt3 = rt1 + freetime(-1, 0, 25, 0, -1, 1)
        self.assertEqual("2023/3/1 14:45:0", str(rt3))
        rt3B = rt1 + freetime(0, 0, 25, 0, -1, 1)
        self.assertEqual("2024/2/29 14:45:0", str(rt3B))

        rt4 = rt1 + freetime(0, 0, 0, 1234, 5678, 9101112)
        self.assertEqual("2024/7/14 7:29:11", str(rt4))

        rt5: realtime = freetime(0, 0, -1234, -5678, -9101112, -13141516) + rt1
        self.assertTrue(isinstance(rt5, realtime))
        self.assertEqual("2002/5/7 17:8:43", str(rt5))

        ft1 = rt1 - realtime(2024, 2, 4, 14, 46, 0)
        self.assertEqual("0/0/0 0:0:-1", str(ft1))

        ft2 = realtime(2024, 2, 4) - realtime(2023, 2, 4)
        self.assertEqual("0/0/365 0:0:0", str(ft2))

    def test_realtime_op2(self) -> None:
        """
        Scaled +-
        """
        from .._xx_redtime import freetime, realtime, realevel

        rt1 = realtime(2024)
        rt2 = rt1 + freetime(-1, 300)
        self.assertEqual("2023", str(rt2))
        self.assertEqual(-1, rt2.month)

        rt3: realtime = realtime(2024, 2, 4, 0, 1) - freetime(0, 0, 0, 0, 0, 3600)
        self.assertEqual("2024/2/4 0:1", str(rt3))

    def test_realtime_rebase(self) -> None:
        from .._xx_redtime import freetime, realtime, realevel, realtimeseries

        rt1 = realtime(2014)
        rt2 = rt1.rebase(realevel.MONTH)
        self.assertEqual(realevel.MONTH, rt2.timescale)
        self.assertEqual("2014/1", str(rt2))
        rt3 = rt2.rebase(realevel.HOUR)
        self.assertEqual(realevel.HOUR, rt3.timescale)
        self.assertEqual("2014/1/1 0", str(rt3))

        rt3.rebase(realevel.SECOND, inplace=True)
        self.assertEqual("2014/1/1 0:0:0", str(rt3))

    def test_realtime_rebase2rts(self) -> None:
        from .._xx_redtime import freetime, realtime, realevel, realtimeseries

        rt1 = realtime(2014)

        rts1: realtimeseries = rt1.rebase2rts(realevel.MONTH)
        self.assertEqual(12, len(rts1.rts))
        self.assertEqual(realevel.MONTH, rts1.timescale)
        self.assertEqual("2014/1", str(rts1.rts[0]))
        self.assertEqual("2014/6", str(rts1.rts[5]))
        self.assertEqual("2014/12", str(rts1.rts[-1]))

        rts2: realtimeseries = rt1.rebase2rts(realevel.HOUR)
        self.assertEqual(8760, len(rts2.rts))
        self.assertEqual(realevel.HOUR, rts2.timescale)
        self.assertEqual("2014/1/1 0", str(rts2.rts[0]))
        self.assertEqual("2014/12/31 23", str(rts2.rts[-1]))

        rt4 = realtime(2024, 2, 6)
        rts3: realtimeseries = rt4.rebase2rts(realevel.SECOND)
        self.assertEqual(86400, len(rts3.rts))
        self.assertEqual(realevel.SECOND, rts3.timescale)
        self.assertEqual("2024/2/6 0:0:0", str(rts3.rts[0]))
        self.assertEqual("2024/2/6 23:59:59", str(rts3.rts[-1]))


    def test_realtimeseries_init(self) -> None:
        from .._xx_redtime import realtimeseries, realtime, freetime
        rts1 = realtimeseries(realtime(2014), realtime(2024), freetime(1))
        self.assertEqual(11, len(rts1.rts))
        self.assertEqual("2014", str(rts1.rts[0]))
        self.assertEqual("2024", str(rts1.rts[-1]))
        self.assertEqual("2023", str(rts1.rts[-2]))

        rts1B = realtimeseries(realtime(2014), realtime(2024))
        self.assertEqual(11, len(rts1B.rts))
        self.assertEqual("2014", str(rts1B.rts[0]))
        self.assertEqual("2024", str(rts1B.rts[-1]))
        self.assertEqual("2023", str(rts1B.rts[-2]))

        rts2 = realtimeseries(realtime(2024, 1, 1), realtime(2024, 12, 31))
        self.assertEqual(366, len(rts2.rts))
        self.assertEqual("2024/1/1", str(rts2.rts[0]))
        self.assertEqual("2024/12/31", str(rts2.rts[-1]))
        self.assertEqual("2024/12/30", str(rts2.rts[-2]))


class Test_array(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_drp(self):
        """
        This function aims to test Array.drp, including test items:
            ● Array.drp(arr1, dims=1, op=DRPC.max)
                test basic functionality
            ● Array.drp(arr1, dims=2, op=DRPC.min, mapping=...)
                test basic mapping
        """

        import numpy as np  #@ wait!! to be optimized, in checking if with numpy or not
        from .._x_array import Array, DRPC  #@sk import

        arr1 = np.arange(24).reshape((2,3,4))
        arr1_drp = Array.drp(arr1, dims=1, op=DRPC.max)
        self.assertListEqual([8,9,10,11,20,21,22,23], arr1_drp.reshape(-1).tolist())  #@sk reference list is set manually

        arr1_drp = Array.drp(arr1, dims=2, op=DRPC.min, mapping={0:[2,3], 1:[0, 1]})
        self.assertListEqual([2,0,6,4,10,8,14,12,18,16,22,20], arr1_drp.reshape(-1).tolist())  #@sk reference list is set manually

    def test_unique_with_mapping(self) -> None:
        from .._x_array import Array

        vseq = [1,1,2,2,3,3,3,1]
        self.assertDictEqual(OrderedDict([(1, (0,1)), (2, (2,3)), (3, (4,6)), (1, (7, 7))]), Array.unique_with_mapping(vseq))


class Test_win(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_path2ww(self) -> None:
        from  rdee import path2wsl, path2win
        self.assertEqual("/mnt/d/recRoot/Roadelse/Life/Daily", path2wsl(r"D:\recRoot\Roadelse\Life\Daily"))
        self.assertEqual(r"D:\recRoot\Roadelse\Life\Daily", path2win(r"/mnt/d/recRoot/Roadelse/Life/Daily"))
        
        with self.assertRaises(Exception):
            path2wsl(r"D:\recRoot\Roadelse\Life\Daily\ababa", require_existed=True)
        with self.assertRaises(Exception):
            path2win(r"/mnt/g/recRoot/Roadelse/Life/Daily", require_existed=True)
        with self.assertRaises(Exception):
            path2win(r"D:\recRoot\Roadelse\Life\Daily\ababa", require_existed=True)
        with self.assertRaises(Exception):
            path2wsl(r"/mnt2/d/recRoot/Roadelse/Life/Daily", require_existed=True)


def run(targets: list[str], remainTest: bool) -> None:
    """
    Runner for the test cases & test functions in this utest packaghe
    Support both TestCase-Level and test_function-level selections, automatically get target TestCases/test-functions and load them into a suite, finally run the suite
    :param targets: a list fo targets to be tested, if empty, run all the tests
    """
    global utest_dir

    #@sk <prepare desc="get all TestCases and TestFunctions in two dictionaries"/>
    allTestCases = {}
    for k, v in globals().items():
        if inspect.isclass(v) and issubclass(v, unittest.TestCase):
            allTestCases[k] = v

    allTestFunctions = {}
    for k, tc in allTestCases.items():
        for mpf in dir(tc):
            if mpf.startswith("test_"):
                allTestFunctions[mpf] = (tc, mpf)

    #@sk <prepare desc="" />
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()

    #@sk <core desc="parse arguments to confirm target TestCases and TestFunctions">
    if not targets:  #@sk branch Handle param-boundary conditions that no targets are set
        target_tcs = list(allTestCases.values())
    else:  #@sk branch normal conditions
        target_tcs = []
        for tcn in targets:
            #@sk <classify desc="parsing 3 kinds of target: TestCase, TestFunction, and TestCase.TestFunction, prefix can be omitted">
            if '.' in tcn:  #@sk branch TestCase.TestFunction
                tcn_classname, tcn_methodname = tcn.split('.')
                tcn_classname = "Test_" + tcn_classname if not tcn_classname.startswith("Test_") else tcn_classname
                tcn_methodname = "test_" + tcn_methodname if not tcn_methodname.startswith("test_") else tcn_methodname

                v = globals().get(tcn_classname)
                if inspect.isclass(v) and issubclass(v, unittest.TestCase) and hasattr(v, tcn_methodname):  #@sk exp use STL:inspect to detect if a symbol denoting class
                    target_tcs.append((v, tcn_methodname))
            elif tcn in allTestCases or f"Test_{tcn}" in allTestCases:  #@sk branch TestCase
                tcn = "Test_" + tcn if not tcn.startswith("Test_") else tcn
                target_tcs.append(allTestCases[tcn])
            elif tcn in allTestFunctions or f"test_{tcn}" in allTestFunctions:  #@sk branch TestFunction
                tcn = "test_" + tcn if not tcn.startswith("test_") else tcn
                target_tcs.append(allTestFunctions[tcn])
            else:  #@sk branch error conditions
                raise RuntimeError(f"Error! Illegal test target, neither TestCase name nor TestFunction name! {tcn}")
            #@sk </classify>
    #@sk </core>


    #@sk <tail desc="run the target tests"/>
    # print(target_tcs)
    for tc in target_tcs:
        if isinstance(tc, tuple):
            suite.addTest(tc[0](tc[1]))  #@sk Here we actually instantiate the TestCase class, the function name is used to tell which function should be tested
        else:
            suite.addTest(loader.loadTestsFromTestCase(tc))
    
    utest_dir = os.path.abspath("ade.utest")
    rmrf(utest_dir)
    os.makedirs(utest_dir, exist_ok=True)
    os.chdir(utest_dir)
    runner.run(suite)
    if not remainTest:
        rmrf(utest_dir)

# encoding = utf-8
from Util import HTMLTestRunner
import time


class GenReport(object):

    def __init__(self):
        print("generate test reports...")

    def genreport(self, suite):

        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        filename = "D:\\seleniumWithPython\\ResultsReport\\Results-" + now + "result.html"
        print(filename)
        fp = open("F:\\automation\\Results\\Results-" + now + "result.html", 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Result', description='Test_Report')
        runner.run(suite)
        print('Test reports generate finished')



# encoding = utf-8
from selenium import webdriver


class GetTableVale(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"F:\automation\webdriver\chromedriver.exe")

    def get_table_value(self):
        self.driver.get(r"F:\seleniumWithPython\Foundations\toBeTest\radiochecbox.html")
        table = self.driver.find_element_by_id("table")
        trlist = table.find_elements_by_tag_name("tr")
        for row in trlist:
            tdlist = row.find_elements_by_tag_name("td")
            for col in tdlist:
                if col.text == "3000元":
                    col.click()
        self.driver.quit()


if __name__ == "__main__":
    gt = GetTableVale()
    gt.get_table_value()

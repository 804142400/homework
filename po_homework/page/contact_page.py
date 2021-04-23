from selenium.webdriver.common.by import By

from homework.po_homework import AddDepartmentPage
from homework.po_homework.page.basepage import BasePage


class ContactPage(BasePage):
    top_add_button = (By.CSS_SELECTOR, ".member_colLeft_top_addBtn")
    add_department_button = (By.CSS_SELECTOR, ".js_create_party")
    department_list = (By.CSS_SELECTOR, ".jstree-node.js_editable.jstree-leaf")

    def goto_add_department(self):
        """
        转跳添加部门页面
        :return:
        """
        self.find(self.top_add_button).click()
        self.find(self.add_department_button).click()
        return AddDepartmentPage(self.driver)

    def get_list(self):
        ele_list = self.driver.find_elements(By.CSS_SELECTOR, ".jstree-node.js_editable.jstree-leaf")
        name_list = [str.lstrip(i.text) for i in ele_list]
        return name_list





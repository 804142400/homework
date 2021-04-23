from selenium.webdriver.common.by import By

from homework.po_homework.page.basepage import BasePage


class AddDepartmentPage(BasePage):
    """
   添加部门页面
   """
    # 定义添加部门页面主要元素

    department_name_input = (By.CSS_SELECTOR, ".qui_inputText.ww_inputText:nth-child(2)")
    department_list = (By.CSS_SELECTOR, ".qui_btn.ww_btn.ww_btn_Dropdown.js_toggle_party_list")
    department_select = (By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id='1688850578238616_anchor']")
    save_btn = (By.CSS_SELECTOR, ".qui_dialog_foot.ww_dialog_foot > a.qui_btn.ww_btn.ww_btn_Blue")

    def add_department(self, new_department_name):
        """
        添加部门并保存
        :return:
        """
        # 使用局部引用，解决循环引用问题
        from homework.po_homework import ContactPage
        # 输入新增的部门名称
        self.find(self.department_name_input).send_keys(new_department_name)
        # 点击所属部门下拉选项，展开部门列表
        self.find(self.department_list).click()
        # 选择所属部门
        self.find(self.department_select).click()
        # 点击保存按钮
        self.find(self.save_btn).click()
        return ContactPage(self.driver)

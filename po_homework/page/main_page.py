
from selenium.webdriver.common.by import By
from homework.po_homework.page.basepage import BasePage
from homework.po_homework import ContactPage


class MainPage(BasePage):
    # 元素定位封装成了一个元祖
    contact_ele = (By.ID, "menu_contacts")

    def goto_contact(self):
        self.find(self.contact_ele).click()
        return ContactPage(self.driver)


    #     print(a, b)



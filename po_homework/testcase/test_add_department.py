import pytest

from homework.po_homework.page.main_page import MainPage


class TestAddDepartment:
    def setup_class(self):
        self.main = MainPage()

    @pytest.mark.parametrize("department_name", ["HR"])
    def test_add_department(self, department_name):
        """
        用来测试添加成员功能
        :return:
        """
        #    1. 跳转到添加成员页面 2. 添加成员 3. 获取成员列表，做断言验证
        # AddDepartment.Page()
        res = self.main.goto_contact().goto_add_department().add_department(department_name).get_list()
        print(res)
        assert 'HR' in res

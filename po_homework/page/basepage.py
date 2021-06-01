import shelve
from time import sleep

from selenium import webdriver


class BasePage:
    """
    封装页面通用方法，比如driver的实例化
    """

    def __init__(self, base_driver=None):
        """
        :param base_driver: 传入driver 实例对象
        """
        # 如果 base_driver 是初始值None，那么就会实例化driver
        if base_driver is not None:
            self.driver = base_driver
        else:
            # # 使用浏览器复用模式
            # chrome_arg = webdriver.ChromeOptions()
            # # 加入调试地址
            # chrome_arg.debugger_address = '127.0.0.1:9222'
            # # 实例化driver对象
            # self.driver = webdriver.Chrome(options=chrome_arg)
            self.driver = webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850481935123'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'h6QmevSJPRJUot_2hn8AoOJFH3NlOZfp6GP7Yc51QGr4tmQobTpS_7jG0TY4xlUOAXk6UjKXQiPzXdnju_X4Du6c1RbPdW9TP2oM7w2xjodMWfu8VYb5N6kvK7xwWRQo0GoE1Uft4nvhAbqzeGS15eJmPj6UrDHhMbAZEzpk62p6udxu7UXz-GMDeIrpMeJroTJXfnjToMAwwoBdzGpc5FgaEcaM1XQhX1s0iDbseS5kWBZx18QgdT-YbaRpPU9kNevHJtVCDCMuW2z96-nFnA'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850481935123'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325097443930'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': '9r-KGhPmw0CutucPTXb1FNNclheaxSV6q_j5vBjmUrLB6VGwdPNwMxMZP3eDzcHj'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a2264668'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '3367730842717632'}, {'domain': 'work.weixin.qq.com', 'expiry': 1618345459, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '2lqqsdi'}, {'domain': '.qq.com', 'expiry': 1618418724, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.6521649.1618226508'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1649849926, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1618228058,1618231569,1618234212,1618313927'}, {'domain': '.work.weixin.qq.com', 'expiry': 1620924327, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 1681404324, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.2009980336.1618067759'}, {'domain': '.work.weixin.qq.com', 'expiry': 1649603602, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1619610310, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '804142400'}, {'domain': '.qq.com', 'expiry': 2147483651, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '155fbb3075715e13aa181ff31621a2cebd9b969e2f390755940c7f091f406be5'}, {'domain': '.qq.com', 'expiry': 2147483659, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': '19QkhYI3tf'}, {'domain': '.qq.com', 'expiry': 1618332384, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '1221384192'}]

            db = shelve.open('./mydb/cookies')
            cookies = db['cookie']
            print(cookies)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            # 重新打开带有cookie信息的index页面
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            # 隐式等待，会在每次find 操作的时候，轮询查找该元素，超时报错
            self.driver.implicitly_wait(3)

    def find(self, locator):
        # 解元祖的操作
        return self.driver.find_element(*locator)

    # def test_cookie(self):
    #     cookies = self.driver.get_cookie()
    #     print(cookies)

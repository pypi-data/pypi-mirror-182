import qrunner


class HomePage(qrunner.Page):
    """APP首页"""
    ad_close = {'res_id': 'bottom_btn', 'desc': '首页广告关闭按钮'}
    my_entry = {'res_id': 'bottom_view', 'index': 3, 'desc': '首页底部我的入口'}

    def go_my(self):
        """进入我的页"""
        self.adr_elem(**self.ad_close).click()
        self.adr_elem(**self.my_entry).click()


class TestGoMyPOM(qrunner.TestCase):
    """进入我的页-pom模式代码"""

    def start(self):
        self.hp = HomePage(self.driver)

    def test_pom(self):
        self.hp.go_my()
        self.assert_in_page('我的服务')


class TestGoMyNormal(qrunner.TestCase):
    """进入我的页-过程模式代码"""

    def start(self):
        self.elem_close = self.adr_elem(res_id='bottom_btn', desc='首页广告关闭按钮')
        self.elem_my = self.adr_elem(res_id='bottom_view', index=3, desc='首页底部我的入口')

    def test_normal(self):
        self.elem_close.click()
        self.elem_my.click()
        self.assert_in_page('我的服务')


if __name__ == '__main__':
    qrunner.main(
        platform='android',
        device_id='UQG5T20414005787',
        pkg_name='com.qizhidao.clientapp'
    )

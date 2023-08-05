import qrunner


class HomePage(qrunner.Page):
    """APP首页"""
    ad_close = {'label': 'close white big', 'desc': '首页广告关闭按钮'}
    my_entry = {'label': '我的', 'desc': '首页底部我的入口'}
    
    def go_my(self):
        self.ios_elem(**self.ad_close).click_exists()
        self.ios_elem(**self.my_entry).click()


class TestGoMyPOM(qrunner.TestCase):
    """进入我的页-POM模式代码"""

    def start(self):
        self.hp = HomePage(self.driver)

    def test_pom(self):
        self.hp.go_my()
        self.assert_in_page('我的服务')


class TestGoMyNormal(qrunner.TestCase):
    """进入我的页-过程模式代码"""

    def start(self):
        self.elem_close = self.ios_elem(label='close white big', desc='首页广告关闭按钮')
        self.elem_my = self.ios_elem(label='我的', desc='首页底部我的入口')

    def test_normal(self):
        self.elem_close.click_exists()
        self.elem_my.click()
        self.assert_in_page('我的服务')


if __name__ == '__main__':
    qrunner.main(
        platform='ios',
        device_id='00008101-000E646A3C29003A',
        pkg_name='com.qizhidao.company'
    )

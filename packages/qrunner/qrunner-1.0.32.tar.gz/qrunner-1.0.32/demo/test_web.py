import qrunner


class PatentPage(qrunner.Page):
    """查专利首页"""
    search_input = {'id_': 'driver-home-step1', 'desc': '查专利首页输入框'}
    search_submit = {'id_': 'driver-home-step2', 'desc': '查专利首页搜索确认按钮'}
    
    def simple_search(self):
        self.web_elem(**self.search_input).set_text('无人机')
        self.web_elem(**self.search_submit).click()


class TestPatentSearchPOM(qrunner.TestCase):
    """专利检索-pom模式代码"""

    def start(self):
        """页面和元素初始化"""
        self.pp = PatentPage(self.driver)

    def test_pom(self):
        """pom模式代码"""
        self.driver.open_url()
        self.pp.simple_search()
        self.assert_title('无人机专利检索-企知道')


class TestPatentSearchNormal(qrunner.TestCase):
    """专利检索-过程模式代码"""

    def start(self):
        """页面和元素初始化"""
        self.elem_input = self.web_elem(id_='driver-home-step1', desc='查专利首页输入框')
        self.elem_submit = self.web_elem(id_='driver-home-step2', desc='查专利首页搜索确认按钮')

    def test_normal(self):
        """过程模式代码"""
        self.driver.open_url()
        self.elem_input.set_text('无人机')
        self.elem_submit.click()
        self.assert_title('无人机专利检索-企知道')


if __name__ == '__main__':
    qrunner.main(
        platform='web',
        base_url='https://patents.qizhidao.com/'
    )

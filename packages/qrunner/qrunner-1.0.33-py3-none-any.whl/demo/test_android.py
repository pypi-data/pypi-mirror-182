import qrunner


class HomePage(qrunner.Page):
    """APP首页"""
    ad_close = {'res_id': 'bottom_btn', 'desc': '广告关闭按钮'}
    search_entry = {'res_id': 'banner', 'desc': '搜索入口'}

    def go_search(self):
        """进入综合搜索"""
        self.adr_elem(**self.ad_close).click_exists()
        self.adr_elem(**self.search_entry).click()


class SearchPage(qrunner.Page):
    """综合搜索页"""
    search_input = {'res_id': 'cet_search_key', 'desc': '搜索框'}
    search_confirm = {'res_id': 'tv_search_cancel', 'desc': '搜索确认按钮'}

    def search(self, keyword: str):
        self.adr_elem(**self.search_input).set_text(keyword)
        self.adr_elem(**self.search_confirm).click()


class TestSearch(qrunner.TestCase):
    """搜索无人机"""

    def start(self):
        self.hp = HomePage(self.driver)
        self.sp = SearchPage(self.driver)

    def test_pom(self):
        self.hp.go_search()
        self.sp.search('无人机')
        self.assert_in_page('航天彩虹无人机股份有限公司')


if __name__ == '__main__':
    qrunner.main(
        platform='android',
        device_id='UJK0220521066836',
        pkg_name='com.qizhidao.clientapp'
    )

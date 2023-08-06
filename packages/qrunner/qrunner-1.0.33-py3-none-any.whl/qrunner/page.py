import time

from qrunner.utils.log import logger
from qrunner.core.android.element import AdrElem
from qrunner.core.ios.element import IosElem
from qrunner.core.web.element import WebElem
from qrunner.core.ocr.element import OCRElem
from qrunner.core.image.element import ImageElem


class Page(object):
    """页面基类，用于pom模式封装"""

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def sleep(n):
        """休眠"""
        logger.info(f"休眠 {n} 秒")
        time.sleep(n)

    def adr_elem(self, *arg, **kwargs):
        return AdrElem(self.driver, *arg, **kwargs)

    def ios_elem(self, *args, **kwargs):
        return IosElem(self.driver, *args, **kwargs)

    def web_elem(self, *args, **kwargs):
        return WebElem(self.driver, *args, **kwargs)

    def ocr_elem(self, *args, **kwargs):
        return OCRElem(self.driver, *args, **kwargs)

    def image_elem(self, *args, **kwargs):
        return ImageElem(self.driver, *args, **kwargs)

    def assert_in_page(self, expect_value, timeout=5):
        """断言页面包含文本"""
        for _ in range(timeout + 1):
            try:
                page_source = self.driver.page_content
                logger.info(f"断言: {page_source}\n包含 {expect_value}")
                assert expect_value in page_source, f"页面内容不包含 {expect_value}"
                break
            except AssertionError:
                time.sleep(1)
        else:
            page_source = self.driver.page_content
            logger.info(f"断言: {page_source}\n包含 {expect_value}")
            assert expect_value in page_source, f"页面内容不包含 {expect_value}"

    def assert_not_in_page(self, expect_value, timeout=5):
        """断言页面不包含文本"""
        for _ in range(timeout + 1):
            try:
                page_source = self.driver.page_content
                logger.info(f"断言: {page_source}\n不包含 {expect_value}")
                assert expect_value not in page_source, f"页面内容不包含 {expect_value}"
                break
            except AssertionError:
                time.sleep(1)
        else:
            page_source = self.driver.page_content
            logger.info(f"断言: {page_source}\n不包含 {expect_value}")
            assert expect_value not in page_source, f"页面内容仍然包含 {expect_value}"

    def assert_title(self, expect_value=None, timeout=5):
        """断言页面标题等于"""
        for _ in range(timeout + 1):
            try:
                title = self.driver.title
                logger.info(f"断言: 页面标题 {title} 等于 {expect_value}")
                assert expect_value == title, f"页面标题 {title} 不等于 {expect_value}"
                break
            except AssertionError:
                time.sleep(1)
        else:
            title = self.driver.title
            logger.info(f"断言: 页面标题 {title} 等于 {expect_value}")
            assert expect_value == title, f"页面标题 {title} 不等于 {expect_value}"

    def assert_in_title(self, expect_value=None, timeout=5):
        """断言页面标题包含"""
        for _ in range(timeout + 1):
            try:
                title = self.driver.title
                logger.info(f"断言: 页面标题 {title} 包含 {expect_value}")
                assert expect_value in title, f"页面标题 {title} 不包含 {expect_value}"
                break
            except AssertionError:
                time.sleep(1)
        else:
            title = self.driver.title
            logger.info(f"断言: 页面标题 {title} 包含 {expect_value}")
            assert expect_value in title, f"页面标题 {title} 不包含 {expect_value}"

    def assert_url(self, expect_value=None, timeout=5):
        """断言页面url等于"""
        for _ in range(timeout + 1):
            try:
                url = self.driver.url
                logger.info(f"断言: 页面url {url} 等于 {expect_value}")
                assert expect_value == url, f"页面url {url} 不等于 {expect_value}"
                break
            except AssertionError:
                time.sleep(1)
        else:
            url = self.driver.url
            logger.info(f"断言: 页面url {url} 等于 {expect_value}")
            assert expect_value == url, f"页面url {url} 不等于 {expect_value}"

    def assert_in_url(self, expect_value=None, timeout=5):
        """断言页面url包含"""
        for _ in range(timeout + 1):
            try:
                url = self.driver.url
                logger.info(f"断言: 页面url {url} 包含 {expect_value}")
                assert expect_value in url, f"页面url {url} 不包含 {expect_value}"
                break
            except AssertionError:
                time.sleep(1)
        else:
            url = self.driver.url
            logger.info(f"断言: 页面url {url} 包含 {expect_value}")
            assert expect_value in url, f"页面url {url} 不包含 {expect_value}"

    def assert_alert_text(self, expect_value):
        """断言弹窗文本"""
        alert_text = self.driver.alert_text
        logger.info(f"断言: 弹窗文本 {alert_text} 等于 {expect_value}")
        assert expect_value == alert_text, f"弹窗文本 {alert_text} 等于 {expect_value}"




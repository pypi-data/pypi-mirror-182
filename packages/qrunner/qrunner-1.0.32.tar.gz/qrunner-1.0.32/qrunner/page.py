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



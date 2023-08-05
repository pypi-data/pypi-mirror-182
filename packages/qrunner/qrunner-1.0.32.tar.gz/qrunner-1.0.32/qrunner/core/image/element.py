import os
import time

from qrunner.utils.log import logger
from qrunner.core.image.image_discern import ImageDiscern


class ImageElem(object):
    """图像识别定位"""

    def __init__(self, driver, image: str):
        self.driver = driver
        self.target_image = image

    def exists(self, retry=3, timeout=3, grade=0.9, gauss_num=111):
        logger.info(f'图像识别判断: {self.target_image} 是否存在')
        for i in range(retry):
            logger.info(f'第{i + 1}次查找:')
            self.driver.screenshot(os.path.join(os.path.join(
                os.path.abspath('./Images/'), 'SourceImage.png')))
            res = ImageDiscern(self.target_image, grade, gauss_num).get_coordinate()
            logger.debug(res)
            if isinstance(res, tuple):
                return True
            time.sleep(timeout)
        else:
            self.driver.screenshot_with_time(f'图像识别定位失败-{self.target_image}')
            return False

    def click(self, retry=3, timeout=3, grade=0.9, gauss_num=111):
        logger.info(f'图像识别点击图片: {self.target_image}')
        for i in range(retry):
            logger.info(f'第{i + 1}次查找:')
            self.driver.screenshot(os.path.join(os.path.join(
                os.path.abspath('./Images/'), 'SourceImage.png')))
            res = ImageDiscern(self.target_image, grade, gauss_num).get_coordinate()
            if isinstance(res, tuple):
                self.driver.click(res[0], res[1])
                return
            time.sleep(timeout)
        else:
            self.driver.screenshot_with_time(f'图像识别定位失败-{self.target_image}')
            raise Exception('未识别到图片，无法进行点击')


if __name__ == '__main__':
    from qrunner.core.android.driver import AndroidDriver

    driver = AndroidDriver()
    driver.pkg_name = 'com.qizhidao.clientapp'
    driver.start_app()
    driver.d(resourceId='com.qizhidao.clientapp:id/bottom_btn').click(timeout=5)
    # elem = OCRElem(driver, '查老板')
    # elem.click()

    elem = ImageElem(driver, 'tpl1670743672123.png')
    elem.click(grade=0.9)

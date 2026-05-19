from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.logger import get_logger
from utils.screenshot import take_screenshot

# test
class BasePage:
    """所有页面对象的基类，封装常用操作。"""

    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)

    # ------------------------------------------------------------------ 元素查找
    def find_element(self, by: str, value: str, timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
        except TimeoutException:
            self.logger.error(f'Element not found [{by}]: {value}')
            take_screenshot(self.driver, 'element_not_found')
            raise

    def find_elements(self, by: str, value: str, timeout: int = 10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
        except TimeoutException:
            return []
        return self.driver.find_elements(by, value)

    # ------------------------------------------------------------------ 基础交互
    def click(self, by: str, value: str) -> None:
        element = self.find_element(by, value)
        element.click()
        self.logger.debug(f'Clicked [{by}]: {value}')

    def get_text(self, by: str, value: str) -> str:
        return self.find_element(by, value).text

    # ------------------------------------------------------------------ 手势
    def swipe_up(self, velocity: int = 5000) -> None:
        self.driver.execute_script('mobile: swipe', {'direction': 'up', 'velocity': velocity})
        self.logger.debug(f'Swiped up (velocity={velocity})')

    def swipe_down(self, velocity: int = 3000) -> None:
        self.driver.execute_script('mobile: swipe', {'direction': 'down', 'velocity': velocity})
        self.logger.debug(f'Swiped down (velocity={velocity})')

    # ------------------------------------------------------------------ 截图
    def screenshot(self, name: str = None) -> str:
        return take_screenshot(self.driver, name or self.__class__.__name__)

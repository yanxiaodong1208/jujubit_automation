from appium import webdriver
from appium.options.ios import XCUITestOptions

from utils.config_loader import config
from utils.logger import get_logger

logger = get_logger(__name__)


class DriverManager:
    """单例式 Appium driver 管理器。"""

    _driver = None

    @classmethod
    def get_driver(cls) -> webdriver.Remote:
        if cls._driver is None:
            cls._driver = cls._create_driver()
        return cls._driver

    @classmethod
    def _create_driver(cls) -> webdriver.Remote:
        dev = config['device']
        app = config['app']
        srv = config['server']

        options = XCUITestOptions()
        options.platform_name = dev['platform_name']
        options.platform_version = str(dev['platform_version'])
        options.device_name = dev['device_name']
        options.udid = dev['udid']
        options.automation_name = dev['automation_name']
        options.auto_accept_alerts = dev.get('auto_accept_alerts', True)
        options.bundle_id = app['bundle_id']

        logger.info(f'Connecting to Appium server: {srv["url"]}')
        driver = webdriver.Remote(srv['url'], options=options)
        driver.implicitly_wait(dev.get('implicit_wait', 10))
        logger.info('Driver initialized successfully')
        return driver

    @classmethod
    def quit_driver(cls) -> None:
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
            logger.info('Driver quit')

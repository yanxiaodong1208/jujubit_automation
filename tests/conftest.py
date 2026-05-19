import pytest

from utils.driver_manager import DriverManager
from utils.logger import get_logger
from utils.screenshot import take_screenshot

logger = get_logger('conftest')


# ------------------------------------------------------------------ fixtures
@pytest.fixture(scope='session')
def driver():
    """Session 级别 driver，整个测试会话共享一个连接。"""
    logger.info('=== Session start: initializing Appium driver ===')
    d = DriverManager.get_driver()
    yield d
    logger.info('=== Session end: quitting Appium driver ===')
    DriverManager.quit_driver()


@pytest.fixture(scope='function', autouse=True)
def screenshot_on_failure(request, driver):
    """用例失败时自动截图。"""
    yield
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        take_screenshot(driver, f'FAILED_{request.node.name}')


# ------------------------------------------------------------------ hooks
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """将每个阶段的结果挂载到 item，供 fixture 读取。"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f'rep_{rep.when}', rep)

import os
from datetime import datetime

from utils.logger import get_logger

logger = get_logger(__name__)


def take_screenshot(driver, name: str = 'screenshot') -> str:
    """截图并保存到 reports/screenshots/，返回文件路径。"""
    save_dir = os.path.join(os.path.dirname(__file__), '..', 'reports', 'screenshots')
    os.makedirs(save_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    path = os.path.join(save_dir, f'{name}_{timestamp}.png')
    driver.save_screenshot(path)
    logger.info(f'Screenshot saved: {path}')
    return path

"""
Demo 测试：首页浏览 3D 帖子

运行方式：
    pytest tests/test_home.py -v
"""
import time

import pytest
import yaml
import os

from pages.detail_page import DetailPage
from pages.home_page import HomePage
from utils.logger import get_logger

logger = get_logger(__name__)


def _load_data() -> dict:
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'test_data.yaml')
    with open(data_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def test_data():
    return _load_data()['browse']


class TestHomeBrowse:
    """首页 3D 浏览 Demo 用例。"""

    def test_tap_post_and_view_3d(self, driver, test_data):
        """Demo：点击一个帖子，连续查看 N 次 3D，再关闭帖子。"""
        time.sleep(5)  # 等待 App 首页加载完成

        home = HomePage(driver)
        detail = DetailPage(driver)

        start_cell = test_data['start_cell']
        view_count = test_data['detail_view_count']

        logger.info(f'Tapping post cell [{start_cell}]')
        home.tap_post(cell_index=start_cell)

        for i in range(view_count):
            logger.info(f'3D view round {i + 1}/{view_count}')
            detail.view_3d_and_return()
            detail.scroll_post()

        logger.info('Closing post')
        home.close_post()

    def test_scroll_feed(self, driver, test_data):
        """Demo：首页上滑刷新两次。"""
        home = HomePage(driver)
        home.scroll_feed(times=2, velocity=test_data['swipe_velocity'])
        logger.info('Feed scrolled successfully')

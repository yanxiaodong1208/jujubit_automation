from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class HomePage(BasePage):
    """首页（瀑布流列表）页面对象。"""

    # --- 定位器 ---
    # 首页帖子缩略图，{index} 替换为 cell 下标（1-based）
    _CELL_IMAGE_CHAIN = (
        "**/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther"
        "/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther"
        "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]"
        "/XCUIElementTypeCollectionView/XCUIElementTypeCell[{index}]"
        "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage"
    )
    _CLOSE_POST_ID = "img down"

    # --- 页面操作 ---
    def tap_post(self, cell_index: int = 1) -> None:
        """点击首页第 cell_index 个帖子。"""
        chain = self._CELL_IMAGE_CHAIN.format(index=cell_index)
        self.click(AppiumBy.IOS_CLASS_CHAIN, chain)
        self.logger.info(f'Tapped post cell [{cell_index}]')

    def close_post(self) -> None:
        """关闭帖子详情（下拉收起）。"""
        self.click(AppiumBy.ACCESSIBILITY_ID, self._CLOSE_POST_ID)
        self.logger.info('Closed post')

    def scroll_feed(self, times: int = 1, velocity: int = 5000) -> None:
        """首页上滑刷新 times 次。"""
        for _ in range(times):
            self.swipe_up(velocity)

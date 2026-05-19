from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class DetailPage(BasePage):
    """帖子详情页（含 3D 预览入口）页面对象。"""

    # --- 定位器 ---
    _BACK_ID = "icon back"
    _BTN_3D_CHAIN = (
        "**/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther"
        "/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther"
        "/XCUIElementTypeOther/XCUIElementTypeOther"
        "/XCUIElementTypeCollectionView/XCUIElementTypeCell"
        "/XCUIElementTypeOther/XCUIElementTypeOther"
        "/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"
    )

    # --- 页面操作 ---
    def click_3d(self) -> None:
        """点击帖子内 3D 预览按钮。"""
        self.click(AppiumBy.IOS_CLASS_CHAIN, self._BTN_3D_CHAIN)
        self.logger.info('Clicked 3D button')

    def go_back(self) -> None:
        """点击返回按钮回到帖子详情。"""
        self.click(AppiumBy.ACCESSIBILITY_ID, self._BACK_ID)
        self.logger.info('Tapped back')

    def view_3d_and_return(self) -> None:
        """点击 3D → 查看 → 返回，一次完整操作。"""
        self.click_3d()
        self.go_back()

    def scroll_post(self, times: int = 1) -> None:
        """在帖子详情内上滑 times 次。"""
        for _ in range(times):
            self.swipe_up()

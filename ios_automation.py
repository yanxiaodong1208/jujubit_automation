import random
import time

from appium import webdriver
from appium.options.ios import XCUITestOptions

# For W3C actions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException, WebDriverException
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.action_chains import ActionChains

# 1. 定义设备能力和App信息
# 这些是告诉Appium如何连接设备和启动App的关键配置
options = XCUITestOptions()

# 平台和设备信息 (必须准确)
options.platform_name = 'iOS'
options.platform_version = '26.1'  # 修改为你的设备系统版本
options.device_name = 'iPhone 15q'  # 修改为你的设备名称（模拟器名称）
options.udid = '00008120-001849EA0EB8201E'

# App信息 (二选一)
# 方式A: 直接指定App的路径 (适用于开发阶段的.app文件)
# options.app = '/path/to/your/AppName.app'

# 方式B: 指定Bundle ID (适用于已安装在设备上的App，更常用)
options.bundle_id = 'com.vast.jujubit'  # 这里以苹果的“设置”App为例

# 自动化引擎 (必须)
options.automation_name = 'XCUITest'

# 其他可选配置
options.auto_accept_alerts = True  # 自动接受系统弹窗（如权限请求）
# options.no_reset = True  # 不重置App状态，延续上次的会话

# 2. 连接Appium Server并初始化驱动
# 确保Appium Server正在 http://localhost:4723 运行
driver = webdriver.Remote('http://localhost:4723', options=options)
driver.implicitly_wait(10)


# 快速滑动
def fast_swipe_up(driver) :
    # 使用 mobile 命令进行快速滑动
    swipe_options = {
        "direction" : "up",
        "velocity" : 5000  # 速度参数，值越大滑动越快
    }
    driver.execute_script('mobile: swipe', swipe_options)


def common_action() :
    # 3d预览
    # time.sleep(3)
    # 3d入口点击
    # time.sleep(3)
    print("3d入口点击")
    CLASS_CHAIN_3D = '**/XCUIElementTypeButton[`name == "3D"`]'
    element_3d = driver.find_element(
        AppiumBy.IOS_CLASS_CHAIN,
        CLASS_CHAIN_3D
    )
    element_3d.click()

    # 返回
    # time.sleep(1)
    print("返回帖子详情")
    back_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "icon back")
    back_button.click()
    # time.sleep(1)
    # except NoSuchElementException as e :
    #     print(f"元素找不到，可能 App 已崩溃: {e}")
    #     pass
    # except WebDriverException as e :
    #     print(f"WebDriver 错误，可能 App 崩溃: {e}")
    #     pass
    # except Exception as e :
    #     print(f"💥 主程序异常: {e}")


def auto_3d() :
    time.sleep(10)
    start_time = time.time()
    current_time = time.time()
    # timeout = 5
    post_num = 0
    # detail_num = 20
    detail_num = 100
    time_min = 25
    page, cell = 1, 1
    while current_time - start_time < time_min * 60 :
        for cell in range(1, 5) :
            if page == 1 and cell == 1 :
                cell = 2
            print(f"点击cell={cell}")
            IMAGE_CLASS_CHAIN = "**/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[" + str(cell) + "]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage"

            # IMAGE_CLASS_CHAIN = "**/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage"
            post_cell = driver.find_element(AppiumBy.IOS_CLASS_CHAIN, IMAGE_CLASS_CHAIN)
            post_cell.click()
            # time.sleep(1)

            for i in range(detail_num) :
                # common_action()
                # 上滑
                print("3d点击")
                IMAGE_CLASS_CHAIN = "**/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"
                # IMAGE_CLASS_CHAIN = "**/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]"
                cell_3d = driver.find_element(AppiumBy.IOS_CLASS_CHAIN, IMAGE_CLASS_CHAIN)
                cell_3d.click()
                post_num += 1
                print(f"no.{post_num} post".center(80, '='))

                print("返回帖子详情")
                # **/XCUIElementTypeButton[`name == "icon back"`]
                back_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "icon back")
                back_button.click()

                print("帖子上滑")
                fast_swipe_up(driver)

            # 关闭帖子
            # time.sleep(1)
            print("关闭帖子")
            close_post = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "img down")
            close_post.click()

            # 首页上滑
            for i in range(random.randint(1, 2)) :
                # time.sleep(1)
                print("首页上滑")
                fast_swipe_up(driver)
                # actions = ActionChains(driver)
                # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
                # actions.w3c_actions.pointer_action.move_to_location(109, 589)
                # actions.w3c_actions.pointer_action.pointer_down()
                # actions.w3c_actions.pointer_action.move_to_location(127, 390)
                # actions.w3c_actions.pointer_action.release()
                # actions.perform()
            current_time = time.time()
    print(f"浏览帖子：{post_num}，消耗时间：{time_min}")


if __name__ == "__main__" :
    auto_3d()

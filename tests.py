import pytest
import time
import os

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

directory = '%s/' % os.getcwd()


class TestOrientation():
    # @pytest.fixture(scope="function")
    # def driver(self, request):
    #     desired_caps = {
    #         "automationName": "Appium",
    #         "appActivity": "com.leia.leialoft.ui.main.view.MainActivity",
    #         "platformName": "Android",
    #         "platformVersion": "8.1.0",
    #         "deviceName": "3a90b04d",
    #         "appPackage": "com.leia.leialoft"
    #     }
    #     driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    #
    #     def fin():
    #         driver.quit()
    #
    #     request.addfinalizer(fin)
    #     return driver

    @pytest.fixture(scope="function")
    def driver(self, request):
        desired_caps = {
            "automationName": "Appium",
            "appActivity": "com.leialoft.filebrowser.FileBrowserActivity",
            "platformName": "Android",
            "platformVersion": "8.1.0",
            "deviceName": "3a90b04d",
            "appPackage": "com.leialoft.redmediaplayer",
            # "noReset": "false",
            # "autoGrantPermissions": "true"
        }
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        def fin():
            driver.quit()

        request.addfinalizer(fin)
        return driver

    def test_some_orientation(self, driver):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'com.android.packageinstaller:id/permission_allow_button')))
        allow_button = driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button')
        allow_button.click()
        assert driver.orientation == 'PORTRAIT'
        driver.save_screenshot(directory + 'file1.png')
        driver.orientation = 'LANDSCAPE'
        time.sleep(1)
        assert driver.orientation == 'LANDSCAPE'
        driver.save_screenshot(directory + 'file2.png')
        driver.orientation = 'Portrait'

    def test_IsLibraryExists(self):
        leias_activities = os.popen(
            'adb shell dumpsys package | findstr -i com.leia.leialoft | findstr Activity').read()

        print(leias_activities)

        assert 'Main' in leias_activities

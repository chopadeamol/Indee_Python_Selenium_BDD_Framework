from datetime import datetime
import time
from behave import given
from behave import when
from behave import then
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from features.pages.loginPage import LoginPage
from utils.readProperties import ReadConfig

class Login:
    try:
        @given('I got navigated to the Indee login page')
        def read_creds_and_navigate_to_url(context):
            options = Options()
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            prefs = {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False
                }
            options.add_experimental_option("prefs", prefs)
            context.driver = webdriver.Chrome(options=options)
            context.lp = LoginPage(context.driver)
            context.baseURL = ReadConfig().getApplicationUrl()
            context.password = ReadConfig().getPassword()
            # navigated to the url
            context.driver.get(context.baseURL)
            # maximize browser window
            context.lp.maximize_browser_window()

        @when('I enter valid access code')
        def enter_access_code(context):
            # Enter access code to sign in
            context.lp.enter_password(context.password)

        @when('Click on sign in button and did so many actions as it is on the same page')
        def sign_in_plus_many_actions(context):
            context.lp = LoginPage(context.driver)
            # click on sign in button
            context.lp.click_sign_in_button()
            # scroll window down
            context.lp.scroll_window_down()
            # click on test automation project
            context.lp.click_on_test_automation_project()
            # click on details tab
            context.lp.click_on_details_tab()
            # click on video tab
            context.lp.click_on_video_tab()
            # scroll down again so that play button will be visible
            context.lp.scroll_window_down()
            # Click on play button
            context.lp.click_on_play_button()
            # switch to iframe
            context.lp.switch_frame()
            # click on in frame play button to pause
            context.lp.click_on_in_frame_play_button()
            # click again on in frame play button to resume playing
            context.lp.click_on_in_frame_play_button()
            # click on volume button to mute it
            context.lp.click_on_volume_button_to_mute()
            # click on volume button again to unmute it
            context.lp.click_on_volume_button_to_unmute()
            # Set volume to 50 percent
            context.lp.set_volume_50()
            # set volume to 100 percent again
            context.lp.set_volume_100()
            # Set volume to 50 percent again
            context.lp.set_volume_50()
            # click on setting button
            context.lp.click_on_in_frame_setting_button()
            # set the resolution to 480p
            context.lp.set_resolution_480p()
            # again click on setting button
            context.lp.click_on_in_frame_setting_button()
            # set the resolution to 720p
            context.lp.set_resolution_720p()
            # click on in frame play button to pause a video
            context.lp.click_on_in_frame_play_button()

        @then('Home page of the Indee website should display')
        def step_impl(context):
            print("Home page of the Indee website is displayed")
            # click on back button to exit from video and get back to home screen
            context.lp.click_to_go_back()
            # click on sign out button to log off and exit
            context.lp.click_on_sign_out_button()


    except Exception as e:
        print("Occurred an Exception", e)
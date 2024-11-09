import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    try:
        def __init__(self, driver):
            self.driver = driver

        access_code_id = "access-code"
        sign_button_xpath = "//span[contains(text(),'Sign In')]"
        scroll_window = "window.scrollTo(0, document.body.scrollHeight);"
        test_automation_xpath = "//h5[contains(text(),'Test automation project')]"
        details_id = "detailsSection"
        video_id = "videosSection"
        play_button_xpath = "(//*[local-name()='svg' and @aria-hidden='true'])[1]"
        iframe_xpath = "//iframe[@id='video_player']"
        in_iframe_play_button = "document.querySelector('#media-player > div.jw-wrapper.jw-reset > div.jw-controls.jw-reset > div.jw-controlbar.jw-reset > div.jw-reset.jw-button-container > div.jw-icon.jw-icon-inline.jw-button-color.jw-reset.jw-icon-playback').click()"
        in_frame_volume_button = "document.querySelector('#media-player > div.jw-wrapper.jw-reset > div.jw-controls.jw-reset > div.jw-controlbar.jw-reset > div.jw-reset.jw-button-container > div.jw-icon.jw-icon-tooltip.jw-icon-volume.jw-button-color.jw-reset.jw-full > svg.jw-svg-icon.jw-svg-icon-volume-100')"
        in_frame_volume_slider = "document.querySelector('#media-player > div.jw-wrapper.jw-reset > div.jw-controls.jw-reset > div.jw-controlbar.jw-reset > div.jw-reset.jw-button-container > div.jw-icon.jw-icon-tooltip.jw-icon-volume.jw-button-color.jw-reset.jw-full > div > div > div > div.jw-rail.jw-reset')"
        in_frame_setting = "document.querySelector('#media-player > div.jw-wrapper.jw-reset > div.jw-controls.jw-reset > div.jw-controlbar.jw-reset > div.jw-reset.jw-button-container > div.jw-icon.jw-icon-inline.jw-button-color.jw-reset.jw-icon-settings.jw-settings-submenu-button').click()"
        in_frame_480p_xpath = "//button[contains(text(),'480p')]"
        in_frame_720_xpath = "//button[contains(text(),'720p')]"
        sign_out_button_xpath1 = "(//*[local-name()='svg' and @viewBox='0 0 32 32'])[4]"


        def enter_password(self, password):
            self.driver.find_element(By.ID, self.access_code_id).send_keys(password)
            time.sleep(5)
            # WebDriverWait(self.driver, 10)

        def maximize_browser_window(self):
            self.driver.maximize_window()
            time.sleep(5)
            # WebDriverWait(self.driver, 10)

        def click_sign_in_button(self):
            self.driver.find_element(By.XPATH, self.sign_button_xpath).click()
            time.sleep(5)
            # sign_in_button = WebDriverWait(self.driver, 5).until(
            #     EC.presence_of_element_located((By.XPATH,self.sign_button_xpath)))
            # sign_in_button.click()

        def scroll_window_down(self):
            self.driver.execute_script(self.scroll_window)
            time.sleep(5)
            # WebDriverWait(self.driver, 5)

        def click_on_test_automation_project(self):
            self.driver.find_element(By.XPATH, self.test_automation_xpath).click()
            time.sleep(5)
            # test_automation_project = WebDriverWait(self.driver, 5).until(
            #     EC.presence_of_element_located((By.XPATH, self.test_automation_xpath)))
            # test_automation_project.click()

        def click_on_details_tab(self):
            self.driver.find_element(By.ID, self.details_id).click()
            time.sleep(4)
            # details_tab = WebDriverWait(self.driver,2).until(EC.presence_of_element_located((By.ID,self.details_id)))
            # details_tab.click()


        def click_on_video_tab(self):
            self.driver.find_element(By.ID, self.video_id).click()
            time.sleep(4)
            # video_tab = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, self.video_id)))
            # video_tab.click()

        def click_on_play_button(self):
            self.driver.find_element(By.XPATH, self.play_button_xpath).click()
            time.sleep(18)
            # play_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.play_button_xpath)))
            # play_button.click()

        def switch_frame(self):
            self.driver.switch_to.frame(self.driver.find_element(By.XPATH, self.iframe_xpath))
            time.sleep(2)
            # switch_to_frame = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, self.iframe_xpath)))
            # switch_to_frame.click()

        def click_on_in_frame_play_button(self):
            self.driver.execute_script(self.in_iframe_play_button)
            time.sleep(5)
            # WebDriverWait(self.driver, 5)

        def click_on_in_frame_setting_button(self):
            self.driver.execute_script(self.in_frame_setting)
            time.sleep(5)

        def set_resolution_480p(self):
            self.driver.find_element(By.XPATH, self.in_frame_480p_xpath).click()
            time.sleep(2)
            # res_480p = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, self.in_frame_480p_xpath)))
            # res_480p.click()

        def set_resolution_720p(self):
            self.driver.find_element(By.XPATH, self.in_frame_720_xpath).click()
            time.sleep(2)
            # res_720p = WebDriverWait(self.driver, 2).until(
            #     EC.presence_of_element_located((By.XPATH, self.in_frame_720_xpath)))
            # res_720p.click()

        def click_to_go_back(self):
            self.driver.back()
            time.sleep(5)
            # WebDriverWait(self.driver,5)

        def click_on_sign_out_button(self):
            self.driver.find_element(By.XPATH, self.sign_out_button_xpath1).click()
            time.sleep(5)
            # signout = WebDriverWait(self.driver, 5).until(
            #     EC.presence_of_element_located((By.XPATH, self.sign_out_button_xpath1)))
            # signout.click()
    except Exception as e:
        print("Exception occurred:",e)
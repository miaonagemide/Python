
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

class Action():
    def __init__(self):

        self.desired_caps = {
            "platformName": "Android",
            "deviceName": "emulator",
            "appPackage": "com.zhiliaoapp.musically",
            "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
            'noReset': True,
            'newCommandTimeout': 0
        }

        self.server = 'http://localhost:4723/wd/hub'

        self.driver = webdriver.Remote(self.server, self.desired_caps)

        self.start_x = 600
        self.start_y = 1200
        self.distance = 1000


   # def taps(self):
        #actionS = TouchAction(self.driver)
        #actionS.tap(element=None, x=500, y=600, count=2).perform()



        #self.driver.tap([(500, 1200)], 500,count=2)
        #sleep(0.2)
        #self.driver.tap([(500, 1200)], 500)
        

    def getSleep(self):
        sleep(2)

    def reRoll(self):

        self.driver.swipe(self.start_x, self.start_y, self.start_x,
                          self.start_y - self.distance)
        sleep(2)

        self.driver.swipe(self.start_x, self.start_y, self.start_x,
                          self.start_y + self.distance)
 
    def scroll(self):

        sleep(2)

        self.driver.swipe(self.start_x, self.start_y, self.start_x,
                              self.start_y-self.distance)

 
if __name__ == 'appiumForProject':
   
    action = Action()


from selenium import webdriver
import ascXp as xp
import ascConst as con
import time

MAX_WAIT_TIME = 5
SLEEP_TIME = 1

class StudentAutoCheckInstance:
    def __init__(self,PersonalInfo,SchoolInfo):
        if not ((type(PersonalInfo) == list) and (type(SchoolInfo) == list)):
            raise TypeError('Information type must be list.')
        self.__PersonalInfo = PersonalInfo
        self.__SchoolInfo = SchoolInfo
    
    def info(self):
        print(f'Student Info : {self.__PersonalInfo}\nSchool Info : {self.__SchoolInfo}')
    
    def run(self):
        Driver = webdriver.Chrome(con.CHROMEDRV_PATH)   #Access to chromedriver

        Driver.get(con.SELFCHCK_URL)                    #Go to self-checking site
        Driver.implicitly_wait(MAX_WAIT_TIME)

        Driver.find_element_by_xpath(xp.MAIN_SCHOOL).click()    #School type (default = Elem, Mid, High)
        Driver.find_element_by_xpath(xp.MAIN_SUBMIT).click()    #School type confirm
        Driver.implicitly_wait(MAX_WAIT_TIME)

        Driver.find_element_by_xpath(xp.SCHOOL_INPUT).click()   #School search input
        Driver.find_element_by_xpath(xp.SCHOOL_REGION(self.__SchoolInfo[2])).click()    #School Region input - by region code
        Driver.find_element_by_xpath(xp.SCHOOL_LEVEL(self.__SchoolInfo[1])).click()     #School Region input - by level code
        Driver.implicitly_wait(MAX_WAIT_TIME)

        Driver.find_element_by_xpath(xp.SCHOOL_NAME_INPUT).send_keys(self.__SchoolInfo[0])
        Driver.find_element_by_xpath(xp.SCHOOL_NAME_SEARCH).click()
        Driver.implicitly_wait(MAX_WAIT_TIME)
        Driver.find_element_by_xpath(xp.SCHOOL_SELECT_FROM_LIST).click()
        Driver.implicitly_wait(MAX_WAIT_TIME)
        Driver.find_element_by_xpath(xp.SCHOOL_SELECT_CONFIRM_BTN).click()
        Driver.implicitly_wait(MAX_WAIT_TIME)

        Driver.find_element_by_xpath(xp.STUDENT_NAME_INPUT).send_keys(self.__PersonalInfo[0])
        Driver.implicitly_wait(MAX_WAIT_TIME)
        Driver.find_element_by_xpath(xp.STUDENT_BIRTH_INPUT).send_keys(self.__PersonalInfo[1] + "\n")
        Driver.implicitly_wait(MAX_WAIT_TIME)
        time.sleep(SLEEP_TIME)
        Driver.find_element_by_xpath(xp.PASSWORD_INPUT).send_keys(self.__PersonalInfo[2] + "\n")
        time.sleep(SLEEP_TIME)
        Driver.find_element_by_xpath(xp.CHECKING_START_BTN).click()
        time.sleep(SLEEP_TIME)
        Driver.implicitly_wait(MAX_WAIT_TIME)

        for items in xp.CHECKING_QUESTION_LIST:
            Driver.find_element_by_xpath(items).click()
            Driver.implicitly_wait(MAX_WAIT_TIME)

        Driver.find_element_by_xpath(xp.CHECKING_CONFIRM).click()
        Driver.implicitly_wait(SLEEP_TIME)
        time.sleep(SLEEP_TIME)

        Driver.quit()
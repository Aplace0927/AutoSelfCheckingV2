import ascConst as con

MAIN_SCHOOL = '/html/body/app-root/div/div[1]/div/ul[1]/li[1]/div/label'
MAIN_SUBMIT = '//*[@id="btnConfirm2"]'
SCHOOL_INPUT = '//*[@id="WriteInfoForm"]/table/tbody/tr[1]/td/button'

def SCHOOL_REGION(Region):
    return '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[1]/td/select/option[' + str(con.SCHOOL_REGION_DICT[Region]) + ']'

def SCHOOL_LEVEL(Level):
    return '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[2]/td/select/option[' + str(con.SCHOOL_LEVEL_DICT[Level]) + ']'

SCHOOL_NAME_INPUT = '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[1]/input'
SCHOOL_NAME_SEARCH = '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button'
SCHOOL_SELECT_FROM_LIST = '//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/p'
SCHOOL_SELECT_FROM_LIST_SELECTOR = '#softBoardListLayer > div.layerContentsWrap > div.layerSchoolSelectWrap > ul > li'
SCHOOL_SELECT_CONFIRM_BTN = '//*[@id="softBoardListLayer"]/div[2]/div[2]/input'

STUDENT_NAME_INPUT = '//*[@id="WriteInfoForm"]/table/tbody/tr[2]/td/input'
STUDENT_BIRTH_INPUT = '//*[@id="WriteInfoForm"]/table/tbody/tr[3]/td/input'
PERSONAL_INFO_CONFIRM = '//*[@id="btnConfirm"]'

PASSWORD_INPUT = '//*[@id="WriteInfoForm"]/table/tbody/tr/td/input'
PASSWORD_SELECTOR = '#WriteInfoForm > table > tbody > tr > td > input'
PASSWORD_CONFIRM = '//*[@id="btnConfirm"]'

CHECKING_START_BTN = '//*[@id="container"]/div/section[2]/div[2]/ul/li/a/button'
CHECKING_QUESTION_LIST = [
    '//*[@id="container"]/div/div/div[2]/div[2]/dl[1]/dd/ul/li[1]/label',
    '//*[@id="container"]/div/div/div[2]/div[2]/dl[2]/dd/ul/li[1]/label',
    '//*[@id="container"]/div/div/div[2]/div[2]/dl[3]/dd/ul/li[1]/label'   
]
CHECKING_CONFIRM = '//*[@id="btnConfirm"]'
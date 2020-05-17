# -*- coding: utf-8 -*-

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


def get_online_friends(user: str, password: str):
    """
    Gets online friends from a ivao webeye account. Returns empty list if no one is online!

    :param user: account username
    :param password: account password
    :return: a list with online friends with format [[name, callsign, time], [name, callsign, time], etc]
    """
    options = Options()
    options.headless = True

    # start chrome driver
    with Chrome(options=options) as driver:
        wait = WebDriverWait(driver, 3)
        driver.get("https://webeyetemp.ivao.aero/")

        # navigate to login
        wait.until(lambda a: a.find_element_by_link_text('Login')).click()

        # fill login form
        wait.until(lambda a: a.find_element_by_name('Id')).send_keys(user)
        wait.until(lambda a: a.find_element_by_name('Pwd')).send_keys(password)

        # send login form
        wait.until(lambda a: a.find_element_by_name('login')).click()
        try:
            # navigate to friends
            wait.until(lambda a: a.find_element_by_link_text('Friends')).click()
            # todo: this find element can be improved to a more specific one
            online_table = wait.until(lambda a: a.find_element_by_id('uiOnlineFriendListTable'))
        except TimeoutException:
            raise LoginInvalidError('TimeoutException when attempting to find Friends tab - login may be invalid!')
        rows = WebDriverWait(online_table, 2).until(lambda a: a.find_elements_by_xpath(".//tbody/tr"))

        # case all friends offline
        if not rows:
            return []

        # else, parse table rows and return list
        output = []
        for elem in rows:
            td_list = elem.find_elements_by_xpath("./td")
            person = []
            for td in td_list[:-1]:
                person.append(td.text)
            output.append(person)
        return output


class LoginInvalidError(Exception):
    pass

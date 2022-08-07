import pytest
import uuid


# fixtures will be applied automatically if they are in the same directory
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # this function helps to detect that some test failed
    # and pass this information to teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def web_browser(request, selenium):

    # в тестах встречаются явные ожидания - time.sleep() и более сложные
    # одновременное применение явных и неявных ожиданий - НЕ ЖЕЛАТЕЛЬНО
    # зададим неявное ожидание В ЦЕЛЯХ ЭКСПЕРИМЕНТА
    selenium.implicitly_wait(5)

    browser = selenium
    browser.set_window_size(1400, 1000)

    # return browser instance to test case:
    yield browser

    # do teardown (this code will be executed after each test):

    if request.node.rep_call.failed:
        # makes screenshot if test fails:
        try:
            browser.execute_script("document.body.bgColor = 'white';")

            # makes screenshot for local debug:
            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

            # for happy debugging:
            print('URL: ', browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)
        except:
            pass # just ignores any errors here
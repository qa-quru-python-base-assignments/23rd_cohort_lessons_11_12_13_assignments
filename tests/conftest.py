import os
from datetime import date

import pytest
import selene
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Remote

from src.models.city import City
from src.models.gender import Gender
from src.models.hobbies import Hobby
from src.models.state import State
from src.models.student import Student
from src.models.subject import Subject
from src.utils import attach


@pytest.fixture(scope="session")
def selenoid_settings():
    load_dotenv()

    return {
        "host": os.getenv("SELENOID_HOST"),
        "login": os.getenv("SELENOID_LOGIN"),
        "password": os.getenv("SELENOID_PASSWORD")
    }


@pytest.fixture()
def browser(selenoid_settings):
    options = Options()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "128.0")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })
    host, login, password = selenoid_settings.values()
    driver = Remote(
        command_executor=f"https://{login}:{password}@{host}/wd/hub",
        options=options
    )
    selene.browser.config.driver = driver

    selene.browser.config.base_url = "https://demoqa.com"

    yield selene.browser

    attach.add_screenshot(selene.browser)
    attach.add_logs(selene.browser)
    attach.add_html(selene.browser)
    attach.add_video(selene.browser)

    selene.browser.quit()


@pytest.fixture()
def student():
    return Student(
        first_name="Test",
        last_name="Testov",
        email="test.testov@test.org",
        gender=Gender.MALE,
        phone_number="1234567890",
        birthdate=date(2000, 1, 1),
        subjects=[Subject.PHYSICS, Subject.MATHS],
        hobbies=[Hobby.SPORTS, Hobby.READING],
        picture="pic.jpg",
        address="Test address",
        state=State.NCR,
        city=City.DELHI
    )

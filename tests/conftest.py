from datetime import date

import pytest
import selene

from src.models.city import City
from src.models.gender import Gender
from src.models.hobbies import Hobby
from src.models.state import State
from src.models.student import Student
from src.models.subject import Subject


@pytest.fixture(scope="function")
def browser():
    selene.browser.config.base_url = "https://demoqa.com"
    selene.browser.driver.maximize_window()
    yield selene.browser
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

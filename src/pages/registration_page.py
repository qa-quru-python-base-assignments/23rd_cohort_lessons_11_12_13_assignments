from __future__ import annotations

from datetime import date
from pathlib import Path

import allure
from selene import have
from selene.core.entity import Collection

from src.models.city import City
from src.models.gender import Gender
from src.models.hobbies import Hobby
from src.models.state import State
from src.models.subject import Subject


class RegistrationPage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step("Открыть страницу с формой регистрации студента")
    def open(self) -> RegistrationPage:
        self.browser.open("/automation-practice-form")
        self.browser.driver.execute_script("$('#fixedban').remove()")
        self.browser.driver.execute_script("$('footer').remove()")
        return self

    @allure.step("Ввести имя")
    def type_first_name(self, value: str) -> RegistrationPage:
        self.browser.element("#firstName").type(value)
        return self

    @allure.step("Ввести фамилию")
    def type_last_name(self, value: str) -> RegistrationPage:
        self.browser.element("#lastName").type(value)
        return self

    @allure.step("Ввести email")
    def type_email(self, value: str) -> RegistrationPage:
        self.browser.element("#userEmail").type(value)
        return self

    @allure.step("Выбрать пол студента")
    def select_gender(self, value: Gender) -> RegistrationPage:
        self.browser.all("[name=gender]").element_by(have.value(value)).element("..").click()
        return self

    @allure.step("Ввести номер телефона")
    def type_phone_number(self, value: str) -> RegistrationPage:
        self.browser.element("#userNumber").type(value)
        return self

    @allure.step("Установить дату рождения")
    def set_birthdate(self, value: date) -> RegistrationPage:
        day, month, year = f"{value.day} {value.strftime('%B')} {value.year}".split()
        self.browser.element("#dateOfBirthInput").click()
        self.browser.element(".react-datepicker__year-select").type(year)
        self.browser.element(".react-datepicker__month-select").type(month)
        self.browser.element(f"[aria-label*='{month} {day}st']").click()
        return self

    @allure.step("Выбрать предметы")
    def select_subjects(self, *args: Subject) -> RegistrationPage:
        for subject in args:
            self.browser.element('#subjectsInput').type(subject).press_enter()
        return self

    @allure.step("Выбрать хобби")
    def select_hobbies(self, *args: Hobby) -> RegistrationPage:
        for hobby in args:
            self.browser.all(".custom-checkbox").element_by(have.text(hobby)).click()
        return self

    @allure.step("Загрузить фотографию")
    def upload_picture(self, filename: str) -> RegistrationPage:
        path = str(
            Path(__file__).parent.parent.parent.joinpath('resources', filename).absolute()
        )
        self.browser.element("#uploadPicture").send_keys(path)
        return self

    @allure.step("Ввести адрес")
    def type_address(self, value: str) -> RegistrationPage:
        self.browser.element("#currentAddress").type(value)
        return self

    @allure.step("Выбрать регион")
    def select_state(self, value: State) -> RegistrationPage:
        self.browser.element("#state").click()
        self.browser.all("[id^='react-select-3-option']").element_by(have.exact_text(value)).click()
        return self

    @allure.step("Выбрать город")
    def select_city(self, value: City) -> RegistrationPage:
        self.browser.element("#city").click()
        self.browser.all("[id^='react-select-4-option']").element_by(have.exact_text(value)).click()
        return self

    @allure.step("Нажать на 'Submit'")
    def click_on_submit(self) -> RegistrationPage:
        self.browser.element("#submit").click()
        return self

    @property
    def registered_student_info(self) -> Collection:
        return self.browser.all(".table td:nth-child(2)")

import allure
from datetime import date
from selene.support.conditions import have

from src.models.student import Student
from src.models.gender import Gender
from src.pages.registration_page import RegistrationPage


def test_registration_form(browser, student):
    registration_page = RegistrationPage(browser)
    (
        registration_page
        .open()
        .type_first_name(student.first_name)
        .type_last_name(student.last_name)
        .type_email(student.email)
        .select_gender(student.gender)
        .type_phone_number(student.phone_number)
        .set_birthdate(student.birthdate)
        .select_subjects(*student.subjects)
        .select_hobbies(*student.hobbies)
        .upload_picture(student.picture)
        .type_address(student.address)
        .select_state(student.state)
        .select_city(student.city)
        .click_on_submit()
    )
    with allure.step("Проверить результат заполнения формы"):
        registration_page.registered_student_info.should(
            have.texts(
                *student.expected_data_list()
            )
        )


def test_registration_mandatory_fields(browser):
    student = Student(
        first_name="Jane",
        last_name="Doe",
        gender=Gender.FEMALE,
        phone_number="9876543210",
        birthdate=date(1995, 5, 15)
    )

    registration_page = RegistrationPage(browser)
    
    with allure.step("Заполнить обязательные поля"):
        (
            registration_page
            .open()
            .type_first_name(student.first_name)
            .type_last_name(student.last_name)
            .select_gender(student.gender)
            .type_phone_number(student.phone_number)
            .set_birthdate(student.birthdate)
            .click_on_submit()
        )

    with allure.step("Проверить результат заполнения формы"):
        registration_page.registered_student_info.should(
            have.texts(
                *student.expected_data_list()
            )
        )

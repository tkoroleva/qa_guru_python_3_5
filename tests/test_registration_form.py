import os

from selene import have
from selene.support.shared import browser


def test_registration_form():
    browser.open('/automation-practice-form')
    browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))

    browser.element('#firstName').type('QA')
    browser.element('#lastName').type('GURU')
    browser.element('#userEmail').type('test@qa.guru')

    browser.all('[for^=gender-radio-3]').element_by(have.text('Other')).click()
    browser.element('#userNumber').type('7999123456')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select>[value="2022"]').click()
    browser.element('.react-datepicker__month-select>[value="10"]').click()
    browser.element('.react-datepicker__day--016').click()

    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()

    browser.element('#uploadPicture').set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), '../res/logo.png.')))

    browser.element('#currentAddress').type('Russia, Moscow')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Panipat').press_enter()
    browser.element('#submit').press_enter()

    browser.element('[class^=modal-title]').should(have.text('Thanks for submitting the form'))
    browser.all('.table-responsive td:nth-child(2)').should(have.exact_texts(
        'QA GURU',
        'test@qa.guru',
        'Other',
        '7999123456',
        '16 November,2022',
        'Computer Science',
        'Reading',
        'logo.png',
        'Russia, Moscow',
        'Haryana Panipat'
    )
    )

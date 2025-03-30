from behave import *
from behave.runner import Context
from playwright.sync_api import Page, expect
import datetime
import re


@given("As an not logged user navigate to homepage")
def step_impl(context: Context):
    page: Page = context.page
    # Navigate to homepage
    page.goto("https://www.kiwi.com/en/")
    # Close all popups
    page.add_locator_handler(
        page.get_by_label("Close"), lambda locator: locator.press("Escape")
    )


@when("I select one-way trip type")
def step_impl(context: Context):
    page: Page = context.page
    page.locator('[data-test="SearchFormModesPicker-active-return"] div').filter(
        has_text="ReturnReturn"
    ).get_by_role("button").click()
    page.locator('[data-test="ModePopupOption-oneWay"]').click()
    page.wait_for_url("**/?inboundDate=no-return**")


@when("Set as departure airport RTM")
def step_impl(context: Context):
    page: Page = context.page
    page.locator('[data-test="PlacePickerInputPlace-close"]').get_by_role("img").click()
    page.wait_for_url("**/**&destination=-&origin=-**")
    page.locator(
        '[data-test="PlacePickerInput-origin"] [data-test="SearchField-input"]'
    ).fill("RTM")
    page.locator(
        '[data-test="PlacepickerModalOpened-origin"] [data-test="PlacePickerRow-city"]'
    ).filter(has_text="Rotterdam, Netherlands").click()
    page.wait_for_url("**/**&origin=rotterdam-netherlands**")


@when("Set the arrival Airport MAD")
def step_impl(context: Context):
    page: Page = context.page
    page.locator(
        '[data-test="PlacePickerInput-destination"] [data-test="SearchField-input"]'
    ).fill("MAD")
    page.locator(
        '[data-test="PlacepickerModalOpened-destination"] [data-test="PlacePickerRow-city"]'
    ).filter(has_text="Madrid, Spain").click()
    page.wait_for_url("**/**&destination=madrid-spain**")


@when("Set the departure time 1 week in the future starting current date")
def step_impl(context: Context):
    page: Page = context.page
    departure_date: datetime.date = datetime.date.today() + datetime.timedelta(days=7)
    departure_date_str: str = (
        f"{departure_date.year:04}-{departure_date.month:02}-{departure_date.day:02}"
    )
    page.locator('[data-test="SearchFieldDateInput"]').click()
    page.locator(
        f'[data-test="NewDatePickerOpen"] [data-test="CalendarContainer"] [data-value="{departure_date_str}"]'
    ).click()
    page.locator('[data-test="SearchFormDoneButton"]').click()
    page.wait_for_url(f"**/**&outboundDate={departure_date_str}**")


@when("Uncheck the `Check accommodation with booking.com` option")
def step_impl(context: Context):
    page: Page = context.page
    page.locator('[data-test="bookingCheckbox"] svg').click()


@when("Click the search button")
def step_impl(context: Context):
    page: Page = context.page
    page.locator('[data-test="LandingSearchButton"]').click()


@then("I am redirected to search results page")
def step_impl(context: Context):
    page: Page = context.page
    expect(page).to_have_url(re.compile(r".*/search/results/.*"))

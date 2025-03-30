from behave import fixture, use_fixture
from behave.model import Scenario
from behave.runner import Context
from playwright.sync_api import Browser, BrowserContext, sync_playwright


@fixture
def playwright_chromium_runner(context: Context):
    with sync_playwright() as playwright:
        browser: Browser = playwright.chromium.launch(headless=False)
        browser_context: BrowserContext = browser.new_context()
        context.page = browser_context.new_page()
        yield
        context.page
        browser_context.close()
        browser.close()


@fixture
def playwright_firefox_runner(context: Context):
    with sync_playwright() as playwright:
        browser: Browser = playwright.firefox.launch(headless=False)
        browser_context: BrowserContext = browser.new_context()
        context.page = browser_context.new_page()
        yield
        context.page
        browser_context.close()
        browser.close()


@fixture
def playwright_webkit_runner(context: Context):
    with sync_playwright() as playwright:
        browser: Browser = playwright.webkit.launch(headless=False)
        browser_context: BrowserContext = browser.new_context()
        context.page = browser_context.new_page()
        yield
        context.page
        browser_context.close()
        browser.close()


def before_scenario(context: Context, scenario: Scenario):
    use_fixture(playwright_chromium_runner, context)

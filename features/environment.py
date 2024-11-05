import allure
import yaml

from playwright.sync_api import sync_playwright

def before_all(context):
    try:
        env = context.config.userdata.get("STAGING", "staging").lower()
        config_file = f"config/{env}.yml"
        with open(config_file, 'r') as file:
            config_data = yaml.safe_load(file)
        for key, value in config_data.items():
            if key not in context.config.userdata:
                context.config.userdata[key] = value
        headless = context.config.userdata.get("headless", True)
        slow_mo = context.config.userdata.get("slow_mo")
        channel = context.config.userdata.get("channel")
        args = context.config.userdata.get("args")
        if isinstance(headless, str):
            headless = headless.lower() == "true"
        context.driver = sync_playwright().start()
        context.browser = context.driver.chromium.launch(headless=headless, slow_mo=slow_mo, channel=channel, args=args)
    except Exception as e:
        raise AssertionError(e)

def before_scenario(context, scenario):
    try:
        context.page = context.browser.new_page()
    except Exception as e:
        raise AssertionError(e)

def before_step(context, step):
    try:
        context.step = step
    except Exception as e:
        raise AssertionError(e)

def after_step(context, step):
    if step.status == "failed":
        try:
            screenshot_bytes = context.page.screenshot()
            allure.attach(screenshot_bytes, name="screenshot", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            raise AssertionError(e)

def after_scenario(context, scenario):
    try:
        if hasattr(context, 'page'):
            context.page.close()
    except Exception as e:
        raise AssertionError(e)

def after_all(context):
    try:
        if hasattr(context, 'browser'):
            context.browser.close()
        if hasattr(context, 'driver'):
            context.driver.stop()
    except Exception as e:
        raise AssertionError(e)

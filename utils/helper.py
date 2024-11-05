import os
import random
import string
import yaml

from behave.configuration import Configuration
from playwright.sync_api import Locator, expect

def load_timeout_from_yaml():
    env = os.getenv("STAGING", "staging").lower()
    yaml_file = f"config/{env}.yml"
    try:
        with open(yaml_file, "r") as file:
            config_data = yaml.safe_load(file)
        return config_data.get("timeout", 5000)
    except Exception as e:
        raise AssertionError(e)

global_timeout = load_timeout_from_yaml()

expect.set_options(timeout=global_timeout)

def get_userdata_value(context, key: str, default=None):
    config: Configuration = context.config
    return config.userdata.get(key, default)

def perform_action(locator: Locator = None, action: str = None, fill_value: str = None):
    if not locator:
        raise AssertionError("Locator must be provided.")
    if action is None:
        return locator
    action = action.lower()
    locator.scroll_into_view_if_needed()
    if action == "click":
        locator.click(timeout=global_timeout)
    elif action == "fill" and fill_value:
        locator.fill(fill_value, timeout=global_timeout)
    elif action == "type" and fill_value:
        locator.type(fill_value, timeout=global_timeout)
    elif action == "press" and fill_value:
        locator.press(fill_value, timeout=global_timeout)
    else:
        raise AssertionError(f"Invalid action '{action}' or missing fill_value for action '{action}'")
    return locator

def generate_email(length=12, domain="gmail.com"):
    char_set = string.ascii_lowercase + string.digits
    username = random.choice(string.ascii_lowercase)
    username += ''.join(random.choices(char_set, k=length - 2))
    username += random.choice(string.ascii_lowercase)
    username += f'@{domain}'
    return username

def generate_password(length=12):
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice('!@#$%&*')
    all_characters = string.ascii_letters + string.digits + '!@#$%&*'
    remaining_length = length - 4
    random_chars = ''.join(random.choice(all_characters) for _ in range(remaining_length))
    password = upper + lower + digit + special + random_chars
    password = ''.join(random.sample(password, len(password)))
    return password

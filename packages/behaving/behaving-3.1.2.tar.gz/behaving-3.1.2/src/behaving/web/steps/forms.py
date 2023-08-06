import base64
import os

from behave import then, when
from behaving.personas.persona import persona_vars
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from splinter.exceptions import ElementDoesNotExist

# Selenium 3 does not account for base64 no longer using encodestring.
# Monkey patch base64 to make it compatible seems the easiest.
base64.encodestring = base64.encodebytes


def find_by_name_or_id(context, selector):
    el = context.browser.find_by_name(selector)
    if not el:
        el = context.browser.find_by_id(selector)
    assert el, "Element with name or id {selector} not found"
    return el.first


@when(u'I fill in "{name}" with "{value}"')
@persona_vars
def fill_in_elem_by_name(context, name, value):
    # Chrome does not clear, so we need to do manually
    if context.browser.driver_name == "Chrome":
        context.execute_steps(f'When I clear field "{name}"')
    el = find_by_name_or_id(context, name)
    el.fill(value)


@when(u'I clear field "{name}"')
@persona_vars
def i_clear_field(context, name):
    el = find_by_name_or_id(context, name)
    # Chrome does not clear, so we need to do manually
    if context.browser.driver_name == "Chrome" and el._element.get_attribute(
        "type"
    ) in [
        "email",
        "textarea",
        "text",
        "password",
        "tel",
        "number",
    ]:
        chars = len(el.value)
        for i in range(0, chars):
            el._element.send_keys(Keys.BACKSPACE)

    assert el, "Element not found"
    el.clear()


@when(u'I type "{value}" to "{name}"')
@persona_vars
def i_type_to(context, name, value):
    el = find_by_name_or_id(context, name)
    for key in el.type(value, slowly=True):
        assert key


@when(u'I choose "{value}" from "{name}"')
@persona_vars
def i_choose_in_radio(context, name, value):
    context.browser.choose(name, value)


@when(u'I check "{name}"')
@persona_vars
def i_check(context, name):
    el = find_by_name_or_id(context, name)
    el.check()


@when(u'I uncheck "{name}"')
@persona_vars
def i_uncheck(context, name):
    el = find_by_name_or_id(context, name)
    el.uncheck()


@when(u'I toggle "{name}"')
def i_toggle(context, name):
    el = find_by_name_or_id(context, name)
    if el.checked:
        el.uncheck()
    else:
        el.check()


@when(u'I select "{value}" from "{name}"')
@persona_vars
def i_select(context, value, name):
    try:
        context.browser.select(name, value)
    except ElementDoesNotExist:
        inp = context.browser.find_by_xpath(
            f"//input[@name='{name}'][@value='{value}']"
        )
        assert inp, u"Element not found"
        inp.first.check()


@when(u'I select by text "{text}" from "{name}"')
@persona_vars
def i_select_text(context, text, name):
    elem = context.browser.find_by_name(name)
    assert elem, u"Element not found"
    elem.select_by_text(text)


@when(u'I focus on "{name}"')
@persona_vars
def i_focus(context, name):
    elem = context.browser.find_by_name(name)
    assert elem, u"Element not found"
    context.browser.execute_script(
        f'document.getElementsByName("{name}")[0].focus();'
    )


@when(u'I press "{name}"')
@persona_vars
def i_press(context, name):
    element = context.browser.find_by_xpath(
        (
            "//*[@id='%(name)s']|"
            "//*[@name='%(name)s']|"
            "//button[contains(string(), '%(name)s')]|"
            "//input[@type='button' and contains(string(), '%(name)s')]|"
            "//input[@type='button' and contains(@value, '%(name)s')]|"
            "//input[@type='submit' and contains(@value, '%(name)s')]|"
            "//a[contains(string(), '%(name)s')]"
        )
        % {"name": name}
    )
    assert element, u"Element not found"
    element.first.click()


@when(u'I press the element with xpath "{xpath}"')
@persona_vars
def i_press_xpath(context, xpath):

    button = context.browser.find_by_xpath(xpath)
    assert button, u"Element not found"
    button.first.click()


@when('I attach the file "{path}" to "{name}"')
@persona_vars
def i_attach(context, name, path):
    if not os.path.exists(path):
        path = os.path.join(context.attachment_dir, path)
        if not os.path.exists(path):
            assert False, u"File not found"
    try:
        context.browser.find_by_name(name).first._element.clear()
    except ElementNotInteractableException:
        pass
    context.browser.attach_file(name, path)


@when('I set the inner HTML of the element with id "{id}" to "{contents}"')
@persona_vars
def set_html_content_to_element_with_id(context, id, contents):
    assert context.browser.evaluate_script(
        f"document.getElementById('{id}').innerHTML = '{contents}'"
    ), u"Element not found or could not set HTML content"


@when('I set the inner HTML of the element with class "{klass}" to "{contents}"')
@persona_vars
def set_html_content_to_element_with_class(context, klass, contents):
    assert context.browser.evaluate_script(
        f"document.getElementsByClassName('{klass}')[0].innerHTML = '{contents}'"
    ), u"Element not found or could not set HTML content"


@then(u'field "{name}" should have the value "{value}"')
@then(u'field "{name}" should have the value "{value}" within {timeout:d} seconds')
@persona_vars
def field_has_value_within_timeout(context, name, value, timeout=None):
    el = context.browser.find_by_xpath(
        ("//*[@id='%(name)s']|" "//*[@name='%(name)s']") % {"name": name}, wait_time=timeout
    )
    assert el, u"Element not found"
    assert el.first.value == value, "Values do not match, expected %s but got %s" % (
        value,
        el.first.value,
    )


@then(u'field "{name}" should be empty')
@persona_vars
def field_is_empty(context, name):
    el = context.browser.find_by_xpath(
        ("//*[@id='%(name)s']|" "//*[@name='%(name)s']") % {"name": name}
    )
    assert el, u"Element not found"
    assert el.first.value == "", u"Field is not empty"


@then(u'"{name}" should be enabled')
@persona_vars
def is_enabled(context, name):
    el = context.browser.find_by_xpath(
        ("//*[@id='%(name)s']|" "//*[@name='%(name)s']") % {"name": name}
    )
    assert el, u"Element not found"
    assert el.first._element.is_enabled()


@then(u'"{name}" should be disabled')
@then(u'"{name}" should not be enabled')
@persona_vars
def is_disabled(context, name):
    el = context.browser.find_by_xpath(
        ("//*[@id='%(name)s']|" "//*[@name='%(name)s']") % {"name": name}
    )
    assert el, u"Element not found"
    assert not el.first._element.is_enabled()


@then(u'field "{name}" should be valid')
@persona_vars
def field_is_valid(context, name):
    assert context.browser.find_by_name(name), u"Element not found"
    assert context.browser.evaluate_script(
        f"document.getElementsByName('{name}')[0].checkValidity()"
    ), "Field is invalid"


@then(u'field "{name}" should be invalid')
@then(u'field "{name}" should not be valid')
@persona_vars
def field_is_invalid(context, name):
    assert context.browser.find_by_name(name), u"Element not found"
    assert not context.browser.evaluate_script(
        f"document.getElementsByName('{name}')[0].checkValidity()"
    ), "Field is valid"


@then(u'field "{name}" should be required')
@persona_vars
def field_is_required(context, name):
    assert context.browser.find_by_name(name), u"Element not found"
    assert context.browser.evaluate_script(
        f"document.getElementsByName('{name}')[0].getAttribute('required')"
    ), "Field is not required"


@then(u'field "{name}" should not be required')
@persona_vars
def field_is_not_required(context, name):
    assert context.browser.find_by_name(name), u"Element not found"
    assert not context.browser.evaluate_script(
        f"document.getElementsByName('{name}')[0].getAttribute('required')"
    ), "Field is required"


@when(u'I send "{key}" to "{name}"')
@persona_vars
def press_enter(context, key, name):
    element = context.browser.find_by_name(name)
    key = getattr(Keys, key, None)
    assert element, u"Element not found"
    assert key, u"Key not in selenium.webdriver.common.keys.Keys"
    element.send_keys(key)

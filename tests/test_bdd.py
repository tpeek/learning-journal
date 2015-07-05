# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from pytest_bdd import scenario, given, when, then
import journal


#
#  Scenarios
#
@scenario('features/homepage.feature',
          'The homepage lists entries for anonymous users')
def test_homepage_as_anon():
    pass


@scenario('features/homepage.feature',
          'The homepage displays relevant buttons for anonymous users')
def test_homepage_buttons_as_anon():
    pass


@scenario('features/homepage.feature',
          'The homepage allows anonymous users to view the detail page')
def test_detail_page_as_anon():
    pass


@scenario('features/homepage.feature',
          'The detail page displays relevant buttons for anonymous users')
def test_detail_buttons_as_anon():
    pass


@scenario('features/homepage.feature',
          'The homepage displays relevant buttons for authorized users')
def test_homepage_as_auth():
    pass


# @scenario('features/homepage.feature',
#           'The detail page displays relevant buttons for authorized users')
# def test_detail_buttons_as_auth():
#     pass
@scenario('features/homepage.feature',
          'An authorized user can edit an entry')
def test_edit_as_auth():
    pass


#
#  Givens
#
@given('an anonymous user')
def an_anonymous_user(app):
    pass


@given('an authorized user')
def an_authorized_user(app, auth_req):
    app.post('/login', {'username': 'admin', 'password': 'secret'},
             status='*')


@given('a list of three entries')
def create_entries(db_session):
    title_template = "Title {}"
    text_template = "Entry Text {}"
    for x in range(3):
        journal.Entry.write(
            title=title_template.format(x + 1),
            text=text_template.format(x + 1),
            session=db_session)
        db_session.flush()


#
#  Whens
#
@when('the user visits the homepage')
def homepage(app):
    response = app.get('/')
    return response


@when('the user clicks on an entry')
def detail_page(app):
    response = app.get('/detail/1')
    return response


@when('the user visits the edit page')
def edit_page(app):
    response = app.get('/edit/1')
    print response.html
    return response


@when('the user edits an entry')
def edit(app, edit_page):
    pass
    # app.post('/edit/1', {'title': 'Test', 'text': 'This is new'},
    #          status='*')


#
#  Thens
#
@then('they see a list of three entries')
def check_entry_list(homepage):
    html = homepage.html
    entries = html.find_all(class_='post')
    assert len(entries) == 3


@then('they will see the detail page')
def see_detail_page(detail_page):
    html = detail_page.html
    text = html.find_all(class_='text')
    title = html.find_all(class_='title')
    assert len(title) == 1
    assert len(text) == 1


#
#  Then Buttons
#
@then('they will see a logout button')
def logout_button(homepage):
    html = homepage.html
    button = html.find_all(id='logout')
    assert len(button) == 1


@then('they will not see a logout button')
def no_logout_button(homepage):
    html = homepage.html
    button = html.find_all(id='logout')
    assert len(button) == 0


@then('they will see a login button')
def login_button(homepage):
    html = homepage.html
    button = html.find_all(id='login')
    assert len(button) == 1


@then('they will not see a login button')
def no_login_button(homepage):
    html = homepage.html
    button = html.find_all(id='login')
    assert len(button) == 0


@then('they will see an add button')
def add_button(homepage):
    html = homepage.html
    button = html.find_all(id='add')
    assert len(button) == 1


@then('they will not see an add button')
def no_add_button(homepage):
    html = homepage.html
    button = html.find_all(id='add')
    assert len(button) == 0


@then('they will see an edit button')
def edit_button(homepage):
    html = homepage.html
    button = html.find_all(id='edit')
    assert len(button) == 1


@then('they will not see an edit button')
def no_edit_button(homepage):
    html = homepage.html
    button = html.find_all(id='edit')
    assert len(button) == 0


@then('the detail page will change')
def test_edit(app):
    response = app.get('/')
    print response.html
#     html = detail_page.html
#     print html
    # title = html.find_all(class_='title')
    # text = html.find_all(class_='text')
    # assert title == "Test"
    # assert text == "This is news"

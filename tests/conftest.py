# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import pytest
from pytest_bdd import given
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from pyramid import testing
from cryptacular.bcrypt import BCRYPTPasswordManager
from bs4 import BeautifulSoup

import journal

TEST_DATABASE_URL = os.environ.get(
    'DATABASE_URL',
    'postgresql://tyler:tyler@localhost:5432/test-learning-journal'
)
os.environ['DATABASE_URL'] = TEST_DATABASE_URL


@pytest.fixture(scope='session')
def connection(request):
    engine = create_engine(TEST_DATABASE_URL)
    journal.Base.metadata.create_all(engine)
    connection = engine.connect()
    journal.DBSession.registry.clear()
    journal.DBSession.configure(bind=connection)
    journal.Base.metadata.bind = engine
    request.addfinalizer(journal.Base.metadata.drop_all)
    return connection


@pytest.fixture()
def db_session(request, connection):
    from transaction import abort
    trans = connection.begin()
    request.addfinalizer(trans.rollback)
    request.addfinalizer(abort)

    from journal import DBSession
    return DBSession


@pytest.fixture()
def app(db_session):
    from journal import main
    from webtest import TestApp
    app = main()
    return TestApp(app)


@pytest.fixture()
def entry(db_session):
    entry = journal.Entry.write(
        title='Test Title',
        text='Test Entry Text',
        session=db_session
    )
    db_session.flush()
    return entry


@pytest.fixture()
def homepage(app):
    return app.get('/')

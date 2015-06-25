# coding: utf-8
foo = 'bar'
foo
from journal import DATABASE_URL
DATABASE_URL
from sqlalchemy import create_engine
engine = create_engine(DATABASE_URL, echo=True)
engine
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
session
session.bind
from journal import Entry
from __future__ import unicode_literals
e1 = Entry()
e1.title = "There's something about sqlalchemy"
e1.text = "It's such a wonderful system for interacting with a database"
e1
e1.text
session.new
session.dirty
session.add(e1)
session.new
session.commit()
results = session.query(Entry)
results
str(results)
results=results.all()
results
type(results)
for entry in results:
    print entry.title
    print "\t{}.formate(entry.text)
    print "\t{}.format(entry.text)
    
for entry in results:
    print entry.title
    print "\t{}.formate(entry.text)
    print "\t{}.format(entry.text)
    
results = session.query(Entry).order_by(Entry.title).all()
for entry in results:
    print "{}: {}".format(entry.id, entry.title)
    print "\t{}".format(entry.text)
    
results = session.query(Entry.order_by(Entry.created.desc()).all())
results = session.query(Entry.order_by(Entry).created.desc()).all()
results = session.query(Entry).order_by(Entry.created.desc()).all()
results.all()
results = session.query(Entry).order_by(Entry.created.desc())
results.all()
for entry in results:
    print "{}: {}".format(entry.id, entry.title)
    print "\t{}".format(entry.text)
    
results.count()
results.session.query(Entry).get(1)
results
results.id
results = results.session.query(Entry).get(1)
results
results.id
results
results = session.query(Entry).order_by(Entry.created.desc())
results = results.filter(Entry.id == 2)
results
str(results)
results = results.filter(Entry.id == 1)
results.one()
get_ipython().magic(u'save sql_exploration.py 1-56')

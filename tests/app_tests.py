from nose.tools import *
from app import app


app.config['TESTING']=True
web=app.test_client()
def test_index():
    rv=web.get('/',follow_redirect=True)
    assert_equal(rv.status_code,200)

    rv=web.get('/game',follow_redirect=True)
    assert_equal(rv.status_code,200)
    assert_in(b'Fill out This Form',rv.data)

from blazeweb.globals import ag
from blazeweb.testing import TestApp

class TestTemplates(object):
    @classmethod
    def setup_class(cls):
        cls.ta = TestApp(ag.wsgi_test_app)

    def test_title_tag(self):
        r = self.ta.get('/')
        assert 'Index | TemplatingBWP Application Administration' in r
        assert 'Change Password' not in r

        r = self.ta.get('/login')
        r = r.follow()
        assert 'Change Password' in r

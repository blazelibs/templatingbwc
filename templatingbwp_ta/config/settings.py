from os import path

from blazeweb.config import DefaultSettings

basedir = path.dirname(path.dirname(__file__))
app_package = path.basename(basedir)

class Default(DefaultSettings):
    def init(self):
        self.dirs.base = basedir
        self.app_package = app_package
        DefaultSettings.init(self)

        self.init_routing()

        self.add_plugin(app_package, 'templating', 'templatingbwp')

        self.template.default = 'templating:admin/layout.html'

        self.name.full = 'TemplatingBWP Application'
        self.name.short = 'TemplatingBWP App'

    def init_routing(self):
        self.add_route('/', endpoint='index.html')
        self.add_route('/authorized-user', endpoint='AuthorizedUser')

class Dev(Default):
    def init(self):
        Default.init(self)
        self.apply_dev_settings()

class Test(Default):
    def init(self):
        Default.init(self)
        self.apply_test_settings()

try:
    from site_settings import *
except ImportError, e:
    if 'No module named site_settings' not in str(e):
        raise

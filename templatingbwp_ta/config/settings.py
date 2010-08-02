import logging
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

        # this plugins are only used for testing, they are not required
        # to use templatingbwp
        self.add_plugin(app_package, 'common', 'commonbwp')
        self.add_plugin(app_package, 'sqlalchemy', 'sqlalchemybwp')
        self.add_plugin(app_package, 'datagrid', 'datagridbwp')

        self.template.default = 'templating:admin/layout.html'
        self.template.admin = 'templating:admin/layout.html'

        self.name.full = 'TemplatingBWP Application'
        self.name.short = 'TemplatingBWP App'

        # database
        self.db.url = 'sqlite:///%s' % path.join(self.dirs.data, 'application.db')

    def init_routing(self):
        self.add_route('/', endpoint='index.html')
        self.add_route('/typography', endpoint='typography.html')
        self.add_route('/login', endpoint='Login')
        self.add_route('/logout', endpoint='Logout')
        self.add_route('/user-messages', endpoint='UserMessages')
        self.add_route('/boxes', endpoint='boxes.html')
        self.add_route('/boxes-and-text', endpoint='boxes_and_text.html')
        self.add_route('/boxes-and-boxes', endpoint='boxes_and_boxes.html')
        self.add_route('/modals', endpoint='modals.html')
        self.add_route('/tables', endpoint='tables.html')
        self.add_route('/forms', endpoint='forms.html')
        self.add_route('/jquery-ui', endpoint='jquery_ui.html')
        self.add_route('/icons', endpoint='icons.html')
        self.add_route('/make/<action>', endpoint='MakeCrud')
        self.add_route('/make/<action>/<int:objid>', endpoint='MakeCrud')

class Dev(Default):
    def init(self):
        Default.init(self)
        self.apply_dev_settings()

    def debug_to_stdout(self):
        format_str = "%(name)s - %(message)s"
        formatter = logging.Formatter(format_str)

        stdout_handler = logging.StreamHandler()
        stdout_handler.setLevel(logging.DEBUG)
        stdout_handler.setFormatter(formatter)
        bwh = logging.getLogger('blazeweb.middleware')
        bwh.addHandler(stdout_handler)
        bwh.setLevel(logging.DEBUG)

class Test(Default):
    def init(self):
        Default.init(self)
        self.apply_test_settings()

try:
    from site_settings import *
except ImportError, e:
    if 'No module named site_settings' not in str(e):
        raise

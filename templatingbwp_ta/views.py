from blazeweb.globals import user
from blazeweb.views import View
from blazeweb.utils import redirect

class Login(View):
    def default(self):
        user.is_authenticated = True
        user.display_name = 'testuser'
        user.add_message('success', 'You have been logged in.')
        redirect('/')

class Logout(View):
    def default(self):
        user.is_authenticated = False
        user.display_name = None
        user.add_message('success', 'You have been logged out.')
        redirect('/')

class UserMessages(View):
    def default(self):
        types = 'error', 'warning', 'notice', 'success'
        for type in types:
            user.add_message(type, 'This is a %s message.' % type)
        self.render_template()

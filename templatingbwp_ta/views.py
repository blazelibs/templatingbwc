from blazeweb.globals import user
from blazeweb.views import View

class AuthorizedUser(View):
    def default(self):
        user.is_authenticated = True
        user.display_name = 'testuser'
        self.render_template()

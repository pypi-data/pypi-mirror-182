from ...fields.grid import VStack
from ...fields.inputs.text import InputTextField
from ...page import Page


class LoginPage(Page):
    def __init__(self):
        super(LoginPage, self).__init__()
        self.fields = VStack([
            InputTextField("user_id"),
            InputTextField("password"),
        ])

    def get_content(self, **kwargs):
        return self.fields.generate()

    def process(self, **data):
        user_id = data['user_id']
        password = data['password']

        self.distributor.generate_token(user_id, password)

        return self.redirect_url("/job",
                                 user_id=user_id,
                                 obj_id=0)

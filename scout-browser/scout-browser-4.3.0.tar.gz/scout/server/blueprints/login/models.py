# -*- coding: utf-8 -*-
from flask_login import UserMixin


class LoginUser(UserMixin):

    def __init__(self, user_data):
        """Create a new user object."""
        self.roles = []
        for key, value in user_data.items():
            setattr(self, key, value)

    def get_id(self):
        return self.email

    @property
    def is_admin(self):
        """Check if the user is admin."""
        return 'admin' in self.roles

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user_info, timestamp):
        return (
                six.text_type(user_info[0]) + six.text_type(timestamp) + six.text_type(user_info[1])
        )


recruitment_token = TokenGenerator()

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

from django.utils import six
class TokenGenerator(PasswordResetTokenGenerator):
    ''''
       We basically extended the PasswordResetTokenGenerator to create a unique token generator to confirm email addresses.
        This make use of your project's SECRET_KEY, so it is a pretty safe and reliable method.'''
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(user.is_active)
        )

account_activation_token = TokenGenerator()

from django.test import TestCase
from api.models import User


class UserTestCase(TestCase):

    user_name = ""

    def setUp(self):
        self.user_name = "foo"
        self.user = User(name=self.user_name)

    def test_model_can_create_a_user(self):
        old_count = User.objects.count()
        self.user.save()
        new_count = User.objects.count()
        self.assertNotEqual(old_count, new_count)


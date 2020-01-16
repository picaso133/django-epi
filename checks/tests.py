from django.test import TestCase
from .models import Check
class CheckTestCase(TestCase):
    def setUp(self):
        Check.objects.create(number=1423, date="1-10-2019", pay_to="Unicorn Consulting", pay_for="1955 Leavenworth", description="", amount=10135.0)


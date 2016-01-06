from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
                name='Fabrício Severo',
                cpf='12345678901',
                email='severo.fabricio@gmail.com',
                phone='00-1111-2222'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription mus have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)
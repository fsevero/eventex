from datetime import datetime
from django.shortcuts import resolve_url as r
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

    def test_str(self):
        self.assertEqual('Fabrício Severo', str(self.obj))

    def test_paid_default_to_false(self):
        """By default, paid must be false"""
        self.assertEqual(False, self.obj.paid)

    def test_absolute_url(self):
        url = r('subscriptions:detail', self.obj.pk)
        self.assertEqual(url, self.obj.get_absolute_url())
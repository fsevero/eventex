from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name="Fabrício Severo", cpf="12345678901",
                    email="severo.fabricio@gmail.com", phone="00-1111-2222")
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscript_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'severo.fabricio@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Fabrício Severo',
            '12345678901',
            'severo.fabricio@gmail.com',
            '00-1111-2222',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
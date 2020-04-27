# coding: utf-8

from unittest import TestCase

from core.business_logic import AddBusinessLogic


class AddBusinessLogicTestCase(TestCase):

    def test__execute__pass_two_integers__result_correct(self):
        bl = AddBusinessLogic()

        self.assertEqual(bl.execute(1, 1), 2)

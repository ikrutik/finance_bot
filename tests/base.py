from unittest import TestCase


class BaseTestUseCase(TestCase):
    def setUp(self) -> None:
        super().setUp()

    def tearDown(self) -> None:
        super().tearDown()

    def test_base_case(self):
        self.assertEqual(str(), str())

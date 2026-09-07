from django.core.checks import run_checks
from django.test import SimpleTestCase


class ProjectSmokeTest(SimpleTestCase):
    def test_django_system_checks_pass(self) -> None:
        self.assertEqual(run_checks(), [])

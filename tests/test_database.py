from django.db import connection
from django.test import SimpleTestCase


class DatabaseConnectivityTest(SimpleTestCase):
    databases = {"default"}

    def test_configured_database_accepts_queries(self) -> None:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            self.assertEqual(cursor.fetchone(), (1,))

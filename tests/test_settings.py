import json
import os
import subprocess
import sys
from pathlib import Path

from django.test import SimpleTestCase


ENVIRONMENT_VARIABLES = {
    "DATABASE_ENGINE",
    "DJANGO_ALLOWED_HOSTS",
    "DJANGO_DEBUG",
    "DJANGO_EMAIL_BACKEND",
    "DJANGO_MEDIA_ROOT",
    "DJANGO_SECRET_KEY",
    "DJANGO_STATIC_ROOT",
    "DJANGO_TIME_ZONE",
    "POSTGRES_DB",
    "POSTGRES_HOST",
    "POSTGRES_PASSWORD",
    "POSTGRES_PORT",
    "POSTGRES_USER",
    "REDIS_URL",
    "SQLITE_PATH",
}


class EnvironmentSettingsTests(SimpleTestCase):
    maxDiff = None

    def read_settings(self, **overrides: str) -> dict[str, object]:
        environment = os.environ.copy()
        for name in ENVIRONMENT_VARIABLES:
            environment.pop(name, None)
        environment.update(overrides)

        script = """
import json
from chorecrew import settings

print(json.dumps({
    "allowed_hosts": settings.ALLOWED_HOSTS,
    "database": settings.DATABASES["default"],
    "debug": settings.DEBUG,
    "email_backend": settings.EMAIL_BACKEND,
    "media_root": str(settings.MEDIA_ROOT),
    "redis_url": settings.REDIS_URL,
    "secret_key": settings.SECRET_KEY,
    "static_root": str(settings.STATIC_ROOT),
    "time_zone": settings.TIME_ZONE,
}, default=str))
"""
        result = subprocess.run(
            [sys.executable, "-c", script],
            check=True,
            capture_output=True,
            env=environment,
            text=True,
        )
        return json.loads(result.stdout)

    def test_safe_direct_development_defaults(self) -> None:
        configured = self.read_settings()

        self.assertTrue(configured["debug"])
        self.assertEqual(configured["allowed_hosts"], [])
        self.assertEqual(
            configured["database"]["ENGINE"], "django.db.backends.sqlite3"
        )
        self.assertEqual(
            configured["database"]["NAME"], str(Path.cwd() / "db.sqlite3")
        )
        self.assertEqual(configured["redis_url"], "redis://localhost:6379/0")
        self.assertEqual(
            configured["email_backend"],
            "django.core.mail.backends.console.EmailBackend",
        )
        self.assertEqual(configured["time_zone"], "UTC")
        self.assertEqual(configured["media_root"], str(Path.cwd() / "media"))
        self.assertEqual(
            configured["static_root"], str(Path.cwd() / "staticfiles")
        )

    def test_container_settings_come_from_the_environment(self) -> None:
        configured = self.read_settings(
            DATABASE_ENGINE="postgresql",
            DJANGO_ALLOWED_HOSTS="app.example.test, localhost",
            DJANGO_DEBUG="false",
            DJANGO_EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
            DJANGO_MEDIA_ROOT="/data/media",
            DJANGO_SECRET_KEY="test-secret",
            DJANGO_STATIC_ROOT="/data/static",
            DJANGO_TIME_ZONE="Europe/Vilnius",
            POSTGRES_DB="chores_test",
            POSTGRES_HOST="database",
            POSTGRES_PASSWORD="database-password",
            POSTGRES_PORT="55432",
            POSTGRES_USER="app_user",
            REDIS_URL="redis://cache:6380/2",
        )

        self.assertFalse(configured["debug"])
        self.assertEqual(
            configured["allowed_hosts"], ["app.example.test", "localhost"]
        )
        self.assertEqual(
            configured["database"],
            {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": "chores_test",
                "USER": "app_user",
                "PASSWORD": "database-password",
                "HOST": "database",
                "PORT": "55432",
            },
        )
        self.assertEqual(configured["redis_url"], "redis://cache:6380/2")
        self.assertEqual(
            configured["email_backend"],
            "django.core.mail.backends.locmem.EmailBackend",
        )
        self.assertEqual(configured["time_zone"], "Europe/Vilnius")
        self.assertEqual(configured["media_root"], "/data/media")
        self.assertEqual(configured["static_root"], "/data/static")
        self.assertEqual(configured["secret_key"], "test-secret")

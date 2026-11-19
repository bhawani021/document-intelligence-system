"""Tests for application configuration"""

from document_intelligence.config.settings import Settings


def test_settings_load_default_values() -> None:
    """Settings should provide expected default values."""

    settings = Settings(_env_file=None)

    assert settings.app_name == "Document Intelligence System"
    assert settings.app_env == "development"
    assert settings.log_level == "INFO"



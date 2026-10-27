# ==========================================
# Python 88 - Dependency Injection Test
# ==========================================

from config import BotSettings
from api_client import connect_to_api


# ==========================================
# 1. Test API Client with Custom Settings
# ==========================================

def test_api_client_with_custom_settings(capsys):

    # Create test configuration
    test_settings = BotSettings(
        bot_name="Invoice Test Bot",
        api_url="https://test-api.example.com",
        timeout=5,
        max_retries=0,
        log_level="DEBUG"
    )

    # Execute API client with test settings
    connect_to_api(test_settings)

    # Capture printed output
    captured = capsys.readouterr()

    # Validate expected values
    assert "https://test-api.example.com/" in captured.out
    assert "Connection timeout: 5 seconds" in captured.out
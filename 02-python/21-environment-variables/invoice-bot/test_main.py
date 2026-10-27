# ==========================================
# Python 88 - Bot Workflow Integration Test
# ==========================================

from config import BotSettings
from main import run_bot


# ==========================================
# 1. Test Complete Bot Workflow
# ==========================================

def test_complete_bot_workflow(capsys):

    # ==========================================
    # 2. Create Test Configuration
    # ==========================================

    test_settings = BotSettings(
        bot_name="Invoice Integration Test Bot",
        api_url="https://test-api.example.com",
        timeout=10,
        max_retries=2,
        log_level="DEBUG"
    )

    # ==========================================
    # 3. Execute Complete Workflow
    # ==========================================

    run_bot(test_settings)

    # ==========================================
    # 4. Capture Bot Output
    # ==========================================

    captured = capsys.readouterr()

    # ==========================================
    # 5. Validate Main Bot
    # ==========================================

    assert "Starting: Invoice Integration Test Bot" in captured.out

    # ==========================================
    # 6. Validate API Client
    # ==========================================

    assert "https://test-api.example.com/" in captured.out

    assert "Connection timeout: 10 seconds" in captured.out

    # ==========================================
    # 7. Validate Invoice Processor
    # ==========================================

    assert "Processing with bot: Invoice Integration Test Bot" in captured.out

    assert "Maximum retries: 2" in captured.out

    # ==========================================
    # 8. Validate Workflow Completion
    # ==========================================

    assert "Invoice Bot completed." in captured.out
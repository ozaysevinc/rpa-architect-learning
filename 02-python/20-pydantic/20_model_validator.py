# ==========================================
# Python 87 - Model Validator
# ==========================================

from typing import Self
from pydantic import BaseModel, Field, model_validator, ValidationError


# ==========================================
# 1. Define Bot Schedule Model
# ==========================================

class BotSchedule(BaseModel):
    bot_name: str
    start_hour: int = Field(ge=0, le=23)
    end_hour: int = Field(ge=0, le=23)

    # ==========================================
    # 2. Validate Working Hours
    # ==========================================

    @model_validator(mode="after")
    def validate_schedule(self) -> Self:

        if self.start_hour >= self.end_hour:
            raise ValueError(
                "Start hour must be earlier than end hour"
            )

        return self


# ==========================================
# 3. Create Bot Schedule
# ==========================================

try:
    schedule = BotSchedule(
        bot_name="Finance Bot",
        start_hour=9,
        end_hour=18
    )

    print("Schedule validated successfully.")
    print(f"Bot: {schedule.bot_name}")
    print(f"Working Hours: {schedule.start_hour}:00 - {schedule.end_hour}:00")

except ValidationError as error:
    print("Schedule validation failed.")
    print(error)
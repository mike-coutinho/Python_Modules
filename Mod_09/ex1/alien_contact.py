from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Optional, Self
from enum import Enum


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validation(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC' (Alien Contact)")

        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contacts must be verified")

        if (self.contact_type == ContactType.telepathic
                and self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")

        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages")

        return self


def custom_rules() -> None:
    print("1. Testing Contact ID validation...")
    try:
        AlienContact(
            contact_id="teste",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'].replace("Value error, ", ""))

    print("\n2. Testing Physical contact validation...")
    try:
        AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.physical,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=False
        )
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'].replace("Value error, ", ""))

    print("\n3. Testing Telepathic contact validation...")
    try:
        AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'].replace("Value error, ", ""))

    print("\n4. Testing Strong signals validation...")
    try:
        AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            is_verified=True
        )
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'].replace("Value error, ", ""))


def main():
    print("Alien Contact Log Validation")
    print("=================================")

    contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime.now(),
        location="Area 51, Nevada",
        contact_type=ContactType.radio,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=True
    )
    print("Valid contact record:")
    print("ID:", contact.contact_id)
    print("Type:", contact.contact_type)
    print("Location:", contact.location)
    print("Signal:", contact.signal_strength)
    print("Duration:", contact.duration_minutes)
    print("Witnesses:", contact.witness_count)
    print("Message:", contact.message_received)

    print("\n=================================")
    print("Expected validation error:")

    custom_rules()


if __name__ == "__main__":
    main()

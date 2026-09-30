from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Self


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validation(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        if not any(
            member.rank in {Rank.commander, Rank.captain}
                for member in self.crew):
            raise ValueError("Must have at least one Commander or Captain")

        experienced_count = sum(
            1 for member in self.crew if member.years_experience > 5)
        if self.duration_days > 365 and experienced_count < len(self.crew) / 2:
            raise ValueError(
                "Long missions (> 365 days) require at least"
                "50% experienced crew (5+ years)")

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def custom_rules(crew_members: list[CrewMember]) -> None:
    print("1. Testing Mission ID validation...")
    try:
        SpaceMission(
            mission_id="12345",
            mission_name="Mars Exploration",
            destination="Mars",
            launch_date=datetime(2026, 3, 15),
            duration_days=30,
            crew=crew_members,
            budget_millions=800.0
        )
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'].replace("Value error, ", ""))

    print("\n2. Testing at least one Commander or Captain validation...")
    crew_members[0].rank = Rank.officer
    try:
        SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Exploration",
            destination="Mars",
            launch_date=datetime(2026, 3, 15),
            duration_days=30,
            crew=crew_members,
            budget_millions=800.0
        )
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'].replace("Value error, ", ""))
    crew_members[0].rank = Rank.commander

    print("\n3. Testing Long missions need 50% experienced crew validation...")
    crew_members[0].years_experience = 1
    crew_members[1].years_experience = 1
    crew_members[2].years_experience = 7
    try:
        SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Exploration",
            destination="Mars",
            launch_date=datetime(2026, 3, 15),
            duration_days=366,
            crew=crew_members,
            budget_millions=800.0
        )
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'].replace("Value error, ", ""))
    crew_members[0].years_experience = 7
    crew_members[1].years_experience = 6
    crew_members[2].years_experience = 9

    print("\n4. Testing All crew members must be active validation...")
    crew_members[1].is_active = False
    try:
        SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Exploration",
            destination="Mars",
            launch_date=datetime(2026, 3, 15),
            duration_days=366,
            crew=crew_members,
            budget_millions=800.0
        )
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'].replace("Value error, ", ""))
    crew_members[1].is_active = True


def main():
    print("Space Mission Crew Validation")
    print("=================================")

    crew_members = [
        CrewMember(
            member_id="M001",
            name="Sarah Connor",
            rank=Rank.commander,
            age=35,
            specialization="Mission Command",
            years_experience=7
        ),
        CrewMember(
            member_id="M002",
            name="John Smith",
            rank=Rank.lieutenant,
            age=37,
            specialization="Navigation",
            years_experience=6
        ),
        CrewMember(
            member_id="M003",
            name="Alice Johnson",
            rank=Rank.officer,
            age=38,
            specialization="Engineering",
            years_experience=9
        )
    ]

    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2024-06-01",
        duration_days=900,
        crew=crew_members,
        budget_millions=2500.0
    )

    print("Valid mission created:")
    print("Mission:", mission.mission_name)
    print("ID:", mission.mission_id)
    print("Destination:", mission.destination)
    print("Duration:", mission.duration_days, "days")
    print(f"Budget: ${mission.budget_millions}M")
    print("Crew Members:")
    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank.value}) - {member.specialization}")

    print("\n=================================")
    print("Expected validation error:")

    custom_rules(crew_members)


if __name__ == "__main__":
    main()

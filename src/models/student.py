from datetime import date

from pydantic import BaseModel

from src.models.city import City
from src.models.gender import Gender
from src.models.hobbies import Hobby
from src.models.state import State
from src.models.subject import Subject


class Student(BaseModel):
    first_name: str
    last_name: str
    email: str
    gender: Gender
    phone_number: str
    birthdate: date
    subjects: list[Subject]
    hobbies: list[Hobby]
    picture: str
    address: str
    state: State
    city: City

    def expected_data_list(self) -> list[str | Gender]:
        return [
            f"{self.first_name} {self.last_name}",
            self.email,
            self.gender,
            self.phone_number,
            f"{self.birthdate.day} {self.birthdate.strftime('%B')},{self.birthdate.year}",
            ", ".join(self.subjects),
            ", ".join(self.hobbies),
            self.picture,
            self.address,
            f"{self.state} {self.city}"
        ]

from dataclasses import dataclass
from typing import List


@dataclass
class CompanyDTO:
    title: str
    number_of_employees: int


@dataclass
class ArchitectorDTO:
    name: str
    age: int
    is_active: bool
    company: List[CompanyDTO]

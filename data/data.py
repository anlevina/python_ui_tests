from dataclasses import dataclass


@dataclass
class Person:
    first_name: str = None
    last_name: str = None
    full_name: str = None
    email: str = None
    age: int = None
    current_address: str = None
    permanent_address: str = None
    salary: int = None
    department: str = None
    mobile: str = None


@dataclass
class Color:
    color_name: list = None


@dataclass
class Date:
    day: str = None
    month: str = None
    year: str = None
    time:  str = None

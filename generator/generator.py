import random
from pathlib import Path

from faker import Faker

from data.data import Person
from data.data import Color
from data.data import Date

faker_en = Faker('en_US')
Faker.seed()


def generated_person():
    yield Person(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        full_name=faker_en.first_name() + ' ' + faker_en.last_name(),
        email=faker_en.email(),
        mobile=faker_en.msisdn(),
        age=random.randint(1, 66),
        current_address=faker_en.address().replace('\n', ' '),
        permanent_address=faker_en.address().replace('\n', ' '),
        salary=random.randint(0, 666666),
        department=faker_en.job()
    )


def generated_file():

    file_name = f'file_for_test{random.randint(0, 10)}.txt'
    base_dir = Path.cwd()
    path = base_dir / file_name
    base_dir.mkdir(parents=True, exist_ok=True)
    file = open(path, 'w+')
    file.write(f'Hello {random.randint(0, 666)}')
    file.close()
    return file_name, str(path)


def generated_subject():

    subjects = ['Hindi', 'English', 'Maths', 'Physics', 'Chemistry', 'Biology', 'Computer Science', 'Commerce',
                'Accounting', 'Economics', 'Arts', 'Social Studies', 'History', 'Civics']
    random_subjects = random.sample(subjects, k=random.randint(1,13))
    return random_subjects


def generated_state_and_city():

    states_list = ['NCR', 'Uttar Pradesh', 'Haryana', 'Rajasthan']
    cities_dict = {
        'NCR': ['Delhi', 'Gurgaon', 'Noida'],
        'Uttar Pradesh': ['Agra', 'Lucknow', 'Merrut'],
        'Haryana': ['Karnal', 'Panipat'],
        'Rajasthan': ['Jaipur', 'Jaiselmer']
    }

    random_state = states_list[random.randint(0, len(states_list)-1)]
    cities = cities_dict[f'{random_state}']
    random_city = cities[(random.randint(0, len(cities_dict[f'{random_state}']) - 1))]

    return random_state, random_city


def generated_color():
    yield Color(
        color_name=['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Black', 'White',
                    'Voilet', 'Indigo', 'Magenta', 'Aqua']
    )


def generated_date():

    hours = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11',
             '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
    minutes = ['00', '15', '30', '45']

    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time=f'{hours[random.randint(0, 23)]}:{minutes[random.randint(0, 3)]}'
    )
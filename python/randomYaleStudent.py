# Random generate a yale student. Used for the Random Person Search Committee
import yalies
import random
from dotenv import load_dotenv
import os

load_dotenv()
api = yalies.API(os.environ.get("YALIES_API_KEY"))

all_people = api.people(filters={'school_code': 'YC'})
person = random.choice(all_people)
print(f'{person.netid} {person.first_name} {person.last_name} {person.college}')


import yalies
import random
from dotenv import load_dotenv
import os

load_dotenv()
api = yalies.API(os.environ.get("YALIES_API_KEY"))
# Never hardcode tokens. Use a config file or environment variable instead.
# The name 'api' can be whatever is most appropriate for your program.

all_people = api.people(filters={'school_code': 'YC'})
person = random.choice(all_people)
print(f'{person.netid} {person.first_name} {person.last_name} {person.college}')


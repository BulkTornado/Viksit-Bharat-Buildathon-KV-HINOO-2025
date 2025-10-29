from sql_connection_module import ConnectToMySQL
from datetime import datetime, timedelta
from time import perf_counter as pct
import random, bcrypt

start_date = datetime(2020, 1, 1)
end_date = datetime(2025, 6, 30)

dates: list[datetime] = sorted([start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds()))) for _ in range(10_000)])
date_with_time: list[str] = [date.strftime('%Y-%m-%d %H:%M:%S') for date in dates]
# date_with_time.sort() # EARLIER FIX. NOT NEEDED ANYMORE.

program_start_time = pct()

male_names = [
    "Aarav","Vivaan","Aditya","Arjun","Reyansh","Sai","Krishna","Ishaan","Rohan","Anay",
    "Vihaan","Hriday","Ritvik","Aryan","Kabir","Rudra","Atharv","Kartik","Manan","Laksh",
    "Yash","Parth","Shaurya","Dev","Tanish","Raghav","Tejas","Nirav","Samar","Kiaan",
    "Anirudh","Ayaan","Advik","Siddharth","Om","Dhruv","Keshav","Veer","Arnav","Pranav",
    "Raj","Harsh","Aarush","Ritesh","Varun","Tanay","Chirag","Nikhil","Harshit","Mayank"
]

female_names = [
    "Aanya","Diya","Myra","Aarohi","Anaya","Ira","Meera","Navya","Siya","Sara",
    "Advika","Isha","Riya","Tara","Anika","Kiara","Amaya","Aadhya","Mira","Saanvi",
    "Lavanya","Kashvi","Ishita","Aaradhya","Avni","Aisha","Nitya","Charvi","Shruti","Mahika",
    "Anvi","Nisha","Riddhi","Pihu","Pari","Aanya","Vanya","Gauri","Aditi","Tanya",
    "Priya","Sneha","Neha","Anushka","Simran","Kriti","Nivedita","Divya","Swara","Rachita"
]

all_names = male_names + female_names

last_names = [
    "Sharma","Verma","Gupta","Mehta","Joshi","Patel","Kumar","Singh","Reddy","Nair",
    "Bose","Iyer","Desai","Menon","Kapoor","Chopra","Malhotra","Agarwal","Pillai","Pandey",
    "Yadav","Rana","Chaudhary","Das","Sen","Mukherjee","Banerjee","Sarkar","Mishra","Tiwari",
    "Tripathi","Bhattacharya","Ray","Roy","Paul","Dutta","Bhandari","Rajput","Rawat","Negi",
    "Gill","Sandhu","Bhatia","Sethi","Grover","Bajaj","Ghosh","Chatterjee","Talwar","Mathur",
    "Kohli","Singhania","Khanna","Sodhi","Dhillon","Wadhwa","Saluja","Saxena","Naidu","Shetty",
    "Rastogi","Goel","Mahajan","Bansal","Lal","Trivedi","Dwivedi","Pathak","Solanki","Raj",
    "Chauhan","Purohit","Upadhyay","Sinha","Mannan","Deshmukh","Sawant","Bhaskar","Naik","Patil",
    "Ramakrishnan","Krishnan","Balakrishnan","Venkatesh","Nambiar","Bhat","Hegde","Joshi Mehta",
    "Kumar Singh","Patel Shah","Rao Iyer","Nair Menon","Das Gupta","Roy Choudhury","Banerjee Sen",
    "Bose Dutta","Mishra Tripathi","Verma Sharma"
]

email_domains = ["gmail", "yahoo", "outlook", "protonmail"]

states = {
    1: 'JAMMU AND KASHMIR', 2: 'HIMACHAL PRADESH', 3: 'PUNJAB', 4: 'CHANDIGARH', 5: 'UTTARAKHAND', 6: 'HARYANA', 7: 'DELHI', 8: 'RAJASTHAN', 9: 'UTTAR PRADESH', 10: 'BIHAR', 11: 'SIKKIM', 12: 'ARUNACHAL PRADESH', 13: 'NAGALAND', 14: 'MANIPUR', 15: 'MIZORAM', 16: 'TRIPURA', 17: 'MEGHALAYA', 18: 'ASSAM', 19: 'WEST BENGAL', 20: 'JHARKHAND', 21: 'ODISHA', 22: 'CHHATTISGARH', 23: 'MADHYA PRADESH', 24: 'GUJARAT', 25: 'DAMAN AND DIU', 26: 'DADRA AND NAGAR HAVELI', 27: 'MAHARASHTRA', 28: 'ANDHRA PRADESH (OLD)', 29: 'KARNATAKA', 30: 'GOA', 31: 'LAKSHADEEP', 32: 'KERALA', 33: 'TAMIL NADU', 34: 'PUDUCHERRY', 35: 'ANDAMAN AND NICOBAR ISLANDS', 36: 'TELANGANA', 37: 'ANDHRA PRADESH (NEW)'}

history_of_email: list[str] = []
history_of_number: list[int] = []

customer_info: list[tuple] = []

# Adding 10,000 customers
starting_range_of_id = 100_000_000
ending_range_of_id = 1_000_000_000

for index in range(starting_range_of_id, ending_range_of_id, 90_000):
    while True:
        # Generating random stuff
        c_fname = random.choice(all_names)
        c_lname = random.choice(last_names)

        random_passwd = f"{'_'.join(c_lname.lower().split())}_{c_fname.lower()}@{random.randint(100, 999)}?".encode('utf-8')

        # Generating stuff that is gonna go in the database
        c_id = random.randint(index, index + 90_000)
        c_name = f'{c_fname} {c_lname}'
        c_email = f'{'_'.join(c_lname.lower().split())}{random.randint(100,999)}{c_fname.lower()}@{random.choice(email_domains)}.com'
        c_number = random.randint(6000000000, 9999999999)
        c_address = f"{'.'*5}, {states.get(random.randint(1, 37))}, India"
        hashed_passwd = bcrypt.hashpw(random_passwd, bcrypt.gensalt(rounds=6))
        hashed_passwd = str(hashed_passwd).replace('b', '').replace('\'', '')
        signup_date = date_with_time[len(customer_info)]

        if c_email in history_of_email or c_number in history_of_number:
            continue

        history_of_email.append(c_email)
        history_of_number.append(c_number)

        _ = (c_id, c_name, c_email, c_number, c_address, hashed_passwd, signup_date)
        customer_info.append(_)
        break

sql_query = "INSERT INTO customer_information VALUES"

input('Connected successfully. Press Enter to continue...')

with ConnectToMySQL('localhost', 'root', 'tks@123?') as conn_ob:
    conn_ob.execute_sql_query("USE BigBasket;")
    # print(", ".join(map(str, customer_info[0:100]))) # DEBUG LINE
    for _ in range(0, len(customer_info), 100):
        batch = customer_info[_:_+100]
        if not batch:
            continue
        conn_ob.execute_sql_query(f"{sql_query} {', '.join(map(str, batch))};")
    conn_ob.execute_sql_query("COMMIT;")

program_end_time = pct()
#print(f"Generated and inserted {len(customer_info):,} customer records.")
print(f"Time of operation: {program_end_time - program_start_time:.3f}s")

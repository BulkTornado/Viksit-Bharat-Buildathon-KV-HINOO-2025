from sql_connection_module import ConnectToMySQL
from datetime import datetime, timedelta
from time import perf_counter as pct
import random

start_date = datetime(2020, 1, 1)
end_date = datetime(2025, 6, 30)

dates: list[datetime] = sorted([
        start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
        for _ in range(50_000)])
date_with_time: list[str] = [date.strftime('%Y-%m-%d %H:%M:%S') for date in dates]

program_start_time = pct()

with ConnectToMySQL('localhost', 'root', 'tks@123?') as conn_ob:
    conn_ob.execute_sql_query("USE Amazon;")
    conn_ob.execute_sql_query("SELECT customer_id FROM customer_information;")
    customer_id = conn_ob.fetch_data() # FETCHES ALL DATA
    # IMPORTANT: Data fetched in the format [(*,), (*,)]
    # NEED TO TARGET THE * VALUE, which is by default a single thing in the tuple row

payment_mode = ['CREDIT', 'DEBIT', 'UPI', 'CASH']

history_of_transaction_id: list[int] = []


transaction_info: list[tuple] = []

# 50,000 unique transaction id's
range_of_id = range(100_000_000, 1_000_000_000, 18_000)

# unique_id = sorted(random.sample(range_of_id, 50_000))

for index in range_of_id:
    t_id = random.randint(index, index + 18_000)
    c_id = random.choice(customer_id)[0] # type: ignore
    t_payment_mode = random.choice(payment_mode)
    t_city = random.randint(1, 37)
    order_amount = random.randint(0, 50_000) + random.choice([0.25, 0.75, 0.50])
    order_date = date_with_time[len(transaction_info)]

    _ = (t_id, c_id, t_payment_mode, t_city, order_amount, order_date) #
    transaction_info.append(_)

sql_query = "INSERT INTO transactions_table VALUES"
#sql_query = "INSERT INTO transactions_table (customer_id, payment_mode, transaction_city, order_amount, order_date) VALUES"


with ConnectToMySQL('localhost', 'root', 'tks@123?') as conn_ob:
    conn_ob.execute_sql_query("USE Amazon;")
    for _ in range(0, len(transaction_info), 100):
        batch = transaction_info[_:_+100]
        conn_ob.execute_sql_query(f"{sql_query} {', '.join(map(str, batch))};")
    conn_ob.execute_sql_query("COMMIT;")

program_end_time = pct()
print(f"Generated and inserted {len(transaction_info):,} transaction_info records.")
print(f'Time of operation: {program_end_time - program_start_time:.3f}s')

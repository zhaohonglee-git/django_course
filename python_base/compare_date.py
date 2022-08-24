from datetime import datetime, timedelta

previous_date = datetime.now() - timedelta(days=1)
current_date = datetime.now()
print(
    datetime.now(),
    previous_date,
)
print(previous_date > current_date)

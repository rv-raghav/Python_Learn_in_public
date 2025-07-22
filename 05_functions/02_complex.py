#You are creating a monthly report for a cafe's sales. Instead of putting all logic in one place, break it down.
#Task: Write a function generate_report() that calls:
#fetch_sales()
#filter_valid_orders()
#summarize_data()

def fetch_sales():
    print("Fetching the sales data")

def filter_valid_orders():
    print("filtering valid sales data")

def summarize_data():
    print("Summarizing sales data")

def generate_report():
    fetch_sales()
    filter_valid_orders()
    summarize_data()
    print("report is ready")

generate_report()
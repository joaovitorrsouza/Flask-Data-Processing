from app.utils.pandas_utils import process_csv
from app.repositories.data_repository import save_records, get_all_records

def handle_upload(file):
    processed_data = process_csv(file)
    save_records(processed_data)
    return processed_data.to_dict(orient="records")

def fetch_data():
    records = get_all_records()
    return [
        {
            "category": r.category,
            "value": r.value
        } for r in records
    ]

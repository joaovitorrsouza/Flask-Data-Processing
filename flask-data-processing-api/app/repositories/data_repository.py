from app.models.dataset import Dataset, db

def save_records(dataframe):
    for _, row in dataframe.iterrows():
        record = Dataset(
            category=row["category"],
            value=row["total_value"]
        )
        db.session.add(record)

    db.session.commit()

def get_all_records():
    return Dataset.query.all()

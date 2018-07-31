import school_scores
list_of_record = school_scores.get_all()

for item in list_of_record:
    print(item["State"]["Code"], item["Year"])

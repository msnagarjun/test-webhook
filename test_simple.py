# Python Function to filter based on file extenstion
data = [{"file_name": "test_1.py", "additions": 10, "deletions": 5}, {"file_name": "test_2.html", "additions": 3, "deletions": 2}]
print sum(map(lambda x: x['additions'], filter(lambda x: "py" in x["file_name"].split(".")[-1], data)))

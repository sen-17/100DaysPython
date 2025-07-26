import requests

URL = "https://opentdb.com/api.php?amount=10&type=boolean"
response = requests.get(URL)
datas = response.json()
# print(data["results"][0]["question"])

question_data = []
for data in datas["results"]:
    question = data["question"]
    answer = data["correct_answer"]
    
    question_data.append( {
    "question" : question,
    "correct_answer" : answer
    })










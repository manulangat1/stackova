import requests
import json 
from bs4 import BeautifulSoup
res = requests.get('https://stackoverflow.com/questions')

soup = BeautifulSoup(res.text,"html.parser")

questions_data = {
    "questions":[ ]
}
# print(soup)
questions = soup.select('.question-summary')

for question in questions:
    q = question.select_one('.question-hyperlink').getText()
    vote_count = question.select_one('.vote-count-post').getText()
    views = question.select_one('.views').attrs['title']
    tags = [i.getText() for i in (question.select('.post-tag'))]
    questions_data['questions'].append({
        "questions": q,
        "views": views,
        "vote_count": vote_count,
        "tags": tags        
    })
json_data = json.dumps(questions_data,sort_keys=True,indent=4)
print(json_data)

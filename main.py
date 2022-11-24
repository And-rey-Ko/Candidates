from flask import Flask
from my_func import load_candidates


candidates_json ="candidates.json"
candidates = load_candidates(candidates_json)
app = Flask(__name__)


@app.route('/')
def get_all():
    tr_list = ['<pre>']
    for item in candidates:
        tr_list.append(f'Имя кандидата:         {item["name"]}' 
                       f'\nПозиция кандидата:     {item["position"]}'
                       f'\nНавыки через запятую:  {item["skills"]}'
                       f'\n\n')
    tr_list.append('</pre>')
    return ''.join(tr_list)


@app.route('/candidates/<int:pk>')
def get_by_pk(pk):
    for item in candidates:
        if item["pk"] == pk:
            resume = (f'<img src="{item["picture"]}">'
                      f'\n\n<pre>'
                      f'\nИмя кандидата:         {item["name"]}'
                      f'\nПозиция кандидата:     {item["position"]}'
                      f'\nНавыки через запятую:  {item["skills"]}'
                      f'\n</pre>')
    return resume


@app.route('/skills/<skill_name>')
def get_by_skill(skill_name):
    tr_list = ['<pre>']
    for item in candidates:
        if skill_name.lower() in item["skills"].lower():
            tr_list.append(f'Имя кандидата:         {item["name"]}' 
                           f'\nПозиция кандидата:     {item["position"]}'
                           f'\nНавыки через запятую:  {item["skills"]}'
                           f'\n\n')
    tr_list.append('</pre>')
    return ''.join(tr_list)


if __name__ == "__main__":
    app.run(debug=True)

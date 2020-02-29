from flask import Flask, render_template, request
import urllib.request, json, random
import os

folder_name = "temp_folder"

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    solution_var = 'bbb'
    if request.method == 'GET':
        
        with urllib.request.urlopen("https://www.randomlists.com/data/words.json") as url:
            word_dict = json.loads(url.read().decode())['data']
        
        rand_value = random.randrange(1, len(word_dict))
        solution_form = word_dict[rand_value]
        open(folder_name+"/"+solution_form, "w")

        while True:
            puzzle = ''.join(random.sample(solution_form, len(solution_form)))
            if puzzle != solution_form:
                break
        
        return render_template('index.html', puzzle=puzzle)
    
    elif request.method == 'POST':

        filename = os.listdir(folder_name)[0]
        filesize = os.path.getsize(folder_name+'/'+filename)
        if filesize == 0:
            os.remove(folder_name+'/'+filename)

        return render_template('index.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
    


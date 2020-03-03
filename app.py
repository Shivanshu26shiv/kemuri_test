import os
import re
from flask import Flask, render_template, request
import urllib.request, json, random

folder_name = "temp_folder"
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():

    status_style = "style=display:none"
    placeholder_parm = '...'
    
    if request.method == 'GET':    
        
        with urllib.request.urlopen("https://www.randomlists.com/data/words.json") as url:
            word_dict = json.loads(url.read().decode())['data']

        '''
        from nltk.corpus import words
        word_list = words.words()
        '''

        while True:
            rand_value = random.randrange(1, len(word_dict))
            solution = word_dict[rand_value]
            puzzle = ''.join(random.sample(solution, len(solution)))
            if puzzle != solution and puzzle != solution[::-1] and 8 > len(solution) > 3 and regex.search(puzzle) == None:
                break

        try:
            files_to_remove = [os.path.join(folder_name, f) for f in os.listdir(folder_name)]
            for f in files_to_remove:
                os.remove(f)

        except FileNotFoundError:
            os.mkdir(folder_name)
                        
        open(folder_name+"/"+solution.lower()+'_'+puzzle.lower(), "w")

        puzzle = list(puzzle.upper())
        return render_template('index.html', solution=solution, puzzle=puzzle, status_style=status_style, placeholder_parm=placeholder_parm, length=len(puzzle))
    
    elif request.method == 'POST':
        
        try:
            filename = os.listdir(folder_name)[0]
        except IndexError:
            return render_template('index.html')

        answer = request.form['answer'].lower()
        solution, puzzle = filename.partition('_')[0], filename.partition('_')[2]
        
        if answer == solution:
            status = "id=fa-check"
            status_style = "style=border-width:2px;border-style:solid;background:limegreen;color:white;line-height:inherit"
        else:
            status = "id=fa-close"
            status_style = "style=border-width:2px;border-style:solid;background:red;color:white;line-height:inherit"

        placeholder_parm = ':' + answer

        puzzle = list(puzzle.upper())
        return render_template('index.html', solution=solution, puzzle=puzzle, status=status, status_style=status_style, placeholder_parm=placeholder_parm, length=len(puzzle))

if __name__ == '__main__':
    app.run(debug=True)
    


from flask import Flask, render_template, request
from wtforms import Form, IntegerField, validators

app = Flask(__name__)

@app.route('/')
def inputForm():
    return render_template('index.html')
  
@app.route('/generate_segitiga', methods=['POST'])
def generateSegitiga():
  form = InputForm(request.form)
  result = []
  if request.method == 'POST' and form.validate():
        number = form.number.data
        for i in range(1, number+1):
            result.append('*' * i)
            
  return render_template('index.html', result=result)

@app.route('/generate_ganjil', methods=['POST'])
def generateGanjil():
  form = InputForm(request.form)
  result = []
  if request.method == 'POST' and form.validate():
        number = form.number.data
        for i in range(1, number+1):
            if i % 2 != 0:
                result.append(i)
            
  return render_template('index.html', result=result)

@app.route('/generate_prima', methods=['POST'])
def generatePrima():
  form = InputForm(request.form)
  result = []
  if request.method == 'POST' and form.validate():
        number = form.number.data
        for i in range(1, number+1):
            if i > 1:
                for j in range(2, i):
                    if i % j == 0:
                        break
                else:
                    result.append(i)
            
  return render_template('index.html', result=result)

class InputForm(Form):
    number = IntegerField('Number:', validators=[validators.data_required()])
    
def main():
    app.run(debug=True)
    
if __name__ == '__main__':
    main()
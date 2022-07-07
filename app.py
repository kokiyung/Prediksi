from flask import Flask,request, render_template
from sklearn.preprocessing import Labelencoder
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

ds = pd.read_csv('DataSet.cvs', usecols= ['SEKOLAH','JS','JG','JM'])

x = ds.iloc[:,:-1].values 
y = ds.iloc[:,-1].values

encorder = labelEncoder()

x[:,0] = encoder.fit_transform(x[:,0])
x[:,1] = encoder.fit_transform(x[:,1])
x[:,2] = encoder.fit_transform(x[:,2])
y = encoder.fit_transform(y)

model = MultinomialNB()

model.fit(x, y)

@app.route('/')
def index():
    return render_template('index.html', predicted="?", SEKOLAH = "?", JS = "?", JG = "?")
 

@app.route('/prediction', methods=['POST'])
def predection():
    SEKOLAH = int(request.form['SEKOLAH'])
    JS = int (request.form['JS'])
    JG = int (request.from['JG'])

    predicted = model.predict([SEKOLAH, JS, JG ])
    if JG == 0:
        JG = "Bertambah"
    elif JG == 1:
        JG = "Berkurang"
    elif JG == 2:
        JG = "Tetap"

    # menampilkan template yang sama dengan membawa data hasil prediksi
    return render_template('index.html', predicted = "Yes" if predicted else "No", SEKOLAH = SEKOLAH, JS = JS, JG = JG )

# drive
if __name__ == '__main__':
    app.run(debug=True)
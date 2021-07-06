import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open(r'LGBMmodel.pkl','rb'))
@app.route('/',methods=['GET'])
def home():
    return render_template('new_ebay.html')
@app.route('/predict',methods=['POST'])
def predict():
    try:
        Bid = float(request.form['Bid'])
        Bidtime = float(request.form['Bidtime'])
        Bidderrate = int(request.form['Bidderrate'])
        OpenBid = float(request.form['OpenBid'])
        prediction = np.expm1(model.predict([[Bid, Bidtime, Bidderrate, OpenBid]]))
        output = round(prediction[0], 2)
        if output < 0:
            return render_template('new_ebay.html', prediction_texts="Cannot sell your Unit")
        else:
            return render_template('new_ebay.html', prediction_text='Auction Price for your product will be ₹{}'.format(output))
    except ValueError:
        return render_template('new_ebay.html', prediction_text="Enter your data in numbers only")
        #return("Enter integer values only")

    #return render_template('new 2.html', prediction_text='Auction Price for your product will be ₹{}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)




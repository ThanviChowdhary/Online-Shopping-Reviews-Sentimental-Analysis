from flask import Flask, request, render_template, flash, redirect, url_for
from wtforms import SubmitField, BooleanField, IntegerField, StringField,PasswordField, validators, TextAreaField
import sys
import Sentiment_website_integration
import honest_deceptive_reviews
from flask import Markup

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'dc98a1dff26acf9dac338188cfb512b5199944ea3f317ea1'


@app.route('/')
def my_form():
    return render_template('product_details.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['nm']
    processed_text = text.upper()
    try:
        if request.form['sentiment'] == 'Analyze_Sentiment':
            sentiment_result, pos, neg = Sentiment_website_integration.run_sentiment_analysis(text)
            return render_template('product_details.html', input_name = text, result = sentiment_result, positive = pos, negative = neg)
            
    except Exception as e:
        print(e)
        
    try:
        if request.form['deceptive'] == 'Analyze_Deceptive':
            honest_result, pos, neg = honest_deceptive_reviews.run_deceptive_analysis(text)
            return render_template('product_details.html', input_name = text, result = honest_result, positive = pos, negative = neg)
            
    except Exception as e:
        print(e)
    sentiment_result, pos, neg = Sentiment_website_integration.run_sentiment_analysis(text)
    return render_template('product_details.html', input_name = text, result = sentiment_result, positive = pos, negative = neg)




if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)

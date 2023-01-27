from flask import Flask
from flask import request
import os
import openai
from flask_cors import CORS

openai.api_key = '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'



app = Flask(__name__)
CORS(app)


@app.route('/prompt',methods=['POST'])
def post_prompt():
    prompt = request.form['prompt']
    response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.3,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
    return response.choices[0].text
import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from collections import Counter

vertexai.init(project="cnpj-analytics", location="us-central1")
generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods= ['POST'])
def generate():
  model = GenerativeModel("gemini-experimental")
  responses = model.generate_content(
      ["""please, create a descrepition of a character for my rgp game"""],
      generation_config=generation_config,
      safety_settings=safety_settings,
      stream=True,
  )
  
  response_list = []
  for response in responses:
    response_list.append(response.text.replace("##", "").replace("**", "").replace("*", ">"))
  #return response.text.replace("##", "").replace("**", "").replace("*", ">")

  delimiter = ""
  result_string = delimiter.join(response_list)
  return result_string

  #for response in responses:
    #print(response.text, end="")

if __name__ == "__main__":
    app.run(port=8080, host='0.0.0.0', debug=True)

#teste9
#teste10
#teste11
#teste12
#teste13
#teste14
#teste15
#teste16
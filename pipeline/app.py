from flask import Flask, jsonify, request, Response, make_response, json
import jsonpickle
import numpy as np
import cv2
import io

from deepface import DeepFace
from deepface.basemodels import FbDeepFace
from deepface.extendedmodels import Age, Gender

from utils.ageCheck import ageCheck
from utils.genderCheck import genderCheck
from utils.deepface import pipe
from utils.ppe import read_info


app = Flask(__name__, instance_relative_config=True)
# app.config.from_object('config.settings')
# app.config.from_pyfile('settings.py', silent=True)

verification_model = {}
analysis_models = {}
CURRENT_YEAR = 2020


@app.route("/", methods=["GET", "POST"])
def analysis():
    if request.method == "POST":
        # Get a check location, names in scrapper Database
        #image = request.files['image'].read()
        face_image = request.files['face_image']
        doc_image = request.files['doc_image']

        #args-->form
        country = request.form.get('country')
        print(country)
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        dob = request.form.get('dob')
        # doc_type = request.args.get('doc_type')
        phone_number = request.form.get('phone_number')


        in_memory_face = io.BytesIO()
        face_image.save(in_memory_face)
        face_image = np.fromstring(in_memory_face.getvalue(), dtype=np.uint8)
        face_image = cv2.imdecode(face_image, 1)

        in_memory_doc = io.BytesIO()
        doc_image.save(in_memory_doc)
        doc_image = np.fromstring(in_memory_doc.getvalue(), dtype=np.uint8)
        doc_image = cv2.imdecode(doc_image, 1)
        #Processing
        #gatherModels(verification_model, analysis_models)
        age, gender = pipe(face_image, doc_image, verification_model, analysis_models)

        # if doc_type == 'passport' or 'national ID':
        extract = read_info(doc_image)
        dob_extract = extract['date_of_birth']
        gender_extract = extract['sex']
        # Gender & Age Check - do a check against a failure here
        gender_results = genderCheck(gender_extract, gender)
        age_results = ageCheck(dob_extract, age)
        # Names Check - do a check against failure here as well
        first_name_results = False
        last_name_results = False
        first_name_extract = extract['names'].lower()
        last_name_extract = extract['surname'].lower()

        if first_name in first_name_extract and last_name in last_name_extract:
            first_name_results = True
            last_name_results = True
        elif first_name in first_name_extract and last_name not in last_name_extract:
            first_name_results = True
        elif first_name not in first_name_extract and last_name in last_name_extract:
            last_name_results = True
        else:
            pass

        # # elif doc_type is utility bill or driver's license
        # Response
        response = {
            'gender_prediction': gender,
            'gender_doc_extract': gender_extract,
            'gender_results':gender_results,
            'age_prediction': age,
            'age_doc_extract': dob_extract,
            'age_results':age_results,
            'first_name_doc_extract': first_name_extract,
            'first_name_results': first_name_results,
            'last_name_doc_extract': last_name_extract,
            'last_name_doc_results': last_name_results
        }
        # # pickle
        # print("Response: ", response)
        # response_pickled = jsonpickle.encode(response)
        # response = jsonify(response)
        return Response(response=response, status=200, mimetype="application/json")
        #return response
    if request.method == "GET":
        return Response(response="Get Req", status=200, mimetype="application/json")


def gatherModels(verification, analysis):
    verification['FbDeepFace'] = FbDeepFace.loadModel()
    analysis['age'] = Age.loadModel()
    analysis['gender'] = Gender.loadModel()
    return verification, analysis

if __name__ == '__main__':
    # Other potential proper location is line 52
    def gatherModels(verification, analysis):
        verification['FbDeepFace'] = FbDeepFace.loadModel()
        analysis['age'] = Age.loadModel()
        analysis['gender'] = Gender.loadModel()
        return verification, analysis
        
    gatherModels(verification_model, analysis_models)
    app.run(debug=True, host="0.0.0.0", threaded=True)






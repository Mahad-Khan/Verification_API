from deepface import DeepFace
from deepface.basemodels import FbDeepFace
import cv2
import json
from deepface.extendedmodels import Age, Gender

# verification_model and analysis_model outside of the function scope
# def gatherModels(verification, analysis):
#     verification_model['FbDeepFace'] = FbDeepFace.loadModel()
#     analysis_models['age'] = Age.loadModel()
#     analysis_models['gender'] = Gender.loadModel()

# change arguments to path variables if needed
def pipe(face_img, doc_img, verification, analysis):
    #analysis_models = {}
    #verification_model = {}
    verification_model = verification
    analysis_models = analysis
    #verification_model['FbDeepFace'] = FbDeepFace.loadModel()
    #analysis_models["age"] = Age.loadModel()
    #analysis_models["gender"] = Gender.loadModel()

    face_img = cv2.imread(face_img)
    doc_img = cv2.imread(doc_img)
    

    match = DeepFace.verify(face_img, doc_img, model_name = "FbDeepFace", model = verification_model['FbDeepFace'])

    if match['distance'] <= 0.55:
            analysis = DeepFace.analyze(face_img, actions=['age', 'gender'], models=analysis_models)
            age = analysis['age']
            gender = analysis['gender']

            return age, gender

# Class Pipe:
# verification_model = {}
# analysis_models = {}
#     def init(self):
#         verification_model['FbDeepFace'] = FbDeepFace.loadModel()
#         analysis_models['age'] = Age.loadModel()
#         analysis_models['gender'] = Gender.loadModel()

#         self.verification = verification_model
#         self.analysis = analysis_models


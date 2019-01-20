from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient

def prediction_call(frm_url):        
    print(frm_url, 'from predition call')
    ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com"
    prediction_key = "fdc8548027114381bd41337662282bc5"
    projectId = "fa50ff7c-c909-4038-bc16-f1b929621ab3"


    # Now there is a trained endpoint that can be used to make a prediction
    predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)

    with open(frm_url, mode="rb") as test_data:
        result = predictor.predict_image(projectId, test_data)

    maxTag = ""
    maxConfidence = 0
    bL = 0
    bT = 0
    bW = 0
    bH = 0
    # Display the results.
    for prediction in result.predictions:
        if prediction.probability > maxConfidence:
            maxTag = prediction.tag_name
            maxConfidence = prediction.probability
            bL = prediction.bounding_box.left
            bT = prediction.bounding_box.top
            bW = prediction.bounding_box.width
            bH = prediction.bounding_box.height
    return maxTag
    # print("\t" + maxTag + ": {0:.2f}%".format(maxConfidence * 100), bL, bT, bW, bH)

from flask import Flask, request, render_template
import json
import boto3

textractclient = boto3.client("textract", aws_access_key_id="AKIAU2V2Z7VMMBL4FFP3",
                              aws_secret_access_key="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", region_name="us-east-1")


app = Flask(__name__)


@app.route("/", methods=["GET"])
def main():
    return render_template("index2.html", jsonData=json.dumps({}))


@app.route("/extract", methods=["POST"])
def extractImage():

    file = request.files.get("filename")
    binaryFile = file.read()
    response = textractclient.detect_document_text(
        Document={
            'Bytes': binaryFile
        }
    )

    extractedText = ""

    for block in response['Blocks']:
        if block["BlockType"] == "LINE":
            extractedText = extractedText+block["Text"]+ " "

    responseJson = {

        "text": extractedText
    }
    print(responseJson)
    return render_template("index2.html", jsonData=responseJson)


app.run("0.0.0.0", port=5000, debug=True)
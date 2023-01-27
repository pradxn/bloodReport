# bloodReport
Project to extract text data from an uploaded medical blood report sample pdf using AWS Textract

## Overview
- Uploading a picture with text using Flask and boto3
- boto3 uses AWS Textract to parse the image and converts into JSON

### JSON Output
{"Blocks": [
      "BlockType": "LINE",
      "Confidence": 84.31163024902344,
      "Geometry": {
        "BoundingBox": {
          "Height": 0.010260550305247307,
          "Left": 0.7662059664726257,
          "Top": 0.1755794882774353,
          "Width": 0.09074240922927856
        },
        "Polygon": [ .... }
        
 - Extract only "Text" data from this JSON
 - Print it out on browser

<img width="1193" alt="Screenshot 2023-01-27 at 21 19 04" src="https://user-images.githubusercontent.com/96560188/215128585-04780d4b-6a4b-4f14-8d8f-6303e8644fa1.png">

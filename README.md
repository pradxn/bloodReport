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

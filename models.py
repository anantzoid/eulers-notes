import requests
import json
import os
# use HPE entity extract api
# TODO make it async call later

def getUploadedFiles():
    return os.listdir("files/")

def extract_entity(filename):
    filename = "files/"+filename
    data = {'apikey': '5a75920d-6cf8-4eff-a448-e7e2fa6ca00c'}
    resp = requests.post("https://api.havenondemand.com/1/api/sync/ocrdocument/v1", data=data, files={'file': open(filename, "r")}) 
    ocr = json.loads(resp.text)
    ocrd = ''
    if 'text_block' in ocr:
        for text in ocr['text_block']:
            ocrd += '\n' + text['text']
    resp = requests.get("https://api.dandelion.eu/datatxt/nex/v1/?include=types%2Cabstract%2Ccategories&token=541790f5453b4f0dac754a8df9774b88&text="+ocrd)
    resp = resp.text
    resp = json.loads(resp)
    keyword_dict = resp['annotations']  if 'annotations' in resp else []
    extracted_entities = {}
    for entity in keyword_dict:
        if entity['spot'] not in extracted_entities:
            extracted_entities[entity['spot']] = entity

    return {'text': ocrd, 'entities': json.dumps(extracted_entities)}

def getFileData(filename):
    return "True"   


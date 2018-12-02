from flask import Flask, render_template, request, jsonify 
from flask_cors import CORS
import pandas as pd
import tabula
import json
import numpy
import img2pdf
import requests
import lxml.html as lh



app = Flask(__name__)
CORS(app)




def toCsvOCRMethod(file, nbPage):
    tabula.convert_into(file, "output" + ".csv", output_format="csv", pages=nbPage)
    
def toPdfOcrMethod():
    with open("output.pdf", "wb") as f:
        f.write(img2pdf.convert("2.png"))


def webScraping():
    url = "http://www.tunisieindustrie.nat.tn/fr/DR.asp?Gvt="
    s = []
    gouvernorats = ""
    for i in range(1,25):
        page = requests.get(url+"{}".format(str(i).zfill(2)))
        doc = lh.fromstring(page.content)
        li_elements = doc.xpath('//li')
        gouvernorats = (doc.xpath('//h2')[0].text_content().split(" ")[1])
    
        if(len(li_elements) > 47):
            j = 0
            for li in li_elements[40:(41+len(li_elements) - 47)]:
                j+=1
                name=li.text_content()
                s.append(('%s %d:"%s"'%(gouvernorats,j,name)))
                
                
                
                
@app.route('/')
def hello():
    return jsonify({'text':'Hello World!'})



# Get all Governorate chomage et IDR 
@app.route('/ChomagesIDR',methods = ['POST', 'GET'])
def getChomage():
    # exportation 
    expoDataIdr = pd.read_csv('idr.csv', sep=',', encoding = "ISO-8859-1")
    expoDataCh = pd.read_csv('chomage.csv', sep=',', encoding = "ISO-8859-1")
    
    # cleaning DATA
    tauxChomage = expoDataCh[['gouvernorat', 'chomage']]
    tauxIdr = expoDataIdr[['gouvernorat', 'IDR']]
    
    # making gonverate uppercase
    tauxChomage['gouvernorat'] = tauxChomage['gouvernorat'].str.upper()
    
    
    # Merging the two criteras
    result = pd.merge(tauxChomage, tauxIdr, on=['gouvernorat'])
    
    return result.to_json(orient='columns')





# Get Governorate by id
@app.route('/Chomage',methods = ['POST', 'GET'])
def getChomageByGovName():
    # exportation 
    expoData = pd.read_csv('../chomage.csv', sep=',', encoding = "ISO-8859-1")
    name = request.args.get('name')
    tauxChomage = expoData[['Regions', 'Chomage']]
    abc = expoData[['Regions', 'Chomage']]
    abc = tauxChomage.loc[tauxChomage['Regions'] == name, ['Chomage']]
    print(tauxChomage)
    print(type(tauxChomage))
    print(type(abc))
    return json.dumps({'gov':numpy.asscalar(abc['Chomage'].iloc[0])})
    


# Get all IDRs 
@app.route('/Idr',methods = ['POST', 'GET'])
def getIDR():
    # exportation 
    expoData = pd.read_csv('../idr.csv', sep=',', encoding = "ISO-8859-1")
    tauxChomage = expoData[['gouvernorat', 'IDR']]
    return tauxChomage.to_json(orient='records')
    



    
    
    
    
    
if __name__ == '__main__':
   app.run(debug = True)

if __name__ == "__main__":
    app.run()
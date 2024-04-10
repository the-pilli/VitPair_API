from flask import Flask, send_file, jsonify, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import base64
import time
import pyautogui
import pandas as pd
import numpy as np
import math
import json
from collections import OrderedDict
from google.cloud import firestore



def save_base64_image(data, filename):
    with open(filename, 'wb') as f:
        f.write(base64.b64decode(data))

#-------------------------------ALFO FUNCTIONS-------------------------------------
def stringMatch(str1, str2):
    str1 = str1.strip()
    str2 = str2.strip()
    str1 = str1.lower()
    str2 = str2.lower()
    minLen = min(len(str1), len(str2))
    score = 0
    for i in range(minLen):
        if(str1[i]==str2[i]):
            score+=1
    if(score==minLen):
        return True
    return False

#Sigmoid Transfer Function to convert deviation to closeness
def sigmoidTF(x):
    return (2*(1/(1+math.exp(2.5*x))))

#------------------------------ALFO FUNCTIONS ENDS-------------------------------------
#collection_ref = db.collection('your_collection')






"""db = firestore.Client()
driver = None
flag = False"""

try:
    driver = webdriver.Chrome()
    action = ActionChains(driver)
    driver.get("http://vtopcc.vit.ac.in/vtop/initialProcess/openPage")
    
    student_img = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "student")))
    
    student_img.click()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "html")))

    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    string_soup = soup.prettify()
    soup = string_soup
    
    print("OOOGA BOOGA")
    alt_index = soup.find('src="data:image/jpeg;base64,')
    if(alt_index != -1):
        alt_text = soup[alt_index+5:]
        end_index = alt_text.find('"')
        captcha_src = alt_text[:end_index]

        print("Second_Booga")
        base64_data = captcha_src.split(',')[1]
        save_base64_image(base64_data, f'captcha.jpeg')
        print(f"Saved image as captcha.jpeg")
        flag = True





except Exception as e:
    print("An error occurred:", e)



app = Flask(__name__)

@app.route('/captcha', methods=['GET'])
def get_captcha():
    if flag == True:
        return send_file('captcha.jpeg', mimetype='image/jpeg')
    else:
        return jsonify({'error': 'Failed'}), 400
    


@app.route('/registerC', methods=['POST'])
def registerC():
    username = request.json.get('username')
    password = request.json.get('password')
    captcha = request.json.get('captcha')




    if not (username and password and captcha):
        return jsonify({"error": "Username, password, and captcha answer are required"})

    
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)
    
    captcha_input = driver.find_element(By.ID, "captchaStr")
    captcha_input.send_keys(captcha)

    
    submitBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "submitBtn")))
    submitBtn.click()

    
    time.sleep(5)
    close_popup = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "btnClosePopup")))
    close_popup.click()

    time.sleep(5)
    # button = driver.find_element_by_xpath("//button[contains(@onclick, 'getButtonBar()')]")
    pyautogui.click(50, 213)
    time.sleep(1)
    pyautogui.click(170, 340)
    time.sleep(1)
    pyautogui.click(177, 374)
    time.sleep(1)
    pyautogui.click(490, 220)
    # button = driver.find_element_by_xpath("//button[@data-bs-target='#acMenuCollapseHDG0064']")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    string_soup = soup.prettify()
    soup = string_soup
    print(soup)


    message = {
        "Name": "Sahil Sunil Agrawal",
        "Phone Number": "9321407297",
        "Registration_Number": "22BRS1283",
        "password": password,
        "Mail ID": "sahil.agrawal2022@gmail.com",
        "Hostel Block": "D",
        "NRI": "No",
        "Religion": "Hindu",
        "Native Language": "Hindi",
        "Native State or UT": "Maharashtra",
        "CGPA": 8.98,
        "High School Board": "CBSE",
        "Year Of Graduation": "2026",
        "Gender" : "Male"
    }
        # name: json["Name"],
        # phoneNumber: json["Phone Number"],
        # mailId: json["Mail ID"],
        # gender: json["Gender"],
        # registrationNumber: json["Registration Number"],
        # yearOfGraduation: json["Year of Graduation"],
        # hostelBlock: json["Hostel Block"],
        # nri: json["NRI"],
        # religion: json["Religion"],
        # nativeLanguage: json["Native Language"],
        # nativeStateOrUt: json["Native State or UT"],
        # careerInterests: json["Career Interests"],
        # cgpa: json["CGPA"]?.toDouble(),
        # highSchoolBoard: json["High School Board"],
        # areaOfInterests:
        #     List<String>.from(json["Area of Interests"].map((x) => x)),
    
    return jsonify(message)
    






@app.route('/registerWC', methods=['POST'])
def registerWC():
    username = request.json.get('username')
    password = request.json.get('password')

    if not (username and password):
        return jsonify({"error": "Username, password, and captcha answer are required"})

    
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)
    

    submitBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "submitBtn")))
    submitBtn.click()


    time.sleep(5)
    close_popup = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "btnClosePopup")))
    close_popup.click()

    time.sleep(5)
    # button = driver.find_element_by_xpath("//button[contains(@onclick, 'getButtonBar()')]")
    pyautogui.click(50, 213)
    time.sleep(1)
    pyautogui.click(170, 340)
    time.sleep(1)
    pyautogui.click(177, 374)
    time.sleep(1)
    pyautogui.click(490, 220)
    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    string_soup = soup.prettify()
    soup = string_soup
    print(soup)

    # button = driver.find_element_by_xpath("//button[@data-bs-target='#acMenuCollapseHDG0064']")
    # button.click()
    
    # print("MOMO BHAI")
    # anchor_tag = driver.find_element_by_xpath("//a[contains(@data-url, 'studentsRecord/StudentProfileAllView')]")
    # anchor_tag.click()

    # button = driver.find_element_by_xpath("//button[@data-bs-dismiss='offcanvas']")
    # button.click()



    message = {
        "Name": "Sahil Sunil Agrawal",
        "Phone Number": "",
        "Registration_Number": "22BRS1283",
        "password": password,
        "Mail ID": "sahil.agrawal2022@gmail.com",
        "Hostel Block": "D",
        "NRI": "No",
        "Religion": "Hindu",
        "Native Language": "Hindi",
        "Native State or UT": "Maharashtra",
        "CGPA": 8.98,
        "High School Board": "CBSE",
        "Year Of Graduation" : "2026",
        "Gender" : "Male"
    }
        # name: json["Name"],
        # phoneNumber: json["Phone Number"],
        # mailId: json["Mail ID"],
        # gender: json["Gender"],
        # registrationNumber: json["Registration Number"],
        # yearOfGraduation: json["Year of Graduation"],
        # hostelBlock: json["Hostel Block"],
        # nri: json["NRI"],
        # religion: json["Religion"],
        # nativeLanguage: json["Native Language"],
        # nativeStateOrUt: json["Native State or UT"],
        # careerInterests: json["Career Interests"],
        # cgpa: json["CGPA"]?.toDouble(),
        # highSchoolBoard: json["High School Board"],
        # areaOfInterests:
        #     List<String>.from(json["Area of Interests"].map((x) => x)),
    
    return jsonify(message)


@app.route('/selection', methods=['POST'])
def selection():
    #For Monish to fix
    temp = request.data
    junior = pd.Series(temp)


    df=pd.read_csv("RegForm (1).csv",index_col='Index')
    """print(df)
    branchList=[]
    for i in df.index:
        branchList.append(df['Registration Number'][i][2:5])
    df.insert(6,"Branch",branchList)"""

    df.columns = ["Name","Phone","Email","Gender","RegNo","GradYear","BranchCode","Hostel","NRI","Religion","Lang","State","Career","CGPA","HSB","Interests"]
    df.index = [int(x) for x in df.index]

    senior=df[df['RegNo']<"22"]
    df=df.T

    #Buliding a state affinity chart
    states=pd.read_csv('stateChart.csv',index_col='States')
    #Building a branch affinity chart
    branch = pd.read_csv('branches.csv',index_col='Branches')
    #Building a block affinity chart
    blocks = pd.read_csv('blocks.csv',index_col='Block')
    #Building a language affinity chart
    lang = pd.read_csv('lang.csv',index_col='Lang')

    #ACTUAL START
    junior1 = junior
    junior1.index = np.random.choice(range(len(junior1)),len(junior1),replace=False)

    #Gender based elimination
    tempdf = senior
    print(type(junior1.index))
    print(type(senior.index))
    tempdf = tempdf[tempdf['Gender']==junior1['Gender']]

    #Maintaining a minimum of 2 year gap
    year = str(int(junior1['RegNo'][:2])-1)
    tempdf = tempdf[tempdf['RegNo']<year]

    tempdf = tempdf[tempdf["NRI"]==junior1["NRI"]]

    matchScore = {}
    avgDeviation = 0
    nonNullCgpa = []
    for i in tempdf.index:
        matchScore[i] = 0

    for i in tempdf.index:
        Code=0

        #Branch Affinity, weight = 0.7 * affinity of the pair
        tempCode = float(branch[tempdf['BranchCode'][i]][junior1['BranchCode']])
        Code += 0.7 * tempCode

        #Block Affinity, weight = 0.6 * affinity of the pair
        tempCode = float(blocks[tempdf['Hostel'][i]][junior1['Hostel']])
        Code += 0.6 * tempCode

        #Language Affinity, weight = 0.8 * affinity of the pair
        tempCode = float(lang[tempdf['Lang'][i]][junior1['Lang']])
        Code += 0.8 * tempCode

        #Religion match, weight 0.05, added to only religion matches
        #Using pd.isnull instead of np.isnan
        if((not pd.isnull(tempdf['Religion'][i])) and (not pd.isnull(junior1['Religion']))):
            if(stringMatch(tempdf['Religion'][i],junior1['Religion'])):
                Code += 0.05

        #For career interests also, if they match, +0.08
        if(tempdf['Career'][i]==junior1['Career']):
            Code += 0.08

        #For CGPA, weights = 0.3 * deviation from target CGPA
        if((not pd.isnull(junior1['CGPA'])) and (not pd.isnull(tempdf['CGPA'][i]))):
            targetCGPA = float(junior1['CGPA']) + 0.2
            avgDeviation += abs(targetCGPA - float(tempdf['CGPA'][i]))
            nonNullCgpa.append(i)
            #Now we use sigmoid transfer function to convert the deviation to closness
            Code += 0.3 * abs(targetCGPA - float(tempdf['CGPA'][i]))

        #For High School Board match, +0.05 if they are the same
        if((not pd.isnull(tempdf['HSB'][i])) and (not pd.isnull(junior1['HSB']))):
            if(stringMatch(tempdf['HSB'][i], junior1['HSB'])):
                Code += 0.05
        
        #For interests, we'll split and match the interests individually
        #For every matching interest, +0.08
        matchingInterests = 0
        if((not pd.isnull(tempdf['Interests'][i])) and (not pd.isnull(junior1['Interests']))):
            seniorInterests = tempdf['Interests'][i].split(',')
            juniorInterests = junior1['Interests'].split(',')
            for j in seniorInterests:
                for k in juniorInterests:
                    if (stringMatch(j,k)):
                        matchingInterests += 1
        Code += matchingInterests * 0.08

        matchScore[i] = Code


    #To handle the cases where CGPA wasn't provided, we simply put the avg deviation * 0.6
    avgDeviation /= len(nonNullCgpa)
    for i in tempdf.index:
        if i not in nonNullCgpa:
            matchScore[i] += avgDeviation

    for i in matchScore:
        matchScore[i] = round((matchScore[i]),4)

    # print("Junior data: ")
    # print(junior1)

    bestMatchIndex = list(matchScore.keys())[0]
    for i in matchScore.keys():
        if matchScore[i]>matchScore[bestMatchIndex]:
            bestMatchIndex=i
    # print("Best Match for you: ")
    # print(df[bestMatchIndex])
    selected_senior = df[bestMatchIndex].to_json()

    return selected_senior
        



@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    captcha_answer = request.json.get('captcha')

    #find in firebase

@app.route('/addInterest', methods=['POST'])
def addInterest():
    interest = request.json.get('interest')
    person = request.json.get('person') #should get person token


"""@app.route("/Chat", methods=["POST"])
def response():
    message = request.json
    collection_name = 'Messages'
    doc_ref = db.collection(collection_name).add(message)"""



if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

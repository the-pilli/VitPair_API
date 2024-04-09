from flask import Flask, send_file, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import base64
import re



def save_base64_image(data, filename):
    with open(filename, 'wb') as f:
        f.write(base64.b64decode(data))








app = Flask(__name__)

@app.route('/captcha', methods=['GET'])
def get_captcha():
    if flag == True:
        return send_file('captcha.jpeg', mimetype='image/jpeg')
    else:
        return jsonify({"error": "Captcha not found"})
    
    


if __name__ == '__main__':
        
    driver = None
    flag = False

    try:
        driver = webdriver.Chrome()
        action = ActionChains(driver)
        driver.get("http://vtopcc.vit.ac.in/vtop/initialProcess/openPage")
        
        student_img = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "student")))
        
        student_img.click()
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "html")))

        
        # username_input = driver.find_element(By.ID, "username")
        # username_input.send_keys(user_bhai)

        # password_input = driver.find_element(By.ID, "password")
        # password_input.send_keys(pass_of_bhai)

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


        
        submitBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "submitBtn")))
        submitBtn.click()


        soup = BeautifulSoup(driver.page_source, "html.parser")
        print(soup)

    except Exception as e:
        print("An error occurred:", e)





    app.run(debug=True)

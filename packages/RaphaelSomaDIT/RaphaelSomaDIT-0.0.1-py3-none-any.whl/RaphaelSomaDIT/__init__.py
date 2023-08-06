import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from getpass import getpass

 
def result(email, password):
    
    login_url = 'https://soma.dit.ac.tz/login'
    secure_url = 'https://soma.dit.ac.tz/'
    # email = input('enter your email: ')
    # password = getpass('enter your password: ')
    session = requests.Session()
    secure_url = 'https://soma.dit.ac.tz/'
    request = session.get(login_url).content

    soup = bs(request,'html.parser')

    csrf = soup.find('input',{'name':'csrf'}).get('value')

    payload = {
            'email': email,
            'password': password,
            'csrf': csrf,  

            }


    p = session.post(login_url,data=payload)

    t = session.get(secure_url)

    soup = bs(t.text, "html.parser")

    link =soup.select('a.nav-link')
    links = [ links.get("href") for links in link] 
    result_url = [l for l in links if '/student-semester-results' in l]
    
    result_url = (f'https://soma.dit.ac.tz{result_url[0]}')
    result_page = session.get(result_url).text

    result = pd.read_html(result_page)
    r = pd.DataFrame(result[0])
    r.to_csv('matokeo_sem1.csv',index=False)

    r = pd.DataFrame(result[1])
    r.to_csv('matokeo_sem2.csv',index=False)

    df1 = pd.read_csv('matokeo_sem1.csv')
    df2= pd.read_csv('matokeo_sem2.csv')
    df_merged = pd.merge(df1, df2, how='outer')
    df_merged.to_csv('matokeo.csv', index=False)


photo=''
regno=''
gender=''
dob=''
mail=''
mobile=''
martial_status=''
academic_year=''
NTA_level=''
name=''
nationality = ''


variable = [
'photo',
'regno',
'gender',
'dob',
'mail',
'mobile',
'martial_status',
'academic_year',
'NTA_level',
'name',
'nationality',   
] 
def studentInfo(email, password):
    
    global photo,mail,mobile,martial_status,nationality,gender,dob,academic_year,NTA_level,regno,name
    
    login_url = 'https://soma.dit.ac.tz/login'
    secure_url = 'https://soma.dit.ac.tz/'
    session = requests.Session()
    secure_url = 'https://soma.dit.ac.tz/'
    request = session.get(login_url).content

    soup = bs(request,'html.parser')

    csrf = soup.find('input',{'name':'csrf'}).get('value')

    payload = {
            'email': email,
            'password': password,
            'csrf': csrf,  

            }


    p = session.post(login_url,data=payload)
    if 'Welcome, you have successfully logged into your account' in p.text:
        print('successful login')
        
        global variable
        print('avaliable variable in the script')
        for variable in variable:
            print(variable)

        t = session.get(secure_url)

        soup = bs(t.text, "html.parser")

        link =soup.select('a.nav-link')
        links = [ links.get("href") for links in link] 
        
        
        person_info = [p for p in links if '/student-profile-registration' in p]


        person_info = (f'https://soma.dit.ac.tz/{person_info[0]}')
        person_info = session.get(person_info).text

        
        soup = bs(person_info,'html.parser')
        name = soup.find(class_='profile-username text-center').text
        
        regno = soup.find(class_='text-muted text-center').find('strong').text.rstrip()
    

        image =  soup.find(class_='profile-user-img img-fluid img-circle').get('src')

        image_url = secure_url+image[1:]
        image_response = session.get(image_url)

        ##save the image
        
        #image = open(f"{regno}.jpg", "wb").write(image_response.content)

        info = soup.select('li.list-group-item')

        content =  []
        for tag in info:
            tag = tag.find(class_="float-right").text.rstrip()
            content.append(tag)

    
        gender =  content[0]
        dob =  content[1]

    

        level = soup.select('p.text-muted')
        level = level[-1].text.strip().replace("   "," ")
    

    
    
    
    
        mail = soup.find('input',{'name':'email'}).get('value')
        mobile = soup.find('input',{'name':'phone_number'}).get('value')
        martial_status = soup.find(id='marital_status_id').find('option',selected=True).text.strip()

        nationality = soup.find(id='nationality_id').find('option',selected=True).text.strip()
    

        academic_info = [p for p in links if '/admission/registrationct' in p]
        academic_info = (f'https://soma.dit.ac.tz/{academic_info[0]}')
        academic_info = session.get(academic_info).text
        soup = bs(academic_info,'html.parser')

        academic_year = soup.find('h4').text.strip()[-9:]
        

        module_link = soup.find_all('a')[-3].get("href")
        module = (f'https://soma.dit.ac.tz{module_link}')

        module = session.get(module).text
        modules = pd.read_html(module)[0]
        modules = pd.DataFrame(modules)
        NTA_level = (modules['Code'][0][5])
    elif 'invalid' in p.text:
        print('Login Failed: invalid credentials'+ str(p.status_code))
    else:
       print('invalid status code') 

def studentImage(email,password):
    
    
        global photo,mail,mobile,martial_status,nationality,gender,dob,academic_year,NTA_level,regno,name
        
        login_url = 'https://soma.dit.ac.tz/login'
        secure_url = 'https://soma.dit.ac.tz/'
        session = requests.Session()
        secure_url = 'https://soma.dit.ac.tz/'
        request = session.get(login_url).content

        soup = bs(request,'html.parser')

        csrf = soup.find('input',{'name':'csrf'}).get('value')

        payload = {
                'email': email,
                'password': password,
                'csrf': csrf,  

                }


        p = session.post(login_url,data=payload)
        if 'Welcome, you have successfully logged into your account' in p.text:
            print('successful login')

            t = session.get(secure_url)

            soup = bs(t.text, "html.parser")

            link =soup.select('a.nav-link')
            links = [ links.get("href") for links in link] 
            
            
            person_info = [p for p in links if '/student-profile-registration' in p]


            person_info = (f'https://soma.dit.ac.tz/{person_info[0]}')
            person_info = session.get(person_info).text

            
            soup = bs(person_info,'html.parser')
            image =  soup.find(class_='profile-user-img img-fluid img-circle').get('src')

            image_url = secure_url+image[1:]
            image_response = session.get(image_url)

            ##save the image
            
            image = open(f"{regno}.jpg", "wb").write(image_response.content)
        
        elif 'invalid' in p.text:
            print('Login Failed: invalid credentials'+ str(p.status_code))
        else:
            print('invalid status code') 
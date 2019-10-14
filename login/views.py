from bs4 import BeautifulSoup
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from selenium import webdriver


# Create your tests here.
from userinfo.models import User


def index(request):
    return render(request, 'login/wink.html')

def afterLogin(request):
    return render(request, 'login/wink_afterlogin.html')

#######chrome option
from login.models import UserScheduleDB

path = 'C:/Users/lizel/AppData/Local/Programs/Python/chromedriver.exe'  # ex. C:/downloads/chromedriver.exe
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
driver = webdriver.Chrome(path, chrome_options=options)

###############chrome option end

def logincheck(id, pw):
    #options = webdriver.ChromeOptions()

    # UserAgent값을 바꿔줍시다!
    #

    driver.get('https://ktis.kookmin.ac.kr/')
    print('driver get finish')
    driver.implicitly_wait(15)
    
    print('implicitly_wait finish')
    driver.execute_script("document.getElementsByName('txt_user_id')[0].value=\'" + id + "\'")
    # time.sleep(1)
    driver.execute_script("document.getElementsByName('txt_passwd')[0].value=\'" + pw + "\'")
    # time.sleep(1)

    driver.find_element_by_xpath(
        '/html/body/form[1]/table/tbody/tr/td/table/tbody/tr[4]/td[1]/table/tbody/tr[2]/td/table/tbody/tr[4]/td[2]/input').click()

    driver.implicitly_wait(3)
    driver.get('https://ktis.kookmin.ac.kr/kmu/ucb.Ucb0164rAGet01.do')
    userinfo = User.objects.all()
    print('userinfo')
    if(userinfo.filter(name=id, password=pw)):
        print('login check - already has data')
    else:
        userinfo = User(name=id, password=pw)
        userinfo.save()
    return 0
def Login(request):
    # id=request.POST['id']
    # pw=request.POST['pw']
    # userInfo = UserInfo.objects.all()
    # userInfo = userInfo.filter(userID=id, userPW=pw)
    # if str(userInfo)=='<QuerySet []>':      #could not search to info
    #     userInfo = UserInfo(userID=id, userPW=pw)
    #     userInfo.save()
    try:    #try login
        # driver.get('https://ktis.kookmin.ac.kr/')
        # driver.implicitly_wait(3)
        id = request.POST['id']
        pw = request.POST['pw']
        # driver.execute_script("document.getElementsByName('txt_user_id')[0].value=\'" + id + "\'")
        # # time.sleep(1)
        # driver.execute_script("document.getElementsByName('txt_passwd')[0].value=\'" + pw + "\'")
        # # time.sleep(1)
        #
        # driver.find_element_by_xpath(
        #     '/html/body/form[1]/table/tbody/tr/td/table/tbody/tr[4]/td[1]/table/tbody/tr[2]/td/table/tbody/tr[4]/td[2]/input').click()
        # driver.implicitly_wait(3)
        # driver.get('https://ktis.kookmin.ac.kr/kmu/ucb.Ucb0164rAGet01.do')
        logincheck(id, pw)
  
        userSchdule = UserScheduleDB.objects.all()
        userSchdule = userSchdule.filter(student_code=id)
        print('user schedule')
        #print(userSchdule)
        if str(userSchdule)=='<QuerySet []>':

            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            soup.prettify(formatter=lambda s: s.replace('&nbsp', ''))
            notices = soup.findAll('td', attrs={'rowspan': '2'})
            notices2 = soup.findAll('td', attrs={'rowspan': '3'})
            # for n in notices:
            #     print(n.text)
            result = ""
            for n in notices2:
                # print(n.text)
                result += n.text

            blank = result[0]
            result = result.replace(blank, '#')
            result = result[1:]
            #print(result)
            result += '!'
            word = ''

            count = 0
            dataA = ''
            dataB = ''
            dataC = ''
            dataD = ''
            dataE = ''
            dataF = ''
            print(result)
            temp=''
            for i in result:
                if i!='#':
                    word+=i
                else:
                    if word == '':
                        word = 'blank'

                        if count == 0:
                            dataA = word
                            count += 1
                        elif count == 1:
                            dataB = word
                            count += 1
                        elif count == 2:
                            dataC = word
                            count += 1
                        elif count == 3:
                            dataD = word
                            count += 1
                        elif count == 4:
                            dataE = word
                            count += 1
                        elif count == 5:
                            dataF = word
                            count += 1
                        elif count == 6:
                            dataG = word
                            count = 0
                            # print(dataA+dataB+dataC+dataD+dataE+dataF)
                            print(dataA)
                            print(dataB)
                            print(dataC)
                            print(dataD)
                            print(dataE)
                            print(dataF)
                            print(dataG)
                            dbInstance = UserScheduleDB(student_code=id, time=dataA, A=dataB, B=dataC,
                                                        C=dataD,
                                                        D=dataE,
                                                        E=dataF, F=dataG)
                            dbInstance.save()

                    else:

                        if count == 0:
                            dataA = word
                            count += 1
                        elif count == 1:
                            dataB = word
                            count += 1
                        elif count == 2:
                            dataC = word
                            count += 1
                        elif count == 3:
                            dataD = word
                            count += 1
                        elif count == 4:
                            dataE = word
                            count += 1
                        elif count == 5:
                            dataF = word
                        elif count == 6:
                            dataG = word
                            count = 0

                            print(dataA)
                            print(dataB)
                            print(dataC)
                            print(dataD)
                            print(dataE)
                            print(dataF)
                            print(dataG)
                            dbInstance = UserScheduleDB(student_code=id, time=dataA, A=dataB, B=dataC,
                                                        C=dataD,
                                                        D=dataE,
                                                        E=dataF, F=dataG)
                            dbInstance.save()

                    word=''

####################################여기까지 1시간 15분 시간표###################
            result=''
            for m in notices:
                # print(m.text)
                result += m.text

            blank = result[0]
            result = result.replace(blank, '#')
            result = result[1:]
            #print(result)
            result += '!'
            word = ''

            count = 0
            dataA = ''
            dataB = ''
            dataC = ''
            dataD = ''
            dataE = ''
            dataF = ''
            print(result)
            temp=''
            for j in result:
                if j!='#':
                    word+=j
                else:
                    if word == '':
                        word = 'blank'

                        if count == 0:
                            dataA = word
                            count += 1
                        elif count == 1:
                            dataB = word
                            count += 1
                        elif count == 2:
                            dataC = word
                            count += 1
                        elif count == 3:
                            dataD = word
                            count += 1
                        elif count == 4:
                            dataE = word
                            count += 1
                        elif count == 5:
                            dataF = word
                            count += 1
                        elif count == 6:
                            dataG = word
                            count = 0
                            # print(dataA+dataB+dataC+dataD+dataE+dataF)
                            print(dataA)
                            print(dataB)
                            print(dataC)
                            print(dataD)
                            print(dataE)
                            print(dataF)
                            print(dataG)

                            dbInstance.time50 = dataA
                            dbInstance.A50 = dataB
                            dbInstance.B50 = dataC
                            dbInstance.C50 = dataD
                            dbInstance.D50 = dataE
                            dbInstance.E50 = dataF
                            dbInstance.F50 = dataG
                            dbInstance.save()

                    else:

                        if count == 0:
                            dataA = word
                            count += 1
                        elif count == 1:
                            dataB = word
                            count += 1
                        elif count == 2:
                            dataC = word
                            count += 1
                        elif count == 3:
                            dataD = word
                            count += 1
                        elif count == 4:
                            dataE = word
                            count += 1
                        elif count == 5:
                            dataF = word
                        elif count == 6:
                            dataG = word
                            count = 0

                            print(dataA)
                            print(dataB)
                            print(dataC)
                            print(dataD)
                            print(dataE)
                            print(dataF)
                            print(dataG)

                            dbInstance.time50 = dataA
                            dbInstance.A50 = dataB
                            dbInstance.B50 = dataC
                            dbInstance.C50 = dataD
                            dbInstance.D50 = dataE
                            dbInstance.E50 = dataF
                            dbInstance.F50 = dataG

                            dbInstance.save()

                    word=''


            return HttpResponseRedirect('/login/afterlogin/')
        else:
            return HttpResponseRedirect('/login/afterlogin/')
    except:     #login fail
        #print('false')
        return HttpResponseRedirect('/login/', messages.error(request, 'false'))





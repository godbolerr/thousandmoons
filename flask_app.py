# -*- coding: UTF-8 -*-
"""
hello_jinja2: Get start with Jinja2 templates
"""
from flask import Flask, render_template, request

import pandas as pd

from datetime import datetime
from dateutil import relativedelta
import pytz




app = Flask(__name__)

@app.route('/')
def main():
    return render_template('birthdate_input.html')

@app.route('/process1', methods=['POST'])
def process1():
     _birthday = request.form.get('birthday')
     print(_birthday)
     return render_template('birthdate_input.html')

@app.route('/process', methods=['POST'])
def process():
    # Retrieve the HTTP POST request parameter value from 'request.form' dictionary
    day = request.form.get('day')  
    month = request.form.get('month')  
    year = request.form.get('year')  
    hour = request.form.get('hour')  
    minute = request.form.get('minute')  
    

    
    today = datetime.now()
    fullmooncountNow = 0
    
    fullMoonCount = 0
    fullmoondates = []
    myfullmoondates = []

    Dict = {}    
 
 
    Dict['day'] = day
    Dict['month'] = month
    Dict['year'] = year
    
       
    try:
        birthdate = datetime(int(year), int(month), int(day), int(hour), int(minute))
    except ValueError as e:
        return render_template('thousandMoons_error.html',bResult=Dict), 400  # 400 Bad Request
    
    #birthdate = datetime(1946, 11, 9, 8, 7, 30)

    if(birthdate is None ):
        return 'Please go back and enter your name...', 400  # 400 Bad Request
    
    fullMoonDatesFile = '/home/textbookscience/mysite/IST_FullMoonDates1900_2100.csv'
    
    #fullMoonDatesFile = './data/IST_FullMoonDates1900_2100.csv'
    
    print("bdate : ",birthdate)

    with open(fullMoonDatesFile) as file:
        df = pd.read_csv(file)


    
    for row in df.itertuples(name="FullMoon"):
        fullMoonDate = row[1]   
        newDate = datetime.strptime(fullMoonDate, '%d-%m-%Y %H:%M')
        fullmoondates.append(newDate)

    #print('Your Date and time of birth :' , birthdate.strftime("%A, %d %B %Y, %I:%M:%S %p") )

    Dict['dateAndTimeOfBirth'] = birthdate.strftime("%A, %d %B %Y, %I:%M:%S %p")
    
    deltaNow = relativedelta.relativedelta(today, birthdate)
    
    # print('Your age on 1001th Full Moon :' , delta.years, 'Years,', delta.months, 'months,', delta.days, 'days')
    
    Dict['yourAgeToday'] =  "" + str(deltaNow.years) +  ' Years, '+  str(deltaNow.months) + ' months, '+  str(deltaNow.days) +  ' days'
    
    for refDate in fullmoondates:
      # print(refDate)

       if ( refDate > birthdate ) :
           #print(refDate," is greater")
           fullMoonCount += 1
           myfullmoondates.append(refDate.strftime("%A, %d %B %Y, %I:%M:%S %p %z"))
          # print(refDate,fullMoonCount, " is greater")
           if ( fullMoonCount == 1 ) :
                #print('First Full Moon             :' , refDate.strftime("%A, %d %B %Y, %I:%M:%S %p") )
                Dict['firstFullMoon'] = refDate.strftime("%A, %d %B %Y, %I:%M:%S %p")
                
           if ( fullmooncountNow == 0 and refDate > today ) :
               fullmooncountNow = fullMoonCount 
               Dict['fullmooncountNow'] = fullmooncountNow
               Dict['fullmooncountNowDate'] = refDate.strftime("%A, %d %B %Y, %I:%M:%S %p")
               
           if ( fullMoonCount > 999 ):
               #print(refDate," is when you will see 1000 full moons")
               curDate = refDate

               #print('1001th Full Moon            :' , curDate.strftime("%A, %d %B %Y, %I:%M:%S %p") )
               Dict['1000th Full Moon'] = curDate.strftime("%A, %d %B %Y, %I:%M:%S %p")

               delta = relativedelta.relativedelta(curDate, birthdate)

              # print('Your age on 1001th Full Moon :' , delta.years, 'Years,', delta.months, 'months,', delta.days, 'days')

               Dict['age1000moon'] =  "" + str(delta.years) +  ' Years, '+  str(delta.months) + ' months, '+  str(delta.days) +  ' days'

               Dict['myfullmoondates'] = myfullmoondates
               
               birth80 =  birthdate + relativedelta.relativedelta(years=80)
              # print('Your 81st birthday          :' ,birth81.strftime("%A, %d %B %Y, %I:%M:%S %p") )
               Dict['80thBirthday'] = birth80.strftime("%A, %d %B %Y, %I:%M:%S %p")
               
               # Find age on 1000th full moon.
               
               

               break    
    
    # Validate and send response
    if birthdate:
        return render_template('thousandMoons_result.html',bResult=Dict)
    else:
        return render_template('thousandMoons_error.html',bResult=Dict), 400  # 400 Bad Request

if __name__ == '__main__':
    app.run(debug=True)
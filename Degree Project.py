"""
This program asks the user for a Fahrenheit temperature then converts it to Celcius then to Kelvin.
Based on the temperature, your browser will open with somethign funny

"""

import webbrowser



tf = int(input("Fahrenheit temp: "))

def f2c (tf) :  #F to C temp
    ct =  (tf-32)*(5/9) 
    return(ct)
    
def c2k(ct) : #C to K
    kt = ct +273.14
    return (kt)


print("Kelvin temp: " + str(c2k(f2c(tf))))

print("...now go crazy you science genius -_- ")



def openbrowser (t):
    
    if  t >= 75: #beaches look up
        webbrowser.open('https://www.google.com/search?sxsrf=ALeKk02H3qFYfI2kQ_Nt3dIOtaeOovIZUA%3A1599936965176&ei=xRldX4KtCsaItQW67JRw&q=beaches+near+me&oq=beaches+near+me&gs_lcp=CgZwc3ktYWIQAzIICAAQsQMQkQIyBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB5QphFYphFgxxNoAHAAeACAAXSIAXSSAQMwLjGYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=psy-ab&ved=0ahUKEwjCo-PTpeTrAhVGRK0KHTo2BQ4Q4dUDCA0&uact=5')
    elif 0<= t <= 32: #amazon search winter coats
        webbrowser.open ('https://www.amazon.com/Winter-Coat/s?k=Winter+Coat')
    elif t < 0: #morgue look up
        webbrowser.open ('https://www.google.com/search?sxsrf=ALeKk03xQbdHRJ09T7tya2bZxdpbSjU7Dg%3A1599937181898&ei=nRpdX6WZNozIsQWKubyABg&q=caskets+for+sale&oq=caskets+for+sale&gs_lcp=CgZwc3ktYWIQAzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6BAgAEEdQnhBYkBhg1xloAHABeACAAZsCiAHsDJIBBTAuMi41mAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=psy-ab&ved=0ahUKEwjl2467puTrAhUMZKwKHYocD2AQ4dUDCA0&uact=5')
    else:
        pass
    

openbrowser (tf)


    


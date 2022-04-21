#from requests_html import HTML, HTMLSession
# QUIZ_GAME USING WEB SCRAPING:


import requests
from  bs4 import BeautifulSoup



print('Welcome to our Quiz Game!!')
name = input('Enter your name:  ')
player = input("do you want to play "+name +" ?  (yes/no) ")
score = 0
total = 0
print('\n ********************************************* \n')
if player.lower() != 'yes':
    print('Hope, See you again.... :)')
    quit()


else:
    
    url = 'https://www.javatpoint.com/data-structure-mcq'
    r = requests.get(url)
    html_cont = r.content
    soup = BeautifulSoup(html_cont, 'html.parser')

    ans_tags = soup.find_all('div',{'class': "testanswer"})
    ans1 = []
    

    for j in range(len(ans_tags)):
        
        
        u = ans_tags[j].get_text()
        u1 = u[9]
        ans1.append(u1)
    

    attach = soup.find_all('ol', {'class': "pointsa"})

    p_tags = soup.find_all('p', {'class': "pq"})
    question = []
    dic = {}

    for j in range(len(p_tags)):

        u1 = p_tags[j].get_text()
        u2 = attach[j].get_text()
        u3 = u1+'  '+u2
        question.append(u3)

   

    k = -1
    for j in question:
        k+=1
        dic[j] = ans1[k]



    a = True
    i = 0
    print("okayy....let's start :)) ")

    x = 0
    while(a):

        i+=1
        if i >12:
            break
        else:
            print('Heyy '+ name +' Welcome to round: '+str(i))
            print()

            print('Every round has five questions.')
            print('===============================')

            
            z = x+5

            for x in range(x,x+5,1):
                print()
                print(question[x])
                #q = question[x]

                answer = input("type your option - (a/b/c/d) ? ")
                #print(dic[question[x]])
                try:

                    if (answer.lower() == dic[question[x]]):
                        print(dic[question[x]])
                        print('Correct answer! :)')
                        score+=1
                        total+=1
                    else:
                        print(dic[question[x]])
                        print('incorrect anser :(')
                        total+=1
                        
                except KeyError:
                    print('Something going wrong.')
            x = z

            
            print()
            ask = input('Are you continue for the next round? ')
            if ask.lower() == 'yes':
                a = True
            else:
                a = False
            print("/**************************************************/")

print('Hey ' +name +', You got '+ str(score) + ' out of ' + str(total))
print('You got '+ str((score/total) * 100) + '% . ')
print()
print("===========================================")
print('See you again.... :)')
print("===========================================")

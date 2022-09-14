from datetime import datetime
from ntpath import join
from .models import Question, Team
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from django.contrib import messages 
import random

# Create your views here.
def regForm(request):
    return render(request, 'hunt/register.html')

def logForm(request):
    return render(request, 'hunt/login.html')

def handleLogin(request):
    if request.method == 'POST':
        logId = request.POST['loginId']
    
        user = authenticate(username=logId, password='hunter')

        if user is not None:
            login(request, user)
            messages.success(request, f"{logId} Logged in successfully.")
            return redirect('home')
        else:
            messages.warning(request, 'Invalid credentials.')
            return redirect('logForm')
    else:
        return HttpResponse('404 Not Found')

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/hunt/')
    
def home(request):
    if request.user.is_authenticated:

        q = Team.objects.filter(team_username= request.user).values('questions')[0]['questions'].split(',')
        teamQuestions = []

        for i in q:
            teamQuestions.append(int(i))
        
        no = Team.objects.filter(team_username= request.user).values('questions_answered')[0]['questions_answered']
        ques = Question.objects.values('question', 'answer')[teamQuestions[no]]
        if no >= 4:
            logout(request)
            return render(request, 'hunt/greet.html')

        params = {'question':ques['question']}
        return render(request, 'hunt/base.html', params)
    else:
        return render(request, 'hunt/login.html')

def handleregister(request):
    if request.method == 'POST':
        registerIds = request.POST['regId']
        registerIds = registerIds.split(",")
        quesNos = Question.objects.values('id', 'level')
        print(quesNos)
        r1 = []
        r2 = []
        r3 = []
        r4 = []

        for i in quesNos:
            if i['level'] == 'R1':
                r1.append(str(i['id']))
            if i['level'] == 'R2':
                r2.append(str(i['id']))
            if i['level'] == 'R3':
                r3.append(str(i['id']))
            if i['level'] == 'R4':
                r4.append(str(i['id']))

        if len(registerIds) != 20:
            for registerId in registerIds:
                registerId = registerId.strip()
                myuser = User.objects.create_user(username=registerId, password='hunter')
                myuser.save()
                qlist = random.choice(r1) + ',' + random.choice(r2) + ',' + random.choice(r3) + ',' + random.choice(r4) + ',0'
                Team.objects.create(team_username=registerId, questions = qlist,time_started = datetime.now(),time_finished = datetime.now(),questions_answered = 0)
                messages.success(request, f"{registerId} has been registered.")

        else:
            d = {}

            temp = registerIds
            for i in r1:
                data = random.sample(temp, 2)
                d[data[0]] = f"{i},"
                d[data[1]] = f"{i},"
                temp.remove(d[data[0]])
                temp.remove(d[data[1]])
            
            temp = registerIds
            for i in r2:
                data = random.sample(temp, 2)
                d[data[0]] += f"{i},"
                d[data[1]] += f"{i},"
                temp.remove(d[data[0]])
                temp.remove(d[data[1]])

            temp = registerIds
            for i in r3:
                data = random.sample(temp, 2)
                d[data[0]] += f"{i},"
                d[data[1]] += f"{i},"
                temp.remove(d[data[0]])
                temp.remove(d[data[1]])

            temp = registerIds
            for i in r4:
                data = random.sample(temp, 2)
                d[data[0]] += f"{i},0"
                d[data[1]] += f"{i},0"
                temp.remove(d[data[0]])
                temp.remove(d[data[1]])

        return redirect('/hunt/')
    else:
        return HttpResponse('404 Not Found')

def handleAnswer(request):
    if request.method == 'POST':
        q = Team.objects.filter(team_username= request.user).values('questions')[0]['questions'].split(',')
        teamQuestions = []
        for i in q:
            teamQuestions.append(int(i))

        no = Team.objects.filter(team_username= request.user).values('questions_answered')[0]['questions_answered']
        ques = Question.objects.values('question', 'answer')[teamQuestions[no]]
        userAns = request.POST['userAnswer']

        print(ques)

        if userAns.lower().strip() == ques['answer'].lower() and no >= 4:
            Team.objects.filter(team_username= request.user).update(time_finished=datetime.now())
            logout(request)
            return render(request, 'hunt/greet.html')

        elif userAns.lower().strip() == ques['answer'].lower() and no <4:

            no += 1
            ques = Question.objects.values('question', 'answer')[teamQuestions[no]]
            params = {'question':ques['question']}
            Team.objects.filter(team_username= request.user).update(questions_answered=no)
            messages.success(request, "Correct Answer!!!")
            return render(request, 'hunt/base.html', params)

        else:
            
            ques = Question.objects.values('question', 'answer')[teamQuestions[no]]
            params = {'question':ques['question']}
            messages.warning(request, 'Wrong Answer.')
            return render(request, 'hunt/base.html', params)

    return HttpResponse('404 Not Found')

def instruction(request):
    return render(request, 'hunt/instruct.html')
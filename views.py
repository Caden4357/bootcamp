from django.shortcuts import render, redirect
from datetime import datetime
import random

def index(request):
    if 'gold' not in request.session or 'activities' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    context = {
        'activities': request.session['activities']
    }
    return render(request, 'index.html', context)

def process_money(request):
    if request.method == 'GET':
        return redirect('/') 
    else:
        # request.method =='POST'
        now_formatted = datetime.now().strftime("%m/%d/%Y %I:%M%p")
        myGold = request.session['gold']
        location = request.POST['location']
        activities = request.session['activities']
        if location == 'farm':
            goldThisTurn = random.randint(10, 20)

        elif location == 'cave':
            goldThisTurn = random.randint(5, 10)

        elif location == 'house':
            goldThisTurn = random.randint(2, 5)

        else:
            goldThisTurn = random.randint(-50, 50)
            
        myGold += goldThisTurn
        request.session['gold'] = myGold
        if goldThisTurn >= 0:
            str = f"Yay You Got {goldThisTurn} from {location} {now_formatted}"
            activities.append(str)
            request.session['activities'] = activities
        else:
            goldThisTurn < 0
            str = f"OH No! you lost {goldThisTurn} from {location} try again! {now_formatted}"
            activities.append(str)
            request.session['activities'] = activities

        if location == 'reset':
            request.session.flush()
            
    return redirect('/') 


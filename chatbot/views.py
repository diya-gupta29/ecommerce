from django.shortcuts import render,redirect
import os
import aiml
from autocorrect import spell
from django.http import HttpResponse
from django.http import JsonResponse
# from django.conf import settings
# from settings import XMLFILES_FOLDER


# Create your views here.

def homeView(request):
    return render(request, 'chatbot/chat.html')


def get_response(request):
    brainfile="brain.dump"
    kernel = aiml.Kernel()
    # path = XMLFILES_FOLDER+'std-startup.xml'
    kernel.bootstrap(learnFiles='std-startup.xml', commands="LOAD AIML B")
    with open('std-startup.xml', 'r') as f:
        print("###############")
    kernel.saveBrain(brainfile)
    query = request.GET.get('msg')
    question=query
           
    response = kernel.respond(question)
    print(type(response))
    it={1,2}
    print(it)
    
    if response=="1":
        data = {
        'text':"Wait, I ll redirect you to our cakes collection",
        'sf':"1c"  
        }
        return JsonResponse(data)
    
    elif response=="2":
        data = {
        'text':"Wait, I ll redirect you to our bouquets collection",
        'sf':"1b"    
        }
        return JsonResponse(data)
    
    elif response=="3":
        data = {
        'text':"Wait, I ll redirect you to our plants collection",
        'sf':"1p"    
        }
        return JsonResponse(data)
    
    elif response=="4":
        data = {
        'text':"Wait, I ll redirect you to our chocolates collection",
        'sf':"1ch"    
        }
        return JsonResponse(data)
    
    p= response.split()
    
    if len(p)==3:
   
        if (p[0]=="CAKES" or p[0]=="cakes") :
            try:
                cat = 1
                if p[1]=="above" or p[1]=="ABOVE":
                    flag=1
                else:
                    flag = 0
                amount = p[2]
                data = {
                        'text':"Wait, I ll redirect you to our cakes collection",
                        'sf':"2c"  ,
                        'flag':flag,
                        'cat':cat,
                        'amount':amount
                        }
                return JsonResponse(data)
            except ValueError:
                pass 
 

        if (p[0].lower()=="chocolates") :
            cat = 2
            if p[1]=="above" or p[1]=="ABOVE":
                flag=1
            else:
                flag = 0
            amount = p[2]
            data = {
                    'text':"Wait, I ll redirect you to our chocolates collection",
                    'sf':"2c"  ,
                    'flag':flag,
                    'cat':cat,
                    'amount':amount
                    }
            return JsonResponse(data)       # Handle the exception

        elif (p[0]=="plants") :
            cat = 3
            if p[1]=="above" or p[1]=="ABOVE":
                flag=1
            else:
                flag = 0
            amount = p[2]
            data = {
                    'text':"Wait, I ll redirect you to our plants collection",
                    'sf':"2c"  ,
                    'flag':flag,
                    'cat':cat,
                    'amount':amount
                    }
            return JsonResponse(data)   # Handle the exception

 

        else:
            cat = 4
            if p[1]=="above" or p[1]=="ABOVE":
                flag=1
            else:
                flag = 0
            amount = p[2]
            data = {
                    'text':"Wait, I ll redirect you to our bouquets collection",
                    'sf':"2c"  ,
                    'flag':flag,
                    'cat':cat,
                    'amount':amount
                    }
            return JsonResponse(data)      # Handle the exception
    
        
    if response:
        data = {
        'text':str(response), 
        }
        return JsonResponse(data)
    else:
        data = {
        'text':"Ahh! I feel am not intelligent enough. I need to learn more.", 
        }
        return JsonResponse(data)
    

import os
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('mydjangoapp/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
os.system("git clone https://BUDDY1609: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@github.com/BUDDY1609/clone-bot-publi okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 -m bot &")

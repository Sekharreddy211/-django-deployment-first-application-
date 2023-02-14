from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def display(request): #view-function
    print("welcome/ url is requested & display() is executed"); 
    #ss ----> is html-data/code
    ss = '''		
		<center>
			<h2 style="color:Blue;">
				Hello User, Welcome to Django First-Project First-App
			</h2>
			<hr />
		</center>
		'''
	
    return HttpResponse(ss)
def show(request):
    ss='''
        <!--
            HTML Webpage to display "Welcome-Message" with different Headings 
            (F:\SAISIR\HTML\Welcome.html)
        -->


        <html>
            <head>
                <title>****welcome-page</title>
                <style>
                    h1{color:blue;}
                    h2{color:green;}
                    h3{color:red;}
                    h4{color:black;}
                    h5{color:orange;}
                    h6{color:yellow;}
                    h1,h3,h5{background-color:yellow;}
                    h2,h4,h6{background-color:lightgreen;}
                    </style>
            </head>
            <body>
                <center>
                    <h1>Welcome to DJANGO HTML webpage sekhar</h1>
                    <hr color="green" width="96%"/>
                    <h2>welcome to DJANGO HTML webpage pyuish</h2>
                    <hr color="green" width="86%"/>
                    <h3>Welcome to DJANGO HTML webpage sekhar</h3>
                    <hr color="green" width="76%"/>
                    <h4>Welcome to DJANGO HTML webpage sekhar</h4>
                    <hr color="brown" width="66%"/>
                    <h5>Welcome to DJANGO HTML webpage pyuish</h5>
                    <hr color="brown" width="56%"/>
                    <h6>Welcome to DJANGO HTML webpage sekhar</h6>
                    <hr color="brown" width="46%"/>
                  </center>
            </body>
        </html>
    '''
    return HttpResponse(ss)
def hello(request):
	print("hello/ url is requested & hello() is executed");
	ss='''
	<html>
		<head>
			<title>Hello Webpage</title>
			<style>
				h1{
					color:Blue;
					width:90%;
				}
				h2{
					color:Green;
					width:80%;
				}
				h3{
					color:Red;
					width:70%;
				}
				h1,h2,h3{
					background-color:lightblue;
					border:2px Solid Brown;
				}
			</style>
		</head>
		<body>
			<center>
				<h1>Hello User..!!!</h1>
				<hr color='brown' width='80%'/>
				<h2>Welcome to Django-App</h2>
				<hr color='brown' width='60%'/>
				<h3>Have a nice day...</h3>
				<hr color='brown' width='40%'/>
			</center>
		</body>
	</html>
	''';
	return HttpResponse(ss);

import time;	
def senddatetime(request):
	print("dtime/ url is requested & senddatetime() is executed");
	ct = time.ctime()
	print("Client Request Date & time on server :: ",ct);
	ss='''
	<html>
		<head>
			<title>Date-time Webpage</title>
			<style>
				h1{
					color:Blue;
					width:90%;
				}
				h2{
					color:Green;
					width:80%;
				}
				h3{
					color:Red;
					width:70%;
				}
				h1,h2,h3{
					background-color:lightgreen;
					border:2px Solid Brown;
				}
			</style>
		</head>
		<body>
			<center>
				<h1>Welcome to DJango-User..!!!</h1>
				<hr color='brown' width='80%'/>
				<h2>Server-Date & Time :: </h2>
				<hr color='brown' width='70%'/>
				<h3>''',ct,'''</h3>
				<hr color='brown' width='60%'/>
			</center>
		</body>
	</html>
	''';
	return HttpResponse(ss);
    
    
    
    
def demo (request):
    print("multiple-request-url same responce");
    htmldata='''<center>
        <h1>welcome demo user!!!</h3>
        <hr />
        <h2>This is same output for diff-multiple-request-urrls</h2>
        <hr />
        <h3>have a great day...</h3>
        </center>''';
    return HttpResponse(htmldata);


def homepage(request):
    htmldata='''<center>
        <h1>welcome to default home-page!!!</h1>
        <hr />
        <h2>your request page is not-found...</h2>
        <hr />
        <h3>plz try other url or link !!!</h3>
    </center>''';
    return HttpResponse(htmldata);
    
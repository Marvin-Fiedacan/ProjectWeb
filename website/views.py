from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.

def home(request):
	if request.method == "POST":
		msg_name = request.POST['name_person']
		msg_email = request.POST['email']
		msg_phonenum = request.POST['phone']
		msg_message = request.POST['message']

		msg_info = msg_message +'\n\n\n\n\nContact Details: ' + '\nPhone Number: ' + str(msg_phonenum) + '\nEmail Adress: ' + msg_email
		send_mail(
			msg_name, #sender_subject
			msg_info, #message
			msg_email, #email_sender
			['gdrivestorage112803@gmail.com'], #mail_receiver
			)    
		return render(request, 'home.html', {'msg_name': msg_name})
	else:
		return render(request, 'home.html', {})

'''
def post_single(request):
	return render(request, 'post-single.html', {})


def typography(request):
	return render(request, 'typography.html', {})

def base(request):
	return render(request, 'base.html', {})
'''
	#'ambinfiedacan@gmail.com', 
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse

from chat.models import Conversation, User

def terms(request):
    return render_to_response('chat/terms.html')

def faq(request):
    return render_to_response('chat/faq.html')

def contact(request):
    return render_to_response('chat/contact.html')

##################################

def index(request):
    return redirect('/conversations')

def conversations(request):
    latest_conversations = Conversation.objects.all().order_by('-creation_date')[:10]
    return render_to_response('chat/conversations.html',
            {'conversations': latest_conversations})

def conversation_details(request, conversation_id, slug=None):
    conversation = get_object_or_404(Conversation, id=conversation_id)

    if slug is None:
        return redirect(conversation_details, conversation_id=conversation_id, slug='yahoo', permanent=True)

    return render_to_response('chat/conversation_details.html',
            {'conversation': conversation})

def user_details(request, username):
    user = get_object_or_404(User, name=username)
    return render_to_response('chat/user_details.html', {'user': user})

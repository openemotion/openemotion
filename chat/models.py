from django.db import models

# FIXME: user django.contrib.auth.models.User instead:
# Possibly use a UserProfile to store additional information.
# from django.contrib.auth.models import User

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class Conversation(models.Model):
    subject = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    requester = models.ForeignKey(User, related_name="conversations_requested")
    responder = models.ForeignKey(User, related_name="conversations_responded")
    status = models.CharField(max_length=255)

    def __unicode__(self):
        return "'{0.subject}' {0.requester} => {0.responder}".format(self)


class Message(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    conversation = models.ForeignKey(Conversation, related_name="messages")
    author = models.ForeignKey(User, related_name="messages")
    text = models.TextField()

    def __unicode__(self):
        return "'{0.text}' by {0.author}".format(self)

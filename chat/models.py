from django.db import models
from study.models import Study

class ChatRoom(models.Model):
    study = models.OneToOneField(Study, on_delete=models.CASCADE, related_name="chat_room")

class Chat(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name="chats")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
from rest_framework import serializers
from .models import Study
from chat.serializers import ChatSerializer

class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = ["id", "title", "content"]


class StudyDetailSerializer(serializers.ModelSerializer):
    chat_history = serializers.SerializerMethodField()
    class Meta:
        model = Study
        fields = ["id", "title", "content", "chat_history"]

    def get_chat_history(self, obj):
        chat_history = obj.chat_room.chats.all()
        return ChatSerializer(chat_history, many=True).data

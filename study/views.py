from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView
from study.models import Study
from chat.models import ChatRoom
from .serializers import StudySerializer, StudyDetailSerializer

class ListStudyAPIView(ListAPIView):
    queryset = Study.objects.all()
    serializer_class = StudySerializer

class DetailStudyAPIView(RetrieveAPIView):
    queryset = Study.objects.all()
    serializer_class = StudyDetailSerializer

class CreateStudyAPIView(CreateAPIView):
    queryset = Study.objects.all()
    serializer_class = StudySerializer

    def perform_create(self, serializer):
        study = serializer.save()
        chat_room = ChatRoom.objects.create(study=study)

class DeleteStudyAPIView(DestroyAPIView):
    queryset = Study.objects.all()
    serializer_class = StudySerializer
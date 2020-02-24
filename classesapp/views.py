from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .serializers import *
from classes.models import Classroom

class ClassroomListAPIView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializer

class ClassroomDetailAPIView(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

class ClassroomCreateAPIView(CreateAPIView):
    serializer_class = ClassroomCreateSerializer

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

class ClassroomUpdateView(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

class ClassroomDeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

class Register(CreateAPIView):
		serializer_class = RegisterSerializer

from rest_framework import generics

from quiz.models import EssayQuestion, MultipleChoiceQuestion, TrueOrFalseQuestion, Quiz
from quiz.serializers import EssayQuestionSerializer, MultipleChoiceQuestionSerializer, TrueOrFalseQuestionSerializer, \
    QuizSerializer


# class EssayQuestionApiV1(APIView):
#
#     def get(self, request):
#         essayQuestions = EssayQuestion.objects.all()
#         serializers = EssayQuestionSerializer(essayQuestions, many=True)
#         return Response(serializers.data)
#
#     def post(self, request):
#         serializer = EssayQuestionSerializer(data=request.data, context={"request": request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)


class EssayQuestionApiV1(generics.ListCreateAPIView):
    queryset = EssayQuestion.objects.all().select_related()
    serializer_class = EssayQuestionSerializer


class EssayQuestionDetailApiV1(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EssayQuestionSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return EssayQuestion.objects.filter(question_id=pk)


class MultipleChoiceQuestionApiV1(generics.ListCreateAPIView):
    queryset = MultipleChoiceQuestion.objects.all().select_related()
    serializer_class = MultipleChoiceQuestionSerializer


class MultipleChoiceQuestionDetailApiV1(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MultipleChoiceQuestionSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return MultipleChoiceQuestion.objects.filter(question_id=pk)


class TrueOrFalseQuestionApiV1(generics.ListCreateAPIView):
    queryset = TrueOrFalseQuestion.objects.all().select_related()
    serializer_class = TrueOrFalseQuestionSerializer


class TrueOrFalseQuestionDetailApiV1(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TrueOrFalseQuestionSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return TrueOrFalseQuestion.objects.filter(question_id=pk)


class QuizApiV1(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

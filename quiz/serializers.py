from rest_framework import serializers

from quiz.models import Question, EssayQuestion, MultipleChoiceQuestion, TrueOrFalseQuestion, Quiz


class QuestionSerializer(serializers.ModelSerializer):
    figure = serializers.SerializerMethodField()

    class Meta:
        model = Question
        exclude = ['createdDttm', 'modifiedDttm', 'reference']

    def get_figure(self, question):
        # TODO: When submitting a question, then return the figure url correctly.
        return "https://dummyimage.com/150x150"


class EssayQuestionSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()
    type = serializers.SerializerMethodField()

    def get_type(self, question):
        return question.__class__.__name__

    class Meta:
        model = EssayQuestion
        fields = ('question', 'answer', 'type')

    def create(self, validatedData):
        question = validatedData.get('question')
        answer = validatedData.get('answer')

        essayQuestionObject = None
        questionObject = Question.objects.create(**question)

        if questionObject:
            essayQuestionObject = EssayQuestion.objects.create(question=questionObject, answer=answer)

        return essayQuestionObject

    def update(self, instance, validatedData):
        question = validatedData.get('question')

        instance.question.content = question.get('content')
        instance.question.explanation = question.get('explanation')
        instance.question.mark = question.get('mark')

        instance.answer = validatedData.get('answer')

        instance.question.save()
        instance.save()
        return instance


class MultipleChoiceQuestionSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()
    type = serializers.SerializerMethodField()

    def get_type(self, question):
        return question.__class__.__name__

    class Meta:
        model = MultipleChoiceQuestion
        fields = ('question', 'answerOrder', 'choices', 'type')

    def create(self, validatedData):
        question = validatedData.get('question')
        choices = validatedData.get('choices')

        mcqObject = None
        questionObject = Question.objects.create(**question)

        if questionObject:
            mcqObject = MultipleChoiceQuestion.objects.create(
                question=questionObject,
                answerOrder=validatedData.get('answerOrder'),
                choices={'choices': choices}
            )

        return mcqObject

    def update(self, instance, validatedData):
        question = validatedData.get('question')

        instance.question.content = question.get('content')
        instance.question.explanation = question.get('explanation')
        instance.question.mark = question.get('mark')

        instance.answerOrder = validatedData.get('answerOrder')
        instance.choices = validatedData.get('choices')

        instance.question.save()
        instance.save()
        return instance


class TrueOrFalseQuestionSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()
    type = serializers.SerializerMethodField()

    def get_type(self, question):
        return question.__class__.__name__

    class Meta:
        model = TrueOrFalseQuestion
        fields = ('question', 'isCorrect', 'type')

    def create(self, validatedData):
        question = validatedData.get('question')
        isCorrect = validatedData.get('isCorrect')

        tofQuestion = None
        questionObject = Question.objects.create(**question)

        if questionObject:
            tofQuestion = TrueOrFalseQuestion.objects.create(
                question=questionObject,
                isCorrect=isCorrect
            )

        return tofQuestion

    def update(self, instance, validatedData):
        question = validatedData.get('question')

        instance.question.content = question.get('content')
        instance.question.explanation = question.get('explanation')
        instance.question.mark = question.get('mark')

        instance.isCorrect = validatedData.get('isCorrect')

        instance.question.save()
        instance.save()
        return instance


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

    def create(self, validatedData):
        raise NotImplemented

    def update(self, instance, validatedData):
        raise NotImplemented

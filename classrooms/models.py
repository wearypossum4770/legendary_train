from django.db.models import (
    CASCADE,
    Model,
    CharField,
    DateField,
    TextField,
    ForeignKey,
    ImageField,
    TextChoices,
    BooleanField,
    DateTimeField,
    OneToOneField,
    ManyToManyField,
)


class Subject(Model):
    name = CharField(max_length=30)
    color = CharField(max_length=7, default="#007bff")

    def __str__(self):
        return self.name


class Quiz(Model):
    owner = ForeignKey(User, on_delete=CASCADE, related_name="quizzes")
    name = CharField(max_length=255)
    subject = ForeignKey(Subject, on_delete=CASCADE, related_name="quizzes")

    def __str__(self):
        return self.name


class Question(Model):
    quiz = ForeignKey(Quiz, on_delete=CASCADE, related_name="questions")
    text = CharField("Question", max_length=255)

    def __str__(self):
        return self.text


class Answer(Model):
    question = ForeignKey(Question, on_delete=CASCADE, related_name="answers")
    text = CharField("Answer", max_length=255)
    is_correct = BooleanField("Correct answer", default=False)

    def __str__(self):
        return self.text

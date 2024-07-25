from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Question, UserResponse
from .forms import UserResponseForm
from django.http import JsonResponse
import json

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'mcq/question_list.html', {'questions': questions})


def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = UserResponseForm(request.POST)
        if form.is_valid():
            user_response = form.save(commit=False)   
            user_response.user = request.user
            user_response.question = question
            user_response.save()
            return redirect('question_list')
    else:
        form = UserResponseForm()
    return render(request, 'mcq/question_detail.html', {'question': question, 'form': form})

def mcq_json(request):
    data=list(Question.objects.values())
    return JsonResponse(data, safe=False)
 


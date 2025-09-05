import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

def test_create_multiple_choices():
    question = Question(title='q1')
    
    question.add_choice('a', True)
    question.add_choice('b', False)

    choice1 = question.choices[0]
    choice2 = question.choices[1]
    
    assert len(question.choices) == 2
    
    assert choice1.is_correct
    assert not choice2.is_correct

def test_create_choice_with_invalid_text():
    question = Question(title='q1')
    
    with pytest.raises(Exception):
        question.add_choice('')
               
    with pytest.raises(Exception):
        question.add_choice('a'*200)

def test_question_points_out_of_range():
    with pytest.raises(Exception):
        Question(title='q1', points=0)

    with pytest.raises(Exception):
        Question(title='q2', points=101)

def test_remove_choice_by_id():
    question = Question('q1', 1)

    choice = question.add_choice('a')
    question.remove_choice_by_id(choice.id)

    assert choice not in question.choices

def test_remove_invalid_choice_by_id():
    question = Question('q1', 1)

    choice = question.add_choice('a')

    with pytest.raises(Exception):
        question.remove_choice_by_id(1000)

def test_remove_all_choices():
    question = Question('q1', 1)

    question.add_choice('a')
    question.add_choice('b')
    question.remove_all_choices()

    assert len(question.choices) == 0

def test_set_correct_choices():
    question = Question('q1', 1)

    choice1 = question.add_choice('a')
    choice2 = question.add_choice('b')
    
    question.set_correct_choices([choice2.id])
    
    assert choice2.is_correct is True
    assert choice1.is_correct is False

def test_set_correct_invalid_choices():
    question = Question('q1', 1)

    with pytest.raises(Exception):
        question.set_correct_choices([10, 1000])

def test_correct_selected_choices_returns_only_correct():
    question = Question('q1', 1, max_selections=2)

    choice1 = question.add_choice('a', True)
    choice2 = question.add_choice('b', False)

    result = question.correct_selected_choices([choice1.id, choice2.id])

    assert result == [choice1.id]

def test_correct_selected_choices_max_selections():
    question = Question('q1', 1, max_selections=1)

    choice1 = question.add_choice('a', True)
    choice2 = question.add_choice('b', True)
    
    with pytest.raises(Exception):
        question.correct_selected_choices([choice1.id, choice2.id])
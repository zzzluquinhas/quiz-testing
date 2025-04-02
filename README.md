[![tests](https://github.com/andrehora/quiz/actions/workflows/tests.yml/badge.svg)](https://github.com/andrehora/quiz/actions/workflows/tests.yml)

# Quiz testing example

Neste exercício, iremos melhorarar os testes de unidade de sistema de quiz.
Você deve realizar os 5 commits descritos abaixo e submeter os 5 links dos commits via Moodle.

### Overview

Primeiramente, explore o código do sistema em [model.py](https://github.com/andrehora/quiz/blob/main/model.py).
Note que temos duas classes: `Question` (que representa as questões do quiz) e `Choice` (escolha das questões).

Explore também os cinco testes em [tests.py](https://github.com/andrehora/quiz/blob/main/tests.py) para entender melhor como o sistema funciona:
Por exemplo:

```python
def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

...
```

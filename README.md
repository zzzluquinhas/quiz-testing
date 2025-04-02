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

Você deve realizar os 5 commits descritos abaixo e submeter os 5 links dos commits via Moodle.

# Commit 1: Running the tests

Antes de iniciar as atividades de teste, precisamos configurar o repositório de trabalho.

### Crie um fork deste repositório

Primeiramente, crie um fork deste repositório.
Para isso, basta clicar no botão `Fork` no canto superior direito.
Caso tenha dúvidas, verifique a documentação do GitHub sobre como [criar fork de um repositório](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo).

### Ative o GitHub Actions para rodar os testes a cada commit

Neste projeto, utilizamos o GitHub Actions (ferramenta de CI/CD do GitHub) para executar os testes automaticamente a cada commit.
Abra o arquivo`.github/workflows/tests.yml` e observe que os testes são executados em três sistemas operacionais (Ubuntu, macOS e Windows) e várias versões da linguagem Python. Veja um exemplo em https://github.com/andrehora/quiz/actions/runs/14231638679.

Ative o GitHub Actions no seu repositório.
Para isso, basta ir na aba `Actions` e clicar no botão verde.

### Clone o seu repositório

Em seguida, clone o seu repositório para uma pasta local e entre na pasta:

```
$ git clone https://github.com/<SEU-USUARIO>/quiz
$ cd quiz
```

### Instale o pytest

Nossos testes utilizam o framework de testes [pytest](https://docs.pytest.org).
Instale o pytest:

```
$ pip install pytest
```

### Rode os testes localmente

Para executar os testes localmente, basta rodar o comando `pytest -v tests.py`:

```
pytest -v ./tests.py
========================================== test session starts ===========================================
...                                                                                     
tests.py::test_create_question PASSED                                                              [ 20%]
tests.py::test_create_multiple_questions PASSED                                                    [ 40%]
tests.py::test_create_question_with_invalid_title PASSED                                           [ 60%]
tests.py::test_create_question_with_valid_points PASSED                                            [ 80%]
tests.py::test_create_choice PASSED                                                                [100%]

=========================================== 5 passed in 0.01s ============================================
```

### Rode os testes remotamente (via GitHub Actions)

Os testes são executados automaticamente no GitHub Actions sempre que um commit é realizado.
Portanto, para rodar os testes no GitHub Actions, realize uma alteração qualquer neste aquivo `README.md` e faça o commit da alteração com a seguinte mensagem *Commit 1: Running the tests*.

Em seguida, clique na aba `Actions` e veja que os testes foram executados com sucesso no GitHub Actions. 
Observe as execuções em múltiplos sistemas operacionais e versões da linguagem Python.

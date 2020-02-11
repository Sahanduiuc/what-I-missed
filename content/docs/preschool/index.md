---
title: 'Базовые навыки'
date: 2020-02-11
weight: 10
---

Бежим из "point-and-click" (GUI) вселенной: 
командная строка, 
текстовый редактор,
markdown, 
контроль версий. 

<!--more-->

## Не хватает обучения простым навыкам

Твит с продолжением:

{{< tweet 1200917769774141442 >}}

На чем фокусируемся мы:

- командная строка
- текстовый редактор
- разметка текста в markdown
- контроль версий (git)
- Jupyter / Colab, удаленные вычисления

## Литература

- [Art of Command Line](https://github.com/jlevy/the-art-of-command-line#basics)
- часть лекций из первой темы в <https://www.sas.upenn.edu/~jesusfv/teaching.html>, включая 
  <https://www.sas.upenn.edu/~jesusfv/Lecture_HPC_3_OS_Basic_Utilities.pdf>
- [Datascience at the Commandline](https://www.datascienceatthecommandline.com/)
- [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/)

## Почему Microsoft так рекламирует свой терминал для Windows?

{{< youtube 8gw0rXPMMPE >}}

### Командная строка 

> Fluency on the command line is a skill often neglected or considered arcane, but it improves your flexibility and productivity as an engineer in both obvious and subtle ways.

### Установка

На Windows - ставим [WSL](https://docs.microsoft.com/ru-ru/windows/wsl/install-win10)

Альтернативы для Windows:

<ul>
<li><a href="https://github.com/bmatzelle/gow/wiki" target="_blank">GOW</a></li>
<li>Cygwin, MinGW</li>
<li><a href="https://git-scm.com/downloads" target="_blank">Git for Windows</a></li>
<li><a href="https://cmder.net/" target="_blank">cmder</a></li>
</ul>

Android:

- [Termux](https://habr.com/ru/post/444950/)

Mac/Linux: все и так есть.

### Идеи

- file system (`~` or `%USERPROFILE%`, `PATH`)
- streams and redirection (`>`, `>>`, `|`)
- arguments and flags ([docopt](http://docopt.org/))
- package managers (apt, choco, brew)

### Пример с командой tree

```
apt-get install tree
man tree
tree / -d -L 2
```
Можно запустить в [Google Colab](https://colab.research.google.com/drive/1kAZEJOak7NZqv8JEIm5p6KatR5zJz1bp)

### Редакторы

- notepad.exe (Windows)
- vim (`:q`), emacs, nano (Linux)
- Notepad++ (Windows)
- семейство `Ctrl-Shift-P`:
  - Atom
  - Sublime
  - VSCode

Pедактор и среда для программирования (IDE) - могут быть разными.

IDE (Python):

- Idle
- Spyder
- PyCharm
- VSCode 

IDE (R):

- R Studio

### Легкая разметка - Markdown

![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Markdown-mark.svg/208px-Markdown-mark.svg.png)

Сферы применения:

- документация
- статические сайты
- текст в Jupyter
- переписка (github issues)
  
Ссылки:

- <https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet>
- <https://commonmark.org/help/>
- <https://pandoc.org/>

### Текстовые приложения

- <http://todotxt.org/>
- <https://gist.github.com>

### Система контроля версий

- `~` Dropbox для кода и любых текстовых файлов
- Важна организация файлов и папок (README.md, `src` и т.д.)
- Возможность совместной работы на кодом (PR, issues)
- Код можно исполнить на другой машине
- Видна история изменений
- Ответвления (версии, ветки)
- Текст можно превратить в статичный сайт
- Тесты, могут исполняться при каждом обновлении кода (CI)
- Интерфейс - и командная строка, и графические клиенты
- git, но она не единственная
- [Github](https://guides.github.com/introduction/flow/) / [Gitlab](https://about.gitlab.com/)

### Дополнительная иллюстрация

![](https://raw.githubusercontent.com/jduckles/dsskills/master/ds_for_research.png)

<https://github.com/jduckles/dsskills> 
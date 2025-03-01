Программа генерирует псевдомонгольские названия для Аврор

**Основные моменты:**
1) Есть список допустимых слогов, из которых составляются слова. Слоги выбираются случайно. 
2) Есть список допустимых окончаний. Для каждого есть определенная вероятность. 
3) Слова генерируются из 4-7 слогов в основной части. Соответственно, с учетом окончания слогов получается 5-8. Это число также рандомное, наиболее часто будут генерироваться слова из 6-7 слогов.
4) Максимальная длина слова ограничена 15 символами.
5) Две гласные не могут стоять подряд.
6) Две одинаковые буквы не могут стоять подряд.
7) Присутствует проверка на плохие буквосочетания.

Версия 1.0 работает в том числе на версиях Python ниже 3.6.
Версия 2.0 и выше работает начиная с Python версии 3.6.

**Change-log:**

*v2.1*
- Добавлена проверка на плохие буквосочетания
- Добавлены вероятности окончаний

*v2.0*
- Код переписан с нуля
- Слова с буквой Ё больше не генерируются
- Добавлены новые окончания
- Добавлено больше допустимых слогов
- Добавлены вероятности длины основной части слова

*v1.0*
- Базовый релиз

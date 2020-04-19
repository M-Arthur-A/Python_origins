"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать с помощью функции-генератора.
"""
from random import randint
from time import sleep


class LotoGame:
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer
        self._money = randint(1, 100)
        self.money = 0
        self.winner = None
        self.raund = 1
        self.maxraund = randint(50, 80)

    def input(self, text):
        return input(f'{text}\n-> : ')

    def check(self):
        """ проверка кто выигрывает"""
        print(f'{self._player.gamer}у повезло с {self._player.score} бочонками.')
        print(f'Тогда как {self._computer.gamer}у повезло с {self._computer.score} бочонками!')
        print('Побеждает', self._player.gamer if self._player.score >= self._computer.score else self._computer.gamer,
              '!!!')

    def randomizer(self):
        exclude = []  # чтобы рандомные числе не повторялись
        while len(exclude) < 90:
            rand = randint(1, 90)
            if rand not in exclude:
                exclude.append(rand)
                yield rand

    def start(self):
        # проверка чтобы вычеркиваемая цифра была
        print("Здравствуйте! Вас приветствует Geekbrain's ЛОТО!")
        print('Совершенно бесплатно мы дарим Вам новенький билет. Взгляните!')
        print(self._player)
        input("Нажмите <Enter>, чтобы поблагодарить Geekbrain's ЛОТО и продолжить...: ")
        print()
        print('Также билет получает Ваш комьютер. Посмотрите на него:')
        print(self._computer)
        print('Мы будем доставать из лот(х)отрона случайный бочонок и называть его номер!')
        print('Если № бочонока совпадает с числом на Вашем билете, Вы можете его вычеркнуть!')
        print('Если номера в Вашем билете нет - продолжить! Если Вы ошибаетесь - побеждает компьютер!')
        input('Прежде чем мы приступим к самому интересному нажмите <Enter>...:')
        print()
        print('Призовой фонд составляет', self._money, 'млн печенек на geekbrains! И Вы можете получить их все!')
        print('Каждые 10 раундов Вы можете остановить лототрон.')
        print('Если у Вас совпадений больше, то Вы получите % от всех совпадений у Вас и у компьютера! Например:')
        print()
        print('90 раундов - 100%. Текущий раунд 10, если у вас 4 совпадения, а у компьютера 3. То % Ваше выиграша')
        print('рассчитывается следующим образом: 10/90 * 4/(4+3) = 6,3% от призового фонда')
        input('Если готовы начать, нажмите <Enter>...')
        print()
        print(f'Сегодня проведем {self.maxraund} раундов. ')

        r = self.input('Либо нажмите <Enter>, чтобы продолжить, либо введите число раундов')
        if r.isnumeric():
            self.maxraund = int(r) if int(r) <= self.maxraund else self.maxraund

        number = self.randomizer()  # создаем генератор случайных уникальных чисел

        while self.raund <= self.maxraund:
            check = 0  # если пользователь захотел узнать кто выигрывает, завершить игру досрочно будет нельзя
            print()
            print()
            print()
            print(
                '____________________________________________________________________________________________________')
            print(f'                                              РАУНД {self.raund}')
            print(
                '____________________________________________________________________________________________________')
            print()
            print(f'Мы достаем из лототрона бочонок под номером.', end='')
            sleep(1)
            print(f'.', end='')
            sleep(1)
            print(f'.')
            sleep(1)
            num = next(number)
            print(
                f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   {num}   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
            print('Напоминаем Ваш билет.')
            print(self._player)
            print('Ваши возможные действия:')
            print(f'                        Чтобы вычеркнуть {num} из Вашего билета,  нажмите <y>')
            print(f'                        Если в Вашем билете не оказалось {num},   нажмите <n>')
            if check == 0:
                print(f'                        Если хотите узнать кто выигрывает,     нажмите <c>')
            if self.raund % 10 == 0 and check == 0:
                print(f'                  !!!!! Чтобы завершить игру и проверить выигрыш, нажмите <e>')

            while True:
                user_in = self.input('Каково Ваше решение?')

                if self.raund % 10 == 0:  # если есть возможность досрочно завершить игру
                    if self._player.score >= self._computer.score:
                        self.money = round(self._money * (self.raund / 90) * (
                                self._player.score / (self._player.score + self._computer.score)))
                    if user_in == 'e':
                        print(f'У Вас {self._player.score} правильных ответов.')
                        print(f'У Компьютера {self._computer.score} правильных ответов.')
                        print(f'Ваш выигрыш составил {self.money} млн печенек.')
                        self.winner = 'Пользователь' if self._player.score >= self._computer.score else 'Компьютер'
                        if self.winner == 'Компьютер':
                            self.money = 0
                        return None
                    else:
                        txt = 'выиграли' if self._player.score >= self._computer.score else 'проиграли'
                        print(f'Если бы Вы завершили игру сейчас, то Вы бы {txt}!')

                if user_in == 'c':
                    txt = 'выигрываете' if self._player.score >= self._computer.score else 'проигрываете'
                    print(f'Вы {txt}!')
                    check = 1
                    continue

                if user_in == 'y':
                    if num in self._player._database:
                        self._player.minus(num)
                        self._player.score += 1
                        break
                    else:
                        print('БЕССЛАВНОЕ ПОРАЖЕНИЕ!!! У Вас нет этого числа!')
                        self.money = 0
                        self.winner = 'Компьютер'
                        return None

                if user_in == 'n':
                    if num not in self._player._database:
                        break
                    else:
                        print('БЕССЛАВНОЕ ПОРАЖЕНИЕ!!! У Вас же было это число!')
                        self.money = 0
                        self.winner = 'Компьютер'
                        return None

                else:
                    print('Выберите, пожалуйста, что-то из перечисленных действий!')
            # Рассчитывем компьютер
            if num in self._computer._database:
                self._computer.minus(num)
                self._computer.score += 1
            self.raund += 1
        self.winner = 'Пользователь' if self._player.score > self._computer.score else 'Компьютер'
        if self.winner == 'Пользователь':
            self.money = self._money
            print(
                f'ПОЗДРАВЛЯЕМ! ВЫ СОРВАЛИ БАНК ({self.money} млн печенек)!!! У Вас счастливых бочноков {self._player.score} против {self._computer.score} у компьютера.')
        elif self._player.score == self._computer.score:
            self.winner = 'Ничья'
            self.money = self._money / 2
            print(f'Ничья! Вы получаете половину призового фонда, а именно {self.money}.')
        else:
            print(
                f'Вам не повезло :( У Вас счастливых бочноков {self._player.score} против {self._computer.score} у компьютера.')


class LotoCard:
    def __init__(self, name):
        self.gamer = name
        self.score = 0

        # создаем уникальные числа в карточке
        self._data = []
        exclude = []
        for _ in range(3):
            temp_list = []
            for i in range(5):
                while True:
                    rand_num = randint(1, 90)
                    if rand_num not in exclude:
                        temp_list.append(rand_num)
                        exclude.append(rand_num)
                        break
            self._data.append(temp_list)

        # добавляем список для последующего анализа программой (убираем списки в списке и делаем сплошной список)
        self._database = flat_list = [item for sublist in self._data for item in sublist]

        # проверка на уникальность чисел в карточке
        if len(self._database) != len(set(self._database)):
            raise CardCreationError('Числа в карточке не уникальны!!!')

        # вставляем рандомные пробелы между элементами каждого ряда в карточке
        # self.card = deepcopy(self._data) #
        self.card = self._data
        for i in range(3):
            for j in range(4):
                self.card[i].insert(randint(0, 4 + int(j)), '  ')

    def __str__(self):
        # обрамляем карточку консольными табличными рамками
        bottom = ''
        maxlen = 2
        if self.gamer == 'Игрок':
            print('======КАРТОЧКА=ИГРОКА=======')
        else:
            print('====КАРТОЧКА=КОМПЬЮТЕРА=====')
        top = u'\u250C' + u'\u2500' * maxlen + (u'\u252C' + u'\u2500' * maxlen) * (9 - 1) + u'\u2510' + '\n'
        for i, j in enumerate(self.card):
            item = map(lambda x: str(x) if len(str(x)) == maxlen else ' ' * (maxlen - len(str(x))) + str(x), j)
            bottom = bottom + u'\u2502' + u'\u2502'.join(item) + u'\u2502' + '\n'
            if i != len(self.card) - 1:
                bottom = bottom + u'\u251C' + u'\u2500' * maxlen + (u'\u253C' + u'\u2500' * maxlen) * (
                        9 - 1) + u'\u2524' + '\n'
            else:
                bottom = bottom + u'\u2514' + u'\u2500' * maxlen + (u'\u2534' + u'\u2500' * maxlen) * (
                        9 - 1) + u'\u2518' + '\n'
        return top + bottom

    def minus(self, num):
        num = int(num)
        self._database.remove(num)
        for i, sublist in enumerate(self.card):
            for ii, j in enumerate(sublist):
                if j == num:
                    self.card[i][ii] = '--'
                    return None  # чтобы выйти из всех циклов


class CardCreationError(Exception):
    def __init__(self, txt):
        self.txt = txt


human_player = LotoCard('Игрок')
computer_player = LotoCard('Компьютер')
game = LotoGame(human_player, computer_player)
game.start()
if game.winner == 'Ничья':
    print('Сегодня ничья!')
else:
    print('Сегодня победил', game.winner, '!!!')
print(f'Ваш выигрыш составил {game.money}')
print('Ваш билет под конец игры выглядел следующим образом:')
print(game._player)

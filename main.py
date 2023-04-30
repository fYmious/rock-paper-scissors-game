import random

game = True

while game:
    choices = ['камень', 'ножницы', 'бумага']
    computer = random.choices(['камень', 'ножницы', 'бумага'])
    player = None
    while not (player in choices):
        player = input('выберите: камень, ножницы или бумага: ').lower()

    print('компьютер:', ''.join(computer))
    print('вы:', player)

    if ''.join(computer) == player:
        print('ничья!')
    elif (''.join(computer) == 'камень' and player == 'ножницы') or (''.join(computer) == 'бумага' and player == 'камень') or (''.join(computer) == 'ножницы' and player == 'бумага'):
        print('вы проиграли')
    else:
        print('вы выиграли!!')

    if not (input('хотите сыграть ещё?(напишите да если хотите)): ').lower() == 'да'):
        game = False

import command_system

def hint():
    message = 'Пока тут ничего нет. Но ведь и квеста пока тоже нет, не так ли?)'
    return message,''

hint_command = command_system.Command()

hint_command.keys = ['подсказка', 'слоожна', 'дай подсказку', 'подскажи',
'наводка', 'дай наводку']
hint_command.description = 'Дать подсказку'
hint_command.process = hint
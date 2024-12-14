team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

# Использование %:
print('количество участников первой команды: %s!' % team1_num)
print('количество участников в обеих командах: %(team1_num)s и %(team2_num)s!' % {'team1_num': team1_num, 'team2_num': team2_num})

# Использование format():
print('количество задач решённых командой 2: {}'.format(score_2))
print('время за которое команда 2 решила задачи: {team1_time} с'.format(team1_time = team1_time))

# Использование f-строк:
print(f'количество решённых задач по командам: {score_1}, {score_2}')
print(f'исход соревнования: {challenge_result}')
print(f'количество задач {tasks_total} и среднее время решения {time_avg}')
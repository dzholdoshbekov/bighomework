import csv



voprosy = []
otvet1 = []
otvet2 = []
otvet3 = []
prav_otvet = []

index = 1
count_correct_answers = 0

score = []

with open('quiz.csv', newline='') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=";")
  for row in csv_reader:
    question = row[0]
    answer1 = row[1]
    answer2 = row[2]
    answer3 = row[3]
    correct_answer = row[4]

    voprosy.append(question)
    otvet1.append(answer1)
    otvet2.append(answer2)
    otvet3.append(answer3)
    prav_otvet.append(correct_answer)

  
while index < len(voprosy):
  print( 'Вопрос №' + str(index) + ':' + voprosy[index])
  print( 'a) ' + otvet1[index])
  print( 'b) ' + otvet2[index])
  print( 'c) ' + otvet3[index])
  user_option = input("Выберите правильный ответ из вариантов (a,b,c): ")

  if user_option == 'a': 
    a = otvet1[index]
    if a == prav_otvet[index]:
      print("Ответ верный!+ 5 баллов на ваш счет!")
      score.append(5)
      count_correct_answers += 1
    else:
      print("Ответ неверный! .")
  elif user_option == 'b':
    b = otvet2[index]
    if b == prav_otvet[index]:
      print("Ответ верный!+ 5 баллов на ваш счет!")
      score.append(5)
      count_correct_answers += 1
    else:
      print("Ответ неверный! .")
  elif user_option == 'c':
    c = otvet3[index]
    if c == prav_otvet[index]:
      print("Ответ верный!+ 5 баллов на ваш счет!")
      score.append(5)
      count_correct_answers += 1
    else:
      print("Ответ неверный!")
  else:
    print("Такого варианта ответа не существует!")

  index += 1

totalscore = sum(score)

print("Тест завершен ваша оценка: " + str(totalscore))
print("Кол-во верных ответов: " + str(count_correct_answers) + " из " + str(len(voprosy) - 1))

if totalscore == 100:
  print("Ваша оценка: A")
elif totalscore >= 95:
  print("Ваша оценка: A-")
elif totalscore >= 90:
  print("Ваша оценка: B+")
elif totalscore >= 87:
  print("Ваша оценка: B")
elif totalscore >= 85:
  print("Ваша оценка: B-")
elif totalscore >= 80:
  print("Ваша оценка: C+")
elif totalscore >= 77:
  print("Ваша оценка: C")
elif totalscore >= 75:
  print("Ваша оценка: C-")
elif totalscore >= 70:
  print("Ваша оценка: D+")
elif totalscore >= 67:
  print("Ваша оценка: D")
elif totalscore >= 65:
  print("Ваша оценка: D-")
else:
  print("Ваша оценка: F")

def hours_to_days(h, d=24):
  s = h / d
  #return int(s)
  return s
print(hours_to_days(48))

#2
def count_successful(students, score=50):
  students_list = str(students).split(' ')
  count_of_pass=0
  for i in range(len(students_list)):
    if int(students_list[i]) >= int(score):
      count_of_pass+=1
  return count_of_pass
print(count_successful('20 30 40 50'))
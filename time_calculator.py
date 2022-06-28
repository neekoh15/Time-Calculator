def add_time(*args):

  keep_going = True
  add_days = int()
  container1 = args[0].split()
  container2 = args[1].split()
  if len(args) >2:
    container3 = args[2]

  exporter1 = container1[0].split(":")
  exporter2 = container2[0].split(":")
  am_or_pm = container1[1]

  #print(am_or_pm)

  hora_ini = int(exporter1[0])
  min_ini = int(exporter1[1])

  hora_sum = int(exporter2[0])
  min_sum = int(exporter2[1])

  #print("hora_ini: ", hora_ini)
  #print("min_ini: ", min_ini)
  #print("hora_sum: ", hora_sum)
  #print("min_sum: ", min_sum)

  if min_ini+min_sum < 60:
    min_ahoras = 0
  else:
    min_ahoras = int((min_ini+min_sum)/60)
  min_result = min_ini + min_sum -60*min_ahoras

  horas_result = hora_ini + hora_sum + min_ahoras


  calculo = (min_sum+hora_sum*60)/1440
  #print(calculo)
  if (min_sum+hora_sum*60)%1440 != 0 and int(calculo) >0:
    days_passed = int(calculo) + 1
  else:
    days_passed =int(calculo)

  days_passed_display = str()
  if days_passed == 1:
    days_passed_display = " (next day)"
  if days_passed >1:
    days_passed_display = " ("+str(days_passed) + " days later)"
  #print(min_sum+hora_sum*60)
  #print("days passed: ",days_passed)


  if am_or_pm == "PM":
    horas_adias = int(horas_result/12)

    if horas_adias%2 == 0:
      am_or_pm_result = "PM"
    else:
      am_or_pm_result = "AM"
      if days_passed == 0:
        days_passed =1
        days_passed_display = " (next day)" 
        add_days = 1

  if am_or_pm == "AM":
    horas_adias = int(horas_result/12)

    if horas_adias%2 == 0:
      am_or_pm_result = "AM"
    else:
      am_or_pm_result = "PM"

  horas_display = horas_result-int(horas_result/12)*12
  horas_display_str = str(horas_display)
  min_display = str(min_result)

  if horas_display == 0:
    horas_display_str = "12"
  if len(min_display) == 1:
    min_display = "0"+min_display
  

  


  if len(args) ==2:
    time_display = horas_display_str+":"+min_display +" "+am_or_pm_result +days_passed_display
  #print(horas_display_str,":", min_display, am_or_pm_result)



  if len(args) ==3:
    starting_day = container3.lower()
    #print(starting_day)

    semana = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    arrival_day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if days_passed >0:
      add_days = days_passed

    index = int()

    for i in range(len(semana)):
      if starting_day == semana[i]:
        index = i
      #print(i)
    #print("index : ",index)
    #print("add days: ", add_days)
    arrival_day_index = days_passed+index -7*((days_passed+index)//7)

    #print("arrival day index: ", arrival_day_index)
    #print("arrival day: ",arrival_day[arrival_day_index])


    time_display = horas_display_str+":"+min_display +" "+am_or_pm_result +", "+ arrival_day[arrival_day_index] +days_passed_display ## <---------- ACA
  #print(horas_display_str,":", min_display, am_or_pm_result)
  print(time_display)


add_time("3:00 PM", "3:10")

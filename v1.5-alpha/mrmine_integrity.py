def m_ic_initialize():
  errors=[]
  errorc=0
  mainlines=248
  guilines=341
  keypresslines=47
  integritylines=57
  launcherlines=44
  mainerror=0
  guierror=0
  keypresserror=0
  integrityerror=0
  launchererror=0
  lines_in_file = open('/workspaces/coolmathgames/v1.5-alpha/mrmine/main_script.py', 'r').readlines()
  number_of_lines = len(lines_in_file)
  print(str(number_of_lines)+"/"+str(mainlines)+" lines, deviation of "+str(mainlines-number_of_lines)+" lines")
  if not number_of_lines==mainlines:
    mainerror=1
  lines_in_file = open('/workspaces/coolmathgames/v1.5-alpha/mrmine/gui.py', "r").readlines()
  number_of_lines = len(lines_in_file)
  print(str(number_of_lines)+"/"+str(guilines)+" lines, deviation of "+str(guilines-number_of_lines)+" lines")
  if not number_of_lines==guilines:
    guierror=1
  lines_in_file = open('/workspaces/coolmathgames/v1.5-alpha/mrmine/keypress_detector.py', "r").readlines()
  number_of_lines = len(lines_in_file)
  print(str(number_of_lines)+"/"+str(keypresslines)+" lines, deviation of "+str(keypresslines-number_of_lines)+" lines")
  if not number_of_lines==keypresslines:
    keypresserror=1
  lines_in_file = open('/workspaces/coolmathgames/v1.5-alpha/mrmine_integrity.py', "r").readlines()
  number_of_lines = len(lines_in_file)
  print(str(number_of_lines)+"/"+str(integritylines)+" lines, deviation of "+str(integritylines-number_of_lines)+" lines")
  if not number_of_lines==integritylines:
    integrityerror=1
  lines_in_file = open('/workspaces/coolmathgames/v1.5-alpha/launcher.py', "r").readlines()
  number_of_lines = len(lines_in_file)
  print(str(number_of_lines)+"/"+str(launcherlines)+" lines, deviation of "+str(launcherlines-number_of_lines)+" lines")
  if not number_of_lines==launcherlines:
    launchererror=1
  if keypresserror==0 and guierror==0 and mainerror==0 and integrityerror==0 and launchererror==0:
    print("Script check complete! Found 0 errors: n/a")
  if keypresserror==1:
    errors+=["keypress_detector.py"]
    errorc+=1
  if guierror==1:
    errors+=["gui.py"]
    errorc+=1
  if mainerror==1:
    errors+=["main_script.py"]
    errorc+=1
  if integrityerror==1:
    errors+=['mrmine_integrity.py']
    errorc+=1
  if launchererror==1:
    errors+=['launcher.py']
    errorc+=1
  if keypresserror==1 or guierror==1 or mainerror==1 or integrityerror==1 or launchererror==1:
    exit("Script check complete! Found "+str(errorc)+""" error(s): """+str(errors))
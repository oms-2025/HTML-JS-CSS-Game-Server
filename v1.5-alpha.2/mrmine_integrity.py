def m_ic_initialize():
  errors=[]
  errorc=0
  mainlines=248
  guilines=341
  keypresslines=47
  integritylines=57
  launcherlines=44
  spritelines=5246
  savewriterlines=4
  mainerror=0
  guierror=0
  keypresserror=0
  integrityerror=0
  launchererror=0
  spriteerror=0
  savewritererror=0
  lines_in_file = open('/workspaces/coolmathgames/v1.5-alpha.2/mrmine/main_script.py', 'r').readlines()
  number_of_lines = len(lines_in_file)
  print(str(number_of_lines)+"/"+str(mainlines)+" lines, deviation of "+str(mainlines-number_of_lines)+" lines")
  if not number_of_lines==mainlines:
    mainerror=1
  lines_in_file = open('/workspaces/coolmathgames/v1.5-alpha.2/mrmine/gui.py', "r").readlines()
  number_of_lines = len(lines_in_file)
  print(str(number_of_lines)+"/"+str(guilines)+" lines, deviation of "+str(guilines-number_of_lines)+" lines")
  if not number_of_lines==guilines:
    guierror=1
  lines_in_file = open('/workspaces/coolmathgames/v1.5-alpha.2/mrmine/keypress_detector.py', "r").readlines()
  number_of_lines = len(lines_in_file)
  print(str(number_of_lines)+"/"+str(keypresslines)+" lines, deviation of "+str(keypresslines-number_of_lines)+" lines")
  if not number_of_lines==keypresslines:
    keypresserror=1
  lines_in_file = open('/workspaces/coolmathgames/v1.5-alpha.2/mrmine_integrity.py', "r").readlines()
  number_of_lines = len(lines_in_file)
  print(str(number_of_lines)+"/"+str(integritylines)+" lines, deviation of "+str(integritylines-number_of_lines)+" lines")
  if not number_of_lines==integritylines:
    integrityerror=1
  lines_in_file = open('/workspaces/coolmathgames/v1.5-alpha.2/launcher.py', "r").readlines()
  number_of_lines = len(lines_in_file)
  print(str(number_of_lines)+"/"+str(launcherlines)+" lines, deviation of "+str(launcherlines-number_of_lines)+" lines")
  if not number_of_lines==launcherlines:
    launchererror=1
  lines_in_file = open('/workspaces/coolmathgames/v1.5-alpha.2/mrmine/sprites.py', 'r').readlines()
  number_of_lines = len(lines_in_file)
  print(str(number_of_lines)+"/"+str(spritelines)+" lines, deviation of "+str(spritelines-number_of_lines)+" lines")
  if not number_of_lines==spritelines:
    spriteerror=1
  lines_in_file = open('/workspaces/coolmathgames/v1.5-alpha.2/mrmine/save_writer.py', 'r').readlines()
  number_of_lines = len(lines_in_file)
  print(str(number_of_lines)+"/"+str(savewriterlines)+" lines, deviation of "+str(savewriterlines-number_of_lines)+" lines")
  if not number_of_lines==savewriterlines:
    savewritererror=1
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
  if spriteerror==1:
    errors+=['sprites.py']
    errorc+=1
  if savewritererror==1:
    errors+=['save_writer.py']
    errorc+=1
  if errorc==0:
    print("Script check complete! Found 0 errors: n/a")
  else:
    exit("Script check complete! Found "+str(errorc)+""" error(s): """+str(errors))
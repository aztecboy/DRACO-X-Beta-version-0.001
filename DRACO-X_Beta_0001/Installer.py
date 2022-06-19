print("Installing modules")
import os,time
try:
    os.system("pip install psutil");os.system("pip install keyboard");os.system("pip install pyfiglet");os.system("pip install pythonnet");os.system("pip install sys")


except:
    print("Failed to install")
    print("Please make sure you have pip installed")
    time.sleep(3)
    quit()
print("finished installing")
time.sleep(3)

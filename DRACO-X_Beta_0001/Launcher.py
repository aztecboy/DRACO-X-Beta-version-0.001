import sys,clr,os,pyfiglet,keyboard,time,psutil;from printy import printy
import wmi;f = wmi.WMI()


clr.AddReference("WeAreDevs_API")
from WeAreDevs_API import ExploitAPI
ex=ExploitAPI()
def clear():
    os.system("cls")
clear()
menu = pyfiglet.figlet_format("DRACO-X", font = "banner3-d" )
printy(menu,"r")

print();printy("Exploiting roblox may get your account banned, we are not responsible.","y")
def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;


printy("~press F5 to inject~","c")
while True:
    if keyboard.is_pressed("F5"):
        try:
            if checkIfProcessRunning("roblox"):
                printy("--injecting--","c")
                if ex.isAPIAttached()==True:
                    break
                status=None
                temp=0
                while True:
                    time.sleep(3)
                    temp+=1

                    if ex.isAPIAttached():
                        break
                    else:
                        try:
                            ex.LaunchExploit()
                            status="Failed"
                        except:
                            status="Error"
                    printy(f"Attempt:{temp} || Status:{status}","r")
                    if temp==6:
                        printy("--injection failed--","r")
                        time.sleep(2)
                        break
                printy("--injected--","c")
                break
            else:
                print();printy("roblox is not running","r")

        except Exception as err:
            printy("Error injecting","r")
            print(err)
            time.sleep(3)
            quit()
clear()
printy(menu,"r")
print();printy("DRACO-X version: Beta 0.001","c")
print()
print();printy("type help for a list of commands","c")
print()
while True:
    print()
    com=input("---> ").split(" ")
    if com[0]=="help":
        printy("-Type clear to clear the terminal.","c")
        printy("-Put a file containing a lua script in the Scripts folder, then type execute-lua <script name> to run it","c")
        printy("-type command help to view a list of commands","c")
        printy("-type inject to inject the api into roblox","c")
    if com[0]=="command":
        if "help" in com[1]:
            printy("-type command bypass to spawn a chat bypass gui","c")
            printy("-type command CMD-X to execute cmd-x in the roblox game","c")
        if "CMD-X" in com[1]:
            with open("MainScripts/cmd.txt","r") as file:
                ex.SendLimitedLuaScript(file.read())
                printy("Executed Command","c")
        if "bypass" in com[1]:
            with open("MainScripts/Byp.lua","r") as file:
                ex.SendLimitedLuaScript(file.read())
                printy("Executed Command","c")
    if com[0]=="clear":
        clear()
    if com[0]=="inject":
        try:
            if ex.isAPIAttached():
                printy("Has already been injected","c")
            else:
                if checkIfProcessRunning("roblox"):
                    printy("--injecting--","c")
                    if ex.isAPIAttached()==True:
                        break
                    ex.LaunchExploit()
                    temp=0
                    while True:
                        time.sleep(3)
                        temp+=1

                        if ex.isAPIAttached():
                            break
                        else:
                            ex.LaunchExploit()
                        printy(f"||Attempt:{temp}||","r")
                        if temp==6:
                            printy("--injection failed--","r")
                            time.sleep(2)
                            break
                    printy("--injected--","c")
                    break
                else:
                    print();printy("roblox is not running","r")

        except Exception as err:
            printy("Error injecting","r")
            print(err)
            time.sleep(3)
    if com[0]=="execute-lua":
        try:
            with open("Scripts/"+com[1],"r") as file:
                ex.SendLimitedLuaScript(file.read())
                printy(f"executed {com[1]}","c")
        except:
            printy("file does not exist","r")


import subprocess
import sys

def runCommands():
        
        #check if args provided correctly
        if len(sys.argv) != 2:
               print("Usage: python3 run.py [INPUT]")
               sys.exit(1)

        #create file
        f = open("output.txt", "w")


        f.write("kto, Kristin To.\n")

        try:
            dateResult = subprocess.run(["date"], capture_output=True, text=True)
            f.write("Command: date\n")
            f.write(dateResult.stdout)
            f.write("\n*****\n")
        except:
            f.write("[ERROR] data command failed\n")
            print("[ERROR] date command failed\n")

        try:
            whoamiResult = subprocess.run(["whoami"], capture_output=True, text=True)
            f.write("Command: whoami\n")
            f.write(whoamiResult.stdout)
            f.write("\n*****\n")
        except:
            f.write("[ERROR] whoami command failed\n")
            print("[ERROR] whoami command failed\n")

        try:
            ifconfigResult = subprocess.run(["ifconfig"], capture_output=True, text=True)
            f.write("Command: ifconfig\n")
            f.write(ifconfigResult.stdout)
            f.write("\n*****\n")
        except:
            f.write("[ERROR] ifconfig command failed\n")
            print("[ERROR] ifconfig commaned failed\n")

        try:
            pingResult = subprocess.run(["ping", str(sys.argv[1]), "-c", "10"], capture_output=True, text=True)
            f.write("Command: ping <INPUT> -c 10\n")
            f.write(pingResult.stdout)
            f.write("\n*****\n")
        except:
            f.write("[ERROR] ping command failed\n")
            print("[ERROR] ping command failed\n")

        try:
            tracerouteResult = subprocess.run(["traceroute", str(sys.argv[1]), "-m", "10"], capture_output=True, text=True)
            f.write("Command: traceroute <INPUT> -m 10\n")
            f.write(tracerouteResult.stdout)
            f.write("\n*****\n")
        except:
            f.write("[ERROR] traceroute command failed\n")
            print("[ERROR] traceroute command failed\n")
        
        f.close()

runCommands()
            

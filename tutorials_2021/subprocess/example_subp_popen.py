# This program is for getting familier with subprocess.popen in order to 
# interact with stdout, stdin, stderr

import subprocess

#program to start subprocess and tap into stdout

pobj=subprocess.Popen(['echo','Hello from Popen'], stdout=subprocess.PIPE)

stdout, stderror=pobj.communicate()  #communicate() returns tuple of stdout and stderr

print(stdout)



# Writing to stdout and stderr and reading it via Popen
print("------------------------------")

f=open("stderr_output.txt",'w')

p1=subprocess.Popen(["echo", "Hi from P1"], stdout=subprocess.PIPE)
# Note: std_test.py write to stdout and stderrr via sys.stdout.write and sys.stderr.writ
proc=subprocess.Popen(["python3", "./std_test.py"], stdout=subprocess.PIPE, stderr=f)
# Writing stderr to file.

output=proc.communicate()

print(output)

f.close()
#p2=subprocess.Popen(["echo", "Hi from P2"],stdin=p1.stdout)

print("\n------------------------Start of new section-------------------")
#Not working. Need more analysis
#P=subprocess.Popen(['python3', 'write_to_stdin.py'], stdin=subprocess.PIPE)
#P.communicate('Hello Sunil') 
#proc = subprocess.Popen(['python', 'write_to_stdin.py'],  stdin=subprocess.PIPE)
#proc.communicate('Hello?')


# write_to_stdin.py
import sys
input = sys.stdin.read()   # This will read stdin data from subprocess.Popen instance

sys.stdout.write('Received: %s'%input)

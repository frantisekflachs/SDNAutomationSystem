import time
import subprocess, os, signal


def kill_child_processes(parent_pid, sig=signal.SIGTERM):
   ps_command = subprocess.Popen("ps -o pid --ppid %d --noheaders" % parent_pid, shell=True, stdout=subprocess.PIPE)
   ps_output = ps_command.stdout.read()
   retcode = ps_command.wait()
   assert retcode == 0, "ps command returned %d" % retcode
   for pid_str in ps_output.split("\n")[:-1]:
      os.kill(int(pid_str), sig)




proc = subprocess.Popen(["gnome-terminal", "-e",
                         "bash -c \"cd /home/user/PycharmProjects/SDNControllers/floodlight && java -jar target/floodlight.jar; /bin/bash -i\""],
                        stdout=subprocess.PIPE)

pid = proc.pid
print(pid)

time.sleep(2)

# ret = os.kill(pid, signal.SIGSTOP)
# print(ret)


kill_child_processes(pid)



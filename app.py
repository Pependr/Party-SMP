import time  
start_time = time.time()

print("Starting server...")
import subprocess
subprocess.call(['java', '-jar', '-Xms12G', '-Xmx12G', '-XX:+UseZGC', '-XX:AllocatePrefetchStyle=1', '-XX:-ZProactive', '-XX:ConcGCThreads=2', 'server.jar'])

print("Hol' up Git Actions!")
print("Running server for next 6 hours")
current_time = time.time()
while current_time - start_time < 3500 * 6:
    current_time = time.time()

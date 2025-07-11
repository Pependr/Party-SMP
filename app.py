import time  
start_time = time.time()

print("Starting server...")
import subprocess
subprocess.call(['java', '-jar', '-Xms6G', '-Xmx6G', '-XX:+UseG1GC', '-XX:MaxGCPauseMillis=130', '-XX:+DisableExplicitGC', '-XX:+AlwaysPreTouch', '-XX:G1NewSizePercent=28', '-XX:G1HeapRegionSize=16M', '-XX:G1ReservePercent=20', '-XX:G1MixedGCCountTarget=3', '-XX:InitiatingHeapOccupancyPercent=10', '-XX:G1MixedGCLiveThresholdPercent=90', '-XX:G1RSetUpdatingPauseTimePercent=0', '-XX:SurvivorRatio=32', '-XX:MaxTenuringThreshold=1', '-XX:G1SATBBufferEnqueueingThresholdPercent=30', '-XX:G1ConcMarkStepDurationMillis=5.0', '-XX:G1ConcRefinementServiceIntervalMillis=150', '-XX:G1ConcRSHotCardLimit=16', '-XX:AllocatePrefetchStyle=3', '-XX:ConcGCThreads=2', 'server.jar'])

print("Hol' up Git Actions!")
print("Running server for next 6 hours")
current_time = time.time()
while current_time - start_time < 3600 * 6:
    current_time = time.time()
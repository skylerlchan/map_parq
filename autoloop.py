import os
import time
from datetime import datetime

while True:
    print(f"\n⏰ Running auto_map_checker.py at {datetime.now().strftime('%H:%M:%S')}")
    
    # Run your map/detection script
    os.system("python auto_map_checker.py")

    # Git commit + push
    os.system("git add index.html annotated_output/*.jpg")
    os.system("git commit -m '🟢 Auto-update map'")
    os.system("git push origin main")

    print("✅ Update pushed. Sleeping for 30 seconds...\n")
    time.sleep(30)

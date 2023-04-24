import time
from Lock import Open, Close
from Hall import HL
import time

def LockL(OC):
    if(OC == True):
        Open()
        time.sleep(30)
        if(HL == True):
            Close()
    
            
        
    
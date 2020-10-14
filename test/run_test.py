
from io import StringIO
import unittest
import os


 
if __name__=='__main__':
    case_path = os.getcwd() #c
    discover = unittest.defaultTestLoader.discover(case_path,pattern="test_cells*.py")      
    output = StringIO()   
    runner = unittest.TextTestRunner(stream=output , verbosity=2) # verbosity  the valude is include of 0,1,2. 1 is default , 0 is simple , 2 is details
    runner.run(discover)
    output.seek(0)
    
    while True:
        strBuf = output.readline()
        if strBuf == "":
            break
        print(strBuf)
    output.close()

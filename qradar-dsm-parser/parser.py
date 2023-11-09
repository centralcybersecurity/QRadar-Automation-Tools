from utils import print_status
import os

DSM_DIR = 'dsms' 

for dsm in os.listdir(DSM_DIR):
    if dsm.endswith('.dsm'):
        data = open(os.path.join(DSM_DIR, dsm)).read()
        valid = validate(data) # parses data 
        print_status(dsm, valid)
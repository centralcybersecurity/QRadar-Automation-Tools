from config import OPEN, CLOSED  
from offense import Offense

open_offenses = [Offense(1, OPEN), Offense(2, OPEN)] 

for offense in open_offenses:
    if should_close(offense):
        offense.update_status(CLOSED)
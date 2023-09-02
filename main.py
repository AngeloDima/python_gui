#dateTime

# %d: Giorno del mese (01-31)
# %m: Mese (01-12)
# %Y: Anno (es. 2023)
# %H: Ore (00-23)
# %M: Minuti (00-59)
# %S: Secondi (00-59)
# %A: Nome del giorno (es. Lunedì)
# %B: Nome del mese (es. Gennaio)
# %Y-%m-%d %H:%M:%S: Formato esteso con data e orario

import datetime

x = datetime.datetime.now()
print(x.strftime("%d/ %m/ %Y"))
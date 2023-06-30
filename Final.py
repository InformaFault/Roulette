import requests
import time
from bloxflip import *

token = "ywmz0d/oyaZsfbajveDgr1UIEso0oCqdJhL4Xqxz0HgWAONcI5+3UJIh0sstXUexE++BxvcztmQiYAQcYqGNxAoHHJiguuvs+1An2iG61pBwgmb8bve1JwY6BO9v//vNEMGQOGSzn2MtSj1cJfuL86tl67QrQzFXWdWbx5HPj/VZTJQC6scFXf34id7zXxxPhlJjMO9xdez0JTB1lhAsG3PExvcrgf1nVnYUBh2WdtZRzctftG7Vkd7C4vbV+igPS4ICpM8x5/9NrjNzSfG6+r/mebImR6bG81PRmFoT8W5KWwOHkvdgM+SpUzLAxxqsoweks8bjYkCBlZS0A4W4gtexrlbRTUCV3mbhMTAp5ci+kTC+94Vq5is33moDtY+TXhCtPzfNVNVIXj06MP5VOMxNSu77hNsJplGk5jJWuTC5AQIPiF6oBrGcBV2CGG6ZVDUsrjr0YeOOGygyOSz2rWej7fPH+sEF0gM6fZ/dCk7fNIMVeIjvLev5DQ2XHuUQXt5HlUryhUIxn0uweGBCJll8cchy6In6hPeLT3rtQcOHGLczMZuT74qOEPOCAAyHYjFH6PXJnzbqFqHgq1vsKTvASQl5wtbgaiEgVUE9Hw7KLr6jo0b3Br1keUh9lKF5O+dSKjukBAPUI9ZDRSeuBUURXDOPAXA1W226FKQq752NxYJgpcc6zWRXz8gTwUjXRx4Aq6h01+UN1F0L3NKWjoG/ci+BXTY9+4t3+cqkAEwDUgZKmxGnfJ6vOUZ+HfUX15lIhIdqdTH9dxz6Llot6RZBlzZpft0foWjsfxPfMgeyI7tOvTClj4Z/6jQVly/+3MN4i7mwlpiJb600xv5BwnM1hOhNpVKC136KelYOmci/NAaz/BkGA2L/f8Tqw6Mh1OtBe4JjFYnO9v49tiy4TRwqUAC/Ime1GinK0hDT16IXUjouV5EmzkaDREqxNOAaiQ5yIId0JtpI6mVcoP9TmcSrk/HwqkgZWDxP161ExbSryqmoZBKs7IY+k8ulVLs9S6kL9M5wxPhVXuV8Un0lnKhQmmSXwIW8QVvs5Kd16x27qEoR+Ly15xOrwHInHeFimSNQrEG+KD2ky7SLaYrnBteGKpAf+mPN3V3b5OQ5CuNAOMJPiqE12/HCibD4W1jYtuLxts4rJWVYmfojGPKEy29bV6vKuNTFHMBWkEcJKBEKsx5YjEbZj5z0ABod4Wy97eS6q/Z9otAS6pj+RSjmFMT5/o8Y0KzHdo1m9D8voIpEntFuqJx61FId/Vi3oE8PI9kYa78Y0eSVUvDRhZ/tirkwKI79ZKe2ADbzEZWxeqK+LyV5uRz0yDrIbFjmeic314HONs0J4i4HmwzMvrXC3Ofj0f1isEgTvH+D1JWlD7+pPlOZfjpfR2/L0/97O2rVErUYJTuaKORsnjfQ1SqzJrXYe9k6KAexMYPekyXyaga54JFTFoL0wWA092qHTnPNOGsA1Hn1JfD44n6okHoUlaO/f2b2QhAFbXDIjKwcqJoJaPv0yez+Sm6SAX6DJ6RQTiSE3rHmXl1Rk1rLIc0B3xU0SKgJY33LebHvM6IvF1y1QT7gOmYemWK40uQHRjLKQV6DdhiVqV4dNJigX4vd9vtdFGm2CwV0JGvKQBb5AuJgdeqdWETpL2rd8aB3QhwRX+iGdXjQhXPh8QPa6e6VSj+gJgIThTfCIvanU3YPlqzBlk2VldBVvMXRwH1z3i5bK48dYdtJReqGfIylTFE6EEdFlEw5qF81EOZzNk4vbltFyuGvtCZUYDa9O/yPlQKG3uNKOOcVMJf1vfCKMt04AgwWFAbR2kh8O+tL424N4qDzF28w8wWDZ9X9OinozvokGzY9gfvLM/2MnvaOsHMzrsxVhhlDDytRRVZAiSxN9lnQJvQ7DxmC33B27aGbNiYm"

previous_block = None
multiplier = 1

def check_roulette_result():
    global previous_block, multiplier
    
    while True:
        time.sleep(3)
        response = requests.get('https://projectmambas.shyzos.xyz/api/games/roulette')
        data = response.json()
        
        
        if not data['success']:
            print("Erreur lors de la récupération des résultats.")
            continue

        current_block = data['eosBlock']
        color = data['winColor']

        if previous_block is None or previous_block != current_block:
            if color == 'red':
                multiplier = 1
            else:
                multiplier *= 2

            print(f"Couleur : {color}")
            print(f"{multiplier}")

            time.sleep(15)

            async def main():

                await slide(token).bet("red", multiplier)

            asyncio.run(main())
            

            previous_block = current_block
        
        time.sleep(1)  # Attendre 1 seconde avant la prochaine vérification

# Exécution du script
check_roulette_result()

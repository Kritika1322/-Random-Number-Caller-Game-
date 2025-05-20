import random
import time

Numbers=list(range(1,101))
random.shuffle(Numbers)

while numbers:
    called_numbers=Numbers.pop()
    print(f"the number called is:{called_numbers}")
    time.sleep(5)

print("All Numbers Called!!\n Game Over!!\n CONGARTUALTIONS To All The Winners")
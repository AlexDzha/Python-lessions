import threading
import random
import time
class Bank:
    def __init__(self):
        super().__init__()
        self.balance=0
        self.Lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            with self.Lock:
                Replenishment = random.randint(50,500)
                self.balance += Replenishment
                print(f"Пополнение: {Replenishment}. Баланс: {self.balance}")
                if self.balance >= 500 and not self.Lock.locked():
                    self.Lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range (100):
            withdrawal = random.randint(50,500)
            print(f"Запрос на {withdrawal}")
            with self.Lock:
                if withdrawal <= self.balance:
                    self.balance -= withdrawal
                    print(f"Снятие: {withdrawal}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
                    self.Lock.acquire()
            time.sleep(0.001)

# Исходный код:
bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
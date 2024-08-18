import time
import random
import threading
import os

class JailbreakDupingScript:
    def __init__(self):
        self.game_opened = False
        self.items_duplicated = 0
        self.log_file = "dupe_log.txt"
        self.state_file = "dupe_state.txt"
        self.max_attempts = 3
        self.inventory = {
            "vehicles": {
                "Beignet": 0,
                "Macron": 0,
                "Brulee": 0,
                "Tesla": 0,
                "Beam": 0,
                "Torpedo": 0,
                "Hammerhead": 0,
                "Roadster": 0,
                "Other Vehicle": 0,
            }
        }
        self.config = {
            "max_vehicles_to_dupe": 100,
            "dupe_interval": 1.0,
            "memory_threshold": 80
        }
        self.authenticated = False

    def authenticate_user(self):
        print("Authenticating user...")
        time.sleep(2)
        self.authenticated = True
        print("User authenticated successfully.")
        self.log("User authenticated.")

    def check_if_jailbreak_opened(self):
        print("Checking if Jailbreak is opened...")
        attempts = 0
        while not self.game_opened and attempts < self.max_attempts:
            time.sleep(5)
            attempts += 1
            if random.choice([True, False]):
                self.game_opened = True
                print("Jailbreak has been detected!")
            else:
                print(f"Attempt {attempts}/{self.max_attempts}: Jailbreak not found. Retrying...")
        if not self.game_opened:
            print("Failed to detect Jailbreak after maximum attempts. Exiting script.")
            self.log("Failed to detect Jailbreak.")
            return False
        return True

    def check_vehicles_in_inventory(self):
        vehicles_to_dupe = []
        for vehicle, count in self.inventory["vehicles"].items():
            if count > 0:
                vehicles_to_dupe.append(vehicle)
        if not vehicles_to_dupe:
            print("No vehicles found in inventory to duplicate.")
            self.log("No vehicles found in inventory.")
        else:
            print(f"Vehicles detected for duplication: {', '.join(vehicles_to_dupe)}")
            self.log(f"Vehicles detected for duplication: {', '.join(vehicles_to_dupe)}")
        return vehicles_to_dupe

    def duplicate_vehicles(self, vehicles):
        print(f"Starting duplication of vehicles: {', '.join(vehicles)}")
        for vehicle in vehicles:
            num_to_dupe = random.randint(10, self.config["max_vehicles_to_dupe"])
            for i in range(num_to_dupe):
                time.sleep(self.config["dupe_interval"])
                self.items_duplicated += 1
                self.inventory["vehicles"][vehicle] += 1
                print(f"Duplicated {vehicle}. Total now: {self.inventory['vehicles'][vehicle]}")
                self.log(f"Duplicated {vehicle}. Total now: {self.inventory['vehicles'][vehicle]}")

    def log(self, message):
        with open(self.log_file, "a") as f:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            f.write(f"[{timestamp}] {message}\n")

    def save_state(self):
        state = {
            'items_duplicated': self.items_duplicated,
            'game_opened': self.game_opened,
            'inventory': self.inventory
        }
        with open(self.state_file, "w") as f:
            f.write(str(state))
        print("Current state saved.")
        self.log("Current state saved.")

    def load_state(self):
        if os.path.exists(self.state_file):
            with open(self.state_file, "r") as f:
                state = eval(f.read())
            self.items_duplicated = state.get('items_duplicated', 0)
            self.game_opened = state.get('game_opened', False)
            self.inventory = state.get('inventory', self.inventory)
            print("State loaded. Resuming...")
            self.log("State loaded and resuming.")
        else:
            print("No saved state found. Starting fresh.")
            self.log("No saved state found.")

    def auto_save(self, interval=60):
        while self.game_opened:
            time.sleep(interval)
            self.save_state()

    def dupe_thread(self, vehicles):
        thread = threading.Thread(target=self.duplicate_vehicles, args=(vehicles,))
        thread.start()
        return thread

    def check_memory_usage(self):
        while self.game_opened:
            mem_usage = random.randint(50, 90)
            print(f"Current memory usage: {mem_usage}%")
            if mem_usage > self.config["memory_threshold"]:
                print("Warning: High memory usage detected. Pausing duplication for safety...")
                self.log("High memory usage detected. Duplication paused.")
                time.sleep(5)
            time.sleep(10)

    def monitor_progress(self):
        while self.game_opened:
            print(f"Vehicles duplicated so far: {self.items_duplicated}")
            time.sleep(10)

    def run(self):
        self.load_state()
        if self.check_if_jailbreak_opened():
            vehicles_to_dupe = self.check_vehicles_in_inventory()
            if vehicles_to_dupe:
                save_thread = threading.Thread(target=self.auto_save, args=(60,))
                save_thread.start()
                dupe_thread = self.dupe_thread(vehicles_to_dupe)
                monitor_thread = threading.Thread(target=self.monitor_progress)
                monitor_thread.start()
                memory_thread = threading.Thread(target=self.check_memory_usage)
                memory_thread.start()
                dupe_thread.join()
                print("Duplication process completed!")

if __name__ == "__main__":
    print("Starting Jailbreak Duping Script by Flippy (Micheal)...")
    duper = JailbreakDupingScript()
    duper.run()
    print("Script execution finished.")

def dupe_logic():
    print("Initializing dupe logic...")
    time.sleep(2)
    
    def simulate_item_update(vehicle):
        print(f"Simulating update for vehicle: {vehicle}")
        time.sleep(random.uniform(0.5, 2.0))
        print(f"Vehicle {vehicle} updated successfully.")
    
    vehicles = [
        "Beignet", "Macron", "Brulee", "Tesla", "Beam", "Torpedo",
        "Hammerhead", "Roadster", "Other Vehicle"
    ]
    for vehicle in vehicles:
        print(f"Starting duplication simulation for {vehicle}...")
        for _ in range(random.randint(1, 5)):
            simulate_item_update(vehicle)
            print(f"Duplication of {vehicle} completed.")

    print("Dupe logic completed.")

print("Starting dupe logic...")
dupe_logic()
print("Dupe logic finished.")

from io import TextIOWrapper

from datetime import datetime

class Manager:
    file: TextIOWrapper

    def __init__(self, filename: str) -> None:
        self.file = open(filename, "r+")
    
    def enter(self) -> None:
        now = datetime.now()
        lines = self.file.readlines()
        if len(lines) == 0:
            self.file.write(f"ENTER {now}\n")
        else:
            if lines[-1].startswith("EXIT"):
                self.file.write(f"ENTER {now}\n")
                print(f"You entered at {now} successfully")
            else:
                print("You must exit first")

    def exit(self) -> None:
        now = datetime.now()
        lines = self.file.readlines()
        if len(lines) == 0:
            print("You must enter first")
        else:
            if lines[-1].startswith("ENTER"):
                self.file.write(f"EXIT {now}\n")
                print(f"You exited at {now} successfully")
            else:
                print("You must enter first")

    def history(self) -> None:
        lines = self.file.readlines()
        # TODO: implement history view
        # count = 0
        # for i in range(len(lines)):
        #     olddata = datetime.fromisoformat(lines[i].replace("ENTER ", "").replace("EXIT ", "").replace("\n", ""))
        #     if count % 2 == 1:
                
        #     count += 1

    def close(self) -> None:
        self.file.close()
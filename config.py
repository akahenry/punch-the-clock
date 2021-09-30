import os

class Config:
    datapath: str
    datafilename: str

    @classmethod
    def __init__(cls) -> None:
        with open(".env", "r") as file:
            for line in file:
                line = line.replace("\n", "")
                data = line.split("=")
                if data[0] == "PUNCH_THE_CLOCK_DATA_PATH":
                    cls.datapath = data[1]
                elif data[0] == "PUNCH_THE_CLOCK_DATA_FILENAME":
                    cls.datafilename = data[1]

        env_datapath = os.getenv("PUNCH_THE_CLOCK_DATA_PATH")
        if env_datapath != None:
            cls.datapath = env_datapath

        env_datafilename = os.getenv("PUNCH_THE_CLOCK_DATA_FILENAME")
        if env_datafilename != None:
            cls.datafilename = env_datafilename

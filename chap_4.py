class Laptop:
    storage_type = "SSD"

    def __init__(self, Ram ,Storage):
        self.Ram = Ram
        self.Storage = Storage
    @classmethod    
    def get_storage_type(cls):
        print(cls.storage_type)

    def get_info(self):
        print(f"Laptop has {self.Ram} Ram & {self.Storage} {self.storage_type}")
            
l1 = Laptop('Bisma', "512")

l1.get_info()
l1.get_storage_type()

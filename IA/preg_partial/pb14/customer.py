class Customer:
    def __init__(self,name):
        self.name = name
        self.member = False
        self.member_type = None

    def get_name(self):
        return self.name

    def is_member(self):
        return self.member
    
    def set_member(self,member):
        self.member = member

    def get_member_type(self):
        return self.member_type

    def set_member_type(self,member_type):
        self.member_type = member_type

    def __str__(self):
        return f"Name: {self.name}, Member: {self.member}, Member_type: {self.member_type}"
    
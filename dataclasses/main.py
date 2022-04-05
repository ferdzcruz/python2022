class person:
    #default values
    # name = 'ferdinand' 
    # address = "imus cavite"

    #initialized a value
    def __init__(self, name,age,gender) -> str:
        self.name = name #instance variable
        self.age = age
        self.gender = gender
        self.agecat = 'young' if age < 20 else 'adult'
        self.asmember = ['father','mother']
        
    def add_member(self, member):
        self.asmember.append(member)

#You can define a function here with values

def values():

    ferdie_profile = person('Ferdinand',40,'M')
    sophie_profile = person('Sophia',9,'F')

    print(ferdie_profile.name, sophie_profile.name)
    print(ferdie_profile.agecat, sophie_profile.agecat)
    sophie_profile.add_member('child')
    print(sophie_profile.asmember[2])


class message:
    def __init__(self,msg) -> str:
        self,msg = msg


        
#default values
# myname = person()
# myname2 = person()
# print(f"Hello{myname.name}!{myname2.name}")
# myname.name = "Sophie"
# print(myname.name , myname2.name)

if __name__ == '__main__':

    values()

    pass






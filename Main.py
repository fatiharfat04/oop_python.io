# programmer = 'fatih'
# def programmer_makan():
#     print('{} makan nasi'.format(programmer))
    
# guru = 'ucup'
# def guru_makan():
#     print('{} makan nasi'.format(guru))

# dokter = 'otong'
# def dokter_makan():
#     print('{} makan nasi'.format(dokter))


# programmer_makan()
# guru_makan()
# dokter_makan()




class orang(object):
    nama = None

    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print("{}, makan nasi".format(self.nama))

class milenial(orang):
    email = None
    __password = None

    def set_pass(self, password):
        self.__password = password

    def __samarkan_pass(self):
        return self.__password.replace('a', '*')

    def set_email(self, email):
        self.email = email

    def info(self):
        print("email kamu adalah {} dan nama kamu {} dan pass {}".format(self.email, self.nama, self.__samarkan_pass()))


class programmer(milenial):

    def info(self):        
        print("email kamu adalah {} dan nama kamu {}".format(self.email, self.nama))

class influencer(milenial):

    def info(self):
        print("email kamu adalah {} dan nama kamu {}".format(self.email, self.nama))


developer = programmer("developer")
developer.set_email("dev@gmail.com")
developer.set_pass("rahasia")
developer.info()

admin = influencer("admin")
admin.set_email("ad@gmail.com")
admin.set_pass("rahasia")
admin.info()




class phone1:
    def detail(self):
        print ('I am phone1')
class phone2:
    def details(self):
        print('I am phone2')
class phone3(phone1,phone2):
     def detailss(self):
         print ('I am phone3')
apple = phone3()
apple.detail()
apple.details()
apple.detailss()
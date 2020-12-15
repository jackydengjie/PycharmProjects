class stu(object):

    def __init__(self,age):
        self.age=age

    def wang(self):
        if self.age<20 :
            print('aaaa')
        else:
            print('bbbb')

def main():
    s1=stu(10)
    s1.wang()

if __name__ == '__main__':
    main()



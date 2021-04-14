'''
Python program to have
Use the mobile phone class(with below conditions) as parent and build the accessory class for a shop for biling purpose.
build a class to store the data of the mobile phones with screen size,ram,company and processor along with Constructor and function to estimate cost of phone based on conditions
  samsung:7000(pr)
  moto:5999
  lenovo:4000
  nokia:6100
  est cost = pr*(scr size/4.0)+pr*(ram/1.0)+pr*(proc/1.0)+0.05*pr

Input
enter screen size(inches):5.5
enter ram (GB):3
enter company name :moto
enter processor speed(Ghz)1.8
do you want a screen guard for your phone? (1 for yes 0 for no):1
do you want a pounch or case for your phone? :1
do you want  earphones for your phone? :0

Output
total cost of your moto phone with accesories is :37843

'''
#mobile class
class mobiles:
    """docstring for mobiles."""
    #ignore the docstring
    #constructor
    def __init__(self, s_size,ram,company,proc):
        self.s_size = s_size
        self.ram = ram
        self.company = company
        self.proc = proc
    #estimator function
    def estimator(self):
        ecost=float()
        if(self.company.lower()=='samsung' or self.company.lower()=='moto'or self.company.lower()=='lenovo' or self.company.lower()=='nokia'):
            if(self.company.lower()=='samsung'):
                ecost = 7000*(self.s_size/4)+7000*(self.ram)+7000*self.proc+0.05*7000
            elif(self.company.lower()=='moto'):
                ecost = 5999*(self.s_size/4)+5999*(self.ram)+5999*self.proc+0.05*5999
            elif(self.company.lower()=='lenovo'):
                ecost = 4000*(self.s_size/4)+4000*(self.ram)+4000*self.proc+0.05*4000
            elif(self.company.lower()=='nokia'):
                ecost = 6100*(self.s_size/4)+6100*(self.ram)+6100*self.proc+0.05*6100
            return ecost
        else:
            print('specified company not available in our catalog')
            return ecost
class acce(mobiles):
    #acce class inheriting mobiles class
    """docstring for acce.mobiles"""
    scg = int()
    pp = int()
    ear = int()
    #constructor
    def __init__(self,scr,ram,com,pro,scg,pp,ear,):
        #initializing mobile instance
        mobiles.__init__(self,scr,ram,com,pro)
        acce.scg = scg
        acce.pp = pp
        acce.ear = ear
        #bill function
    def bill(self):
        #getting data from mobile's estimator
        phc = mobiles.estimator(self)
        tc = acce.scg*200+acce.pp*300+acce.ear*700
        print('total cost of your '+self.company+' phone with accesories is :'+str(int(phc+tc)))


scr = float(input('enter screen size(inches):'))
ram = float(input('enter ram (GB):'))
com = str(raw_input('enter company name :'))
pro = float(input('enter processor speed(Ghz)'))
scg = int(input('do you want a screen guard for your phone? (1 for yes 0 for no):'))
pp = int(input('do you want a pounch or case for your phone? :'))
ear = int(input('do you want  earphones for your phone? :'))
#instantiating acce class
k = acce(scr,ram,com,pro,scg,pp,ear)
k.bill()

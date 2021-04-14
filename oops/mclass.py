'''
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

Output
the estimated cost of your moto phone is around:37343
'''
# mobiles class
class mobiles:
    """docstring for mobiles."""
    #constructor initializing the class variables
    def __init__(self, s_size,ram,company,proc):
        self.s_size = s_size
        self.ram = ram
        self.company = company
        self.proc = proc

    def estimator(self):
        ecost=float()
        #cost estimator calculating the cost based on company if company not listed printing not available in our catalog
        if(self.company.lower()=='samsung' or self.company.lower()=='moto'or self.company.lower()=='lenovo' or self.company.lower()=='nokia'):
            if(self.company.lower()=='samsung'):
                ecost = 7000*(self.s_size/4)+7000*(self.ram)+7000*self.proc+0.05*7000
            elif(self.company.lower()=='moto'):
                ecost = 5999*(self.s_size/4)+5999*(self.ram)+5999*self.proc+0.05*5999
            elif(self.company.lower()=='lenovo'):
                ecost = 4000*(self.s_size/4)+4000*(self.ram)+4000*self.proc+0.05*4000
            elif(self.company.lower()=='nokia'):
                ecost = 6100*(self.s_size/4)+6100*(self.ram)+6100*self.proc+0.05*6100
            print('the estimated cost of your '+self.company+' phone is around:'+str(int(ecost)))
        else:
            print('specified company not available in our catalog')

scr = float(input('enter screen size(inches):'))
ram = float(input('enter ram (GB):'))
com = str(raw_input('enter company name :'))
pro = float(input('enter processor speed(Ghz)'))
#creating instance of mobiles
k = mobiles(scr,ram,com,pro)
#calling estimator function
k.estimator()

from collections import OrderedDict
class Splitwise:
    Group=OrderedDict()
    def __init__(self):
        pass
    def create_group(self,group_name):
        Splitwise.Group[group_name]={}
        print "Group {} created".format(group_name)
    def add_persons(self,group,persons):
        if group not in Splitwise.Group.keys():
            print "Please create {} first".format(group)
        else:
            for i in persons:
                Splitwise.Group[group][i]=0
            print "Added users"
    def add_transactions(self,group,transactions):
        grp=Splitwise.Group[group]
        for i,j in transactions:
            grp[i]+=j
    def balance_of_person(self,group,person):
        grp=Splitwise.Group[group]
        total_sum=0
        total_sum=sum(grp.values())
        print "Total expenditure for {} : {}".format(group,total_sum)
        per_head_share=total_sum/len(grp)
        print "Balance for {} ".format(person)+"is {}".format(grp[person]-per_head_share)
        return (grp[person]-per_head_share)
    def balance_of_persons_in_group(self,group):
        grp=Splitwise.Group[group]
        for i in grp.keys():
            self.balance_of_person(group,i)
    def balance_of_persons_across_groups(self,person):
        grp=Splitwise.Group.keys()
        
        val=0
        for i in grp:
            if person in Splitwise.Group[i].keys():
                val+=self.balance_of_person(i,person)
        print person+ "balance",val
        print grp
    def pr(self):
        print Splitwise.Group
s=Splitwise()
s.create_group('Flipkart')
s.create_group('Party')
s.add_persons('Flipkart',['Aman','b','c'])
s.add_persons('Flipkart',['d'])
s.add_persons('Party',['Aman','Satya'])
s.add_transactions('Party',[('Aman',50)])
s.add_transactions('Flipkart',[('Aman',40),('b',160)])
s.add_transactions('Flipkart',[('Aman',10),('b',10)])
s.add_transactions('Flipkart',[('c',30),('d',60),('c',110)])
s.balance_of_person('Flipkart',"b")
s.balance_of_persons_in_group('Flipkart')
s.balance_of_persons_across_groups("Aman")
s.pr()

import csv
from collections import OrderedDict, namedtuple
def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)

    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def main(tschedule):
    
 with open('input.csv', mode='r') as infile:
    reader = csv.reader(infile)
    row=next(reader)
    presenter,hours,cost=row[0],row[1],row[2]
    tup = namedtuple('tup', [presenter,hours,cost])
    mydict = dict([(rows[0],[rows[1],rows[2]]) for rows in reader])
    presenter=[]
 maxpresent_mincost(mydict,tup)
 mincost_present(mydict,tup)
 
def result_pattern(d):
    """ Result pattern"""
    print "1)Maximum number of presenter with min cost"
    print "Presenters\thours\tcost"
    mincost=d.get('mincost')
    if mincost:
        
       for d in  mincost:
        print str(d[0])+"\t"+str(d[1])+"\t$"+str(d[2])

    else:
        print "Not enough presenters"
        
def result_pattern1(d):
    """ Result pattern"""
    print "2)Minimum cost presenter"
    print "Presenters\thours\tcost"
    mincost=d.get('mincost')
    if mincost:     
       for d in  mincost:
        print str(d[0])+"\t"+str(d[1])+"\t$"+str(d[2])
    else:
        print "Not enough presenters"
 
def maxpresent_mincost(mydict,tup):
     presenter=[]
     for pres in combinations(mydict,3):
       thour=sum(int(mydict[i][0]) for i in pres)
       tcost =sum(int(mydict[i][1][1:]) for i in pres)
       presenter.append((pres,thour,tcost))
     mydict['presenter']=presenter
     output = OrderedDict()
     count=0;
     minlist=[]
     for pres,thour,tcost in mydict['presenter']:  
        if thour==tschedule:
            count +=1
            if count==1:
                minlist.append(tup(pres,thour,tcost))
                output['mincost']=minlist
            elif count:
               #print pres,thour,tcost
               #print output['mincost'][0].cost
               if output['mincost'][0].cost == tcost:
                 minlist.append(tup(pres,thour,tcost))
                 output['mincost']=minlist
               if output['mincost'][0].cost >tcost:
                   minlist=[]
                   minlist.append(tup(pres,thour,tcost))
                   output['mincost']=minlist
               
          
     result_pattern(output)
     
def mincost_present(mydict,tup):
     keys=mydict.keys()
     keys.pop()
     r=len(keys)
     combination=[]
     while r:
         
         for comb in combinations(keys,r):
             combination.append(comb)
         r-=1
     #print combination
     presenter=[]
     for pres in combination:
         thour=sum(int(mydict[i][0]) for i in pres)
         tcost =sum(int(mydict[i][1][1:]) for i in pres)
         presenter.append((pres,thour,tcost))
     mydict['mincost_pres']=presenter
     #print mydict['mincost_pres']
     mydict['presenter']=presenter
     output = OrderedDict()
     count=0;
     minlist=[]
     for pres,thour,tcost in mydict['presenter']:  
        if thour==tschedule:
            count +=1
            if count==1:
                minlist.append(tup(pres,thour,tcost))
                output['mincost']=minlist
            elif count:
                
               if output['mincost'][0].cost == tcost:
                 minlist.append(tup(pres,thour,tcost))
                 output['mincost']=minlist
               if output['mincost'][0].cost >tcost:
                   minlist=[]
                   minlist.append(tup(pres,thour,tcost))
                   output['mincost']=minlist
     
     output['mincost']=[minpres for minpres in minlist if len(minpres.Name)==3]
     result_pattern1(output)
         
            

if __name__=="__main__":

    """Assumed time shcedule 3 and exactly 3 slots"""
    tschedule=3
    main(tschedule)
    
            
        

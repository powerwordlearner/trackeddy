## All this functions were grenerated to dynamically print output.
import sys
import numpy as np
import time
import matplotlib

class Printer():
    """
    Print things to stdout on one line dynamically
    """ 
    def __init__(self):
        self.tic=time.clock()
        sys.stdout.flush()
        
    def printtextoneline(self,string):
        sys.stdout.write("\r\x1b[K"+string.__str__())
        sys.stdout.flush()

    def timepercentprint(self,minv,maxv,step,i,neddies,loop2=None,diagnostics=False):
        data=[]
        percent=(float(i+1)/maxv)*100.0
        etime=round(time.clock()-self.tic)
        stmtime=round((etime/percent)*100)
        
        progress=int(20/(maxv/(step*(i+1))))
        emptyprog=20-progress
        if loop2!=None:
            percent2ndloop=float((float(loop2[2]+1)/loop2[1])*10)
            print(percent2ndloop*10,percent)
            stmtime=round(etime*np.exp(1-(percent2ndloop*10/percent))*100)
            if percent2ndloop==10:
                percent2ndloop='>'
            else:
                percent2ndloop=int(percent2ndloop)
            sys.stdout.write("\r 0% [{0}{1}{2}]{3}% | Elapsed Time: {4} s | Estimated Time: {5} s | Info: {6} |".format("="*progress,percent2ndloop,' '*emptyprog,round(percent),etime,stmtime,neddies))
            data.append(stmtime)
            if i != maxv and loop2[2]!=loop2[1]:
                sys.stdout.flush()
            else:
                print('')
                plt.plot(data)
                plt.show()
        else:
            sys.stdout.write("\r 0% [{0}>{1}]{2}% | Elapsed Time: {3} s | Estimated Time: {4} s | Info: {5} |".format("="*progress,' '*emptyprog,round(percent),etime,stmtime,neddies))
            if percent != 100 and i!=maxv:
                sys.stdout.flush()
            else:
                print('')
        
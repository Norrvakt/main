@@ -0,0 +1,25 @@
# -*- coding: cp1252 -*-
agg = 3;
strosocker = 3;
vaniljsocker = 2;
bakpulver = 2;
vetemjol = 3;
smor = 75;
vatten = 1;

def sockerkaka(antal):
    print ((antal*agg)/4) ,"st �gg"
    print ((antal*strosocker)/4.0) ,"dl str�socker"
    print ((antal*vaniljsocker)/4.0) ,"tsk vaniljsocker"
    print ((antal*bakpulver)/4.0) ,"tsk bakpulver"
    print ((antal*smor)/4.0) ,"g sm�r"
    print ((antal*vatten)/4.0) ,"dl vatten"

#sockerkaka(4)
#sockerkaka(7)
    
def kostnad(P, r, a):
    k = P + (a + 1)*P*r/2
    print "Den totala kostnaden efter",a, "�r �r" ,k, "kr"
kostnad(50000, 0.03, 10)
    

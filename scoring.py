import math

########################
##DICTIONARY KEYS##
#sl = left shoulder
#sr = right shoulder
#el = left elbow
#er = right elbow
#wl = left wrist
#wr = right wrist
#n = neck
#h = hip
#k = knee
#a = ankle
########################

class Scoring(object):
    
    def __init__(self, dic) :
        
        self.sl = dic['sl']
        self.sr = dic['sr']
        self.el = dic['el']
        self.er = dic['er']
        self.wl = dic['wl']
        self.wr = dic['wr']
        self.n = dic['n']
        self.h = dic['h']
        self.k = dic['k']
        self.a = dic['a']
        
    
    def dist(tup1, tup2) :
        (x1, y1) = tup1
        (x2, y2) = tup2
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    
    def slope(tup1, tup2) :
        (x1, y1) = tup1
        (x2, y2) = tup2
        if x1 = x2 : 
            return None
        return ((y1-y2)/(x1-x2))
                
    #sl = shoulder left
    #el = elbow left
    #hl = hand left
    def correctFrontDOWN(self, threshold = 100) :
        (slx, sly) = self.sl
        (srx, sry) = self.sr
        (elx, ely) = self.el
        (hlx, hly) = self.hl        
        (erx, ery) = self.er
        (hrx, hry) = self.hr

        score = 0
        if abs(slope((elx, ely), (hlx, hly))) > 2 :
            score += 50
        if abs(slope((erx, ery), (hrx, hry))) > 2 :
            score += 50
        if (dist((slx, sly), (elx, ely)) <= (0.7)*dist((elx, ely), (hlx, hly))) :
            score += 10
        if (dist((srx, sry), (erx, ery)) <= (0.7)*dist((erx, ery), (hrx, hry))) :
            score += 10
        return (score >= threshold)
        
        
    def correctFrontUP(self, threshold = 150) :
        (slx, sly) = self.sl
        (srx, sry) = self.sr
        (elx, ely) = self.el
        (hlx, hly) = self.hl        
        (erx, ery) = self.er
        (hrx, hry) = self.hr
        score = 0
        if abs(slope((elx, ely), (slx, sly))) > 80 :
            score += 50
        if abs(slope((erx, ery), (srx, sry))) > 80 :
            score += 50
        if abs(slope((elx, ely), (hlx, hly))) > 80 :
            score += 50
        if abs(slope((erx, ery), (hrx, hry))) > 80 :
            score += 50
        return (score >= threshold)
    
        
    #n = neck
    #h = hip
    #k = knee
    #a = ankle
    def correctSideDOWN(self, threshold = 70) :
        (nx, ny) = self.n
        (hx, hy) = self.h
        (kx, ky) = self.k
        (ax, ay) = self.a    

        m1 = slope((nx, ny), (hx, hy))
        m2 = slope((hx, hy), (kx, ky))
        m3 = slope((kx, ky), (ax, ay))
        if abs(m1) <= 0.18 :
            score += 20
        if abs(m2) <= 0.18 :
            score += 20
        if abs(m3) <= 0.18 :
            score += 20
        if abs(m1-m2) <= 0.09 :
            score += 15
        if abs(m2-m3) <= 0.09 :
            score += 15
        return score >= threshold
        
    
    def correctSideUP(self, threshold = 110) :
        (nx, ny) = self.n
        (hx, hy) = self.h
        (kx, ky) = self.k
        (ax, ay) = self.a
        m1 = slope((nx, ny), (hx, hy))
        m2 = slope((hx, hy), (kx, ky))
        m3 = slope((kx, ky), (ax, ay))
        if (math.tan(math.pi / 12)) <= abs(m1) <= (math.tan(25*math.pi/180)) : 
            score += 20
        if (math.tan(math.pi / 12)) <= abs(m2) <= (math.tan(25*math.pi/180)) : 
            score += 20
        if (math.tan(math.pi / 12)) <= abs(m3) <= (math.tan(25*math.pi/180)) : 
            score += 20
        if abs(m1-m2) <= 0.09 :
            score += 50
        if abs(m2-m3) <= 0.09 :
            score += 50
        return score >= threshold

    
    
    
    

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


low_pos = {

        'n' :  (960, 680),
        'sr' :(834, 610),
        'er': (751, 563), 
        'wr' : (751, 704), 
        'sl' :(1043, 610),
        'el': (1168, 563),
        'wl': (1126, 704)
        
}



class Scoring(object):
    
    def __init__(self, dic) :

        
        self.sl = dic.get('sl')
        self.sr = dic['sr']
        self.el = dic['el']
        self.er = dic['er']
        self.wl = dic['wl']
        self.wr = dic['wr']
        self.n = dic['n']
        self.h = dic['h']
        self.k = dic['k']
        self.a = dic['a']
        
    
    def dist(self,x1,y1,x2,y2) :

        return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    
    def slope(self,x1,y1,x2,y2) :

        if x1 == x2 : 
            return None
        return ((y1-y2)/(x1-x2))
                
    #sl = shoulder left
    #el = elbow left
    #hl = hand left
    def correctFrontDOWN(self, threshold = 100) :
        (slx, sly) = self.sl
        (srx, sry) = self.sr
        (elx, ely) = self.el
        (hlx, hly) = self.wl        
        (erx, ery) = self.er
        (hrx, hry) = self.wr

        score = 0
        if (not isinstance(self.slope(elx, ely, hlx, hly), int)) or abs(self.slope(elx, ely, hlx, hly)) > 2 :
            score += 50
        if (not isinstance(self.slope(erx, ery, hrx, hry), int)) or abs(self.slope(erx, ery, hrx, hry)) > 2 :
            score += 50
        if (self.dist(slx, sly, elx, ely) <= (0.7)*self.dist(elx, ely, hlx, hly)) :
            score += 10
        if (self.dist(srx, sry, erx, ery) <= (0.7)*self.dist(erx, ery, hrx, hry)) :
            score += 10
        return (score >= threshold)
        
        
    def correctFrontUP(self, threshold = 150) :
        (slx, sly) = self.sl
        (srx, sry) = self.sr
        (elx, ely) = self.el
        (hlx, hly) = self.wl        
        (erx, ery) = self.er
        (hrx, hry) = self.wr
        score = 0
        
        
        if (not isinstance(self.slope(elx, ely, slx, sly), int)) or abs(self.slope(elx, ely, slx, sly)) > 80 :
            score += 50
        if (not isinstance(self.slope(erx, ery, srx, sry), int)) or abs(self.slope(erx, ery, srx, sry)) > 80 :
            score += 50
        if (not isinstance(self.slope(elx, ely, hlx, hly), int)) or abs(self.slope(elx, ely, hlx, hly)) > 80 :
            score += 50
        if (not isinstance(self.slope(erx, ery, hrx, hry), int)) or abs(self.slope(erx, ery, hrx, hry)) > 80 :
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
        score = 0
        m1 = self.slope(nx, ny, hx, hy)
        m2 = self.slope(hx, hy, kx, ky)
        m3 = self.slope(kx, ky, ax, ay)
        
        if not (isinstance(m1, int) and isinstance(m2, int) and isinstance(m3, int)) : return False
        
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
        score = 0
        m1 = self.slope(nx, ny,hx, hy)
        m2 = self.slope(hx, hy,kx, ky)
        m3 = self.slope(kx, ky,ax, ay)
        
        if not (isinstance(m1, int) and isinstance(m2, int) and isinstance(m3, int)) : return False
        
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

    
if __name__ == '__main__':    
    
    score = Scoring(low_pos)   
    print(score.correctFrontDOWN())

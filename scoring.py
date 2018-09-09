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
    
    def __init__(self, sideUp, sideDown, frontUp, frontDown) :
        self.sideUp = sideUp
        self.sideDown = sideDown
        self.frontUp = frontUp
        self.frontDown = frontDown
        self.results = self.get_results()
        
    
    def dist(self,x1,y1,x2,y2) :

        return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    
    def slope(self,x1,y1,x2,y2) :

        if x1 == x2 : 
            return None
        return ((y1-y2)/(x1-x2))
                

    def correctFrontDOWN(self, threshold = 100) :
        (lsx, lsy) = self.frontDown['ls']
        (rsx, rsy) = self.frontDown['rs']
        (lex, ley) = self.frontDown['le']
        (lwx, lwy) = self.frontDown['lw']        
        (rex, rey) = self.frontDown['re']
        (rwx, rwy) = self.frontDown['rw']

        score = 0
        errors = dict()


        #elbows tucked in
        if ((not isinstance(self.slope(lex, ley, lwx, lwy), int)) or (abs(self.slope(lex, ley, lwx, lwy)) > 5) ) and ((not isinstance(self.slope(rex, rey, rwx, rwy), int)) or (abs(self.slope(rex, rey, rwx, rwy)) > 5) ):
            score += 40

        else :
            errors['le'] = self.frontDown['le']
            errors['re'] = self.frontDown['re']


        if (self.dist(lsx, lsy, lex, ley) <= (0.55)*self.dist(lex, ley, lwx, lwy)) and (self.dist(rsx, rsy, rex, rey) <= (0.55)*self.dist(rex, rey, rwx, rwy)) :
            score += 60

        else :
            errors['le'] = self.frontDown['le']
            errors['re'] = self.frontDown['re']

        if (score < threshold) : #there must have been errors
            return {'hasErrors' : True, 'score' : score, 'points' : errors}

        return {'hasErrors' : False, 'score' : score}
        
    def correctFrontUP(self, threshold = 100) :
        (lsx, lsy) = self.frontUp['ls']
        (rsx, rsy) = self.frontUp['rs']
        (lex, ley) = self.frontUp['le']
        (rex, rey) = self.frontUp['re']
        (lwx, lwy) = self.frontUp['lw']        
        (rwx, rwy) = self.frontUp['rw']

        score = 0
        errors = dict()
        
        if ((not isinstance(self.slope(lex, ley, lsx, lsy), int)) or abs(self.slope(lex, ley, lsx, lsy)) > 4) and ((not isinstance(self.slope(rex, rey, rsx, rsy), int)) or abs(self.slope(rex, rey, rsx, rsy)) > 4) :
            score += 50

        else :
            errors['le'] = self.frontUp['le']
            errors['re'] = self.frontUp['re']
            errors['ls'] = self.frontUp['ls']
            errors['rs'] = self.frontUp['rs']

        if ((not isinstance(self.slope(lex, ley, lwx, lwy), int)) or abs(self.slope(lex, ley, lwx, lwy)) > 4) and ((not isinstance(self.slope(rex, rey, rwx, rwy), int)) or abs(self.slope(rex, rey, rwx, rwy)) > 4) :
            score += 50
        else :
            errors['le'] = self.frontUp['le']
            errors['re'] = self.frontUp['re']
            errors['lw'] = self.frontUp['lw']
            errors['rw'] = self.frontUp['rw']

        if (score < threshold) : #there must have been errors
            return {'hasErrors' : True, 'score' : score, 'points' : errors}

        return {'hasErrors' : False, 'score' : score}    
        
    #n = neck
    #h = hip
    #k = knee
    #a = ankle
    def correctSideDOWN(self, threshold = 80) :
        (nx, ny) = self.sideDown['n']
        (sx, sy) = self.sideDown['ls']
        (hx, hy) = self.sideDown['lh']
        (kx, ky) = self.sideDown['lk']
        (ax, ay) = self.sideDown['la']   

        score = 0
        errors = dict()

        m1 = self.slope(sx, sy, hx, hy)
        m2 = self.slope(hx, hy, kx, ky)
        m3 = self.slope(kx, ky, ax, ay)
        
        if not (isinstance(m1, int) and isinstance(m2, int) and isinstance(m3, int)) : 
            return {'hasErrors' : true, 'score' : 0, 'points' : {'n' : self.sideDown['n'], 'ls' : self.sideDown['ls'], 
            'lh' : self.sideDown['lh'], 'lk' : self.sideDown['lk'], 'la' : self.sideDown['la']}}
        
        if abs(m1) <= 0.18 :
            score += 20
        else :
            errors['ls'] = self.sideDown['ls']

        if abs(m2) <= 0.18 :
            score += 20
        else :
            errors['ls'] = self.sideDown['ls']

        if abs(m3) <= 0.18 :
            score += 20
        else :
            errors['ls'] = self.sideDown['ls']

        if abs(m1-m2) <= 0.1 :
            score += 20

        if abs(m2-m3) <= 0.1 :
            score += 20

        if (score < threshold) : #there must have been errors
            return {'hasErrors' : True, 'score' : score, 'points' : errors}

        return {'hasErrors' : False, 'score' : score}    

        
    
    def correctSideUP(self, threshold = 80) :

        (nx, ny) = self.sideUp['n']
        (sx, sy) = self.sideUp['ls']
        (hx, hy) = self.sideUp['lh']
        (kx, ky) = self.sideUp['lk']
        (ax, ay) = self.sideUp['la']   

        score = 0
        errors = dict()

        m1 = self.slope(sx, sy, hx, hy)
        m2 = self.slope(hx, hy, kx, ky)
        m3 = self.slope(kx, ky, ax, ay)    

        if not (isinstance(m1, int) and isinstance(m2, int) and isinstance(m3, int)) :
            return {'hasErrors' : true, 'score' : 0, 'points' : {'n' : self.sideUp['n'], 'ls' : self.sideUp['ls'], 
                    'lh' : self.sideUp['lh'], 'lk' : self.sideUp['lk'], 'la' : self.sideUp['la']}}

        
        if (math.tan(math.pi / 12)) <= abs(m1) <= (math.tan(25*math.pi/180)) : 
            score += 15
        if (math.tan(math.pi / 12)) <= abs(m2) <= (math.tan(25*math.pi/180)) : 
            score += 15
        if (math.tan(math.pi / 12)) <= abs(m3) <= (math.tan(25*math.pi/180)) : 
            score += 15

        if (not math.tan(math.pi / 12)) <= abs((m1 + m2 + m3)/3) <= (math.tan(25*math.pi/180)) :
            errors['ls'] = self.sideUp['ls']

        if abs(m1-m2) <= 0.09 :
            score += 30
        else :
            errors['lh'] = self.sideUp['lh']

        if abs(m2-m3) <= 0.09 :
            score += 25
        else :
            errors['lk'] = self.sideUp['lk']

        if (score < threshold) : #there must have been errors
            return {'hasErrors' : True, 'score' : score, 'points' : errors}

        return {'hasErrors' : False, 'score' : score}  


    def get_results(self) :
        return (self.correctSideUP(), self.correctSideDOWN(), self.correctFrontUP(), self.correctFrontDOWN())


    

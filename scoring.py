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
        (lsx, lsy) = self.frontDown['LS']
        (rsx, rsy) = self.frontDown['RS']
        (lex, ley) = self.frontDown['LE']
        (lwx, lwy) = self.frontDown['LW']        
        (rex, rey) = self.frontDown['RE']
        (rwx, rwy) = self.frontDown['RW']

        score = 0
        errors = dict()

        print("fronDown -")
        print('Slope lew = ', self.slope(lex, ley, lwx, lwy) ) 
        print('Slope rew = ', self.slope(rex, rey, rwx, rwy) ) 
        #elbows tucked in
        if ((self.slope(lex, ley, lwx, lwy) == None) or (abs(self.slope(lex, ley, lwx, lwy)) > 3.7) ) and (((self.slope(rex, rey, rwx, rwy) == None)) or (abs(self.slope(rex, rey, rwx, rwy)) > 3.7) ):
            score += 50

        else :
            errors['LE'] = self.frontDown['LE']
            errors['RE'] = self.frontDown['RE']

        print('Ratio of left shoulder elbow / left elbow wrist - ', self.dist(lsx, lsy, lex, ley) / self.dist(lex, ley, lwx, lwy))
        print('Ratio of elbow sep / shoulder sep --', self.dist(lex,ley,rex,rey) / self.dist(lsx,lsy,rsx,rsy))
    
        
        if (self.dist(lsx, lsy, lex, ley) <= (0.7)*self.dist(lex, ley, lwx, lwy)) and (self.dist(rsx, rsy, rex, rey) <= (0.7)*self.dist(rex, rey, rwx, rwy)) :
            score += 10
        elif (self.dist(lsx, lsy, lex, ley) <= (0.65)*self.dist(lex, ley, lwx, lwy)) and (self.dist(rsx, rsy, rex, rey) <= (0.65)*self.dist(rex, rey, rwx, rwy)) :
            score += 20

        else :
            errors['LE'] = self.frontDown['LE']
            errors['RE'] = self.frontDown['RE']

        if (self.dist(lsx, lsy, rsx, rsy)*(1.4) >= self.dist(lex, ley, rex, rey)):
            score += 30
        else :
            errors['LE'] = self.frontDown['LE']
            errors['RE'] = self.frontDown['RE']

        if (score < threshold) : #there must have been errors
            return {'hasErrors' : True, 'score' : score, 'points' : errors}

        return {'hasErrors' : False, 'score' : score}
        
    def correctFrontUP(self, threshold = 100) :
        (lsx, lsy) = self.frontUp['LS']
        (rsx, rsy) = self.frontUp['RS']
        (lex, ley) = self.frontUp['LE']
        (rex, rey) = self.frontUp['RE']
        (lwx, lwy) = self.frontUp['LW']        
        (rwx, rwy) = self.frontUp['RW']

        score = 0
        errors = dict()
        
        print("frontUP -")
        print('Slope les = ', self.slope(lsx, lsy, lex, ley) ) 
        print('Slope res = ', self.slope(rsx, rsy, rex, rey) ) 
        if ((self.slope(lex, ley, lsx, lsy) == None) or abs(self.slope(lex, ley, lsx, lsy)) > 1.2) and ((self.slope(rex, rey, rsx, rsy) == None) or abs(self.slope(rex, rey, rsx, rsy)) > 1.2) :
            score += 30

        else :
            errors['LE'] = self.frontUp['LE']
            errors['RE'] = self.frontUp['RE']
            errors['LS'] = self.frontUp['LS']
            errors['RS'] = self.frontUp['RS']
        print('\n')
        print('Slope lew = ', self.slope(lex, ley, lwx, lwy) ) 
        print('Slope rew = ', self.slope(rex, rey, rwx, rwy) ) 
        if ((self.slope(lex, ley, lwx, lwy) == None) or abs(self.slope(lex, ley, lwx, lwy)) > 3) and ((self.slope(rex, rey, rwx, rwy) == None) or abs(self.slope(rex, rey, rwx, rwy)) > 3) :
            score += 70
        else :
            errors['LE'] = self.frontUp['LE']
            errors['RE'] = self.frontUp['RE']
            errors['LW'] = self.frontUp['LW']
            errors['RW'] = self.frontUp['RW']

        if (score < threshold) : #there must have been errors
            return {'hasErrors' : True, 'score' : score, 'points' : errors}

        return {'hasErrors' : False, 'score' : score}    
        
    #n = neck
    #h = hip
    #k = knee
    #a = ankle
    def correctSideDOWN(self, threshold = 80) :
        (nx, ny) = self.sideDown['N']
        (sx, sy) = self.sideDown['LS']
        (hx, hy) = self.sideDown['LH']
        (kx, ky) = self.sideDown['LK']
        (ax, ay) = self.sideDown['LA']   

        score = 0
        errors = dict()

        m1 = self.slope(sx, sy, hx, hy)
        m2 = self.slope(hx, hy, kx, ky)
        m3 = self.slope(kx, ky, ax, ay)
        
        # if not (isinstance(m1, int) and isinstance(m2, int) and isinstance(m3, int)) : 
        #     return {'hasErrors' : True, 'score' : 0, 'points' : {'N' : self.sideDown['N'], 'LS' : self.sideDown['LS'], 
        #     'LH' : self.sideDown['LH'], 'LK' : self.sideDown['LK'], 'LA' : self.sideDown['LA']}}
        
        print("Side Down:")
        print("slope shoulder hip:", m1)
        print("slope hip knee", m2)
        print("slope knee ankle", m3)


        if abs(m1) <= 0.18 :
            score += 20
        else :
            errors['LS'] = self.sideDown['LS']

        if abs(m2) <= 0.18 :
            score += 20
        else :
            errors['LS'] = self.sideDown['LS']

        if abs(m3) <= 0.18 :
            score += 20
        else :
            errors['LS'] = self.sideDown['LS']

        if abs(m1-m2) <= 0.1 :
            score += 20

        if abs(m2-m3) <= 0.1 :
            score += 20

        if (score < threshold) : #there must have been errors
            return {'hasErrors' : True, 'score' : score, 'points' : errors}

        return {'hasErrors' : False, 'score' : score}    

        
    
    def correctSideUP(self, threshold = 80) :

        (nx, ny) = self.sideUp['N']
        (sx, sy) = self.sideUp['LS']
        (hx, hy) = self.sideUp['LH']
        (kx, ky) = self.sideUp['LK']
        (ax, ay) = self.sideUp['LA']   

        score = 0
        errors = dict()

        m1 = self.slope(sx, sy, hx, hy)
        m2 = self.slope(hx, hy, kx, ky)
        m3 = self.slope(kx, ky, ax, ay)    

        # if not (isinstance(m1, int) and isinstance(m2, int) and isinstance(m3, int)) :
        #     return {'hasErrors' : True, 'score' : 0, 'points' : {'N' : self.sideUp['N'], 'LS' : self.sideUp['LS'], 
        #             'LH' : self.sideUp['LH'], 'LK' : self.sideUp['LK'], 'LA' : self.sideUp['LA']}}

        print("Side up:")
        print("slope shoulder hip:", m1)
        print("slope hip knee", m2)
        print("slope knee ankle", m3)

        if (math.tan(math.pi / 12)) <= abs(m1) <= (math.tan(25*math.pi/180)) : 
            score += 15
        if (math.tan(math.pi / 12)) <= abs(m2) <= (math.tan(25*math.pi/180)) : 
            score += 15
        if (math.tan(math.pi / 12)) <= abs(m3) <= (math.tan(25*math.pi/180)) : 
            score += 15

        if (not math.tan(math.pi / 12)) <= abs((m1 + m2 + m3)/3) <= (math.tan(25*math.pi/180)) :
            errors['LS'] = self.sideUp['LS']

        if abs(m1-m2) <= 0.09 :
            score += 30
        else :
            errors['LH'] = self.sideUp['LH']

        if abs(m2-m3) <= 0.09 :
            score += 25
        else :
            errors['LK'] = self.sideUp['LK']

        if (score < threshold) : #there must have been errors
            return {'hasErrors' : True, 'score' : score, 'points' : errors}

        return {'hasErrors' : False, 'score' : score}  


    def get_results(self) :
        #return (self.correctSideUP(), self.correctSideDOWN(), self.correctFrontUP(), self.correctFrontDOWN())
        return (self.correctSideUP())


    

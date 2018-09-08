import math


def dist((x1, y1), (x2, y2)) :
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def slope((x1, y1), (x2, y2)) :
    if x1 = x2 : 
        return None
    return ((y1-y2)/(x1-x2))
    
    
    
#sl = shoulder left
#el = elbow left
#hl = hand left
def correctFrontDOWN((slx, sly), (elx, ely), (hlx, hly), (srx, sry), (erx, ery), (hlx, hly), threshold = 100) :
    score = 0
    if abs(slope((elx, ely), (hlx, hly))) > 20 :
        score += 50
    if abs(slope((erx, ery), (hrx, hry))) > 20 :
        score += 50
    if (dist((slx, sly), (elx, ely)) <= (0.7)*dist((elx, ely), (hlx, hly))) :
        score += 10
    if (dist((srx, sry), (erx, ery)) <= (0.7)*dist((erx, ery), (hrx, hry))) :
        score += 10
    return (score >= threshold)
    
    
def correctFrontUP((slx, sly), (elx, ely), (hlx, hly), (srx, sry), (erx, ery), (hlx, hly), threshold = 150) :
    score = 0
    if abs(slope((elx, ely), (slx, sly))) > 80 :
        score += 50
    if abs(slope((erx, ery), (srx, sry))) > 80 :
        score += 50
    if abs(slope((elx, ely), (hlx, hly))) > 80 :
        score += 50
    if abs(slope((erx, ery), (hrx, hry))) > 80 :
        score += 50
    
    
    
#n = neck
#h = hip
#k = knee
#a = ankle
def correctSideDOWN((nx, ny), (hx, hy), (kx, ky), (ax, ay), threshold = 70) :
    m1 = slope((nx, ny), (hx, hy))
    m2 = slope(hx, hy), (kx, ky))
    m3 = slope((kx, ky), (ax, ay))
    if abs(m1) <= 0.18 :
        score += 20
    if abs(m2) <= 0.18 :
        score += 20
    if abs(m3) <= 0.18 :
        score += 20
    if abs(m1-m2) <= 0.15 :
        score += 15
    if abs(m2-m3) <= 0.15 :
        score += 15
    return score >= threshold
    

def correctSideUP((nx, ny), (hx, hy), (kx, ky), (ax, ay), threshold = 110) :
    m1 = slope((nx, ny), (hx, hy))
    m2 = slope(hx, hy), (kx, ky))
    m3 = slope((kx, ky), (ax, ay))
    if (math.tan(math.pi / 18)) <= abs(m1) <= (math.tan(25*math.pi/180)) : 
        score += 20
    if (math.tan(math.pi / 18)) <= abs(m2) <= (math.tan(25*math.pi/180)) : 
        score += 20
    if (math.tan(math.pi / 18)) <= abs(m3) <= (math.tan(25*math.pi/180)) : 
        score += 20
    if abs(m1-m2) <= 0.15 :
        score += 50
    if abs(m2-m3) <= 0.15 :
        score += 50
    return score >= threshold

    
    
    
    
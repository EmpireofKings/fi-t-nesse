class FinalResult:
    def cal_sideUp(this, error, dic={}):
        message=" "
        sol ={}
        if(error):
            message= "You need to improve your posture"
            for val in dic.keys():
                if (val == "N") :
                    sol.add ("Neck should be straighter. Try preventing rounded necks or looking down")
                elif (val =="LS") :
                    sol.add("Keep your shoulders at approxiamtely 180 degree with each other. Prevent bending")
                elif (val == "LH"):
                    sol.add("Keep your hips approximately in line with the spinal chord")
                elif (val == "LK") :
                    sol.add("Your knees should be in line with the leg. Prevent bending them/taking additional support from them")
                else :
                    sol.add("Your ankle needs to be straighter")
                
        else:
            message="You were perfect!"

        return (message, sol)

    def cal_sideDown(this,error, dic={}):
        message=" "
        sol ={}
        if(error):
            message= "Some improvement in posture/depth is needed"
            for val in dic.keys():
                if (val == "N") :
                    sol.add("Neck should be in line with your back")
                elif (val =="LS") :
                    sol.add("Keep your shoulders at approxiamtely 180 degree with each other. Prevent bending")
                elif (val == "LH"):
                    sol.add("Keep your hips approximately in line with the spinal chord")
                elif (val == "LK") :
                    sol.add("Your knees should be in line with the leg. Prevent bendinging them/taking additional support from them")
                else :
                    sol.add("Your ankle needs to be straighter")
        else:
            message= "You were perfect!"
        return (message, sol)


    def cal_frontUp(this,error, dic={}):
        sol= {}
        message= " "
        if(error):
            message= "You need some imporvement in the width between your bodyn parts/posture"
            for val in dic.keys():
                if (val == "LS") :
                    sol.add("Your left shoulder should be straighter i.e. appox 90 degree with the neck")
                elif (val =="RS") :
                    sol.add("Your right shoulder should be straighter i.e. appox 90 degree with the neck")
                elif (val == "LE"):
                    sol.add("Keep your left elbow should be approximately straight")
                elif (val == "RE") :
                    sol.add("Your knees should be in line with the leg. Prevent bendinging them/taking additional support from them")
                elif (val =="LW"):
                    sol.add("Keep your left hand directly below your left shoulder")
                else:
                    sol.add("Keep your right hand directly below your right shoulder")
        else:
            message= "You were perfect!"
        return (message,sol)



    def cal_frontDown(this,error, dic={}):
        sol= {}
        message= " "
        if(error):
            message="You need some improvement in your muscle tension"
            for val in dic.keys():
                if (val == "LS") :
                    sol.add("Your left shoulder needs to be in line with the spinal cord")
                elif (val =="RS") :
                    sol.add("Your right shoulder needs to be in line with the spinal cord")
                elif (val == "LE"):
                    sol.add("Keep your left elbow needs to be tucked in")
                elif (val == "RE") :
                    sol.add("Your right elbow needs to be tucked in")
                elif (val =="LW"):
                    sol.add("Keep your left hand directly below your left shoulder")
                else:
                    sol.add("Keep your right hand directly below your right shoulder")
        else:
            message= "You were perfect"
        return (message, sol)


    def main(this,sideUp, sideDown, frontUp, frontDown):
        if (sideUp['hasErrors']):
            res_sideUp = this.cal_sideUp(sideUp["hasErrors"], sideUp["points"])
        else:
            res_sideUp = ("", )
        if (sideDown['hasErrors']):
            res_sideDown = this.cal_sideDown(sideDown["hasErrors"], sideDown[
        "points"])
        if (frontUp['hasErrors']):
            res_frontUp = this.cal_frontUp(frontUp["hasErrors"], frontUp["points"])
        if (frontDown['hasErrors']):
            res_frontDown = this.cal_frontDown(frontDown["hasErrors"], frontDown["points"])
        
        return (res_sideUp, res_sideDown, res_frontUp, res_frontDown)

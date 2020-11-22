class ColorError(Exception):
    def __init__(self, *args, **kwargs):
        """
        A Exception for Color Class
        """
        pass
class Color():
    def __init__(self,args):
        color=args.rstrip(" ")
        self.black="#000000"

        self.white="#ffffff"

        self.orange_light="#ff915b"
        self.orange="#ff8000"
        self.orange_strong="#b35900"

        self.green_light="#80ff80"
        self.green="#80ff00"
        self.green_strong="#00ff00"
        
        self.yellow_light="#ffff80"
        self.yellow="#ffff00"
        self.yellow_strong="#d7d700"

        self.brown_light="#dd6f00"
        self.brown="#804000"
        self.brown_strong="#4a2500"

        self.grey_light="#c0c0c0"
        self.grey="#808080"
        self.grey_strong="#5e5c5c"
        
        self.blue_light="#80ffff"
        self.blue="#00ffff"
        self.blue_strong="#0080ff"

        self.red_light="#ff6f6f"
        self.red="#ff8080"
        self.red_strong="#c40000"

        self.violet_light="#800080"
        self.violet="#8000ff"
        self.violet_strong="#400080"

        self.pink_light="#ff80c0"
        self.pink="#ff80ff"
        self.pink_strong="#ff00ff"

        if "black"==color.lower() \
            \
        or "white"==color.lower() \
            \
        or "orange_light"==color.lower() \
        or "orange"==color.lower() \
        or "orange_strong"==color.lower() \
            \
        or "green_light"==color.lower() \
        or "green"==color.lower() \
        or "green_strong"==color.lower() \
            \
        or "yellow_light"==color.lower() \
        or "yellow"==color.lower() \
        or "yellow_strong"==color.lower() \
            \
        or "brown_light"==color.lower() \
        or "brown"==color.lower() \
        or "brown_strong"==color.lower() \
            \
        or "grey_light"==color.lower()\
        or "grey"==color.lower() \
        or "grey_strong"==color.lower() \
            \
        or "blue_light"==color.lower() \
        or "blue"==color.lower() \
        or "blue_strong"==color.lower() \
            \
        or "red_light"==color.lower()\
        or "red"==color.lower() \
        or "red_strong"==color.lower()\
            \
        or "violet_light"==color.lower() \
        or "violet"==color.lower() \
        or "violet_strong"==color.lower() \
            \
        or "pink_light"==color.lower()\
        or "pink"==color.lower()\
        or "pink_strong"==color.lower():
            exec("self.color=self."+args.lower())
        elif len(color)==6:
            if color[0].lower()=="f" or color[0].lower()=="a" or color[0].lower()=="b" or color[0].lower()=="c" or color[0].lower()=="d" or color[0].lower()=="e" or color[0]=="1" or color[0]=="2" or color[0]=="3" or color[0]=="4" or color[0]=="5" or color[0]=="6" or color[0]=="7" or color[1]=="8" or color[1]=="9" or color[0]=="0":
                if color[1].lower()=="f" or color[1].lower()=="a" or color[1].lower()=="b" or color[1].lower()=="c" or color[1].lower()=="d" or color[1].lower()=="e" or color[1]=="1" or color[1]=="2" or color[1]=="3" or color[1]=="4" or color[1]=="5" or color[1]=="6" or color[1]=="7" or color[1]=="8" or color[1]=="9" or color[1]=="0":
                    if color[2].lower()=="f" or color[2].lower()=="a" or color[2].lower()=="b" or color[2].lower()=="c" or color[2].lower()=="d" or color[2].lower()=="e" or color[2]=="1" or color[2]=="2" or color[2]=="3" or color[2]=="4" or color[2]=="5" or color[2]=="6" or color[2]=="7" or color[2]=="8" or color[2]=="9" or color[2]=="0":
                        if color[3].lower()=="f" or color[3].lower()=="a" or color[3].lower()=="b" or color[3].lower()=="c" or color[3].lower()=="d" or color[3].lower()=="e" or color[3]=="1" or color[3]=="2" or color[3]=="3" or color[3]=="4" or color[3]=="5" or color[3]=="6" or color[3]=="7" or color[3]=="8" or color[3]=="9" or color[3]=="0":
                            if color[4].lower()=="f" or color[4].lower()=="a" or color[4].lower()=="b" or color[4].lower()=="c" or color[4].lower()=="d" or color[4].lower()=="e" or color[4]=="1" or color[4]=="2" or color[4]=="3" or color[4]=="4" or color[4]=="5" or color[4]=="6" or color[4]=="7" or color[4]=="8" or color[4]=="9" or color[4]=="0":
                                if color[5].lower()=="f" or color[5].lower()=="a" or color[5].lower()=="b" or color[5].lower()=="c" or color[5].lower()=="d" or color[5].lower()=="e" or color[5]=="1" or color[5]=="2" or color[5]=="3" or color[5]=="4" or color[5]=="5" or color[5]=="6" or color[5]=="7" or color[5]=="8" or color[5]=="9" or color[5]=="0":
                                    self.color=args
                                else:
                                    raise ColorError("""
Unknow color: {}
                   ^""".format(color))
                            else:
                                raise ColorError("""
Unknow color: {}
                  ^""".format(color))
                        else:
                            raise ColorError("""
Unknow color: {}
                 ^""".format(color))
                    else:
                        raise ColorError("""
Unknow color: {}
                ^""".format(color))
                else:
                    raise ColorError("""
Unknow color: {}
               ^""".format(color))
            else:
                raise ColorError("""
Unknow color: {}
              ^""".format(color))
        elif len(color)==7\
        and color[0]=="#":
            if color[1].lower()=="f" or color[1].lower()=="a" or color[1].lower()=="b" or color[1].lower()=="c" or color[1].lower()=="d" or color[1].lower()=="e" or color[1]=="1" or color[1]=="2" or color[1]=="3" or color[1]=="4" or color[1]=="5" or color[1]=="6" or color[1]=="7" or color[1]=="8" or color[1]=="9" or color[1]=="0":
                if color[2].lower()=="f" or color[2].lower()=="a" or color[2].lower()=="b" or color[2].lower()=="c" or color[2].lower()=="d" or color[2].lower()=="e" or color[2]=="1" or color[2]=="2" or color[2]=="3" or color[2]=="4" or color[2]=="5" or color[2]=="6" or color[2]=="7" or color[2]=="8" or color[2]=="9" or color[2]=="0":
                    if color[3].lower()=="f" or color[3].lower()=="a" or color[3].lower()=="b" or color[3].lower()=="c" or color[3].lower()=="d" or color[3].lower()=="e" or color[3]=="1" or color[3]=="2" or color[3]=="3" or color[3]=="4" or color[3]=="5" or color[3]=="6" or color[3]=="7" or color[3]=="8" or color[3]=="9" or color[3]=="0":
                        if color[4].lower()=="f" or color[4].lower()=="a" or color[4].lower()=="b" or color[4].lower()=="c" or color[4].lower()=="d" or color[4].lower()=="e" or color[4]=="1" or color[4]=="2" or color[4]=="3" or color[4]=="4" or color[4]=="5" or color[4]=="6" or color[4]=="7" or color[4]=="8" or color[4]=="9" or color[4]=="0":
                            if color[5].lower()=="f" or color[5].lower()=="a" or color[5].lower()=="b" or color[5].lower()=="c" or color[5].lower()=="d" or color[5].lower()=="e" or color[5]=="1" or color[5]=="2" or color[5]=="3" or color[5]=="4" or color[5]=="5" or color[5]=="6" or color[5]=="7" or color[5]=="8" or color[5]=="9" or color[5]=="0":
                                if color[6].lower()=="f" or color[6].lower()=="a" or color[6].lower()=="b" or color[6].lower()=="c" or color[6].lower()=="d" or color[6].lower()=="e" or color[6]=="1" or color[6]=="2" or color[6]=="3" or color[6]=="4" or color[6]=="5" or color[6]=="6" or color[6]=="7" or color[6]=="8" or color[6]=="9" or color[6]=="0":
                                    self.color=args
                                else:
                                    raise ColorError("""
Unknow color: {}
                    ^""".format(color))
                            else:
                                raise ColorError("""
Unknow color: {}
                   ^""".format(color))
                        else:
                            raise ColorError("""
Unknow color: {}
                  ^""".format(color))
                    else:
                        raise ColorError("""
Unknow color: {}
                 ^""".format(color))
                else:
                    raise ColorError("""
Unknow color: {}
                ^""".format(color))
            else:
                raise ColorError("""
Unknow color: {}
               ^""".format(color))
    def change(self,args):
        color=args
        if "black" in color or "white" in color or "green" in color or "yellow" in color or "brown" in color or "grey" in color or "blue" in color or "red" in color or "violet" in color or "pink" in color:
            exec("self.color=self."+args)
        elif len(color)==6\
        and color[1].lower()=="f" or color[0]=="f" or color[0]=="1" or color[0]=="2" or color[0]=="3" or color[0]=="4" or color[0]=="5" or color[0]=="6" or color[0]=="7" or color[1]=="8" or color[1]=="9" or color[0]=="0"\
        and color[1].lower()=="f" or color[1]=="f" or color[1]=="1" or color[1]=="2" or color[1]=="3" or color[1]=="4" or color[1]=="5" or color[1]=="6" or color[1]=="7" or color[1]=="8" or color[1]=="9" or color[1]=="0"\
        and color[2].lower()=="f" or color[2]=="f" or color[2]=="1" or color[2]=="2" or color[2]=="3" or color[2]=="4" or color[2]=="5" or color[2]=="6" or color[2]=="7" or color[2]=="8" or color[2]=="9" or color[2]=="0"\
        and color[3].lower()=="f" or color[3]=="f" or color[3]=="1" or color[3]=="2" or color[3]=="3" or color[3]=="4" or color[3]=="5" or color[3]=="6" or color[3]=="7" or color[3]=="8" or color[3]=="9" or color[3]=="0"\
        and color[4].lower()=="f" or color[4]=="f" or color[4]=="1" or color[4]=="2" or color[4]=="3" or color[4]=="4" or color[4]=="5" or color[4]=="6" or color[4]=="7" or color[4]=="8" or color[4]=="9" or color[4]=="0"\
        and color[5].lower()=="f" or color[5]=="f" or color[5]=="1" or color[5]=="2" or color[5]=="3" or color[5]=="4" or color[5]=="5" or color[5]=="6" or color[5]=="7" or color[5]=="8" or color[5]=="9" or color[5]=="0":
            self.color=args
        elif len(color)==7\
        and color[0]=="#"\
        and color[1].lower()=="f" or color[1]=="f" or color[1]=="1" or color[1]=="2" or color[1]=="3" or color[1]=="4" or color[1]=="5" or color[1]=="6" or color[1]=="7" or color[1]=="8" or color[1]=="9" or color[1]=="0"\
        and color[2].lower()=="f" or color[2]=="f" or color[2]=="1" or color[2]=="2" or color[2]=="3" or color[2]=="4" or color[2]=="5" or color[2]=="6" or color[2]=="7" or color[2]=="8" or color[2]=="9" or color[2]=="0"\
        and color[3].lower()=="f" or color[3]=="f" or color[3]=="1" or color[3]=="2" or color[3]=="3" or color[3]=="4" or color[3]=="5" or color[3]=="6" or color[3]=="7" or color[3]=="8" or color[3]=="9" or color[3]=="0"\
        and color[4].lower()=="f" or color[4]=="f" or color[4]=="1" or color[4]=="2" or color[4]=="3" or color[4]=="4" or color[4]=="5" or color[4]=="6" or color[4]=="7" or color[4]=="8" or color[4]=="9" or color[4]=="0"\
        and color[5].lower()=="f" or color[5]=="f" or color[5]=="1" or color[5]=="2" or color[5]=="3" or color[5]=="4" or color[5]=="5" or color[5]=="6" or color[5]=="7" or color[5]=="8" or color[5]=="9" or color[5]=="0"\
        and color[6].lower()=="f" or color[6]=="f" or color[6]=="1" or color[6]=="2" or color[6]=="3" or color[6]=="4" or color[6]=="5" or color[6]=="6" or color[6]=="7" or color[6]=="8" or color[6]=="9" or color[6]=="0":
            self.color=args
        else:
            self.color="#000000"
    def get(self):
        return self.color
    def return_color_name(self):
#white and black
        if self.black==self.color.lower() or self.black=="#"+self.color:
            self.name="black"
        elif self.white==self.color.lower() or self.white=="#"+self.color:
            self.name="white"
#orange
        elif self.orange_light==self.color.lower() or self.orange_light=="#"+self.color:
            self.name="orange_light"
        elif self.orange==self.color.lower() or self.orange=="#"+self.color:
            self.name="orange"
        elif self.orange_strong==self.color.lower() or self.orange_strong=="#"+self.color:
            self.name="orange_strong"
#green
        elif self.green_light==self.color.lower() or self.green_light=="#"+self.color:
            self.name="green_light"
        elif self.green==self.color.lower() or self.green=="#"+self.color:
            self.name="green"
        elif self.green_strong==self.color.lower() or self.green_strong=="#"+self.color:
            self.name="green_strong"
#yellow
        elif self.yellow_light==self.color.lower() or self.yellow_light=="#"+self.color:
            self.name="yellow_light"
        elif self.yellow==self.color.lower() or self.yellow=="#"+self.color:
            self.name="yellow"
        elif self.yellow_strong==self.color.lower() or self.yellow_strong=="#"+self.color:
            self.name="yellow_strong"
#brown
        elif self.brown_light==self.color.lower() or self.brown_light=="#"+self.color:
            self.name="brown_light"
        elif self.brown==self.color.lower() or self.brown=="#"+self.color:
            self.name="brown"
        elif self.brown_strong==self.color.lower() or self.brown_strong=="#"+self.color:
            self.name="brown_strong"
#grey
        elif self.grey_light==self.color.lower() or self.grey_light=="#"+self.color:
            self.name="grey_light"
        elif self.grey==self.color.lower() or self.grey=="#"+self.color:
            self.name="grey"
        elif self.grey_strong==self.color.lower() or self.grey_strong=="#"+self.color:
            self.name="grey_strong"
#blue
        elif self.blue_light==self.color.lower() or self.blue_light=="#"+self.color:
            self.name="blue_light"
        elif self.blue==self.color.lower() or self.blue=="#"+self.color:
            self.name="blue"
        elif self.blue_strong==self.color.lower() or self.blue_strong=="#"+self.color:
            self.name="blue_strong"
#red
        elif self.red_light==self.color.lower() or self.red_light=="#"+self.color:
            self.name="red_light"
        elif self.red==self.color.lower() or self.red=="#"+self.color:
            self.name="red"
        elif self.red_strong==self.color.lower() or self.red_strong=="#"+self.color:
            self.name="red_strong"
#violet
        elif self.violet_light==self.color.lower() or self.violet_light=="#"+self.color:
            self.name="violet_light"
        elif self.violet==self.color.lower() or self.violet=="#"+self.color:
            self.name="violet"
        elif self.violet_strong==self.color.lower() or self.violet_strong=="#"+self.color:
            self.name="violet_strong"
#pink
        elif self.pink_light==self.color.lower() or self.pink_light=="#"+self.color:
            self.name="pink_light" 
        elif self.pink==self.color.lower() or self.pink=="#"+self.color:
            self.name="pink" 
        elif self.pink_strong==self.color.lower() or self.pink_strong=="#"+self.color:
            self.name="pink_strong" 
        else:
            self.name=self.color
        return self.name
    def invert(self):
        color=self.color
        self.colut=""
        for i in color:
            i=i.lower()
            if i=="0":
                self.colut=self.colut+"f"
            if i=="1":
                self.colut=self.colut+"e"
            if i=="2":
                self.colut=self.colut+"d"
            if i=="3":
                self.colut=self.colut+"c"
            if i=="4":
                self.colut=self.colut+"b"
            if i=="5":
                self.colut=self.colut+"a"
            if i=="6":
                self.colut=self.colut+"9"
            if i=="7":
                self.colut=self.colut+"8"
            if i=="8":
                self.colut=self.colut+"7"
            if i=="9":
                self.colut=self.colut+"6"
            if i=="f":
                self.colut=self.colut+"0"
            if i=="a":
                self.colut=self.colut+"5"
            if i=="b":
                self.colut=self.colut+"4"
            if i=="c":
                self.colut=self.colut+"3"
            if i=="d":
                self.colut=self.colut+"2"
            if i=="e":
                self.colut=self.colut+"1"
        self.color=self.colut

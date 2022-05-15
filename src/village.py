import colorama
from colorama import Back, Fore,Style
import numpy as np

class UpdateHealth:
    def __init__(self,obj):
        self.obj = obj
        
    def update(self):
        pass
    
class Wall:
    def __init__(self,arr,x,y):
        self.arr = arr
        self.x = x
        self.y = y
        self.Health = 100
        
    def createWall(self):
        if(self.Health > 0):
            for i in range(self.x, self.x+40,2):
                self.arr[self.y][i] = f"{Back.BLACK}#{Back.RESET}"
                self.arr[self.y][i+1] = f"{Back.YELLOW}#{Back.RESET}"
        else:
            for i in range(self.x, self.x+40,2):
                self.arr[self.y][i] = " "
                self.arr[self.y][i+1] = " "
    
class Canon:
    def __init__(self,arr,x,y):
        self.arr = arr
        self.x = x
        self.y = y
        self.Health = 300
        self.Damage = 2
    
    def createCanon(self):
        if(self.Health > 0):
            for i in range(self.x+4,self.x+4+int(self.Health/30)):
                if self.Health > 150:
                    self.arr[self.y-2][i] = f"{Back.GREEN} {Back.RESET}"
                elif self.Health > 60:
                    self.arr[self.y-2][i] = f"{Back.YELLOW} {Back.RESET}"
                else:
                    self.arr[self.y-2][i] = f"{Back.RED} {Back.RESET}"
                    
                    
            for i in range(self.y,self.y+8):
                for j in range(self.x,self.x+20):
                    if(i==self.y or i==self.y+7):
                        if(j==self.x or j==self.x+19):
                            self.arr[i][j] = f"{Back.BLUE}+{Back.RESET}"
                        else:
                            self.arr[i][j] = f"{Back.BLUE}-{Back.RESET}"
                    if(j==self.x or j==self.x+19):
                        if(i==self.y or i==self.y+7):
                            self.arr[i][j] = f"{Back.BLUE}+{Back.RESET}"
                        else:
                            self.arr[i][j] = f"{Back.BLUE}|{Back.RESET}"
            
            for i in range(self.x+4,self.x+17):
                self.arr[self.y+2][i] = f"{Back.BLACK}>{Back.RESET}"
                self.arr[self.y+3][i] = f"{Back.BLACK}*{Back.RESET}"
            
            self.arr[self.y+4][self.x+6] = f"{Back.BLACK}/{Back.RESET}"
            self.arr[self.y+4][self.x+7] = f"{Back.BLACK}/{Back.RESET}"
            self.arr[self.y+5][self.x+5] = f"{Back.BLACK}/{Back.RESET}"
            self.arr[self.y+5][self.x+6] = f"{Back.BLACK}/{Back.RESET}"
            
            for i in range(self.x+4,self.x+8):
                self.arr[self.y+6][i] = f"{Back.BLACK}={Back.RESET}"
        else:
            for i in range(self.x+4,self.x+4+int(self.Health/10)):
                if self.Health > 50:
                    self.arr[self.y-2][i] = " "
                elif self.Health > 20:
                    self.arr[self.y-2][i] = " "
                else:
                    self.arr[self.y-2][i] = " "
                    
                    
            for i in range(self.y,self.y+8):
                for j in range(self.x,self.x+20):
                    if(i==self.y or i==self.y+7):
                        if(j==self.x or j==self.x+19):
                            self.arr[i][j] = " "
                        else:
                            self.arr[i][j] = " "
                    if(j==self.x or j==self.x+19):
                        if(i==self.y or i==self.y+7):
                            self.arr[i][j] = " "
                        else:
                            self.arr[i][j] = " "
            
            for i in range(self.x+4,self.x+17):
                self.arr[self.y+2][i] = " "
                self.arr[self.y+3][i] = " "
            
            self.arr[self.y+4][self.x+6] = " "
            self.arr[self.y+4][self.x+7] = " "
            self.arr[self.y+5][self.x+5] = " "
            self.arr[self.y+5][self.x+6] = " "
            
            for i in range(self.x+4,self.x+8):
                self.arr[self.y+6][i] = " "
                
    def updateCanon(self):
        for i in range(self.x+4,self.x+4+int(self.Health/30)):
            if self.Health > 150:
                self.arr[self.y-2][i] = " "
            elif self.Health > 60:
                self.arr[self.y-2][i] = " "
            else:
                self.arr[self.y-2][i] = " "  
            
        for i in range(self.x+4+int(self.Health/30),self.x+14):
            self.arr[self.y-2][i] = " "  
        self.createCanon()
        
        
    def attack(self):
        pass

class Hut:
    def __init__(self,arr,x,y,color1,color2):
        self.arr = arr
        self.x = x
        self.y = y
        self.color1 = color1
        self.color2 = color2
        self.Health = 100
        
    def createHut(self):
        if(self.Health > 0):
            for i in range(self.x,self.x+int(self.Health/10)):
                if self.Health > 50:
                    self.arr[self.y-2][i] = f"{Back.GREEN} {Back.RESET}"
                elif self.Health > 20:
                    self.arr[self.y-2][i] = f"{Back.YELLOW} {Back.RESET}"
                else:
                    self.arr[self.y-2][i] = f"{Back.RED} {Back.RESET}"
                    
            self.arr[self.y][self.x] = f'{self.color1}/{Back.RESET}'
            self.arr[self.y][self.x+1] = f'{self.color1}\\{Back.RESET}'
            self.arr[self.y+1][self.x-1] = f'{self.color1}/{Back.RESET}'
            self.arr[self.y+1][self.x] = f'{self.color1}_{Back.RESET}'
            self.arr[self.y+1][self.x+1] = f'{self.color1}_{Back.RESET}'
            self.arr[self.y+1][self.x+2] = f'{self.color1}\\{Back.RESET}'
            self.arr[self.y+2][self.x-1] = f'{self.color2}|{Back.RESET}'
            self.arr[self.y+2][self.x+2] = f'{self.color2}|{Back.RESET}'
            self.arr[self.y+2][self.x] = f'{self.color2} {Back.RESET}'
            self.arr[self.y+2][self.x+1] = f'{self.color2} {Back.RESET}'
            self.arr[self.y+3][self.x-1] = f'{self.color2}|{Back.RESET}'
            self.arr[self.y+3][self.x] = f'{self.color2}_{Back.RESET}'
            self.arr[self.y+3][self.x+1] = f'{self.color2}_{Back.RESET}'
            self.arr[self.y+3][self.x+2] = f'{self.color2}|{Back.RESET}'
        else:
            for i in range(self.x,self.x+int(self.Health/10)):
                if self.Health > 50:
                    self.arr[self.y-2][i] = " "
                elif self.Health > 20:
                    self.arr[self.y-2][i] = " "
                else:
                    self.arr[self.y-2][i] = " "
                    
            self.arr[self.y][self.x] = " "
            self.arr[self.y][self.x+1] = " "
            self.arr[self.y+1][self.x-1] = " "
            self.arr[self.y+1][self.x] = " "
            self.arr[self.y+1][self.x+1] = " "
            self.arr[self.y+1][self.x+2] = " "
            self.arr[self.y+2][self.x-1] = " "
            self.arr[self.y+2][self.x+2] = " "
            self.arr[self.y+2][self.x] = " "
            self.arr[self.y+2][self.x+1] = " "
            self.arr[self.y+3][self.x-1] = " "
            self.arr[self.y+3][self.x] = " "
            self.arr[self.y+3][self.x+1] = " "
            self.arr[self.y+3][self.x+2] = " "
            
    def updateHut(self):
        for i in range(self.x,self.x+int(self.Health/10)):
            if self.Health > 50:
                self.arr[self.y-2][i] = " "
            elif self.Health > 20:
                self.arr[self.y-2][i] = " "
            else:
                self.arr[self.y-2][i] = " "
        for i in range(self.x+int(self.Health/10),self.x+10):
            self.arr[self.y-2][i] = " "
        
        self.createHut()
        

class Building:
    def __init__(self,arr,x,y,color):
        self.arr = arr
        self.x = x
        self.y = y
        self.color = color
        self.Health = 400
        
    def createBuilding(self):
        if self.Health > 0:
            for i in range(self.x,self.x+int(self.Health/40)):
                if self.Health > 200:
                    self.arr[self.y-2][i] = f"{Back.GREEN} {Back.RESET}"
                elif self.Health > 80:
                    self.arr[self.y-2][i] = f"{Back.YELLOW} {Back.RESET}"
                else:
                    self.arr[self.y-2][i] = f"{Back.RED} {Back.RESET}"
                    
            for i in range(self.y,self.y+10):
                for j in range(self.x, self.x+10):
                    if i%3==0:
                        self.arr[i][j] = f"{self.color}-{Back.RESET}"
                    if j==self.x or j==self.x+9:
                        self.arr[i][j] = f"{self.color}|{Back.RESET}"
                    elif self.arr[i][j]==" ":
                        self.arr[i][j] = f"{Back.YELLOW}*{Back.RESET}"
        else:
            for i in range(self.x,self.x+int(self.Health/10)):
                if self.Health > 50:
                    self.arr[self.y-2][i] = " "
                elif self.Health > 20:
                    self.arr[self.y-2][i] = " "
                else:
                    self.arr[self.y-2][i] = " "
                    
            for i in range(self.y,self.y+10):
                for j in range(self.x, self.x+10):
                    if i%3==0:
                        self.arr[i][j] = " "
                    if j==self.x or j==self.x+9:
                        self.arr[i][j] = " "
                    elif self.arr[i][j]==f"{Back.YELLOW}*{Back.RESET}":
                        self.arr[i][j] = " "            
                        
    def updateBuilding(self):
        for i in range(self.x,self.x+int(self.Health/40)):
            if self.Health > 200:
                self.arr[self.y-2][i] = " "
            elif self.Health > 80:
                self.arr[self.y-2][i] = " "
            else:
                self.arr[self.y-2][i] = " "
        for i in range(self.x+int(self.Health/40),self.x+10):
            self.arr[self.y-2][i] = " "
            
        self.createBuilding()

class village:
    def __init__(self):
        self.width, self.height = 203, 50
        self.display = [[" " for i in range(self.width)] for j in range(self.height)]
        
    def setBoundary(self):
        for i in range(self.height):
            for j in range(self.width):
                if(i==0 or i==self.height-1):
                    if(j==0 or j==self.width-1):
                        self.display[i][j] = Back.WHITE+"+"+Back.RESET
                    else:
                        self.display[i][j] = Back.WHITE+"-"+Back.RESET
                if(j==0 or j==self.width-1):
                    if(i==0 or i==self.height-1):
                        self.display[i][j] = Back.WHITE+"+"+Back.RESET
                    else:
                        self.display[i][j] = Back.WHITE+"|"+Back.RESET
                        
    # def townHall(self):
    #     self.rTown = [12,29]
    #     self.cTown = [80,130]
    #     s = "TOWN HALL"
    #     for i in range(100,109):
    #         self.display[13][i] = s[i-100]
            
    #     for i in range(self.rTown[0],self.rTown[1]):
    #         for j in range(self.cTown[0],self.cTown[1]):
    #             if(i==self.rTown[0] or i==self.rTown[1]-1):
    #                 if(j==self.cTown[0] or j==self.cTown[1]-1):
    #                     self.display[i][j] = f"{Back.RED}+{Back.RESET}"
    #                 else:
    #                     self.display[i][j] = f"{Back.RED}-{Back.RESET}"
    #             if(j==self.cTown[0] or j==self.cTown[1]-1):
    #                 if(i==self.rTown[0] or i==self.rTown[1]-1):
    #                     self.display[i][j] = f"{Back.RED}+{Back.RESET}"
    #                 else:
    #                     self.display[i][j] = f"{Back.RED}|{Back.RESET}"
    #             if i>23:
    #                 if(self.display[i][j] == " "):
    #                     self.display[i][j] = f"{Back.GREEN} {Back.RESET}"
                    
    def spawningPoints(self):
        pass
                    
                    
    





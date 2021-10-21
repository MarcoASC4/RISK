# Risk.py
# Marco Gonzalez
# Marco
# mgonza24
# Section 2

from graphics import *
from random import randrange

#(CLOD)
class Player:
    
    def __init__ (self, name, order, territories = 6, army=24):
        self.name = name
        self.order = order
        self.army = army
        self.territories = territories
        
    def display(self, win):
        if self.order == 1:
            resources = Text(Point(-16,15), "Territories: " + str(self.territories) + " Troops: " + str(self.army))
            resources.draw(win)
            return resources
        else:
            resources = Text(Point(-16,-18), "Territories: " + str(self.territories) + " Troops: " + str(self.army))
            resources.draw(win)
            return resources
            
    def armySize(self):
        return self.army
    
    def terrs(self):
        return self.territories
    
    def armyQ(self, num):
        self.army = self.army + num
        
    def getOrder(self):
        return self.order
#(CLOD)           
class Land:
    
    def __init__(self, rect, letter, color = "blue", troops = 0, owner = "notOwned"):
        self.rect = rect
        self.letter = letter
        self.color = color
        self.rect.setFill(color)
        self.troops = troops
        self.owner = owner
        
    def draw(self, win):
        self.rect.draw(win)
        
    def undraw(self):
        self.rect.undraw()
    
    def display(self):
        print(self.rect,self.troops, self.owner)
        
    def getTroops(self):
        return self.troops
        
    def changeColor(self, color): 
        self.color = color
        self.rect.setFill(color)
        
    def getColor(self):
        return self.color
    
    def getRect(self):
        return self.rect
    
    def getLetter(self):
        return self.letter
    
    def drawLetter(self,win):
        rect = self.rect
        point = rect.getP1()
        xVal = point.getX()
        yVal = point.getY()
        
        lette =  Text(Point(xVal +3.5,yVal +5), self.letter)
        lette.draw(win)
        
    def troopsAllocated(self,win):
        rect = self.rect
        point = rect.getP1()
        xVal = point.getX()
        yVal = point.getY()
        
       
        troop = Text(Point(xVal +2,yVal+1), "Troops: " + str(self.troops))
        troop.draw(win)
        
        return troop
        
    def assignUnits(self, num):
        self.troops = self.troops + num
        return self.troops
# Rolls Dice       
def rollDice(attk, defen):
    attkRolls = []
    defenRolls = []
    
    for a in range(attk):
        #(RND)
        roll = randrange(1,7)
        attkRolls.append(roll)
        
    for b in range(defen):
        roll = randrange(1,7)
        defenRolls.append(roll)
        
    return attkRolls, defenRolls
    
    
        
# Attack Phase        
def attack(win, playerAttk, playerDef, playerTileListOne, playerTileListTwo, playerTileLetterOne, playerTileLetterTwo, tileTxtOne, tileTxtTwo,statsOne, statsTwo):
    orda = playerAttk.getOrder()
    
    if orda == 1:
        playerNote = Text(Point(-14,6), "Purple Player Attack")
        playerNote.draw(win)
    
    elif orda == 2:
        playerAttac = Text(Point(-14,6), "Yellow Player Attack")
        playerAssign.draw(win)
    
    attackTile = Text(Point(-18, 4), "Attack Tile")
    attackTile.draw(win)
    attackLetter = Entry(Point(-18, 2), 3)
    attackLetter.draw(win)
    
    defendingTile = Text(Point(-10,4), "Defending Tile")
    defendingTile.draw(win)
    defendingLetter = Entry(Point(-10,2), 3)
    defendingLetter.draw(win)
    
    enterButton = Rectangle(Point(-15, -5), Point(-13,-4))
    enterButton.setFill("grey")
    enterButton.draw(win)
    buttonTxt = Text(Point(-14,-4.5), "Enter")
    buttonTxt.draw(win)
    
    button(win,enterButton)
    #(IEB)
    ALetter = attackLetter.getText()
    DLetter = defendingLetter.getText()
    
    while  playerTileLetterOne.count(ALetter) == 0 or playerTileLetterTwo.count(DLetter) == 0 :
        button(win,enterButton)
    
    AIndex = playerTileLetterOne.index(ALetter)
    DIndex = playerTileLetterTwo.index(DLetter)
        
    objTileOne = playerTileListOne[AIndex]
    objTileTwo = playerTileListTwo[DIndex]
        
    attkList, defenList = rollDice(3,2)
    attkList.sort(reverse=True)
    defenList.sort(reverse=True)
        
    attackPlayer = 0
    defendPlayer = 0
    for k in range(len(defenList)):
        attkVal = attkList[k]
        defenVal = defenList[k]
            
        if attkVal > defenVal:
            defendPlayer+=1
                
        elif attkVal < defenVal:
            attackPlayer+=1
                
        elif attkVal == defenVal:
            attackPlayer+=1
                
    objTileOne.assignUnits(-1*attackPlayer)
    objTileTwo.assignUnits(-1*defendPlayer)
        
    numTroopOne = objTileOne.getTroops()
    numTroopTwo = objTileTwo.getTroops()
        
    tileTxtOne[AIndex].undraw()
    tileTxtOne[AIndex].setText("Troops: " + str(numTroopOne))
    tileTxtOne[AIndex].draw(win)
        
    tileTxtTwo[DIndex].undraw()
    tileTxtTwo[DIndex].setText("Troops: " + str(numTroopTwo))
    tileTxtTwo[DIndex].draw(win)
        
    
    
    
    
# Assign Units   
def firstAssign(win, player, playerTileList,playerTileLetter):
    troopsNum = player.armySize()
    txt = []
    statsList = []
    for a in range(len(playerTileList)):
        troopsAdded = playerTileList[a].assignUnits(1)
        x = playerTileList[a].troopsAllocated(win)
        txt.append(x)
        player.armyQ(-1)
        troopsNum = player.armySize()
    stats = player.display(win)   
    
    while troopsNum != 0:
        num, letter = assignButton(win, player)
        index = playerTileLetter.index(letter)
        troopAdd = playerTileList[index].assignUnits(int(num))
        txt[index].setText("Troops: " + str(troopAdd))
        player.armyQ(-1*int(num))
        troopsNum = player.armySize()
        stats.setText("Territories: " + str(player.terrs()) + " Troops: " + str(troopsNum))
    
    return txt, stats
        
# assign and gets letter of tile and number of units    
def assignButton(win, player):
    playerAssign = Text(Point(-14,6), "Purple Player Assign Troops")
    playerAssign.draw(win)
    
    troops = Text(Point(-14, 5), "Troops")
    troops.draw(win)
    numTroops = Entry(Point(-14, 3), 3)
    numTroops.draw(win)
    
    tile = Text(Point(-14,0), "Tile")
    tile.draw(win)
    tileLetter = Entry(Point(-14,-2), 3)
    tileLetter.draw(win)
    
    enterButton = Rectangle(Point(-15, -5), Point(-13,-4))
    enterButton.setFill("grey")
    enterButton.draw(win)
    buttonTxt = Text(Point(-14,-4.5), "Enter")
    buttonTxt.draw(win)
    
    button(win,enterButton)
    
    for d in [playerAssign,troops,numTroops,tile,tileLetter,enterButton,buttonTxt]:
        d.undraw()
    #(IEB)
    num = numTroops.getText()
    rectLetter = tileLetter.getText()
    
    return num, rectLetter
    
    
    
    
# sort alpabetacally   
def sortAlph(playerOne,playerTwo):
    playerOneL = []
    playerTwoL = []
    
    for obj in playerOne:
        letter = obj.getLetter()
        playerOneL.append(letter)
        
    for obj in playerTwo:
        letter = obj.getLetter()
        playerTwoL.append(letter)
        
        
        
    return playerOneL, playerTwoL
    
#choose between random or save file
def mapChoose(win):
    randButton = Rectangle(Point(-19,7),Point(-10,10))
    randButton.setFill("grey")
    randButton.draw(win)
    
    randButtonTxt = Text(Point(-14.5,8.5), "Generate Random Map")
    randButtonTxt.draw(win)
    
    orText = Text(Point(-14, 0), "OR")
    orText.setStyle("bold")
    orText.draw(win)
    
    
    fileTxt = Text(Point(-14, -5), "Insert File Name (No '.txt')")
    fileTxt.draw(win)
    fileEntry = Entry(Point(-17,-7), 10)
    fileEntry.draw(win)
    fileButton = Rectangle(Point(-15,-7.5),Point(-13,-6.5))
    fileButton.setFill("grey")
    fileButton.draw(win)
    fileButtonTxt = Text(Point(-14,-7), "Enter")
    fileButtonTxt.draw(win)
    
    option = mapButtons(win, randButton, fileButton)
    
    for ud in [randButton,randButtonTxt,orText,fileTxt,fileEntry,fileButton,fileButtonTxt]:
        ud.undraw()
    
    if option == 1:
        playerOne, playerTwo = setRandTiles(win)
        return playerOne, playerTwo
    
    if option == 2:
        #(IEB)
        fileEntryTxt = fileEntry.getText()
        playerOne, playerTwo = setFileTiles(win, fileEntryTxt)
        
        return playerOne, playerTwo, option

    
# draws between random or file    
def mapButtons(win,randButton,fileButton):
    pointOneR = randButton.getP1()
    pointTwoR = randButton.getP2()
    xOneR, yOneR = pointOneR.getX(), pointOneR.getY()
    xTwoR, yTwoR = pointTwoR.getX(), pointTwoR.getY()
    
    pointOneF = fileButton.getP1()
    pointTwoF = fileButton.getP2()
    xOneF, yOneF = pointOneF.getX(), pointOneF.getY()
    xTwoF, yTwoF = pointTwoF.getX(), pointTwoF.getY()
    
    check = 0
    while check == 0:
        validClick = win.getMouse()
        xVal = validClick.getX()
        yVal = validClick.getY()
        
        if xVal >= xOneR and xVal <= xTwoR and yVal >= yOneR and yVal <= yTwoR:
            check = 1
            return 1
            
        if xVal >= xOneF and xVal <= xTwoF and yVal >= yOneF and yVal <= yTwoF:
            check = 2
            return 2
            
    
# sets random tiles
def setRandTiles(win):
    objTiles = []
    landTiles = []
    
    letter = 64
    for i in range(-20,20,10):
        for k in range(-8,20,7):
            points = Rectangle(Point(k,i),Point(k+7,i+10))
            letter = letter + 1
            char = chr(letter)
            rect = Land(points, char)
            p = rect.getRect()
            objTiles.append(rect)
    
    count = 0
    while len(objTiles) > 4:
        x = len(objTiles)
        for l in range(x-1, -1, -1):
            areaObj = objTiles[l]
            terrain = randrange(2)
            if count == 12:
                break
            elif terrain == 1:
                landTiles.append(areaObj)
                objTiles.pop(l)
                count+=1
    #(LOOD)   
    playerOneTiles = []
    playerTwoTiles = [] 
    
        
    p1Count = 0
    while len(landTiles) > 6:
        x = len(landTiles)
        for h in range(x-1,-1,-1):
            p1 = landTiles[h]
            pick = randrange(2)
            if p1Count == 6:
                break
            
            elif pick == 1:
                p1.changeColor("purple")
                playerOneTiles.append(p1)
                landTiles.pop(h)
                p1Count+=1
                
    for land in landTiles:
        land.changeColor("yellow")
        playerTwoTiles.append(land)
        
    for box in range(6):
        
        playerOneTiles[box].draw(win)
        playerTwoTiles[box].draw(win)
        
    for box in range(4):
        objTiles[box].draw(win)
    #(OTXT)    
    saveMap = Text(Point(-16,0), "Save Map (Leave Blank If No)")
    saveMap.draw(win)
    fileEntry = Entry(Point(-16, -1), 5)
    fileEntry.draw(win)
    
    fileButton = Rectangle(Point(-16,-3.5),Point(-14,-2.5))
    fileButton.setFill("grey")
    fileButton.draw(win)
    #(OTXT)
    fileButtonTxt = Text(Point(-15,-3), "Enter")
    fileButtonTxt.draw(win)
    
    button(win, fileButton)
    
    fileName = fileEntry.getText()
    
    if fileName == "":
        for g in [saveMap,fileEntry,fileButton,fileButtonTxt]:
            g.undraw()
        return playerOneTiles, playerTwoTiles
    
    else:
        allTile = playerOneTiles + playerTwoTiles + objTiles
        realFile = fileName + ".txt"
        #(OFL)
        outfile = open(realFile, "w")
        
        for t in range(len(allTile)):
            obj = allTile[t]
            r = obj.getRect()
            p1, p2 = r.getP1(), r.getP2()
            xOne, yOne = p1.getX(), p1.getY()
            xTwo, yTwo = p2.getX(), p2.getY()
            c = obj.getColor()
            l = obj.getLetter()
            print(str(xOne) + "," +str(yOne)+","+str(xTwo)+","+str(yTwo)+","+str(l)+","+str(c), file=outfile)
            
        for g in [saveMap,fileEntry,fileButton,fileButtonTxt]:
            g.undraw()
            
        return playerOneTiles, playerTwoTiles
    
    
        
    return playerOneTiles, playerTwoTiles
#draws tile from file                
def setFileTiles(win, entry):
    seaTiles = []
    temp = []
    playerOneTiles = []
    playerTwoTiles = []
    
    file = entry + ".txt"
    #(IFL)
    infile = open(file, "r")
    lines = infile.readlines()
    
    for f in lines:
        item = f.rstrip()
        items = item.split(",")
        xOne = float(items[0])
        yOne = float(items[1])
        xTwo = float(items[2])
        yTwo = float(items[3])
        letter = items[4]
        color = items[5]
        
        rect = Rectangle(Point(xOne,yOne),Point(xTwo,yTwo))
        area = Land(rect, letter, color)
        
        if color == "blue":
            seaTiles.append(area)
        elif color == "green":
            temp.append(area)
            
    p1Count = 0
    while len(temp) > 6:
        x = len(temp)
        for h in range(x-1,-1,-1):
            p1 = temp[h]
            pick = randrange(2)
            if p1Count == 6:
                break
            
            elif pick == 1:
                p1.changeColor("purple")
                playerOneTiles.append(p1)
                temp.pop(h)
                p1Count+=1
                
    for land in temp:
        land.changeColor("yellow")
        playerTwoTiles.append(land)
        
    for box in range(6):
        
        playerOneTiles[box].draw(win)
        playerTwoTiles[box].draw(win)
        
    for box in range(4):
        seaTiles[box].draw(win)
        
    return playerOneTiles, playerTwoTiles
            
    
    
    
        
    
 # sets uup window           
def setUpWin():
    #(GW)
    win = GraphWin("RISK", 1100, 800)
    win.setCoords(-20,-20,20,20)
    return win
# sets up startt screen
def startScreen(win):
    #(OTXT)
    title = Text(Point(0,17), "RISK")
    title.setSize(24)
    title.setStyle("bold")
    title.draw(win)
    sub = Text(Point(0, 14), "Press Enter To Start")
    sub.draw(win)
    
    start = win.getKey()
    if start == "Return":
        win.close()
# button function which only works when clicked on
def button(win,name):
    pointOne = name.getP1()
    pointTwo = name.getP2()
    xOne, yOne = pointOne.getX(), pointOne.getY()
    xTwo, yTwo = pointTwo.getX(), pointTwo.getY()
    
    check = 0
    while check == 0:
        #(IMS)
        validClick = win.getMouse()
        xVal = validClick.getX()
        yVal = validClick.getY()
        
        if xVal >= xOne and xVal <= xTwo and yVal >= yOne and yVal <= yTwo:
            check = 1
#sets up game screen
def gameScreen(win):
    playerBox = Rectangle(Point(-20,-20), Point(-8, 20))
    playerBox.draw(win)
    mapBox = Rectangle(Point(-8,-20), Point(20,20))
    mapBox.setFill("light blue")
    mapBox.draw(win)
    
    title = Text(Point(-14, 19), "RISK")
    title.draw(win)
    
    playerName = Text(Point(-16, 17), "Player 1 Name")
    playerName.draw(win)
    
    purpleCirc = Circle(Point(-12, 17), .5)
    purpleCirc.setFill("purple")
    purpleCirc.draw(win)
    
    entryOne = Entry(Point(-16,15), 10)
    entryOne.draw(win)
    
    buttonOne = Rectangle(Point(-14,14.5), Point(-12, 15.5))
    buttonOne.setFill("grey")
    buttonOne.draw(win)
    
    buttonText = Text(Point(-13, 15), "Enter")
    buttonText.draw(win)
    
    button(win, buttonOne)
    #(IEB)
    playerOne = entryOne.getText()
    playerName.setText("{0:<20}".format(playerOne))
    entryOne.undraw()
    entryOne.setText("")
    buttonOne.undraw()
    buttonText.undraw()
    
    playerNameTwo = playerName.clone()
    playerNameTwo.move(0, -33)
    playerNameTwo.setText("Player 2 Name")
    playerNameTwo.draw(win)
    
    yellowCirc = purpleCirc.clone()
    yellowCirc.move(0,-33)
    yellowCirc.setFill("yellow")
    yellowCirc.draw(win)
    
    entryTwo = entryOne.clone()
    entryTwo.move(0, -33)
    entryTwo.draw(win)
    
    buttonTwo = buttonOne.clone()
    buttonTwo.move(0, -33)
    buttonTwo.draw(win)
    
    buttonTextTwo = buttonText.clone()
    buttonTextTwo.move(0,-33)
    buttonTextTwo.draw(win)
    
    button(win, buttonTwo)
    #(IEB)
    playerTwo = entryTwo.getText()
    playerNameTwo.setText("{0:<20}".format(playerTwo))
    entryTwo.undraw()
    buttonTwo.undraw()
    buttonTextTwo.undraw()
    
    return playerOne, playerTwo
  
def main():
    #(FNC)
    startWin = setUpWin()
    startScreen(startWin)
    gameWin = setUpWin()
    nameOne, nameTwo = gameScreen(gameWin)
    playerOne = Player(nameOne, 1)
    playerTwo = Player(nameTwo, 2)
    playerOneTiles, playerTwoTiles = mapChoose(gameWin)
    
    
    
    for t in range(6):
        playerOneTiles[t].drawLetter(gameWin)
        playerTwoTiles[t].drawLetter(gameWin)
    
    
    playerOneTerr, playerTwoTerr = sortAlph(playerOneTiles,playerTwoTiles)
    tileTxtListOne, statsOne = firstAssign(gameWin,playerOne,playerOneTiles,playerOneTerr)
    tileTxtListTwo, statsTwo = firstAssign(gameWin, playerTwo,playerTwoTiles,playerTwoTerr)
    
    attack(gameWin, playerOne, playerTwo, playerOneTiles, playerTwoTiles, playerOneTerr, playerTwoTerr, tileTxtListOne, tileTxtListTwo, statsOne, statsTwo)
     
main()

template = """
         <control type="image" id="%d%d">
            <posx>%d</posx>
            <posy>%d</posy>
            <width>64</width>
            <height>64</height>
            <texture>blank.png</texture>
         </control>
         <control type="label" id="1%d%d">
            <posx>-100</posx>
            <posy>-100</posy>
            <width>6</width>
            <height>6</height>
            <label>C</label>
         </control>
         <control type="button">
            <posx>%d</posx>
            <posy>%d</posy>
            <width>64</width>
            <height>64</height>
            <onclick lang="python"><![CDATA[
turn = mc.GetActiveWindow().GetLabel(101).GetLabel()
img = 'reversiblack.png'
if turn == "Player 1":
    mc.GetActiveWindow().GetLabel(101).SetLabel("Player 2")
    img = 'reversiwhite.png'
else:
    mc.GetActiveWindow().GetLabel(101).SetLabel("Player 1")
    
mc.GetActiveWindow().GetLabel(1%d%d).SetLabel(turn)
mc.GetActiveWindow().GetImage(%d%d).SetTexture(img)

dirs = [[1,0],[1,1],[1,-1],[0,-1],[0,1],[-1,-1],[-1,1],[-1,0]]
x0 = %d
y0 = %d
for d in dirs:
    x = x0
    y = y0
    cont = True
    tu = False
    while cont:
        x += d[0]
        y += d[1]
        if x==0 or x>8 or y==0 or y>8:
            break
        id = 100+10*x+y
        t = mc.GetActiveWindow().GetLabel(id).GetLabel()
        if t == "C":
            cont = False
        if t == turn:
            tu = True
            cont = False
    if tu:
        while x != x0 or y != y0:    
            x -= d[0]
            y -= d[1]
            id = 100+10*x+y
            mc.GetActiveWindow().GetImage(id-100).SetTexture(img)
            mc.GetActiveWindow().GetLabel(id).SetLabel(turn)
            
]]></onclick>
         </control>
"""

SIZE = 8

for x in range(1, SIZE+1):
    for y in range(1, SIZE+1):
        posX = 64*(x-1)+382
        posY = 64*(y-1)+102
        print template % (x,y, posX, posY, x, y, posX, posY, x, y, x, y, x, y)
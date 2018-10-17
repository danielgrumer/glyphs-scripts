#MenuTitle: Araham | Position BottomDots Anchors in between two selected nodes
# -*- coding: utf-8 -*-
__doc__="""
Position BottomDots Anchors in between two selected nodes
"""


import math

Font = Glyphs.font
selectedLayers = Font.selectedLayers


ANCHOR1 = 'bottomDots'
ANCHOR2 = 'bottom'

def getMiddle(p1,p2):
     midX = p1 + (p2-p1)/2
     return midX

def process( thisLayer ):
	for thisPath in thisLayer.paths:
		points = [] # start to collect points
		for x in reversed( range( len( thisPath.nodes ))):
			thisNode = thisPath.nodes[x]
	
			if thisNode.selected == True:
				points.append(thisNode.x)
				points.append(thisNode.y)
# 		print points
		
		if (len(points) == 4):	# means two points			
			myX = getMiddle(points[0], points[2])
			myY = getMiddle(points[1], points[3])
		
		elif (len(points) == 2): # means one point
			myX = points[0]
			myY = points[1]
			      
		if (len(points) > 0): # then, update the whole thing
			thisLayer.anchors[ANCHOR1].position = NSPoint(myX, myY)
			thisLayer.anchors[ANCHOR2].position = NSPoint(myX, myY - 120)


	
					
for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent
	print "Processing", thisGlyph.name

	thisLayer.setDisableUpdates()
	thisGlyph.beginUndo()

	process( thisLayer )

	thisGlyph.endUndo()
	thisLayer.setEnableUpdates()



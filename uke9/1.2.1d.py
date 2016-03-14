# -*- coding: utf-8 -*-
# Gruppe 13: Morten Amundsen, Nora Krogh, Marius Fosseli, Erlend Sætre, Joakim Kilen
# Denne koden er basert på/inspirert av http://codepad.org/cywKyxXO

print """
A man has to get across a river with a chicken, a fox, and a bag of grain.
The boat can only bring the man and one of the objects at the same time.
If the man leaves the fox alone with the chicken, the fox will eat it.
If the man leaves the chicken alone with the grain, the chicken will eat it.
"""

# Solution to the problem:
#
# The man has to transport the chicken over to the right side of the river, then come back alone.
# He then has to bring the grain, and transport it to the right side.
# He must then transport the chicken back to the left side.
# Now he must transport the fox over to the right side.
# Finally, he must go back, pick up the chicken, and transport it to the right side.

# A configuration is a nested tuple: ((left,right),desc)
# left and right are sets representing the entities on each shore
# and 'desc' is a description how this configuration was reached

man,chicken,grain,fox=("man","chicken","grain","fox")
objects=(chicken,grain,fox,None)

# Define that chicken + grain alone, or fox + chicken alone results in game over.
gameover=(set((chicken,grain)), set((fox,chicken)))

# return whether an undesirable situation occurs
def lost(cfg):
    for shore in cfg[0]:
        if man not in shore:
            for forbidden in gameover:
                if shore.issuperset(forbidden):
                    return True
    return False

# return True when the end condition is reached (when all entities are on the right shore)
def done(cfg):
    left,right=cfg[0]
    return left==set()
    
# Let the man go across the river, taking an object with him.
# If 'item' is 'None', the man doesn't transport anything
# Return the new configuration, or None if the crossing can't be performed
# because the item is not on the same shore as the man.
def boat(cfg,item):
    left,right=[set(x) for x in cfg[0]] # make copies, because 'left' and 'right' will be mutated
    # determine on which shore the man is, and to which shore he will boat
    if man in left:
        src,dst=left,right
    else:
        src,dst=right,left
    # make sure that if there's an item to carry, it is on the same side as the man
    if item and not item in src:
        return None
    # Transport the man and possibly an item
    desc="--> Going right [---\ \_ man " if man in left else "<-- Going left [---\ ~~~~~~~~~~~~~~~~ \_ man "
    src.remove(man)
    dst.add(man)
    if item:
        src.remove(item)
        dst.add(item)
        desc+= "+ " +item + " _/ ~~~~~~~~~~~~~~~~ /---]"
    else:
        desc+="_/ /---]"
    return ((left,right),desc) # return the resulting configuration

# pretty-print a configuration
def printcfg(cfg,level=0):
    left,right=cfg[0]
    verdict="Game Over!" if lost(cfg) else "(Safe!)"
    print "    "*level,", ".join(left),"  ~~~  ",", ".join(right),cfg[1],verdict

# given a certain configuration, generate the configurations that could result from it
def onegeneration(cfg):
    followups=[]
    for item in objects:
        followup=boat(cfg,item)
        if not followup: continue
        followups.append(followup)
    return followups

# recursively generate from a given configuration
def generate(cfg,level=0):
    solutionstack.extend([None]*(level-len(solutionstack)+1))
    solutionstack[level]=cfg[1]
    printcfg(cfg,level)
    childs=onegeneration(cfg)
    for child in childs:
        if lost(child): # skip configurations which are not allowed
            continue
        if child[0] in previouscfgs: # skip shore configurations which have been seen before
            continue
        previouscfgs.append(child[0])
        generate(child,level+1)

# starting configuration
cfg=((set((man,chicken,grain,fox)), set()),"")

# this records any previously encountered configurations
previouscfgs=[cfg[0]]

# keep a solution stack for later printing
solutionstack=[]

# go!
print "Check what solutions are safe:"
generate(cfg)

print "\nThe solution - Step by Step:"
for step in solutionstack:
    if step:
        print "\n",step
        
print """
[chicken + grain + fox + man ---\ \_ _/ ~~~~~~~~~~~~~~~~ /---]
1. The man brings the chicken to the right side.
2. The man goes back.
3. The man brings the grain to the right side.
4. The man picks up the chicken and brings it back to the left side.
5. The man picks up the fox, and brings it to the right side.
6. The man goes back to the left side.
7. The man brings the chicken to the right side.
[---\ ~~~~~~~~~~~~~~~~ \_ _/ /--- man + chicken + fox + grain]
"""
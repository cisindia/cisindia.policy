from collective.grok import gs
from cisindia.policy import MessageFactory as _

@gs.importstep(
    name=u'cisindia.policy', 
    title=_('cisindia.policy import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('cisindia.policy.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here

class Packet:
    def __init__(self,genTime,size,bound,userId,channelCond):
        self.arrTime = genTime
        self.bound = bound
        self.boundFix = bound
        self.size = size
        self.userId = userId
        self.channelCond = channelCond
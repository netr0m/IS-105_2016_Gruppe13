class SM:
    def start(self):
        self.state = self.startState
        
    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        return o
    
    def getNextValues(self, state, inp):
        nextState = self.getNextState(self, state, inp)
        return (nextState, nextState)
    
    def transduce(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]
    
    # Hvis maskinen ikke har INN-data (settet I er tomt)
    def run(self, n = 10):
        return self.transduce([None]*n)
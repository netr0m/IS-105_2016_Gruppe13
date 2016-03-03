class SM:
    def start(self):
        self.state = self.startState
        
    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        return o
    
    def transduce(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]
    
    # Hvis maskinen ikke har INN-data (sett I er tomtm)
    def run(self, n = 10):
        return self.transduce([None]*n)
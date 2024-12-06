class State:
    def __init__(self, name, output, neighbours = [0,0] ):
        self.name = name
        self.output = output
        self.neighbours = neighbours

    def return_name(self):
        return self.name

    def return_input(self):
        return self.input

    def return_output(self):
        return self.output

    def return_neighbours(self):
        return self.neighbours

    def set_neighbours(self, nb):
        self.neighbours = nb

class Moore:
    def __init__(self, states, data):
        self.states = states
        self.data = data


    def machine(self):
        curr_state = self.states[0]
        for n in range(len(self.data)):
            next = curr_state.return_neighbours()[self.data[n]]
            print(curr_state.return_name(), " -> ", next.return_name(), "   out: ", curr_state.return_output(),"\n")
            curr_state = next



A=State("A", 0)
B=State("B", 0)
C=State("C",0)
D=State("D", 1)
A.set_neighbours([A,B])
B.set_neighbours(([C,A]))
C.set_neighbours([A,D])
D.set_neighbours([C,A])

data=[0,0,1,0,1,0,0,1,0,1,0,1]
states=[A,B,C,D]
test_machine=Moore(states,data)

test_machine.machine()
print(data)


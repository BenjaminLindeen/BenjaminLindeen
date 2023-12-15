import sat_interface

def tt1():
    '''Propositions:
        A: Amy is a truth-teller
        B: Bob is a truth-teller
        C: Cal is a truth-teller

    return a list containing all entailed propositions or negated propositions
    '''
    print("Truth-tellers and liars I")
    print("-------------------------")
    ttprob = sat_interface.KB(["~A ~B",
                               "B A",
                               "~B ~C",
                               "C B",
                               "~C ~A",
                               "~C ~B",
                               "A B C"])

    entailed = []
    if ttprob.test_literal("A") == False:
        entailed.append('~A')
        print("Amy is a liar")
    if ttprob.test_literal("~A") == False:
        entailed.append('A')
        print("Amy is a truth-teller")
    if ttprob.test_literal("B") == False:
        entailed.append('~B')
        print("Bob is a liar")
    if ttprob.test_literal("~B") == False:
        entailed.append('B')
        print("Bob is a truth-teller")
    if ttprob.test_literal("C") == False:
        entailed.append('~C')
        print("Cal is a liar")
    if ttprob.test_literal("~C") == False:
        entailed.append('C')
        print("Cal is a truth-teller")

    print("Entailed: ", entailed)
    print("-------------------------")
    return entailed

def tt2():
    '''Propositions:
        A: Amy is a truth-teller
        B: Bob is a truth-teller
        C: Cal is a truth-teller
    '''
    print("Truth-tellers and liars II")
    ttprob = sat_interface.KB(["~A C",
                               "C B",
                               "~B ~C",
                               "~B C",
                               "A C",
                               "~C B ~A"])
    entailed = []
    if ttprob.test_literal("A") == False:
        entailed.append('~A')
        print("Amy is a liar")
    if ttprob.test_literal("~A") == False:
        entailed.append('A')
        print("Amy is a truth-teller")
    if ttprob.test_literal("B") == False:
        entailed.append('~B')
        print("Bob is a liar")
    if ttprob.test_literal("~B") == False:
        entailed.append('B')
        print("Bob is a truth-teller")
    if ttprob.test_literal("C") == False:
        entailed.append('~C')
        print("Cal is a liar")
    if ttprob.test_literal("~C") == False:
        entailed.append('C')
        print("Cal is a truth-teller")

    print("Entailed: ", entailed)
    print("-------------------------")
    return entailed

def prize():
    '''Propositions:
        R: The red box is telling the truth
        G: The green box is telling the truth
        B: The blue box is telling the truth
        Rp: The prize inside the red box
        Gp: The prize inside the green box
        Bp: The prize inside the blue box
    '''
    print("Prize box")

    ttprob = sat_interface.KB(["~Rp R","~R Rp","Rp G", "~G ~Rp", "Bp B", "~B ~Bp", "~R ~G", "~B ~G", "~R ~B","~Rp ~Gp", "~Bp ~Gp", "~Rp ~Bp"])
    entailed = []

    if ttprob.test_literal("R") == False:
        entailed.append('~R')
        print("Red box is false")
    if ttprob.test_literal("~R") == False:
        entailed.append('R')
        print("Red box is the truth")
    if ttprob.test_literal("G") == False:
        entailed.append('~G')
        print("Green box is false")
    if ttprob.test_literal("~G") == False:
        entailed.append('G')
        print("Green box is the truth")
    if ttprob.test_literal("B") == False:
        entailed.append('~B')
        print("Blue box is false")
    if ttprob.test_literal("~B") == False:
        entailed.append('B')
        print("Blue box is the truth")

    if ttprob.test_literal("Rp") == False:
        entailed.append('~Rp')
        print("Red box does not have the prize")
    if ttprob.test_literal("~Rp") == False:
        entailed.append('Rp')
        print("Red box has the prize")
    if ttprob.test_literal("Gp") == False:
        entailed.append('~Gp')
        print("Green box does not have the prize")
    if ttprob.test_literal("~Gp") == False:
        entailed.append('Gp')
        print("Green box has the prize")
    if ttprob.test_literal("Bp") == False:
        entailed.append('~Bp')
        print("Blue box does not have the prize")
    if ttprob.test_literal("~Bp") == False:
        entailed.append('Bp')
        print("Blue box has the prize")

    print("Entailed: ", entailed)
    return entailed


def salt():
    '''Propositions:
        C: Caterpillar is a truth teller
        S: Cheshire Cat is a truth teller
        B: Bill the Lizard is a truth teller
        Cs: Caterpillar stole the salt
        Ss: Cat stole the salt
        Bs: Lizard stole the salt
    '''
    print("A salt and battery")
    ttprob = sat_interface.KB(["~Bs C",
                               "~C Bs",
                               "Ss S",
                               "~S ~Ss",
                               "~C B",
                               "~B C",
                               "C S B",
                               "~C ~S ~B",
                               "Ss Bs Cs",
                               "~Cs ~Ss",
                               "~Cs ~Bs",
                               "~Ss ~Bs"])
    entailed = []
    # your code here!
    if ttprob.test_literal("C") == False:
        entailed.append('~C')
        print("Caterpillar is a liar")
    if ttprob.test_literal("~C") == False:
        entailed.append('C')
        print("Caterpillar is a truth-teller")
    if ttprob.test_literal("S") == False:
        entailed.append('~S')
        print("Cat is a liar")
    if ttprob.test_literal("~S") == False:
        entailed.append('S')
        print("Cat is a truth-teller")
    if ttprob.test_literal("B") == False:
        entailed.append('~B')
        print("Bill is a liar")
    if ttprob.test_literal("~B") == False:
        entailed.append('B')
        print("Bill is a truth-teller")

    if ttprob.test_literal("Cs") == False:
        entailed.append('~Cs')
        print("Caterpillar did not steal")
    if ttprob.test_literal("~Cs") == False:
        entailed.append('Cs')
        print("Caterpillar stole the salt")
    if ttprob.test_literal("Ss") == False:
        entailed.append('~Ss')
        print("Cat did not steal")
    if ttprob.test_literal("~Ss") == False:
        entailed.append('Ss')
        print("Cat stole the salt")
    if ttprob.test_literal("Bs") == False:
        entailed.append('~Bs')
        print("Bill did not steal")
    if ttprob.test_literal("~Bs") == False:
        entailed.append('Bs')
        print("Bill stole the salt")
    print("Entailed: ", entailed)
    print("-------------------------")

    return entailed

def main():
    tt1()
    tt2()
    salt()
    prize()

if __name__ == '__main__':
    main()

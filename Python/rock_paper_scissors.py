#rock_paper_scissors game in python
def play():
    n=int(input("How many rounds should this game have?"))
    while n<1:
        print("Invalid choice")
        n=int(input("How many rounds should this game have?"))
    options=['r','rock','rocks','p','paper','papers','s','scissors','scissor']
    print("::Welcome to Rock Paper Scissors::")
    player_1=input("Enter the name of player 1: \n")
    player_2=input("Enter the name of player 2: \n")
    for i in range(n):
        choice_1=input(f"{player_1}'s turn: choose between r(rock), p(paper),s(scissors): ")
        while choice_1.lower() not in options:
            print("\n Choose between r/p/s \n")
            choice_1=input(f"{player_1}'s turn: choose between r(rock), p(paper),s(scissors): ")
        choice_2=input(f"{player_2}'s turn: choose between r(rock), p(paper),s(scissors): ")
        while choice_2.lower() not in options:
            print("\n Choose between r/p/s \n")
            choice_2=input(f"{player_2}'s turn: choose between r(rock), p(paper),s(scissors): ")
        if (choice_1[:1].lower()=='r' and choice_2[:1].lower()=='s') or (choice_1[:1].lower()=='s' and choice_2[:1].lower()=='p') or (choice_1[:1].lower()=='p' and choice_2[:1].lower()=='r'):
            print(f"{player_1} won!")
        else:
            print(f"{player_2} won!")
if __name__=='__main__':
    play()

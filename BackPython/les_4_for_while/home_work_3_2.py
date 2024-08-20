questions = ["My name ___  Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]
wright_count = 0
balls = 0
print('Hi, if ready - enter "ready"')
ready_ans = input()
if ready_ans == 'ready':
    print("Nice! Let's start!")
    for i in range(len(questions)):
        print(f'Question {i+1}:')
        print(questions[i])
        ans=input('Print an answer: ')
        if ans == answers[i]:
            wright_count += 1
            balls +=3
            print("that's wright!")
        else:
            for n in range (1,3):
                
                print(f"That's wrong! You have {3-n} attempts")
                ans = input('Enter an answer: ')
                
                if ans == answers[i]:
                    
                    print('Very well! Wright answer')
                    print(f"You've got {3-n} points")
                    balls += (3-n)
                    break
                else:
                    print("Wrong!")
            print(f"Wright answer is '{answers[i]}'")             
    print(f"Well, you've got an {wright_count} wright ansvers of {len(questions)}. It's an {wright_count/len(questions)*100} prescents of wright. Toy've got {balls} points.")            
else:
    print("Oh..( Well, good buye!")    

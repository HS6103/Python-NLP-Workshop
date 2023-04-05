# -*- coding: utf-8 -*-
# press q to quit (done)
# exception raising (done)
# other functions
    # 等差數列(done)，記憶(done)，平均
    # 圖形介面 (N/A)

def calculation():
    cnt = 0
    while True:
        try:
            if cnt !=0:
                print("Hint: Press 'm' to import answer from last operation. \n")
            ans = 0
            a = (input("Please enter a number: \n"))
            b = (input("Please enter another number: \n"))
            ops = input("Press 1 for +, 2 for -, 3 for *, 4 for /:\n")
            
            if ops not in ['1','2','3','4']:
                print("invalid operator, please try again \n")
                continue
            else:
                if a == 'm':
                    a = memory[-1]
                elif b == 'm':
                    b = memory[-1]
                    
                num_1 = int(a)
                num_2 = int(b)
                    
                if ops == '1':
                    ans = (num_1+num_2)
                elif ops == '2':
                    ans = (num_1-num_2)
                elif ops == '3':
                    ans = (num_1*num_2)
                else:
                    ans =(num_1/num_2)
                print("The answer is", ans)
                memory.append(str(ans))
                cnt += 1
                
                exit_prompt = input("Press any key to continue, or press 'r' to return to main menu: \n")
                if exit_prompt == 'r':
                    break
                else:
                    continue
    #exception_handling
        except ZeroDivisionError:
            print("The divider must not be zero \n")
            continue
        
        except ValueError:
            print("Input must be an integer \n")
            continue
            
def arith():
    while True:
        initial = int(input("Please enter your starting number: \n"))
        cd = int(input("Please enter your common difference: \n"))
        length = int(input("Please enter your your desired length: \n"))
        lst = []
        for i in range(length):
            initial += cd*i
            lst.append(initial)
        memory.append(lst)
        print("Result: ",lst, "\n")
        exit_prompt = input("Press any key to continue, or press 'r' to return to main menu: \n")
        if exit_prompt == 'r':
            break
        else:
            continue
        
def recall():
    print(memory)   


#main_program
while True:
    #initialization
    memory = []
    
    
    #function_selection(main menu)
    try:
        # if cnt == 0:
            menu_prompt = input("Hello, press 1 for simple calculation, press 2 for arithmatic progression, or press 'q' to quit \n")
            if menu_prompt == '1':
                calculation()
                continue
            elif menu_prompt == '2':
                arith()
                continue
            elif menu_prompt == 'q':
                print("Understandable, have a nice day :)")
                break
                
            
        
        
        
    # #exception_handling
    # except ZeroDivisionError:
    #     print("The divider must not be zero \n")
    #     continue
    
    # except ValueError:
    #     print("Input must be an integer \n")
    #     continue
    except IndexError:
        print("No item found in memory\n")
        continue
    

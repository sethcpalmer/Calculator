history = []
while True:
        try:
            expression = input("Enter calculation: ")
            expression = expression.replace("^", "**")
            if expression == "quit":
                break
            if expression == "history":
                if not history:
                    print("No history available.")
                else:
                    for item in history:
                        print(item)  
            if expression == "clear":
                history.clear()
                print("History cleared.")  
            if expression == "help":
                print("""
            Commands:
            help
            history
            clear
            quit
            """)        
                continue
            result = eval(expression)
            print(result)
            history.append(f"{expression} = {result}")
        except ZeroDivisionError:
            print("Cannot divide by Zero.")
        except SyntaxError:
            print("Invalid syntax.")
        except:    
            print("Invalid input")
        
    
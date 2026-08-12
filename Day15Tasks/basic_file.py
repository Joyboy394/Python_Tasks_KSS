def log_actions():
    log_file = "user_actions.log"
    
    print("User Action Logger (type 'exit' to stop)")
    
    while True:
        action = input("Enter action to log: ")
        
        if action.lower() == "exit":
            print("Logging stopped.")
            break
        
        try:
            with open(log_file, "a") as f:
                f.write(action + "\n")
            print(f"Logged: {action}")
        
        except IOError as e:
            print(f"Error writing to file: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

log_actions()

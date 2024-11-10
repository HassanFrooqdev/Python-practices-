while True:
    experience = input("What's your level? (Developer / Beginner / Quit): ").strip().lower()
    
    if experience == "developer":
        print("Python: 'Oh my goodness, welcome, fellow Developer! Let's create magic together!' 🐍✨")
    elif experience == "beginner":
        print("Python: Hahaha... I will make you cry... I mean, help you learn! 😈'")
    elif experience == "quit":
        print("Python: 'Goodbye, come back soon! 👋'")
        break
    else:
        print("Python: 'Ohh I don't recognize that level. Are you a Developer or Beginner?'")


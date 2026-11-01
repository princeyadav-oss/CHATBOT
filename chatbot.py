import tkinter as tk
from tkinter import scrolledtext, messagebox
from datetime import datetime
import webbrowser
import ast
import operator
import json
import os


# -----------------------------------
# FILES
# -----------------------------------
USER_FILE = "chatbot_users.json"


# -----------------------------------
# USER DATA FUNCTIONS
# -----------------------------------
def load_users():
    if os.path.exists(USER_FILE):
        try:
            with open(USER_FILE, "r") as file:
                return json.load(file)
        except:
            return {}
    return {}


def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)


# -----------------------------------
# LOGIN PORTAL
# -----------------------------------
class LoginPortal:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot Login Portal")
        self.root.geometry("900x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#0f172a")

        self.users = load_users()
        self.show_login_page()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # -----------------------------------
    # LOGIN PAGE
    # -----------------------------------
    def show_login_page(self):
        self.clear_window()

        left_frame = tk.Frame(self.root, bg="#020617", width=380)
        left_frame.pack(side=tk.LEFT, fill=tk.Y)
        left_frame.pack_propagate(False)

        tk.Label(
            left_frame,
            text="Smart Chatbot",
            font=("Arial", 28, "bold"),
            bg="#020617",
            fg="white"
        ).pack(pady=(120, 10))

        tk.Label(
            left_frame,
            text="Login to continue your\nreal-life AI assistant",
            font=("Arial", 14),
            bg="#020617",
            fg="#94a3b8",
            justify="center"
        ).pack(pady=10)

        tk.Label(
            left_frame,
            text="â Study Help\nâ Calculations\nâ News & Wikipedia\nâ Search Assistant\nâ Chat History Style UI",
            font=("Arial", 13),
            bg="#020617",
            fg="#38bdf8",
            justify="left"
        ).pack(pady=40)

        right_frame = tk.Frame(self.root, bg="#0f172a")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        tk.Label(
            right_frame,
            text="Already Have Account?",
            font=("Arial", 24, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack(pady=(90, 20))

        # Username Entry with placeholder
        self.login_username = tk.Entry(
            right_frame,
            font=("Arial", 14),
            width=32,
            fg="gray",
            bg="white"
        )
        self.login_username.pack(pady=10, ipady=8)
        self.login_username.insert(0, "Username")
        self.login_username.bind("<FocusIn>", self.clear_username_placeholder)
        self.login_username.bind("<FocusOut>", self.add_username_placeholder)

        # Password Entry with placeholder
        self.login_password = tk.Entry(
            right_frame,
            font=("Arial", 14),
            width=32,
            fg="gray",
            bg="white"
        )
        self.login_password.pack(pady=10, ipady=8)
        self.login_password.insert(0, "Password")
        self.login_password.bind("<FocusIn>", self.clear_password_placeholder)
        self.login_password.bind("<FocusOut>", self.add_password_placeholder)

        tk.Button(
            right_frame,
            text="Login",
            font=("Arial", 13, "bold"),
            bg="#2563eb",
            fg="white",
            width=25,
            bd=0,
            command=self.login_user
        ).pack(pady=15, ipady=6)

        tk.Button(
            right_frame,
            text="Forgot Password?",
            font=("Arial", 11),
            bg="#0f172a",
            fg="#38bdf8",
            bd=0,
            command=self.show_forgot_page
        ).pack(pady=5)

        tk.Button(
            right_frame,
            text="Create New User Account",
            font=("Arial", 12, "bold"),
            bg="#16a34a",
            fg="white",
            width=25,
            bd=0,
            command=self.show_register_page
        ).pack(pady=20, ipady=6)

    # -----------------------------------
    # PLACEHOLDER FUNCTIONS
    # -----------------------------------
    def clear_username_placeholder(self, event):
        if self.login_username.get() == "Username":
            self.login_username.delete(0, tk.END)
            self.login_username.config(fg="black")

    def add_username_placeholder(self, event):
        if self.login_username.get() == "":
            self.login_username.insert(0, "Username")
            self.login_username.config(fg="gray")

    def clear_password_placeholder(self, event):
        if self.login_password.get() == "Password":
            self.login_password.delete(0, tk.END)
            self.login_password.config(fg="black", show="*")

    def add_password_placeholder(self, event):
        if self.login_password.get() == "":
            self.login_password.config(show="")
            self.login_password.insert(0, "Password")
            self.login_password.config(fg="gray")

    # -----------------------------------
    # REGISTER PAGE
    # -----------------------------------
    def show_register_page(self):
        self.clear_window()

        frame = tk.Frame(self.root, bg="#0f172a")
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(
            frame,
            text="Create New Account",
            font=("Arial", 26, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack(pady=(50, 20))

        self.reg_name = tk.Entry(frame, font=("Arial", 14), width=35)
        self.reg_name.pack(pady=8, ipady=8)
        self.reg_name.insert(0, "Full Name")

        self.reg_username = tk.Entry(frame, font=("Arial", 14), width=35)
        self.reg_username.pack(pady=8, ipady=8)
        self.reg_username.insert(0, "Username")

        self.reg_password = tk.Entry(frame, font=("Arial", 14), width=35, show="*")
        self.reg_password.pack(pady=8, ipady=8)

        self.reg_answer = tk.Entry(frame, font=("Arial", 14), width=35)
        self.reg_answer.pack(pady=8, ipady=8)
        self.reg_answer.insert(0, "Security Answer: Favourite Color")

        tk.Button(
            frame,
            text="Register",
            font=("Arial", 13, "bold"),
            bg="#16a34a",
            fg="white",
            width=25,
            bd=0,
            command=self.register_user
        ).pack(pady=20, ipady=6)

        tk.Button(
            frame,
            text="Back to Login",
            font=("Arial", 12),
            bg="#334155",
            fg="white",
            width=20,
            bd=0,
            command=self.show_login_page
        ).pack(pady=5, ipady=5)

    # -----------------------------------
    # FORGOT PASSWORD PAGE
    # -----------------------------------
    def show_forgot_page(self):
        self.clear_window()

        frame = tk.Frame(self.root, bg="#0f172a")
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(
            frame,
            text="Forgot Password",
            font=("Arial", 26, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack(pady=(80, 20))

        tk.Label(
            frame,
            text="Enter username and your security answer",
            font=("Arial", 13),
            bg="#0f172a",
            fg="#94a3b8"
        ).pack(pady=5)

        self.forgot_username = tk.Entry(frame, font=("Arial", 14), width=35)
        self.forgot_username.pack(pady=10, ipady=8)
        self.forgot_username.insert(0, "Username")

        self.forgot_answer = tk.Entry(frame, font=("Arial", 14), width=35)
        self.forgot_answer.pack(pady=10, ipady=8)
        self.forgot_answer.insert(0, "Favourite Color")

        tk.Button(
            frame,
            text="Recover Password",
            font=("Arial", 13, "bold"),
            bg="#f59e0b",
            fg="white",
            width=25,
            bd=0,
            command=self.recover_password
        ).pack(pady=20, ipady=6)

        tk.Button(
            frame,
            text="Back to Login",
            font=("Arial", 12),
            bg="#334155",
            fg="white",
            width=20,
            bd=0,
            command=self.show_login_page
        ).pack(pady=5, ipady=5)

    # -----------------------------------
    # USER FUNCTIONS
    # -----------------------------------
    def register_user(self):
        name = self.reg_name.get().strip()
        username = self.reg_username.get().strip()
        password = self.reg_password.get().strip()
        answer = self.reg_answer.get().strip().lower()

        if (
            name == "" or username == "" or password == "" or answer == "" or
            name == "Full Name" or username == "Username" or
            answer == "security answer: favourite color"
        ):
            messagebox.showerror("Error", "Please fill all details.")
            return

        if username in self.users:
            messagebox.showerror("Error", "Username already exists.")
            return

        self.users[username] = {
            "name": name,
            "password": password,
            "security_answer": answer
        }

        save_users(self.users)
        messagebox.showinfo("Success", "Account created successfully.")
        self.show_login_page()

    def login_user(self):
        username = self.login_username.get().strip()
        password = self.login_password.get().strip()

        if username == "Username" or password == "Password" or username == "" or password == "":
            messagebox.showerror("Login Failed", "Please enter username and password.")
            return

        if username in self.users and self.users[username]["password"] == password:
            user_name = self.users[username]["name"]
            self.open_chatbot(user_name, username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def recover_password(self):
        username = self.forgot_username.get().strip()
        answer = self.forgot_answer.get().strip().lower()

        if username == "" or answer == "" or username == "Username" or answer == "favourite color":
            messagebox.showerror("Error", "Please fill all details.")
            return

        if username in self.users:
            if self.users[username]["security_answer"] == answer:
                password = self.users[username]["password"]
                messagebox.showinfo("Password Found", "Your password is: " + password)
            else:
                messagebox.showerror("Error", "Security answer is wrong.")
        else:
            messagebox.showerror("Error", "Username not found.")

    def open_chatbot(self, name, username):
        self.clear_window()
        SmartChatbotApp(self.root, name, username)


# -----------------------------------
# SMART CHATBOT APP
# -----------------------------------
class SmartChatbotApp:
    def __init__(self, root, user_name, username):
        self.root = root
        self.user_name = user_name
        self.username = username

        self.root.title("Smart Real-Life Chatbot")
        self.root.geometry("1050x700")
        self.root.resizable(False, False)
        self.root.configure(bg="#111827")

        self.create_interface()

    # -----------------------------------
    # MAIN INTERFACE
    # -----------------------------------
    def create_interface(self):
        self.sidebar = tk.Frame(self.root, bg="#050505", width=250)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.sidebar.pack_propagate(False)

        self.main_area = tk.Frame(self.root, bg="#111827")
        self.main_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.create_sidebar()
        self.create_chat_area()

    # -----------------------------------
    # SIDEBAR
    # -----------------------------------
    def create_sidebar(self):
        menu_items = [
            "â  New Chat",
            "â¥  Library",
            "â±  Projects",
            "â¦  Apps",
            "â  Explore GPTs",
            "â¯  More"
        ]

        for item in menu_items:
            if "New Chat" in item:
                command = self.new_chat
            else:
                command = self.sidebar_info

            tk.Button(
                self.sidebar,
                text=item,
                font=("Arial", 12),
                bg="#050505",
                fg="white",
                anchor="w",
                bd=0,
                padx=18,
                pady=10,
                activebackground="#1f2937",
                activeforeground="white",
                command=command
            ).pack(fill=tk.X, pady=2)

        tk.Label(
            self.sidebar,
            text="GPTs",
            font=("Arial", 11, "bold"),
            bg="#050505",
            fg="white",
            anchor="w",
            padx=18
        ).pack(fill=tk.X, pady=(25, 5))

        tk.Button(
            self.sidebar,
            text="ð¤  Basic Rule-Based Chatbot",
            font=("Arial", 11),
            bg="#2d2d2d",
            fg="white",
            anchor="w",
            bd=0,
            padx=18,
            pady=10
        ).pack(fill=tk.X, pady=3)

        tk.Label(
            self.sidebar,
            text="Recents",
            font=("Arial", 11, "bold"),
            bg="#050505",
            fg="white",
            anchor="w",
            padx=18
        ).pack(fill=tk.X, pady=(25, 5))

        recent_items = [
            "Basic Rule-Based Chatbot",
            "Study Explanation",
            "Calculation Chat",
            "Wikipedia Search"
        ]

        for item in recent_items:
            tk.Label(
                self.sidebar,
                text=item,
                font=("Arial", 10),
                bg="#050505",
                fg="#e5e7eb",
                anchor="w",
                padx=18,
                pady=6
            ).pack(fill=tk.X)

        bottom = tk.Frame(self.sidebar, bg="#050505")
        bottom.pack(side=tk.BOTTOM, fill=tk.X, pady=15)

        tk.Label(
            bottom,
            text="ð   " + self.user_name + "\n     Logged In",
            font=("Arial", 10),
            bg="#050505",
            fg="white",
            anchor="w",
            padx=15,
            justify="left"
        ).pack(fill=tk.X)

        tk.Button(
            bottom,
            text="Logout",
            font=("Arial", 10, "bold"),
            bg="#dc2626",
            fg="white",
            bd=0,
            command=self.logout
        ).pack(fill=tk.X, padx=15, pady=8)

    # -----------------------------------
    # CHAT AREA
    # -----------------------------------
    def create_chat_area(self):
        tk.Label(
            self.main_area,
            text="Smart Real-Life Chatbot",
            font=("Arial", 22, "bold"),
            bg="#111827",
            fg="white",
            pady=15
        ).pack(fill=tk.X)

        tk.Label(
            self.main_area,
            text="Ask me anything: study, calculation, news, Wikipedia, search, time and more",
            font=("Arial", 11),
            bg="#111827",
            fg="#9ca3af"
        ).pack()

        self.chat_area = scrolledtext.ScrolledText(
            self.main_area,
            wrap=tk.WORD,
            font=("Arial", 12),
            bg="#1f2937",
            fg="white",
            insertbackground="white",
            state="disabled",
            padx=12,
            pady=12
        )
        self.chat_area.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        bottom_frame = tk.Frame(self.main_area, bg="#111827")
        bottom_frame.pack(fill=tk.X, padx=20, pady=12)

        self.user_entry = tk.Entry(
            bottom_frame,
            font=("Arial", 13),
            bg="#374151",
            fg="white",
            insertbackground="white",
            width=62,
            bd=0
        )
        self.user_entry.pack(side=tk.LEFT, padx=(0, 10), ipady=12)
        self.user_entry.bind("<Return>", self.send_message)

        tk.Button(
            bottom_frame,
            text="Send",
            font=("Arial", 12, "bold"),
            bg="#10a37f",
            fg="white",
            width=10,
            bd=0,
            command=self.send_message
        ).pack(side=tk.LEFT, padx=5, ipady=5)

        tk.Button(
            bottom_frame,
            text="Clear",
            font=("Arial", 12, "bold"),
            bg="#dc2626",
            fg="white",
            width=10,
            bd=0,
            command=self.clear_chat
        ).pack(side=tk.LEFT, padx=5, ipady=5)

        self.bot_message("Hello " + self.user_name + "! I am your smart chatbot.")
        self.bot_message("Type 'help' to see all commands.")

    # -----------------------------------
    # MESSAGE DISPLAY
    # -----------------------------------
    def user_message(self, message):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, "You: " + message + "\n", "user")
        self.chat_area.config(state="disabled")
        self.chat_area.yview(tk.END)

    def bot_message(self, message):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, "Bot: " + message + "\n\n", "bot")
        self.chat_area.config(state="disabled")
        self.chat_area.yview(tk.END)

    def send_message(self, event=None):
        user_input = self.user_entry.get().strip()

        if user_input == "":
            return

        self.user_entry.delete(0, tk.END)
        self.user_message(user_input)

        response = self.get_response(user_input)
        self.bot_message(response)

    # -----------------------------------
    # BOT LOGIC
    # -----------------------------------
    def get_response(self, user_input):
        message = user_input.lower().strip()

        if message in ["hi", "hello", "hey", "hii"]:
            return "Hello " + self.user_name + "! How can I help you today?"

        elif message in ["how are you", "how are you?"]:
            return "I'm fine and ready to help you."

        elif message in ["thanks", "thank you"]:
            return "You're welcome!"

        elif message in ["bye", "exit", "quit"]:
            self.root.after(1000, self.root.destroy)
            return "Goodbye " + self.user_name + "! Have a great day."

        elif message == "help":
            return self.help_menu()

        elif message == "time":
            return "Current time is " + datetime.now().strftime("%I:%M %p")

        elif message == "date":
            return "Today's date is " + datetime.now().strftime("%d-%m-%Y")

        elif message == "day":
            return "Today is " + datetime.now().strftime("%A")

        elif message.startswith("calculate"):
            expression = user_input.replace("calculate", "", 1).strip()
            return self.calculate(expression)

        elif self.looks_like_math(message):
            return self.calculate(user_input)

        elif message.startswith("explain"):
            topic = message.replace("explain", "", 1).strip()
            return self.explain_topic(topic)

        elif message.startswith("what is"):
            topic = message.replace("what is", "", 1).strip().replace("?", "")
            return self.answer_question(topic)

        elif message.startswith("search"):
            topic = user_input.replace("search", "", 1).strip()
            return self.open_google(topic)

        elif message.startswith("google"):
            topic = user_input.replace("google", "", 1).strip()
            return self.open_google(topic)

        elif message.startswith("wikipedia"):
            topic = user_input.replace("wikipedia", "", 1).strip()
            return self.open_wikipedia(topic)

        elif message.startswith("news"):
            topic = user_input.replace("news", "", 1).strip()
            return self.open_news(topic)

        elif message.startswith("youtube"):
            topic = user_input.replace("youtube", "", 1).strip()
            return self.open_youtube(topic)

        elif "joke" in message:
            return "Why do programmers prefer dark mode? Because light attracts bugs!"

        elif "motivation" in message:
            return "Keep practicing daily. Small progress every day creates big success."

        elif "study tips" in message:
            return (
                "Study Tips:\n"
                "1. Read short notes first.\n"
                "2. Learn definitions clearly.\n"
                "3. Practice important questions.\n"
                "4. Draw diagrams where needed.\n"
                "5. Revise before sleeping."
            )

        elif "exam tips" in message:
            return (
                "Exam Tips:\n"
                "1. Write point-wise answers.\n"
                "2. Underline keywords.\n"
                "3. Attempt easy questions first.\n"
                "4. Draw neat diagrams.\n"
                "5. Manage time properly."
            )

        else:
            return (
                "I don't have a direct answer saved for this.\n"
                "You can try:\n"
                "search " + user_input + "\n"
                "wikipedia " + user_input + "\n"
                "news " + user_input
            )

    # -----------------------------------
    # HELP MENU
    # -----------------------------------
    def help_menu(self):
        return (
            "Available Commands:\n\n"
            "Chat:\n"
            "hello, how are you, thanks, bye\n\n"
            "Study:\n"
            "explain python\n"
            "explain if else\n"
            "explain loop\n"
            "explain function\n"
            "explain chatbot\n"
            "explain operating system\n"
            "explain machine learning\n\n"
            "Questions:\n"
            "what is python\n"
            "what is chatbot\n"
            "what is gui\n"
            "what is operating system\n\n"
            "Internet:\n"
            "search Python programming\n"
            "wikipedia Artificial Intelligence\n"
            "news technology\n"
            "youtube Python tutorial\n\n"
            "Tools:\n"
            "calculate 10 + 20\n"
            "time\n"
            "date\n"
            "day\n"
            "joke\n"
            "motivation\n"
            "study tips\n"
            "exam tips"
        )

    # -----------------------------------
    # CALCULATION
    # -----------------------------------
    def looks_like_math(self, message):
        symbols = ["+", "-", "*", "/", "%"]
        return any(symbol in message for symbol in symbols)

    def calculate(self, expression):
        try:
            if expression == "":
                return "Please enter calculation. Example: calculate 10 + 20"

            result = self.safe_eval(expression)
            return "Answer: " + str(result)
        except:
            return "Invalid calculation. Example: calculate 10 + 20"

    def safe_eval(self, expression):
        allowed_operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Mod: operator.mod,
            ast.Pow: operator.pow
        }

        def eval_node(node):
            if isinstance(node, ast.Num):
                return node.n

            elif isinstance(node, ast.Constant):
                if isinstance(node.value, (int, float)):
                    return node.value
                raise ValueError("Invalid value")

            elif isinstance(node, ast.BinOp):
                left = eval_node(node.left)
                right = eval_node(node.right)
                op = type(node.op)

                if op in allowed_operators:
                    return allowed_operators[op](left, right)

                raise ValueError("Invalid operator")

            elif isinstance(node, ast.UnaryOp):
                value = eval_node(node.operand)

                if isinstance(node.op, ast.USub):
                    return -value

                return value

            else:
                raise ValueError("Invalid expression")

        tree = ast.parse(expression, mode="eval")
        return eval_node(tree.body)

    # -----------------------------------
    # STUDY EXPLANATIONS
    # -----------------------------------
    def explain_topic(self, topic):
        explanations = {
            "python": "Python is a high-level programming language used in AI, ML, web development, automation and data science.",
            "if else": "If-else is a decision-making statement. If condition is true, one block runs, otherwise another block runs.",
            "loop": "Loop is used to repeat code multiple times. Python has for loop and while loop.",
            "function": "A function is a reusable block of code that runs when it is called.",
            "chatbot": "A chatbot is a software program that communicates with users and gives automatic replies.",
            "gui": "GUI means Graphical User Interface. It allows users to interact using buttons, windows and text boxes.",
            "tkinter": "Tkinter is Python's standard GUI library used to create desktop applications.",
            "operating system": "An operating system manages hardware, software, memory, files and processes.",
            "machine learning": "Machine Learning is a part of AI where computers learn from data.",
            "ai": "AI means Artificial Intelligence. It helps machines perform intelligent tasks.",
            "database": "A database is an organized collection of data.",
            "html": "HTML is used to create the structure of web pages.",
            "css": "CSS is used to design and style web pages.",
            "sql": "SQL is used to manage data in databases.",
            "input output": "Input means taking data from the user. Output means displaying result to the user.",
            "file handling": "File handling means creating, reading, writing and saving files using Python."
        }

        if topic in explanations:
            return explanations[topic]

        return self.open_google(topic)

    # -----------------------------------
    # QUESTION ANSWERS
    # -----------------------------------
    def answer_question(self, topic):
        answers = {
            "python": "Python is a popular programming language.",
            "chatbot": "A chatbot is a program that talks with users automatically.",
            "gui": "GUI stands for Graphical User Interface.",
            "tkinter": "Tkinter is Python's standard GUI library.",
            "operating system": "An operating system manages computer hardware and software.",
            "ai": "AI means Artificial Intelligence.",
            "machine learning": "Machine Learning helps computers learn from data.",
            "database": "A database stores organized data.",
            "function": "A function is a reusable block of code.",
            "loop": "A loop repeats a block of code multiple times.",
            "if else": "If-else is used for decision making in programming."
        }

        if topic in answers:
            return answers[topic]

        return self.open_google(topic)

    # -----------------------------------
    # INTERNET FUNCTIONS
    # -----------------------------------
    def open_google(self, topic):
        if topic == "":
            return "Please write something to search."

        url = "https://www.google.com/search?q=" + topic.replace(" ", "+")
        webbrowser.open(url)
        return "I opened Google search for: " + topic

    def open_wikipedia(self, topic):
        if topic == "":
            return "Please write topic. Example: wikipedia computer"

        url = "https://en.wikipedia.org/wiki/Special:Search?search=" + topic.replace(" ", "+")
        webbrowser.open(url)
        return "I opened Wikipedia for: " + topic

    def open_news(self, topic):
        if topic == "":
            topic = "latest news"

        url = "https://news.google.com/search?q=" + topic.replace(" ", "+")
        webbrowser.open(url)
        return "I opened latest news for: " + topic

    def open_youtube(self, topic):
        if topic == "":
            return "Please write topic. Example: youtube python tutorial"

        url = "https://www.youtube.com/results?search_query=" + topic.replace(" ", "+")
        webbrowser.open(url)
        return "I opened YouTube search for: " + topic

    # -----------------------------------
    # OTHER BUTTON FUNCTIONS
    # -----------------------------------
    def sidebar_info(self):
        messagebox.showinfo("Info", "This is a demo sidebar option for realistic chatbot design.")

    def clear_chat(self):
        self.chat_area.config(state="normal")
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.config(state="disabled")
        self.bot_message("New chat started. Type 'help' to see commands.")

    def new_chat(self):
        self.clear_chat()

    def logout(self):
        answer = messagebox.askyesno("Logout", "Do you want to logout?")
        if answer:
            for widget in self.root.winfo_children():
                widget.destroy()
            LoginPortal(self.root)


# -----------------------------------
# MAIN PROGRAM
# -----------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginPortal(root)
    root.mainloop()
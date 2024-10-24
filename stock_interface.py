import tkinter as tk
import joblib
import random


class QuizInterface():
    def __init__(self):
        '''
            Constructor

            Builds root window and displays initial question
            Initializes main logic loop for GUI
            Loads prediction model
        '''
        # Load model
        self.model = joblib.load('lin_reg_model.pkl')
        
        # Create GUI
        self.root = tk.Tk()
        self.root.title("Stock Quiz Interface")
        self.root.geometry("900x600")

        self.display_new_question()

        self.root.mainloop()

    def display_new_question(self):
        '''
            Clears previous question (if any) and displays new question
        '''
        for widget in self.root.winfo_children():
            widget.destroy()
        
        question_text = tk.Label(self.root, text=self.generate_question())
        question_text.pack(pady=20)

        higher_button = tk.Button(self.root, text="Higher", command=self.on_higher)
        higher_button.pack(side=tk.LEFT, padx=30, pady=30)

        lower_button = tk.Button(self.root, text="Lower", command=self.on_lower)
        lower_button.pack(side=tk.RIGHT, padx=30, pady=30)

    def generate_question(self):
        '''
            Randomly generates data for questions
        '''
        self.open = random.randint(100, 450)
        self.high = random.randint(100, 450)
        self.low = random.randint(100, 450)
        self.close = random.randint(100, 450)
        self.adj_close = random.randint(100, 450)
        self.volume = random.randint(100, 450)
        self.ndc = random.randint(100, 450)

        question_format = f'''
        Given yesterday's information, decide if today's price will be higher or lower:
        Open: {self.open},
        High: {self.high},
        Low: {self.low},
        Close: {self.close},
        Volume: {self.volume}
        '''

        return question_format
    
    def get_prediction(self):
        '''
            Passes data to model and receives prediction
        '''
        input_features = [[self.open,self.high, self.low, self.close, self.adj_close, self.volume]]
        prediction = self.model.predict(input_features)[0]
        return prediction

    def on_higher(self):
        '''
            Tests prediction against user answer "Higher"
        '''
        predicted_price = self.get_prediction()

        if predicted_price > self.close:
            result = "Correct!"
        else:
            result = "Wrong!"

        self.show_result(result)

    def on_lower(self):
        '''
            Tests prediction against user answer "Lower"
        '''
        predicted_price = self.get_prediction()

        if predicted_price < self.close:
            result = "Correct!"
        else:
            result = "Wrong!"

        self.show_result(result)

    def show_result(self, result):
        '''
            Dispalys result (i.e. if user was correct or not) in main window
        '''
        result_label = tk.Label(text=result)
        result_label.pack(pady=10)

        next_button = tk.Button(self.root, text="Next Question", command=self.display_new_question)
        next_button.pack(pady=20)




if __name__ == "__main__":
    '''
        Create root window and intialize GUI loop
    '''
    quiz = QuizInterface()
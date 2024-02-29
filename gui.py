import tkinter as tk
from tkinter import ttk, scrolledtext
from syntax_analyzer import syntax_analyzer 

class GrammarAnalyzerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Analizador gramática 11")
        self.configure(bg='gray20')
        self.initialize_ui()

    def initialize_ui(self):
        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('TButton', font=('Helvetica', 12, 'bold'), background='gray30', foreground='white')
        style.configure('TEntry', font=('Helvetica', 12), background='gray25', foreground='black')
        style.configure('TFrame', background='gray20')

        main_frame = ttk.Frame(self, padding="10 10 10 10", style='TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True)

        self.entry = ttk.Entry(main_frame, width=100, font=('Helvetica', 12))
        self.entry.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky='ew')

        self.process_button = ttk.Button(main_frame, text="Iniciar", command=self.process_input)
        self.process_button.grid(row=1, column=0, pady=10, padx=5, sticky='ew')

        exit_button = ttk.Button(main_frame, text="Salir", command=self.quit)
        exit_button.grid(row=1, column=1, pady=10, padx=5, sticky='ew')

        self.result_area = scrolledtext.ScrolledText(main_frame, height=15, width=150, wrap=tk.WORD, background='gray12', foreground='white')
        self.result_area.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky='nsew')

        main_frame.rowconfigure(2, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

    def process_input(self):
        user_input = self.entry.get()
        result = syntax_analyzer(user_input)  
        self.result_area.delete('1.0', tk.END)
        self.result_area.insert(tk.END, result)

if __name__ == "__main__":
    app = GrammarAnalyzerGUI()
    app.mainloop()

import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Calculadora")
        self.janela.configure(background='#f0f0f0')
        self.janela.geometry("300x400")

        # Variável para armazenar a expressão
        self.expressao = ""
        
        # Entry para mostrar os números
        self.entrada = tk.Entry(self.janela, width=20, font=('Arial', 18), justify='right')
        self.entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Botões
        botoes = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        # Criando e posicionando os botões
        row = 1
        col = 0
        for botao in botoes:
            cmd = lambda x=botao: self.click(x)
            tk.Button(self.janela, text=botao, width=5, height=2,
                     font=('Arial', 14), command=cmd).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Botão Clear
        tk.Button(self.janela, text='C', width=5, height=2,
                 font=('Arial', 14), command=self.clear).grid(row=5, column=0, columnspan=2)
        
    def click(self, caractere):
        if caractere == '=':
            try:
                resultado = eval(self.expressao)
                self.entrada.delete(0, tk.END)
                self.entrada.insert(0, resultado)
                self.expressao = str(resultado)
            except:
                messagebox.showerror("Erro", "Expressão inválida")
                self.clear()
        else:
            self.expressao += caractere
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, self.expressao)
    
    def clear(self):
        self.expressao = ""
        self.entrada.delete(0, tk.END)
    
    def iniciar(self):
        self.janela.mainloop()

if __name__ == '__main__':
    calc = Calculadora()
    calc.iniciar()
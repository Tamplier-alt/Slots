def offer_credit(root, balance_label, balance_ref):
    import tkinter as tk
    credit_window = tk.Toplevel(root)
    credit_window.title("Платёж")
    tk.Label(credit_window, text="Баланс недостаточен!\nВведите сумму пополнения:", font=('Arial', 14)).pack(pady=10)

    credit_entry = tk.Entry(credit_window, font=('Arial', 14), width=10, justify='center')
    credit_entry.pack(pady=5)

    def take_credit():
        try:
            credit_amount = int(credit_entry.get())
            if credit_amount >= 1:
                balance_ref[0] += credit_amount
                balance_label.config(text=f'Баланс: {balance_ref[0]}')
                credit_window.destroy()
            else:
                tk.Label(credit_window, text="Сумма должна быть ≥ 1", font=('Arial', 12), fg='red').pack()
        except ValueError:
            tk.Label(credit_window, text="Некорректный ввод", font=('Arial', 12), fg='red').pack()

    tk.Button(credit_window, text="Пополнить", font=('Arial', 12), command=take_credit).pack(pady=5)
    tk.Button(credit_window, text="Отмена", font=('Arial', 12), command=credit_window.destroy).pack(pady=5)
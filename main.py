import tkinter as tk
from config import symbols
from engine import spin, check_win
from credit import offer_credit
from ui import update_log, update_jackpot_log
import random

balance = [1000]
bet_amount = [50]
game_log = []
jackpot_attempts_log = []
attempts_since_jackpot = [0]

spin_steps = 10
spin_delay = 100
current_step = [0]
final_reels = [[]]

def play():
    if balance[0] < bet_amount[0]:
        offer_credit(root, balance_label, balance)
        return

    final_reels[0] = spin()
    current_step[0] = 0
    animate_spin()

def animate_spin():
    if current_step[0] < spin_steps:
        temp_reels = random.choices(symbols, k=5)
        result_label.config(text=' | '.join(temp_reels))
        current_step[0] += 1
        root.after(spin_delay, animate_spin)
    else:
        reels = final_reels[0]
        result = ' | '.join(reels)
        balance[0], message = check_win(reels, bet_amount[0], balance[0], attempts_since_jackpot[0], jackpot_attempts_log)

        if 'JACKPOT' in message:
            jackpot_label.config(text=f'Попыток до джекпота: {attempts_since_jackpot[0]}')
            attempts_since_jackpot[0] = 0
            update_jackpot_log(jackpot_log_text, jackpot_attempts_log)
        else:
            attempts_since_jackpot[0] += 1
            jackpot_label.config(text=f'Попыток до джекпота: {attempts_since_jackpot[0]}')

        result_label.config(text=result)
        message_label.config(text=message)
        balance_label.config(text=f'Баланс: {balance[0]}')
        if "Потеря" in message:
            msg_parts = message.replace("→ ", "").split("Потеря")
            formatted_message = f'{msg_parts[0].strip()}\nПотеря{msg_parts[1]}'
        else:
            formatted_message = message.replace("→ ", "")

        spin_number = len(game_log) + 1
        game_log.append(f'{spin_number}. {result}\n{formatted_message}')
        update_log(log_text, game_log)

def update_bet():
    try:
        new_bet = int(bet_entry.get())
        if new_bet >= 1:
            bet_amount[0] = new_bet
            bet_label.config(text=f'Ставка: {bet_amount[0]}')
        else:
            bet_label.config(text='Ставка должна быть ≥ 1')
    except ValueError:
        bet_label.config(text='Некорректная ставка')

root = tk.Tk()
root.title("Слоты")
root.configure(bg="#222")

title_label = tk.Label(root, text="ДЭПАЛКА", font=('Arial Black', 32), fg="gold", bg="#222")
title_label.pack(pady=10)

result_frame = tk.Frame(root, bg="#222")
result_frame.pack(pady=10)
result_label = tk.Label(result_frame, text='🍒 | 🍋 | 🔔 | 💎 | 7', font=('Arial', 36), fg="white", bg="#222")
result_label.pack()

message_label = tk.Label(root, text='', font=('Arial', 18), fg="lightgreen", bg="#222")
message_label.pack(pady=5)

info_frame = tk.Frame(root, bg="#222")
info_frame.pack(pady=5)

balance_label = tk.Label(info_frame, text=f'Баланс: {balance[0]}', font=('Arial', 14), fg="white", bg="#222")
balance_label.grid(row=0, column=0, padx=10)

bet_label = tk.Label(info_frame, text=f'Ставка: {bet_amount[0]}', font=('Arial', 14), fg="white", bg="#222")
bet_label.grid(row=0, column=1, padx=10)

bet_entry = tk.Entry(info_frame, font=('Arial', 14), width=6, justify='center')
bet_entry.grid(row=0, column=2, padx=5)

update_bet_button = tk.Button(info_frame, text='Обновить', font=('Arial', 12), command=update_bet, bg="#444", fg="white")
update_bet_button.grid(row=0, column=3, padx=5)

spin_button = tk.Button(root, text='Дэпнуть хату', font=('Arial', 20), command=play, bg="darkred", fg="white")
spin_button.pack(pady=10)

log_frame = tk.Frame(root, bg="#222")
log_frame.pack(pady=10)

left_log_frame = tk.Frame(log_frame, bg="#222")
left_log_frame.pack(side='left', padx=10)

log_label = tk.Label(left_log_frame, text='История спинов', font=('Arial', 12, 'bold'), fg="white", bg="#222")
log_label.pack()
log_text = tk.Text(left_log_frame, height=10, width=40, font=('Arial', 12), state='disabled', bg="#111", fg="lightgray")
log_text.pack()

right_log_frame = tk.Frame(log_frame, bg="#222")
right_log_frame.pack(side='right', padx=10)

jackpot_log_label = tk.Label(right_log_frame, text='История джекпотов', font=('Arial', 12, 'bold'), fg="white", bg="#222")
jackpot_log_label.pack()
jackpot_log_text = tk.Text(right_log_frame, height=10, width=40, font=('Arial', 12), state='disabled', bg="#111", fg="lightgray")
jackpot_log_text.pack()

jackpot_label = tk.Label(root, text='Попыток до джекпота: 0', font=('Arial', 14), fg="orange", bg="#222")
jackpot_label.pack(pady=5)

quit_button = tk.Button(root, text='Кнопка БАБЛО вывод', font=('Arial', 14), command=root.destroy, bg="#333", fg="white")
quit_button.pack(pady=10)

root.mainloop()

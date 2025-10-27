def update_log(log_text, game_log):
    log_text.config(state='normal')
    log_text.delete(1.0, 'end')
    for entry in game_log[-10:]:
        log_text.insert('end', entry + '\n')
    log_text.config(state='disabled')

def update_jackpot_log(jackpot_log_text, jackpot_attempts_log):
    jackpot_log_text.config(state='normal')
    jackpot_log_text.delete(1.0, 'end')
    for entry in jackpot_attempts_log[-10:]:
        jackpot_log_text.insert('end', entry + '\n')
    jackpot_log_text.config(state='disabled')
from config import symbols, weights, multipliers

def spin():
    import random
    return random.choices(symbols, weights=weights, k=5)

def check_win(reels, bet_amount, balance, attempts_since_jackpot, jackpot_log):
    streak = 1
    for i in range(1, len(reels)):
        if reels[i] == reels[i - 1]:
            streak += 1
        else:
            break

    if streak >= 3:
        symbol = reels[0]
        win = round(bet_amount * multipliers[symbol])
        balance += win
        if streak == 5:
            jackpot_log.append(f'🎯 Джекпот после {attempts_since_jackpot} попыток → +{win}')
            message = f'JACKPOT! Пять {symbol} подряд → Выигрыш: +{win}'
        else:
            message = f'{streak} подряд {symbol} → Выигрыш: +{win}'
    else:
        balance -= bet_amount
        message = f'Нет выигрышной линии → Потеря: -{bet_amount}'

    return balance, message

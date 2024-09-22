V = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())

pipe_one_debit = P1 * H
pipe_two_debit = P2 * H
total_debit = pipe_one_debit + pipe_two_debit

if total_debit < V:
    full_of_percent = total_debit // V * 100
    pipe_one_percent = pipe_one_debit / total_debit * 100
    pipe_two_percent = pipe_two_debit // total_debit * 100
    print(f"The pool is {full_of_percent:.2f}% full. Pipe 1: {pipe_one_percent:.2f}%. " \
                f"Pipe 2: {pipe_two_percent:.2f}%.")
else:
    print(f"For {H} hours the pool overflows with " \
               f"{total_debit - V:.2f} liters.")
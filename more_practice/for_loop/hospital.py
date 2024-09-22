DOCTORS = 7

period = int(input())

treated_patience = 0
untreated_patience = 0

for days in range(1, period + 1):
    patience = int(input())

    if days % 3 == 0 and untreated_patience > treated_patience:
        DOCTORS += 1

    if patience <= DOCTORS:
        treated_patience += patience
    else:
        treated_patience += DOCTORS
        untreated_patience += patience - DOCTORS

print(f'Treated patients: {treated_patience}.')
print(f'Untreated patients: {untreated_patience}.')

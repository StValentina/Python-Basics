cargo_amount = int(input())

van_cargo = 0
cargo_van_price = 0
truck_cargo = 0
cargo_truck_price = 0
train_cargo = 0
cargo_train_price = 0

for _ in range(1, cargo_amount + 1):
    cargo = int(input())

    if cargo <= 3:
        van_cargo += cargo
    elif 4 <= cargo <= 11:
        truck_cargo += cargo
    elif 12 <= cargo:
        train_cargo += cargo

cargo_van_price = van_cargo * 200
cargo_truck_price = truck_cargo * 175
cargo_train_price = train_cargo * 120

total_cargo = van_cargo + truck_cargo + train_cargo
total_price = cargo_van_price + cargo_truck_price + cargo_train_price

print(f'{total_price / total_cargo:.2f}')
print(f'{(van_cargo / total_cargo) * 100:.2f}%')
print(f'{(truck_cargo / total_cargo) * 100:.2f}%')
print(f'{(train_cargo / total_cargo) * 100:.2f}%')
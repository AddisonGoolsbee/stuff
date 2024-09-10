def sum_prices(filename):
    total_sum = 0.0
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    price = float(line.strip())
                    total_sum += price
                except ValueError:
                    print(f"Warning: Skipping invalid value '{line.strip()}'")
        return total_sum
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
        return None


total = sum_prices('prices.txt')

if total is not None:
    print(f"${total:.2f}, split 2 ways is ${total / 2:.2f} each.")

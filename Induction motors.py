# Induction-motors
print("Induction Motor Calculator")

f = float(input("Enter supply frequency (Hz): "))
P = int(input("Enter number of poles: "))

# Calculate synchronous speed
Ns = (120 * f) / P

print("Synchronous Speed =", Ns, "RPM")

choice = input("Do you want to enter slip percentage? (yes/no): ")

if choice.lower() == "yes":
    slip_percent = float(input("Enter slip (%): "))

    # Calculate rotor speed
    Nr = Ns * (1 - slip_percent / 100)

    print("Slip =", slip_percent, "%")
    print("Rotor Speed =", Nr, "RPM")

else:
    Nr = float(input("Enter rotor speed (RPM): "))

    # Calculate slip
    slip = ((Ns - Nr) / Ns) * 100

    print("Rotor Speed =", Nr, "RPM")
    print("Slip =", slip, "%")

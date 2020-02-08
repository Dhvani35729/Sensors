# https: // www.mouser.ca/Embedded-Solutions/Computing/Single-Board-Computers/_/N-aez3t

# Min Supply Voltage: 1.8V
# 10

# Min Supply Voltage: 3V
# 6

# Min Supply Voltage: 3.3V
# 151

# Min Supply Voltage: 3.7V
# 4

# Min Supply Voltage: 5V
# 223

# Min Supply Voltage: 5.5V
# 2

# Min Supply Voltage: 7V
# 4

# Min Supply Voltage: 7.5V
# 2

# Min Supply Voltage: 8V
# 3

# Min Supply Voltage: 9V
# 56

# Min Supply Voltage: 12V
# 530

# Min Supply Voltage: 15V
# 1

# Min Supply Voltage: 19V
# 3

# Min Supply Voltage: 24V
# 3

# Min Supply Voltage: 25V
# 2

# Min Supply Voltage: 30V
# 4

# Min Supply Voltage: 36V
# 1

total = 10+6+151+4+223+2+4+2+3+56+530+1+3+3+2+4+1
min_vol_total = (10*1.8) + (6*3) + (151*3.3) + (4*3.7) + (223*5) + \
    (2*5.5) + (4*7) + (2*7.5) + (3*8) + (56*9) + (530*12) + \
    (1*15) + (3*19) + (3*24) + (2*25) + (4*30) + (1*36)

avg = min_vol_total / total
print(avg)

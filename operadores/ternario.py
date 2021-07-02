lockdown = True  # Fique em casa haha
grana = 30

status = 'Em casa' if lockdown or grana <= 100 else 'Uhuuu'

print(status)
print(f'O status é: {status}')

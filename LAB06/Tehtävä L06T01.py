import datetime

sekunnit = int(input("Syötä sekunnit: "))

tunnit = sekunnit // 3600
minuutit = (sekunnit % 3600) // 60
loput_sekunnit = sekunnit % 60
print(f"{tunnit:02d}:{minuutit:02d}:{loput_sekunnit:02d}")

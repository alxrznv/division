def division(dm, dt):
    ct = 0
    temp = 1
    if dm < dt:
        return 0
    else:
        while dt <= dm:
            dt = dt << 1
            temp = temp << 1

        while temp > 1:
            dt = dt >> 1
            temp = temp >> 1
            if dm >= dt:
                dm = dm - dt
                ct |= temp

        return ct


dm = int(input("Введите делимое: "))
dt = int(input("Введите делитель: "))
ct = division(dm, dt)
print("Частное:", ct)
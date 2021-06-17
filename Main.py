from Device import Device
def addDevice():
    devices = []

    adding = True

    while adding:
        name = input("Insert device's name")
        power = input("Insert device's power consumption")
        amount = input("Insert amount of same-type devices")
        avgUse = input("Insert device's average daily usage in hours")


        devices.append(Device(name, power, amount, avgUse))

        nextDev = input("Would you like to add another device? Y/N").upper()

        if not nextDev == 'Y':
            adding = False

    return devices

def Main():

    devices = addDevice()
    totalUsage = 0

    output = int(input("1. Daily usage\n"
                   "2. Monthly usage\n"
                   "3. Yearly Usage\n"
                   "4. Add another device"))

    for d in devices:
        print(d)

    if output == 1:
        for d in devices:
            usage = d.dailyUse()
            print(f'{d.name}: {usage}kWh')
            totalUsage += usage
        print(f'Totale usage: {totalUsage}kWh')
    if output == 2:
        for d in devices:
            usage = d.monthlyUse()
            print(f'{d.name}: {usage}kWh')
            totalUsage += usage
        print(f'Totale usage: {totalUsage}kWh')
    if output == 3:
        for d in devices:
            usage = d.yearlyUse()
            print(f'{d.name}: {usage}kWh')
            totalUsage += usage
        print(f'Totale usage: {totalUsage}kWh')


if __name__ == '__main__':
    Main()

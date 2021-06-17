class Device:
    """Device class description

    Inputs:
        Device name
        Power in watts
        Amount of same-type devices
        AvgUse average daily usage in hours

    Methods:
        dailyUse returns daily power consumption by device in kWh
        monthlyUSe returns monthly power consumption by device in kWh
        yearlyUse returns yearly power consumption by device in kWh


   """

    __slots__ = ['name', 'power', 'amount', 'avgUse']

    def __init__(self, name: str, power, amount, avgUse):
        self.name = name
        self.power = int(power)
        self.amount = int(amount)
        self.avgUse = float(avgUse)

    def dailyUse(self):
        return ((self.power * self.avgUse)/1000) * self.amount

    def monthlyUse(self):
        return 30 * (self.dailyUse())

    def yearlyUse(self):
        return 365 * (self.dailyUse())

    def __str__(self):
        return self.name

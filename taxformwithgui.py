from breezypythongui import EasyFrame

class TaxCalculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Tax Calculator")
        self.setResizable(False)

        self.addLabel(text="Gross income", row=0, column=0)
        self.incomeField = self.addFloatField(value=0.0, row=0, column=1, width=15)

        self.addLabel(text="Dependents", row=1, column=0)
        self.dependentField = self.addIntegerField(value=0, row=1, column=1, width=5)

        self.addButton(text="Compute", row=2, column=0, columnspan=2, command=self.computeTax)

        self.addLabel(text="Total tax", row=3, column=0)
        self.taxField = self.addFloatField(value=0.0, row=3, column=1, width=15, precision=2, state="readonly")

    def computeTax(self):
        income = self.incomeField.getNumber()
        dependents = self.dependentField.getNumber()

        baseDeduction = 500
        taxRate = 0.10 #change to 10% for fun

        taxableIncome = max(0.0, income - (baseDeduction * dependents))
        totalTax = taxableIncome * taxRate

        self.taxField.setNumber(totalTax)

def main():
    TaxCalculator().mainloop()

if __name__ == "__main__":
    main()

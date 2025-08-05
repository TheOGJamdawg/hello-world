from breezypythongui import EasyFrame

class TemperatureConverter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Temperature Converter")
        self.setResizable(False)

        self.addLabel(text="Fahrenheit", row=0, column=0)
        self.addLabel(text="Celsius", row=0, column=1)

        self.fahrField = self.addFloatField(value = 32.0,
                                                row = 1,
                                                column = 0,
                                                width = 10,
                                                precision = 2)
        self.celsiusField = self.addFloatField(value = 0.0,
                                                row = 1,
                                                column = 1,
                                                width = 10,
                                                precision = 2)

        self.addButton(text=">>>>",
                       row = 2,
                       column = 0,
                       command = self.convertToCelsius) # press button to convert to Celcius
        self.addButton(text="<<<<",
                       row = 2,
                       column = 1,
                       command = self.convertToFahrenheit) # press button to convert to Fahrenheit

    def convertToCelsius(self):
        fahr = self.fahrField.getNumber()
        celsius = (fahr - 32) * 5 / 9
        self.celsiusField.setNumber(round(celsius, 2))

    def convertToFahrenheit(self):
        celsius = self.celsiusField.getNumber()
        fahr = (celsius * 9 / 5) + 32
        self.fahrField.setNumber(round(fahr, 2))

def main():
    TemperatureConverter().mainloop()

if __name__ == "__main__":
    main()

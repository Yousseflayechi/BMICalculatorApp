# BMI Calculator App

The BMI Calculator App is a simple graphical user interface (GUI) application developed using the Python `tkinter` library. This app allows users to calculate their Body Mass Index (BMI) based on their weight in kilograms and height in meters.

## Features

- **User-Friendly Interface**: The app provides a user-friendly interface with labeled input fields and a "Calculate your BMI" button.

- **BMI Calculation**: Users can input their weight in kilograms and height in meters, and the app calculates their BMI using the formula: `BMI = weight / (height^2)`. The result is displayed in a text box on the interface.

- **BMI Categories**: The calculated BMI is categorized into different ranges:
  - If BMI is less than or equal to 18.5, the user is categorized as "underweight."
  - If BMI is between 18.5 and 24.9 (inclusive), the user is categorized as "normal."
  - If BMI is between 25 and 39.9 (inclusive), the user is categorized as "overweight."
  - If BMI is greater than or equal to 40, the user is categorized as "obese."

- **Immediate Feedback**: The app provides immediate feedback to the user by displaying both the calculated BMI and the corresponding category.

## How to Use

1. Launch the BMI Calculator App.

2. Enter your weight in kilograms in the "Your weight in kg" input field.

3. Enter your height in meters in the "Your height in m" input field.

4. Click the "Calculate your BMI" button.

5. The calculated BMI and your BMI category will be displayed in the text box below.

## Requirements

- Python 3.x
- The `tkinter` library is required, which is included in most standard Python installations.

## Usage

1. Clone this repository to your local machine.

2. Run the `bmi_calculator.py` script using Python.

3. Follow the on-screen instructions to input your weight and height.

4. View your calculated BMI and category on the application interface.

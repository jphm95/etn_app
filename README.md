
# ETN app Android. Test Automation Project

## Overview

This project focuses on automating the testing of the ETN (Enlaces Terrestres Nacionales a mexican bus company) Android application using Appium and Python in PyCharm. The automation suite is designed to validate key functionalities of the app, ensuring a smooth user experience.

## Features

- **Automated Testing**: Simulates user interactions within the ETN mobile application, covering ticket booking and route selection.


## Technologies Used

- **Python**: The primary programming language used for automation scripts.
- **Appium**: Framework for automating mobile applications.
- **PyCharm**: Integrated Development Environment (IDE) for Python development.
- **Android Studio**: Used for setting up the Android emulator.
.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/jphm95/etn_app_android.git

2. Navigate to the project directory:
   ```bash
   cd etn_app_android

3. Open the project in PyCharm or your preferred IDE.
   Ensure all necessary dependencies are installed. You can use pip to install required packages:
   ```bash
   pip install Appium-Python-Client

4. Set up the Android emulator in Android Studio and configure the desired capabilities in your Appium scripts.

5. Run Appium Server (https://appium.io/docs/en/latest/quickstart/)
   
6. Run the tests using your preferred method in PyCharm.
   
## Challenges and Solutions

- Dynamic Elements: Handled dynamic UI components by implementing explicit waits to ensure elements are interactable during tests.

- Emulator Performance: Optimized emulator settings for smoother test execution, reducing lag and improving reliability.

- User actions: Doing scroll and interact with some elements.

## Future Work

- Test Assertions.
- Expand the test suite to cover more functionalities of the ETN app.
- Integrate continuous integration/continuous deployment (CI/CD) for automated testing on code changes.
- Enhance reporting features for better insights into test results.   
- Test for IOS Version

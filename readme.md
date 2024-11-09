# Download and install Microsoft Visual Studio Code

https://code.visualstudio.com/

# Download and install Python

https://www.python.org/downloads/windows/

# Download and install Java

https://www.java.com/download/ie_manual.jsp

# Install Dependencies

pip install -r requirements.txt

# Install Playwright Drivers

playwright install

# Install Extensions

Get-Content extensions.txt | ForEach-Object { code --install-extension $_ }

# To run the test suite

behave -D ENV=staging

# To create allure report

allure\bin\allure generate --single-file --clean --name "Test Report"

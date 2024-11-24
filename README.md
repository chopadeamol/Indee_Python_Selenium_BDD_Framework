# Indee_Python_Selenium_BDD_Framework
    
    I have used the following command to run a specific file and generate report in the mentioned directory
    behave features/login.feature -f html-pretty -o reports/allure-results/behave-report.html

    1. behave --tags @smoke:
            This will run all features or scenarios with the @smoke tag.

    2. behave --tags ~@smoke 
            This will exclude a tag based test

    3. behave features/login.feature
            If your .feature file is named login.feature and located in the features folder, you can run it directly by specifying the file path
    
    4. behave --tags @smoke --dry-run
            Dry Run: Use the --dry-run flag to verify which scenarios will run without actually executing them
    
    5. behave features/login.feature --tags @smoke
        To run only tests with a certain tag in a specific file
    
    6. behave features/login.feature:10
        Run a Specific Scenario by Line Number
        If the test file contains multiple scenarios and you want to run one specific scenario, specify the line number where the scenario starts
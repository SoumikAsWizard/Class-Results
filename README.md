This program helps teachers quickly analyze student performance from CSV files.
It shows which students are doing good (Grades A & B) and calculates both class-wise and overall performance.
It also generates a summary_report.csv file with the results.

📂 1. Preparing the CSV Files

Each teacher should feed the CSV file for their class.
The CSV must have exactly two columns:

Name,Grade
Aarav,A
Ishita,B
Rohan,C
Meera,A
Kabir,B
Ananya,A
Sahil,D
Priya,B
Dev,F
Riya,A


Name → Student’s name

Grade → Student’s average grade (A, B, C, D, or F)

Save the file as classA.csv, classB.csv, etc.


⚙️ 2. Running the Program

Make sure Python and pandas library are installed:

pip install pandas


Save the script as analyze_students.py.

Run the program from terminal/command prompt:

python analyze_students.py


When asked, enter one or more CSV filenames separated by spaces:

Enter CSV filenames separated by spaces (e.g., classA.csv classB.csv classC.csv): classA.csv classB.csv classC.csv

📑 4. Summary Report

After running, a file called summary_report.csv will be created in the same folder.
It contains class-wise and overall statistics, like this:

Class,Total Students,Good Students (A & B),Percentage Good
classA.csv,10,7,70.0
classB.csv,5,3,60.0
classC.csv,6,4,66.67
Overall,21,14,66.67


Teachers can open this file in Excel, Google Sheets, or any CSV reader.

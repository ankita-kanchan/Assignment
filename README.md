# Club house Hash Table Assignment using Python.
In this Problem, you have to write an application in Python 3.7 that keeps track of club members
and their details.
A newly opened club house is inviting guests to register into their membership program. They have
received a lot of entries and need help retrieving details of their applicants quickly. In order to do this,
they need your help in designing a system that can quickly save and find the applicant details based
on the applicant’s name. The details that need to be included are:

1. Applicant Name
2. Phone Number
3. Member reference
4. Application status


The club house would like to use the system to provide the following functionality
1. Add names of applicants and other details into the system
2. Find and update applicant details based on applicant’s name
3. Generate a list of applicants who have been referred by a particular member
4. Generate a report on the number of applications in the various stages of processing (Applied,
Verified, Approved)

Design a hash table, which uses applicant’s name as the key to hash elements into the hash
table. Generate necessary hash table definitions needed and provide a design document (1 page)
detailing clearly the design and the details of considerations while making this design and the reasons
for the specific choice of hash function.
Design a hash function HashId() which accepts the applicant’s name as a parameter and returns
the hash value.Create / populate the hash table from the list of applicant names and the corresponding details
given in the input file.
Operations:
1. def initializeHash(self): This function creates an empty hash table and points to null.

2. def insertAppDetails(ApplicationRecords, name, phone, memRef, status): This function
inserts the applicant’s name and corresponding details into the hash table. The inputs need
to be read from a file inputPS26.txt which contains the all the applicant details. The file read
can happen outside the function and only the information in every individual row needs to be
passed to the function. Each applicant’s details should be recorded in one row separated by
a slash (“/”) as shown below.
Sample inputPS26.txt file entries
Aravind Shetty / 9988112311 / 11321 / Applied
Deepak Prasad / 9923212234 / / Applied
Sandhya Raman / 9213231311 / 11129 / Verified
Joginder Singh / 8234219326 / 21299 / Applied
Vinay Shah / 9912356788 / 11129 / Approved
…..
After successfully inserting the applicant details, a summary of the insert status should be
output to the file outputPS26.txt in the below format.
Successfully inserted xx applications into the system.
Where xx is the number of applications.

3. def updateAppDetails(ApplicationRecords, name, phone, memRef, status): This
function finds the applicant’s details based on the name and updates the corresponding
details into the hash table. The inputs need to be read from a file promptsPS26.txt which
contains the below tag to indicate an update.
Update: Deepak Prasad / 9923212234 / / Verified
After the update is done, the update summary should be sent to the outputPS26.txt file in the
below format.
Updated details of xxxxxxxxxx. Yyyy has been changed.
Where xxxx is the Name of the applicant and yyyy is the field(s) that has/have been updated.

4. def memRef(ApplicationRecords, memID): This function prints the list of all applicants who
have been referred by a particular member. The member number can be read from the file
promptsPS26.txt. The input can be identified with the tag mentioned below
memberRef: 11129
The list of applicants should be output in a file outputPS26.txt and should contain the
applicant’s details including name, phone number and application status.
Output format:
---------- Member reference by 11129 ----------
Sandhya Raman / 9213231311 / Verified
Vinay Shah / 9912356788 / Approved


5. def appStatus(ApplicationRecords): This function prints the list of number of applications
in each stage of the application process including Applied, Verified and Approved. This
function is triggered when the below tag is encountered in the promptsPS26.txt file. The input
can be identified with the tag mentioned below
appStatus
This list should be output to outputPS26.txt that contains the number of applications in each
status.
Output format:
---------- Application Status ----------
Applied: 3
Verified: 1
Approved: 1

6. def destroyHash(ApplicationRecords): This function destroys all the entries inside hash
table. This is a clean-up code.

7. Include all other functions that are required to support these basic mandatory functions.

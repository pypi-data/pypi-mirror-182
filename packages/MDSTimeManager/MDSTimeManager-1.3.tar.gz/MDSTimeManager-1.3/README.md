#Build Stamp
[![Build Status](https://app.travis-ci.com/a-foote/MDS_TimeManager.svg?branch=main)](https://app.travis-ci.com/a-foote/MDS_TimeManager)

# MDS_TimeManager

This package that can help UBC Master of Data Science (MDS) students manage their time. A student can view the upcoming deliverables 
(Quizzes, Labs/Assignments, Projects) or get recommendations on study time for each course over the next 7 days.

## Sub-package 1 - setup

### Module 1: course.py

This module will have classes for entities Course, Deliverable, Quiz, Assignment and Lab. Deliverable class will be inherited by class 
Quiz, Assignment and Lab since they share common attributes.

#### class Course

- This class is the blueprint for all the courses that will be in each block. In this project we only work with Block 3 courses.
- Block 3 courses are defined in this package (they can be taken as inputs from the user in future additions).
- The attributes of this class are: cname, instructor, block, rank, deliverables.
- 'cname' is the name of the course, 'instructor' is the professor who will teach the course, 'block' represents the block the course
will be taught in, 'rank' represents the difficulty level a student assigns to the course, it defaults to 1. Ranks go from 1 to 3 with
1 being 'easy', 2 being 'moderate' and 3 being 'hardest'. 'deliverables' will represent the deliverables for that course which will mainly
be objects of type Quiz, AssignLab and Project. 
	
#### class Deliverable

- This is the parent class for Quiz, AssignLab and Project classes.
- The dname, date and status attributes of this class are shared by each of the child classes.
- The child classes have their own unique attributes as well in addition to the attributes being inherited.
- 'dname' will hold the name for the deliverable type, 'date' will contain the due date for the deliverable and 'status' tells whether
the deliverable is complete or not. It defaults to 'Incomplete' for the child class objects.

#### class Quiz

- This is one of the child classes of class Deliverable.
- The attributes unique to this class are: topics and qtype.
- 'topics' represents the topics that will be on the upcoming quiz, and 'qtype' has the type of questions that will be asked like MCQs,
long answers, coding or a combination of these. 

#### class AssignLab

- This is another child class of class Deliverable.
- This class will represent objects of type Lab and Assignment both. They will be named accordingly. Since, the attributes for both of
these types of deliverables were same, they were combined to be in one class.
- The attributes unique to this class are: dur, durleft, subloc.
- 'dur' represents the time it will take to complete this deliverable, and 'durleft' represents the time left to complete this 
deliverable and 'subloc' shows where this deliverable has to be submitted on Canvas or using a repository.


#### class Project

- This is another child class of class Deliverable.
- This deliverable represents the Projects in the course (if applicable).
- The attributes unique to this class are: milestones, dur, durleft, repo.
- 'milestones' is supposed to represent any milestones that a student will have during the course of the project, 'dur' represents the 
time it will take to complete the project, and 'durleft' represents the time left to complete the project and 'repo' represents the github
link of the repository.

### Module 2:  people.py

This package will include a class ‘People’ which will have some basic attributes that will be inherited by the class Instructor and 
class Student. Main functions will be the getter, setter and delete methods.

#### class Person

- This is the parent class for Instructor and Student classes.
- The 'name' attribute of this class is shared by each of the child classes.
- The child classes have their own unique attributes as well in addition to the attribute being inherited.
	
#### class Instructor

- This is one of the child classes of class Person.
- It inherits the attribute 'name' from the parent class.
- The attributes unique to this class are: hours and comm.
- 'hours' describes the Office hours of the instructor and 'comms' describes the instructor's preferred method of communication.

#### class Student

- This is one of the child classes of class Person.
- It inherits the attribute 'name' from the parent class.
- The attributes unique to this class is: sID.
- 'sID' is the student number which is unique to a student.

## Sub-package 2 - system

### Module 1: deliverableviewer.py

This module shows what deliverables are due in the next 7 days. 

#### next7days

	- The next7days function takes no input and simply returns the next 7 dates (DD) from the current date.
	- usage: next7days()
	- output example: If today is December, 12: the return value will be a list: ['13','14','15','16','17','18','19']

#### deliverableSearch

	- The deliverableSearch function takes in a list of course objects and returns a list of deliverable objects that have due dates within the next 7 days.
	- usage: DeliverableSearch(courselist)
	- output example: [<MDSTimeManager.setup.course.Quiz object at 0x00000281B4D51040>] if printing returned value

#### deliverableViewer

	- The deliverableViewer function takes in a list of deliverable objects (AssignLab, Quiz, or Project), from the deliverableSearch function, that have a due date in the next 7 days, and prints the course name, deliverable name, and due date.
	- usage: deliverableViewer(deliverablelist)
	- output example: "Data533: Quiz         due on: 12/20 (MM/DD)"

#### deliverableAll

	- The deliverableAll function takes in a list of course objects and prints the course name, deliverable name, and due date of all deliverables for each course.
	- usage: deliverableViewer(courselist)
	- output example: 	Data533: Quiz,12/20
						Data533: Lab 1,12/05
						Data533: Project- Time Manager,12/22

### Module 2: timemanager.py

This module takes the next 7 days study time availability, inputed by the user and recommends an allotted study time for each course 
depending on how they have ranked the course and upcoming deliverables.

#### userinput

	- The userinput function takes in a list of course objects and collects input from the user regarding their study time for the next 7 days, ranks for each course, and amount of time needed to complete the associated deliverables. Then it outputs the amount of study time less time needed to complete the deliverables and returns that value.
	- usage: userinput(courselist)
	- output example: 20.0

#### fetchranks

	- The fetchRanks function takes in a list of course objects and returns the total of all ranks associated with each course in the list.
	- usage: fetchRanks(courselist)
	- output example: 1.0

#### timemanagercal

	- The timemanagercalc function takes in the time availability, returned from the userinput function, and a list of course objects, then prints the recommended study time for each course less the time needed to complete the deliverables.
	- usage: timeanagercal(timeavailable, course_list)
	- output example: 
						Recommended study time for Object Oriented Programming is 2.50 hours (150 mins)
						Recommended study time for Data Collection is 5.00 hours (300 mins)
						Recommended study time for Resampling and Regularization is 7.50 hours (450 mins)
						Recommended study time for Modelling and Simulation is 5.00 hours (300 mins)
						
### Module 3: main.py
This module  is the main control center for the package and runs all other modules from here.

#### execute
	- The execute function runs provides the user with a menu option and calls the other module functions/methods as needed.
	- usage: import MDSTimeManager as mdstm, mdstm.execute()
	- output example: 
	
					Welcome to the MDSTimeManager! 

					Please note:
					Presently this tool is strictly for use by MDS Okanagan students in Block 3 of 2022. 
					Future versions of this package will expand for use in all blocks for both MDS Vancouver and Okanagan students.


					Enter one of the following options:
					1    : Use the deliverableviewer and see upcoming or all due dates
					2    : Use the timemanagercalc and get study time recommendations
					x    : Quit the session
					 2



					Please choose a rank for the following courses out of (1,2,3) with 3 being most difficult.
					For Object Oriented Programming: 
					 3
					For Data Collection: 
					 1
					For Resampling and Regularization: 
					 1
					For Modelling and Simulation: 
					 1
					How much time is available in the next 7 days for studies (in hours)?  20

					How much time (in hours) you think you will take for the following:

					For Data543: Assignment 2           due on: 12/16 (MM/DD)
					 1
					For Data571: Assignment 2           due on: 12/19 (MM/DD)
					 2
					For Data 581: Lab 3                 due on: 12/15 (MM/DD)
					 2


					Time left after assignments and labs: 15.00 hours

					Recommended study time for Object Oriented Programming is 7.50 hours (450 mins)
					Recommended study time for Data Collection is 2.50 hours (150 mins)
					Recommended study time for Resampling and Regularization is 2.50 hours (150 mins)
					Recommended study time for Modelling and Simulation is 2.50 hours (150 mins)


					Enter one of the following options:
					1    : Use the deliverableviewer and see upcoming or all due dates
					2    : Use the timemanagercalc and get study time recommendations
					x    : Quit the session
					 x

					Your MDSTimeManger session is over. Have a good day :)

					
Link to the PyPi package: https://pypi.org/project/MDSTimeManager/

####################################################################################################
Sub-package 1
Module 1:  People
This package will include a class ‘People’ which will have some basic attributes that will be inherited by the class Instructor and class Student. Main functions will be the getter, setter and delete methods.
Module 2: Deliverables
This module will have classes for entities Course, Deliverable, Quiz, Assignment and Lab. Deliverable class will be inherited by class Quiz, Assignment and Lab since they share common attributes.
Sub-package 2
Module 1: DeliverableViewer
This module will be able to show what the deliverables in the next 7 days are like Labs, Assignments, or upcoming Quizzes or Projects and the date they are [due] on.
Module 2: TimeManager
This module will be doing all the computations for the package. It will take study time availability, for the next 7 days, from the student and recommend an allotted study time for each course depending on how they have ranked the course and upcoming deliverables.


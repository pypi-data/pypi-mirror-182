try:
    import datetime 

    import MDSTimeManager.system.deliverableviewer as dv
    import MDSTimeManager.setup.course as c
    import MDSTimeManager.system.TimeManager as tm 
    import MDSTimeManager.system.deliverableviewer as dv
    import MDSTimeManager.setup.mdstmerror as err

except ImportError as ierr:
    print("The following import error occured in the timemanager module:",ierr)
    
def userinput(Courses):
    try:
        t=0.0
        next7deliverables = dv.DeliverableSearch(Courses)

        print("\nPlease choose a rank for the following courses out of (1,2,3) with 3 being most difficult.")
        for course in Courses:
            while True:
                try:
                    rank = input(f"For {course}: ")
                    if rank in ["1","2","3"]:
                        break
                    else:
                        raise err.usrInputError(rank)
                except err.usrInputError as uie:
                    print(uie.value,"is an invalid rank, please try again.")
            course.rank = rank
        
        while True:
            try:
                weektime = float(input("How much time is available in the next 7 days for studies (in hours)? "))
                if weektime >= 0.0 and weektime <= 70.0:
                    break
                else:
                    raise err.usrInputError(weektime)
            except err.usrInputError as uie:
                print(uie.value,"is an invalid amount of time, please try again.")
                
        weektime = float(weektime)
        w = weektime
        if len(next7deliverables) > 0 and (any(isinstance(asslab, c.AssignLab) for asslab in next7deliverables) or any(isinstance(proj, c.Project) for proj in next7deliverables)):
            print("\nHow much time (in hours) you think you will take for the following:\n")
        for deliverable in next7deliverables:
            if isinstance(deliverable,c.AssignLab) or isinstance(deliverable,c.Project) :
                while True:
                    try:
                        time = float(input(f"For {deliverable}: "))
                        if time >= 0.0 and time <= 50.0:
                            break
                        else:
                            raise err.usrInputError(time)
                    except err.usrInputError as uie:
                        print(uie.value,"is an invalid amount of time, please try again.")
                time = float(time)
                t = t + time
                weektime = weektime - time
                deliverable.dur = time
            else:
                continue
        if t > w:
            return 0
        else:
            print(f"\n\nTime left after assignments and labs: {weektime:.2f} hours\n")
            return weektime
    
    except Exception as ex:
        print(f'Error Message: {ex}')
        print(f'Error Type: {type(ex)}')
        print("Please try again!")

def fetchranks(course_list):
    try:
        totalranks = 0.0
        for course in course_list:
            totalranks = totalranks + float(course.rank)
        return totalranks
    
    except TypeError as te:
        print("A TypeError has occured with message:",te)
    except Exception as ex:
        print(f'Error Message: {ex}')
        print(f'Error Type: {type(ex)}')
        print("Please try again!")
    
def timemanagercal(timeavailable, course_list):
    try:
        if timeavailable <= 0:
            print("\nTime alloted for studying is less than or equal to the time you will work on deliverables.\n")
            print("Study time cannot be recommended.\n")
        else:
            studytime = 0.0
            tr = fetchranks(course_list)
            for course in course_list:
                cr = float(course.rank)
                studytime = (cr/tr)*timeavailable
                print(f"Recommended study time for {course} is {studytime:.2f} hours ({studytime*60:1.0f} mins)")
    
    except TypeError as te:
        print("A TypeError has occured with message:",te)
    except AttributeError:
        print("An error occured when calculating study time recommendations.")
    except Exception as ex:
        print(f'Error Message: {ex}')
        print(f'Error Type: {type(ex)}')
        print("Please try again!")
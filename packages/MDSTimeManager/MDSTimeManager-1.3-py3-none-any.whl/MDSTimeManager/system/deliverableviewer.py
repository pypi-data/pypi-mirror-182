import datetime

def next7dates():
    """
    The function returns the next 7 dates (DD) from the current date.
    
    Input:
    The function does not require any inputs and can be called directly.
    
    Output:
    If today is December, 12: the output will be a list: ['13','14','15','16','17','18','19']
    """
    datelist=[]
    for i in range(0,7):
        datelist.append(str((datetime.datetime.now()+datetime.timedelta(i)).day))
    return datelist

def DeliverableViewer(deliverable_list):
    try:
        print("Deliverables due in the next 7 days are:\n")
        for deliverable in deliverable_list:
            print(deliverable)
        print("\n")
    
    except Exception as ex:
        print(f'Error Message: {ex}')
        print(f'Error Type: {type(ex)}')
        print("Please try again!")

def DeliverableSearch(course_list):
    try:
        lst = []
        for course in course_list:
            for deliverable in course.deliverables:
                if (deliverable.date.split("/")[1] in next7dates()):
                    lst.append(deliverable)
        return lst
    
    except ValueError:
        print("DeliverableSearch failed when looking for deliverables due in the next 7 days.")
    except Exception as ex:
        print(f'Error Message: {ex}')
        print(f'Error Type: {type(ex)}')
        print("Please try again!")
        
def DeliverableAll(course_list):
    try:
        for course in course_list:
            for deliverable in course.deliverables:
                print(f"{deliverable.dname},{deliverable.date}")
    except AttributeError:
        print("An error occured when looking for all deliverables.")
    except Exception as ex:
        print(f'Error Message: {ex}')
        print(f'Error Type: {type(ex)}')
        print("Please try again!")

     
   
import csv
def into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writeow(["Name","Age","Contact number","Email_ID"])
                            
        writer.writerow(info_list)
                            
if '_name_'=='_main_':
   condition=True
   student_num=1

while(condition):
       student_info=input("enter student information for student #{} in this format(Name Age Contact_Number Email_ID): ".format(student_num))
       
       student_info_list=student_info.split('')
       
       print("\nThe entered information is -\nName: {}\nAge: {}\nContact_number: {}\nEmail_ID: {}"
             .format(student_info_list[0], student_info_list[1], student_info_list[2]))

       choice_check=input("is the entered information correct?(yes/no):")
       if choice_check=="yes":
           into_csv(student_info_list)
           
           condition_check=input("enter (yes/no) if you want to enter information for another student:")
           
           if condition_check=="yes":
               
               condition=True
               
               student_num=student_num+1
               
               if condition_check=="no":
                  condition=False
               
               elif choice_check=="no":
                   
                    print("\nPlease re enter the values")

      
       

                            
                            

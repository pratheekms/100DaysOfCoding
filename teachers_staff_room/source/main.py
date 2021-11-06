# main program

import db

t_db=db.create_conn('teachersstaffroom')
print(t_db)

db.print_table_data(t_db)

def main():
    count=1
    operations_list=['add teacher','view teacher info','modify teacher info','delete teacher']
    print("Please select the operation")
    for i,op in enumerate(operations_list):
        print(str(i+1)+'. '+op)
    user_option=int(input('Please select an option: '))
    print('you have selected:'+(operations_list[user_option-1]))
    if user_option==1:
        add_teacher_info(t_db)
    elif user_option==2:
        view_teacher_info()
    elif user_option==3:
        modify_teacher_info()
    elif user_option==4:
        delete_teacher()



def add_teacher_info(t_db):
    print('in add_teacher_info')
    teacher_dict={'fname':'','lname':'',
    'gender':'','title':'','qualification':'','primary_subjet':'','seconday_subject':'','phno':'','email_id':''
    }
    # print(teacher_dict)
    for key in teacher_dict.keys():
        teacher_dict[key]=str(input('enter '+key+': '))
    print('afert details:',teacher_dict)
    user_input=tuple((x for x in teacher_dict.values()))
    new_teacher_id=db.insert_new_record(t_db,user_input)
    print('printing table data:')
    db.print_table_data(t_db)
    print('New teacher {} created with ID: {}.'.format(teacher_dict['fname'],new_teacher_id))

    # print(tp)



def view_teacher_info():
    print('in view_teacher_info')
    teacher_id=int(input('enter teacher ID: '))
    teacher_details=db.view_teacher_details(t_db,teacher_id)
    if teacher_details:
        print('Teacher Details:')
        for col,val in teacher_details[0].items():
            print(col+': '+str(val))
    else:
        print('Record does not exists for Teacher ID: {}'.format(teacher_id))

def modify_teacher_info():
    print('in modify_teacher_info')

def delete_teacher():
    print('in delete_teacher')

if __name__=='__main__':
    # main()
    view_teacher_info()
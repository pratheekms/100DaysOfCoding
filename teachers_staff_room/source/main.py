# main program

from typing import Optional
import db

t_db=db.create_conn('teachersstaffroom')
# print(t_db)

# db.print_table_data(t_db)

def main():
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
    print('Please enter new teacher details below')
    # print('in add_teacher_info')
    # teacher_dict={'fname':'','lname':'',
    # 'gender':'','title':'','qualification':'','primary_subjet':'','seconday_subject':'','phno':'','email_id':''
    # }
    # print(teacher_dict)
    teacher_dict={}
    col_names=db.get_column_names(t_db)
    for col in col_names[1:]:
        teacher_dict[col]=str(input('enter '+col+': '))
    # for key in teacher_dict.keys():
    #     teacher_dict[key]=str(input('enter '+key+': '))
    # print('afert details:',teacher_dict)
    user_input=tuple((x for x in teacher_dict.values()))
    new_teacher_id=db.insert_new_record(t_db,user_input)
    # print('printing table data:')
    # db.print_table_data(t_db)
    print('New teacher {} created with ID: {}.'.format(teacher_dict['first_name'],new_teacher_id))

    # print(tp)



def view_teacher_info():
    # print('in view_teacher_info')
    teacher_id=int(input('enter teacher ID: '))
    teacher_details=db.view_teacher_details(t_db,teacher_id)
    if teacher_details:
        print('Teacher Details:')
        for col,val in teacher_details[0].items():
            print(col+': '+str(val))
    else:
        print('Record does not exists for Teacher ID: {}'.format(teacher_id))
    user_choice=str(input('Do you want to modify the details?(y/n)'))
    if user_choice.lower()=='y':
        modify_teacher_info(teacher_id)
    else:
        exit(0)


def modify_teacher_info(teacher_id=None):
    # print('in modify_teacher_info')
    if teacher_id is None:
        teacher_id=int(input('enter teacher id: '))
    col_names=db.get_column_names(t_db)
    print("Please select the operation")
    for i,op in enumerate(col_names):
        print(str(i+1)+'. '+op)
    user_option=int(input('Please select an option: '))
    print('you have selected:'+(col_names[user_option-1]))

    new_val=input('enter new value to {}'.format(col_names[user_option-1]))
    db.update_teacher_record(t_db,col_names[user_option-1],new_val,teacher_id)
    u_choice=str(input('do you want to update another field?(y/n)'))
    while u_choice.lower() not in ("yes","no","y","n"):
        u_choice=str(input('do you want to update another field?(y/n)'))
    if u_choice.lower()=='y':
        modify_teacher_info(teacher_id)
    elif u_choice.lower()=='n':
        teacher_details=db.view_teacher_details(t_db,teacher_id)
        if teacher_details:
            print('Teacher Details after modification:')
            for col,val in teacher_details[0].items():
                print(col+': '+str(val))


def delete_teacher():
    # print('in delete_teacher')
    teacher_id=str(input('enter teacher id: '))
    record_to_be_deleted=db.view_teacher_details(t_db,teacher_id)
    # print(record_to_be_deleted)
    if record_to_be_deleted:
        print('Teacher Details:')
        for col,val in record_to_be_deleted[0].items():
            print(col+': '+str(val))
        user_choice=str(input('Do you want to delete teacher {} from records?(y/n)'.format(record_to_be_deleted[0]['first_name'])))
        if user_choice.lower()=='y':
            db.delete_teacher(t_db,teacher_id)
        else:
            print('Record NOT deleted')
            exit(0)
    else:
        print('Record does not exists for Teacher ID: {}'.format(teacher_id))

if __name__=='__main__':
    main()
    # view_teacher_info()
    # modify_teacher_info()
    # db.get_column_names(t_db)
    # delete_teacher()
    t_db.close()
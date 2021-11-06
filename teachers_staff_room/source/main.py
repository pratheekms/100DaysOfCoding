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
        add_teacher_info()
    elif user_option==2:
        view_teacher_info()
    elif user_option==3:
        modify_teacher_info()
    elif user_option==4:
        delete_teacher()



def add_teacher_info():
    print('in add_teacher_info')

def view_teacher_info():
    print('in view_teacher_info')

def modify_teacher_info():
    print('in modify_teacher_info')

def delete_teacher():
    print('in delete_teacher')

if __name__=='__main__':
    main()
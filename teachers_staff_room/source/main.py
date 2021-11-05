# main program

import db

t_db=db.create_conn('teachersstaffroom')
print(t_db)

db.print_table_data(t_db)
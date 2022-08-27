import modules.db_connection as dbc

mycursor = dbc.mydb.cursor()

def addGroup():
    try:
        print("Adding group details in database....")
        insert_group_previleges = """INSERT INTO group_privileges (group_name,user_access_control,print_report,view_time_table,view_channel_info,create_user,delete_user,create_grp,delete_grp,grp_list,add_session,delete_session) values (%(grp_name)s,%(user_access_control)s,%(print_report)s,%(view_time_table)s,%(view_channel_info)s,%(create_user)s,%(delete_user)s,%(create_grp)s,%(delete_grp)s,%(grp_list)s,%(add_session)s,%(delete_session)s)"""

        mycursor.execute(insert_group_previleges,grp_priv)
        dbc.mydb.commit()
        
        return 1

    except Exception as e:

        dbc.mydb.rollback()
        print("Error: ",e)
        return 0


grp_priv = {}

grp_priv['grp_name'] = input("Group name: ")
grp_priv['user_access_control'] = bool(input("User access control: ") or 0)
grp_priv['print_report'] = bool(input("Print Report: ") or 0)
grp_priv['view_time_table'] = bool(input("View Time Table: ") or 0)
grp_priv['view_channel_info'] = bool(input("View channel info: ") or 0)
grp_priv['create_user'] = bool(input("Create User: ") or 0)
grp_priv['create_grp'] = bool(input("Create Group: ") or 0)
grp_priv['grp_list'] = bool(input("Group List: ") or 0)
grp_priv['add_session'] = bool(input("Add session: ") or 0)
grp_priv['delete_user'] = bool(input("Delete User: ") or 0)
grp_priv['delete_grp'] = bool(input("Delete Group: ") or 0)
grp_priv['delete_session'] = bool(input("Delete Session: ") or 0)

print(grp_priv)

addGroup()
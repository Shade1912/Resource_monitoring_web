import modules.db_connection as dbc

mycursor = dbc.mydb.cursor()

def editGroup(group_name):
    try:
        grp_priv = {}
        grp_priv['group_name'] = group_name
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
        
        update_query = '''UPDATE group_privileges SET user_access_control= %(user_access_control)s ,print_report= %(print_report)s ,view_time_table= %(view_time_table)s ,view_channel_info= %(view_channel_info)s ,create_user= %(create_user)s ,delete_user= %(delete_user)s ,create_grp= %(create_grp)s ,delete_grp= %(delete_grp)s ,grp_list= %(grp_list)s ,add_session= %(add_session)s ,delete_session= %(delete_session)s WHERE group_name = %(group_name)s'''

        mycursor.execute(update_query,grp_priv)
        dbc.mydb.commit()
        return 1

    except Exception as e:
        dbc.mydb.rollback()
        return 0

editGroup("Admin2")
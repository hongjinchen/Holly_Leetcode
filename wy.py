action_list=[{'id': '1', 'action': '1', 'time': '1'}, {'id': '2', 'action': '0', 'time': '2'}, {'id': '1', 'action': '0', 'time': '3'}, {'id': '2', 'action': '0', 'time': '4'}]

user_last_is_update_action_list=[]
# 判定是否是一个用户中两次1行为是连续的

error_user=[]
for action in action_list:
    user_id=action["id"]
    user_action=action["action"]
    if user_action=="0":
        if user_id not in user_last_is_update_action_list:
            user_last_is_update_action_list.append(user_id)
        else:
            error_user.append(user_id)
    else:
         if user_id in user_last_is_update_action_list: 
            user_last_is_update_action_list.remove(user_id)
print(error_user)
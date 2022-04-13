import sqlite3
import random
import pandas as pd

def q_time_test(Q_TIME):
    global T_obs
    if Q_TIME < 20:
        T_obs = 'mo'
    elif Q_TIME >= 20 and Q_TIME <= 60:
        T_obs = 'rst'
    else:
        T_obs = 'rsq' 
def q_hint_test(N_HINT):
    global H_obs
    if N_HINT == 1:
        H_obs = 'rst'
    elif N_HINT == 2 or N_HINT == 3:
        H_obs = 'rsq'
    else:
        H_obs = 'mo'
def answer_test(USER_ANSWER):
    global A_obs
    if USER_ANSWER == 0:
        A_obs = 'rsq'
    else:
        A_obs = 'mo'

conn = sqlite3.connect('analyse.db')
cur = conn.cursor()

cur.execute("""Select * from QB_TABLE""")
questions_df = pd.DataFrame(cur.fetchall())
questions_df.columns = ['Q_ID','Sub_ID','SK_LVL','Question','Op1','Op2','Op3','Op4','Answer']
cur.execute("""Select * from USER_ANALYSIS_TABLE""")
analyse_ds_df = pd.DataFrame(cur.fetchall())
analyse_ds_df.columns = ['U_ID','Q_ID','Sub_ID','SK_LVL','Q_Time','N_Hint',"User_Answer"]
print(analyse_ds_df)

def update_processed_data():
    cur.execute("""DELETE FROM PROCESSED_DATA""")
    for i in range(len(analyse_ds_df)):
        user_id = analyse_ds_df['U_ID'][i]
        subject_id = analyse_ds_df['Sub_ID'][i]
        question_id = analyse_ds_df['Q_ID'][i]
        q_hint_test(analyse_ds_df['N_Hint'][i])
        q_time_test(analyse_ds_df['Q_Time'][i])
        answer_test(analyse_ds_df['User_Answer'][i])
        Sk_lvl = analyse_ds_df['SK_LVL'][i]
        cur.execute("""INSERT INTO PROCESSED_DATA VALUES(?,?,?,?,?,?,?)""",(int(user_id),subject_id,question_id,H_obs,T_obs,A_obs,int(Sk_lvl)))
    conn.commit()
update_processed_data()
cur.execute("""SELECT * FROM PROCESSED_DATA""")
Processed_Data = pd.DataFrame(cur.fetchall())
Processed_Data.columns = ['U_ID','Sub_ID','Q_ID','H_Obs','T_Obs','A_Obs','SK_LVL']
print(Processed_Data)

def add_into_qp():
    global q_add_list
    q_add_list = []
    for i in range(len(Processed_Data)):
        verdict = ''
        grouping_list = []
        grouping_list.append(Processed_Data['H_Obs'][i])
        grouping_list.append(Processed_Data['A_Obs'][i])
        grouping_list.append(Processed_Data['T_Obs'][i])
        if grouping_list[0] == 'rst':
            verdict = 'rst'
        elif grouping_list[0] == 'rsq':
            verdict = 'rsq'
        else:
            if grouping_list[1] == 'rsq':
                verdict = 'rsq'
            else:
                if grouping_list[2] == 'mo':
                    verdict = 'mo'
                elif grouping_list[2] == 'rsq':
                    verdict = 'rsq'
                else:
                    verdict = 'rst'
        if verdict == 'mo':
            pass
        elif verdict == 'rst':
            for j in range(len(questions_df)):
                if (questions_df['SK_LVL'][j] == Processed_Data['SK_LVL'][i]):
                    temp_list = []
                    if questions_df['Q_ID'][j] not in temp_list:
                        temp_list.append(questions_df['Q_ID'][j])
                    else:
                        continue
                else:
                    continue
            rc = random.choice(temp_list)
            if rc not in q_add_list:
                q_add_list.append(rc)
        else:
            if Processed_Data['Q_ID'][i] not in q_add_list:
                q_add_list.append(Processed_Data['Q_ID'][i])
add_into_qp()
print(q_add_list)

conn.commit()
conn.close()
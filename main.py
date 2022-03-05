import streamlit as st

a = st.subheader('name')
name = st.text_input('')

gender = st.radio("gender", ("m", "f"))

b = st.subheader('age')
age = st.number_input('')

rank = st.radio("tear", ("iron", 'bronze', 'silver' ,'gold', 'platinum', 'diamond', 'master', 'grandmaster', 'challenger'))

line = st.multiselect('often line',
                              ['top', 'jg', 'mid', 'adc', 'sup'])
st_line = ''.join(line)

head = st.subheader("often play champ")
champ = st.text_input(' ')

c = st.header("Average play time per day")
time = st.time_input('')

fin = st.button
file = ['name : ', name,'\n', 'gender : ', gender,'\n', "age : ",
        str(age), '\n', "rank : ", rank,'\n',
        "line : ", st_line, '\n',"champ : ", champ, '\n',"time : ", str(time), "\n"]
if st.button("sub"):
    from glob import glob
    total_files = glob("*.txt")
    with open("text_{}.txt".format(str(len(total_files) + 1)), 'w') as f:
        for ans in file:
            f.write(ans)
        f.close()

import streamlit as st
import functions

#funkcija za dodavanje novih itema na listu
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.update_list(todos)


##### Funkcija koja se koristi za citanje fajla
todos = functions.get_user_input()

##### Dodaj naslov
st.title("Monthly Rollercoaster")

##### Dodaj podnaslov
st.subheader("Add items that should be executed this month.")

##### Dodaj polje za unos, sa place holderom
st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

##### Za svaki item u fajlu, napravi checkbox na webapp
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.update_list(todos)
        del st.session_state[todo]
        st.rerun()


import streamlit as st
import pandas as pd
import os

# Function to load menu from Excel file
def load_menu():
    if not os.path.exists('menu.xlsx'):
        create_empty_menu()
    menu_df = pd.read_excel('menu.xlsx')
    return menu_df

# Function to create an empty menu Excel file
def create_empty_menu():
    df = pd.DataFrame(columns=['Day', 'Breakfast', 'Lunch', 'Dinner'])
    df.to_excel('menu.xlsx', index=False)

# Function to save menu to Excel file
def save_menu(menu_df):
    menu_df.to_excel('menu.xlsx', index=False)

# Student Page
def student_page():
    st.title("Student Menu")

    menu_df = load_menu()
    st.write(menu_df)

# Manager Page
def manager_page():
    st.title("Manager Menu")

    menu_df = load_menu().copy()  # Make a copy of the DataFrame

    # Option to add new item to menu
    st.header("Add Item to Menu")
    new_day = st.text_input("Day:")
    new_breakfast = st.text_input("Breakfast:")
    new_lunch = st.text_input("Lunch:")
    new_dinner = st.text_input("Dinner:")
    if st.button("Add"):
        new_item = pd.DataFrame({'Day': [new_day], 'Breakfast': [new_breakfast], 'Lunch': [new_lunch], 'Dinner': [new_dinner]})
        menu_df = pd.concat([menu_df, new_item], ignore_index=True)
        save_menu(menu_df)
        st.success("Item added successfully!")

    # Option to delete item from menu
    st.header("Delete Item from Menu")
    delete_index = st.selectbox("Select index to delete:", menu_df.index)
    if st.button("Delete"):
        menu_df = menu_df.drop(delete_index)
        save_menu(menu_df)
        st.success("Item deleted successfully!")

    # Option to update item in menu
    st.header("Update Item in Menu")
    update_index = st.selectbox("Select index to update:", menu_df.index)
    new_day = st.text_input("Day:", value=menu_df.loc[update_index, 'Day'])
    new_breakfast = st.text_input("Breakfast:", value=menu_df.loc[update_index, 'Breakfast'])
    new_lunch = st.text_input("Lunch:", value=menu_df.loc[update_index, 'Lunch'])
    new_dinner = st.text_input("Dinner:", value=menu_df.loc[update_index, 'Dinner'])
    if st.button("Update"):
        menu_df.loc[update_index, 'Day'] = new_day
        menu_df.loc[update_index, 'Breakfast'] = new_breakfast
        menu_df.loc[update_index, 'Lunch'] = new_lunch
        menu_df.loc[update_index, 'Dinner'] = new_dinner
        save_menu(menu_df)
        st.success("Item updated successfully!")

    st.write(menu_df)


# Main App
def main():
    page = st.sidebar.radio("Navigation", ["Student", "Manager"])

    if page == "Student":
        student_page()
    elif page == "Manager":
        manager_page()

if __name__ == "__main__":
    main()

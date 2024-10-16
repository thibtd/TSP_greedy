import streamlit as st
from get_long_lat_cities import get_long_lat_dataFrame
from tspEurope import compute_distances,simulation,plot_path
import numpy as np

def logic(numSim:int, cities_input_list:list, startingCity:str):
    #computations
    cities = get_long_lat_dataFrame(cities=cities_input_list)
    distances = compute_distances(cities)
    visited, distancesTravelled = simulation(numSim, cities, distances, startingCity=startingCity)
    plot = plot_path(cities, visited, distancesTravelled)
    return visited, distancesTravelled, plot


def Input():
    
    st.title("Travelling Salesman Problem")
    st.write("This app demonstrates a solution to the the Travelling Salesman Problem by utilising a greedy algorithm.")
    st.write("The solution is based on the best path found after running the algorithm for a given number of iterations.")
    st.header("The app takes different inputs :")
    col1, col2= st.columns(2,gap="small")
    with col1:
        st.write("        - The number of iterations to run the simulation.")
        st.write("        - The starting city for the salesman.")
        st.write("       - The cities to include in the simulation.")
    with col2:
        numSim = int(st.number_input("Enter the number of iterations to run the simulation", value=100))
        
        default_cities ="Brussels,Paris,Madrid, Frankfurt,Poznań,Copenhagen,Kraków,Berlin,Vienna,Rome,Amsterdam,Lisbon,Stockholm,Oslo,Helsinki, \
        Vilnius,Dublin,Warsaw,Budapest,Prague"
        cities_input = st.text_area("Enter the cities to include in the simulation, separated by a comma", value= default_cities)
        cities_input_list = cities_input.split(",")
        print(cities_input_list)
        if len(cities_input_list) < 3:
            st.warning("Please enter at least 3 cities.")
            cities_input_list = default_cities
        startingCity = st.selectbox("Select the starting city for the salesman", cities_input_list)

    return numSim, cities_input_list, startingCity

def output(plot:object, visited:list, distancesTravelled:list):
    col3, col4 = st.columns(2,gap="small")
    with col3:
        st.plotly_chart(plot, use_container_width=True) 
    with col4:
        st.header(f"The best path found after {numSim} iterations is:")
        st.markdown(f"The total distance travelled is **{np.round(sum(distancesTravelled),0)}** km.",)
        for i in range(len(visited)-1):
            st.write(f"Step {i+1}: {visited[i]} -> {visited[i+1]} in {np.round(distancesTravelled[i],0)}km. ")
    

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    numSim, cities_input_list, startingCity = Input()
    
    if st.button("Run Simulation",icon="🛠️"):
        visited,distancesTravelled, plot =logic(numSim, cities_input_list, startingCity) 
        output(plot, visited, distancesTravelled)





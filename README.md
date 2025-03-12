# **Unit Ball Visualization in Different Norms**  

This project visualizes **unit balls** in different randomly chosen **Lp norms**. It generates unit balls using **random centers, norms, and colors**, then plots them using Matplotlib. It includes two main scripts: `main.py` and `closest_with_color_and_location.py`.

## **Features**  
- **main.py**:
   - Randomly generates **unit balls** in various **Lp norms**  
   - Colors the unit balls based on **RGB values**  
   - Orders and groups balls by their distances in different norms  
   - Displays a **grid and axis-centered plot**
- **closest_with_color_and_location.py**:
   - Finds and plots the closest pair of circles based on their measures, and visualizes circles with different norms and colors.



## **Usage**  
- The script randomly generates **N unit balls** and visualizes them.  
- Balls are displayed in both **individual positions** and **ordered rows** based on RGB distances.


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/alexnat009/UnitBallsInDifferentNorms.git
    cd your-repo-name
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install numpy
    pip install matplotlib
    ```


## **Customization**  
You can modify:  
- `number_of_balls` to change the number of unit balls.  
- Norm ranges in `random.uniform(0.1, 5)` to experiment with different norms.  
## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.


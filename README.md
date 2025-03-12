# **Unit Ball Visualization in Different Norms**  

This project visualizes **unit balls** in different randomly chosen **Lp norms**. It generates unit balls using **random centers, norms, and colors**, then plots them using Matplotlib.

## **Features**  
- Randomly generates **unit balls** in various **Lp norms**  
- Colors the unit balls based on **RGB values**  
- Orders and groups balls by their distances in different norms  
- Displays a **grid and axis-centered plot**  

## **Installation**  

1. Clone the repository:  
   ```bash
   git clone https://github.com/alexnat009/UnitBallsInDifferentNorms.git
   cd UnitBallsInDifferentNorms
   ```

2. Install dependencies (if needed):  
   ```bash
   pip install matplotlib numpy
   ```

3. Run the script:  
   ```bash
   python main.py
   ```

## **Usage**  
- The script randomly generates **8 unit balls** and visualizes them.  
- Balls are displayed in both **individual positions** and **ordered rows** based on RGB distances.  

## **Customization**  
You can modify:  
- `number_of_balls` to change the number of unit balls.  
- Norm ranges in `random.uniform(0.1, 5)` to experiment with different norms.  

## **Example Output**  
A plot showing unit balls with different norms and colors.

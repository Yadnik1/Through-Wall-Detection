# Through-Wall Detection Using UWB Radar System

Through-wall radar systems have grown immensely popular due to their potential applications in military and civil sectors. These systems aim to detect objects, especially humans, present inside rooms or structures, shielded by walls. Traditional narrowband radar systems face challenges due to the superimposition of multi-path returned signals, making it hard to distinguish the target signal from the multi-path signals. However, ultra-wide band (UWB) through-wall radar systems have shown promise in distinguishing these signals effectively.

## Project Overview

This project focuses on implementing a UWB Radar system for imaging to obtain electromagnetic images from behind or through walls. The technique provides an electromagnetic "vision" behind walls to detect, count, and localize individuals inside a room or building.

**Key Objectives:**
- Achieve higher range measurement accuracy and range resolution.
- Recognize the type of targets and generate radar images.
- Minimize the effects of passive interferences like rain and fog.
- Reduce the radar's 'Dead Zone'.
- Enhance radar operation security.
- Improve immunity to external radiation.

## UWB Radar System Details

1. **TWD-UWB radar operation**: The radar transmits a narrow RF pulse and samples echoes from different receiver terminals sequentially.
2. **Pulse width**: A pulse width of 700ps is planned. The pulse isn't rectangular but is similar to a wavelet.
3. **Effective sampling rate**: Planned effective sampling rate is 250ps (4 GSPS). It ensures that the echo isn't missed due to inappropriate sampling.
4. **Accurate phase measurement**: Cross range target positioning accuracy is dependent on accurate phase measurement.

## Python Implementation & Visualization

### Correlated Data Visualization
![Correlated Data Visualization](https://github.com/Yadnik1/Through-Wall-Detection/blob/main/images/Correlated%20Data.PNG?raw=true)

The Python codebase provided serves two primary functions:

1. **Algorithm Implementation**: The UWB radar system's operations and pulse transmissions are algorithmically simulated. This ensures accurate detection and localization of targets behind walls.
   
2. **Data Visualization**:
   - **Reflectivity Plots**: These plots display the reflection strength from different points. 
   ![Reflectivity Plot](https://github.com/Yadnik1/Through-Wall-Detection/blob/main/images/Reflectivity%20Plot.PNG?raw=true)
   
   - **Intensity Plots**: These represent the magnitude of the detected signals. Intense spots indicate potential target locations behind the wall.
   ![Intensity Data](https://github.com/Yadnik1/Through-Wall-Detection/blob/main/images/Intensity%20data.PNG?raw=true)
   
   - **Heat Map**: Heat maps provide a graphical representation of data where values are depicted by colors. It helps in quickly spotting areas of interest.
   ![Heat Map](https://github.com/Yadnik1/Through-Wall-Detection/blob/main/images/Heat%20Map.PNG?raw=true)

### GUI Representation
![GUI Representation](https://github.com/Yadnik1/Through-Wall-Detection/blob/main/images/GUI.PNG?raw=true)

### File Selection Interface
![Select File Interface](https://github.com/Yadnik1/Through-Wall-Detection/blob/main/images/Select%20file.PNG?raw=true)

## Getting Started

*Here you might want to add steps on how to run the python code, any dependencies required, and other setup-related information.*

## Conclusion

The UWB through-wall radar system holds significant potential for real-world applications, especially in defense sectors.

*Feel free to add sections on contributions, authors, acknowledgements, etc. as per your project's needs.*

# Through-Wall Detection Using UWB Radar System

Through-wall radar systems have grown immensely popular due to their potential applications in military and civil sectors. These systems aim to detect objects, especially humans, present inside rooms or structures, shielded by walls.

## Project Overview

This project focuses on implementing a UWB Radar system for imaging to obtain electromagnetic images from behind or through walls. The technique provides an electromagnetic "vision" behind walls to detect, count, and localize individuals inside a room or building.

### Key Objectives:

- Achieve higher range measurement accuracy and range resolution.
- Recognize the type of targets and generate radar images.
- Minimize the effects of passive interferences like rain and fog.
- Reduce the radar's 'Dead Zone'.
- Enhance radar operation security.
- Improve immunity to external radiation.

## UWB Radar System Details

- **TWD-UWB radar operation**: The radar transmits a narrow RF pulse and samples echoes from different receiver terminals sequentially.
- **Pulse width**: A pulse width of 700ps is planned.
- **Effective sampling rate**: Planned effective sampling rate is 250ps (4 GSPS).
- **Accurate phase measurement**: Cross range target positioning accuracy is dependent on accurate phase measurement.

## Python Implementation & Visualization

### Algorithm Flowchart
An illustrative flowchart highlighting the primary steps involved in the processing algorithm.
![Algorithm Flowchart](https://github.com/Yadnik1/Through-Wall-Detection/blob/main/images/Algorithm%20flowchart.PNG?raw=true)

### GUI Representation
The primary user interface for the radar system, where users can input parameters and visualize results.
![GUI Representation](https://github.com/Yadnik1/Through-Wall-Detection/blob/main/images/GUI.PNG?raw=true)

### File Selection Interface
Interface that allows users to select specific data files for processing.
![Select File Interface](https://github.com/Yadnik1/Through-Wall-Detection/blob/main/images/Select%20file.PNG?raw=true)

### Correlated Data Visualization
Displays the correlation between the captured radar signals over time.
![Correlated Data Visualization](https://github.com/Yadnik1/Through-Wall-Detection/blob/main/images/Correlated%20Data.PNG?raw=true)

### Reflectivity Plot
Showcases how different targets reflect the radar signal. A higher reflectivity indicates a more substantial object or obstacle.
![Reflectivity Plot](https://github.com/Yadnik1/Through-Wall-Detection/blob/main/images/Reflectivity%20Plot.PNG?raw=true)

### Intensity Data
Highlights the signal strength or intensity captured by the radar. This data is crucial for identifying the presence of objects.
![Intensity Data](https://github.com/Yadnik1/Through-Wall-Detection/blob/main/images/Intensity%20data.PNG?raw=true)

### Heat Map
A visual representation that indicates the intensity of detected objects in different regions. The warmer the color, the higher the object's presence or intensity.
![Heat Map](https://github.com/Yadnik1/Through-Wall-Detection/blob/main/images/Heat%20Map.PNG?raw=true)

## Mathematical Background

Let a particular “range sector (±70⁰) be divided into 14 sections of 10 deg each, 7 on each side. This forms the basis of signal processing where signals received by multiple receivers provide valuable information about target localization.

The in-depth mathematical framework involves the use of Path matrices, Reflectivity matrices, and received signal matrices. The core problem revolves around given a received signal matrix \(X\), how to determine the Reflectivity matrix \(B\). The solution to this is derived using Singular Value Decomposition (SVD) technique and other matrix operations.


## Getting Started

1. Please clone the Repository
2. Run the main.py file
3. In the GUI, please select the InputData - 29Mar20223a file
4. Proceed by clicking on "Process Data"

## Conclusion

The UWB through-wall radar system holds significant potential for real-world applications, especially in defense sectors.

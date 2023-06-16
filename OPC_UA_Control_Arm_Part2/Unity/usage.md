# Unity package for Robot Arm 3D

## In-project package
1. Universal RP
    1. Re-bake lighting in Windows -> Rendering -> Lighting
    1. Re-bake Occlusion in Windows -> Rendering -> Occlusion. This allow Unity only render what camera see in game mode
    1. Convert material and generate graphic setting for URP in Windows -> Rendering -> Render Pipeline Converter
2. XR Plugin Management
1. Oculus XR Plugin

## In-asset package
1. Oculus integration. Follow their tutorial to set up graphic setting and camera seeting: https://developer.oculus.com/documentation/unity/unity-conf-settings/


## Tips
1. In Windows -> Analysis, there're several tools to measure game performance:
    1. Profiler: Watch CPU, GPU usage. if CPU is spending too much time for Gfx.WaitForPresent, this mean your project is **Gpu bound** - GPU is spending too much time rendering the scene, and CPU, which complete its job faster, has to wait for GPU. More info can be found here: https://github.com/UnityCommunity/UnityLibrary/wiki/Profiler:-Overhead---Gfx.WaitForPresent-explained
    1. Enable GPU profiler to see draw call, and spot potential issue with GPU draw.
    1. Frame Debug: useful to see how does Unity render the frame. To lower frame drawing, consider using the same material for several object in the scene, or make that object static, and apply **Pre-bake lighting.**
2. In Game tab, notice:
    1. **Stats**: report game statistic, especially the **Batches**; the lower the Batches, the better.
    1. Choose **Play Unfocused** to prevent Unity to jump from **Editor Tab** to **Game Tab**
# Unity package for Robot_Arm_3D

This is a VR application which contain robotic arm 3D model as well as buttons to control the real entity. 

## Necessary in-project package:

1. URP
    1. You may need to "re-bake" the lighting setting. go to Windows->Rendering->Lighting and Generate Lighting. This is going to take a long time, so be patient.
    1. Re-bake Occlusion to allow Unity only render thing that camera see. Set object as Occludee/Occluder static to make this work.
    1. Go to Render Pipeline converter to convert object to the correct material in URP, also generate all graphic settings.
1. Oculus XR Plugin
1. XR Plugin Management

## Necessary in-asset pakage:
1. Oculus integration (this project is using version 53.1)
    1. Follow their tutorial to setup graphic setting: https://developer.oculus.com/documentation/unity/unity-conf-settings/

## Tips
1. Go to Windows->Analysis, there're several tools to measure game performance.
    1. Profiler: watch cpu, gpu usage, see what's the problem. If cpu spent a lot of time in Gfx.WaitForPresent, it mean that your project is **GPU bound**, which mean gpu spend too much time rendering the scene. More info here https://github.com/UnityCommunity/UnityLibrary/wiki/Profiler:-Overhead---Gfx.WaitForPresent-explained.
    1. If GPU is rendering too much, in the Profiler, enable GPU profiler and see the number of draw call to see what is affecting performance.
    1. Frame Debug: helpful to know how does Unity render a scene, this may help you spot the problem when Unity overdraw
1. In the **Game** tab, notice **Stats -> Batches**. The lower the Batches, the better. 
1. In **Game** tab, choose **Play Unfocused** to prevent Unity to jump from the **editor** tab to **play** tab when play the game.
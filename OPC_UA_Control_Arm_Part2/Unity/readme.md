
## Tips
1. Go to Windows->Analysis, there're several tools to measure game performance.
    1. Profiler: watch cpu, gpu usage, see what's the problem. If cpu spent a lot of time in Gfx.WaitForPresent, it mean that your project is **GPU bound**, which mean gpu spend too much time rendering the scene. More info here https://github.com/UnityCommunity/UnityLibrary/wiki/Profiler:-Overhead---Gfx.WaitForPresent-explained.
    1. If GPU is rendering too much, in the Profiler, enable GPU profiler and see the number of draw call to see what is affecting performance.
    1. Frame Debug: helpful to know how does Unity render a scene, this may help you spot the problem when Unity overdraw
1. In the **Game** tab, notice **Stats -> Batches**. The lower the Batches, the better. 
1. In **Game** tab, choose **Play Unfocused** to prevent Unity to jump from the **editor** tab to **play** tab when play the game.
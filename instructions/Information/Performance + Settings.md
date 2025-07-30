# Description
These are the settings suggested by CheesyDDA on the HD2-Discord and has simply been copied.
# Overview
- **Texture quality: ULTRA**, no diff on other settings, MEDIUM for a 2% PERFORMANCE gain (LE- if needed but likely won't).,
- **Object Detail Quality: HIGH** not worth dropping a couple frames.,
- **Render Distance: HIGH**, there is no visible difference between ULTRA and HIGH save the extra frames by going HIGH.,
- **Shadow Quality: MEDIUM (HE)**, I like how soft the shadows look in MEDIUM giving a 4-5% increase in PERFORMANCE while giving a similar look in ULTRA and HIGH, LOW (LE) will give the best PERFORMANCE by 8% from ULTRA without making the shadows look like blobs no noticeable difference in PERFORMANCE from LOWEST to LOW.,
- **Particle Quality: HIGH**, MEDIUM (LE) for 3% PERFORMANCE gain.,
- **Reflection Quality: LOW**, the HIGH settings looks great but the occlusion artifacts will ruin the look of the game as the water reflection tries to overlap the objects in the game. Until helldivers 2 fixes this issue with light scatters and the way objects absorb the light, I am keeping this LOW for best PERFORMANCE gain of 7%. MEDIUM vs LOW has little to no visual difference, and LOWEST looks like crap with no PERFORMANCE change.,
- **Space Quality: LOW**, the most useless setting here as it changes one star in the sky with little to no difference not worth giving away 6-8% PERFORMANCE gain.,
- **Ambient Occlusion: ON**, Keep this on, your game looks awesome with this on!!! unless you want jagged edges with a 3-4% PERFORMANCE gain up to you!,
- **Screen Space Global Illumination: OFF**, this is suppose to upgrade the lighting around the shadows bouncing off the environment of the game but it makes shadows give an incorrect glow. Keeping this setting off actually makes the game look better with a 3-4% PERFORMANCE gain.,
- **Vegetation and Rubble Density: HIGH**, 2-4% PERFORMANCE gain ,depending on maps, reducing the distance grass and shrubs pop up, no visual difference in ULTRA and HIGH. Going lower than HIGH will likely cause random shrubs and rocks to pop up out of nowhere with only a 1% PERFORMANCE difference.,
- **Terrain Quality: HIGH**, game looks great. go LOW (LE) for 4% PERFORMANCE gain. Not worth the sacrifice but if you must.,
- **Volumetric Fog Qual: MEDIUM**, No difference visually from HIGH to MEDIUM. However going to LOW or LOWEST certain lights will no longer cast through the fog, I like the way it looks so I will be keeping it on. But, if it obstructs view go for LOWEST for the 6% PERFORMANCE gain. Basically: Extra lighting details (MEDIUM) or Extra frames (LOWEST) your choice.,
- **Volumetric Cloud Quality: LOW**, no difference in visuals, go low for a 5% PERFORMANCE gain. LOWEST will give an extra 2% PERFORMANCE gain but you lose a lot of cloud quality,
- **Lighting Quality: LOW** only difference is on the ship. 3% PERFORMANCE gain.,
- **Anti-Aliasing: ON**, game will look bad if off. IF you really need the performance gains, you can turn it off and turn sharpness down to 0 to reduce the effects of jaggedness on objects for a an increase in PERFORMANCE by 6%.,
- **Render Scale, ULTRA QUALITY**, NATIVE to ULTRA QUALITY increased performance by almost 20%, however for me it didn't improve going lower. (Go QUALITY or BALANCED if LE GPU) . DON'T USE PERFORMANCE THEY SUCKKKKKK.,
- **Async Compute:** **enabled** if you want to offload some CPU tasks to the GPU. **disabled** for (HE), If you have good cpu than turning this on could decrease GPU load.
# Tips for best Performance
- Ensure VSYNC is **OFF**. 
    - GSync, Adaptive Sync, and FastSync are fine, but may limit your framerate to the maximum refresh rate of your display.,
    - If you cannot maintain the FPS required to hit your monitor's maximum refresh rate, VSYNC will progressively HALVE your refresh rate, and thus your framerate, and lock it there.
- Make sure you are on one of the suggested [[GPU Drivers]]:
    - NVIDIA: 566.36, AMD RDNA: 24.12.1, AMD VEGA: 22.11.2,
- Clear your `Shader Cache` after every game update.
    - Delete the `%APPDATA%\Arrowhead\Helldivers2\shader_cache`folder.,
- If you have a NVIDIA GPU, try running [[DirectX11|DX11]] mode.
    - Right click the game in steam, and pick Properties.,
    - In the `Launch Options` textbox, add `--use-d3d11`,
    - AMD users beware: This launch option may make your game unable to start.
- Make sure your Windows `Power Plan` is set to `High Performance`
    - Click Start, type `power plan`, pick `Choose a power plan`, click the radio button next to `High Performance`.
- Make sure your GPU `Power management` is set to `Prefer Maximum Performance`.
    - Open the NVIDIA App, Click Graphics, Pick Helldivers2, change `Power Management Mode` to `Prefer maximum performance`,
- Set your High Performance GPU in Windows
    - Hellbomb script option `[P]` and follow the on-screen steps.
* Make sure to set up your [[Set Pagefile|Pagefile]] correctly.
# Display Resolutions
It is noted that Helldivers 2 is very limited in terms of Resolution - either a 5/4 or 16/9 is only possible since everything else would interfere with the levels, according to this post: 
https://steamcommunity.com/app/394510/discussions/0/496880503069875485/#c496880503078246862

Linux Users may want to try Gamescope, but there is no guarantee in resolving this issue.
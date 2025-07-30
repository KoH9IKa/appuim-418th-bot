# Description
These are the settings suggested by CheesyDDA on the HD2-Discord https://discord.com/channels/1102970375731691612/1218153537914273802/1310715880681771008
- Ensure VSYNC is **OFF**. 
    - GSync, Adaptive Sync, and FastSync are fine, but may limit your framerate to the maximum refresh rate of your display.,
    - If you cannot maintain the FPS required to hit your monitor's maximum refresh rate, VSYNC will progressively HALVE your refresh rate, and thus your framerate, and lock it there.
- Make sure you are on one of the suggested gpu driver:
    - NVIDIA: 566.36, AMD RDNA: 24.12.1, AMD VEGA: 22.11.2,
- Clear your `Shader Cache` after every game update.
    - Delete the `%APPDATA%\Arrowhead\Helldivers2\shader_cache`folder.,
- If you have a NVIDIA GPU, try running in dx11 mode.
    - Right click the game in steam, and pick Properties.,
    - In the `Launch Options` textbox, add `--use-d3d11`,
    - AMD users beware: This launch option may make your game unable to start.
- Make sure your Windows `Power Plan` is set to `High Performance`
    - Click Start, type `power plan`, pick `Choose a power plan`, click the radio button next to `High Performance`.
- Make sure your GPU `Power management` is set to `Prefer Maximum Performance`.
    - Open the NVIDIA App, Click Graphics, Pick Helldivers2, change `Power Management Mode` to `Prefer maximum performance`,
- Set your High Performance GPU in Windows
    - Hellbomb script option `[P]` and follow the on-screen steps.
- Make sure to set up your page file set correctly.

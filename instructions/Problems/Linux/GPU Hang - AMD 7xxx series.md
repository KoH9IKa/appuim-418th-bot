# Description
When playing Helldivers 2 on Linux with a 7xxx series AMD graphics card, the driver stops working and a GPU reset is initiated.
# Problem
The problem stems from using the AMD RX 7xxx series Graphic Cards and Mesa 25.1. This is because the workaround for GFX11 was removed.

For more info: https://gitlab.freedesktop.org/mesa/mesa/-/issues/13369#note_2962408
# Solution
Either turn off "Async Compute" when playing or set Steam launch option `--use-d3d11`. However the latter can potentially cause issues such as microstuttering or it could fail to start altogether. For more information, see [[DirectX11]].

If you are unsure if the current problem arises from a GPU driver issue, you can request the user to give you a "kernel log" - a GPU reset will be logged there and explicitly called out by the kernel and is therefore easy to read out.

`kernel: [drm:amdgpu_mes_reset_legacy_queue [amdgpu]] *ERROR* failed to reset legacy`
`queue kernel: amdgpu 0000:03:00.0: amdgpu: Ring gfx_0.0.0 reset failure`
`kernel: amdgpu 0000:03:00.0: amdgpu: GPU reset begin!`
# GPU Reset with RX 7900 XTX
An older error that aligns with this problem is the GPU reset that occured with older Versions of Mesa3D. 

There have been several fixes to adress this issue:

* https://docs.mesa3d.org/relnotes/24.0.4.html
* https://docs.mesa3d.org/relnotes/24.1.0.html

Users should use newer versions of Mesa3D so this shouldn't be a problem anymore, but will be listed here in case it occurs again or a user actually uses an old version of Mesa.
# ComfyUI-RealESRGAN_Upscaler [![ComfyUI - Homepage](https://img.shields.io/badge/ComfyUI-Homepage-aa00ee)](https://github.com/comfyanonymous/ComfyUI) [![ComfyUI - Manager](https://img.shields.io/badge/ComfyUI-Manager-2aeeef)](https://github.com/ltdrdata/ComfyUI-Manager)

> [!IMPORTANT]  
> <p align="justify">🚧 This documentation is still under 
> construction. The development of the upscaler is a ongoing 
> activity. There might be small differenes in comparison of 
> node and documentation.</p>

> [!CAUTION]
> <p align="justify">Please note, that the node will run, only
> if an error in one Python package file is fixed. See the 
> related section for informations on this topic.</p> 

# Preface

<p align="justify">This node uses the RealESRGAN model from
xinntao [1]. This is my personal favourite upscaling model and 
upscaling approach.</p>

## Whats New

<p align="justify">Yesterday I added a bunch of things to the node.
Now the node is a little bit more complicated than before. On the 
other hand side the node considers now everything which is possible
to do with the node.</p>

## Upscaling

<p align="justify">One can set the scaling factor in steps of 0.1
in the node. For the moment there is no known limit for the scaling
factor. I used for example an unrealistic scaling factor of 30.0 
for upscaling of a test image. The limiting factor is in this case 
the size of the image file.</p>

## Node Preview

<p align="justify">Figure 1 shows the node preview. Input is an image. 
Main output is the upscaled image. In addition to this one can output
the local installation with respect to the GPUs. In case of an error
the error can be printed too.</p>

<img src="./images/node_preview.png" alt="node preview" width="512">
<p><i>Figure 1: Main node preview</i></p>

## Node Parameter
The node has following parameter

+ scale_factor (FLOAT)
+ tile_number (INT)
+ tile_pad (INT)
+ pre_pad (INT)
+ fp_format (STRING)
+ denoise (FLOAT)
+ netscale (INT)
+ gpu_id (LIST)
+ model (LIST)

## What the Node Does

The node can upscale images which have following formats

- JPG/JPEG
- PNG
- WEBP

## Workflow Preview

Figure 2 shows the example workflow preview.

<img src="./images/workflow_preview.png" alt="node preview" width="1024">
<p><i>Figure 2: Workflow preview</i></p>

Figure 3 shows the example workflow preview.

<img src="./images/workflow_error_preview.png" alt="node preview" width="1024">
<p><i>Figure 3: Workflow preview</i></p>

## Installation

<p align="justify">Use the ComfyUI Manager for the installation.
Use my nick 'zentrocdot' or for 'ComfyUI_realESRGAN_Upscaler'</p>

## Known Problems

While first run I got an error message that the installation
of the node failed. After first investigation I found the 
problem. Fix for the moment is as follows. Go into directory
ComfyUI. Then search for a file.

<code>find -name "degradations.py"</code>

This looks like.

<code>./venv/lib/python3.10/site-packages/basicsr/data/degradations.py</code>

Open the file e.g.

<code>nano ./venv/lib/python3.10/site-packages/basicsr/data/degradations.py</code>

and change

<code>from torchvision.transforms.functional_tensor import rgb_to_grayscale</code>

to

<code>from torchvision.transforms.functional import rgb_to_grayscale</code>


After that, the node will work.

## Bug Fixing

in the directory is a file called fix.bash. This can be used to fix
the bug in the Python package.

## Error Screen

While working on the node I have also provoked errors for testing purposes. 
When the number of netscale is not matching the value of the model's
netscale one got an error. 

![Bildschirmfoto vom 2025-02-09 08-57-01](https://github.com/user-attachments/assets/03771469-3a59-4115-baba-a362b60d20fb)

<p><i>Figure 2: Error message preview</i></p>

<p align="justify">The error led to unexpected behaviour of the node.
This was the reason to rethink the programming. Now I catch the error
Over the output ERROR one can make such an error visible. To prevent 
misleading results the output is an empty image with text.</p> 

## Limitations

to-do ...

## To-Do

<p align="justify">There are a plenty of things to to</p>

## Example Using Converted Models

![Bildschirmfoto vom 2025-02-09 15-56-44](https://github.com/user-attachments/assets/6d89033e-65df-479e-87fc-18dcad30c418)



![Bildschirmfoto vom 2025-02-09 15-57-03](https://github.com/user-attachments/assets/15f0a4e3-9df2-49b1-bcb8-e90597284240)



## Credits

<p align="justify">Special credits goes to xinntao (Xintao Wang) for his excellent 
work on ESRGAN and RealESRGAN models The results achieved are quite impressive.</p> 

## Final Words

Have fun. Be inspired!

# Reference

[1] https://github.com/xinntao/Real-ESRGAN

[2] https://github.com/xinntao/Real-ESRGAN/blob/master/docs/model_zoo.md

[3] https://arxiv.org/abs/2107.10833

[3] https://github.com/zentrocdot/ESRGAN_RRBD_CONVERTER

[4] https://github.com/ltdrdata/ComfyUI-Manager

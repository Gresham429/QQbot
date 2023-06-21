import os
import io
import warnings
import base64

from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
import numpy as np
from torchvision.transforms import GaussianBlur

from config.config import STABILITY_API_KEY

# Our Host URL should not be prepended with "https" nor should it have a trailing slash.
os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'

# Sign up for an account at the following link to get an API Key.
# https://dreamstudio.ai/

# Click on the following link once you have created an account to be taken to your API Key.
# https://dreamstudio.ai/account

# Paste your API Key below.

os.environ['STABILITY_KEY'] = STABILITY_API_KEY

# Set up our connection to the API.
stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'],  # API Key reference.
    verbose=True,  # Print debug messages.
    engine="stable-diffusion-xl-beta-v2-2-2",  # Set the engine to use for generation.
    # Available engines: stable-diffusion-v1 stable-diffusion-v1-5 stable-diffusion-512-v2-0 stable-diffusion-768-v2-0
    # stable-diffusion-512-v2-1 stable-diffusion-768-v2-1 stable-diffusion-xl-beta-v2-2-2 stable-inpainting-v1-0 stable-inpainting-512-v2-0
)


def from_text_to_image(requirement: str) -> object:
    # Set up our initial generation parameters.
    answers = stability_api.generate(
        prompt="赛博朋克的风格：" + requirement,
        # seed=992446758,  # seed identifies the unique image, that means, the image in the same seed are same
        steps=30,  # Amount of inference steps performed on image generation. Defaults to 30.
        cfg_scale=8.0,  # Influences how strongly your generation is guided to match your prompt.
        # Setting this value higher increases the strength in which it tries to match your prompt.
        # Defaults to 7.0 if not specified.
        width=768,  # Generation width, defaults to 512 if not included.
        height=512,  # Generation height, defaults to 512 if not included.
        samples=1,  # Number of images to generate, defaults to 1 if not included.
        sampler=generation.SAMPLER_K_DPMPP_2M  # Choose which sampler we want to denoise our generation with.
        # Defaults to k_dpmpp_2m if not specified. Clip Guidance only supports ancestral samplers.
        # (Available Samplers: ddim, plms, k_euler, k_euler_ancestral, k_heun, k_dpm_2, k_dpm_2_ancestral, k_dpmpp_2s_ancestral, k_lms, k_dpmpp_2m, k_dpmpp_sde)
    )

    # Set up our warning to print to the console if the adult content classifier is tripped.
    # If adult content classifier is not tripped, save generated images.
    seed = 0
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again.")
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                img.save(".\\image\\" + str(
                    artifact.seed) + "text-image.png")  # Save our generated images with their seed number as the filename.
                seed = artifact.seed

    file_path = ".\\image\\" + str(seed) + "text-image.png"

    # 读取生成的图片文件,转换为Base64编码并返回
    with open(file_path, "rb") as file:
        image_data = file.read()
    return base64.b64encode(image_data).decode("utf-8")


def from_image_to_image(img: bytes) -> object:
    image = Image.open(io.BytesIO(img))

    # 调整图像尺寸为64的倍数
    new_width = 768
    new_height = 512
    resized_image = image.resize((new_width, new_height))

    answers = stability_api.generate(
        prompt="将照片二次元可爱化",



        init_image=resized_image,  # Assign our previously generated img as our Initial Image for transformation.
        start_schedule=0.6,  # Set the strength of our prompt in relation to our initial image.
        # seed=54321,   # If attempting to transform an image that was previously generated with our API,
                        # initial images benefit from having their own distinct seed rather than using the seed of the original image generation.
        steps=50,  # Amount of inference steps performed on image generation. Defaults to 30.
        cfg_scale=7.0,  # Influences how strongly your generation is guided to match your prompt.
        # Setting this value higher increases the strength in which it tries to match your prompt.
        # Defaults to 7.0 if not specified.
        width=768,  # Generation width, defaults to 512 if not included.
        height=512,  # Generation height, defaults to 512 if not included.
        sampler=generation.SAMPLER_K_DPMPP_2M  # Choose which sampler we want to denoise our generation with.
        # Defaults to k_lms if not specified. Clip Guidance only supports ancestral samplers.
        # (Available Samplers: ddim, plms, k_euler, k_euler_ancestral, k_heun, k_dpm_2, k_dpm_2_ancestral, k_dpmpp_2s_ancestral, k_lms, k_dpmpp_2m, k_dpmpp_sde)
    )

    # Set up our warning to print to the console if the adult content classifier is tripped.
    # If adult content classifier is not tripped, save generated image.
    seed = 0
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again.")
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                img.save(".\\image\\" + str(
                    artifact.seed) + "image-image.png")  # Save our generated image with its seed number as the filename and the 2-img2img suffix so that we know this is our transformed image.
                seed = artifact.seed

    file_path = ".\\image\\" + str(seed) + "image-image.png"

    # 读取生成的图片文件,转换为Base64编码并返回
    with open(file_path, "rb") as file:
        image_data = file.read()
    return base64.b64encode(image_data).decode("utf-8")

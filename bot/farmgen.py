from .config import FARMGEN_BASE
import urllib.parse

BASE_DESC = "мультяшно-реалистичная ферма в стиле Pixar, яркая, зелёное поле, красный амбар, забор, животные, солнце, голубое небо"

def get_farm_img_url():
    safe_prompt = urllib.parse.quote(BASE_DESC)
    return f"{FARMGEN_BASE}{safe_prompt}?width=512&height=512&nologo=true"

from google import genai
from config import API_KEY
client = genai.Client(api_key=API_KEY)

def extract_receipt(image_bytes: bytes):
    import PIL.Image
    import io
    image = PIL.Image.open(io.BytesIO(image_bytes))
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=["Extract item, cost and category from this receipt. Return JSON only with keys: item, cost, category", image]
    )
    return response.text
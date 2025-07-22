

from PIL import Image, ImageDraw, ImageFont

# === Chemins ===
base_image_path = "img/Lancelot_Banniere_Transparent.png"
font_path = "fonts/Jacquard24Charted-Regular.ttf"  # Assure-toi que ce fichier existe
output_path = "img/Lancelot_Medieval_Jacquard.png"

# === Paramètres du texte ===
text = "Lancelot en prose"
font_size = 48
padding_top = 120  # Espace au-dessus pour le texte

# === Charger la bannière de base ===
base = Image.open(base_image_path).convert("RGBA")

# === Créer une nouvelle image avec espace en haut ===
new_width = base.width
new_height = base.height + padding_top
final_img = Image.new("RGBA", (new_width, new_height), (255, 255, 255, 0))

# === Coller la bannière dans le bas ===
final_img.paste(base, (0, padding_top), base)

# === Charger la police ===
try:
    font = ImageFont.truetype(font_path, font_size)
except IOError:
    raise Exception(f"⚠️ Police introuvable : {font_path}. Assure-toi que le fichier est bien présent.")

# === Préparer dessin ===
draw = ImageDraw.Draw(final_img)

# === Calculer la taille du texte avec textbbox ===
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# === Position centrée ===
x = (new_width - text_width) // 2
y = (padding_top - text_height) // 2

# === Dessiner le texte (avec ombre) ===
draw.text((x + 2, y + 2), text, font=font, fill=(0, 0, 0, 80))  # Ombre
draw.text((x, y), text, font=font, fill=(60, 30, 10, 255))      # Texte principal

# === Sauvegarde ===
final_img.save(output_path, "PNG")
print(f"✅ Image générée : {output_path}")

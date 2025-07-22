from PIL import Image

# === Chemins vers tes images ===
image_gauche_path = "img/lancelot.png"
image_droite_path = "img/par_maints.png"
output_path = "img/Lancelot_Banniere_Transparent.png"

# === Ouvrir les images en mode RGBA ===
img_gauche = Image.open(image_gauche_path).convert("RGBA")
img_droite = Image.open(image_droite_path).convert("RGBA")

# === Harmoniser la hauteur ===
target_height = min(img_gauche.height, img_droite.height)
ratio_gauche = target_height / img_gauche.height
ratio_droite = target_height / img_droite.height

img_gauche_resized = img_gauche.resize((int(img_gauche.width * ratio_gauche), target_height))
img_droite_resized = img_droite.resize((int(img_droite.width * ratio_droite), target_height))

# === Créer une image finale transparente ===
total_width = img_gauche_resized.width + img_droite_resized.width
final_image = Image.new("RGBA", (total_width, target_height), (255, 255, 255, 0))

# === Coller les deux images ===
final_image.paste(img_gauche_resized, (0, 0), img_gauche_resized)
final_image.paste(img_droite_resized, (img_gauche_resized.width, 0), img_droite_resized)

# === Sauvegarder ===
final_image.save(output_path, "PNG")
print(f"Image créée : {output_path}")


from PIL import Image, ImageDraw, ImageFont

# === Charger la bannière de base ===
base = Image.open("img/Lancelot_Banniere_Transparent.png").convert("RGBA")

# === Créer une nouvelle image avec de l'espace pour le titre ===
padding_top = 120
new_img = Image.new("RGBA", (base.width, base.height + padding_top), (255, 255, 255, 0))
new_img.paste(base, (0, padding_top), base)

# === Charger la police Jacquard 24 Charted ===
font_path = "fonts/Jacquard24Charted-Regular.ttf"
font_size = 48

try:
    font = ImageFont.truetype(font_path, font_size)
except IOError:
    raise Exception("⚠️ Vérifie que la police est bien à l’emplacement spécifié.")

# === Ajouter le titre médiéval ===
draw = ImageDraw.Draw(new_img)
text = "La légende de Lancelot du Lac"
text_width, text_height = draw.textsize(text, font=font)
x = (new_img.width - text_width) // 2
y = (padding_top - text_height) // 2

# Optionnel : ombre
draw.text((x + 2, y + 2), text, font=font, fill=(0, 0, 0, 80))

# Texte principal
draw.text((x, y), text, font=font, fill=(60, 30, 10, 255))

# === Sauvegarde ===
output_path = "img/Lancelot_Medieval_Jacquard.png"
new_img.save(output_path, "PNG")
print(f"✅ Image sauvegardée sous : {output_path}")

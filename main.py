def create_prompt(subject, color, use):
    return f"/imagine prompt: a {subject}, with a {color} background, {use}"

uses = [
    "--niji 5, low resolution",
    "--niji 5, high resolution",
    "as an art-piece, low resolution",
    "as an art-piece, high resolution",
    "as a tattoo template, low resoltution",
    "as a tattoo template, high resolution",
    "as a cartoon, low resolution",
    "as a cartoon, high resolutuon",
    "as clip art for children audience, low resolution",
    "as clip art for children audience, high resolution",
    "as clip art for corporate documentation use, low resolutuon",
    "as clip art for corporate documentation use, high resolution",
    "as  a corporate logo for professional services business, low resolution",
    "as  a corporate logo for professional services business, high resolution",
    "as a corporate logo for a canned-food business, low resolutuon",
    "as a corporate logo for a canned-food business, high resolutuon",
    "as a corporate logo for a clothing business, low resolution",
    "as a corporate logo for a clothing business, high resolution",
    "as clip art for gift-card use, low resolution",
    "as clip art for gift-card use, high resolution",
    "as iconography, low resolution",
    "as iconography, high resolution",
    "as an emoji, low resolution",
    "as an emoji, high resolution",
    "as a racing-car logo, low resolution",
    "as a racing-car logo, high resolution",
    "as a sports-team logo, low resolution",
    "as a sports-team logo, high resolution", 
]

for use in uses:
    print(create_prompt('red rose', 'white', use))

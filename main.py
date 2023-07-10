def create_prompt(subject, color, use):
    return f"/imagine prompt: a {subject}, with a {color} background, {use}"

uses = [
    "--niji 5",
    "as an art-piece",
    "as a tattoo template",
    "as a cartoon",
    "as clip art for children audience",
    "as clip art corporate documentation use",
    "as corporate logo for professional services business",
    "as corporate logo for canned-food business",
    "as corporate logo for a clothing business",
    "as clip art for gift-card use",
    "as iconography",
    "as an emoji",
    "as a racing-car logo",
    "as a football-team logo"
]

for use in uses:
    print(create_prompt('red rose', 'white', use))

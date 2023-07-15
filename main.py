def create_prompt(subject, backgroundAdjective, use):
    return f"/imagine prompt: a {subject}, with a {backgroundAdjective} background, {use}"

subject = input("Object name: ")
backgroundAdjective = input("Background color or other adjective applicable to a background: ")

uses = [
    "low resolution, --niji 5",
    "medium resolution, --niji 5",
    "high resolution, --niji 5",
    "as an art-piece, low resolution",
  "as an art-piece, medium resolution",
    "as an art-piece, high resolution",
    "as a tattoo template, low resoltution",
  "as a tattoo template, medium resolution",
    "as a tattoo template, high resolution",
    "as a cartoon, low resolution",
    "as a cartoon, medium resolution",
    "as a cartoon, high resolutuon",
    "as clip art for children audience, low resolution",
  "as clip art for children audience, medium resolution",
    "as clip art for children audience, high resolution",
    "as clip art for corporate documentation use, low resolutuon",
  "as clip art for corporate documentation use, medium resolution",
    "as clip art for corporate documentation use, high resolution",
    "as  a corporate logo for professional services business, low resolution",
  "as  a corporate logo for professional services business, medium resolution",
    "as  a corporate logo for professional services business, high resolution",
    "as a corporate logo for a canned-food business, low resolutuon",
  "as a corporate logo for a canned-food business, medium resolution",
    "as a corporate logo for a canned-food business, high resolutuon",
    "as a corporate logo for a clothing business, low resolution",
  "as a corporate logo for a clothing business, medium resolution",
    "as a corporate logo for a clothing business, high resolution",
    "as clip art for gift-card use, low resolution",
  "as clip art for gift-card use, medium resolution",
    "as clip art for gift-card use, high resolution",
    "as iconography, low resolution",
    "as iconography, medium resolution",
    "as iconography, high resolution",
    "as an emoji, low resolution",
    "as an emoji, medium resolution",
    "as an emoji, high resolution",
    "as a racing-car logo, low resolution",
    "as a racing-car logo, medium resolution",
    "as a racing-car logo, high resolution",
    "as a sports-team logo, low resolution",
    "as a sports-team logo, medium resolution",
    "as a sports-team logo, high resolution", 
    "as a badge for an astronaut uniform, low resolution",
    "as a badge for an astronaut uniform, medium resolution",
  "as a badge for an astronaut uniform, high resolution",
  "as a badge for a sports-team uniform, low resolution, --niji 5",
  "as a badge for a sports-team uniform, medium resolution, --niji 5",
  "as a badge for a sports-team uniform, high resolution, --niji 5",
    "engaged with by a beautiful-young-asian woman wearing a tight dress, woman looking at camera with a big white smile and flirty eyes, low resolution",
    "engaged with by a beautiful-young-asian woman wearing a tight dress, woman looking at camera with a big white smile and flirty eyes, medium resolution",
    "engaged with by a beautiful-young-asian woman wearing a tight dress, woman looking at camera with a big white smile and flirty eyes, high resolution",
  "engaged with by a beautiful-young-asian woman wearing a tight dress, woman looking at camera with a big white smile and flirty eyes, low resolution, --niji 5",
  "engaged with by a beautiful-young-asian woman wearing a tight dress, woman looking at camera with a big white smile and flirty eyes, medium resolution, --niji 5",
  "engaged with by a beautiful-young-asian woman wearing a tight dress, woman looking at camera with a big white smile and flirty eyes, high resolution, --niji 5",
  "engaged with by a handsome businessman dressed formally, man looking at camera with a big white smile and flirty eyes, low resolution",
  "engaged with by a handsome businessman dressed formally, man looking at camera with a big white smile and flirty eyes, medium resolution",
  "engaged with by a handsome businessman dressed formally, man looking at camera with a big white smile and flirty eyes, high resolution",
  "engaged with by a handsome businessman dressed formally, man looking at camera with a big white smile and flirty eyes, low resolution, --niji 5",
  "engaged with by a handsome businessman dressed formally, man looking at camera with a big white smile and flirty eyes, medium resolution, --niji 5",
  "engaged with by a handsome businessman dressed formally, man looking at camera with a big white smile and flirty eyes, high resolution, --niji 5",
  "as a pog artwork, low resolution",
  "as a pog artwork, medium resolution",
  "as a pog artwork, high resolution",
  "as a hat-pin artwork, low resolution",
  "as a hat-pin artwork, medium resolution",
  "as a hat-pin artwork, high resolution",
  "as a symbol to be place in-line with text, low resolution",
  "as a symbol to be place in-line with text, medium resolution",
  "as a symbol to be place in-line with text, high resolution",
  "as artwork for a mug, low resolution",
  "as artwork for a mug, medium resolution",
  "as artwork for a mug, high resolution",
  "as a mug, low resolution, --niji 5",
  "as a mug, medium resolution, --niji 5",
  "as a mug, high resolution, --niji 5",
  "as a mug, low resolution, --niji 5",
  "on its own, as a cartoon, low resolution, --s 500",
  "on its own, as a cartoon, medium resolution, --s 500",
  "on its own, as a cartoon, high resolution, --s 500",
  "as a cartoon, low resolution",
  "as a cartoon, medium resolution",
  "as a cartoon, high resolution",
  "as grimdark fantasy digital art, low resolution, --s 500",
  "as grimdark fantasy digital art, medium resolution, --s 500",
  "as grimdark fantasy digital art, high resolution, --s 500",
  "as grimdark fantasy digital art, low resolution, --s 1000",
  "as grimdark fantasy digital art, medium resolution, --s 1000",
  "as grimdark fantasy digital art, high resolution, --s 1000",
  "as a modern art-piece statute, ultra-photorealistic, low resolution",
  "as a modern art-piece statute, ultra-photorealistic, medium resolution",
  "as a modern art-piece statute, ultra-photorealistic, high resolution"
  
]


for use in uses:
    print(create_prompt(subject, backgroundAdjective, use))
    #print, but add "--niji 5" to the end of the prompt"
      #print(create_prompt(subject, backgroundAdjective, use, "--niji 5"))
    #print, but add ", low resolution" to the end of the prompt"
      #print(create_prompt(subject, backgroundAdjective, use, ", low resolution"))
    #print, but add ", medium resolution" to the end of the prompt"
      #print(create_prompt(subject, backgroundAdjective, use, ", medium resolution"))
    #print, but add ", high resolution" to the end of the prompt"
      #print(create_prompt(subject, backgroundAdjective, use, ", high resolution"))

# 
##

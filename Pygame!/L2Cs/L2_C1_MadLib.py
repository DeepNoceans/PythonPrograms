print("Mad Lib Game")
print("Enter answers to the following prompts\n")

guy = input("Name of a brave knight: ")
girl = input("Name of princess: ")
clan = input("Cool/Heroic animal (plural): ")
enemy = input("Evil animal (plural): ")
hours = input("Number from 2-5: ")
weapon = input("Medival weapon (singular)(close combat): ")
horse = input("Name of horse: ")
metal = input("Type of metal: ")
adjective = input("Weird adjective: ")
story = "\nGUY the brave knight was playing cards with the\n" +\
        "local weaponsmith when we was suddenly called to the duty of\n" +\
        "saving princess GIRL. Princess GIRL was captured by\n" +\
        "the evil kingdom of ENEMY only HOURS hours ago. In honor\n"+\
        "of his kingdom, the kingdom of CLAN, GUY the knight grabbed\n"+\
        "his WEAPON and headed off towards the kingdom of ENEMY\n" +\
        "on his trusty steed, HORSE. With his shiny WEAPON and his\n"+\
        "gleaming armor made of METAL, GUY barged into the evil\n"+\
        "kingdom's castle. He glared at his ADJ enemies with absolute \n"+\
        "hatred. He saw princess GIRL tied up next to the fat king of \n"+\
        "the kingdom of ENEMY. The knight raised his WEAPON and charged\n"+\
        "at the king on the throne. He plowed through the crowds of ADJ people\n"+\
        "effortlessly with his armor made of METAL. Before the king could escape\n"+\
        "from his throne, the knight leaped into the air with his sharp WEAPON held up \n"+\
        "above his head, pointing downwards with uncontrollable rage. The knight slowly\n"+\
        "soured above the helpless crowd as if he were in slow motion. The king, too\n"+\
        "large to escape his throne in time, could only say his last prayers. As the brave\n"+\
        "Descended with no other wish than the eradication of the man behind the imprisonment\n"+\
        "of the beautiful princess GIRL. The final blow was about the commence, when suddenly, \n"+\
        "the story ended."
       

story = story.replace("GUY", guy)
story = story.replace("GIRL", girl)
story = story.replace("CLAN",clan)
story = story.replace("ENEMY", enemy)
story = story.replace("HOURS", hours)
story = story.replace("WEAPON",weapon)
story = story.replace("HORSE", horse)
story = story.replace("METAL", metal)
story = story.replace("ADJ", adjective)


print(story)








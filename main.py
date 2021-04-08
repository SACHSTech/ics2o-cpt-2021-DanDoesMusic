import pygame
import random
""" 
A basic pygame template
"""
 
 
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)
GREEN    = (0,255,27,255)
TEAL     = (45,164,168,)


pygame.init()
  
# Set the width and height of the screen [width, height]
size = (1366,768)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
#---images---#
bedroom = pygame.image.load("bedroom.jpg").convert_alpha ()
bedroom = pygame.transform.scale(bedroom,(1366,768))
rest = pygame.image.load("Main_rest.jpg").convert_alpha ()
rest = pygame.transform.scale(rest,(366,468))
Main = pygame.image.load("Main_char.jpg").convert_alpha ()
Main = pygame.transform.scale(Main,(366,468))
Patch_2 = pygame.image.load("2_eyepatch.jpg").convert_alpha ()
Patch_2= pygame.transform.scale(Patch_2,(366,468))
Main_fight = pygame.image.load("Main_fight.jpg").convert_alpha ()
Main_fight = pygame.transform.scale(Main_fight,(366,468))
Patch_fight = pygame.image.load("2_fight.jpg").convert_alpha ()
Patch_fight = pygame.transform.scale(Patch_fight,(366,468))
Doctor = pygame.image.load("Felica.jpg").convert_alpha ()
Doctor = pygame.transform.scale(Doctor,(366,468))
Doc_rest = pygame.image.load("Felica_rest.jpg").convert_alpha ()
Doc_rest = pygame.transform.scale(Doc_rest,(366,468))
Doc_main = pygame.image.load("Felica.jpg").convert_alpha ()
Doc_main = pygame.transform.scale(Doc_main,(366,468))
Doc_fight = pygame.image.load("Felica_fight.png").convert_alpha ()
Doc_fight = pygame.transform.scale(Doc_fight,(366,468))
Magic = pygame.image.load("Alice.jpg").convert_alpha ()
Magic = pygame.transform.scale(Magic,(366,468))
Magic_fight = pygame.image.load("Alice_cast.jpg").convert_alpha ()
Magic_fight = pygame.transform.scale(Magic_fight,(366,468))
Magic_rest = pygame.image.load("Alice_rest.jpg").convert_alpha ()
Magic_rest = pygame.transform.scale(Magic_rest,(366,468))
cow = pygame.image.load("cow.png").convert_alpha ()
cow = pygame.transform.scale(cow,(366,468))
cow.set_colorkey(RED)
slime = pygame.image.load("slime.png").convert_alpha ()
slime = pygame.transform.scale(slime,(366,468))
wolf = pygame.image.load("wolf.png").convert_alpha ()
wolf = pygame.transform.scale(wolf,(366,468))
skeleton = pygame.image.load("skeleton.png").convert_alpha ()
skeleton = pygame.transform.scale(skeleton,(366,468))
swordsman = pygame.image.load("swordsman.png").convert_alpha ()
swordsman = pygame.transform.scale(swordsman,(366,468))
wizard = pygame.image.load("wizard.png").convert_alpha ()
wizard = pygame.transform.scale(wizard,(400,950))
flame = pygame.image.load("flame.png").convert_alpha ()
flame = pygame.transform.scale(flame,(366,468))
inn = pygame.image.load("inn.jpg").convert_alpha ()
inn = pygame.transform.scale(inn,(1366,768))
Main_2 = pygame.image.load("Main_2.jpg").convert_alpha ()
Main_2 = pygame.transform.scale(Main_2,(366,468))
winter = pygame.image.load("winter.jpg").convert_alpha ()
winter = pygame.transform.scale(winter,(1366,768))
die = pygame.image.load("death.png").convert_alpha ()
die = pygame.transform.scale(die,(1366,768))
grass = pygame.image.load("grass.jpg").convert_alpha ()
grass = pygame.transform.scale(grass,(1366,768))
grass_2 = pygame.image.load("grass_2.jpg").convert_alpha ()
grass_2 = pygame.transform.scale(grass_2,(1366,768))
grass_3 = pygame.image.load("grass_3.jpg").convert_alpha ()
grass_3 = pygame.transform.scale(grass_3,(1366,768))
castle_out = pygame.image.load("castle_out.jpg").convert_alpha ()
castle_out = pygame.transform.scale(castle_out,(1366,768))
castle_in = pygame.image.load("castle_in.jpg").convert_alpha ()
castle_in = pygame.transform.scale(castle_in,(1366,768))

Main.set_colorkey(GREEN)
Main_2.set_colorkey(GREEN)
Doctor.set_colorkey(GREEN)
Magic.set_colorkey(TEAL)
Main_fight.set_colorkey(GREEN)
Magic_fight.set_colorkey(TEAL)
Doc_fight.set_colorkey(TEAL)
Doc_rest.set_colorkey(GREEN)
slime.set_colorkey(GREEN)
Magic_rest.set_colorkey(TEAL)
cow.set_colorkey(RED)
Player_health = 300
cow_health = 50
slime_health = 55
wolf_health = 60
skeleton_health = 75
sword_health = 90
wizard_health = 100


# --- text----#
font = pygame.font.SysFont("Arial",18,True)
page_1_text = font.render("its gonna be a long day... OF GAMING I LOVE SATURDAYS sylvestor said as he rolled out of bed and got dressed and adorned his eyepatch",True,BLACK) 
page_2_text = font.render("as our main character walked up to the computer he felt somthing was not right but thought nothing of it and turned it on",True,BLACK) 
page_3_text = font.render("I love this game he said as he opened minecraft and turned on his shaders until a smoking smell portruded his pc but he oaid no mind to it",True,BLACK)
page_4_text = font.render("BOOOM the computer went as his fan broke down and his GPU exploded and the glass case ",True,BLACK)
page_4_b_text = font.render("shattered but he was un harmed adn yet he had collapsed due to shock and his vison went black",True,BLACK)   
page_5_text = font.render("as his eyes open and things start to focous he hears Oh you're finally awake he hears ",True,BLACK) 
page_6_text = font.render("you just appeared in my closet and were out for hours and had a blistering fever where are you from",True,BLACK) 
page_7_text = font.render("I am Slyvester and I'm from a small town in canada called lemmington",True,BLACK) 
page_8_text = font.render("Well its very nice to meet you, You're gonna need some money so come with me we have a few jobs to do",True,BLACK) 
page_9_text = font.render("were gonna have to walk just a bit but we shouldn't have a hard time with this we are meeting my friend there",True,BLACK) 
page_10_text = font.render("HIIIIIIIIIIIIIIIIIIIIIIIIIIIII the figure said before she raised her hat and cloak Im Alice and I am a magican ",True,BLACK)
page_11_text = font.render("anyway we are gonna fight that cow over there ",True,BLACK)
page_14_text = font.render("wait a minute sylvester said why did the cow turn into a RTX 3090  as he pulled the part from the fire and put it in his bag",True,BLACK)
page_15_text = font.render("this is a top of the line computer part im taking this home with me",True,BLACK)
page_16_text = font.render("computer? whats that the other two said looking bewildered ",True,BLACK)
page_17_text = font.render("Its a migic box you can play games on thats how I died mine exploed trying to play doki doki littriture club",True,BLACK)
page_18_text = font.render("hey that kinda sounds like the name of this game oki doki PC game Alice said looking at the player",True,BLACK)
page_19_text = font.render("wait what the other two said looking confused",True,BLACK)
page_20_text = font.render("never mind Alice said Anyway we gotta fight a few more animals to prepair the scriptures said a hero would visit us and fight the skeleton king",True,BLACK)
page_21_text = font.render("well we better get going there are 5 more fabled beasts ranging in strength and we must slay all 5",True,BLACK)
page_22_text = font.render("but first we rest lets head back to the inn for the night ",True,BLACK)
page_23_text = font.render("and so the next day they went out on the venture",True,BLACK)
page_24_text = font.render("UHHHHHHHHH how much longer is it slyvester said its not too much farther Alice said as they charged farther into the forest",True,BLACK)
page_25_text = font.render("there it is the minty slime of the south the second of 6 evils we must vequish",True,BLACK)
page_27_text = font.render("IT HAPPENED AGAIN sylvester as he pulled a cpu from the fires of the beasts death",True,BLACK)
page_28_text = font.render("these are the main part of computers if we can get one going ill show you what this can do",True,BLACK)
page_29_text = font.render("as they went farther and farther ahead they shared stores and exchanged details of their lives",True,BLACK)
page_30_text = font.render("oh my how much farther up is itwhat are we even looking for ",True,BLACK)
page_31_text = font.render("we are looking for the grand dark wolf simeon",True,BLACK)
page_32_text = font.render("I THINK I SEE IT JUST AHEAD as they cheered in unisin lets do this guys we need to get this done",True,BLACK)
page_34_text = font.render("this time as the beast fell a computer hard disc storage part flew from the beast and into the main characters hands and he quickly put it in his bag ",True,BLACK)
page_35_text = font.render("we have 3 more to go the next 3 are gonna be the toughest there is the boxer of the 3rd circle the swordsman of the 6th and the grand wizard of the 9th circle",True,BLACK)
page_36_text = font.render("they are all in that castle just up ahead ",True,BLACK)
page_37_text = font.render("and as they walked and walked they got there and had to brace themselves for the fights to come",True,BLACK)
page_38_text = font.render("Oh you finnally arrived the skeleton said you DARE oppose ME? you must best me in a true fight 1 on 1",True,BLACK)
page_39_text = font.render("oh you're on sylvester said as the other 2 left the castle awaiting his return ",True,BLACK)
page_41_text = font.render("this time the enemy had not fallen with a boom or flame he spoke softly you have bested me take this as he ",True,BLACK)
page_41_b_text = font.render("hands him RAM and says you deserve it and falls apart",True,BLACK)
page_42_text = font.render("as the bones turned to dust and blew away our hero raced into the next room and was greeted by the swordsman",True,BLACK)
page_43_text = font.render("you bested my friend he was a fool to chalange you on equal footing a real man challanges when they are at the advantage now PERISH",True,BLACK)
page_45_text = font.render("You really are a worthy adversery as he passes a power supply to him before turning to water",True,BLACK)
page_46_text = font.render("then suddenly the wizard apeared from the sky you brute you forced your way through lets see if you are as tactical as you say you are ",True,BLACK)
page_48_text = font.render("this time there was no sound as he fell a motherboard was placed into sylvesters bag as he was teleported back to the others ",True,BLACK)
page_49_text = font.render("how did it go Alice said It was great I got all the parts for a computer lets put it together then we can play that oki doki game you talked about  ",True,BLACK)
page_49_b_text = font.render("as they all looked at the camera awkwardly  ",True,BLACK)
page_50_text = font.render("anyway lets get this together ",True,BLACK)
page_51_text = font.render("THE END",True,BLACK)
















page_variable = 1
eye_variable = 1
# -------- Main Program Loop -----------
died = False
while not done:
    # --- Main event loop            
    roll = False
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if died:
                    page_variable = 1
                else:
                    page_variable +=1
            if event.key == pygame.K_q:
                roll = True


    # --- Game logic should go here
    if page_variable == 13:
        if roll:
            player_dice = random.randint(1,20)
            npc_dice = random.randint(1,20)
            print(Player_health,cow_health,player_dice,npc_dice)  
            if npc_dice > player_dice:
                Player_health = Player_health -5
            if player_dice > npc_dice:
                cow_health = cow_health -10
        if Player_health <= 0:
            screen.blit(die,(0,0))
            died = True
        if cow_health <= 0:
            print("your did it")

    if page_variable == 26:
        health = 25
        if roll:
            player_dice = random.randint(1,20)
            npc_dice = random.randint(1,20)
            print(Player_health,slime_health,player_dice,npc_dice)  
            if npc_dice > player_dice:
                Player_health = Player_health -5
            if player_dice > npc_dice:
                slime_health = slime_health -10
        if Player_health <= 0:
            screen.blit(die,(0,0))
            died = True
        if slime_health <= 0:
            print("your did it")
    if page_variable == 33:
        player_health = 100
        if roll:
            player_dice = random.randint(1,20)
            npc_dice = random.randint(1,20)
            print(Player_health,wolf_health,player_dice,npc_dice)  
            if npc_dice > player_dice:
                Player_health = Player_health -5
            if player_dice > npc_dice:
                wolf_health = wolf_health -10
        if Player_health <= 0:
            screen.blit(die,(0,0))
            died = True
        if slime_health <= 0:
            print("your did it")
    if page_variable == 40:
        player_health = 100
        if roll:
            player_dice = random.randint(1,20)
            npc_dice = random.randint(1,20)
            print(Player_health,skeleton_health,player_dice,npc_dice)  
            if npc_dice > player_dice:
                Player_health = Player_health -15
            if player_dice > npc_dice:
                skeleton_health = skeleton_health -15
        if Player_health <= 0:
            screen.blit(die,(0,0))
            died = True
        if skeleton_health <= 0:
            print("your did it")
    if page_variable == 44:
        player_health = 100
        if roll:
            player_dice = random.randint(1,20)
            npc_dice = random.randint(1,20)
            print(Player_health,sword_health,player_dice,npc_dice)  
            if npc_dice > player_dice:
                Player_health = Player_health -25
            if player_dice > npc_dice:
                sword_health = sword_health -10
        if Player_health <= 0:
            screen.blit(die,(0,0))
            died = True
        if sword_health <= 0:
            print("your did it")
    if page_variable == 47:
        player_health = 100
        if roll:
            player_dice = random.randint(1,20)
            npc_dice = random.randint(1,20)
            print(Player_health,wizard_health,player_dice,npc_dice)  
            if npc_dice > player_dice:
                Player_health = Player_health -25
            if player_dice > npc_dice:
                wizard_health = wizard_health -15
        if Player_health <= 0:
            screen.blit(die,(0,0))
            died = True
        if wizard_health <= 0:
            print("your did it")

    # First, clear the screen to white or whatever background colour. 
    # Don't put other drawing commands above this, or they will be erased with this command.


    if page_variable == 1: 
        screen.blit(bedroom,(0,0))
        screen.blit(rest,[600,300,600,200])
        rest.set_colorkey(GREEN)
        pygame.draw.rect(screen,WHITE,[0, 600, 1300, 200])
        screen.blit(page_1_text,(0,600))
    elif page_variable == 2:
        screen.blit(Patch_2,[1000,200,600,600])
        screen.blit(bedroom,(0,0))
        screen.blit(Main,[1000,200,600,600])
        Main.set_colorkey(GREEN)
        pygame.draw.rect(screen,WHITE,[0, 600, 1000, 200])
        screen.blit(page_2_text,(0,600))
    elif page_variable == 3:
        screen.blit(Patch_2,[1000,200,600,600])
        screen.blit(bedroom,(0,0))
        screen.blit(Main,[600,300,800,200])
        screen.blit(flame,[300,100,100,900])
        Main.set_colorkey(GREEN)
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_3_text,(0,600))
    elif page_variable == 4:
        screen.blit(Patch_2,[1000,200,600,600])
        screen.blit(bedroom,(0,0))
        screen.blit(Main,[600,300,800,200])
        screen.blit(flame,[300,100,100,900])
        Main.set_colorkey(GREEN)
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_4_text,(0,600))
        screen.blit(page_4_b_text,(0,650))
    elif page_variable == 5:
        screen.blit(Patch_2,[1000,200,600,600])
        screen.blit(inn,(0,0))
        screen.blit(Main_2,[780,50,100,000])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_5_text,(0,600))
    elif page_variable == 6:
        screen.blit(Patch_2,[1000,200,600,600])
        screen.blit(inn,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main_2,[780,50,100,000])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_6_text,(0,600))
    elif page_variable == 7:
        screen.blit(Patch_2,[1000,200,600,600])
        screen.blit(inn,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main_2,[780,50,100,000])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_7_text,(0,600))
    elif page_variable == 8:
        screen.blit(inn,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main,[780,50,100,000])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_8_text,(0,600))
    elif page_variable == 9:
        screen.blit(winter,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main,[780,50,100,000])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_9_text,(0,600))
    elif page_variable == 10:
        screen.blit(winter,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main,[780,50,100,000])
        screen.blit(Magic,[600,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_10_text,(0,600))
    elif page_variable == 11:
        screen.blit(winter,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main,[780,50,100,000])
        screen.blit(Magic,[600,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_11_text,(0,600))
    elif page_variable == 12:
        screen.blit(winter,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main,[780,50,100,000])
        screen.blit(Magic,[600,100,500,200])
        screen.blit(cow,[100,100,500,200])
    elif page_variable == 13:
        screen.blit(winter,(0,0))
        screen.blit(Main_fight,[780,50,100,000])
        screen.blit(Magic_fight,[600,100,500,200])
        screen.blit(cow,[100,100,500,200])
        screen.blit(Doc_fight,[400,100,500,200])
    if Player_health <= 0:
        screen.blit(die,(0,0))
    elif page_variable == 14:
        screen.blit(winter,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main,[780,50,100,000])
        screen.blit(Magic,[600,100,500,200])
        screen.blit(flame,[100,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_14_text,(0,600))
    elif page_variable == 15:
        screen.blit(winter,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main,[780,50,100,000])
        screen.blit(Magic,[600,100,500,200])
        screen.blit(flame,[100,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_15_text,(0,600))                 
    elif page_variable == 16:
        screen.blit(winter,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main,[780,50,100,000])
        screen.blit(Magic,[600,100,500,200])
        screen.blit(flame,[100,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_16_text,(0,600))
    elif page_variable == 17:
        screen.blit(winter,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main,[780,50,100,000])
        screen.blit(Magic,[600,100,500,200])
        screen.blit(flame,[100,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_17_text,(0,600))
    elif page_variable == 18:
        screen.blit(winter,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main,[780,50,100,000])
        screen.blit(Magic,[600,100,500,200])
        screen.blit(flame,[100,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_18_text,(0,600))
    elif page_variable == 19:
        screen.blit(winter,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main,[780,50,100,000])
        screen.blit(Magic,[600,100,500,200])
        screen.blit(flame,[100,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_19_text,(0,600))
    elif page_variable == 20:
        screen.blit(winter,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main,[780,50,100,000])
        screen.blit(Magic,[600,100,500,200])
        screen.blit(flame,[100,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_20_text,(0,600))
    elif page_variable == 21:
        screen.blit(winter,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main,[780,50,100,000])
        screen.blit(Magic,[600,100,500,200])
        screen.blit(flame,[100,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_21_text,(0,600))      
    elif page_variable == 22:
        screen.blit(inn,(0,0))
        screen.blit(Main_2,[880,50,100,000])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_22_text,(0,600)) 
    elif page_variable == 23:
        screen.blit(grass  ,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main,[780,50,100,000])
        screen.blit(Magic,[600,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_23_text,(0,600))
    elif page_variable == 24:
        screen.blit(grass  ,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main,[780,50,100,000])
        screen.blit(Magic,[600,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_24_text,(0,600))
    elif page_variable == 25:
        screen.blit(grass  ,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main,[780,50,100,000])
        screen.blit(Magic,[600,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_25_text,(0,600))
    elif page_variable == 26:
        screen.blit(grass  ,(0,0))
        screen.blit(Doc_fight,[400,100,500,200])
        screen.blit(Main_fight,[780,50,100,000])
        screen.blit(Magic_fight,[600,100,500,200])
        screen.blit(slime,[100,100,500,200])
    elif page_variable == 27:
        screen.blit(grass  ,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main,[780,50,100,000])
        screen.blit(Magic,[600,100,500,200])
        screen.blit(flame,[100,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_27_text,(0,600))    
    elif page_variable == 28:
        screen.blit(grass_2,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main,[780,50,100,000])
        screen.blit(Magic,[600,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_28_text,(0,600))  
    elif page_variable == 29:
        screen.blit(grass_2,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main,[780,50,100,000])
        screen.blit(Magic,[600,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_29_text,(0,600)) 
    elif page_variable == 30:
        screen.blit(grass_2,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main,[780,50,100,000])
        screen.blit(Magic,[600,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_30_text,(0,600)) 
    elif page_variable == 31:
        screen.blit(grass_3,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main,[780,50,100,000])
        screen.blit(Magic,[600,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_31_text,(0,600))  
    elif page_variable == 32:
        screen.blit(grass_3,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main,[780,50,100,000])
        screen.blit(Magic,[600,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_32_text,(0,600))
    elif page_variable == 33:
        screen.blit(grass_3,(0,0))
        screen.blit(Doc_fight,[400,310,500,600])
        screen.blit(Main_fight,[780,310,700,600])
        screen.blit(Magic_fight,[600,310,400,600])
        screen.blit(wolf,[100,200,700,200]) 
    elif page_variable == 34:
        screen.blit(grass_3,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main,[780,50,100,000])
        screen.blit(Magic,[600,100,500,200])
        screen.blit(flame,[100,200,700,200]) 
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_34_text,(0,600))
    elif page_variable == 35:
        screen.blit(grass_3,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main,[780,50,100,000])
        screen.blit(Magic,[600,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_35_text,(0,600))
    elif page_variable == 36:
        screen.blit(grass_3,(0,0))
        screen.blit(Doctor,[400,100,500,200])
        screen.blit(Main,[780,50,100,000])
        screen.blit(Magic,[600,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_36_text,(0,600))
    elif page_variable == 37:
        screen.blit(castle_out,(0,0))
        screen.blit(Doctor,[400,310,500,200])
        screen.blit(Main,[780,315,100,000])
        screen.blit(Magic,[600,315,500,200])
        pygame.draw.rect(screen,WHITE,[0, 000, 1400, 200])
        screen.blit(page_37_text,(0,000))
    elif page_variable == 38:
        screen.blit(castle_in,(0,0))
        screen.blit(Doctor,[400,310,500,200])
        screen.blit(Main,[780,315,100,000])
        screen.blit(Magic,[600,315,500,200])
        screen.blit(skeleton,[100,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_38_text,(0,600))
    elif page_variable == 39:
        screen.blit(castle_in,(0,0))
        screen.blit(Main,[780,315,100,000])
        screen.blit(skeleton,[100,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_39_text,(0,600))
    elif page_variable == 40:
        screen.blit(castle_in,(0,0))
        screen.blit(Main,[780,315,100,000])
        screen.blit(skeleton,[100,100,500,200])               
    elif page_variable == 41:
        screen.blit(castle_in,(0,0))
        screen.blit(Main,[780,50,100,000])
        screen.blit(skeleton,[100,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_41_text,(0,600))
        screen.blit(page_41_b_text,(0,650))
    elif page_variable == 42:
        screen.blit(castle_in,(0,0))
        screen.blit(Main,[780,50,100,000])
        screen.blit(swordsman,[100,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_42_text,(0,600))
    elif page_variable == 43:
        screen.blit(castle_in,(0,0))
        screen.blit(Main,[780,50,100,000])
        screen.blit(swordsman,[100,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_43_text,(0,600))
    elif page_variable == 44:
        screen.blit(castle_in,(0,0))
        screen.blit(Main,[780,50,100,000])
        screen.blit(swordsman,[100,100,500,200])
    elif page_variable == 45:
        screen.blit(castle_in,(0,0))
        screen.blit(Main,[780,50,100,000])
        screen.blit(swordsman,[100,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_45_text,(0,600))
    elif page_variable == 46:
        screen.blit(castle_in,(0,0))
        screen.blit(Main,[780,50,100,000])
        screen.blit(wizard,[100,100,500,200])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_46_text,(0,600))
    elif page_variable == 47:
        screen.blit(castle_in,(0,0))
        screen.blit(Main,[780,50,100,000])
        screen.blit(wizard,[100,100,500,200])
    elif page_variable == 48:
        screen.blit(castle_in,(0,0))
        screen.blit(Main,[780,50,100,000])
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_48_text,(0,600))
    elif page_variable == 49:
        screen.blit(castle_out,(0,0))
        screen.blit(Doctor,[400,310,500,200])
        screen.blit(Main,[780,315,100,000])
        screen.blit(Magic,[600,315,500,200])
        pygame.draw.rect(screen,WHITE,[0, 000, 1400, 200])
        screen.blit(page_49_text,(0,000))
    elif page_variable == 50:
        screen.blit(castle_out,(0,0))
        screen.blit(Doctor,[400,310,500,200])
        screen.blit(Main,[780,315,100,000])
        screen.blit(Magic,[600,315,500,200])
        pygame.draw.rect(screen,WHITE,[0, 000, 1400, 200])
        screen.blit(page_50_text,(0,000))
    elif page_variable == 51:
        screen.blit(inn,(0,0))
        pygame.draw.rect(screen,WHITE,[0, 600, 1400, 200])
        screen.blit(page_51_text,(0,600)) 

















    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
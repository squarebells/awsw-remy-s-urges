label sqb_remy_m1_trash:

    c "(Let's see, what do we have here...)"
    play sound "fx/rummage2.ogg"
    $ renpy.pause (1.5)
    if remytrashn == 0:
        $ remytrashn += 1
        $ remytrash = False
        m "There were a bunch of smelly, wet paper tissues in Remy's trash bin."
        c "(Nope. I'm not going to touch that.)"
        c "(What does he even do in his office?)"

jump remyoffmenu

label sqb_remy_m1_start:

    $ bangok_four_playerhasdick = False
    
    play sound "fx/button_press.ogg"
    $ renpy.pause (1.0)
    play sound2 "fx/sphereboot.ogg"
    m "At the press of a button, the screen came to life, accompanied by the whir of the machine, opening up to Remy's desktop. It seemed that he had forgotten to log out or lock his computer."
    $ renpy.pause (2.0)
    m "Looking for anything interesting on the desktop, I immediately noticed two programs running on the taskbar. By mousing over I found out that first one was called 'Ultimate Fantasy V', probably a game of some sort, and the other one was just named 'Web Browser'."
    c "(I have to admit that the names aren't very imaginative. Which one should I check out first?)"
    
    menu:
        "Check out the game Remy had left on.":
               
            $ renpy.pause (1.0)
            c "(I can't wait to play some dragon video games.)"
            $ renpy.pause (1.0)
            m "The screen went black for a few seconds after I opened up the game from the taskbar, and then colorful images appeared on the screen."
            stop music fadeout 1.0
            scene black with dissolve
            $ renpy.pause (2.0)
        
            jump sqb_remy_m1_end
        
        "Look at what Remy was browsing earlier.":
        
            $ renpy.pause (0.5)        
            c "(I wonder how similar dragon internet is compared to ours.)"
            play sound "fx/button_unpress.ogg"
            $ renpy.pause (2.0)
            c "(Looks like Remy was reading some gossip earlier today. Nothing very interesting here.)"
            $ renpy.pause (2.0)
            c "(Wait, why didn't I realize this sooner? If I wanted to find out more about dragon culture and society I should have just used a computer to gather information instead of reading books.)"
            c "(Let's do a search to find out more on what dragons think about humans.)"
            play sound "fx/keyboard.ogg"
            $ renpy.pause (1.0)
            m "As soon as I typed 'human' to the address bar, the browser auto-filled it with a rather questionable set of words."
            $ renpy.pause (1.0)
            c "(Oh my...)"
            c "(Human, female, nude, sex, interspecies...{w} and male on human? Is this a link with tags to a porn site?)" #Dragonworld has its own e6
            m "I knew I shouldn't have continued on invading Remy's privacy, but I wasn't able to resist the urge of wanting to find out what kind of porn dragons have made of humans."
            
    c "(Anything for progress, I guess? I feel like I'm about to make an important breakthrough in advancing the relations of our peoples.)"
    $ renpy.pause (2.0)
    m "After a moment's hesitation, I managed to gather enough courage to finally access the link."
    play sound "fx/button_unpress.ogg"
    $ renpy.pause (1.0)
    m "The site opened up to a green quadrupedal dragon fucking something resembling a very ugly humanoid from behind on the floor. Based on some of their mammalian traits I could recognize them as a female. Lastly, I noticed that the green dragon was most likely of the same dragon species as Remy."
    c "(Is this what dragons think human women look like? I feel kind of offended.)"
    c "(I can't help but also notice that dragon and its dick are pretty massive compared to the ugly humanoid. I wonder if Remy is as big as him?)"
    m "Then I noticed that Remy was still logged on to the porn site and that there was a favorites tab. With a sudden unexplained impulse, I clicked it next."
    play sound "fx/button_unpress.ogg"
    $ renpy.pause (1.0)
    m "The next page opened up to numerous pictures of quadrupedal dragons fucking what I could again vaguely recognize as a female human. More interestingly, an ovum with rapidly advancing sperm cells had been added into some of the pictures to show that the human was being impregnated by the dragon."
    m "On the page there were even two pictures in which the human was laying eggs, with presumably the dragon father of those eggs helping out with the ordeal."
    c "(This is kinky as fuck. I'm not sure if I should be doing this but for some reason right now I feel as if I was being glued to the computer by an invisible force.)"
    m "I decided that the correct course of action was to look through some more, for research of course."
    play sound "fx/keyboard.ogg"
    $ renpy.pause (2.0)
    play sound "fx/button_unpress.ogg"
    $ renpy.pause (4.0)
    m "After a few more pictures I was getting so aroused that I felt an urge to start masturbating."
    c "(I've noticed Remy giving me some strange stares and this finally explains why. I wonder if he is actually willing to have sex with me though? I have to admit that seeing all this porn has piqued my curiosity... in his capabilities.)"
    c "(I'll just look through the next page and then stop. It would be very awkward if someone came in right now.)"
    $ renpy.pause (2.0)
    play sound "fx/door/handle.wav"
    $ renpy.pause (2.0)
    play sound "fx/door/doorclose3.wav"
    $ renpy.pause (1.0)   
    show remy normal with dissolve
    Ry "All done. Now we can finally chat some more about the myths that we have of humans."
    show remy look with dissolve
    $ renpy.pause (1.0)
    Ry "What are you doing on my computer? You should have asked for permission first."
    m "I turned around to face Remy's gaze and he saw what I had been doing."
    Ry "Hey, t-that's private."
    c "You're a very kinky dragon, Remy. I didn't know you fantasize about fucking humans."
    $ renpy.pause (1.0)
    
    if remymood <= 10:
        
        Ry look "Could you please shut down the monitor, step away from my computer and forget everything you saw?"
        c "What's the big deal? I think this stuff is pretty hot too."
        Ry sad "Please, you're making me feel very uncomfortable. Let's never mention this ever again."
        c "(Damn it. I guess he wasn't comfortable enough sharing his kinks with me.)"
        c "Alright. I'm sorry, Remy. I shouldn't have invaded your privacy like that."
        Ry normal "Invaded my privacy? What are you even talking about?"
        c "Oh, right."
        show remy smile with dissolve
        c "Anyways, why do you have a bed in your office? Do you live here?"
        
        jump sqb_remy_m1_fail
    
    else:
       pass
    
    Ry shy "T-that's not something you should reveal on a first date..."
    c "We're on a date? Your interest in meeting me wasn't strictly professional?"
    Ry sad "..."
    c "Just kidding, I wouldn't mind if this was a date. You're super nice, Remy." 
    show remy shy with dissolve
    c "Anyway, I was offended a little bit by how ugly you dragons think humans are."
    Ry normal "I agree that female humans in our media aren't very nice to look at, and I'm actually relieved to hear that we got it wrong. I just assumed ugliness is the reason you cover your bodies."
    c "Not at all. I guarantee I'm smooth and round underneath my clothes."
    $ renpy.pause (1.0) 
    c "I could even show you if you asked nicely. We have to correct this gross misunderstanding."
    show remy shy with dissolve
    $ renpy.pause (2.0) 
    Ry smile "You would do that for me!? I can't begin to describe how excited the prospect of breaking new ground makes me right now."
    c "(I hope it excites you in more ways than one.)"
    c "Of course I am. Still, you need to do something for me first."
    Ry normal "What do you need? I'd be willing to do anything to learn more about humans!"
    c "{i}Anything?{i}"
    c "Well, I've seen most of you already since you barely wear any clothing." 
    c "There's still something you could do for me."
    Ry "Yes? Go on, break the suspense and tell me what it is already."
    c "Well, uhh...{w} when browsing through your favorite porn I was surprised by the size and shape of dragon genitalia, so could you show me yours? Only if you'd feel comfortable doing that, of course."
    Ry shy "..."
    m "I noticed him fidget around and start panting due to my sudden sexual advance."
    c "(Please, Remy. I want to see a real dragon penis, not just an image representation of one.)"
    m "He hesitated for a few moments while shifting his gaze between me and the bed next to us."
    $ renpy.pause (1.0)
    Ry "S-sure... would it be fine if I laid on the bed on my back while you did the inspection?"
    c "Yeah. I can get a perfect view if you're on the bed on your back."
    c "Just one more thing. Are you sure that no one is going to barge in like you just did?"
    Ry normal "I don't think so. Everyone in this department already went home or is working remotely and I already completed all my tasks for today. No one is going to bother me for the rest of the evening."
    c "Alright. You can get on the bed now."
    hide remy with dissolve
    $ renpy.pause (1.0)
    play sound "fx/sheet.wav"
    
    if persistent.bangok_cloacas == True:
        m "Without hesitation, Remy stepped next to the bed, jumped carefully on it on his back and spread his hindlegs apart towards me. I noticed a single large horizontal slit between them."   
    else:
        m "Without hesitation, Remy stepped next to the bed, jumped carefully on it on his back and spread his hindlegs apart towards me. I noticed a single large horizontal slit between them and another smaller one below it."  
        
    play sound "fx/undress.ogg"
    m "Wanting to get a much more intimate feeling of Remy, I undressed except for my bra and panties and sat on the bed next to him."
    show remy shy with dissolve
    m "I leaned towards Remy's hindquarters and started stroking his cute and soft lower belly, making him look pleased and hum contently."
    show remy smile with dissolve
    play soundloop "fx/rub2.ogg"
    c "(Looks like all of his male parts are internal. I wonder if his testicles are inside him somewhere over here?)"
    $ renpy.pause (1.0)
    m "Then, sitting next to him on the bed for a minute made me finally realize just how much bigger he actually was compared to me."
    c "(This stud of a dragon must be at least four to five times bigger than I am. I would feel slightly intimidated if I didn't already know that he likes humans a lot. Even for such a nerdy boy there's some muscle and mass to admire.)"
    $ renpy.pause (1.0)
    Ry "..."
    stop soundloop fadeout 1.0
    c "Remy, you're very brave and a big boy, but where's the rest of you?"
    Ry shy "Oh... I completely forgot because I enjoyed the touch of your smooth skin so much."
    $ renpy.pause (1.0)
    m "Remy shifted and clenched his hindquarters a little bit, and then a small, pinkish shaft appeared out of his horizontal slit."
    c "That's it? I thought you'd be at least a little bit bigger."
    Ry smile "Give me a moment, that's just the tip."
    show remy shy with dissolve
    $ renpy.pause (1.0)    
    m "After steadying himself some more on his back, Remy continued clenching the muscles in his lower body, and the rest of his pinkish and tapered penis slowly slid out. When fully exposed it was very large, as I had correctly expected from a dragon several times bigger than a human."
    c "(It's girthier than my forearm. I want my pussy destroyed by it yesterday.)"
    Ry "Well?"
    c "It looks so beautiful..."
    Ry smile "You really think so? I'm so happy that I didn't disappoint."
    Ry normal "Now that you've seen me, can I see you?"
    c "Sure, Remy."
    play sound "fx/undress.ogg"
    m "I took off my bra and panties and threw them on the floor. Remy eyed my breasts curiously and then looked at my lower body."
    Ry shy "What about your... umm..."
    c "My pussy? Soon Remy, soon."
    c "(You'll see a lot of it right before you mount me from behind.)"
    c "Can I play with your dick?"
    Ry shy "O-of course, anything for you."
    play sound "fx/rub2.ogg"
    play sound2 "fx/lewd/lickslow.ogg"
    queue sound2 "fx/lewd/lickslow.ogg"
    queue sound2 "fx/lewd/lickslow.ogg"
    show remy smile with dissolve
    m "I stroked Remy's shaft a few times, guided it into my mouth and gave the tapered tip a few licks. There was a slight taste of musk, but it was just a little bit different, maybe even exotic and enjoyable."
    c "(So, this is what a male dragon tastes like.)"
    stop sound fadeout 1.0
    play sound "fx/lewd/blowjob.ogg"
    show remy shy with dissolve
    m "To finish off my exploration efforts, I engulfed Remy's large tip in my mouth and gave it an audible suck."
    Ry "Ah... you're enjoying it a lot, aren't you?"
    $ renpy.pause (2.0)
    m "After I pulled back, I was again astonished by the shape and size of Remy's dick."
    c "I've never seen a penis that tapers at the tip like this."
    Ry normal "Actually, its purpose is to penetrate the cervix of someone you want-"
    show remy shy with dissolve
    $ renpy.pause (1.0)
    Ry "-to make children with before an ejaculation in order to guarantee impregnation. But I wouldn't do that unless that someone asked me to, because it might make them feel a bit uncomfortable or even cause some pain if not being prepared for."
    c "That would indeed be a nasty surprise, if the recipient wasn't expecting it. I'm up for trying it later, when we're more familiar with each other's bodies and limits."
    #Not sure yet if disabling the cervpen tag will make this significantly less extreme or disable it altogether in the date 4 scene
    show remy look with dissolve
    $ renpy.pause (2.0)
    Ry smile "Did you just say want to have sex with me!?"
    c "I thought that would be blatantly obvious by now. Did you seriously think that I have just been teasing you all this time?"    
    c "We have to be careful though, because your dick is too long to completely fit inside me." 
    c "So, you can't hilt yourself inside me under any circumstance, no matter how much you want to. You don't want to break your favorite human, do you?"
    Ry normal "I would never do something like that! You can place your trust in me."
    c "Thank you, Remy. We'll do it slowly at first in order find out how much of you I can take."
    $ renpy.pause (1.0)
    show remy shy with dissolve
    play sound "fx/lewd/lickslow.ogg"
    m "I gave Remy's dick a couple more strokes and I realized we had had enough foreplay already. I wanted his breeding tool inside me right now."
    c "I'm done with the first course. I want you to mount me, my dragon lover."
    Ry "W-wait a second. Umm...{w} d-do you want to use protection with me?"    
    c "I don't have any condoms on me, not that I would want to use one anyway, unless you really insisted. Seeing your porn made me want a huge mess in my pussy with your dragon tool. I want you to fill me up well and good."
    Ry smile "It just so happens that's exactly what I wanted to do as well. Actually, I've fantasized about breeding you ever since I realized you were a female of your species."
    c "Remy, even though I said I didn't want to use protection, do you think you should be telling me something like that on our first time doing it?"
    Ry shy "S-sorry...{w} I just can't stop thinking about it."
    $ renpy.pause (1.0)
    c "About what?"
    Ry "A-about i-impregnating you with a dragon-human crossbreed."
    c "(This would have gone so badly if I wasn't fantasizing about that as well.)"
    c "..."
    Ry sad "I don't know why I blurted it out like that."
    c "It's fine. After seeing some of your porn I warmed up to the idea of interspecies breeding actually being amazing." 
    c "I wouldn't mind starting a family with you because I was planning to stay here anyway. The human world is a pretty terrible place to live in right now, so I don't want to go back."
    show remy smile with dissolve
    m "Remy's eyes and entire facial expression lit up with a combination of unparalleled lust and joy."
    c "So, if you manage to knock me up I'll marry you and stay with you here for the rest of my life."
    Ry normal "I'll try my best! I know I am extremely virile."
    c "(I've been looking for a husband like you for a while now, so I'll just marry you even if we can't have biological kids. I'm not so sure if our species can crossbreed.)"
    c "Let's get to it then. Time to find out how strong your seed is."
    Ry shy "Wait a second. There's one more thing."
    Ry "Actually, I'm not so sure if we should be having sex in my office."
    Ry normal "Like I said, there is no one working in this part of the building at this time, but what if someone wandering around comes to check out the noise? The janitor is probably still around."
    Ry "Could we just go over to my place?"
    c "No, I'm so horny that I want to do it right now. Going all the way over to your apartment would ruin the mood for me." 
    c "If you actually want to fuck your crossbreed child into me, you're going to have to be brave enough to do it at your workplace."
    show remy shy with dissolve
    $ renpy.pause (1.0)
    Ry smile "Fine... you win."
    c "Finally. Get off the bed so we can start."
    hide remy with dissolve
    stop soundloop fadeout 1.0
    play sound "fx/sheet.wav"
    m "With those words, Remy slid off the bed and at the same time I laid on it perpendicularly on my stomach. Remy was behind me, watching with glee the entire time as I was getting into position."
    c "How about some lubrication? Let's put your tongue into use."
    Ry "Oh, of course. I hope that you will like that part of me as well."
    m "When I steadied myself on my legs and raised my backside up, I felt Remy lean his head towards my ass in an instant."
    $ renpy.pause (2.0)
    m "I felt his hot breath on my pussy and after a few moments his big, wet dragon tongue started dragonhandling my labia and vulva."
    play soundloop "fx/lewd/lickslow.ogg"
    c "Aah..."
    Ry "How does it feel? As for me, human vaginas feel... different."
    c "It f-feels great, Remy. You can go deeper if you want."
    m "With my permission, Remy penetrated deep into my vagina with his tongue while also massaging my clit with it."
    c "Ahh!" with vpunch
    m "Remy tried to mumble something, but I couldn't hear him because he was deep in my pussy. Then, he pushed even deeper, and I felt a strange feeling in my lower belly. His tongue made it all the way to my cervix."
    c "Mmm... that's my most inner sanctum. I'm giving you permission to put a child in there. You're going to be the only one who's allowed to do that."
    m "As a response, I only could hear some horny grunts and pants from Remy. I imagined that Remy's dick probably perked up in attention as well, ready to go at a moment's notice."
    $ renpy.pause (2.0)
    c "Let's move onto the main course. I want to orgasm as you impregnate me with your brood."
    stop soundloop fadeout 1.0
    m "Remy pulled out of my pussy and sat on the floor, and I got up and turned around on the bed towards him. His huge, erect cock was pointing menacingly towards me like a spear about to impale me."
    show remy normal with dissolve
    c "You continue to surprise me with your assets, Remy. In addition to your dick being large, your tongue was as well."
    Ry shy "I don't know what to say. I mean, thank you... I love hearing you say that."
    stop music fadeout 1.0
    c "Alright, lets fuck. From behind is probably the safest, considering our size difference. We'll use your bed as a cushion to make it more comfortable for me."
    c "Get on top of me and I'll guide you in {i}slowly{/i}. We'll have to find out how deep you can go without breaking me. Seriously, keep that in mind when you fuck me."
    Ry normal "Don't worry about it. I won't ruin the evening by hurting you in even the slightest way."
    hide remy with dissolve
    play sound "fx/bed.ogg"
    m "Already eager to be bred I turned around, got on the bed on my belly and for the second time presented my pussy to Remy."
    m "He came in closer, got up on his hindlegs and planted his forelegs next to me on the bed."
    c "Now, let me guide you inside."
    Ry shy "P-please do... in this position I can't see where I'm aiming at."
    play sound "fx/lewd/lickslow.ogg"
    m "I arched my back upwards a little bit, reached backwards with my arm to grab Remy's hot and hard dragon dick and started guiding it towards my pussy."
    play sound "fx/lewd/pussy.ogg"
    m "After leaning in a little bit with my guidance, the tip of his penis was nested at the entrance to my vagina."
    play sound "fx/sheet.wav"
    m "Then, to be able to leverage himself better, he came down even closer and partially sandwiched me between himself and the bed."
    play sound "fx/lewd/penslow.ogg"
    queue sound "fx/lewd/penfast.ogg"
    m "Remy leaned down from behind and licked my cheek and mouth with his wet tongue."
    Ry "I love you, [player_name]. I want to make many children with you."
    c "Then you better start pushing in before we die of old age."
    play sound "fx/lewd/pussy.ogg"
    queue sound "fx/lewd/penslow.ogg"
    queue sound "fx/lewd/penslow.ogg"
    m "Remy complied, and I started feeling his hot dragon rod pushing forward properly, forcing its way into me."
    c "You're such a big boy, Remy. Keep going."
    play sound "fx/lewd/penfast.ogg"
    queue sound "fx/lewd/penslow.ogg"
    m "He kept pushing in slowly. Because his dick was much bigger than any penis or dildo that I had ever had, my pussy was now stretching desperately to be able to fit him."
    play sound "fx/lewd/blowjob.ogg"
    queue sound "fx/lewd/penslow.ogg"
    m "Then, after being filled by Remy's dragon dick for a couple of long seconds more, he slowed down and I again felt the strange feeling in my lower belly."
    c "There. This is as as far as you can go, for now."
    Ry "Got it. I could feel a bit more resistance, so I slowed down."
    c "Now, pull yourself back and penetrate me all the way in slowly."
    play sound "fx/lewd/penslow.ogg"
    queue sound "fx/lewd/penfast.ogg"
    queue sound "fx/lewd/pussy.ogg"
    m "With my permission, Remy partially pulled out and then re-speared me with his massive dragon shaft, which caused me to shudder and made my pussy let out some more audible squelches."
    m "I could feel my breeding hole start to shape up even more to accommodate Remy's size better."
    c "You're such a big fucking stud, Remy. My pussy is about to get destroyed so badly that I won't feel anything if I ever decide to have sex with a human again."
    m "Remy only replied with several grunts and pants and then I felt some of his saliva drop on my back."
    c "(That cute big guy must be at the top of his world right now. He's so lucky that I am the human who came through the portal.)"
    c "Your dick is the best thing in the world, Remy. I'm ready for you to start pumping into me. I'll tell you if you need to slow down."
    c "It's time for you to properly breed me."
    Ry "I'll impregnate you!"
    play soundloop "fx/lewd/penslow.ogg"
    m "With that remark, Remy started pounding my pussy with the most loving care in the world."
    c "Fuck me, Remy! Tight human pussy is what you have wanted all along."
    c "Pound me to bits and inseminate me with your powerful and virile dragon seed!"
    stop soundloop fadeout 1.0
    play soundloop "fx/lewd/penfast.ogg"
    m "Remy really liked that remark and reciprocated by fucking me harder."
    Ry "We're going to have {i}so{/i} many children, [player_name]!"
    c "Fuck the first one of our brood of children into me, Remy!"
    $ renpy.pause (4.0)
    m "Judging by his grunting and moaning, Remy was already going to cum. It seemed that due to having been aroused for such a long time he couldn't last very long."
    Ry "I-I'm coming!"
    c "I want your dragon swimmers in my womb! They're going to completely ravage my egg!"
    play sound "fx/snarl.ogg"
    Ry "Get pregnant!"
    stop soundloop fadeout 1.0
    play sound "fx/lewd/penslow.ogg"    
    play sound2 "fx/lewd/cum.ogg"
    queue sound "fx/lewd/penslow.ogg"
    queue sound2 "fx/lewd/cum.ogg"
    queue sound2 "fx/lewd/cumlots.ogg"
    m "As promised, Remy came inside me with the power of a thousand horny dragons. All in a split second, I first felt his incredibly warm cum fill me but then it also started forcefully bursting out of my pussy as he completed his final thrusts." with vpunch
    m "His load had been so massive that with nowhere to go that it had to simultaneously explode in both directions."
    m "The force of Remy's semen expanding my pussy and the thought of tens of millions of his strong dragon swimmers being about to make short work of my lone, defenseless ovum caused me to cum as well."
    c "Ngghh! Ahh!" with vpunch
    $ renpy.pause (2.0)
    play sound "fx/kiss.wav"
    show remy shy with dissolve
    m "Fully spent after depositing his load into my pussy, Remy slumped on top of me and started kissing and licking my neck."
    play sound "fx/lewd/lickslow.ogg"
    queue sound "fx/lewd/lickslow.ogg"
    $ renpy.pause (6.0)
    play sound "fx/lewd/pussy.ogg"
    m "After lying on top of me for about half a minute, Remy pulled out of my pussy and climbed on the bed to embrace me in a hug with his entire body."
    play sound "fx/rub2.ogg"
    m "Then as I as I hugged him back, he wrapped me with his wings and rubbed the side of my head with his snout."
    stop sound fadeout 1.0
    play music "mx/fireplace.ogg"
    $ renpy.pause (1.0)
    Ry "I-I l-love you so much, [player_name]."
    c "I love you too, Remy."
    $ renpy.pause (1.0)
    c "(Being fucked and hugged by a dragon is amazing.)"
    $ renpy.pause (1.0)    
    c "(I just realized I let him cum inside me before we even had our first kiss.)"
    play sound "fx/kiss.wav"
    m "I leaned in and kissed Remy on the mouth."
    show remy smile with dissolve
    c "You're adorable."
    $ renpy.pause (4.0)    
    show remy normal with dissolve
    m "We lay there together for a long while more, not wanting to go back to our mundane, everyday lives."
    Ry shy "H-hey... just a thought."
    c "Yeah?"
    Ry "Are you s-sure you want to crossbreed with me? Starting a f-family is a pretty big commitment...{w} and we aren't even of the same species."
    c "(Seems that he still has some doubts and self-esteem issues.)"
    c "Of course, Remy. I meant everything I said."
    c "You're gentle, considerate, caring and intelligent. I feel so lucky to have found you. Also, there is nothing wrong with interspecies relationships." 
    c "Actually, even thinking about having a such a gentle giant of a dragon for a husband excites me for multiple reasons, especially because then I can use your umm... different and bigger assets."
    Ry smile "Thank you for those kind words. I am so happy that you like me."
    Ry shy "Sorry. I f-feel kind of rude asking questions like these, because sometimes it seems that maybe I don't actually deserve all this."
    c "(Seeing such a gentle and kind dragon sad is so heartbreaking.)"    
    c "It's alright, Remy. You deserve to be happy. I'll always be there for you."
    show remy smile with dissolve
    play sound "fx/rub2.ogg"
    m "I started scratching the back of his head to comfort him."
    m "Remy sniffed and hugged me tighter."
    Ry "I love you so much. Thank you for coming to visit me."
    c "If I had known beforehand what I was going to find here I would have been the first one in line to come over."
    #Refer back to this conversation when Remy reveals in date 3 why he's depressed
    $ renpy.pause (2.0)
    c "So, how do you want to go forward from here?"
    Ry normal "We carry on as usual without making any announcements yet, seeing each other whenever we have the time. There's no need to make a big deal about it." 
    Ry "If I really just succeeded in knocking you up, things will probably have died down before you start showing any immobilizing or other adverse effects of pregnancy. When the time comes, you should be able to go on maternity leave."
    Ry smile "It would be the first-ever dragon-human pregnancy, so we should take as many precautions as possible. Regular medical check-ups are going to be mandatory."
    c "(Damn, I just realized something. Since dragons are so much bigger than humans, I wonder how big Remy's kid is going to be if crossbreeding is actually possible? Can it even fit inside me? Is it going to be a fetus or an egg?)"
    Ry normal "Still, you'll have to start doing pregnancy tests, so we can get prepared ahead of time in case we succeeded today. I'll get them for you so you can keep your mind focused on your important job."
    c "Look, I'm not sure how likely it's for you to be able to get me pregnant. I remember hearing that even different species of dragons can't crossbreed, and our taxonomies are even more different than that."
    c "I would love for you to be able to impregnate me but just remember that we still don't know if that's even possible."
    Ry smile "You're right, of course. In any case, shouldn't we still keep trying as much as we can? It's going to be a lot of fun."
    c "I agree. I would like to try with you a lot."
    show remy normal with dissolve
    $ renpy.pause (1.0)
    play sound "fx/sheet.wav"
    m "Not feeling like cuddling any more, I got off the bed and started picking up my clothes and putting them on. Then I noticed the mess Remy's cum and my own love juices had made on the carpet."
    c "What a mess. You came so much that your cum literally exploded out of my pussy."
    Ry "Don't worry about it. I'll clean it up since this is my office."
    c "Thanks a lot. I'm completely beat."
    $ renpy.pause (1.0)
    c "Next time time we fuck I'll let you cum directly into my womb so we don't have to clean it up from the floor or bed. Remember, any of your sperm that doesn't go into my womb isn't trying to impregnate me."
    Ry shy "I... uh..."
    c "You're so cute, Remy. You want to be a daddy so badly but you're shy about it."
    Ry "Y-yeah..."
    $ renpy.pause (2.0)
    show remy normal with dissolve
    play sound "fx/bed.ogg"
    m "I finally finished putting my clothes back on. They smelled of sex, like the entire office did."
    c "So, when's our next date? I can't wait to hang out with you again."
    Ry "Just call me up whenever you have some free time from your important duties."
    Ry smile "I mean, I can't wait to be with you again as well, [player_name]."
    Ry normal "Let's meet at my apartment to in order to avoid any unnecessary surprises during sex. I'll even cook you dinner to repay for all the help you did for me."
    c "Thank you for the offer. I would love that kind of date a lot."
    c "You sure you're fine cleaning up over here all by yourself?"
    Ry "Sure. Leave it all to me."
    c "Alright. See ya."
    Ry smile "Bye."
    $ renpy.pause (1.0)
    stop music fadeout 1.0
    play sound "fx/door/handle.wav"
    $ renpy.pause (2.0)
    hide remy with dissolve
    play sound "fx/door/doorclose3.wav"
    $ renpy.pause (1.0)
    scene black with dissolve
    m "I left Remy to clean up his office, my only thoughts during the trek back to my apartment being fantasizing about our next meeting. I couldn't wait to be creampied by him again, next time in his home. The way things were going, I would also be able to call it my home not before long."
    m "I wanted our home to be filled by our children, hopefully coming to this world in the near future. Right now, the thing I wanted the most in life was for Remy to sire lots of offspring with me. He truly is the perfect father for a large brood of interspecies children."
    m "Something like this happening would have been unimaginable to me just a few weeks ago. Who could have guessed that they would visit a world with another sentient species, let alone that they were going to marry one of them?"
    m "For the first time after the flare had hit, my life again felt like it was on track towards something positive. To secure my future, the only thing I would have to do was to stop Reza and establish friendly relations between our peoples."
    m "This seemed like a relatively simple task, considering all that had happened to me so far."
    
    $ remystatus = "good"        
    $ remyscenesfinished = 1
    $ sqbhadsexwithremy1 = True
    $ persistent.remy1skip = True
    
    #Magmalink's date end function didn't work for some reason so I'm using the old method
    
    if chapter4unplayed == False:

        jump chapter4chars

    elif chapter3unplayed == False:

        jump chapter3chars

    elif chapter2unplayed == False:

        jump chapter2chars
    else:


        jump chapter1chars
    
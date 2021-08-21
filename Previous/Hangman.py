word_list=['accessible','ambiguous','amusement','apologise','arithmetic','baroness','cake','calculator','cellar','charismatic','chemical','contest','creature','curtain','cynical','decisive','descriptive','different','digestion','downtown','education','encourage','endurable','exclusive','fiction','gorgeous','hilarious','hoax','hospital','impartial','innovate','insurance','jellyfish','knapsack','knight','locket','machine','magical','magnificent','measure','mysterious','notebook','oatmeal','obsolete','organisation','periodic','perpetual','political','quality','quarantine','resolute','scissors','secretary','selective','theory','thirsty','thunder','umbrella','vacation','website','whereabouts','xenophobia','yacht','zodiac','zebra','zipper']
secret_list=['GLaDOS','Frisk','Tails','Krabs','Karamari','Funtimes','Nether','Cuphead','Plantera','Lancer','Brandon','Glubfub','Spooky','Leviathan','Peashooter','Pringles','Stickmin','Opelucid','Bertie','Bendy','Determination','Radiance','Hornet']
clues=['(of a place) able to be reached or entered easily','open to more than one interpretation; not having one obvious meaning','the state or experience of finding something funny','express regret for something that one has done wrong','the branch of mathematics dealing with the properties and manipulation of numbers','the wife or widow of a member of the lowest order of the British nobility, usually being referred to as ‘Lady','a soft sweet food made from a mixture of flour, fat, eggs, sugar, and other ingredients, baked and sometimes iced or decorated','a small electronic device with a keyboard and a visual display used for making mathematical calculations','a room below ground level in a house, often used for storing wine or coal','exercising a compelling charm which inspires devotion in others','a distinct compound or substance, especially one which has been artificially prepared or purified','an event in which people compete for supremacy in a sport or other activity, or in a quality','an animal, as distinct from a human being','a screen of heavy cloth or other material that can be raised or lowered at the front of a stage','doubtful as to whether something will happen or whether it is worthwhile','having or showing the ability to make decisions quickly and effectively','describing something, especially in a detailed, interesting way','not the same as another or each other; unlike in nature, form, or quality','the process of digesting food','in or relating to the central part or main business and commercial area of a town or city','the process of receiving or giving systematic instruction, especially at a school or university','give support, confidence, or hope (to someone)','able to be tolearable','restricted to a person, group, or area concerned.','literature in the form of prose, especially novels, that describes imaginary events and people','beautiful; very attractive','extremely amusing','a humorous or malicious deception','an institution providing medical and surgical treatment and nursing care for sick or injured people','treating all rivals or disputants equally','make changes in something established, especially by introducing new methods, ideas, or products','an arrangement by which a company or the state undertakes to provide a guarantee of compensation for specified loss, damage, illness, or death in return for payment of a specified premium','an aquatic animal with a gelatinous bell or saucer-shaped body that is typically transparent','a soldier\'s or hiker\'s bag with shoulder straps, carried on the back, and typically made of canvas or other weatherproof materia','a man who served his sovereign or lord as a mounted soldier in armour','a small ornamental case, typically made of gold or silver, worn round a person\'s neck on a chain and used to hold things of sentimental value, such as a photograph or lock of hair','an apparatus using mechanical power and having several parts, each with a definite function and together performing a particular task','relating to, using, or resembling magic','extremely beautiful, elaborate, or impressive','ascertain the size, amount, or degree of something by using an instrument or device marked in standard units','difficult or impossible to understand, explain, or identify','a small book with blank or ruled pages for writing notes in','a type of coarse flour made of hulled oat grains that have either been milled or steel-cut','no longer produced or used; out of date','an organised group of people with a particular purpose, such as a business or government department','appearing or occurring at intervals','never ending or changing','relating to the government or public affairs of a country','the standard of something as measured against other things of a similar kind; the degree of excellence of something','a state of isolation in which people or animals that have arrived from elsewhere or been exposed to infectious or contagious disease are placed','admirably purposeful, determined, and unwavering','an instrument used for cutting cloth, paper, and other material','a person employed by an individual or in an office to assist with correspondence, make appointments, and carry out administrative tasks','relating to or involving the selection of the most suitable or best qualified','a plausible or scientifically acceptable general principle offered to explain phenomena','feeling a need to drink','a loud rumbling or crashing noise heard after a lightning flash due to the expansion of rapidly heated air','a device consisting of a circular canopy of cloth on a folding metal frame supported by a central rod, used as protection against rain','an extended period of leisure and recreation, especially one spent away from home or in travelling; a holiday.','a set of related web pages located under a single domain name, typically produced by a single person or organization','the place where someone or something is','dislike of or prejudice against people from other countries','a medium-sized sailing boat equipped for cruising or racing','An astrological system which divides the heavens into twelve equal divisions e.g. Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius, Pisces','an African wild horse with black-and-white stripes and an erect mane.','a device consisting of two flexible strips of metal or plastic with interlocking projections closed or opened by pulling a slide along them, used to fasten garments, bags, and other items']
secret_clues=['alternate form: potato','7th human soul; 8th fallen human','helicopter fox','has a serious addiction to money','underground hospital in a 1000-door mansion','\'Press the red button now, to administer a controlled shock.\'','\'Achievement Get: We Need to Go Deeper\'','One of two brothers that \'ended up on the wrong side of the tracks\'','\'Achievement Get: The Great Southern Plantkill\'','alternate form: chair','Male protagonist of Gen III','Keymaster of the Vault of Secrets','Main antagonist of the jumpscare mansion','a sea dragon, a ghost, a sea emperor and a reaper walk into a bar...','The 1st plant you ever get; costs 100 <game currency>', 'the potato guy that seems to be part of the Mexican Mafia','Protagonist of BTB, ETP, STB, ITA, FTC, and CTM','Location of Gen V\'s final gym','A nickname; \'Achievement Get: Around and Around / Going to Be Sick\'','Main antagonist of the Studio, and main protagonist of Tombstone Picnic','DT','\'Seek The Kingdom\'s Forgotten Light\'','The Gendered Child']
choices=['y','n','Y','N']
unlocked=False
import random
repeated=True
secret=False
while repeated:
    win=False
    repeated=False
    seperate=[]
    wrong=[]
    if secret:
        key=random.randint(0,22)
        word=secret_list[key]
    else:
        key=random.randint(0,65)
        word=word_list[key]
    displayed_list=['_']*len(word)
    for n in range(len(word)):
        seperate.append(word[n])
    print("There are "+str(len(word))+" letters in the word.")
    for guesses in range(9):
        print("           ")
        print(" ".join(displayed_list))
        print("Letters not in word: "+" ".join(wrong))
        correct=0
        guess=input("Guess a letter, or enter a word: ")
        if not unlocked:
            if guess=="administrator":
                guess=input("Insert password: ")
                if guess=="password1":
                    print("Access granted")
                    guess=input("Commence system override? (Y/N): ")
                    if guess=="Y":
                        unlocked=True
                        win=True
                        print("Commencing system override...")
                        print("Secret list activated.")
                        break
                    else:
                        print("Guesses remaining: "+str(9-guesses))
                        continue
                else:
                    print("Access denied")
                    print("Guesses remaining: "+str(9-guesses))
                    continue
        if len(guess)==1:
            for n in range(len(word)):
                if guess.lower()==seperate[n].lower():
                    displayed_list[n]=seperate[n]
                    correct+=1
            if correct==0:
                print("Letter entered is not in word.")
                if guess not in wrong:
                    wrong.append(guess.lower())
            else:
                print("Letter entered is found in word "+str(correct)+" time(s).")
        elif guess.lower()!=word.lower():
            print("That is not the correct word. Try again.")
        if guess.lower()==word.lower() or displayed_list==seperate:
            if displayed_list==seperate:
                print(" ".join(displayed_list))
            print("Congratulations! You have solved the puzzle!")
            win=True
            break
        print("Guesses remaining: "+str(9-guesses))  
    if not win:
        print("           ")
        print(" ".join(displayed_list))
        print("Letters not in word: "+" ".join(wrong))
        if not secret:
            print("Final clue: "+clues[key])
        else:
            print("Final clue: "+secret_clues[key])
        guess=input("Please enter your final guess: ")
        if guess.lower() != word.lower():
            print("Game over. The word is actually "+word+".")
        else:
            print("Congratulations! You have solved the puzzle!")
    ask=input("Would you like to play again? (Y/N): ")
    while ask not in choices:
        print("Error. Please enter only 'Y' or 'N'.")
        ask=input("Would you like to play again? (Y/N): ")
    if ask.upper()=="Y":
        repeated=True
        if unlocked:
            ask=input("Switch modes? (Y/N): ")
            while ask not in choices:
                print("Error. Please enter only 'Y' or 'N'.")
                ask=input("Switch modes? (Y/N): ")
            if ask.upper()=="Y" and secret:
                secret=False
            elif ask.upper()=="Y" and not secret:
                secret=True




import csv
import os
from os import path
from math import floor
import random

class Character:

    def __init__(self, name="", quests_completed = [], quests_unlocked=[], quests_locked=[]):
        try:
            real_path = os.path.dirname(os.path.realpath(__file__))
            file_path = real_path+'/'+name+'.csv'
            with open(file_path, encoding="utf-16", errors='ignore') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        self.quests_completed = set()
                        self.quests_unlocked = set()
                        self.quests_locked = set()
                        line_count += 1
                    if line_count == 1:    
                        self.name = row["Name"]
                        self.member = row["Member"]
                        self.quest_points = (int)(row["Quest Points"])
                        self.skills = {"attack":(int)(row["Attack"]), "strength":(int)(row["Strength"]), "defence":(int)(row["Defence"]), "ranged":(int)(row["Ranged"]), "prayer":(int)(row["Prayer"]), "magic":(int)(row["Magic"]), "runecrafting":(int)(row["Runecrafting"]), "construction":(int)(row["Construction"]), "constitution":(int)(row["Constitution"]), "agility":(int)(row["Agility"]), "herblore":(int)(row["Herblore"]), "thieving":(int)(row["Thieving"]), "crafting":(int)(row["Crafting"]), "fletching":(int)(row["Fletching"]),  "slayer":(int)(row["Slayer"]),  "hunter":(int)(row["Hunter"]), "mining":(int)(row["Mining"]), "smithing":(int)(row["Smithing"]), "fishing":(int)(row["Fishing"]), "cooking":(int)(row["Cooking"]), "firemaking":(int)(row["Firemaking"]), "woodcutting":(int)(row["Woodcutting"]), "farming":(int)(row["Farming"])}
                        self.current_task = row["Current Task"] 
                        self.total = row["Objectives Completed"]
                        if row["Quests Completed"] != "":
                            self.quests_completed.add(row["Quests Completed"])
                        
                        if row["Quests Unlocked"] != "":    
                            self.quests_unlocked.add(row["Quests Unlocked"])
                        
                        if row["Quests Locked"] != "":
                            self.quests_locked.add(row["Quests Locked"])
                        
                    else:
                        if row["Quests Completed"] != "":
                            self.quests_completed.add(row["Quests Completed"])    
                        if row["Quests Unlocked"] != "":    
                            self.quests_unlocked.add(row["Quests Unlocked"])
                        if row["Quests Locked"] != "":
                            self.quests_locked.add(row["Quests Locked"])
            
                    line_count += 1

                    
        except: 
            print("File not found")
            self.name = name
            self.member = False
            self.quest_points = 0
            self.skills = {"attack":1, "strength":1, "defence":1, "ranged":1, "prayer":1, "magic":1}
            self.quests_completed = quests_completed
            self.quests_unlocked = quests_unlocked
            self.quests_locked = quests_locked

        finally:
            self.combat_level = combat_level(self.skills["attack"], self.skills["strength"], self.skills["defence"], self.skills["ranged"], self.skills["magic"], self.skills["constitution"], self.skills["prayer"])
    
    
    def write_character_to_file(self, selector="all"):

        #UPDATE THIS
        selector = "all"

        real_path = os.path.dirname(os.path.realpath(__file__))
        file_path = real_path+'/'+self.name+'.csv'
        with open(file_path, encoding="utf-16", mode='w', errors='ignore') as csv_file:

            fieldnames = ['Name', 'Member', 'Attack', 'Strength', 'Defence', 'Ranged', 'Prayer', 'Magic', 'Runecrafting', 'Construction', 'Constitution', 'Agility', 'Herblore', 'Thieving', 'Crafting', 'Fletching', 'Slayer',	'Hunter', 'Mining', 'Smithing', 'Fishing', 'Cooking', 'Firemaking', 'Woodcutting', 'Farming', 'Quests Completed', 'Quests Unlocked', 'Quests Locked', 'Quest Points', 'Current Task', 'Objectives Completed']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            if selector == "all":
                quests_completed = list(self.quests_completed)
                quests_unlocked = list(self.quests_unlocked)
                quests_locked = list(self.quests_locked)


                base_line = {'Name': self.name, 'Member':self.member, 'Attack':self.skills["attack"], 'Strength':self.skills["strength"], 'Defence':self.skills["defence"], 'Ranged':self.skills["ranged"], 'Prayer':self.skills["prayer"], 'Magic':self.skills["magic"], 'Runecrafting':self.skills["runecrafting"], 'Construction':self.skills["construction"], 'Constitution':self.skills["constitution"], 'Agility':self.skills["agility"], 'Herblore':self.skills["herblore"], 'Thieving':self.skills["thieving"], 'Crafting':self.skills["crafting"], 'Fletching':self.skills["fletching"], 'Slayer':self.skills["slayer"],	'Hunter':self.skills["hunter"], 'Mining':self.skills["mining"], 'Smithing':self.skills["smithing"], 'Fishing':self.skills["fishing"], 'Cooking':self.skills["cooking"], 'Firemaking':self.skills["firemaking"], 'Woodcutting':self.skills["woodcutting"], 'Farming':self.skills["farming"], 'Quest Points':self.quest_points, 'Current Task':self.current_task, 'Objectives Completed':self.total}

                if quests_completed:
                    base_line["Quests Completed"] = quests_completed[0]
                    quests_completed.pop(0)
                if quests_unlocked:
                    base_line["Quests Unlocked"] = quests_unlocked[0]
                    quests_unlocked.pop(0)
                if quests_locked:
                    base_line["Quests Locked"] = quests_locked[0]
                    quests_locked.pop(0)

                writer.writerow(base_line)

                while(quests_completed or quests_unlocked or quests_locked):
                    line = {}
                    if quests_completed:
                        line["Quests Completed"] = quests_completed[0]
                        quests_completed.pop(0)
                    if quests_unlocked:
                        line["Quests Unlocked"] = quests_unlocked[0]
                        quests_unlocked.pop(0)
                    if quests_locked:
                        line["Quests Locked"] = quests_locked[0]
                        quests_locked.pop(0)
                    writer.writerow(line)

            if selector == "skills":
                base_line = {'Name': self.name, 'Member':self.member, 'Attack':self.skills["attack"], 'Strength':self.skills["strength"], 'Defence':self.skills["defence"], 'Ranged':self.skills["ranged"], 'Prayer':self.skills["prayer"], 'Magic':self.skills["magic"], 'Runecrafting':self.skills["runecrafting"], 'Construction':self.skills["construction"], 'Constitution':self.skills["constitution"], 'Agility':self.skills["agility"], 'Herblore':self.skills["herblore"], 'Thieving':self.skills["thieving"], 'Crafting':self.skills["crafting"], 'Fletching':self.skills["fletching"], 'Slayer':self.skills["slayer"],	'Hunter':self.skills["hunter"], 'Mining':self.skills["mining"], 'Smithing':self.skills["smithing"], 'Fishing':self.skills["fishing"], 'Cooking':self.skills["cooking"], 'Firemaking':self.skills["firemaking"], 'Woodcutting':self.skills["woodcutting"], 'Farming':self.skills["farming"], 'Quest Points':self.quest_points}
                writer.writerow(base_line)

            if selector == "quests":
                quests_completed = list(self.quests_completed)
                quests_unlocked = list(self.quests_unlocked)
                quests_locked = list(self.quests_locked)

                base_line = {}

                if quests_completed:
                    base_line["Quests Completed"] = quests_completed[0]
                    quests_completed.pop(0)
                if quests_unlocked:
                    base_line["Quests Unlocked"] = quests_unlocked[0]
                    quests_unlocked.pop(0)
                if quests_locked:
                    base_line["Quests Locked"] = quests_locked[0]
                    quests_locked.pop(0)

                writer.writerow(base_line)

                while(quests_completed or quests_unlocked or quests_locked):
                    line = {}
                    if quests_completed:
                        line["Quests Completed"] = quests_completed[0]
                        quests_completed.pop(0)
                    if quests_unlocked:
                        line["Quests Unlocked"] = quests_unlocked[0]
                        quests_unlocked.pop(0)
                    if quests_locked:
                        line["Quests Locked"] = quests_locked[0]
                        quests_locked.pop(0)
                    writer.writerow(line)


    def update_locked_quests(self, quest):
        self.quests_locked.add(quest)
        self.write_character_to_file("quests")

    def update_complete_quests(self, quest):
        self.quests_completed.add(quest)
        self.quests_unlocked.remove(quest)
        self.write_character_to_file("quests")


    def update_skills(self, skill, level):
        self.skills[skill] += (int)(level)
        self.write_character_to_file("skills")


    def canComplete(self, quest_list):
        temp = set()
        for key in quest_list:
            if(quest_list[key].canComplete(self)): 
                temp.add(quest_list[key].title)

        c = self.quests_unlocked | temp
        self.quests_unlocked = c
        locked_quests = [x for x in self.quests_locked if x not in temp]
        self.quests_locked = locked_quests

        self.write_character_to_file("quests")

    def toString(self):
        print("{} \n    Has Levels: {}".format(self.name, self.skills))
        print("    Is Combat Level: {} with {} Quest Points".format(self.combat_level, self.quest_points))
        print("    Has completed: ", end="")
        for quest in self.quests_completed:
            print(quest, end=", ")
        
        print("\n    Has Unlocked: ", end="")
        for quest in self.quests_unlocked:
            print(quest, end=", ")
    
        print("\n    Has Locked: ", end="")
        for quest in self.quests_locked:
            print(quest, end=", ")

        print("")


class Quest:

    def __init__(self, title="", skill_requirements = {}, quest_requirements={}, combat_requirement = 0, quest_point_requirement = 0, members=False):
        self.title = title
        self.members = members
        self.skill_requirements = skill_requirements
        self.quest_requirements = quest_requirements
        self.combat_requirement = combat_requirement
        self.quest_point_requirement = quest_point_requirement

    def canComplete(self, character):
        can_complete = True
        for key in self.skill_requirements:
            if self.skill_requirements[key] > character.skills[key]:
                can_complete = False

        for quest in self.quest_requirements:
            if quest not in character.quests_completed:
                can_complete = False
        if self.combat_requirement > character.combat_level:
            can_complete = False

        if self.quest_point_requirement > character.quest_points:
            can_complete = False
        return can_complete

    def toString(self):
        print(self.title)
        print("    Skill Requirements: {}".format(self.skill_requirements))
        print("    Quest Requirements: {}".format(self.quest_requirements))
        print("    Combat Requirements: {}".format(self.combat_requirement))
        print("    Quest Point Requirements: {}".format(self.quest_point_requirement))

def combat_level(attack, strength, defence, ranged, magic, constitution, prayer):
    base = floor(0.25*(defence + constitution + floor(prayer/2)))
    melee = 0.325*(attack + strength)
    ranged = 0.325*(floor(3*ranged/2))
    magic = 0.325*(floor(3*magic/2))
    maximum = max([melee, ranged, magic])
    return (int)(floor(base + maximum)+1)


def quest_list():
    quest_list = {}
    try:
        real_path = os.path.dirname(os.path.realpath(__file__))
        file_path = real_path+'/quest_list.csv'
        with open(file_path, encoding="utf-16", errors='ignore') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            skill = {}
            quest_point_requirement = 0
            combat_requirement = 0
            quest_requirements = set()
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                if line_count == 1:
                    title = row["Title"]
                    if row["Skill"] != "":
                        skill[row["Skill"]] = (int)(row["Level"])
                    if row["Quest Requirements"] != "":
                        quest_requirements.add(row["Quest Requirements"])
                    members = row["Member"]
                    
                if line_count > 1 and row["Title"] != "":    
                    skill_requirements = {}
                    skill_requirements.update(skill)
                    quest = Quest(title=title, skill_requirements=skill_requirements, quest_requirements=quest_requirements, members=members, quest_point_requirement=quest_point_requirement, combat_requirement=combat_requirement)
                    quest_list[title] = quest

                    skill = {}
                    quest_requirements = set()
                    combat_requirement = 0
                    quest_point_requirement = 0

                    title = row["Title"]
                    if row["Skill"] != "":
                        skill[row["Skill"]] = (int)(row["Level"])

                    if row["Quest Requirements"] != "":
                        quest_requirements.add(row["Quest Requirements"])

                    if row["Combat Requirement"] != "":
                        combat_requirement = (int)(row["Combat Requirement"])

                    if row["Quest Point Requirement"] != "":
                        quest_point_requirement = (int)(row["Quest Point Requirement"])


                    members = row["Member"]

                if line_count>1 and row["Title"] == "":
                    if row["Skill"] != "":
                        skill[row["Skill"]] = (int)(row["Level"])
                    if row["Quest Requirements"] != "":
                        quest_requirements.add(row["Quest Requirements"])

                
                line_count += 1
                
        skill_requirements = {}
        skill_requirements.update(skill)
        quest = Quest(title=title, skill_requirements=skill_requirements, quest_requirements=quest_requirements)
        quest_list[title] = quest

    except: 
        print("File not found")

    finally:
    
        return quest_list

def generate_scenario(character):
    if character.current_task == "":
        choice = random.randint(1, 101)
        if choice >= 98 and len(character.quests_unlocked) != 0:
            quest_list = list(character.quests_unlocked)
            quest_choice = quest_list[random.randint(0, len(character.quests_unlocked)-1)]
            print("You must complete the quest {}".format(quest_choice))
            character.current_task = "quest:"+quest_choice
            return
        if choice >= 95:
            task_choice = random.randint(0,2)
            if task_choice == 1:
                print("You must complete a diary task from the area you are currently in.")
                character.current_task = "task:1"
                return
            if task_choice == 2:
                print("You must complete a diary task from any area apart from the one you are currently in")
                character.current_task = "task:2"
                return
        if choice >= 90:
            print("Random event! Complete a slayer task!")
            character.current_task = "slayer"
            return
        else:
            skill_list = ["attack", "strength", "defence", "ranged", "prayer", "magic", "runecrafting", "construction", "constitution", "agility", "herblore", "thieving", "construction", "fletching", "slayer", "hunter", "mining", "smithing", "fishing", "cooking", "firemaking", "woodcutting", "farming"]
            skill_choice = skill_list[random.randint(0, 22)]

            while character.skills[skill_choice] == 99:
                skill_choice = skill_list[random.randint(0, 22)]


            x = (int)((100 - character.skills[skill_choice])/10)
            level = random.randint(1, x+1)

            print("You must level " + skill_choice + " by {} level(s) to achieve level {}".format(level, (str)(character.skills[skill_choice]+(int)(level))))
            character.current_task = "skill:"+skill_choice+":"+(str)(level)+":"+ (str)(character.skills[skill_choice]+(int)(level))
            return

    current_task = character.current_task.split(":")
    if current_task[0] == "quest":
        print("You're current task is to complete the quest: {}".format(current_task[1]))
    if current_task[0] == "skill":
        print("You're current task is to level {} by {} level(s) to achieve level {}".format(current_task[1], current_task[2], current_task[3]))
    if current_task[0] == "task":
        if current_task[1] == 1:
            print("Your current task is to complete a diary task from the area you are currently in.")
        else:
            print("Your current task is to complete a diary task from any area except the one you are in.")
    if current_task[0] == "slayer":
            print("You're current task is to complete a slayer assignment.")
    return

def scenario_complete(character):
    if character.current_task == "":
        print("No task currently set")
        return True

    current_task = character.current_task.split(":")
    complete = input("Objective complete (y/n)?: ")
    if current_task[0] == "skill":
        if complete == "y":
            character.update_skills(current_task[1], current_task[2])
            character.current_task = ""
            character.total = (int)(character.total) + 1
            return True
    if current_task[0] == "quest":
        if complete == "y":
            character.update_complete_quests(current_task[1])
            character.current_task = ""
            return True
    if current_task[0] == "task":
        if complete == "y":
            character.current_task = ""
            return True
    if current_task[0] == "slayer":
        if complete == "y":
            character.current_task = ""
            return True
    if complete == "skip":
        character.current_task = ""
        return False
    if complete == "exit":
        return False

    return True
    
quest_list = quest_list()

"""
for key in quest_list:
    (myCharacter.quests_locked).add(quest_list[key].title)
myCharacter.canComplete(quest_list)
"""

character_name = input("Enter your characters name: ")
if character_name == "exit":
    exit()
myCharacter = Character(character_name)
print("Enter 'exit' at any time to go back.")
game_loop = True

while(game_loop):
    game_selection = input("1: Generate Scenario \n2: Update Levels\n")
    if game_selection == "exit":
        game_loop = False
        break
    if game_selection == "1":
        generate_loop = True
        while(generate_loop):
            generate_scenario(myCharacter)
            generate_loop = scenario_complete(myCharacter)
    if game_selection == "2":
        update_loop = True
        while(update_loop):
            skill = input("Enter skill to update: ")
            if skill == "exit":
                update_loop = False
                break
            level = input("Enter level: ")
            if level == "exit":
                update_loop = False
                break
            myCharacter.skills[skill] = (int)(level)

myCharacter.write_character_to_file()
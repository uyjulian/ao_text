from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0100_1.bin",                # FileName
        "c0100",                    # MapName
        "c0100",                    # Location
        0x0004,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 24000, 500, 30, 45, 0, 360, 1100, 0, -3500, 0, 0, 1, 4, 0, 7, 0, 8],
    )

    BuildStringList((
        "c0100_1",                # 0
    ))

    ChipFrameInfo(256, 0)                                        # 0

    ScpFunction((
        "Function_0_100",          # 00, 0
        "Function_1_DEA",          # 01, 1
        "Function_2_20A5",         # 02, 2
        "Function_3_2E47",         # 03, 3
        "Function_4_3498",         # 04, 4
        "Function_5_40FA",         # 05, 5
        "Function_6_4337",         # 06, 6
        "Function_7_4651",         # 07, 7
        "Function_8_4DCE",         # 08, 8
        "Function_9_4EE8",         # 09, 9
        "Function_10_56B2",        # 0A, 10
        "Function_11_605D",        # 0B, 11
        "Function_12_6304",        # 0C, 12
        "Function_13_6F23",        # 0D, 13
        "Function_14_7077",        # 0E, 14
        "Function_15_71D2",        # 0F, 15
        "Function_16_72FC",        # 10, 16
        "Function_17_7392",        # 11, 17
        "Function_18_73F8",        # 12, 18
        "Function_19_745B",        # 13, 19
        "Function_20_7594",        # 14, 20
        "Function_21_8EE3",        # 15, 21
        "Function_22_9453",        # 16, 22
        "Function_23_9614",        # 17, 23
        "Function_24_9B5A",        # 18, 24
        "Function_25_9CD7",        # 19, 25
        "Function_26_A1D0",        # 1A, 26
    ))


    def Function_0_100(): pass

    label("Function_0_100")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1A1")

    ChrTalk(
        0xFE,
        (
            "I think I finally got out … …\x01",
            "What is the tree floating in that sky?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It surely does not fall anywhere, is it?\x01",
            "…… I am worried and insecure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE6")

    label("loc_1A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1AF")
    Jump("loc_DE6")

    label("loc_1AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_334")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29F")

    ChrTalk(
        0xFE,
        (
            "Accidents happened in the past,\x01",
            "It was due to the \"dark fight\" of the two major powers … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, the spies between the two countries\x01",
            "What was the result of mutually getting along?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Honestly I did not think deeply,\x01",
            "If that is true you can not forgive.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_32F")

    label("loc_29F")


    ChrTalk(
        0xFE,
        (
            "Accidents happened in the past,\x01",
            "It was due to the \"dark fight\" of the two major powers … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Honestly I did not think deeply,\x01",
            "If that is true you can not forgive.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32F")

    Jump("loc_DE6")

    label("loc_334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_468")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EF")

    ChrTalk(
        0xFE,
        (
            "I hired that armed group\x01",
            "It's rumored that even the Imperial government … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In that sense, when\x01",
            "You do not know whether it attacks you, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I think so, I am very anxious …\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_463")

    label("loc_3EF")


    ChrTalk(
        0xFE,
        (
            "I hired that armed group\x01",
            "It's rumored that even the Imperial government … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I think of when I will attack again,\x01",
            "I am terribly uneasy …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_463")

    Jump("loc_DE6")

    label("loc_468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_505")

    ChrTalk(
        0xFE,
        (
            "People in Mainz, surely\x01",
            "I think I have a hard time these days …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "People with weapons\x01",
            "Suddenly I got on board,\x01",
            "I am afraid just to imagine … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE6")

    label("loc_505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_572")

    ChrTalk(
        0xFE,
        "Today I was asked to use mama.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… … Because it leaked out,\x01",
            "Please buy an urgent bucket.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE6")

    label("loc_572")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5CB")

    ChrTalk(
        0xFE,
        (
            "It's like that an ambulance will go out so much …\x01",
            "It seems that a pretty big accident happened.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE6")

    label("loc_5CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_655")

    ChrTalk(
        0xFE,
        "Do I really want to live by myself?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There is surely a yearning,\x01",
            "I only have one person at home\x01",
            "It feels quite lonesome …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE6")

    label("loc_655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_768")

    ChrTalk(
        0xFE,
        (
            "Byte, byte ……\x01",
            "I wonder if you are in a safe place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, if you earn efficiently\x01",
            "Also the choice of hostess … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……No no no,\x01",
            "I wonder what I am thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter how much you earn, Ogasan's\x01",
            "It is impossible for you to drink alcohol.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7B3")

    label("loc_768")


    ChrTalk(
        0xFE,
        (
            "If I want to live alone, I should byte a … …\x01",
            "What kind of work is suitable for me?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B3")

    Jump("loc_DE6")

    label("loc_7B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_97F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EA")

    ChrTalk(
        0xFE,
        (
            "If you live alone, personally\x01",
            "I think that Nishi-dori direction is the best … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Considering rents or realistic lines,\x01",
            "After all, you settle down to East Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although the old city is exceptional for fluffy,\x01",
            "I'm more concerned about security than anything ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Or, if you stand on your own\x01",
            "I must search bytes before that.\x01",
            "… ….\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_97A")

    label("loc_8EA")


    ChrTalk(
        0xFE,
        (
            "If you live alone, personally\x01",
            "I think that Nishi-dori direction is the best … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Or, if you stand on your own\x01",
            "I must search bytes before that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97A")

    Jump("loc_DE6")

    label("loc_97F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_9E0")

    ChrTalk(
        0xFE,
        "Oh, it is already such a time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Go home soon\x01",
            "I have to help Mama.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE6")

    label("loc_9E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A83")

    ChrTalk(
        0xFE,
        (
            "The heads of the crossbells also enter\x01",
            "As soon as you finish it is not it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone was riding a car\x01",
            "I did not understand well ….\x01",
            "Only VIP impression came.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE6")

    label("loc_A83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_BD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B37")

    ChrTalk(
        0xFE,
        (
            "Just as with the trade council from tomorrow,\x01",
            "It feels a bit strange to running around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A while ago, I was patrolling\x01",
            "Having been caught by a police officer,\x01",
            "I was asked my first duties questions in my life.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BCC")

    label("loc_B37")


    ChrTalk(
        0xFE,
        (
            "I was the first to ask a job question,\x01",
            "I will excuse some people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not think anyone can help with housework\x01",
            "I do not want to say it in a loud voice ……\x01",
            "I'm terrified.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCC")

    Jump("loc_DE6")

    label("loc_BD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C4F")

    ChrTalk(
        0xFE,
        (
            "I am in the house because it's raining\x01",
            "I dislike being standing still.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Put in your favorite umbrella,\x01",
            "Let's take a walk, ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE6")

    label("loc_C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_DE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD9")

    ChrTalk(
        0xFE,
        (
            "A lot of police cars came out\x01",
            "I was surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, it seems that it seems like the police\x01",
            "It might be cool.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE6")

    label("loc_CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D93")

    ChrTalk(
        0xFE,
        (
            "How come my dad is already\x01",
            "I wonder about walking around the house naked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Consideration for daughter around the age\x01",
            "To say that it is missing …… It is no longer a crime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, I want to live by myself ~.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DE6")

    label("loc_D93")


    ChrTalk(
        0xFE,
        "Oh, I want to live by myself ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, somewhere\x01",
            "I wonder if there are no good properties.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE6")

    TalkEnd(0xFE)
    Return()

    # Function_0_100 end

    def Function_1_DEA(): pass

    label("Function_1_DEA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_FBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F0D")

    ChrTalk(
        0xFE,
        (
            "Although details are not clear well,\x01",
            "Apparently that \"God machine\" or something\x01",
            "It seems weapons have been lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Regardless of the method's promise ……\x01",
            "President Dieter certainly\x01",
            "He had prepared the power to protect the crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a result, although it caused great confusion,\x01",
            "I can not blame him very much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_FB8")

    label("loc_F0D")


    ChrTalk(
        0xFE,
        (
            "Regardless of the method's promise ……\x01",
            "President Dieter certainly\x01",
            "He had prepared the power to protect the crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a result, although it caused great confusion,\x01",
            "I can not blame him very much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB8")

    Jump("loc_20A1")

    label("loc_FBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_FCB")
    Jump("loc_20A1")

    label("loc_FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1133")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_109E")

    ChrTalk(
        0xFE,
        "Hmm … … declaring asset freezing,?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No doubt Mayor Mayor Dieter\x01",
            "I do not think I will take hard-line measures … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, as he says, for us to stand up\x01",
            "Maybe it is not timely besides now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_112E")

    label("loc_109E")


    ChrTalk(
        0xFE,
        (
            "No doubt Mayor Mayor Dieter\x01",
            "I do not think I will take hard-line measures … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But certainly, for us to stand up\x01",
            "Maybe it is not timely besides now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_112E")

    Jump("loc_20A1")

    label("loc_1133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_12D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1236")

    ChrTalk(
        0xFE,
        (
            "The attack of the other day … …\x01",
            "That is decided as the work of the empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Recently I seem to have covered a cat,\x01",
            "Originally, the choice of means is their nature … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Roundabout, using mean means\x01",
            "It is aiming for aggression at all … …\x01",
            "That is Elebonia!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_12D3")

    label("loc_1236")


    ChrTalk(
        0xFE,
        (
            "The attack of the other day … …\x01",
            "That is decided as the work of the empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Roundabout, using mean means\x01",
            "It is aiming for aggression at all … …\x01",
            "That is Elebonia!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D3")

    Jump("loc_20A1")

    label("loc_12D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1370")

    ChrTalk(
        0xFE,
        "In this incident, empire behind the back … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Hmm, if so\x01",
            "Just just following you as before\x01",
            "Crossbell may be defending and breaking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A1")

    label("loc_1370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_137E")
    Jump("loc_20A1")

    label("loc_137E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_146F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_141A")

    ChrTalk(
        0xFE,
        (
            "In the west, something\x01",
            "It seems it was also an accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Kawabori Kawaraga ……\x01",
            "The goddess of the sky#8REarth#Okay, please protect everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_146A")

    label("loc_141A")


    ChrTalk(
        0xFE,
        (
            "Kawabori Kawaraga ……\x01",
            "The goddess of the sky#8REarth#Okay, please protect everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_146A")

    Jump("loc_20A1")

    label("loc_146F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1593")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1536")

    ChrTalk(
        0xFE,
        (
            "Although it can not be said unconditionally,\x01",
            "Apparently the younger generation is\x01",
            "There seems to be many people who agree on independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Generations that do not know the conflict, or …\x01",
            "I really know the seriousness of things\x01",
            "I'm worried about whether you are a male.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_158E")

    label("loc_1536")


    ChrTalk(
        0xFE,
        (
            "Generations that do not know the conflict, or …\x01",
            "I really know the seriousness of things\x01",
            "I'm worried about whether you are a male.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_158E")

    Jump("loc_20A1")

    label("loc_1593")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_169A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1660")

    ChrTalk(
        0xFE,
        (
            "Hmm, honestly\x01",
            "At the age of this year the word \"independence\"\x01",
            "I did not expect to hear it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Independence or independence ……\x01",
            "It surely feels like a dream if it can be realized,\x01",
            "I do not think it will go well … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1695")

    label("loc_1660")


    ChrTalk(
        0xFE,
        (
            "Independence or independence ……\x01",
            "Would it be a dream come true?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1695")

    Jump("loc_20A1")

    label("loc_169A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_18A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1811")

    ChrTalk(
        0xFE,
        (
            "Trade councils can not listen,\x01",
            "It is not relayed by conductivity communication.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In other words,\x01",
            "Through the publicity of the city and stakeholders\x01",
            "You know it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Especially in general it was unknown\x01",
            "Cross Bell Times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Reliability, stability, speed of articles …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whichever we take, in this place\x01",
            "Beats the Crossbell Times\x01",
            "Information sources do not exist easily.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18A4")

    label("loc_1811")


    ChrTalk(
        0xFE,
        (
            "Trade councils can not listen,\x01",
            "It is not relayed by conductivity communication.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In other words,\x01",
            "Through the publicity of the city and stakeholders\x01",
            "You know it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18A4")

    Jump("loc_20A1")

    label("loc_18A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_19E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_196E")

    ChrTalk(
        0xFE,
        (
            "Oh, if you notice it already\x01",
            "Is not the sun going down?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hokkaido, this is also a trade meeting\x01",
            "I was exposed to the air.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The old lady went back to her early in the morning.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19DB")

    label("loc_196E")


    ChrTalk(
        0xFE,
        (
            "Oh, if you notice it already\x01",
            "Is not the sun going down?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The old lady went back to her early in the morning.\x02",
    )

    CloseMessageWindow()

    label("loc_19DB")

    Jump("loc_20A1")

    label("loc_19E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1CB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A71")

    ChrTalk(
        0xFE,
        (
            "In the restaurant there\x01",
            "A woman in the eastward style entered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I got an intellectual face.\x01",
            "It was a beautiful woman.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CAB")

    label("loc_1A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C0E")

    ChrTalk(
        0xFE,
        (
            "Hmm, the new city hall building\x01",
            "Did it appear properly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is actually five years since the announcement of the architectural plan.\x01",
            "Rumor is at least one more year until completion\x01",
            "I was told that it would take … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Immediately after the inauguration of the mayor of Croix IBC\x01",
            "It is decided to introduce capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to that, for a bullshit conflict\x01",
            "Construction proceeded at a rapid pitch without being affected,\x01",
            "Finally it was completed on the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ho ho ho, truth\x01",
            "Mayor Claise Mayor.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CAB")

    label("loc_1C0E")


    ChrTalk(
        0xFE,
        (
            "It is actually five years since the announcement of the architectural plan.\x01",
            "Rumor is at least one more year until completion\x01",
            "I was told that it would take … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ho ho ho, truth\x01",
            "Mayor Claise Mayor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CAB")

    Jump("loc_20A1")

    label("loc_1CB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1E23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D99")

    ChrTalk(
        0xFE,
        (
            "Hmm, it's time to start from tomorrow\x01",
            "The trade meeting will start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mayor Clois Mayor\x01",
            "Anyway, as well as being the mayor\x01",
            "It is the president of IBC.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At the conference its leadership\x01",
            "I do not expect you to demonstrate it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E1E")

    label("loc_1D99")


    ChrTalk(
        0xFE,
        (
            "Hmm, it's time to start from tomorrow\x01",
            "The trade meeting will start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To Mayor of Crois,\x01",
            "Make that leadership fully\x01",
            "I do not want you to demonstrate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E1E")

    Jump("loc_20A1")

    label("loc_1E23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1E31")
    Jump("loc_20A1")

    label("loc_1E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_20A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EA9")

    ChrTalk(
        0xFE,
        (
            "Also from here,\x01",
            "I saw an arrest play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Police are quite\x01",
            "You seem to be doing your best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A1")

    label("loc_1EA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FDB")

    ChrTalk(
        0xFE,
        (
            "Empire and republican parties involved in the case incident\x01",
            "Councilor for corruption disappears, from the back society\x01",
            "That Rubathe shop also disappeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so,\x01",
            "Representatives of imperialists still have seats\x01",
            "The current situation of going to the top has changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Speedup of law amendment etc.\x01",
            "I can tell you about a good fight …… Mayor Croise\x01",
            "I hope I will work harder.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20A1")

    label("loc_1FDB")


    ChrTalk(
        0xFE,
        "…… It sure was a black moon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rubache is gone,\x01",
            "Yatsura started making width\x01",
            "There are also rumors that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Legal making for citizens to live in peace … …\x01",
            "To Mayor of Crois, more\x01",
            "I will not do my best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A1")

    TalkEnd(0xFE)
    Return()

    # Function_1_DEA end

    def Function_2_20A5(): pass

    label("Function_2_20A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2147")

    ChrTalk(
        0xFE,
        (
            "Well, I am going\x01",
            "I will return to the Orkis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The city office is also in the middle of confusion,\x01",
            "Anyway, not to make a face\x01",
            "It does not start.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E43")

    label("loc_2147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2155")
    Jump("loc_2E43")

    label("loc_2155")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2163")
    Jump("loc_2E43")

    label("loc_2163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_22C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2235")

    ChrTalk(
        0xFE,
        "Hello, Mimi is innocent and cute.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But even so\x01",
            "Why armed groups tell Crossbell's bell\x01",
            "I guess I took it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's so much worth stolen\x01",
            "I do not think there is something … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_22C0")

    label("loc_2235")


    ChrTalk(
        0xFE,
        (
            "Even so,\x01",
            "Why armed groups tell Crossbell's bell\x01",
            "I guess I took it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's so much worth stolen\x01",
            "I do not think there is something … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22C0")

    Jump("loc_2E43")

    label("loc_22C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_231C")

    ChrTalk(
        0xFE,
        (
            "People in Mainz are worried …\x01",
            "I wonder there are also Mimi's children.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E43")

    label("loc_231C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2385")

    ChrTalk(
        0xFE,
        "Look, Mimi.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dendenbutsu on the handrail\x01",
            "I'm back and forth.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E43")

    label("loc_2385")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2424")

    ChrTalk(
        0xFE,
        (
            "It is commonplace ….\x01",
            "The ambulance was pretty quick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For emergency vehicles\x01",
            "Although there is no speed limit,\x01",
            "When you are watching it will smile a little.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E43")

    label("loc_2424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_25A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_251D")

    ChrTalk(
        0xFE,
        "Well, guess what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However,\x01",
            "The market is still too expensive\x01",
            "People can not handle it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though it is still difficult, half of now\x01",
            "Even if it only lowers about 20\x01",
            "It's pretty easy to get out of hand.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_25A1")

    label("loc_251D")


    ChrTalk(
        0xFE,
        "Well, guess what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is impossible right now,\x01",
            "At the very least, when I reach the retirement age\x01",
            "I want to get it anyhow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25A1")

    Jump("loc_2E43")

    label("loc_25A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2797")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26ED")

    ChrTalk(
        0xFE,
        (
            "Recently, in the world\x01",
            "Just about talking about independence\x01",
            "It seems that attention is going on ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just the other day, the revision of the basic traffic law\x01",
            "Do not forget what you did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the next law amendment,\x01",
            "In addition to the penalty system so far\x01",
            "\"License suspension system\" was added.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With a little power guide by this\x01",
            "I hope the accident will decrease.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2792")

    label("loc_26ED")


    ChrTalk(
        0xFE,
        (
            "If you commit a certain violation in the future,\x01",
            "Driver's license stopped for a certain period …\x01",
            "That means you can not drive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With a little power guide by this\x01",
            "I hope the accident will decrease.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2792")

    Jump("loc_2E43")

    label("loc_2797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_27A5")
    Jump("loc_2E43")

    label("loc_27A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2806")

    ChrTalk(
        0xFE,
        (
            "Well, let me wait.\x01",
            "I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well then, shall we go there immediately?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E43")

    label("loc_2806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2814")
    Jump("loc_2E43")

    label("loc_2814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_289A")

    ChrTalk(
        0xFE,
        (
            "Along with the complete relocation of the city hall,\x01",
            "For a while for the Orkis Tower\x01",
            "I decided to pack it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, I'm getting busy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E43")

    label("loc_289A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2C1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BAC")

    ChrTalk(
        0xFE,
        (
            "I saw it yesterday, though ….\x01",
            "You guys, a very rare guide car\x01",
            "You seem to be riding?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, in fact\x01",
            "It is ZCF's new type of power guide car.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    ChrTalk(
        0xFE,
        "Why, that ZCF is a driving car! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "By the way, do you know the maximum speed?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FYes, I have not tried it yet,\x01",
            "1500 Sergei seems to be hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wha … …!\x01",
            "With that type and its speed,\x01",
            "ZCF did it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, what is that.\x01",
            "Conductive vehicle manufacturers are now\x01",
            "I will finally enter the 3 strong era.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, if it becomes like this in the future\x01",
            "It will be more and more fun!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FIs not it ~!\x02\x03",
            "With this competition getting overheated,\x01",
            "More amazing kids are getting more and more ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x109, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#00012FYou know, it is quite exciting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109FHehe, I really like Noel.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 0)
    Jump("loc_2C1A")

    label("loc_2BAC")


    ChrTalk(
        0xFE,
        (
            "No way, that ZCF\x01",
            "I guess that he was developing a driving vehicle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, this will continue\x01",
            "Keep an eye on the trends of each company!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C1A")

    Jump("loc_2E43")

    label("loc_2C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2E43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CA5")

    ChrTalk(
        0xFE,
        (
            "Again the development of the traffic law\x01",
            "I have to do it as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is important to let Mimi play alone\x01",
            "I will be scared.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E43")

    label("loc_2CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D87")

    ChrTalk(
        0xFE,
        (
            "Before this, at a tremendous speed\x01",
            "Run through this central square\x01",
            "I saw a guided vehicle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it was clearly dangerous speed,\x01",
            "I immediately informed the police ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if it was caught properly.\x01",
            "… … I'm worried about it again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2E43")

    label("loc_2D87")


    ChrTalk(
        0xFE,
        (
            "Nonetheless, with the current basic traffic law\x01",
            "Even if it is caught in dangerous driving\x01",
            "I am fine only with a fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Recently, even in Congress\x01",
            "It is a place we are stepping up to strengthen penalties\x01",
            "I'm expecting it in the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E43")

    TalkEnd(0xFE)
    Return()

    # Function_2_20A5 end

    def Function_3_2E47(): pass

    label("Function_3_2E47")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2EFB")

    ChrTalk(
        0xFE,
        (
            "Because my husband returns to the city hall\x01",
            "I think that we will also return to the house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I am worried about various things in the future … …\x01",
            "As long as the family is together,\x01",
            "I feel like I can survive anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3494")

    label("loc_2EFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2F09")
    Jump("loc_3494")

    label("loc_2F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2FAA")

    ChrTalk(
        0xFE,
        (
            "There is no help but …\x01",
            "The appearance of tourists in this week\x01",
            "You almost disappeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Cross Bell\x01",
            "I wonder what will go on ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3494")

    label("loc_2FAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3044")

    ChrTalk(
        0xFE,
        (
            "Since the guide's work is off for the time being,\x01",
            "Now I have three family members.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried about the previous things, but ….\x01",
            "I can save my child's smile.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3494")

    label("loc_3044")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3052")
    Jump("loc_3494")

    label("loc_3052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3060")
    Jump("loc_3494")

    label("loc_3060")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_306E")
    Jump("loc_3494")

    label("loc_306E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_307C")
    Jump("loc_3494")

    label("loc_307C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_308A")
    Jump("loc_3494")

    label("loc_308A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_325C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31AE")

    ChrTalk(
        0xFE,
        "Eh, Kohon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can see behind everyone on the right hand side,\x01",
            "It is \"Oval Store\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Its name is \"Genten\"\x01",
            "Conductive products gather in the continent\x01",
            "It is famous as a shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Citizen, of course,\x01",
            "Popular with tourists as well\x01",
            "It is a shop that goes at the cutting edge of the times.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3257")

    label("loc_31AE")


    ChrTalk(
        0xFE,
        (
            "Eh, what you can see right behind everyone,\x01",
            "Oval store \"Genten\" is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Citizen, of course,\x01",
            "Popular with tourists as well\x01",
            "It is a shop that goes at the cutting edge of the times.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3257")

    Jump("loc_3494")

    label("loc_325C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_32A3")

    ChrTalk(
        0xFE,
        (
            "Yeah, let's go ahead.\x01",
            "Mimi and I are hungry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3494")

    label("loc_32A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_346F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32BE")
    Call(1, 6)
    Jump("loc_346A")

    label("loc_32BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D8")

    ChrTalk(
        0xFE,
        "Eh, Kohon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can see it on your right hand side,\x01",
            "It is \"Bell of Crossbell\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Its origins are old and over 500 years ago,\x01",
            "It is said to go back to the medieval era.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since being excavated in the Seven Year calendar year 1185,\x01",
            "Today as a symbol of the city\x01",
            "It is familiar among citizens.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_346A")

    label("loc_33D8")


    ChrTalk(
        0xFE,
        (
            "Well, you can see it on your right,\x01",
            "It is \"Bell of Crossbell\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Its origins are old and over 500 years ago,\x01",
            "It is said to go back to the medieval era.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_346A")

    Jump("loc_3494")

    label("loc_346F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_347D")
    Jump("loc_3494")

    label("loc_347D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_348B")
    Jump("loc_3494")

    label("loc_348B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3494")

    label("loc_3494")

    TalkEnd(0xFE)
    Return()

    # Function_3_2E47 end

    def Function_4_3498(): pass

    label("Function_4_3498")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_35DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_357E")

    ChrTalk(
        0xFE,
        (
            "Dad, from now on again\x01",
            "I go to work ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, Lloyd guys as well\x01",
            "You are on the job forever, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mimi, everyone's thing too\x01",
            "I will support you so please do your best!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_35D5")

    label("loc_357E")


    ChrTalk(
        0xFE,
        (
            "Papa and Lloyd guys as well\x01",
            "I am doing my best at work and great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Mimi is going to support you as well.\x02",
    )

    CloseMessageWindow()

    label("loc_35D5")

    Jump("loc_40F6")

    label("loc_35DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_35E8")
    Jump("loc_40F6")

    label("loc_35E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_36BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3652")

    ChrTalk(
        0xFE,
        (
            "A guide car with that screen,\x01",
            "It was cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "My father seems to be pleased.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_36B6")

    label("loc_3652")


    ChrTalk(
        0xFE,
        (
            "Dad, city hall work\x01",
            "He got busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Conversely, I have a mother\x01",
            "The travel company is closed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36B6")

    Jump("loc_40F6")

    label("loc_36BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_378C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3750")

    ChrTalk(
        0xFE,
        (
            "Eh, what you see on the right of everyone\x01",
            "It is a crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is it allele?\x01",
            "Kane has gone somewhere?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3787")

    label("loc_3750")


    ChrTalk(
        0xFE,
        (
            "Cross Bell's Kane,\x01",
            "Where have you gone?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3787")

    Jump("loc_40F6")

    label("loc_378C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_38E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3882")

    ChrTalk(
        0xFE,
        (
            "Something, today\x01",
            "Many people have an obstinate face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, Lloyd's kids ……\x01",
            "I'm afraid I'm getting cheerful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, yes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FThank you, Mimi-chan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No.\x01",
            "You are welcome.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_38DF")

    label("loc_3882")


    ChrTalk(
        0xFE,
        (
            "Something, today\x01",
            "Many people have an obstinate face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Everyone will be laughed at by Mr. Sun.\x02",
    )

    CloseMessageWindow()

    label("loc_38DF")

    Jump("loc_40F6")

    label("loc_38E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_392C")

    ChrTalk(
        0xFE,
        "Wow, that is true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Perhaps it is a lost child?\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F6")

    label("loc_392C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_399C")

    ChrTalk(
        0xFE,
        (
            "When an ambulance passes,\x01",
            "Everybody has to give way\x01",
            "I can not do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That is a traffic rule.\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F6")

    label("loc_399C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3A57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A1C")

    ChrTalk(
        0xFE,
        "ぷ ぷ ~, ぷ ぷ ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dad, again\x01",
            "I guess you are thinking about a car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I really do love you ~.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3A52")

    label("loc_3A1C")


    ChrTalk(
        0xFE,
        "ぷ ぷ ~, ぷ ぷ ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The passenger's seat belongs to Mimi.\x02",
    )

    CloseMessageWindow()

    label("loc_3A52")

    Jump("loc_40F6")

    label("loc_3A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3B1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AC7")

    ChrTalk(
        0xFE,
        (
            "Eh, everyone's\x01",
            "What can you see on the right …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Is it? Is it? Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, right hand is your right hand?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3B18")

    label("loc_3AC7")


    ChrTalk(
        0xFE,
        (
            "Well, Mom\x01",
            "What did he say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What can be seen on the right …… Right hand?\x02",
    )

    CloseMessageWindow()

    label("loc_3B18")

    Jump("loc_40F6")

    label("loc_3B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3BA1")

    ChrTalk(
        0xFE,
        "Hmm, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do not miss this souvenir\x01",
            "There is no choice but to buy it.\x01",
            "Pasha, Pashak.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40F6")

    label("loc_3BA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3C04")

    ChrTalk(
        0xFE,
        "Dining out, eating out, today's eating out ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mimi, the shop of east street\x01",
            "I want to eat \"Chu\"?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40F6")

    label("loc_3C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3C92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C1F")
    Call(1, 6)
    Jump("loc_3C8D")

    label("loc_3C1F")


    ChrTalk(
        0xFE,
        "Hmm, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is definitely a picture\x01",
            "I have to accommodate it.\x01",
            "Pasha, Pashak.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C8D")

    Jump("loc_40F6")

    label("loc_3C92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3F8F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EAC")
    TurnDirection(0xB, 0x1A2, 0)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "Oh, Lloyd's guys\x01",
            "I'm taking Mimi's unknown child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Eh, that clothes are cool.\x01",
            "Do you mean wind and wind?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        (
            "How to notice the goodness of this clothes\x01",
            "You have quite a chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Huhun, this is only one thing in the world\x01",
            "You are tailor - made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Whoops?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, that's it.\x01",
            "It was a maid 's clothes.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "No, that's not the case ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(Hello, these two people also exchange\x01",
            "Something fresh and funny. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DC, 6)
    Jump("loc_3F1A")

    label("loc_3EAC")

    TurnDirection(0xB, 0x1A2, 0)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "Made san.\x01",
            "Who is it, is not it really a girl?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "So it is different …\x02",
    )

    CloseMessageWindow()

    label("loc_3F1A")

    Jump("loc_3F8A")

    label("loc_3F1F")


    ChrTalk(
        0xFE,
        (
            "Dad, with Mimi for a while\x01",
            "You will not play around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But, because I work, I have to put up with it.\x02",
    )

    CloseMessageWindow()

    label("loc_3F8A")

    Jump("loc_40F6")

    label("loc_3F8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4044")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FAA")
    Call(1, 5)
    Jump("loc_403F")

    label("loc_3FAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4000")

    ChrTalk(
        0xFE,
        "Pitchi Pitch, ぴ っ ち ぴ っ ち ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's raining today, is not it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_403F")

    label("loc_4000")


    ChrTalk(
        0xFE,
        (
            "Mimi's father\x01",
            "There is no eye on the driving vehicle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Do not mind.\x02",
    )

    CloseMessageWindow()

    label("loc_403F")

    Jump("loc_40F6")

    label("loc_4044")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_40F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40A7")

    ChrTalk(
        0xFE,
        (
            "Car, keep the rules\x01",
            "Let's get on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I know Mimi too ~.\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F6")

    label("loc_40A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40B9")
    Call(1, 5)
    Jump("loc_40F6")

    label("loc_40B9")


    ChrTalk(
        0xFE,
        (
            "Everyone in the New Kamushi Shima.\x01",
            "Do your best at work~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40F6")

    TalkEnd(0xFE)
    Return()

    # Function_4_3498 end

    def Function_5_40FA(): pass

    label("Function_5_40FA")


    ChrTalk(
        0xB,
        (
            "Oh, Eloy to Lloyd!\x01",
            "in addition……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "Oh, Tio and\x01",
            "Randy-kun, what is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Turnaround,\x01",
            "Are you still closed for a while?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FNo, that's why\x01",
            "I do not have it …\x02\x03",
            "#00000FTwo people are still\x01",
            "There are other jobs to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYeah, and these two\x01",
            "He is a new member of the Special Affairs Division.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        "Oh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well then, from now on\x01",
            "It's a new blindfold ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FWell, how come?\x01",
            "Is not it an accurate naming?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FHuhuu, thanks in the future.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Yes, my regards!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 1)
    Return()

    # Function_5_40FA end

    def Function_6_4337(): pass

    label("Function_6_4337")

    OP_4B(0xB, 0xFF)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xB, 0x0, 0)
    TurnDirection(0xF, 0x0, 0)

    ChrTalk(
        0xB,
        "Oh, they are Lloyd's.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I will introduce Mimi's mother.\x01",
            "I am doing sightseeing guide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Huhuu, nice to meet you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Always my daughter\x01",
            "He seems to be caring\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, such a thing\x01",
            "I have not done anything serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FEven so, sightseeing guides\x01",
            "It is wonderful to be done.\x02\x03",
            "Are you still working today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "No, it is during the trade meeting\x01",
            "Have a day off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "So, during that time, with this girl\x01",
            "I plan to spend time with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FWell, it is a uniform, is not it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Well, that is ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Mimi asked me to wear it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I will be learning the guide from now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHaha, I see.\x01",
            "That was good, was not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Yes, I see. ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Lloyd's guys as well\x01",
            "Please be careful and go.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x0, 0x0)
    OP_93(0xB, 0x0, 0x0)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0xB, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x14A, 2)
    Return()

    # Function_6_4337 end

    def Function_7_4651(): pass

    label("Function_7_4651")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_468D")

    ChrTalk(
        0xFE,
        (
            "What an enormous tree …\x01",
            "Is not it impossible?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DCA")

    label("loc_468D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_469B")
    Jump("loc_4DCA")

    label("loc_469B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_46D1")

    ChrTalk(
        0xFE,
        "Arios, you were super cool ~!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DCA")

    label("loc_46D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4747")

    ChrTalk(
        0xFE,
        (
            "Today is the administrative district\x01",
            "What is a charity event?\x01",
            "It looks like you're doing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Why do not you go looking at some?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DCA")

    label("loc_4747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4806")

    ChrTalk(
        0xFE,
        (
            "It's too scary to be a mysterious armed group.\x01",
            "To prevent them from being licked\x01",
            "Dad says it should be independent … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Was it a referendum?\x01",
            "I could vote for 18, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DCA")

    label("loc_4806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4814")
    Jump("loc_4DCA")

    label("loc_4814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4863")

    ChrTalk(
        0xFE,
        (
            "The ambulance was terrible momentum.\x01",
            "…… I hurry to have an accident, but I do not mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DCA")

    label("loc_4863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_48E4")

    ChrTalk(
        0xFE,
        "Eh, I will stop dieting! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mumumu, since he made a strangely clever face ……\x01",
            "I will not be like you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DCA")

    label("loc_48E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4949")

    ChrTalk(
        0xFE,
        "…………………………………….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… If you do anything,\x01",
            "Do you exercise or restrict your diet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DCA")

    label("loc_4949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_49E6")

    ChrTalk(
        0xFE,
        (
            "Hey, Arios-sama and\x01",
            "Albert Okamoto,\x01",
            "It seems that everything is quite good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good ~, if you can\x01",
            "I also want to get along with the two of you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DCA")

    label("loc_49E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4A58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A06")
    Call(1, 8)
    ClearChrFlags(0xC, 0x10)
    Jump("loc_4A53")

    label("loc_4A06")


    ChrTalk(
        0xFE,
        "Hmm, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(… with this condition\x01",
            "I do not do it at all. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A53")

    Jump("loc_4DCA")

    label("loc_4A58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4B1A")

    ChrTalk(
        0xFE,
        (
            "I saw Daimyo Albert! Is it?\x01",
            "That jaw beard, is not it wonderful?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Prime Minister Osborne is also cool,\x01",
            "I guess it's hard to get close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But, both of them are bearded, do not they?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DCA")

    label("loc_4B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4BC7")

    ChrTalk(
        0xFE,
        (
            "Not to mention Arios, of course,\x01",
            "Mayor Dieter is also nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, rather than wanting to be a girlfriend\x01",
            "I feel like an ideal daddy.\x01",
            "I wonder if you will adopt me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DCA")

    label("loc_4BC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4BD5")
    Jump("loc_4DCA")

    label("loc_4BD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4DCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C2F")

    ChrTalk(
        0xFE,
        "……Yes? What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I am a little busy now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DCA")

    label("loc_4C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D02")

    ChrTalk(
        0xFE,
        (
            "A little stupid of redheads a while ago\x01",
            "I got stuck up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it was pretty cool\x01",
            "If you say ~ is not a type,\x01",
            "\"I am also, do not mind ☆\" … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Mu, Muukatsuku ~! It is!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4D65")

    label("loc_4D02")


    ChrTalk(
        0xFE,
        (
            "Fu-tsu, going out of yourself\x01",
            "\"I am not type too\" to say! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Mu, Muukatsuku ~! It is!\x02",
    )

    CloseMessageWindow()

    label("loc_4D65")

    Jump("loc_4DCA")

    label("loc_4D6A")


    ChrTalk(
        0xFE,
        (
            "home work~?\x01",
            "You can not do such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way,\x01",
            "Dear Arios, you seem to be on business again?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DCA")

    TalkEnd(0xFE)
    Return()

    # Function_7_4651 end

    def Function_8_4DCE(): pass

    label("Function_8_4DCE")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xC,
        (
            "By the way, linally\x01",
            "Do you keep jogging?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Huh, oh yeah ….\x01",
            "Well, as it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It is impossible to diet\x01",
            "Because I thought it was not good,\x01",
            "I'd like to take interest in recently ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Well, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "(… with this condition\x01",
            "I do not do it at all. )\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_8_4DCE end

    def Function_9_4EE8(): pass

    label("Function_9_4EE8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4F59")

    ChrTalk(
        0xFE,
        (
            "Yeah, pale light\x01",
            "I also feel beautiful … ….\x01",
            "It is super creepy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What will happen from now …?\x02",
    )

    CloseMessageWindow()
    Jump("loc_56AE")

    label("loc_4F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4F67")
    Jump("loc_56AE")

    label("loc_4F67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4FE9")

    ChrTalk(
        0xFE,
        (
            "Yeah yeah, that white military uniform also appears\x01",
            "It really suits you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If Arios is present,\x01",
            "I do not care what happens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56AE")

    label("loc_4FE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_505E")

    ChrTalk(
        0xFE,
        (
            "That's right.\x01",
            "It seems to be meaningful to participate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Anything else let's invite someone else.\x02",
    )

    CloseMessageWindow()
    Jump("loc_56AE")

    label("loc_505E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_50E5")

    ChrTalk(
        0xFE,
        "We are still 15 years old.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I do not really know about independence … …\x01",
            "To be honest, I may be relieved not to vote.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56AE")

    label("loc_50E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_50F3")
    Jump("loc_56AE")

    label("loc_50F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5140")

    ChrTalk(
        0xFE,
        (
            "I already have a Pruna\x01",
            "You should not say such noisy things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56AE")

    label("loc_5140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_51A5")

    ChrTalk(
        0xFE,
        "… I decided.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I gave up my diet and I\x01",
            "I will find a man who likes me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56AE")

    label("loc_51A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_521A")

    ChrTalk(
        0xFE,
        (
            "Haa, there is no exercise or dietary restrictions\x01",
            "I wonder if I do not have a diet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Someone tell me to do anything!\x02",
    )

    CloseMessageWindow()
    Jump("loc_56AE")

    label("loc_521A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_52BF")

    ChrTalk(
        0xFE,
        (
            "By the way, Arios\x01",
            "Medal from the Prime Minister of Remifferia\x01",
            "You have been awarded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The two people got along well,\x01",
            "I wonder if that was the chance?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56AE")

    label("loc_52BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_535C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52DF")
    Call(1, 8)
    ClearChrFlags(0xC, 0x10)
    Jump("loc_5357")

    label("loc_52DF")


    ChrTalk(
        0xFE,
        (
            "Even if you say that you feel like going away\x01",
            "Does it continue properly, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well then, then,\x01",
            "I wonder if I will run today and return.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5357")

    Jump("loc_56AE")

    label("loc_535C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_54D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_543D")

    ChrTalk(
        0xFE,
        (
            "Beard beard ……\x01",
            "I also like the real people too ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "More than that I\x01",
            "I was next to Prince Oliver\x01",
            "Is it a type of tall soldier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it is OK at once, for people of a physique\x01",
            "I would like you to hold a princess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_54D2")

    label("loc_543D")


    ChrTalk(
        0xFE,
        (
            "More than that I\x01",
            "I was next to Prince Oliver\x01",
            "Is it a type of tall soldier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it is OK at once, for people of a physique\x01",
            "I would like you to hold a princess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54D2")

    Jump("loc_56AE")

    label("loc_54D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5553")

    ChrTalk(
        0xFE,
        (
            "Certainly Mayor Dieter\x01",
            "It may be an ideal dad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tentatively, like my dad\x01",
            "I do not even smell a fudge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56AE")

    label("loc_5553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5561")
    Jump("loc_56AE")

    label("loc_5561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_56AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55CE")

    ChrTalk(
        0xFE,
        "Dangerous driving? Do not know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We are talkative\x01",
            "I was absorbed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56AE")

    label("loc_55CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_564D")

    ChrTalk(
        0xFE,
        (
            "…… That red-headed older brother,\x01",
            "It was a sort of hen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I went into a department store,\x01",
            "Who was it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56AE")

    label("loc_564D")


    ChrTalk(
        0xFE,
        (
            "Oh, by the way, I told you today.\x01",
            "It was a Sunday school from evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Have you done homework before for Pruna?\x02",
    )

    CloseMessageWindow()

    label("loc_56AE")

    TalkEnd(0xFE)
    Return()

    # Function_9_4EE8 end

    def Function_10_56B2(): pass

    label("Function_10_56B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5742")

    ChrTalk(
        0xFE,
        (
            "Why is that so\x01",
            "Is the huge tree floating in the air?\x01",
            "It is physically impossible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Or, here I am\x01",
            "Can I distribute balloons …?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6059")

    label("loc_5742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5750")
    Jump("loc_6059")

    label("loc_5750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5803")

    ChrTalk(
        0xFE,
        (
            "Crossbell independent country ……\x01",
            "I was supposed to be serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it is not a floating atmosphere,\x01",
            "For the time being that it is a founding memorial\x01",
            "Even making original balloons makes it a little.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6059")

    label("loc_5803")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5811")
    Jump("loc_6059")

    label("loc_5811")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_58A3")

    ChrTalk(
        0xFE,
        (
            "Although it is an armed group, I do not know what it is,\x01",
            "I will do something ridiculous at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll balloon and go somewhere right now\x01",
            "I feel like I want to say it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6059")

    label("loc_58A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_58B1")
    Jump("loc_6059")

    label("loc_58B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_592D")

    ChrTalk(
        0xFE,
        (
            "How about a balloon?\x01",
            "…… It's not like I'm saying anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, accident\x01",
            "I wonder what happened.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6059")

    label("loc_592D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5A25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59C8")

    ChrTalk(
        0xFE,
        "How about a balloon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Adults will not be shy\x01",
            "Please do come!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sometimes you forget the difficult things\x01",
            "Why do not you return to your childhood?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5A20")

    label("loc_59C8")


    ChrTalk(
        0xFE,
        (
            "Adults will not be shy\x01",
            "Please do come!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Once in a while\x01",
            "Why do not you return to your childhood?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A20")

    Jump("loc_6059")

    label("loc_5A25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5B79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B13")

    ChrTalk(
        0xFE,
        (
            "Before this, tourists' children\x01",
            "\"Why do balloons float? \"\x01",
            "I was asked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There I am soaked\x01",
            "\"Because my dreams are full\"\x01",
            "I replied ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Recently children are terrible.\x01",
            "I will laugh with my nose from my side.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5B74")

    label("loc_5B13")


    ChrTalk(
        0xFE,
        "Let 's have more dreams, children.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Gas lighter than air?\x01",
            "Yeah, the balloon is packed with dreams.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B74")

    Jump("loc_6059")

    label("loc_5B79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5BE0")

    ChrTalk(
        0xFE,
        "How about a balloon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now the emblem of the country participating in the trade meeting\x01",
            "I get a printed balloon ~.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6059")

    label("loc_5BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_5C59")

    ChrTalk(
        0xFE,
        "Well, I wonder if I will return today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks a lot for the crowd today as well.\x01",
            "I was able to give out balloons as much as I could.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6059")

    label("loc_5C59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5CE5")

    ChrTalk(
        0xFE,
        (
            "No, this is a limousine\x01",
            "I was really nervous when I passed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is it, the time of the founding memorial festival?\x01",
            "You also have a different enthusiasm.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6059")

    label("loc_5CE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5EE8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E29")
    TurnDirection(0xE, 0x1A2, 0)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "Oh my god there.\x01",
            "How about a balloon?\x01",
            "It will be fun floating and fun ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "- I do not need it.\x01",
            "It's just that kind of disturbing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "OK, then what color is it?\x01",
            "- Oh yeah?\x01",
            "Did you say you're in the way now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Haha, apparently Shin\x01",
            "Something childish\x01",
            "It looks like you're killing me. )\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x1DD, 1)
    Jump("loc_5E95")

    label("loc_5E29")


    ChrTalk(
        0xE,
        (
            "Surely there are children who are not interested in balloons\x01",
            "There are quite a lot though ….\x01",
            "I do not think there is denying so far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I'm going down a bit to drift.\x02",
    )

    CloseMessageWindow()

    label("loc_5E95")

    Jump("loc_5EE3")

    label("loc_5E9A")


    ChrTalk(
        0xFE,
        "How about a balloon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Red, blue, green to yellow.\x01",
            "I have various colors.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EE3")

    Jump("loc_6059")

    label("loc_5EE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5EF6")
    Jump("loc_6059")

    label("loc_5EF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6059")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F7C")

    ChrTalk(
        0xFE,
        (
            "Bibi on the earlier car,\x01",
            "I skipped some balloons!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, I want to have it …\x01",
            "Return home …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6059")

    label("loc_5F7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FF7")

    ChrTalk(
        0xFE,
        (
            "How about a balloon?\x01",
            "Cross Bell sightseeing\x01",
            "Please come along with us ~ ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be in a pleasant mood\x01",
            "It is a guarantee ~.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6059")

    label("loc_5FF7")


    ChrTalk(
        0xFE,
        (
            "Balloons are also available for tourists\x01",
            "We are distributing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyone who wants it\x01",
            "Please speak to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6059")

    TalkEnd(0xFE)
    Return()

    # Function_10_56B2 end

    def Function_11_605D(): pass

    label("Function_11_605D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_606E")
    Jump("loc_6300")

    label("loc_606E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6128")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6104")

    ChrTalk(
        0x11,
        "#01203FGurururu …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHello, if you are doing this here\x01",
            "It is exactly like a guard dog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#01200FGuru …… Won.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_6123")

    label("loc_6104")


    ChrTalk(
        0x11,
        "#01200FGuru …… Won.\x02",
    )

    CloseMessageWindow()

    label("loc_6123")

    Jump("loc_6300")

    label("loc_6128")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_6139")
    Jump("loc_6300")

    label("loc_6139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6147")
    Jump("loc_6300")

    label("loc_6147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6300")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6168")
    Call(1, 23)
    Return()

    label("loc_6168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62DE")

    ChrTalk(
        0x11,
        "#01203FGurururu …………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_627F")

    ChrTalk(
        0x101,
        "#00005FOh, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#01200F…………won.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A5,
        "#01100FIt's nothing special.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell, that's right.\x02\x03",
            "#00000FWell, do not ask for an answering machine today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A5,
        "#01109FZeit, I'm coming!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#01200Fwon.\x02",
    )

    CloseMessageWindow()
    Jump("loc_62D6")

    label("loc_627F")


    ChrTalk(
        0x101,
        (
            "#00003F(I still said something ……\x01",
            "If there is Tio or Kea\x01",
            "I understand. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62D6")

    SetScenarioFlags(0x1, 1)
    Jump("loc_62FB")

    label("loc_62DE")


    ChrTalk(
        0x11,
        "#01203FGurururu …………\x02",
    )

    CloseMessageWindow()

    label("loc_62FB")

    Jump("loc_6300")

    label("loc_6300")

    TalkEnd(0xFE)
    Return()

    # Function_11_605D end

    def Function_12_6304(): pass

    label("Function_12_6304")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6495")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_641A")

    ChrTalk(
        0xFE,
        (
            "Although it became a serious thing,\x01",
            "Do not be afraid, Mr. Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Up to now we've got a bunch of scrumples\x01",
            "If you guys are drowning,\x01",
            "I will definitely lead to a solution to this incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because I guarantee,\x01",
            "Go with confidence!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000Fmy mother……\x01",
            "Thank you, Kate-senpai.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_6490")

    label("loc_641A")


    ChrTalk(
        0xFE,
        (
            "If you are Lloyd,\x01",
            "I will definitely lead to a solution to this incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Go with confidence!\x01",
            "We will also work hard for the wide area crime prevention division!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6490")

    Jump("loc_6F1F")

    label("loc_6495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_64A3")
    Jump("loc_6F1F")

    label("loc_64A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_64B1")
    Jump("loc_6F1F")

    label("loc_64B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_64BF")
    Jump("loc_6F1F")

    label("loc_64BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_66B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6615")

    ChrTalk(
        0xFE,
        (
            "In occupation case of Mainz\x01",
            "The citizen who is shocked\x01",
            "Naturally it seems to be … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not care about somewhere\x01",
            "Many people think that they get a lot of impression.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then after receiving an incident\x01",
            "Voices affirming national independence\x01",
            "I also get the impression of rising at a stretch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, we\x01",
            "Everyone feels uneasy than necessary,\x01",
            "You have to be careful about making a noise.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_66B3")

    label("loc_6615")


    ChrTalk(
        0xFE,
        (
            "Apparently among the citizens,\x01",
            "Various thoughts are spreading\x01",
            "It looks like … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, we\x01",
            "Everyone feels uneasy than necessary,\x01",
            "You have to be careful about making a noise.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66B3")

    Jump("loc_6F1F")

    label("loc_66B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_675A")

    ChrTalk(
        0xFE,
        (
            "Transit railway managed somehow this morning\x01",
            "I heard that it was restored\x01",
            "I was relieved really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In addition to being unable to use railroads,\x01",
            "When thinking of this rain\x01",
            "I think that it was hard work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F1F")

    label("loc_675A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_67FD")

    ChrTalk(
        0xFE,
        (
            "It's a derailment accident … …\x01",
            "It was also a serious thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, for a while,\x01",
            "Traffic volume will increase as well.\x01",
            "I need to put in a spirit and organize the traffic.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F1F")

    label("loc_67FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6984")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_691B")
    OP_93(0xFE, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        "Pippy, Pippy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please steer the guided car.\x01",
            "Please cooperate with city safety!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)
    Sleep(300)

    ChrTalk(
        0xFE,
        (
            "I wonder if this is an independent advocate ….\x01",
            "Recently the driving force from foreign countries\x01",
            "I feel that it is decreasing slightly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, that's why\x01",
            "I will not mind alerting you of an accident, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_697F")

    label("loc_691B")

    OP_93(0xFE, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        "Pippy, Pippy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please steer the guided car.\x01",
            "Please cooperate with city safety!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_697F")

    Jump("loc_6F1F")

    label("loc_6984")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6C06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B43")

    ChrTalk(
        0xFE,
        (
            "Recently also,\x01",
            "People who can not keep traffic rules\x01",
            "It seems to be increasing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Traffic rules and bitefully say,\x01",
            "Before that, it is important for the driver\x01",
            "It is a morale and a good man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone should have taught at Sunday school\x01",
            "Morality becomes an adult and can not protect … …\x01",
            "This is a really sad thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You also have a handle\x01",
            "When you grasp always to the surrounding people\x01",
            "Do not forget your attention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYes, of course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F…… But I knew it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_6C01")

    label("loc_6B43")


    ChrTalk(
        0xFE,
        (
            "Traffic rules and bitefully say,\x01",
            "Before that, it is important for the driver\x01",
            "It is a morale and a good man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone should have taught at Sunday school\x01",
            "Morality becomes an adult and can not protect … …\x01",
            "This is a really sad thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C01")

    Jump("loc_6F1F")

    label("loc_6C06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6C91")

    ChrTalk(
        0xFE,
        (
            "Terrorist appears\x01",
            "I have a high possibility … ….\x01",
            "It really does not matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For suspicious people and things,\x01",
            "I have to pay full attention.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F1F")

    label("loc_6C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6D30")

    ChrTalk(
        0xFE,
        (
            "Let's have a limo on board with the leaders\x01",
            "I was guided, but ….\x01",
            "I was pretty nervous about running water.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What do you mean, aura?\x01",
            "It is also transmitted through a car.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F1F")

    label("loc_6D30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6DE6")

    ChrTalk(
        0xFE,
        (
            "Travel from place to place from today\x01",
            "With the relationship I started, the number of illegal parking\x01",
            "It seems that it is drastically decreasing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope it will be like this from now on ….\x01",
            "Well, for the time being, it's a good thing\x01",
            "I wonder if I can complain.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F1F")

    label("loc_6DE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6F16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EAD")
    OP_93(0xFE, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        (
            "Pippy, Pippy!\x01",
            "Please slow down the power train.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)
    Sleep(300)

    ChrTalk(
        0xFE,
        (
            "From the usual day on rainy days\x01",
            "The traffic volume will increase slightly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The road surface is also slippery,\x01",
            "You need more attention than usual.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_6F11")

    label("loc_6EAD")


    ChrTalk(
        0xFE,
        (
            "From the usual day on rainy days\x01",
            "Slightly, traffic volume increases.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The road surface is also slippery,\x01",
            "You need more attention than usual.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F11")

    Jump("loc_6F1F")

    label("loc_6F16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6F1F")

    label("loc_6F1F")

    TalkEnd(0xFE)
    Return()

    # Function_12_6304 end

    def Function_13_6F23(): pass

    label("Function_13_6F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7076")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6FEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F5F")
    Call(0, 104)
    Jump("loc_6FEE")

    label("loc_6F5F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "If it is a black truck, a while ago\x01",
            "I went out to the east side of the street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you follow, you also\x01",
            "The one who got on the driving force car\x01",
            "Is not it okay?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_6FEE")

    Return()

    label("loc_6FEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FFD")
    Call(1, 26)
    Return()

    label("loc_6FFD")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hunting guys …\x01",
            "Why \"Cross Bell's Bell\"\x01",
            "I guess they stole it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… Well, even though I thought\x01",
            "There is no choice but.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_7076")

    Return()

    # Function_13_6F23 end

    def Function_14_7077(): pass

    label("Function_14_7077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71D1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7119")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70B3")
    Call(0, 104)
    Jump("loc_7118")

    label("loc_70B3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "As soon as the truck,\x01",
            "I was about to arrive at the Tangram main gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I pray for your good luck!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_7118")

    Return()

    label("loc_7119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7127")
    Call(1, 26)
    Return()

    label("loc_7127")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "For the current guard,\x01",
            "Tension condition with two major powers\x01",
            "It is a matter of concern.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will search for the place of \"bell\"\x01",
            "After patrol, a degree of\x01",
            "It will be priority.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_71D1")

    Return()

    # Function_14_7077 end

    def Function_15_71D2(): pass

    label("Function_15_71D2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7224")

    ChrTalk(
        0xFE,
        (
            "The trade conference is finally coming to the mountain …\x01",
            "I have to improve my concentration more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72F8")

    label("loc_7224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7298")

    ChrTalk(
        0xFE,
        (
            "Finally the leaders\x01",
            "I came to the crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tentatively the unveiling ceremony\x01",
            "I was relieved not to have anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72F8")

    label("loc_7298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_72F8")

    ChrTalk(
        0xFE,
        (
            "Tour of the city is a trade meeting\x01",
            "It is scheduled to continue until the final day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm feeling enthusiastic.\x02",
    )

    CloseMessageWindow()

    label("loc_72F8")

    TalkEnd(0xFE)
    Return()

    # Function_15_71D2 end

    def Function_16_72FC(): pass

    label("Function_16_72FC")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "\"Defense Army\" for \"fighting\"\x01",
            "It is power to \"defend\" not by force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We are savage\x01",
            "It is different from the Empire and the Republican Army.\x01",
            "So, please be relieved.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_72FC end

    def Function_17_7392(): pass

    label("Function_17_7392")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I take away the symbol of the city …\x01",
            "What on earth are you being harassed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I messed up my favorite spot.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_7392 end

    def Function_18_73F8(): pass

    label("Function_18_73F8")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Tell me that the bell is gone,\x01",
            "It was true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is it an armed group …?\x01",
            "The purpose is really a mystery.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_73F8 end

    def Function_19_745B(): pass

    label("Function_19_745B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7561")

    ChrTalk(
        0x12,
        "#01111F……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F… … Kea?\x01",
            "What's wrong with me.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x12, 0x0, 500)
    Sleep(300)

    ChrTalk(
        0x12,
        (
            "#01105FAh … no, it's nothing.\x02\x03",
            "#01109FEveryone, do your best at work today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F…………?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x159, 1)
    SetScenarioFlags(0x151, 6)
    Jump("loc_7590")

    label("loc_7561")


    ChrTalk(
        0x12,
        "#01109FEveryone, do your best at work today.\x02",
    )

    CloseMessageWindow()

    label("loc_7590")

    TalkEnd(0xFE)
    Return()

    # Function_19_745B end

    def Function_20_7594(): pass

    label("Function_20_7594")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75AE")
    Call(1, 23)
    Return()

    label("loc_75AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7712")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7712")

    ChrTalk(
        0x104,
        "#00302FLike Koppe, how are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Anyway ~ ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FSomehow I am hungry\x01",
            "Looks like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FWow, I\x01",
            "I want to give food!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIs Koppe a fish caught?\x01",
            "If it is \"Nekomanma\"\x01",
            "You are willing to eat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh, I wonder if I had it now … ….?\x02\x03",
            "#00000FAnyway, do not forget\x01",
            "I have to give food every morning.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x159, 3)
    TalkEnd(0xFE)
    Return()

    label("loc_7712")

    ClearScenarioFlags(0x1, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7721")
    Call(1, 22)

    label("loc_7721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_779E")

    ChrTalk(
        0x101,
        (
            "#00005F(by the way……\x01",
            "There was a caught fish. )\x02\x03",
            "#00004F(Even if you give it to Coppe\x01",
            "It might be nice. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13A, 0)

    label("loc_779E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_77C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 1)), scpexpr(EXPR_END)), "loc_77C4")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_77C4")

    Jump("loc_78CC")

    label("loc_77C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_77EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 0)), scpexpr(EXPR_END)), "loc_77E5")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_77E5")

    Jump("loc_78CC")

    label("loc_77EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_780B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 7)), scpexpr(EXPR_END)), "loc_7806")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7806")

    Jump("loc_78CC")

    label("loc_780B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_782C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 6)), scpexpr(EXPR_END)), "loc_7827")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7827")

    Jump("loc_78CC")

    label("loc_782C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_784D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 5)), scpexpr(EXPR_END)), "loc_7848")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7848")

    Jump("loc_78CC")

    label("loc_784D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_786E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 4)), scpexpr(EXPR_END)), "loc_7869")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7869")

    Jump("loc_78CC")

    label("loc_786E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_788F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 3)), scpexpr(EXPR_END)), "loc_788A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_788A")

    Jump("loc_78CC")

    label("loc_788F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_78B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 2)), scpexpr(EXPR_END)), "loc_78AB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_78AB")

    Jump("loc_78CC")

    label("loc_78B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_78CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 1)), scpexpr(EXPR_END)), "loc_78CC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_78CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8EDC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_78E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8ED7")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 1)
    MenuCmd(1, 1, "talk")
    MenuCmd(1, 1, "To feed")
    MenuCmd(1, 1, "quit")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_795B")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_795B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EA2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7998")
    MenuCmd(1, 1, "Fighter")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7998")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_END)), "loc_79BF")
    MenuCmd(1, 1, "Snow shave")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_79BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_79E0")
    MenuCmd(1, 1, "Ezel")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_79E0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7A01")
    MenuCmd(1, 1, "Kasagin")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7A01")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7A28")
    MenuCmd(1, 1, "Almorican beech")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7A28")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_END)), "loc_7A47")
    MenuCmd(1, 1, "Tutas")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7A47")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7A68")
    MenuCmd(1, 1, "Orocho")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7A68")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7A87")
    MenuCmd(1, 1, "Lock")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7A87")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7AAA")
    MenuCmd(1, 1, "Rainbow")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7AAA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7ACD")
    MenuCmd(1, 1, "Piragna")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7ACD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7AEC")
    MenuCmd(1, 1, "Calf")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7AEC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7B11")
    MenuCmd(1, 1, "Grant Bus")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7B11")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_END)), "loc_7B32")
    MenuCmd(1, 1, "Trad")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7B32")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7B57")
    MenuCmd(1, 1, "Gladieta")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7B57")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7B78")
    MenuCmd(1, 1, "Rainy")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7B78")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_END)), "loc_7B99")
    MenuCmd(1, 1, "Sansho")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7B99")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7BBA")
    MenuCmd(1, 1, "Samona")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7BBA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7BDB")
    MenuCmd(1, 1, "Arona")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7BDB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_END)), "loc_7BFA")
    MenuCmd(1, 1, "Eel")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7BFA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_END)), "loc_7C1F")
    MenuCmd(1, 1, "Adamantas")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7C1F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_END)), "loc_7C44")
    MenuCmd(1, 1, "Quinciser")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7C44")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7C65")
    MenuCmd(1, 1, "Parc")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7C65")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_END)), "loc_7C86")
    MenuCmd(1, 1, "Titan")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7C86")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_END)), "loc_7CAD")
    MenuCmd(1, 1, "Gordosamna")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7CAD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大鲵', 0x0)"), scpexpr(EXPR_END)), "loc_7CD2")
    MenuCmd(1, 1, "Freshwater")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7CD2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('锦鲤', 0x0)"), scpexpr(EXPR_END)), "loc_7CF9")
    MenuCmd(1, 1, "Noble Carb")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7CF9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠耀神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7D1A")
    MenuCmd(1, 1, "Emerald")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7D1A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('琥耀岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7D3F")
    MenuCmd(1, 1, "Tiga rock")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7D3F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('红耀食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7D68")
    MenuCmd(1, 1, "Crimson Eta")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7D68")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('苍耀巨龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7D8D")
    MenuCmd(1, 1, "Bull Dragon")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7D8D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨骨龙皇鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7DB0")
    MenuCmd(1, 1, "Giga Look")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7DB0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('猫食', 0x0)"), scpexpr(EXPR_END)), "loc_7DD3")
    MenuCmd(1, 1, "Nekomanma")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7DD3")

    MenuCmd(1, 1, "quit")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7E1D")
    Jump("loc_8E93")

    label("loc_7E1D")

    TalkEnd(0xFE)
    EventBegin(0x1)
    OP_4B(0x10, 0xFF)
    Fade(500)
    SetChrPos(0x10, -21980, 1300, -19300, 270)
    SetChrPos(0x0, -23900, 1300, -19070, 89)
    SetChrPos(0x1, -23540, 1300, -20210, 89)
    SetChrPos(0x2, -25020, 1300, -19860, 89)
    SetChrPos(0x3, -25130, 1300, -18930, 89)
    SetChrPos(0x4, -26200, 1300, -19870, 89)
    SetChrPos(0x5, -26790, 1300, -19180, 89)
    OP_68(-23130, 3900, -19610, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    ChrTalk(
        0xFE,
        "Nyanny … … spray\x02",
    )

    CloseMessageWindow()

    def lambda_7EEE():

        label("loc_7EEE")

        TurnDirection(0x0, 0x10, 0)
        Yield()
        Jump("loc_7EEE")

    QueueWorkItem2(0x0, 1, lambda_7EEE)

    def lambda_7F00():

        label("loc_7F00")

        TurnDirection(0x1, 0x10, 0)
        Yield()
        Jump("loc_7F00")

    QueueWorkItem2(0x1, 1, lambda_7F00)

    def lambda_7F12():

        label("loc_7F12")

        TurnDirection(0x2, 0x10, 0)
        Yield()
        Jump("loc_7F12")

    QueueWorkItem2(0x2, 1, lambda_7F12)

    def lambda_7F24():

        label("loc_7F24")

        TurnDirection(0x3, 0x10, 0)
        Yield()
        Jump("loc_7F24")

    QueueWorkItem2(0x3, 1, lambda_7F24)

    def lambda_7F36():

        label("loc_7F36")

        TurnDirection(0x4, 0x10, 0)
        Yield()
        Jump("loc_7F36")

    QueueWorkItem2(0x4, 1, lambda_7F36)

    def lambda_7F48():

        label("loc_7F48")

        TurnDirection(0x5, 0x10, 0)
        Yield()
        Jump("loc_7F48")

    QueueWorkItem2(0x5, 1, lambda_7F48)
    SetChrFlags(0x10, 0x8000)
    OP_93(0x10, 0x0, 0x1F4)
    Sleep(50)
    ClearChrFlags(0x10, 0x1)
    Sound(809, 0, 80, 0)

    def lambda_7F74():
        OP_9D(0xFE, 0xFFFFA92A, 0x5DC, 0xFFFFC324, 0x708, 0x1F40)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7F74)
    WaitChrThread(0x10, 1)
    Sound(809, 0, 80, 0)

    def lambda_7F9B():
        OP_9D(0xFE, 0xFFFFA7CC, 0x10CC, 0xFFFFC69E, 0x1130, 0x1388)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7F9B)
    WaitChrThread(0x10, 1)
    Sound(844, 0, 80, 0)

    def lambda_7FC2():
        OP_9D(0xFE, 0xFFFFA75E, 0x514, 0xFFFFDFBC, 0x708, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7FC2)
    WaitChrThread(0x10, 1)
    Sleep(2000)
    OP_93(0x10, 0xB4, 0x1F4)
    Sound(809, 0, 80, 0)

    def lambda_7FF3():
        OP_9D(0xFE, 0xFFFFA7CC, 0x10CC, 0xFFFFC69E, 0x1194, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7FF3)
    WaitChrThread(0x10, 1)
    Sound(809, 0, 80, 0)

    def lambda_801A():
        OP_9D(0xFE, 0xFFFFA92A, 0x5DC, 0xFFFFC324, 0x640, 0x1388)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_801A)
    WaitChrThread(0x10, 1)
    Sound(844, 0, 80, 0)

    def lambda_8041():
        OP_9D(0xFE, 0xFFFFAA24, 0x514, 0xFFFFB49C, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_8041)
    WaitChrThread(0x10, 1)
    SetChrFlags(0x10, 0x1)
    OP_93(0x10, 0x10E, 0x1F4)
    ClearChrFlags(0x10, 0x8000)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    EndChrThread(0x4, 0x1)
    EndChrThread(0x5, 0x1)

    ChrTalk(
        0xFE,
        "Futako … ….\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_8115")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_810B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('斗鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('ＥＰ１', 1)

    label("loc_810B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8115")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_END)), "loc_8163")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8159")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('雪花蟹', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '精神１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('精神１', 1)

    label("loc_8159")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8163")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_81B1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81A7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('蓝带神仙鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔防２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('魔防２', 1)

    label("loc_81A7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_81B1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_END)), "loc_81FF")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81F5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('银伞鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '省ＥＰ１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('省ＥＰ１', 1)

    label("loc_81F5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_81FF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_END)), "loc_824D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8243")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('阿尔摩利卡鲫鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '移动１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('移动１', 1)

    label("loc_8243")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_824D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_END)), "loc_829B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8291")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('乌龟', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '命中１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('命中１', 1)

    label("loc_8291")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_829B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_END)), "loc_82E9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82DF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('橙河鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '恶戏'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('恶戏', 1)

    label("loc_82DF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_82E9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_8337")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_832D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('岩穴鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '防御２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('防御２', 1)

    label("loc_832D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8337")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_END)), "loc_8385")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_837B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('虹鳟鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '情报'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('情报', 1)

    label("loc_837B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8385")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_83D3")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83C9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('食人鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '暗之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('暗之刃', 1)

    label("loc_83C9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_83D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_END)), "loc_8421")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8417")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('鲤鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＨＰ１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('ＨＰ１', 1)

    label("loc_8417")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8421")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_END)), "loc_846F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8465")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('大口鲈鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '攻击１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('攻击１', 1)

    label("loc_8465")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_846F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_END)), "loc_84BD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84B3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('黑鲑', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '混乱之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('混乱之刃', 1)

    label("loc_84B3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84BD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_850B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8501")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('角斗鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '妨害１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('妨害１', 1)

    label("loc_8501")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_850B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_END)), "loc_8559")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_854F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('冷水鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '丹精'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('丹精', 1)

    label("loc_854F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8559")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_END)), "loc_85A7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_859D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('小鲵', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '回避１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('回避１', 1)

    label("loc_859D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_85A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_END)), "loc_85F5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85EB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('鲑鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '驱动１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('驱动１', 1)

    label("loc_85EB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_85F5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_8643")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8639")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('金龙鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '炎伤之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('炎伤之刃', 1)

    label("loc_8639")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8643")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_END)), "loc_8691")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8687")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('鳗鲡', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '行动力１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('行动力１', 1)

    label("loc_8687")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8691")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_END)), "loc_86DF")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86D5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('钢壳龟', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '石化之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('石化之刃', 1)

    label("loc_86D5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_86DF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_END)), "loc_872D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8723")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('巨血蟹', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '攻击３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('攻击３', 1)

    label("loc_8723")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_872D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_877B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8771")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('珍珠龙鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '命中３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('命中３', 1)

    label("loc_8771")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_877B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_END)), "loc_87C9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87BF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('巨鲶', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '防御３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('防御３', 1)

    label("loc_87BF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_87C9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_END)), "loc_8817")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_880D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('金鲑', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '天眼'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('天眼', 1)

    label("loc_880D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8817")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大鲵', 0x0)"), scpexpr(EXPR_END)), "loc_8865")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_885B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('大鲵', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＨＰ３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('ＨＰ３', 1)

    label("loc_885B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8865")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('锦鲤', 0x0)"), scpexpr(EXPR_END)), "loc_88B3")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88A9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('锦鲤', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '幸运'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('幸运', 1)

    label("loc_88A9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_88B3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠耀神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_8901")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88F7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('翠耀神仙鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '美臭'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('美臭', 1)

    label("loc_88F7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8901")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('琥耀岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_894F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8945")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('琥耀岩穴鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '虎威'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('虎威', 1)

    label("loc_8945")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_894F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('红耀食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_899D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8993")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('红耀食人鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '龙眼'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('龙眼', 1)

    label("loc_8993")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_899D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('苍耀巨龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_89EB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89E1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('苍耀巨龙鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '治愈'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('治愈', 1)

    label("loc_89E1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_89EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨骨龙皇鱼', 0x0)"), scpexpr(EXPR_END)), "loc_8A39")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A2F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('巨骨龙皇鱼', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '混乱之刃２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('混乱之刃２', 1)

    label("loc_8A2F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A39")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('猫食', 0x0)"), scpexpr(EXPR_END)), "loc_8A8B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A81")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('猫食', 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽鱼肉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "× 3 was received.\x02",
        )
    )

    AddItemNumber('魔兽鱼肉', 3)

    label("loc_8A81")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A8B")

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8AB2")
    SetScenarioFlags(0x13B, 1)
    Jump("loc_8B35")

    label("loc_8AB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8AC3")
    SetScenarioFlags(0x13B, 0)
    Jump("loc_8B35")

    label("loc_8AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8AD4")
    SetScenarioFlags(0x13A, 7)
    Jump("loc_8B35")

    label("loc_8AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8AE5")
    SetScenarioFlags(0x13A, 6)
    Jump("loc_8B35")

    label("loc_8AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8AF6")
    SetScenarioFlags(0x13A, 5)
    Jump("loc_8B35")

    label("loc_8AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8B07")
    SetScenarioFlags(0x13A, 4)
    Jump("loc_8B35")

    label("loc_8B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8B18")
    SetScenarioFlags(0x13A, 3)
    Jump("loc_8B35")

    label("loc_8B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8B29")
    SetScenarioFlags(0x13A, 2)
    Jump("loc_8B35")

    label("loc_8B29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8B35")
    SetScenarioFlags(0x13A, 1)

    label("loc_8B35")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 1)), scpexpr(EXPR_END)), "loc_8B52")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 2)), scpexpr(EXPR_END)), "loc_8B65")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 3)), scpexpr(EXPR_END)), "loc_8B78")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 4)), scpexpr(EXPR_END)), "loc_8B8B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 5)), scpexpr(EXPR_END)), "loc_8B9E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 6)), scpexpr(EXPR_END)), "loc_8BB1")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 7)), scpexpr(EXPR_END)), "loc_8BC4")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 0)), scpexpr(EXPR_END)), "loc_8BD7")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 1)), scpexpr(EXPR_END)), "loc_8BEA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CC4")

    ChrTalk(
        0xFE,
        "Nyanny … ♪ ♪\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('灵猫', 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C77")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '灵猫'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('灵猫', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_8CC4")

    label("loc_8C77")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '银耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('银耀珠', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_8CC4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D05")

    ChrTalk(
        0x102,
        "#00105FOh … … will you give me this?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E51")

    label("loc_8D05")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D3B")

    ChrTalk(
        0x103,
        "#00205FAre you giving me this?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E51")

    label("loc_8D3B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D71")

    ChrTalk(
        0x104,
        "#00305FDoes he give me this?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E51")

    label("loc_8D71")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DA7")

    ChrTalk(
        0x109,
        "#10105FWell, will you give me this?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E51")

    label("loc_8DA7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DE1")

    ChrTalk(
        0x105,
        "#10305FOh, will you give me this?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E51")

    label("loc_8DE1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E24")

    ChrTalk(
        0x106,
        (
            "#10705FEr …\x01",
            "Can I get it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E51")

    label("loc_8E24")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E51")

    ChrTalk(
        0x10A,
        "#00605FDo you give me this?\x02",
    )

    CloseMessageWindow()

    label("loc_8E51")


    ChrTalk(
        0x101,
        (
            "#0000FHello, Thank you.\x01",
            "I will thank you for using it.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    EventEnd(0x4)
    Return()

    label("loc_8E93")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8ED2")

    label("loc_8EA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8EB6")
    Jump("loc_8ED2")

    label("loc_8EB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8ED2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 21)

    label("loc_8ED2")

    Jump("loc_78E9")

    label("loc_8ED7")

    Jump("loc_8EDF")

    label("loc_8EDC")

    Call(1, 21)

    label("loc_8EDF")

    TalkEnd(0xFE)
    Return()

    # Function_20_7594 end

    def Function_21_8EE3(): pass

    label("Function_21_8EE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8FB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F98")

    ChrTalk(
        0x10,
        "Damn it …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FKoppe, for a while\x01",
            "I'd like an answering machine.\x02\x03",
            "#00200FI'm sure Keea is here\x01",
            "I will bring you back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "…… Hey hey.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8FB2")

    label("loc_8F98")


    ChrTalk(
        0x10,
        "…… Hey hey.\x02",
    )

    CloseMessageWindow()

    label("loc_8FB2")

    Jump("loc_9452")

    label("loc_8FB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_8FC5")
    Jump("loc_9452")

    label("loc_8FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8FEB")

    ChrTalk(
        0x10,
        "Fukuya ~~ … …\x02",
    )

    CloseMessageWindow()
    Jump("loc_9452")

    label("loc_8FEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_900D")

    ChrTalk(
        0x10,
        "Fumi ah ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9452")

    label("loc_900D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_902F")

    ChrTalk(
        0x10,
        "Nyao …?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9452")

    label("loc_902F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_903D")
    Jump("loc_9452")

    label("loc_903D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9061")

    ChrTalk(
        0x10,
        "Nice ~ ~ …\x02",
    )

    CloseMessageWindow()
    Jump("loc_9452")

    label("loc_9061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9083")

    ChrTalk(
        0x10,
        "Fumi ah ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9452")

    label("loc_9083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_90A7")

    ChrTalk(
        0x10,
        "Fukaya ~~.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9452")

    label("loc_90A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9158")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_913F")

    ChrTalk(
        0x10,
        "Nyao.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FWhatching\x01",
            "Long time no see, Koppe.\x02\x03",
            "I am from today too\x01",
            "I will restart food production.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Say hello to me\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9153")

    label("loc_913F")


    ChrTalk(
        0x10,
        "Say hello to me\x02",
    )

    CloseMessageWindow()

    label("loc_9153")

    Jump("loc_9452")

    label("loc_9158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_9258")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9241")

    ChrTalk(
        0x10,
        "Nice to meet you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00600FIs it a cat kept at the support department?\x02\x03",
            "#00603F(Hold on … …)\x01",
            "… …. You too are in a difficult place\x01",
            "It is strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Hey ~~ O … … spray\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(Mr. Dudley,\x01",
            "Surprisingly cat treatment is good … …)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9253")

    label("loc_9241")


    ChrTalk(
        0x10,
        "Nyao\x02",
    )

    CloseMessageWindow()

    label("loc_9253")

    Jump("loc_9452")

    label("loc_9258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_9274")

    ChrTalk(
        0x10,
        "Nya\x02",
    )

    CloseMessageWindow()
    Jump("loc_9452")

    label("loc_9274")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9296")

    ChrTalk(
        0x10,
        "Fumi ah ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9452")

    label("loc_9296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_92B6")

    ChrTalk(
        0x10,
        "Anyway ~ ~.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9452")

    label("loc_92B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_92C4")
    Jump("loc_9452")

    label("loc_92C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_9452")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_943A")

    ChrTalk(
        0x101,
        (
            "#00005FYes, to Coppe\x01",
            "I have to do feeds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Nya\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9357")

    ChrTalk(
        0x1A5,
        "#01100FI've got hungry now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_938F")

    label("loc_9357")


    ChrTalk(
        0x105,
        (
            "#10300FBut, well now.\x01",
            "It seems to be full of stomach.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_938F")


    ChrTalk(
        0x102,
        (
            "#00100FBefore the section chief leaves\x01",
            "She seems to have raised food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FIt is a little disappointing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell, if I get fish next time\x01",
            "Shall I bring it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13B, 2)
    Jump("loc_9452")

    label("loc_943A")


    ChrTalk(
        0x10,
        "Nyanaya ~ spray\x02",
    )

    CloseMessageWindow()

    label("loc_9452")

    Return()

    # Function_21_8EE3 end

    def Function_22_9453(): pass

    label("Function_22_9453")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_9461")
    SetScenarioFlags(0x1, 3)

    label("loc_9461")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_END)), "loc_946F")
    SetScenarioFlags(0x1, 3)

    label("loc_946F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_947D")
    SetScenarioFlags(0x1, 3)

    label("loc_947D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_END)), "loc_948B")
    SetScenarioFlags(0x1, 3)

    label("loc_948B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_END)), "loc_9499")
    SetScenarioFlags(0x1, 3)

    label("loc_9499")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_END)), "loc_94A7")
    SetScenarioFlags(0x1, 3)

    label("loc_94A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_END)), "loc_94B5")
    SetScenarioFlags(0x1, 3)

    label("loc_94B5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_94C3")
    SetScenarioFlags(0x1, 3)

    label("loc_94C3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_END)), "loc_94D1")
    SetScenarioFlags(0x1, 3)

    label("loc_94D1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_94DF")
    SetScenarioFlags(0x1, 3)

    label("loc_94DF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_END)), "loc_94ED")
    SetScenarioFlags(0x1, 3)

    label("loc_94ED")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_END)), "loc_94FB")
    SetScenarioFlags(0x1, 3)

    label("loc_94FB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_END)), "loc_9509")
    SetScenarioFlags(0x1, 3)

    label("loc_9509")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_9517")
    SetScenarioFlags(0x1, 3)

    label("loc_9517")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_END)), "loc_9525")
    SetScenarioFlags(0x1, 3)

    label("loc_9525")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_END)), "loc_9533")
    SetScenarioFlags(0x1, 3)

    label("loc_9533")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_END)), "loc_9541")
    SetScenarioFlags(0x1, 3)

    label("loc_9541")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_954F")
    SetScenarioFlags(0x1, 3)

    label("loc_954F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_END)), "loc_955D")
    SetScenarioFlags(0x1, 3)

    label("loc_955D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_END)), "loc_956B")
    SetScenarioFlags(0x1, 3)

    label("loc_956B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_END)), "loc_9579")
    SetScenarioFlags(0x1, 3)

    label("loc_9579")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_9587")
    SetScenarioFlags(0x1, 3)

    label("loc_9587")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_END)), "loc_9595")
    SetScenarioFlags(0x1, 3)

    label("loc_9595")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_END)), "loc_95A3")
    SetScenarioFlags(0x1, 3)

    label("loc_95A3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大鲵', 0x0)"), scpexpr(EXPR_END)), "loc_95B1")
    SetScenarioFlags(0x1, 3)

    label("loc_95B1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('锦鲤', 0x0)"), scpexpr(EXPR_END)), "loc_95BF")
    SetScenarioFlags(0x1, 3)

    label("loc_95BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠耀神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_95CD")
    SetScenarioFlags(0x1, 3)

    label("loc_95CD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('琥耀岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_95DB")
    SetScenarioFlags(0x1, 3)

    label("loc_95DB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('红耀食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_95E9")
    SetScenarioFlags(0x1, 3)

    label("loc_95E9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('苍耀巨龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_95F7")
    SetScenarioFlags(0x1, 3)

    label("loc_95F7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨骨龙皇鱼', 0x0)"), scpexpr(EXPR_END)), "loc_9605")
    SetScenarioFlags(0x1, 3)

    label("loc_9605")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('猫食', 0x0)"), scpexpr(EXPR_END)), "loc_9613")
    SetScenarioFlags(0x1, 3)

    label("loc_9613")

    Return()

    # Function_22_9453 end

    def Function_23_9614(): pass

    label("Function_23_9614")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_93(0x10, 0x10E, 0x0)
    SetChrPos(0x101, -25020, 1300, -19860, 90)
    SetChrPos(0x102, -25130, 1300, -18930, 90)
    SetChrPos(0x109, -26200, 1300, -19870, 90)
    SetChrPos(0x105, -26790, 1300, -19180, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_968F")
    SetChrPos(0x1A5, -24820, 1300, -16830, 133)

    label("loc_968F")

    OP_68(-24880, 3000, -20830, 0)
    MoveCamera(43, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(10510, 0)
    OP_0D()

    ChrTalk(
        0x11,
        "#01200FGururururu …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FZeit, Koppe.\x01",
            "Did you stay with him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FHehe, you are on good terms as usual.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHe keeps him at the mission support section\x01",
            "It is a police dog.\x02\x03",
            "#10300FRegards, again, Zeit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#01203FGuru …… Won.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_98F7")

    ChrTalk(
        0x1A5,
        (
            "#01104F\"The\" keeping \"is incorrect,\x01",
            "It is here that I look after my troubles. \"\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x105,
        "#6P#10309FAhaha, this was a stupid thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell, well ….\x01",
            "I always get helped.\x01",
            "It is high as pride as usual …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9967")

    label("loc_98F7")


    ChrTalk(
        0x101,
        (
            "#00005FWhat I want to say somewhat\x01",
            "It seems likely, but …\x02\x03",
            "#00003FWell, if there is Tio or Kea\x01",
            "I do understand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9967")

    TurnDirection(0x109, 0x10, 500)

    ChrTalk(
        0x109,
        (
            "#6P#10102FHuhu, I was not good at dogs though\x01",
            "I got used to Zeit.\x02\x03",
            "#10105FSo, what's this black cat?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x10, 500)

    ChrTalk(
        0x101,
        (
            "#6P#00000FOh, I mean Koppe.\x02\x03",
            "Cross Bell Communication Company in this building\x01",
            "Since I moved in\x01",
            "It seems they are living.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#11PNice to meet you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FHehe, it is cute.\x02\x03",
            "#10109FHaha, in the future from the support department\x01",
            "You can touch with a cat … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FMr. Noel was a cat lover.\x01",
            "Hehe, I look forward to the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#11PFumi ah ……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -24690, 1300, -19050, 90)
    SetScenarioFlags(0x139, 7)
    OP_4C(0x10, 0xFF)
    OP_93(0x10, 0xB4, 0x0)
    OP_4C(0x11, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_23_9614 end

    def Function_24_9B5A(): pass

    label("Function_24_9B5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9B91")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B91")
    Call(1, 26)
    Return()

    label("loc_9B91")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "\"Cross Bell's Bell\"\x01",
            "S 1185, in Crossbell Autonomous province\x01",
            "A huge bell excavated.\x01",
            "From the situation of the excavated site\x01",
            "It is considered to be a thing of the Middle Ages.\x01",
            "It consists of multiple metals,\x01",
            "Hitting a comfortable low tone when striking.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Depending on influential people at the time\x01",
            "Although it is presumed that it was made,\x01",
            "There are still many theories in its use.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_24_9B5A end

    def Function_25_9CD7(): pass

    label("Function_25_9CD7")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A1CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A184")

    ChrTalk(
        0x1A2,
        (
            "Gironde Weapons Association ……\x01",
            "Well, is this legal weapons store?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Alright, I'll drop in a bit.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_9DA1")

    def lambda_9D71():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9D71)
    Sleep(50)

    def lambda_9D81():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9D81)
    Sleep(50)

    def lambda_9D91():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9D91)
    Sleep(300)
    Jump("loc_9E18")

    label("loc_9DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_9DDF")

    def lambda_9DAF():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9DAF)
    Sleep(50)

    def lambda_9DBF():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9DBF)
    Sleep(50)

    def lambda_9DCF():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9DCF)
    Sleep(300)
    Jump("loc_9E18")

    label("loc_9DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_9E18")

    def lambda_9DED():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9DED)
    Sleep(50)

    def lambda_9DFD():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9DFD)
    Sleep(50)

    def lambda_9E0D():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9E0D)
    Sleep(300)

    label("loc_9E18")


    ChrTalk(
        0x101,
        (
            "#00003FSorry, Shin.\x01",
            "As you are told, this is a weapon shop.\x02\x03",
            "#00001FBecause there are dangerous goods inside,\x01",
            "To guide you as expected … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Funk, to the bed\x01",
            "You do not have to touch the goods, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "I am interested here.\x01",
            "I will come and get away if you come.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F(Fuu … ….\x01",
            "Ellie, please do it. )\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00100F(Hehe, okay.)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00103FHey Shin, you are\x01",
            "Important important keeping things.\x02\x03",
            "So,\x01",
            "Even if the possibility of emergency\x01",
            "I have to eliminate the danger.\x02\x03",
            "#00100FBecause Shin is clever\x01",
            "You know the circumstances, do not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Well …\x01",
            "Certainly I can understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHehe, it was good.\x01",
            "As expected, Shin is a wise gentleman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Is that … Yes.\x01",
            "I am a good boy, Oguchi!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_A0FE")

    ChrTalk(
        0x104,
        "#00309F(Haha, the effect of young lady is enormous.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A17C")

    label("loc_A0FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_A144")

    ChrTalk(
        0x109,
        (
            "#10109F(Haha,\x01",
            "Ellie 's effect is tremendous. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A17C")

    label("loc_A144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_A17C")

    ChrTalk(
        0x105,
        "#10302F(Huhu, the effect of Ellie is enormous.\x02",
    )

    CloseMessageWindow()

    label("loc_A17C")

    SetScenarioFlags(0x1DC, 7)
    Jump("loc_A1CC")

    label("loc_A184")


    ChrTalk(
        0x101,
        (
            "#00000FNow I am taking a shin.\x01",
            "Let's stop entering weapons shops.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A1CC")

    TalkEnd(0xFF)
    Return()

    # Function_25_9CD7 end

    def Function_26_A1D0(): pass

    label("Function_26_A1D0")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x14, 0x0)
    OP_4B(0x15, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 150, 0, -3900, 0)
    SetChrPos(0x109, 1330, 0, -4640, 0)
    SetChrPos(0x102, 2590, 0, -3300, 315)
    SetChrPos(0x103, -1610, 0, -4590, 0)
    SetChrPos(0x105, -900, 0, -5970, 0)
    SetChrPos(0x104, 740, 0, -6130, 0)
    OP_68(-1190, 1900, -5280, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(11710, 0)
    SetChrFlags(0xF, 0x8)
    OP_0D()
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 7)), scpexpr(EXPR_END)), "loc_A518")

    ChrTalk(
        0x14,
        "Hello, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Everyone in the Special Affairs Division,\x01",
            "Serward Noel also appreciates.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FIs cheers for good work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "By the way, my previous work\x01",
            "Is it alright?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A3CF")

    ChrTalk(
        0x101,
        (
            "#00002F#2POh, after I solved it just now.\x01",
            "Thanks to Franz, thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Haha, I do not quite understand it\x01",
            "I am honored to serve you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A490")

    label("loc_A3CF")


    ChrTalk(
        0x101,
        (
            "#00003F#2POh, oh …… It's the place I just finished.\x02\x03",
            "#00006F(Because I ignored the story\x01",
            "I missed the cheaters … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Haha, I do not quite understand it\x01",
            "I wish I had a paragraph.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A490")


    ChrTalk(
        0x101,
        (
            "#00005F#2PBy the way, Franz,\x01",
            "Today you guard here\x01",
            "You were in?\x02\x03",
            "Always Kate senpai\x01",
            "It's a place to guard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A602")

    label("loc_A518")


    ChrTalk(
        0x14,
        "Hey, are not they Lloyd's?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Everyone in the Special Affairs Division,\x01",
            "Serward Noel also appreciates.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FIs cheers for good work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#2PFranz, today you are\x01",
            "You guarded in here, are not you?\x02\x03",
            "Always Kate senpai\x01",
            "It's a place to guard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A602")


    ChrTalk(
        0x14,
        (
            "Oh, my seniors in a separate case\x01",
            "I'm going to other places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Temporarily place this place\x01",
            "It was supposed to be security.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-2320, 2800, -900, 2000)
    MoveCamera(45, 8, 0, 2000)
    OP_6E(660, 2000)
    SetCameraDistance(15930, 2000)
    Sleep(2500)

    ChrTalk(
        0x102,
        (
            "#12P#00108F\"Cross Bell's Bell\" … …\x01",
            "The red constellation stole it\x01",
            "You guessed it.\x02\x03",
            "#00101FThe security here is also being strengthened\x01",
            "That's the relationship, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Anyway, important to the crossbell\x01",
            "Cultural property is stolen translation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Just to be sure, I got from the guard\x01",
            "I'm coming to cheer.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1190, 1900, -5280, 2000)
    MoveCamera(45, 21, 0, 2000)
    OP_6E(660, 2000)
    SetCameraDistance(11710, 2000)
    Sleep(2500)

    ChrTalk(
        0x103,
        (
            "#00206F#3PThe stolen purpose,\x01",
            "Places brought in\x01",
            "I do not understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Oh, once the police and the guards\x01",
            "I am searching, but,\x01",
            "It is in a state not found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#4PUncle Takashi ……\x01",
            "What on earth do you do this\x01",
            "Did you do it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F#4PJuff, a bit to carry around\x01",
            "It's a bulky thing but.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#2P……Anyways,\x01",
            "Leave things about \"bells\"\x01",
            "Let us do our work.\x02\x03",
            "#00000FWell then, Franz.\x01",
            "Take care of the city guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Oh, I see you again.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0x14, 0x0)
    OP_4C(0x15, 0x0)
    ClearChrFlags(0xF, 0x8)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 150, 0, -3900, 0)
    SetScenarioFlags(0x190, 4)
    EventEnd(0x5)
    Return()

    # Function_26_A1D0 end

    SaveToFile()

Try(main)

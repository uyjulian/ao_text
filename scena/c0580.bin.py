from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0580.bin",                # FileName
        "c0580",                    # MapName
        "c0580",                    # Location
        0x0028,                     # MapIndex
        "ed7117",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 40, 0, 0, 0, 1],
    )

    BuildStringList((
        "c0580",                  # 0
        "Mrs. Imelda",            # 1
        "SE制御",                 # 2
    ))

    AddCharChip((
        "chr/ch09002.itc",                   # 00
    ))

    DeclNpc(4294966546, 100,     4800,    180,  261,  0x0, 0,   0,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(4294966546, 0,       3500,    1500,    4294966546, 1500,    4800,    0x007E, 0,  2,  0x0000)

    ChipFrameInfo(276, 0)                                        # 0

    ScpFunction((
        "Function_0_114",          # 00, 0
        "Function_1_126",          # 01, 1
        "Function_2_19B",          # 02, 2
        "Function_3_19F",          # 03, 3
        "Function_4_235F",         # 04, 4
        "Function_5_2C9C",         # 05, 5
        "Function_6_39B9",         # 06, 6
        "Function_7_39CF",         # 07, 7
    ))


    def Function_0_114(): pass

    label("Function_0_114")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Return()

    # Function_0_114 end

    def Function_1_126(): pass

    label("Function_1_126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_142")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_159")

    label("loc_142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_159")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17A")
    Sound(128, 1, 50, 0)

    label("loc_17A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_191")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)

    label("loc_191")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x0)
    Return()

    # Function_1_126 end

    def Function_2_19B(): pass

    label("Function_2_19B")

    Call(0, 3)
    Return()

    # Function_2_19B end

    def Function_3_19F(): pass

    label("Function_3_19F")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C1")
    TalkEnd(0x8)
    Call(0, 5)
    Return()

    label("loc_1C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E4")
    TalkEnd(0x8)
    Call(0, 4)
    Return()

    label("loc_1E4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_235B")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Shop\x01",      # 1
            "Quit\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23E")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_23E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_25D")
    OP_AF(0x43)
    Jump("loc_26F")

    label("loc_25D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_26D")
    OP_AF(0x44)
    Jump("loc_26F")

    label("loc_26D")

    OP_AF(0x43)

    label("loc_26F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2356")

    label("loc_27E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_292")
    Jump("loc_2356")

    label("loc_292")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2356")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_519")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45D")

    ChrTalk(
        0x8,
        (
            "(*klak klak, klak klak*...) \x01",
            "So the President was arrested and a giant\x01",
            "tree has appeared in the Marshlands, eh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Especially regarding that giant\x01",
            "tree, various guesses about it\x01",
            "are flying across the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since such a thing has appeared, \x01",
            "maybe I should make it a new\x01",
            "tourist attraction?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If I did that, I would even\x01",
            "make a killing once diplomatic\x01",
            "relations resume. Ihya hya hya...!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_514")

    label("loc_45D")


    ChrTalk(
        0x8,
        (
            "Although the world is in a\x01",
            "uproar, to me that giant tree\x01",
            "looks like a jade plant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've got to secure it as my\x01",
            "property for when diplomatic\x01",
            "relations resume. Ihya hya hya...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_514")

    Jump("loc_2356")

    label("loc_519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_72C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A1")

    ChrTalk(
        0x8,
        "Oh? If it isn't the Support Section kids.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now that you guys are here, things\x01",
            "are going to get interesting again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FInteresting for you, but troublesome for us...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FAnyway, please be careful\x01",
            "not to go outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I got it, I got it. I'll just\x01",
            "watch the proceedings from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At least get that\x01",
            "President for me.\x01",
            "Ihya hya hya...!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_727")

    label("loc_6A1")


    ChrTalk(
        0x8,
        (
            "Now that you guys are here, things\x01",
            "are going to get interesting again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At least get that\x01",
            "President for me.\x01",
            "Ihya hya hya...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_727")

    Jump("loc_2356")

    label("loc_72C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D1")

    ChrTalk(
        0x8,
        (
            "Ihya hya hya...! That address\x01",
            "was pretty interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can't believe he'd insult the\x01",
            "Empire and Republic that badly.\x01",
            "It was beyond my expectations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now then. I don't know what that Dieter\x01",
            "boy is planning, but neither the Empire\x01",
            "nor the Republic are going to stay quiet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya, I've got to move the\x01",
            "mountain of antiques in my storehouse\x01",
            "somewhere safe while I still can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9B2")

    label("loc_8D1")


    ChrTalk(
        0x8,
        (
            "I don't know what that Dieter boy is\x01",
            "planning, but neither the Empire nor\x01",
            "the Republic are going to stay quiet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya, I've got to move the\x01",
            "mountain of antiques in my storehouse\x01",
            "somewhere safe while I still can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B2")

    Jump("loc_2356")

    label("loc_9B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD7")

    ChrTalk(
        0x8,
        (
            "During that attack, a giant monster\x01",
            "appeared in Downtown and destroyed\x01",
            "the apartments I own there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya, from the condition they were in,\x01",
            "I can only laugh at the fact they were destroyed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...*sigh*, good grief.\x01",
            "What will happen to that area?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B92")

    label("loc_AD7")


    ChrTalk(
        0x8,
        (
            "I went to see my destroyed apartments,\x01",
            "but I couldn't help but laugh at their condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Rebuilding them will be a pain\x01",
            "and take a lot of mira...\x01",
            "I'd rather just sell the land.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B92")

    Jump("loc_2356")

    label("loc_B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD6")

    ChrTalk(
        0x8,
        (
            "Those jaegers. Occupying\x01",
            "a town is an outrageous\x01",
            "act, to be sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I tried to contact the Doll\x01",
            "Studio along the mountain\x01",
            "path, but it wouldn't connect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya. It's Jｶrg, so\x01",
            "I suppose there's no\x01",
            "need to be worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He might even be making dolls\x01",
            "in a situation like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D89")

    label("loc_CD6")


    ChrTalk(
        0x8,
        (
            "I tried to contact the Doll\x01",
            "Studio along the mountain\x01",
            "path, but it wouldn't connect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heehee. Well, it's Jｶrg, so\x01",
            "he might be making dolls\x01",
            "even in a situation like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D89")

    Jump("loc_2356")

    label("loc_D8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_FDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F47")

    ChrTalk(
        0x8,
        (
            "Ihya hya. With this rain,\x01",
            "I get even fewer\x01",
            "customers than normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since you're all here, will\x01",
            "you do the shelf cleaning\x01",
            "I usually do at this time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FA-As expected, we'll pass.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya. That was a joke. There's\x01",
            "expensive goods on those shelves.\x01",
            "I won't ever let a soul touch them.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetScenarioFlags(0x0, 0)
    Jump("loc_FD8")

    label("loc_F47")


    ChrTalk(
        0x8,
        (
            "According to the orbal net,\x01",
            "it'll be clear this afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya. While that may be true, it\x01",
            "doesn't mean I'll have more customers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD8")

    Jump("loc_2356")

    label("loc_FDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1147")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10AB")

    ChrTalk(
        0x8,
        (
            "I just saw some info\x01",
            "on the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They said there was\x01",
            "a train derailment at \x01",
            "West Crossbell Highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya. Is it just\x01",
            "me that smells\x01",
            "something suspicious?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1142")

    label("loc_10AB")


    ChrTalk(
        0x8,
        (
            "According to the orbal net,\x01",
            "a train derailment occurred at\x01",
            "West Crossbell Highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya. Is it just\x01",
            "me that smells\x01",
            "something suspicious?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1142")

    Jump("loc_2356")

    label("loc_1147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_12FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1259")

    ChrTalk(
        0x8,
        (
            "Even someone like me\x01",
            "don't know many things\x01",
            "about that old man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They say he's an eccentric,\x01",
            "taciturn doll maker who \x01",
            "doesn't show his face often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I'm good as long as I can \x01",
            "make a profit from that Doll Studio.\x01",
            "Ihya hya hya...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12F9")

    label("loc_1259")


    ChrTalk(
        0x8,
        (
            "Even someone like me\x01",
            "don't know many things\x01",
            "about that old man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I'm good as long as I can \x01",
            "make a profit from that Doll Studio.\x01",
            "Ihya hya hya...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12F9")

    Jump("loc_2356")

    label("loc_12FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_14B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1419")

    ChrTalk(
        0x8,
        (
            "(*klak klak klak klak*...)\x01",
            "Hmm, I see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even on the orbal net\x01",
            "there're arguments for and\x01",
            "against the independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's no mistake\x01",
            "that supporters posted\x01",
            "most of them, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya. The arguments continue,\x01",
            "but I'm still deciding.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14AC")

    label("loc_1419")


    ChrTalk(
        0x8,
        (
            "It seems there're arguments for\x01",
            "and against the independence\x01",
            "on the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya. The arguments continue,\x01",
            "but I'm still deciding.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14AC")

    Jump("loc_2356")

    label("loc_14B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_185D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17B8")

    ChrTalk(
        0x8,
        (
            "Oh, you are...\x01",
            "From Epstein aren't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FIt's been awhile, Mrs. Imelda.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya. So finally, all Special\x01",
            "Support Section members are assembled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It looks like you have been assigned to \x01",
            "the Trade Conference security. Having a\x01",
            "perfect security system is what's important.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FAs usual, it seems\x01",
            "you know quite a bit...\x02\x03",
            "#00000FIn your case, Mrs. Imelda...\x01",
            "In a certain sense it's reassuring you\x01",
            "get info only for your personal enjoyment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya. You can rest easy\x01",
            "on that point, as I don't care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I believe in acting\x01",
            "so as not to get\x01",
            "caught by the police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F...Telling this\x01",
            "to us is...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 4)
    Jump("loc_1858")

    label("loc_17B8")


    ChrTalk(
        0x8,
        (
            "Ihya hya. So finally, all Special\x01",
            "Support Section members are assembled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm looking forward to seeing \x01",
            "what you guys do from\x01",
            "here on, in my own way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1858")

    Jump("loc_2356")

    label("loc_185D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1A55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1999")

    ChrTalk(
        0x8,
        (
            "(*klak klak klak klak*...)\x01",
            "Ho ho, I see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's a big fuss\x01",
            "over Orchis Tower\x01",
            "on the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder if it will have a\x01",
            "positive effect on our\x01",
            "economy because of tourism.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya. I've got to secure\x01",
            "property from which the tower can\x01",
            "be seen well while I still can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A50")

    label("loc_1999")


    ChrTalk(
        0x8,
        (
            "I wonder if it will have a\x01",
            "positive effect on our\x01",
            "economy because of tourism.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya. I've got to secure\x01",
            "property from which the tower can\x01",
            "be seen well while I still can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A50")

    Jump("loc_2356")

    label("loc_1A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1DD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B8D")

    ChrTalk(
        0x8,
        (
            "Oh yes, I recently started to read a\x01",
            "serially released novel series, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Interesting was interesting, but\x01",
            "it just didn't match my tastes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya, this is my chance.\x01",
            "I'll force it on you guys.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2F0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2F0, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x188, 2)
    Jump("loc_1DCD")

    label("loc_1B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CE0")

    ChrTalk(
        0x8,
        (
            "I heard the heads of state are gathering\x01",
            "for tomorrow's Trade Conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The other leaders aside, I'd want to see\x01",
            "the "Blood and Iron Chancellor" and\x01",
            "the Republican President face off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The countries have long opposed each other,\x01",
            "so I wonder how their meeting will go...\x01",
            "Ihya hya, it'll be a sight to see.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DCD")

    label("loc_1CE0")


    ChrTalk(
        0x8,
        (
            "I'd absolutely want to see the "Blood and\x01",
            "Iron Chancellor" and the Republican\x01",
            "President face off tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The countries have long opposed each other,\x01",
            "so I wonder how their meeting will go...\x01",
            "Ihya hya, it'll be a sight to see.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DCD")

    Jump("loc_2356")

    label("loc_1DD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_1F39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EB0")

    ChrTalk(
        0x8,
        (
            "It seems some suspicious\x01",
            "people entered the old Revache\x01",
            "building the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And here I thought Heiyue had\x01",
            "gotten their hands on it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya, things are\x01",
            "getting interesting.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F34")

    label("loc_1EB0")


    ChrTalk(
        0x8,
        (
            "Just when I thought Heiyue would get their\x01",
            "hands on the old Revache building...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya, things are\x01",
            "getting interesting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F34")

    Jump("loc_2356")

    label("loc_1F39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_21AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20E7")

    ChrTalk(
        0x8,
        (
            "Come to think of it, the old Revache\x01",
            "building in the back alley is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At this rate, it'll belong\x01",
            "to Heiyue before long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya. Being this the case,\x01",
            "I should've bought it before\x01",
            "and sold it back at a high price.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(Oh yeah. Come to think of it,\x01",
            "she's a land owner...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21AA")

    label("loc_20E7")


    ChrTalk(
        0x8,
        (
            "By the way, the old Revache\x01",
            "building in the back alley...\x01",
            "It seems Heiyue will acquire it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya. Being this the case,\x01",
            "I should've bought it before\x01",
            "and sold it back at a high price.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21AA")

    Jump("loc_2356")

    label("loc_21AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2356")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22E3")

    ChrTalk(
        0x8,
        (
            "I'll take notice of the restarted\x01",
            "Support Section going forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya... \x01",
            "I'll look forward to the fun of seeing\x01",
            "you making hot news again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FI-It's not that we're doing it\x01",
            "so you can have fun, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309FHu hu, what a very interesting old lady.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2356")

    label("loc_22E3")


    ChrTalk(
        0x8,
        (
            "I'll take notice of the restarted\x01",
            "Support Section going forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya, entertain\x01",
            "me again, will you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2356")

    Jump("loc_1EE")

    label("loc_235B")

    TalkEnd(0x8)
    Return()

    # Function_3_19F end

    def Function_4_235F(): pass

    label("Function_4_235F")

    EventBegin(0x0)
    Fade(500)
    OP_68(-730, 1150, 2860, 0)
    MoveCamera(314, 24, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24040, 0)
    SetChrPos(0x101, -1540, 0, 1900, 45)
    SetChrPos(0x102, 390, 0, 2110, 0)
    SetChrPos(0x109, -1050, 0, 800, 0)
    SetChrPos(0x105, 150, 0, 830, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#11PIhya hya, welcome.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#11POhh look, it's the\x01",
            "little SSS team again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PIhya hya, it's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FLong time no see, Mrs. Imelda.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FYou look well, as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHmph, I sure don't feel that way.\x01",
            "Lately it's just been one\x01",
            "boring day after another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PRevache has gone out of business, and you guys\x01",
            "suspended your activities for awhile, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAnd on top of all that, even\x01",
            "my info broker on the orbal\x01",
            "net has closed up shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105F(An information broker on the orbal net...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F(She must be talking about Jona.\x01",
            " Now he's transferred to the Foundation...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#11POh, come to think of it, there's\x01",
            "some faces I don't recognize.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAre you the new\x01",
            "SSS guys?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PA Guardian Force member, and the leader of a\x01",
            "delinquent group... Ihya hya, now that you've\x01",
            "restarted, all the interesting pieces are lined up.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#6P#10105FW-Wait, how did you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FUhhm, don't you think you\x01",
            "know too much even without\x01",
            "using your information broker?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIhya hya hya...\x01",
            "It's not like I only\x01",
            "have one source.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10309FAhaha, what a very interesting old lady.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#11POh right, since you guys\x01",
            "all came all this way,\x01",
            "I'll give you this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PHere, take it.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x321),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x321, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        "#6P#00105FThis is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIhya hya, it's the key to my\x01",
            "property, the lovely "Maison\x01",
            "Imelda" in Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FOh yeah I remember seeing\x01",
            "that name on the side of a\x01",
            "run-down apartment building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PHey! It's not run down!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHmph, well whatever. At least the monsters\x01",
            "love it. They're infesting the place.\x01",
            "Clean them up for me if you feel like it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00006FW-Wait, I'm sure you even\x01",
            "put up an extermination\x01",
            "support request...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106FSo in the end, we're being forced into it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIhya hya... \x01",
            "Well, only if you feel like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PGood luck, young ones.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -750, 0, 2000, 0)
    SetScenarioFlags(0x139, 4)
    OP_29(0x67, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_4_235F end

    def Function_5_2C9C(): pass

    label("Function_5_2C9C")

    EventBegin(0x0)
    Fade(500)
    SoundLoad(841)
    OP_68(-730, 1150, 2860, 0)
    MoveCamera(314, 24, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24040, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -250, 0, 2000, 0)
    SetChrPos(0x102, -1250, 0, 1750, 0)
    SetChrPos(0x103, -250, 0, 500, 0)
    SetChrPos(0x104, -1250, 0, 250, 0)
    SetChrPos(0x109, -2840, 0, 390, 44)
    SetChrPos(0x105, -1360, 0, -710, 44)
    OP_0D()
    BeginChrThread(0x9, 1, 0, 6)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Mrs. Imelda is using a communication device\x01",
            "installed beneath the counter.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x9, 1)

    ChrTalk(
        0x8,
        (
            "#11P...Tch, damn old man. \x01",
            "He's not picking up at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FMrs. Imelda, what\x01",
            "are you doing?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3061")

    ChrTalk(
        0x8,
        "#11POh, it's you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAh, I wanted to ask that Jｶrg\x01",
            "about my new doll, and so\x01",
            "I was trying to contact him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FMeister Jｶrg...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYeah, but ever since earlier\x01",
            "it just won't connect at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHe's probably at the Doll Studio, but...\x01",
            "Tch, if he's in the middle of working,\x01",
            "it'll be awhile before he answers.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#6P#00003F(...We heard that Meister Jｶrg is an\x01",
            "old acquaintance of Mrs. Imelda\x01",
            "from that request we did earlier.)\x02\x03",
            "(This is a chance, so maybe I'll ask\x01",
            "her something about the Doll Studio.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34C2")

    label("loc_3061")


    ChrTalk(
        0x8,
        "#11POh, it's you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAh, I wanted to ask that Jｶrg\x01",
            "about my new doll, and so\x01",
            "I was trying to contact him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PBut ever since earlier\x01",
            "it just won't connect at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHe's probably at the Doll Studio, but...\x01",
            "Tch, if he's in the middle of working,\x01",
            "it'll be awhile before he answers.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)
    Sleep(50)
    OP_64(0x102)
    Sleep(50)
    OP_64(0x103)
    Sleep(50)
    OP_64(0x104)
    Sleep(50)
    OP_64(0x109)
    Sleep(50)
    OP_64(0x105)

    ChrTalk(
        0x101,
        (
            "#6P#00005FJｶrg...\x01",
            "And a new doll...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00005FC-Could you be talking about...\x01",
            "Jｶrg Rosenberg, the engineer!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FMrs. Imelda, do\x01",
            "you know him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYeah. For now, I have a\x01",
            "contract to be his doll\x01",
            "sales representative.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIt's just, he's an eccentric\x01",
            "old man. He's inflexible and\x01",
            "easily annoyed.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#6P#00006F(...To think we'd find an acquaintance\x01",
            "of his in a place like this.)\x02\x03",
            "(This is a chance, so maybe I'll ask\x01",
            "her something about the Doll Studio.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34C2")


    ChrTalk(
        0x8,
        (
            "#11P...Even so, do you all\x01",
            "need something with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIhya hya. If you need to\x01",
            "deal in antiques, I'm\x01",
            "ready anytime, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FU-Umm, it's not that. We'd like\x01",
            "to ask you a little something...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd asked about the Rosenberg\x01",
            "Studio and Meister Jｶrg.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#11P...Why are you guys snooping\x01",
            "around there again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FU-Umm... \x01",
            "We were just curious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POh well, fine...\x01",
            "Not even I know that\x01",
            "much about Jｶrg.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThey say he's an eccentric,\x01",
            "taciturn doll maker who \x01",
            "doesn't show his face often.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_376D")

    ChrTalk(
        0x8,
        (
            "#11PI told you before too he's handling\x01",
            "the Arc-en-ciel's stage settings...\x01",
            "But I don't know any more than that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37BD")

    label("loc_376D")


    ChrTalk(
        0x8,
        (
            "#11PAlthough I'm his sales rep, I don't\x01",
            "know the details of his situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37BD")


    ChrTalk(
        0x109,
        "#10106FI-Is that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWell, as long as I can profit\x01",
            "off his dolls, I'm happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI don't know about that\x01",
            "old man's private life\x01",
            "Ihya hya hya...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303F(I-I see... That's a pretty\x01",
            "distant relationship.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200F(That could be the very\x01",
            "reason why they remain\x01",
            "acquainted...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300F(Well, if this is how it is,\x01",
            "I suppose our only choice\x01",
            "is to visit him directly...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000F(You're right...\x01",
            "Let's go, everyone.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -750, 0, 2000, 0)
    SetScenarioFlags(0x16F, 5)
    OP_24(0x349)
    EventEnd(0x5)
    Return()

    # Function_5_2C9C end

    def Function_6_39B9(): pass

    label("Function_6_39B9")

    Sound(841, 2, 50, 0)
    Sleep(1800)
    OP_24(0x349)
    Sound(813, 0, 20, 0)
    Sleep(500)
    Return()

    # Function_6_39B9 end

    def Function_7_39CF(): pass

    label("Function_7_39CF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_7_39CF end

    SaveToFile()

Try(main)

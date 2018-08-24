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
        "Function_4_220D",         # 04, 4
        "Function_5_2AF0",         # 05, 5
        "Function_6_37E4",         # 06, 6
        "Function_7_37FA",         # 07, 7
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2209")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Shop\x01",        # 1
            "Cancel\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_240")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_240")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_280")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_25F")
    OP_AF(0x43)
    Jump("loc_271")

    label("loc_25F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_26F")
    OP_AF(0x44)
    Jump("loc_271")

    label("loc_26F")

    OP_AF(0x43)

    label("loc_271")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2204")

    label("loc_280")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_294")
    Jump("loc_2204")

    label("loc_294")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2204")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42F")

    ChrTalk(
        0x8,
        (
            "(*typing*...) So the president\x01",
            "was arrested and a huge tree\x01",
            "has appeared, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Especially regarding that huge\x01",
            "tree, various guesses about it\x01",
            "are flying across the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since such a thing has\x01",
            "appeared, maybe I should make\x01",
            "it a new tourist attraction?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If I do that, I'll make a\x01",
            "killing once diplomatic\x01",
            "relations resume. Hya hya hya!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4E4")

    label("loc_42F")


    ChrTalk(
        0x8,
        (
            "Although the world is in a\x01",
            "uproar, to me that huge tree\x01",
            "looks like a jade plant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've got to secure it as my\x01",
            "property for when diplomatic\x01",
            "relations resume. Hya hya hya...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E4")

    Jump("loc_2204")

    label("loc_4E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_700")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_679")

    ChrTalk(
        0x8,
        (
            "Oh? If it isn't the\x01",
            "Support Section kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now that you guys are\x01",
            "here, things are going to\x01",
            "get interesting again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FIf you're amused, then\x01",
            "it means problems for\x01",
            "us, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FAnyway, please be\x01",
            "careful not to go\x01",
            "outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I got it, I got it. I'll\x01",
            "just watch the\x01",
            "proceedings from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At least get that\x01",
            "President for me. Hya\x01",
            "hya hya!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_6FB")

    label("loc_679")


    ChrTalk(
        0x8,
        (
            "Now that you guys are\x01",
            "here, things are going to\x01",
            "get interesting again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At least get that\x01",
            "President for me. Hya\x01",
            "hya hya!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FB")

    Jump("loc_2204")

    label("loc_700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_985")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A0")

    ChrTalk(
        0x8,
        (
            "Hya hya hya! That\x01",
            "address was pretty\x01",
            "interesting.\x02",
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
            "Hya hya, I've got to move the\x01",
            "mountain of antiques in my storehouse\x01",
            "somewhere safe while I still can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_980")

    label("loc_8A0")


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
            "Hya hya, I've got to move the\x01",
            "mountain of antiques in my storehouse\x01",
            "somewhere safe while I still can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_980")

    Jump("loc_2204")

    label("loc_985")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA3")

    ChrTalk(
        0x8,
        (
            "During that attack, a giant monster\x01",
            "appeared in Downtown and destroyed\x01",
            "the apartment I own there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hya hya, from the condition\x01",
            "it was in, I can only laugh\x01",
            "at the fact it was destroyed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...*sigh*, good grief.\x01",
            "What's going to happen\x01",
            "to that area?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B59")

    label("loc_AA3")


    ChrTalk(
        0x8,
        (
            "I went to see my destroyed\x01",
            "apartment, but I couldn't help\x01",
            "but laugh at its condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Rebuilding it will be a pain\x01",
            "and take a lot of mira... I'd\x01",
            "rather just sell the land.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B59")

    Jump("loc_2204")

    label("loc_B5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C97")

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
            "I tried contacting the doll\x01",
            "studio along the mountain\x01",
            "path, but it wouldn't connect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hya hya. It's Jｶrg, so I\x01",
            "suppose there's no need\x01",
            "to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He might be making dolls\x01",
            "even in a situation like\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D4A")

    label("loc_C97")


    ChrTalk(
        0x8,
        (
            "I tried contacting the doll\x01",
            "studio along the mountain\x01",
            "path, but it wouldn't connect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heehee. Well, it's Jｶrg, so\x01",
            "he might be making dolls even\x01",
            "in a situation like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D4A")

    Jump("loc_2204")

    label("loc_D4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F01")

    ChrTalk(
        0x8,
        (
            "Hya hya. With this rain,\x01",
            "I get even fewer\x01",
            "customers than normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since you're all here, will\x01",
            "you do the shelf cleaning I\x01",
            "usually do at this time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FA-As expected, we'll\x01",
            "pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hya hya. That was a joke. There's\x01",
            "expensive goods on those shelves.\x01",
            "I won't let a soul touch them.\x02",
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
    Jump("loc_F91")

    label("loc_F01")


    ChrTalk(
        0x8,
        (
            "According to the orbal\x01",
            "net, it'll be clear this\x01",
            "afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hya hya. While that may\x01",
            "be true, it doesn't mean\x01",
            "I'll have more customers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F91")

    Jump("loc_2204")

    label("loc_F96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_10F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_105F")

    ChrTalk(
        0x8,
        (
            "I just saw some info on\x01",
            "the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They said there was a\x01",
            "derailment along West\x01",
            "Crossbell Highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hya hya. Is it just me\x01",
            "that smells something\x01",
            "suspicious?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10F2")

    label("loc_105F")


    ChrTalk(
        0x8,
        (
            "According to the orbal net,\x01",
            "a derailment occurred along\x01",
            "West Crossbell Highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hya hya. Is it just me\x01",
            "that smells something\x01",
            "suspicious?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10F2")

    Jump("loc_2204")

    label("loc_10F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1292")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11F7")

    ChrTalk(
        0x8,
        (
            "As expected, there's a\x01",
            "lot of info on that old\x01",
            "man on the net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They say he's an eccentric\x01",
            "doll maker who doesn't\x01",
            "show his face or speak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I'm good as long as\x01",
            "that doll studio's making\x01",
            "a profit. Hya hya hya...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_128D")

    label("loc_11F7")


    ChrTalk(
        0x8,
        (
            "As expected, there's a\x01",
            "lot of info on that old\x01",
            "man on the net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I'm good as long as\x01",
            "that doll studio's making\x01",
            "a profit. Hya hya hya...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_128D")

    Jump("loc_2204")

    label("loc_1292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_142A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1396")

    ChrTalk(
        0x8,
        (
            "(*typing*...) Hmm, I\x01",
            "see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even on the net there\x01",
            "are arguments for and\x01",
            "against independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's no mistake that\x01",
            "supporters posted most\x01",
            "of them, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hya hya. The arguments\x01",
            "continue, but I'm still\x01",
            "deciding.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1425")

    label("loc_1396")


    ChrTalk(
        0x8,
        (
            "It seems there are arguments\x01",
            "for and against independence\x01",
            "on the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hya hya. The arguments\x01",
            "continue, but I'm still\x01",
            "deciding.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1425")

    Jump("loc_2204")

    label("loc_142A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_17B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_170E")

    ChrTalk(
        0x8,
        (
            "Oh, you are... You're\x01",
            "from Epstein aren't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIt's been a while, Mrs.\x01",
            "Imelda.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hya hya. So finally, all\x01",
            "the Special Support Section\x01",
            "members are assembled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I looks like you guys are entering\x01",
            "the trade conference. I'm glad they\x01",
            "have a security detail set up.\x02",
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
            "#00006FAs usual, it seems you know quite a\x01",
            "bit...\x02\x03",
            "#00000FIn your case, you obtain\x01",
            "information for personal enjoyment.\x01",
            "In a way, you're helping us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hya hya. You can rest\x01",
            "easy on that point, as I\x01",
            "don't care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I believe in acting so\x01",
            "as not to get caught by\x01",
            "the police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F...That's our line,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 4)
    Jump("loc_17B0")

    label("loc_170E")


    ChrTalk(
        0x8,
        (
            "Hya hya. So finally, all\x01",
            "the Special Support Section\x01",
            "members are assembled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm looking forward to\x01",
            "seeing what you guys do from\x01",
            "here on, in my own way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17B0")

    Jump("loc_2204")

    label("loc_17B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1991")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18DC")

    ChrTalk(
        0x8,
        (
            "(*typing*...) Hoho, I\x01",
            "see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's a big fuss over\x01",
            "Orchis Tower on the\x01",
            "orbal net.\x02",
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
            "Hya hya. I've got to secure\x01",
            "property that can be seen from\x01",
            "the tower while I still can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_198C")

    label("loc_18DC")


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
            "Hya hya. I've got to secure\x01",
            "property that can be seen from\x01",
            "the tower while I still can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_198C")

    Jump("loc_2204")

    label("loc_1991")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1D0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AD4")

    ChrTalk(
        0x8,
        (
            "Oh yes, I recently\x01",
            "started reading a serial\x01",
            "novel series, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Interesting things are\x01",
            "interesting, but it just didn't\x01",
            "match my taste, you see?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hya hya, since you're\x01",
            "here. I think I'll force\x01",
            "it on you guys.\x02",
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
    Jump("loc_1D06")

    label("loc_1AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C1E")

    ChrTalk(
        0x8,
        (
            "I heard the heads of state\x01",
            "are gathering for tomorrow's\x01",
            "trade conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The other leaders aside, I want the\x01",
            "Blood and Iron Chancellor and the\x01",
            "Republican President to face off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The countries have long opposed each\x01",
            "other, so I wonder how their meeting will\x01",
            "go... Hya hya, it'll be a sight to see.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D06")

    label("loc_1C1E")


    ChrTalk(
        0x8,
        (
            "I absolutely want to see the Blood and\x01",
            "Iron Chancellor and the Republican\x01",
            "President face off tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The countries have long opposed each\x01",
            "other, so I wonder how their meeting will\x01",
            "go... Hya hya, it'll be a sight to see.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D06")

    Jump("loc_2204")

    label("loc_1D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_1E70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DE8")

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
            "And here I thought\x01",
            "Heiyue had gotten their\x01",
            "hands on it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hya hya, things are\x01",
            "getting interesting.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E6B")

    label("loc_1DE8")


    ChrTalk(
        0x8,
        (
            "Just when I thought Heiyue\x01",
            "would get their hands on\x01",
            "the old Revache building...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hya hya, things are\x01",
            "getting interesting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E6B")

    Jump("loc_2204")

    label("loc_1E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2092")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FF7")

    ChrTalk(
        0x8,
        (
            "Come to think of it, the\x01",
            "old Revache building in\x01",
            "the back alley is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At this rate, it'll\x01",
            "belong to Heiyue before\x01",
            "long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hya hya. If it happens,\x01",
            "my property values will\x01",
            "go up.\x02",
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
            "#00006F(Oh yeah. Come to think\x01",
            "of it, she's a land\x01",
            "owner...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_208D")

    label("loc_1FF7")


    ChrTalk(
        0x8,
        (
            "Oh yeah, the old Revache\x01",
            "building near the alley... It\x01",
            "seems Heiyue will acquire it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hya hya. If it happens,\x01",
            "my property values will\x01",
            "go up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_208D")

    Jump("loc_2204")

    label("loc_2092")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2204")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2192")

    ChrTalk(
        0x8,
        (
            "I'll take notice of the\x01",
            "restarted Support\x01",
            "Section going forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hya hya... I'll look\x01",
            "forward to good news\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FT-That's nothing to look\x01",
            "forward to, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHaha, what an\x01",
            "interesting old lady.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2204")

    label("loc_2192")


    ChrTalk(
        0x8,
        (
            "I'll take notice of the\x01",
            "restarted Support\x01",
            "Section going forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heehee, I'm always up\x01",
            "for a good time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2204")

    Jump("loc_1EE")

    label("loc_2209")

    TalkEnd(0x8)
    Return()

    # Function_3_19F end

    def Function_4_220D(): pass

    label("Function_4_220D")

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
        "#11PHeehee, welcome!\x02",
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
        (
            "#11PIhya hya, it's been a\x01",
            "while, hasn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FLong time no see, Mrs.\x01",
            "Imelda.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FYou look well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWell I sure don't feel that\x01",
            "way. Lately it's just been\x01",
            "one boring day after another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PRevache has gone out of business,\x01",
            "and you guys suspended your\x01",
            "activities for a while, too.\x02",
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
        (
            "#6P#00105F(An information broker\x01",
            "on the orbal net...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F(She must be talking\x01",
            "about Jona. He's working\x01",
            "at the foundation now.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#11POh, come to think of it,\x01",
            "there are some faces I\x01",
            "don't recognize.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAre you guys new\x01",
            "members?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PA guardian force member, and the leader of a\x01",
            "delinquent group... Heehee, now that you've\x01",
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
        "#6P#10105FWait, how did you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FWord gets around even\x01",
            "without information\x01",
            "brokers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHeehee, it's not like I\x01",
            "only have one source.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FAhaha, what an\x01",
            "interesting woman.\x02",
        )
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
            "#11PHeehee, it's the key to my\x01",
            "property, the lovely\x01",
            "Maison Imelda in Downtown.\x02",
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
            "#11PHumph, well whatever. At least the monsters\x01",
            "love it. They're infesting the place. Clean\x01",
            "them up for me if you feel like it.\x02",
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
            "#6P#00006FWait, this is sounding\x01",
            "strangely familiar...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FSo in the end, we're\x01",
            "being forced into it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHeehee... Well, only if\x01",
            "you feel like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PGood luck, little ones.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -750, 0, 2000, 0)
    SetScenarioFlags(0x139, 4)
    OP_29(0x67, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_4_220D end

    def Function_5_2AF0(): pass

    label("Function_5_2AF0")

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
            "Mrs. Imelda is using a\x01",
            "communication device installed\x01",
            "beneath the counter.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x9, 1)

    ChrTalk(
        0x8,
        (
            "#11P...Tch, that old man.\x01",
            "Make it a little easier\x01",
            "to get through!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FMrs. Imelda, what are\x01",
            "you doing?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2EB6")

    ChrTalk(
        0x8,
        "#11POh, it's you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAh, I wanted to ask Jｶrg\x01",
            "about my new doll, and so I\x01",
            "was trying to contact him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FOld Man Jｶrg?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYeah, but ever since\x01",
            "earlier it just won't\x01",
            "connect at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHe's probably at the doll studio, but...\x01",
            "Tch, if he's in the middle of working,\x01",
            "it'll be a while before he answers.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#6P#00003F(...We heard Jｶrg is an old\x01",
            "acquaintance of Mrs. Imelda from\x01",
            "that request we did earlier.)\x02\x03",
            "(This is a good opportunity...\x01",
            "I'll try asking her something\x01",
            "about the Doll Studio.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3311")

    label("loc_2EB6")


    ChrTalk(
        0x8,
        "#11POh, it's you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAh, I wanted to ask Jｶrg\x01",
            "about my new doll, and so I\x01",
            "was trying to contact him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI've been at it a while\x01",
            "and he just won't pick\x01",
            "up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHe's probably at the doll studio, but...\x01",
            "Tch, if he's in the middle of working,\x01",
            "it'll be a while before he answers.\x02",
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
            "#6P#00005FJｶrg... And she said a\x01",
            "new doll...\x02",
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
            "#6P#00005FC-Could you be talking\x01",
            "about... Jｶrg Rosenberg,\x01",
            "the engineer!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FMrs. Imelda, do you know\x01",
            "him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYeah. I'm basically his\x01",
            "doll sales\x01",
            "representative.\x02",
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
            "#6P#00006F(...To think we'd find an\x01",
            "acquaintance of his in a place\x01",
            "like this.)\x02\x03",
            "(This is a good opportunity...\x01",
            "I'll try asking her something\x01",
            "about the Doll Studio.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3311")


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
            "#11PHya hya. If you need to\x01",
            "deal in antiques, I'm\x01",
            "ready anytime, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FU-Umm, it's not that.\x01",
            "We'd like to ask you a\x01",
            "little something...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd asked about\x01",
            "Rosenberg Studio and Old\x01",
            "Man Jｶrg.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#11P...What are you guys\x01",
            "doing snooping around\x01",
            "there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FU-Umm~... We were just\x01",
            "curious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAh, it's fine... Not\x01",
            "even I know that much\x01",
            "about Jｶrg.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThey say he's an eccentric\x01",
            "doll maker who doesn't\x01",
            "show his face or speak.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_359B")

    ChrTalk(
        0x8,
        (
            "#11PI asked him to handle the Arc-\x01",
            "en-Ciel set once. I don't know\x01",
            "what happened after that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EB")

    label("loc_359B")


    ChrTalk(
        0x8,
        (
            "#11PAlthough I'm his sales\x01",
            "rep, I don't know the\x01",
            "details of his situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35EB")


    ChrTalk(
        0x109,
        "#10106FI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWell, as long as I can\x01",
            "profit off his dolls,\x01",
            "I'm happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI don't know about that\x01",
            "old man's private life.\x01",
            "Hya hya hya...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303F(I-I see... That's a\x01",
            "pretty distant\x01",
            "relationship.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200F(That could be the very\x01",
            "reason why they remain\x01",
            "acquainted, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300F(Well, if this is how it is,\x01",
            "I suppose our only choice is\x01",
            "to visit him directly.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000F(You're right... Let's\x01",
            "go, everyone.)\x02",
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

    # Function_5_2AF0 end

    def Function_6_37E4(): pass

    label("Function_6_37E4")

    Sound(841, 2, 50, 0)
    Sleep(1800)
    OP_24(0x349)
    Sound(813, 0, 20, 0)
    Sleep(500)
    Return()

    # Function_6_37E4 end

    def Function_7_37FA(): pass

    label("Function_7_37FA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_7_37FA end

    SaveToFile()

Try(main)

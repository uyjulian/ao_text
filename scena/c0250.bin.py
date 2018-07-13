from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0250.bin",                # FileName
        "c0250",                    # MapName
        "c0250",                    # Location
        0x000E,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 14, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0250",                  # 0
        "Leyte",                  # 1
        "Pinset",                 # 2
        "Fei",                    # 3
        "Kｷken",                 # 4
        "Ryｹ",                   # 5
        "Chiruru",                # 6
    ))

    AddCharChip((
        "chr/ch10300.itc",                   # 00
        "chr/ch22300.itc",                   # 01
        "chr/ch22302.itc",                   # 02
        "chr/ch32700.itc",                   # 03
        "chr/ch32702.itc",                   # 04
        "apl/ch50148.itc",                   # 05
        "chr/ch21000.itc",                   # 06
        "chr/ch21002.itc",                   # 07
        "chr/ch20600.itc",                   # 08
        "chr/ch20500.itc",                   # 09
    ))

    DeclNpc(51830,   0,       115930,  0,    261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4294912986, 0,       52840,   90,   261,  0x0, 0,   1,   0,   0,   1,   0,   6,   255,  0)
    DeclNpc(4294913916, 0,       52599,   270,  261,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4294915377, 0,       108370,  90,   261,  0x0, 0,   6,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4294909296, 0,       107489,  0,    389,  0x0, 0,   8,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4294909567, 0,       106739,  180,  389,  0x0, 0,   9,   0,   0,   0,   0,   13,  255,  0)

    ChipFrameInfo(412, 0)                                        # 0

    ScpFunction((
        "Function_0_19C",          # 00, 0
        "Function_1_24C",          # 01, 1
        "Function_2_277",          # 02, 2
        "Function_3_5E2",          # 03, 3
        "Function_4_64A",          # 04, 4
        "Function_5_1F9C",         # 05, 5
        "Function_6_23AF",         # 06, 6
        "Function_7_2FE9",         # 07, 7
        "Function_8_3182",         # 08, 8
        "Function_9_3AC5",         # 09, 9
        "Function_10_4906",        # 0A, 10
        "Function_11_4A6F",        # 0B, 11
        "Function_12_4B99",        # 0C, 12
        "Function_13_4CCF",        # 0D, 13
    ))


    def Function_0_19C(): pass

    label("Function_0_19C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1D4"),
        (1, "loc_1E0"),
        (2, "loc_1EC"),
        (3, "loc_1F8"),
        (4, "loc_204"),
        (5, "loc_210"),
        (6, "loc_21C"),
        (SWITCH_DEFAULT, "loc_228"),
    )


    label("loc_1D4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_1E0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_1EC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_1F8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_204")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_210")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_21C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_228")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_234")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_24B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_24B")

    Return()

    # Function_0_19C end

    def Function_1_24C(): pass

    label("Function_1_24C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_276")
    OP_94(0xFE, 0xFFFF28BA, 0xC9A4, 0xFFFF30C6, 0xD2C8, 0x3E8)
    Sleep(300)
    Jump("Function_1_24C")

    label("loc_276")

    Return()

    # Function_1_24C end

    def Function_2_277(): pass

    label("Function_2_277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_296")
    SetChrPos(0xA, -58130, 0, 58620, 0)
    Jump("loc_5E1")

    label("loc_296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2E0")
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -54030, 0, 104830, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -53850, 0, 106300, 180)
    SetChrFlags(0xD, 0x10)
    Jump("loc_5E1")

    label("loc_2E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_32B")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xA, -51060, 400, 56380, 180)
    SetChrChipByIndex(0xA, 0x4)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -56700, 0, 110990, 225)
    Jump("loc_5E1")

    label("loc_32B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_33E")
    SetChrFlags(0xA, 0x80)
    Jump("loc_5E1")

    label("loc_33E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_369")
    SetChrPos(0x9, -58130, 0, 58620, 0)
    BeginChrThread(0x9, 0, 0, 0)
    BeginChrThread(0xA, 0, 0, 1)
    Jump("loc_5E1")

    label("loc_369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_39E")
    SetChrPos(0xA, -51250, 500, 57180, 315)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x40)
    EndChrThread(0xA, 0x0)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    Jump("loc_5E1")

    label("loc_39E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3B1")
    SetChrFlags(0xA, 0x80)
    Jump("loc_5E1")

    label("loc_3B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3CF")
    SetChrFlags(0x8, 0x80)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    Jump("loc_5E1")

    label("loc_3CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_426")
    SetChrPos(0xA, -51250, 500, 57180, 315)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x40)
    EndChrThread(0xA, 0x0)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x7)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xB, -51780, 150, 112520, 90)
    Jump("loc_5E1")

    label("loc_426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_45B")
    SetChrPos(0x9, -57750, 400, 52200, 180)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x80)
    Jump("loc_5E1")

    label("loc_45B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_494")
    SetChrPos(0x9, -58130, 0, 58620, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_484")
    SetChrFlags(0x9, 0x10)

    label("loc_484")

    SetChrFlags(0xA, 0x80)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_5E1")

    label("loc_494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4E5")
    SetChrPos(0x9, -58130, 0, 58620, 0)
    SetChrFlags(0x9, 0x10)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xB, 0x7)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xB, -51780, 150, 112520, 90)
    Jump("loc_5E1")

    label("loc_4E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4F8")
    SetChrFlags(0xA, 0x80)
    Jump("loc_5E1")

    label("loc_4F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_567")
    SetChrPos(0x8, 57650, 0, 108310, 270)
    SetChrFlags(0x9, 0x10)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xC, -54030, 0, 104830, 0)
    SetChrPos(0xD, -53850, 0, 106300, 180)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_558")
    SetChrFlags(0xC, 0x10)

    label("loc_558")

    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    Jump("loc_5E1")

    label("loc_567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5E1")
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, -51250, 500, 57180, 315)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x40)
    EndChrThread(0xA, 0x0)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xB, -53760, 0, 107910, 180)
    SetChrPos(0xD, -53850, 0, 106300, 0)
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D2")
    SetChrFlags(0xB, 0x10)

    label("loc_5D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E1")
    SetChrFlags(0xD, 0x10)

    label("loc_5E1")

    Return()

    # Function_2_277 end

    def Function_3_5E2(): pass

    label("Function_3_5E2")

    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_620")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_649")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)

    label("loc_649")

    Return()

    # Function_3_5E2 end

    def Function_4_64A(): pass

    label("Function_4_64A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_806")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_775")

    ChrTalk(
        0xFE,
        (
            "Cecil contacted us just now.\x01",
            "For now, she's safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But somehow,\x01",
            "it seems she's worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It might be because the hospital\x01",
            "suddenly became very busy, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have time, I'd like you\x01",
            "to stop by the hospital. \x01",
            "It seems she has a lot to talk about.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_801")

    label("loc_775")


    ChrTalk(
        0xFE,
        (
            "Somehow, it seems\x01",
            "Cecil's worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have time, I'd like you\x01",
            "to stop by the hospital. \x01",
            "It seems she has a lot to talk about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_801")

    Jump("loc_1F98")

    label("loc_806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABA")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "My, if it isn't Lloyd!\x01",
            "Where have you been?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's right, did you see Cecil?\x01",
            "I haven't seen her at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FA-Aunt, calm down.\x01",
            "...I'm happy to see you after a long time.\x02\x03",
            "#00000FSister Cecil is at the hospital now.\x01",
            "She seems she's doing fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, thank goodness...\x01",
            "You came back to us\x01",
            "Lloyd. I'm so relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's dangerous outside.\x01",
            "you should hide at my home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh, thanks but... There's\x01",
            "somewhere we need to go,\x01",
            "no matter what.\x02\x03",
            "#00000FPlease wait\x01",
            "here, aunt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Alright... I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, be careful, ok?\x01",
            "If anything happened\x01",
            "to you all, I'd...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, of course.\x01",
            "...See you later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BD, 7)
    Jump("loc_B33")

    label("loc_ABA")


    ChrTalk(
        0xFE,
        (
            "Thank goodness...\x01",
            "You've come back to us,\x01",
            "Lloyd. I'm so relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goddess of the Sky,\x01",
            "please...protect them...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B33")

    Jump("loc_1F98")

    label("loc_B38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B46")
    Jump("loc_1F98")

    label("loc_B46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C97")

    ChrTalk(
        0xFE,
        (
            "Yesterday, I tried to\x01",
            "call the hospital, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems Cecil and the\x01",
            "others are very busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...I bet.\x02\x03",
            "#00008FIt looks like a lot of\x01",
            "patients were hospitalized\x01",
            "due to that attack...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh*, I'm worried.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Cecil has a tendency to\x01",
            "work too hard... I hope\x01",
            "she doesn't hurt herself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D03")

    label("loc_C97")


    ChrTalk(
        0xFE,
        (
            "The hospital has gotten very\x01",
            "busy due to that attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if Cecil is\x01",
            "getting proper rest...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D03")

    Jump("loc_1F98")

    label("loc_D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_DAA")

    ChrTalk(
        0xFE,
        (
            "An occupation... The\x01",
            "people of Mainz must\x01",
            "fear for their lives...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard the CGF are having a tough\x01",
            "battle. I wonder what will happen...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F98")

    label("loc_DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_11B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_110C")

    ChrTalk(
        0xFE,
        (
            "Oh, come to think of it,\x01",
            "the Arc-en-ciel renewal\x01",
            "performance is tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But it seems tickets sold out\x01",
            "in the blink of an eye...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, just when did little\x01",
            "Ilya become so amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105F"L-Little" Ilya...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FCome to think of it, sister Cecil\x01",
            "and Miss Ilya are childhood\x01",
            "friends, aren't they.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, she stood out even back then.\x01",
            "She strangely got along with Cecil\x01",
            "and they often played together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She even punched a boy, who was\x01",
            "being mean to Cecil, with all\x01",
            "her might and made him cry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, that's very\x01",
            "like Miss Ilya, isn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FI feel bad for the\x01",
            "kiddo, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, when kids are mean,\x01",
            "it means they like their target...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FWell, because Miss Ilya hit him,\x01",
            "it must've made a precious\x01",
            "memory for him, in a way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FI-I wonder about that...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16C, 3)

    label("loc_110C")


    ChrTalk(
        0xFE,
        (
            "Uh uh, that's the same little\x01",
            "Ilya who's the superstar\x01",
            "leading Arc-en-ciel...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been proud of her ever since I\x01",
            "first met her, when she was just a kid.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F98")

    label("loc_11B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_124E")

    ChrTalk(
        0xFE,
        (
            "My, those just now...\x01",
            "Weren't those ambulances?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems like several passed by... Maybe\x01",
            "some kind of traffic accident occurred.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F98")

    label("loc_124E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_125C")
    Jump("loc_1F98")

    label("loc_125C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1409")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_137C")

    ChrTalk(
        0xFE,
        (
            "Crossbell State independence...\x01",
            "It seems a referendum will be\x01",
            "held on that question.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is a very difficult question.\x01",
            "I'll speak with my husband about it\x01",
            "and then decide my vote.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Which option is right? The answer\x01",
            "isn't so easy to come up with.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1404")

    label("loc_137C")


    ChrTalk(
        0xFE,
        (
            "I'll speak with my\x01",
            "husband about it before\x01",
            "deciding my vote.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Which option is right? The answer\x01",
            "isn't so easy to come up with.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1404")

    Jump("loc_1F98")

    label("loc_1409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_16FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1669")

    ChrTalk(
        0xFE,
        (
            "My, you're...\x01",
            "Tio, was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FHello. It's been awhile.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uh uh, I'm glad you're doing well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you get some time, let's\x01",
            "have dinner all together again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FMadam's cooking... *giggle*,\x01",
            "I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FYeah, your cooking has truly the "taste\x01",
            "of a mother"...it's really delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FWow, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FThat sounds good... \x01",
            "I'll look forward to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Your new members are\x01",
            "invited, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, I'll have\x01",
            "to do my best\x01",
            "for all of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThanks, aunt. I'll let\x01",
            "you know when we\x01",
            "have some time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 1)
    Jump("loc_16F5")

    label("loc_1669")


    ChrTalk(
        0xFE,
        (
            "With this, all members of the\x01",
            "Support Section are assembled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, if you get some time, I'd\x01",
            "love to treat all of you to dinner.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F5")

    Jump("loc_1F98")

    label("loc_16FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_178B")

    ChrTalk(
        0xFE,
        (
            "Oh, before I knew it, the\x01",
            "sky has become all dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My husband is coming back home so\x01",
            "I must hurry up and prepare dinner.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F98")

    label("loc_178B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1A04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1994")

    ChrTalk(
        0x101,
        (
            "#00000FAunt, I went to say hello\x01",
            "to sister Cecil yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, is that right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, I assume Cecil\x01",
            "was glad to see you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHa ha, yeah... It looked\x01",
            "like she was doing well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu, she was more lovely a woman\x01",
            "that I imagined. I was shocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FThat's right, she was\x01",
            "very open-minded...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FI know, right?\x01",
            "She's right in my\x01",
            "strike zone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FY-You... You'd deliver\x01",
            "that line even in\x01",
            "front of her mother?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FR-Really, seriously...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 0)

    label("loc_1994")


    ChrTalk(
        0xFE,
        (
            "Uh uh, it looks like\x01",
            "Cecil is very popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you like, please continue\x01",
            "to be friends with her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F98")

    label("loc_1A04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1B99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B57")

    ChrTalk(
        0xFE,
        (
            "When I went out shopping\x01",
            "today, I saw a number of\x01",
            "patrol officers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It really seems that the police\x01",
            "have gotten busier too, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThe Trade Conference starts tomorrow.\x01",
            "We too are to patrol the city while\x01",
            "completing support requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My, my...that must be\x01",
            "tough. But, please\x01",
            "do your best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B94")

    label("loc_1B57")


    ChrTalk(
        0xFE,
        (
            "You police must have\x01",
            "it tough, but please\x01",
            "do your best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B94")

    Jump("loc_1F98")

    label("loc_1B99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1D51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BB4")
    Call(0, 5)
    Jump("loc_1D4C")

    label("loc_1BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CAF")

    ChrTalk(
        0xFE,
        (
            "My husband works\x01",
            "as the city's\x01",
            "librarian, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's been friends with a certain\x01",
            "reporter for a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That person is very\x01",
            "knowledgeable and they talk\x01",
            "at length whenever they meet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uh uh, just like children.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D4C")

    label("loc_1CAF")


    ChrTalk(
        0xFE,
        (
            "My husband has been friends\x01",
            "with a certain reporter\x01",
            "for a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That person is very\x01",
            "knowledgeable and they talk\x01",
            "at length whenever they meet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D4C")

    Jump("loc_1F98")

    label("loc_1D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1F98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D6C")
    Call(0, 5)
    Jump("loc_1F98")

    label("loc_1D6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F34")

    ChrTalk(
        0xFE,
        (
            "By the way, Lloyd, have you\x01",
            "gotten in touch with Cecil yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, by orbal communication.\x01",
            "I'd like to go meet her in\x01",
            "person if I get the chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, you look manlier\x01",
            "since you got back. I think\x01",
            "Cecil will be surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FU-Uhh, I guess.\x01",
            "Ha ha ha...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00111F(Somehow he seems embarrassed.\x01",
            "...I wonder what he's thinking.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F(Hu hu, I'm getting more and\x01",
            "more interested in this Miss Cecil.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F98")

    label("loc_1F34")


    ChrTalk(
        0xFE,
        (
            "Lloyd, you look manlier\x01",
            "since you've gotten back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, I think Cecil\x01",
            "will be surprised.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F98")

    TalkEnd(0xFE)
    Return()

    # Function_4_64A end

    def Function_5_1F9C(): pass

    label("Function_5_1F9C")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "My, oh my...\x01",
            "If it isn't Lloyd!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FI'm back, aunt Leyte.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, thank goodness\x01",
            "you're all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like the Support Section's\x01",
            "with you. Is your training with\x01",
            "Section One already finished?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, just the other day.\x01",
            "Sorry if I haven't stopped\x01",
            "by in awhile, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FIs she the lady of the house?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah. She's been looking after\x01",
            "me ever since I was little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FShe's the mother of Miss Cecil,\x01",
            "who is always helping us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FSpeaking of Miss Cecil, \x01",
            "I met her before at the hospital...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAh, so you know\x01",
            "her too, Noｱl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHmm, am I the only\x01",
            "one left out here?\x02\x03",
            "#10302FIt seems her relationship with\x01",
            "you is somewhat unusual... \x01",
            "I'd love to hear all about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FD-Don't say\x01",
            "it's "unusual."\x02\x03",
            "#00000FWell, there'll be a chance to\x01",
            "see sister Cecil in the future,\x01",
            "so I'll introduce you at that time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, the Support Section\x01",
            "seems fun as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lloyd, please come\x01",
            "anytime if there's\x01",
            "anything troubling you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 5)
    Return()

    # Function_5_1F9C end

    def Function_6_23AF(): pass

    label("Function_6_23AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2508")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2491")

    ChrTalk(
        0xFE,
        (
            "My father has been depressed ever\x01",
            "since rail service stopped, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He immediately cheered up and\x01",
            "tried his hand at various things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good grief. Mechanical\x01",
            "enthusiasts never learn.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2503")

    label("loc_2491")


    ChrTalk(
        0xFE,
        (
            "Good grief. Mechanical\x01",
            "enthusiasts never learn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, I guess that's one\x01",
            "of my father's good points.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2503")

    Jump("loc_2FE5")

    label("loc_2508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2577")

    ChrTalk(
        0xFE,
        "I-I wonder what happened...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What are Miss Mariabell and\x01",
            "the President trying to do...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE5")

    label("loc_2577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_260D")

    ChrTalk(
        0xFE,
        (
            "My father went to the station early\x01",
            "this morning and seems very busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I wish he'd at least take\x01",
            "it easy when he's at home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE5")

    label("loc_260D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_26B8")

    ChrTalk(
        0xFE,
        (
            "In the incident the other day, \x01",
            "Arc-en-ciel's Miss Ilya\x01",
            "was seriously injured...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I won't get to see her\x01",
            "amazing performance. This sucks...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE5")

    label("loc_26B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_27E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2767")

    ChrTalk(
        0xFE,
        (
            "The Arc-en-ciel renewal\x01",
            "performance opens today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, my father seems\x01",
            "worried about something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder if something happened...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27E1")

    label("loc_2767")


    ChrTalk(
        0xFE,
        (
            "The opening day of an Arc-\x01",
            "en-ciel performance should\x01",
            "be an auspicious day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder if something happened...\x02",
    )

    CloseMessageWindow()

    label("loc_27E1")

    Jump("loc_2FE5")

    label("loc_27E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2872")

    ChrTalk(
        0xFE,
        (
            "My father has been busy ever\x01",
            "since yesterday dealing\x01",
            "with the derailment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll give him some\x01",
            "peace and quiet today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE5")

    label("loc_2872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_291E")

    ChrTalk(
        0xFE,
        (
            "After my father heard there was\x01",
            "a train accident, he flew\x01",
            "out of here in a hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard he went to the station,\x01",
            "but I wonder if he's all right...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE5")

    label("loc_291E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_29CF")

    ChrTalk(
        0xFE,
        (
            "That father of mine...he said he\x01",
            "wanted to go see how my\x01",
            "sister's doing today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Father doesn't get days off that often.\x01",
            "I wish he'd take it easy at home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE5")

    label("loc_29CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2A73")

    ChrTalk(
        0xFE,
        (
            "Whenever father gets back\x01",
            "from a business trip, he\x01",
            "jumps straight into bed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "C'mon. He'll get the sheets dirty\x01",
            "if he doesn't change clothes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE5")

    label("loc_2A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2B9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AFC")

    ChrTalk(
        0xFE,
        (
            "I'm reading a fashion magazine\x01",
            "with Miss Mariabell on the cover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Aww. I want to be just like her...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B9A")

    label("loc_2AFC")


    ChrTalk(
        0xFE,
        (
            "*sigh*, why is Miss Mariabell\x01",
            "so pretty? And intelligent too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say women like her are\x01",
            "gifted both with intelligence\x01",
            "and beauty. Must be nice...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B9A")

    Jump("loc_2FE5")

    label("loc_2B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2CE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C78")

    ChrTalk(
        0xFE,
        (
            "...Ah! There's a railway\x01",
            "book mixed in on the shelf\x01",
            "of my fashion magazines...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This must be my father's doing,\x01",
            "for sure. I wonder how many times\x01",
            "will he use the same tactics.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_2CDE")

    label("loc_2C78")


    ChrTalk(
        0xFE,
        (
            "Sometimes father does like this\x01",
            "to try to make me like the railway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Honestly, how impudent.\x02",
    )

    CloseMessageWindow()

    label("loc_2CDE")

    Jump("loc_2FE5")

    label("loc_2CE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2EB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E31")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0xFE,
        (
            "Everyone is a child. Just\x01",
            "seeing a big building like that\x01",
            "makes them say "Ahh! Ahh!"\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...W-Well, I guess it's\x01",
            "a little amazing, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rather than a building, it's\x01",
            "more fun looking at fashion\x01",
            "magazines, and more useful, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(You're not supposed\x01",
            "to compare those...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    OP_93(0xFE, 0x0, 0x0)
    Jump("loc_2EAC")

    label("loc_2E31")


    ChrTalk(
        0xFE,
        (
            "(*flipping pages*...) \x01",
            "Wow, the girl in this \x01",
            "photo is really pretty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I knew it, this\x01",
            "kind of waist\x01",
            "is better...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EAC")

    Jump("loc_2FE5")

    label("loc_2EB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2F44")

    ChrTalk(
        0xFE,
        (
            "Father is again away\x01",
            "on a month-long\x01",
            "business trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's a rail engineer, and it looks\x01",
            "like he's busy with various things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE5")

    label("loc_2F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2FDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F5F")
    Call(0, 7)
    Jump("loc_2FD7")

    label("loc_2F5F")


    ChrTalk(
        0xFE,
        (
            "I just want to be\x01",
            "as cool and smart\x01",
            "as Miss Mariabell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't want to be an engineer, \x01",
            "like my father wants.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FD7")

    Jump("loc_2FE5")

    label("loc_2FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2FE5")

    label("loc_2FE5")

    TalkEnd(0xFE)
    Return()

    # Function_6_23AF end

    def Function_7_2FE9(): pass

    label("Function_7_2FE9")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x9,
        (
            "Miss Mariabell leads the IBC\x01",
            "technology division and knows\x01",
            "a lot about orbal tech.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmm... Should I\x01",
            "study to become an\x01",
            "orbal engineer?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "P-Pinseeet! You're finally\x01",
            "taking interest in the\x01",
            "path of an engineer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Alright, now's the chance.\x01",
            "Won't you aim to be a rail\x01",
            "engineer like your father?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...I hate that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#4S*crushed*!#3S\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 2)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_7_2FE9 end

    def Function_8_3182(): pass

    label("Function_8_3182")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3344")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3298")

    ChrTalk(
        0xFE,
        (
            "My skills as a rail engineer are\x01",
            "useless with transcontinental rail\x01",
            "service suspended like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I can do something\x01",
            "regarding orbal bus and\x01",
            "car maintenance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Alright, I'll head over to the City\x01",
            "Meeting Hall and look for work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_333F")

    label("loc_3298")


    ChrTalk(
        0xFE,
        (
            "With my skills as a rail\x01",
            "engineer, I should be able to\x01",
            "help with car or bus maintenance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Alright, I'll head over to the City\x01",
            "Meeting Hall and look for work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_333F")

    Jump("loc_3AC1")

    label("loc_3344")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_33C6")

    ChrTalk(
        0xFE,
        (
            "Pinset, you mustn't go outside. \x01",
            "Stay here at home with your father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm sure your sister is all right...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AC1")

    label("loc_33C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3577")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34C7")

    ChrTalk(
        0xFE,
        (
            "I've gone to help out at Crossbell\x01",
            "Station this morning but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was crowded with foreigners\x01",
            "trying to return home, and the\x01",
            "situation was chaotic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll end my break earlier than\x01",
            "usual and return there to help out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3572")

    label("loc_34C7")


    ChrTalk(
        0xFE,
        (
            "The station was crowded with foreigners trying\x01",
            "to return home, and the situation was chaotic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll end my break earlier than\x01",
            "usual and return there to help out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3572")

    Jump("loc_3AC1")

    label("loc_3577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3585")
    Jump("loc_3AC1")

    label("loc_3585")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3605")

    ChrTalk(
        0xFE,
        (
            "How could this happen?\x01",
            "I can't believe Mainz was...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That armed group... \x01",
            "What could be their objective?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AC1")

    label("loc_3605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3629")

    ChrTalk(
        0xFE,
        "*snore snore*...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AC1")

    label("loc_3629")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3637")
    Jump("loc_3AC1")

    label("loc_3637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_37E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_373E")
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Since I have the chance, \x01",
            "I think I'll go see Wendy working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Pinset, I hope you'll study to become and\x01",
            "engineer too after seeing your sister working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Enough already!\x01",
            "I told you, I'm not\x01",
            "gonna be an engineer!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_37E0")

    label("loc_373E")


    ChrTalk(
        0xFE,
        (
            "Pinset, I hope you'll study to become and\x01",
            "engineer too after seeing your sister working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It will sure be useful for becoming\x01",
            "an engineer in the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37E0")

    Jump("loc_3AC1")

    label("loc_37E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3854")

    ChrTalk(
        0xFE,
        (
            "*mmm mmm*...\x01",
            "My own bed\x01",
            "is the best...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At this rate, I'm going\x01",
            "to sleep like a rock...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AC1")

    label("loc_3854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3862")
    Jump("loc_3AC1")

    label("loc_3862")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3870")
    Jump("loc_3AC1")

    label("loc_3870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_387E")
    Jump("loc_3AC1")

    label("loc_387E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_388C")
    Jump("loc_3AC1")

    label("loc_388C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3925")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38A7")
    Call(0, 7)
    Jump("loc_3920")

    label("loc_38A7")


    ChrTalk(
        0xFE,
        (
            "Hmm... Well,\x01",
            "no need to rush.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She inherited my blood,\x01",
            "so it's certain she'll be a\x01",
            "fine engineer in the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3920")

    Jump("loc_3AC1")

    label("loc_3925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3AC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A62")

    ChrTalk(
        0x101,
        (
            "#00005FAh, you're\x01",
            "Wendy's father...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYou look tired, somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*mmm mmm*... I just got back\x01",
            "from a business strip...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry Pinset, but you're going\x01",
            "to have to eat by yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F...Looks like you're half asleep.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F*giggle*, let's leave quietly.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3AC1")

    label("loc_3A62")


    ChrTalk(
        0xFE,
        (
            "...Huh? Where\x01",
            "did Pinset go...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh right, today she\x01",
            "has Sunday School...\x01",
            "*mmm mmm*...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AC1")

    TalkEnd(0xFE)
    Return()

    # Function_8_3182 end

    def Function_9_3AC5(): pass

    label("Function_9_3AC5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3C83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BDD")

    ChrTalk(
        0xFE,
        (
            "That Ryｹ, somehow he intends to go around\x01",
            "helping the neighborhood just with the kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was planning on teaching him\x01",
            "how to be a merchant. Hmm,\x01",
            "a tactical retreat, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I suppose he can't calm\x01",
            "down if he doesn't anything.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3C7E")

    label("loc_3BDD")


    ChrTalk(
        0xFE,
        (
            "Leaving Ryｹ aside... Being how she is,\x01",
            "Chiruru has resumed traveling again.\x01",
            "This time she went to Tangram Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good grief. Are my\x01",
            "children ever home?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C7E")

    Jump("loc_4902")

    label("loc_3C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3D37")

    ChrTalk(
        0xFE,
        (
            "My children are at home and I can \x01",
            "have some piece of mind for now, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried about things are outside.\x01",
            "What kind of situation we're in, I wonder.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4902")

    label("loc_3D37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3E79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E0A")

    ChrTalk(
        0xFE,
        (
            "I seems like something terrible\x01",
            "is happening to Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Anyway, I can relax\x01",
            "because Chiruru's home safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's times like these when a\x01",
            "family should be together.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3E74")

    label("loc_3E0A")


    ChrTalk(
        0xFE,
        (
            "I seems like something terrible\x01",
            "is happening to Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to be ready\x01",
            "for anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E74")

    Jump("loc_4902")

    label("loc_3E79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3F02")

    ChrTalk(
        0xFE,
        (
            "That incident was serious...\x01",
            "I hope IBC resumes \x01",
            "business before long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Banks are very important\x01",
            "to us merchants.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4902")

    label("loc_3F02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3F81")

    ChrTalk(
        0xFE,
        (
            "I didn't think anything\x01",
            "like this could happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Chiruru left on a trip. I wonder if she's all right...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4902")

    label("loc_3F81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4082")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_402B")

    ChrTalk(
        0xFE,
        (
            "I was a naughty child once,\x01",
            "and would always run around\x01",
            "barefoot in the rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In that sense, Ryｹis similar to how\x01",
            "I was as a child.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_407D")

    label("loc_402B")


    ChrTalk(
        0xFE,
        (
            "Ryｹ is like how\x01",
            "I was as a child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That must be why\x01",
            "he's such a handful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_407D")

    Jump("loc_4902")

    label("loc_4082")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_40C3")

    ChrTalk(
        0xFE,
        (
            "Hmm, did I hear\x01",
            "the sound of \x01",
            "loud sirens...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4902")

    label("loc_40C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_41EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4181")

    ChrTalk(
        0xFE,
        (
            "My daughter Chiruru\x01",
            "is back from her trip. \x01",
            "She's now out with a friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Both Ryｹ and\x01",
            "Chiruru are blessed\x01",
            "with good friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm thankful\x01",
            "for that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_41E9")

    label("loc_4181")


    ChrTalk(
        0xFE,
        (
            "Chiruru is hardly ever at\x01",
            "home. She likes to spend\x01",
            "time with Katerina.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm thankful\x01",
            "for that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41E9")

    Jump("loc_4902")

    label("loc_41EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_428C")

    ChrTalk(
        0xFE,
        (
            "I was thinking of\x01",
            "having Ryｹ help me\x01",
            "with work today, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before I knew it, he left.\x01",
            "That little devil is quite\x01",
            "the escape artist.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4902")

    label("loc_428C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4312")

    ChrTalk(
        0xFE,
        (
            "Today too, Ryｹ and\x01",
            "the others went out\x01",
            "to see Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They saw it yesterday but\x01",
            "never gets tired of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4902")

    label("loc_4312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_443F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43C2")

    ChrTalk(
        0xFE,
        (
            "One day I'd like to have Ryｹ inherit\x01",
            "the wholesale store job, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When it comes to that\x01",
            "guy, he thinks nothing\x01",
            "but to play. Boy oh boy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_443A")

    label("loc_43C2")


    ChrTalk(
        0xFE,
        (
            "Ryｹ's results at Sunday School\x01",
            "too are no good at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He shouldn't be only playing\x01",
            "but study a little too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_443A")

    Jump("loc_4902")

    label("loc_443F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_45B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4534")

    ChrTalk(
        0xFE,
        (
            "For three years I've run a\x01",
            "wholesale business in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the inauguration ceremony,\x01",
            "I've ordered a lot of goods\x01",
            "from the department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I always knew Crossbell was\x01",
            "a good place to do business.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_45B2")

    label("loc_4534")


    ChrTalk(
        0xFE,
        (
            "For the inauguration ceremony,\x01",
            "I've ordered a lot of goods\x01",
            "from the department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Mwoh oh, business is roaring.\x02",
    )

    CloseMessageWindow()

    label("loc_45B2")

    Jump("loc_4902")

    label("loc_45B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_46FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4666")

    ChrTalk(
        0xFE,
        (
            "That Ryｹ has been inviting\x01",
            "Mr. Tallys' little Momo to play\x01",
            "with him more often lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope he's not teaching\x01",
            "her anything dangerous...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_46F6")

    label("loc_4666")


    ChrTalk(
        0xFE,
        (
            "If he taught little Momo something\x01",
            "dangerous, I'd never be able to\x01",
            "apologize enough to her parents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder if Ryｹis being careful.\x02",
    )

    CloseMessageWindow()

    label("loc_46F6")

    Jump("loc_4902")

    label("loc_46FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4883")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47F6")

    ChrTalk(
        0xFE,
        (
            "Chiruru will probably\x01",
            "leave on a trip at once...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "While my family's all here,\x01",
            "I think I'll make some of my\x01",
            "special fried rice for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm originally from the Republic.\x01",
            "I'm very familiar with Eastern cuisine.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_487E")

    label("loc_47F6")


    ChrTalk(
        0xFE,
        (
            "I'm originally from the Republic.\x01",
            "I'm very familiar with Eastern cuisine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, the only thing I can\x01",
            "make well is fried rice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_487E")

    Jump("loc_4902")

    label("loc_4883")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4902")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_489E")
    Call(0, 10)
    Jump("loc_4902")

    label("loc_489E")


    ChrTalk(
        0xFE,
        (
            "Good grief... No matter what\x01",
            "trouble she gets into, I never get\x01",
            "the sense that she's learning.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4902")

    TalkEnd(0xFE)
    Return()

    # Function_9_3AC5 end

    def Function_10_4906(): pass

    label("Function_10_4906")

    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xB,
        (
            "Oh Chiruru, you're back.\x01",
            "Your trip was quite long this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I think you said you were walking\x01",
            "the Mainz mountains on foot\x01",
            "or something crazy like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yeah... I had a little\x01",
            "accident on the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "*sigh*, looks like I'm not ready for it yet.\x01",
            "I'll try again if there's another chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "You never learn...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_10_4906 end

    def Function_11_4A6F(): pass

    label("Function_11_4A6F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4A80")
    Jump("loc_4B95")

    label("loc_4A80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4B18")

    ChrTalk(
        0xFE,
        (
            "Martial law is so boring, so we\x01",
            "secretly went out to play. But\x01",
            "when we did, it became like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh*, I don't get it at all!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B95")

    label("loc_4B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4B95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B33")
    Call(0, 12)
    Jump("loc_4B95")

    label("loc_4B33")


    ChrTalk(
        0xFE,
        (
            "My sis is somehow\x01",
            "a little weird...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I often see her going into\x01",
            "weird places by herself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B95")

    TalkEnd(0xFE)
    Return()

    # Function_11_4A6F end

    def Function_12_4B99(): pass

    label("Function_12_4B99")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xC,
        (
            "Hey, sis. Where're\x01",
            "you travelling next?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmm... For now, I'm\x01",
            "planning on taking\x01",
            "a walk in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "There's still a lot of\x01",
            "places I haven't been to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Wow. You sure\x01",
            "are a weirdo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I often see you going into\x01",
            "weird places by yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "...You're one to talk.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xC, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_12_4B99 end

    def Function_13_4CCF(): pass

    label("Function_13_4CCF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4CE0")
    Jump("loc_5091")

    label("loc_4CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4DE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DAA")
    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xFE,
        (
            "I'm getting annoyed, not being\x01",
            "able to leave the city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Hmph. To bed, then.\x01",
            "Wake me up when it's over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hey, this is no time to be sleeping!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 5)
    Jump("loc_4DE0")

    label("loc_4DAA")


    ChrTalk(
        0xFE,
        (
            "Wake me up when this is over. \x01",
            "I'm going to bed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DE0")

    Jump("loc_5091")

    label("loc_4DE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4F10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E91")

    ChrTalk(
        0xFE,
        (
            "I feel like strange things have been\x01",
            "happening all over Crossbell lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe it's best to refrain from\x01",
            "going on trips for awhile...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4F0B")

    label("loc_4E91")


    ChrTalk(
        0xFE,
        (
            "Maybe it's best to refrain from\x01",
            "going on trips for awhile...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I can't do anything else, \x01",
            "so I'm going to bed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F0B")

    Jump("loc_5091")

    label("loc_4F10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4F1E")
    Jump("loc_5091")

    label("loc_4F1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4FF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F39")
    Call(0, 12)
    Jump("loc_4FEB")

    label("loc_4F39")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xFE,
        (
            "You're one to talk. Before, you\x01",
            "snuck into the Geofront, and when they\x01",
            "rescued you, you came back crying.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xC)

    ChrTalk(
        0xC,
        "Wha... I did NOT cry!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)

    label("loc_4FEB")

    Jump("loc_5091")

    label("loc_4FF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5091")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_500B")
    Call(0, 10)
    Jump("loc_5091")

    label("loc_500B")


    ChrTalk(
        0xFE,
        (
            "Traveling the Mainz mountains\x01",
            "on foot was too hard for me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The next time I challenge them,\x01",
            "I'm going to succeed for sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5091")

    TalkEnd(0xFE)
    Return()

    # Function_13_4CCF end

    SaveToFile()

Try(main)

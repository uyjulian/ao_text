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
        "Function_5_1E89",         # 05, 5
        "Function_6_228B",         # 06, 6
        "Function_7_2E6C",         # 07, 7
        "Function_8_2FF7",         # 08, 8
        "Function_9_3903",         # 09, 9
        "Function_10_46EA",        # 0A, 10
        "Function_11_4853",        # 0B, 11
        "Function_12_4976",        # 0C, 12
        "Function_13_4AA7",        # 0D, 13
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_767")

    ChrTalk(
        0xFE,
        (
            "Cecil contacted us just\x01",
            "now. For now, she's\x01",
            "safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But she seems worried\x01",
            "for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It might be because the\x01",
            "hospital suddenly became\x01",
            "very busy, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I have time, I'd like to\x01",
            "stop by the hospital. We\x01",
            "have a lot to talk about.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7E3")

    label("loc_767")


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
            "If I have time, I'd like to\x01",
            "stop by the hospital. We\x01",
            "have a lot to talk about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E3")

    Jump("loc_1E85")

    label("loc_7E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_AEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A70")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Wow, if it isn't Lloyd!\x01",
            "Where have you been?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's right, have you\x01",
            "seen Cecil? I haven't\x01",
            "seen her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FC-Calm down Aunt Leyte,\x01",
            "you can relax.\x02\x03",
            "#00000FCecil's at the hospital.\x01",
            "She seems fine.\x02",
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
            "Hide here with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FThanks for the offer but...\x01",
            "There's somewhere we need\x01",
            "to go, no matter what.\x02\x03",
            "#00000FPlease wait here, Aunt\x01",
            "Leyte.\x02",
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
            "But, be careful, ok? If\x01",
            "anything happened to you\x01",
            "all, I'd...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, of course. ...See\x01",
            "you later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BD, 7)
    Jump("loc_AEA")

    label("loc_A70")


    ChrTalk(
        0xFE,
        (
            "Thank goodness... You've\x01",
            "come back to us, Lloyd.\x01",
            "I'm so relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goddess of the Sky,\x01",
            "please... protect\x01",
            "them...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AEA")

    Jump("loc_1E85")

    label("loc_AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_AFD")
    Jump("loc_1E85")

    label("loc_AFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C50")

    ChrTalk(
        0xFE,
        (
            "Yesterday, a call came\x01",
            "in from the hospital,\x01",
            "but...\x02",
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
            "due to that attack.\x02",
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
    Jump("loc_CBC")

    label("loc_C50")


    ChrTalk(
        0xFE,
        (
            "The hospital has gotten\x01",
            "very busy due to that\x01",
            "attack.\x02",
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

    label("loc_CBC")

    Jump("loc_1E85")

    label("loc_CC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D63")

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
            "I heard the CGF are having\x01",
            "a tough battle. I wonder\x01",
            "what will happen...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E85")

    label("loc_D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1139")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1097")

    ChrTalk(
        0xFE,
        (
            "Oh, come to think of it,\x01",
            "the Arc-en-Ciel renewal\x01",
            "performance is tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But it seems tickets\x01",
            "sold out in the blink of\x01",
            "an eye...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, just when did\x01",
            "Ilya-chan become so\x01",
            "amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FI-Ilya "chan"?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FCome to think of it, Ilya\x01",
            "and Cecil were childhood\x01",
            "friends, weren't they.\x02",
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
            "She punched a guy who was\x01",
            "being mean to Cecil with all\x01",
            "her might and made him cry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHaha, that's very like\x01",
            "Ilya, isn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FI feel bad for the guy,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHaha, because when kids\x01",
            "are mean, it means they\x01",
            "like their target.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FWell, because Ilya hit\x01",
            "him, it must've made a\x01",
            "precious memory for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FI-I wonder about that...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16C, 3)

    label("loc_1097")


    ChrTalk(
        0xFE,
        (
            "Haha, that's the same\x01",
            "Ilya that's the superstar\x01",
            "leading Arc-en-Ciel...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been proud of her ever\x01",
            "since I first met her, when\x01",
            "she was just a kid.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E85")

    label("loc_1139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_11D1")

    ChrTalk(
        0xFE,
        (
            "My, that just now...\x01",
            "Wasn't that an\x01",
            "ambulance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems like several passed\x01",
            "by... Maybe some kind of\x01",
            "traffic accident occurred.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E85")

    label("loc_11D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_11DF")
    Jump("loc_1E85")

    label("loc_11DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_138B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12FF")

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
            "I'll speak with my husband about\x01",
            "it and then decide my vote.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Which option is right?\x01",
            "The answer isn't so easy\x01",
            "to come up with.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1386")

    label("loc_12FF")


    ChrTalk(
        0xFE,
        (
            "I'll speak with my\x01",
            "father about it before\x01",
            "deciding my vote.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Which option is right?\x01",
            "The answer isn't so easy\x01",
            "to come up with.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1386")

    Jump("loc_1E85")

    label("loc_138B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_163F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15AF")

    ChrTalk(
        0xFE,
        (
            "My, that's... Tio, was\x01",
            "it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FHello. It's been a\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I'm glad you're\x01",
            "doing well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you get some time,\x01",
            "let's have dinner\x01",
            "together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FYour cooking... I'm\x01",
            "looking forward to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FYeah, your home\x01",
            "cooking's delicious~.\x02",
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
            "#10109FThat sounds good... I'll\x01",
            "look forward to it.\x02",
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
            "Haha, I'll have to do my\x01",
            "best for all of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThanks Aunt Leyte. I'll\x01",
            "let you know when we\x01",
            "have some time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 1)
    Jump("loc_163A")

    label("loc_15AF")


    ChrTalk(
        0xFE,
        (
            "With this, all members\x01",
            "of the Support Section\x01",
            "are assembled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, if you get some\x01",
            "time, I'd love to treat\x01",
            "all of you to dinner.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_163A")

    Jump("loc_1E85")

    label("loc_163F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_16C9")

    ChrTalk(
        0xFE,
        (
            "Oh, before I knew it,\x01",
            "the sky has become all\x01",
            "dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My husband is coming\x01",
            "home, so I must hurry\x01",
            "and prepare dinner.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E85")

    label("loc_16C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1925")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18B6")

    ChrTalk(
        0x101,
        (
            "#00000FAunt Leyte, I saw Cecil\x01",
            "yesterday.\x02",
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
            "Haha, I assume Cecil was\x01",
            "glad to see you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHaha, yeah... It looked\x01",
            "like she was doing well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHehe, she was more\x01",
            "beautiful than I\x01",
            "imagined. I was shocked.\x02",
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
            "#00309FI know, right? She's\x01",
            "right in my strike zone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FY-You... You'd deliver\x01",
            "that line even in front\x01",
            "of her mother?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FI mean, seriously...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 0)

    label("loc_18B6")


    ChrTalk(
        0xFE,
        (
            "Haha, it looks like\x01",
            "Cecil is very popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you like, please\x01",
            "continue to be friends\x01",
            "with her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E85")

    label("loc_1925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1AB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A76")

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
            "The police have gotten\x01",
            "busier lately, haven't\x01",
            "they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThe trade conference starts tomorrow.\x01",
            "On our end, we're to patrol the city\x01",
            "while completing support requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My, my, that must be\x01",
            "tough. But, please do\x01",
            "your best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AB3")

    label("loc_1A76")


    ChrTalk(
        0xFE,
        (
            "You police must have it\x01",
            "tough, but please do\x01",
            "your best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AB3")

    Jump("loc_1E85")

    label("loc_1AB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1C67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AD3")
    Call(0, 5)
    Jump("loc_1C62")

    label("loc_1AD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC9")

    ChrTalk(
        0xFE,
        (
            "My dad works as the\x01",
            "city's librarian, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's been friends with a\x01",
            "certain reporter for a\x01",
            "long time.\x02",
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
        (
            "Haha, just like\x01",
            "children.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C62")

    label("loc_1BC9")


    ChrTalk(
        0xFE,
        (
            "My dad has been friends\x01",
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

    label("loc_1C62")

    Jump("loc_1E85")

    label("loc_1C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1E85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C82")
    Call(0, 5)
    Jump("loc_1E85")

    label("loc_1C82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E21")

    ChrTalk(
        0xFE,
        (
            "By the way, Lloyd, have\x01",
            "you gotten in touch with\x01",
            "Cecil?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, by orbal communication.\x01",
            "I'd like to go there if I get\x01",
            "the chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, you seem stronger\x01",
            "since you got back. I think\x01",
            "Cecil will be surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FU-Uhh, I guess.\x01",
            "Hahaha...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00111F(He seems embarrassed. I\x01",
            "wonder what he's\x01",
            "thinking.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F(Haha, I'm getting more\x01",
            "and more interested in\x01",
            "Cecil.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E85")

    label("loc_1E21")


    ChrTalk(
        0xFE,
        (
            "Lloyd, you seem stronger\x01",
            "since you've gotten\x01",
            "back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I think Cecil will\x01",
            "be surprised.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E85")

    TalkEnd(0xFE)
    Return()

    # Function_4_64A end

    def Function_5_1E89(): pass

    label("Function_5_1E89")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "My oh my... If it isn't\x01",
            "Lloyd!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FI'm back, Leyte.\x02",
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
            "#00000FYeah, it finished just the\x01",
            "other day. Sorry if I haven't\x01",
            "stopped by in a while, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FIs she the lady of the\x01",
            "house?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah. She's been looking\x01",
            "after me ever since I\x01",
            "was little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FShe's the mother of\x01",
            "Cecil, who is always\x01",
            "helping us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FSpeaking of Cecil, I met\x01",
            "her before at the\x01",
            "hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAh, so you know her too,\x01",
            "Noｱl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHmm, am I the only one left out\x01",
            "here?\x02\x03",
            "#10302FIt seems her relationship with\x01",
            "you is somewhat unusual... I've\x01",
            "love to hear all about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FD-Don't call it "unusual".\x02\x03",
            "#00000FWell, there'll be a chance to\x01",
            "see Cecil in the future. I'll\x01",
            "introduce you at that time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, the Support\x01",
            "Section seems fun as\x01",
            "always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lloyd, please come\x01",
            "anytime if there's\x01",
            "something troubling you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 5)
    Return()

    # Function_5_1E89 end

    def Function_6_228B(): pass

    label("Function_6_228B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_23E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2375")

    ChrTalk(
        0xFE,
        (
            "My dad has been depressed\x01",
            "ever since rail service\x01",
            "stopped, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He had a change of heart\x01",
            "and has been trying his\x01",
            "hand at different things.\x02",
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
    Jump("loc_23E4")

    label("loc_2375")


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
            "...Well, I guess that's\x01",
            "one of my dad's good\x01",
            "points.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23E4")

    Jump("loc_2E68")

    label("loc_23E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2450")

    ChrTalk(
        0xFE,
        (
            "I-I wonder what\x01",
            "happened...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What are Mariabell and\x01",
            "the President trying to\x01",
            "do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E68")

    label("loc_2450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_24E0")

    ChrTalk(
        0xFE,
        (
            "My dad went to the station\x01",
            "early this morning and\x01",
            "seems very busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish he'd at least\x01",
            "take it easy when he's\x01",
            "at home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E68")

    label("loc_24E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2584")

    ChrTalk(
        0xFE,
        (
            "In the incident the other\x01",
            "days, Arc-en-Ciel's Ilya\x01",
            "was seriously injured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I won't get to see\x01",
            "her amazing performance.\x01",
            "This sucks...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E68")

    label("loc_2584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_26AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2630")

    ChrTalk(
        0xFE,
        (
            "The Arc-en-Ciel renewal\x01",
            "performance opens today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, my dad seems\x01",
            "worried about something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if something\x01",
            "happened...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26A6")

    label("loc_2630")


    ChrTalk(
        0xFE,
        (
            "Opening day of an Arc-en-\x01",
            "Ciel performance should\x01",
            "be an auspicious day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if something\x01",
            "happened...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26A6")

    Jump("loc_2E68")

    label("loc_26AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2734")

    ChrTalk(
        0xFE,
        (
            "My dad has been busy ever\x01",
            "since yesterday dealing\x01",
            "with the derailment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll give him some peace\x01",
            "and quiet today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E68")

    label("loc_2734")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_27DD")

    ChrTalk(
        0xFE,
        (
            "After my dad heard there was\x01",
            "a train accident, he flew\x01",
            "out of here in a hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard he went to the\x01",
            "station, but I wonder if\x01",
            "he's all right...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E68")

    label("loc_27DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_287C")

    ChrTalk(
        0xFE,
        (
            "Dad! You said you wanted\x01",
            "to go see how my\x01",
            "sister's doing today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dad doesn't get days off\x01",
            "that often. I wish he'd\x01",
            "take it easy at home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E68")

    label("loc_287C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_291D")

    ChrTalk(
        0xFE,
        (
            "Whenever dad gets back\x01",
            "from a business trip, he\x01",
            "jumps straight into bed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "C'mon. He'll get the\x01",
            "sheets dirty if he\x01",
            "doesn't change clothes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E68")

    label("loc_291D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2A37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29A1")

    ChrTalk(
        0xFE,
        (
            "I'm reading a fashion\x01",
            "magazine with Mariabell\x01",
            "on the cover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aww. I want to be just\x01",
            "like her...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A32")

    label("loc_29A1")


    ChrTalk(
        0xFE,
        (
            "*sigh*, why is Mariabell\x01",
            "so pretty? Her face is\x01",
            "pretty too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say women like her\x01",
            "have both intelligence and\x01",
            "beauty. Must be nice...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A32")

    Jump("loc_2E68")

    label("loc_2A37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2B7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B08")

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
            "This is my father's doing for\x01",
            "sure. I wonder how many times\x01",
            "he'll use the same tactics.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_2B78")

    label("loc_2B08")


    ChrTalk(
        0xFE,
        (
            "My father does things like\x01",
            "this sometimes to try to\x01",
            "make me like the railway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Honestly, how impudent.\x02",
    )

    CloseMessageWindow()

    label("loc_2B78")

    Jump("loc_2E68")

    label("loc_2B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2D44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CC9")
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
            "magazine, and more useful, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(You're not supposed to\x01",
            "compare them...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    OP_93(0xFE, 0x0, 0x0)
    Jump("loc_2D3F")

    label("loc_2CC9")


    ChrTalk(
        0xFE,
        (
            "(*flipping pages*) Wow,\x01",
            "the girl in this photo\x01",
            "is really pretty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I knew it, this kind of\x01",
            "waist is better...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D3F")

    Jump("loc_2E68")

    label("loc_2D44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2DCF")

    ChrTalk(
        0xFE,
        (
            "Dad is away on a month-\x01",
            "long business trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's a rail engineer, and\x01",
            "it looks like he's busy\x01",
            "with various things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E68")

    label("loc_2DCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2E5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DEA")
    Call(0, 7)
    Jump("loc_2E5A")

    label("loc_2DEA")


    ChrTalk(
        0xFE,
        (
            "I just want to be as\x01",
            "cool and smart are\x01",
            "Mariabell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't want to be an\x01",
            "engineer, like my dad\x01",
            "wants.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E5A")

    Jump("loc_2E68")

    label("loc_2E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2E68")

    label("loc_2E68")

    TalkEnd(0xFE)
    Return()

    # Function_6_228B end

    def Function_7_2E6C(): pass

    label("Function_7_2E6C")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x9,
        (
            "Mariabell leads the IBC\x01",
            "Technology Division and knows\x01",
            "a lot about orbal tech.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmm... Should I study to\x01",
            "become an orbal\x01",
            "engineer?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "P-Pinset! You're finally\x01",
            "taking interest in the\x01",
            "path of an engineer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Alright, now's the time.\x01",
            "Why not try being a rail\x01",
            "engineer like your dad?\x02",
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

    # Function_7_2E6C end

    def Function_8_2FF7(): pass

    label("Function_8_2FF7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_31B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_310D")

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
            "Alright, I'll head over\x01",
            "to the City Meeting Hall\x01",
            "and look for work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_31B4")

    label("loc_310D")


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
            "Alright, I'll head over\x01",
            "to the City Meeting Hall\x01",
            "and look for work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31B4")

    Jump("loc_38FF")

    label("loc_31B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_323A")

    ChrTalk(
        0xFE,
        (
            "Pinset, you mustn't go\x01",
            "outside. Stay here at\x01",
            "home with your father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure your sister is\x01",
            "all right...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38FF")

    label("loc_323A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_33EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_333B")

    ChrTalk(
        0xFE,
        (
            "I've went to help out at\x01",
            "Crossbell Station this\x01",
            "morning but...\x02",
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
            "I'll end my break earlier\x01",
            "than usual and return\x01",
            "there to help out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33E6")

    label("loc_333B")


    ChrTalk(
        0xFE,
        (
            "The station was crowded with\x01",
            "foreigners trying to return home,\x01",
            "and the situation was chaotic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll end my break earlier\x01",
            "than usual and return\x01",
            "there to help out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33E6")

    Jump("loc_38FF")

    label("loc_33EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_33F9")
    Jump("loc_38FF")

    label("loc_33F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3478")

    ChrTalk(
        0xFE,
        (
            "How could this happen? I\x01",
            "can't believe Mainz\x01",
            "was...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That armed group... What\x01",
            "could be their\x01",
            "objective?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38FF")

    label("loc_3478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3497")

    ChrTalk(
        0xFE,
        "Ugh, ugh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_38FF")

    label("loc_3497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_34A5")
    Jump("loc_38FF")

    label("loc_34A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_362A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_359D")
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Since I have the chance,\x01",
            "I think I'll go see\x01",
            "Wendy working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope Pinset wants to\x01",
            "become an engineer after\x01",
            "seeing her sister working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Enough already! I told\x01",
            "you, I'm not gonna be an\x01",
            "engineer!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_3625")

    label("loc_359D")


    ChrTalk(
        0xFE,
        (
            "I hope Pinset wants to\x01",
            "become an engineer after\x01",
            "seeing her sister working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the future, I want to\x01",
            "be of use as an\x01",
            "engineer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3625")

    Jump("loc_38FF")

    label("loc_362A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3698")

    ChrTalk(
        0xFE,
        (
            "*mumble*... My own bed\x01",
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
    Jump("loc_38FF")

    label("loc_3698")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_36A6")
    Jump("loc_38FF")

    label("loc_36A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_36B4")
    Jump("loc_38FF")

    label("loc_36B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_36C2")
    Jump("loc_38FF")

    label("loc_36C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_36D0")
    Jump("loc_38FF")

    label("loc_36D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3765")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36EB")
    Call(0, 7)
    Jump("loc_3760")

    label("loc_36EB")


    ChrTalk(
        0xFE,
        (
            "Hmm... Well, no need to\x01",
            "rush.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I had my blood drawn, so\x01",
            "it's certain I'll be a fine\x01",
            "engineer in the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3760")

    Jump("loc_38FF")

    label("loc_3765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_38FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38A1")

    ChrTalk(
        0x101,
        (
            "#00005FAh, you're Wendy's\x01",
            "father...\x02",
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
            "*mumble*... I just got\x01",
            "back from a business\x01",
            "strip...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry Pinset, but you're\x01",
            "going to have to eat by\x01",
            "yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F...Looks like you're\x01",
            "half asleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHaha, you should take it\x01",
            "easy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_38FF")

    label("loc_38A1")


    ChrTalk(
        0xFE,
        (
            "...Huh? Where did Pinset\x01",
            "go...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh right, she has Sunday\x01",
            "School today...\x01",
            "*mumble*...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38FF")

    TalkEnd(0xFE)
    Return()

    # Function_8_2FF7 end

    def Function_9_3903(): pass

    label("Function_9_3903")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3ABB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A11")

    ChrTalk(
        0xFE,
        (
            "That Ryｹ. He's planning on\x01",
            "taking just kids to help\x01",
            "out in the neighborhood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was planning on teaching him\x01",
            "how to be a merchant. Hmm. A\x01",
            "tactical retreat, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I suppose he can't\x01",
            "calm down if he doesn't\x01",
            "anything.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3AB6")

    label("loc_3A11")


    ChrTalk(
        0xFE,
        (
            "I suppose Ryｹ is fine... Chiruru being\x01",
            "who she is, she resumed traveling again.\x01",
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

    label("loc_3AB6")

    Jump("loc_46E6")

    label("loc_3ABB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3B55")

    ChrTalk(
        0xFE,
        (
            "If my children were home\x01",
            "I could relax, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried about the situation\x01",
            "outside. What kind of situation\x01",
            "is this, I wonder.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46E6")

    label("loc_3B55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3C96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C29")

    ChrTalk(
        0xFE,
        (
            "I seems like something\x01",
            "terrible is happening to\x01",
            "Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Anyway, I can relax\x01",
            "because Chiruru's home\x01",
            "safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's in times like these\x01",
            "that a family should be\x01",
            "together.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3C91")

    label("loc_3C29")


    ChrTalk(
        0xFE,
        (
            "I seems like something\x01",
            "terrible is happening to\x01",
            "Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to prepare for\x01",
            "the worst.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C91")

    Jump("loc_46E6")

    label("loc_3C96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3D1E")

    ChrTalk(
        0xFE,
        (
            "That incident was serious...\x01",
            "I hope IBC resumes business\x01",
            "before long.\x02",
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
    Jump("loc_46E6")

    label("loc_3D1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3D9D")

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
        (
            "Chiruru left on a trip.\x01",
            "I wonder if she's all\x01",
            "right...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46E6")

    label("loc_3D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3E9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E47")

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
            "In that sense, Ryｹ is\x01",
            "similar to how I was as\x01",
            "a child.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3E99")

    label("loc_3E47")


    ChrTalk(
        0xFE,
        (
            "Ryｹ is like how I was as\x01",
            "a child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That must be why he's\x01",
            "such a handful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E99")

    Jump("loc_46E6")

    label("loc_3E9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3EDC")

    ChrTalk(
        0xFE,
        (
            "Hmm, did I hear the\x01",
            "sound of a loud siren?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46E6")

    label("loc_3EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4005")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F98")

    ChrTalk(
        0xFE,
        (
            "My daughter Chiruru is\x01",
            "back from her trip. She's\x01",
            "now out with friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Both Ryｹ and Chiruru are\x01",
            "blessed with good\x01",
            "friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm thankful for that.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4000")

    label("loc_3F98")


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
        "I'm thankful for that.\x02",
    )

    CloseMessageWindow()

    label("loc_4000")

    Jump("loc_46E6")

    label("loc_4005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_40A3")

    ChrTalk(
        0xFE,
        (
            "I was thinking of having\x01",
            "Ryｹ help me with work\x01",
            "today, but...\x02",
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
    Jump("loc_46E6")

    label("loc_40A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4119")

    ChrTalk(
        0xFE,
        (
            "I'm going to see Orchis\x01",
            "tower with Ryｹ today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He saw it yesterday but\x01",
            "never gets tired of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46E6")

    label("loc_4119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4239")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41C9")

    ChrTalk(
        0xFE,
        (
            "One day I'd like to have\x01",
            "Ryｹ inherit the wholesale\x01",
            "store job, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When it comes to that\x01",
            "boy, he thinks of nothing\x01",
            "but play. Boy oh boy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4234")

    label("loc_41C9")


    ChrTalk(
        0xFE,
        (
            "Ryｹ's Sunday School\x01",
            "grades are no good\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He shouldn't just play,\x01",
            "but study a little\x01",
            "too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4234")

    Jump("loc_46E6")

    label("loc_4239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_43AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_432B")

    ChrTalk(
        0xFE,
        (
            "For three years I've run\x01",
            "a wholesale business in\x01",
            "Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the unveiling ceremony,\x01",
            "I've ordered a lot of goods\x01",
            "from the department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I always knew Crossbell\x01",
            "was a good place to do\x01",
            "business.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_43A7")

    label("loc_432B")


    ChrTalk(
        0xFE,
        (
            "For the unveiling ceremony,\x01",
            "I've ordered a lot of goods\x01",
            "from the department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Muhoho, I've profited\x01",
            "greatly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43A7")

    Jump("loc_46E6")

    label("loc_43AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_44D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4450")

    ChrTalk(
        0xFE,
        (
            "That Ryｹ has been inviting\x01",
            "Tallys' Momo to play with\x01",
            "him more often lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope he's not teaching\x01",
            "her anything\x01",
            "dangerous...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_44CD")

    label("loc_4450")


    ChrTalk(
        0xFE,
        (
            "If he taught Momo something\x01",
            "dangerous, I'd never hear\x01",
            "the end of it from Tallys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if Ryｹ is being\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44CD")

    Jump("loc_46E6")

    label("loc_44D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4667")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45DA")

    ChrTalk(
        0xFE,
        (
            "Chiruru will probably\x01",
            "leave on one of her\x01",
            "trips right away...\x02",
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
            "I'm originally from the\x01",
            "Republic. I'm very familiar\x01",
            "with Eastern cuisine.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4662")

    label("loc_45DA")


    ChrTalk(
        0xFE,
        (
            "I'm originally from the\x01",
            "Republic. I'm very familiar\x01",
            "with Eastern cuisine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, the only thing I\x01",
            "can make well is fried\x01",
            "rice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4662")

    Jump("loc_46E6")

    label("loc_4667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_46E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4682")
    Call(0, 10)
    Jump("loc_46E6")

    label("loc_4682")


    ChrTalk(
        0xFE,
        (
            "Good grief... No matter what\x01",
            "trouble she gets into, I never get\x01",
            "the sense that she's learning.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46E6")

    TalkEnd(0xFE)
    Return()

    # Function_9_3903 end

    def Function_10_46EA(): pass

    label("Function_10_46EA")

    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xB,
        (
            "Oh Chiruru, you're back.\x01",
            "Your trip was quite long\x01",
            "this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I think you said you were walking\x01",
            "the Mainz mountains on foot or\x01",
            "something crazy like that.\x02",
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
            "*sigh*, looks like I'm not ready\x01",
            "for it yet. I'll try again if\x01",
            "there's another chance.\x02",
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

    # Function_10_46EA end

    def Function_11_4853(): pass

    label("Function_11_4853")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4864")
    Jump("loc_4972")

    label("loc_4864")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_48F8")

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
        (
            "Ah, I don't get it at\x01",
            "all!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4972")

    label("loc_48F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4972")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4913")
    Call(0, 12)
    Jump("loc_4972")

    label("loc_4913")


    ChrTalk(
        0xFE,
        (
            "My sister is a little\x01",
            "strange...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I often see her going\x01",
            "into weird places by\x01",
            "herself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4972")

    TalkEnd(0xFE)
    Return()

    # Function_11_4853 end

    def Function_12_4976(): pass

    label("Function_12_4976")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xC,
        (
            "Hey, Chiruru. Where are\x01",
            "we playing next?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmm... For now, I'm\x01",
            "planning on taking a\x01",
            "walk in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "There's still a lot of\x01",
            "places I haven't been.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Wow. You sure are weird.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I often see you going\x01",
            "into weird places by\x01",
            "yourself.\x02",
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

    # Function_12_4976 end

    def Function_13_4AA7(): pass

    label("Function_13_4AA7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4AB8")
    Jump("loc_4E61")

    label("loc_4AB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4BBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B82")
    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xFE,
        (
            "I'm getting annoyed, not\x01",
            "being able to leave the\x01",
            "city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Hmph. To bed, then.\x01",
            "Wake me up when it's\x01",
            "over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hey, this is no time to\x01",
            "be sleeping!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 5)
    Jump("loc_4BB7")

    label("loc_4B82")


    ChrTalk(
        0xFE,
        (
            "Wake me up when this is\x01",
            "over. I'm going to bed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BB7")

    Jump("loc_4E61")

    label("loc_4BBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4CE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C69")

    ChrTalk(
        0xFE,
        (
            "I feel like strange things\x01",
            "have been happening all\x01",
            "over Crossbell lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe it's best to\x01",
            "refrain from going on\x01",
            "trips for a while...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4CE3")

    label("loc_4C69")


    ChrTalk(
        0xFE,
        (
            "Maybe it's best to\x01",
            "refrain from going on\x01",
            "trips for a while...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I can't do anything\x01",
            "else, so I'm going to\x01",
            "bed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CE3")

    Jump("loc_4E61")

    label("loc_4CE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4CF6")
    Jump("loc_4E61")

    label("loc_4CF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4DC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D11")
    Call(0, 12)
    Jump("loc_4DC3")

    label("loc_4D11")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xFE,
        (
            "You're one to talk. Before, you snuck\x01",
            "into the Geofront, and when they\x01",
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

    label("loc_4DC3")

    Jump("loc_4E61")

    label("loc_4DC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4E61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DE3")
    Call(0, 10)
    Jump("loc_4E61")

    label("loc_4DE3")


    ChrTalk(
        0xFE,
        (
            "Traveling the Mainz\x01",
            "mountains on foot was\x01",
            "too hard for me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The next time I\x01",
            "challenge them, I'll\x01",
            "succeed for sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E61")

    TalkEnd(0xFE)
    Return()

    # Function_13_4AA7 end

    SaveToFile()

Try(main)

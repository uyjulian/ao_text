from ScenarioHelper import *

def main():
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
        "Leyte",                 # 1
        "Pance",                 # 2
        "Fay",                 # 3
        "Kouken",               # 4
        "Ryu",                 # 5
        "Chiluru",                 # 6
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
        "Function_5_1ED7",         # 05, 5
        "Function_6_22B8",         # 06, 6
        "Function_7_2DDC",         # 07, 7
        "Function_8_2F66",         # 08, 8
        "Function_9_37D2",         # 09, 9
        "Function_10_459A",        # 0A, 10
        "Function_11_46BE",        # 0B, 11
        "Function_12_47EA",        # 0C, 12
        "Function_13_4930",        # 0D, 13
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_757")

    ChrTalk(
        0xFE,
        (
            "Please contact Cecil earlier.\x01",
            "I was relieved for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just forgetting something\x01",
            "It looks like he is indulgent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because the hospital suddenly became busy\x01",
            "I do not think so ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have time,\x01",
            "Please stop by a hospital.\x01",
            "Because I would like to talk a lot.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7DA")

    label("loc_757")


    ChrTalk(
        0xFE,
        (
            "Cecil, somewhat intrigued\x01",
            "It looks like he is indulgent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have time,\x01",
            "Please stop by a hospital.\x01",
            "Because I would like to talk a lot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DA")

    Jump("loc_1ED3")

    label("loc_7DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABB")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Well, Lloyd is not you …!\x01",
            "Where have you been going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's right, did you meet Cecil?\x01",
            "I have not been able to see her for quite some time …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FOh, calm down.\x01",
            "… … It's nice to see you after a long absence.\x02\x03",
            "#00000FCecil 's older sister is now a hospital.\x01",
            "It looked like I was doing fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh yeah, it was good …\x01",
            "Lloyd also came back,\x01",
            "Aunt, I was really relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Outside is dangerous, on an aunt\x01",
            "Keep hiding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FNo, thankfully ….\x01",
            "I just have to go\x01",
            "There is a place not to be done.\x02\x03",
            "#00000FAunt,\x01",
            "Please wait here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yes … I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, are you going to be careful?\x01",
            "If you have something,\x01",
            "I, already …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, of course.\x01",
            "……see you later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BD, 7)
    Jump("loc_B40")

    label("loc_ABB")


    ChrTalk(
        0xFE,
        (
            "Was good……\x01",
            "Lloyd also came back,\x01",
            "Aunt, I was really relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh goddess of the sky, please\x01",
            "Your patronage … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B40")

    Jump("loc_1ED3")

    label("loc_B45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B53")
    Jump("loc_1ED3")

    label("loc_B53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C9A")

    ChrTalk(
        0xFE,
        (
            "Yesterday, to the hospital\x01",
            "I tried to contact you ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Cecils are\x01",
            "It seems to be busy quite often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F… It will be so.\x02\x03",
            "#00008FBecause of that raid incident,\x01",
            "There are also many patients in the hospital\x01",
            "It seems I got hospitalized … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haha, I'm worried.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Cecil is kinda,\x01",
            "Because it is too severe … …\x01",
            "I hope not to break your body.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CFE")

    label("loc_C9A")


    ChrTalk(
        0xFE,
        (
            "Under the influence of that raid incident,\x01",
            "The hospital seems to be busy quite often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Cecil, properly\x01",
            "I wonder if I'm resting …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CFE")

    Jump("loc_1ED3")

    label("loc_D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_DA8")

    ChrTalk(
        0xFE,
        (
            "It is an occupation incident,\x01",
            "People in Mainz\x01",
            "I guess you have a terrible feeling …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard that the guard is also struggling,\x01",
            "I wonder what will happen ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ED3")

    label("loc_DA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1174")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10EA")

    ChrTalk(
        0xFE,
        (
            "Oh, by the way, tomorrow\x01",
            "Of alkane shell\x01",
            "It was a renewal performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The tickets quickly\x01",
            "I heard that it was sold out … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, Iria also unknowingly noticed\x01",
            "I became a wonderful person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FI, Iria \"chan\" …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005Fby the way……\x01",
            "Cecil's older sister and Iria\x01",
            "I was a childhood friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, it is a conspicuous child from that time.\x01",
            "I admire himself with Cecil,\x01",
            "Well they were playing with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To a boy who was mean to Cecil\x01",
            "It took me as much as I could,\x01",
            "There were also things that made me cry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHehe, it seems to be Iria\x01",
            "It is an episode.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWell, the opponent's prisoner\x01",
            "It is kind of poor … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuff, the child's mean\x01",
            "It is because the favor is turned inside out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FWell, Iria's beaten up,\x01",
            "In a sense valuable memories\x01",
            "I wonder if I could do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FWell, how about that … ….\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16C, 3)

    label("loc_10EA")


    ChrTalk(
        0xFE,
        (
            "Hehe, Iria like that too\x01",
            "Now pull the alkane shell\x01",
            "Super star……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know it since I was a kid.\x01",
            "My aunt has a high nose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ED3")

    label("loc_1174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_11F6")

    ChrTalk(
        0xFE,
        (
            "Oh, now I am …\x01",
            "Is not it the sound of an ambulance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that many cars have passed ……\x01",
            "I wonder whether it was also a traffic accident.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ED3")

    label("loc_11F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1204")
    Jump("loc_1ED3")

    label("loc_1204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_139E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1314")

    ChrTalk(
        0xFE,
        (
            "Crossbell City national independence ……\x01",
            "In order to ask about its pros and cons,\x01",
            "It seems that a referendum will be held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is a pretty difficult question, is not it?\x01",
            "I often consult with my father,\x01",
            "I have to decide which one to vote for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder which is right,\x01",
            "It is not an easy answer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1399")

    label("loc_1314")


    ChrTalk(
        0xFE,
        (
            "For voting,\x01",
            "Talk with your father well\x01",
            "I'm thinking of deciding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder which is right,\x01",
            "It is not an easy answer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1399")

    Jump("loc_1ED3")

    label("loc_139E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1682")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1605")

    ChrTalk(
        0xFE,
        (
            "Oh, over there … ….\x01",
            "You sure was a Tio-chan, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FThank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Huhu, you look fine and tomorrow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If time is available\x01",
            "Let 's eat meals together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FOkama's dish ……\x01",
            "Hehe, I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FOh, exactly like the taste of bags\x01",
            "It is really delicious ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FOh, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FThat's nice …\x01",
            "I have to look forward to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course new members\x01",
            "You are invited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehuu, that time\x01",
            "Wear it with your arms\x01",
            "Because I will make it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThank you, Aunt.\x01",
            "If time is available\x01",
            "I will let you in the way.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 1)
    Jump("loc_167D")

    label("loc_1605")


    ChrTalk(
        0xFE,
        (
            "Now the members of the support department\x01",
            "You all got it together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhuu, if time is available again\x01",
            "Let 's eat meals together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_167D")

    Jump("loc_1ED3")

    label("loc_1682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1700")

    ChrTalk(
        0xFE,
        (
            "Oh no, in a moment\x01",
            "The sky has become totally dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My father will come back,\x01",
            "I have to prepare meals in a hurry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ED3")

    label("loc_1700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1971")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1902")

    ChrTalk(
        0x101,
        (
            "#00000FAunt, yesterday to Cecil elder sister\x01",
            "I greeted you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, it was.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, it's Cecil too\x01",
            "Were not you glad?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHaha, well …\x01",
            "It looks like she was doing fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHuff, beyond imagining\x01",
            "I was surprised at a wonderful woman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FWell, very much\x01",
            "There is a tolerance … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FIs not it ~? Anyway,\x01",
            "My striking in the middle\x01",
            "You're my sister!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FOh, you … hey ….\x01",
            "In front of Cecil's mother\x01",
            "How is that expression?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FReally it is true at all …\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 0)

    label("loc_1902")


    ChrTalk(
        0xFE,
        (
            "Huhu, Cecil!\x01",
            "It seems pretty popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you do not mind, from now on\x01",
            "Please give it to me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ED3")

    label("loc_1971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1AE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A9C")

    ChrTalk(
        0xFE,
        (
            "When you go shopping today,\x01",
            "A police guy who is traveling\x01",
            "I saw anyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all police,\x01",
            "You seem to be busy, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIt's a trade meeting since tomorrow.\x01",
            "While we do support requests\x01",
            "I'm looking around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh dear……\x01",
            "I think it is difficult,\x01",
            "Good luck with your work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AE0")

    label("loc_1A9C")


    ChrTalk(
        0xFE,
        (
            "You guys are\x01",
            "I think that it is hard,\x01",
            "Good luck with your work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AE0")

    Jump("loc_1ED3")

    label("loc_1AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1C8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B00")
    Call(0, 5)
    Jump("loc_1C87")

    label("loc_1B00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BF5")

    ChrTalk(
        0xFE,
        (
            "My father,\x01",
            "As a librarian at the library\x01",
            "I am working ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With a journalist from before\x01",
            "Have friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He seems to be a very knowledgeable person,\x01",
            "When that person is coming\x01",
            "I mean I'm talking to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehe he is like a child.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C87")

    label("loc_1BF5")


    ChrTalk(
        0xFE,
        (
            "My dad,\x01",
            "With a journalist from before\x01",
            "Have friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He seems to be a very knowledgeable person,\x01",
            "When that person is coming\x01",
            "I mean I'm talking to you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C87")

    Jump("loc_1ED3")

    label("loc_1C8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1ED3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA7")
    Call(0, 5)
    Jump("loc_1ED3")

    label("loc_1CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E5F")

    ChrTalk(
        0xFE,
        (
            "By the way, Mr. Lloyd,\x01",
            "I have already contacted Cecil?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, once in power communication.\x01",
            "Next time on another occasion\x01",
            "I will let you go again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, after returning home\x01",
            "Still more#2RTakuma#It seems I got better,\x01",
            "Cecil may be surprised, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, I guess so.\x01",
            "Ha ha ha …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00111F(Somehow it's embarrassing.\x01",
            "…… I wonder what you imagined. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F(To Huh, with Cecil\x01",
            "I'm getting more and more interested. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1ED3")

    label("loc_1E5F")


    ChrTalk(
        0xFE,
        (
            "Lloyd, come back\x01",
            "It seems that it got even stronger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, if you see Cecil\x01",
            "You might be surprised.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ED3")

    TalkEnd(0xFE)
    Return()

    # Function_4_64A end

    def Function_5_1ED7(): pass

    label("Function_5_1ED7")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Oh no … Oh no.\x01",
            "Lloyd is not you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FLady Aunt, I'm home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Planning is\x01",
            "It seems to be healthy and anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The support department also seems to be together,\x01",
            "One course's training\x01",
            "Did it finally end?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, the other day.\x01",
            "It is a little looking out\x01",
            "I was late ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FWho is this madam?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, something from childhood\x01",
            "It is a person who takes care of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWe are indebted to ourselves,\x01",
            "It is Mr. Cecil's mother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FCecil-san,\x01",
            "I met you at a hospital before …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, that's right Noel\x01",
            "I was acquainted with her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHmm, only me\x01",
            "Is it a fellow out?\x02\x03",
            "#10302FSomehow with Lloyd\x01",
            "It seems like an inequitable relationship ……\x01",
            "By all means I'd like to hear the story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FIt is an incompatible relationship,\x01",
            "It is not like that.\x02\x03",
            "#00000FWell Cecil's sister\x01",
            "There will be opportunities to meet again later,\x01",
            "I will introduce it even then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, support department\x01",
            "It looks like fun as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lloyd, something again\x01",
            "If there is something in trouble\x01",
            "You can come anytime.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 5)
    Return()

    # Function_5_1ED7 end

    def Function_6_22B8(): pass

    label("Function_6_22B8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_23FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_238D")

    ChrTalk(
        0xFE,
        (
            "Father, after the railroad stopped\x01",
            "Although I was not well for a while … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Try again soon\x01",
            "You are thrusting your neck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Completely, a mecha\x01",
            "I do not care.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23F5")

    label("loc_238D")


    ChrTalk(
        0xFE,
        (
            "Completely, a mecha\x01",
            "I do not care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… Well that is my dear\x01",
            "It's a nice place though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23F5")

    Jump("loc_2DD8")

    label("loc_23FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2469")

    ChrTalk(
        0xFE,
        "I wonder what's going on ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Maria Bell and the president\x01",
            "You managed to do something ……?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DD8")

    label("loc_2469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_24EB")

    ChrTalk(
        0xFE,
        (
            "Father, today from morning\x01",
            "I'm going to be very busy going to the station.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… At least while I am at home\x01",
            "I want you to be slow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DD8")

    label("loc_24EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2582")

    ChrTalk(
        0xFE,
        (
            "In this incident,\x01",
            "Iria of the alkane shell\x01",
            "You got a big injury ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if I can see that wonderful play already.\x01",
            "I do not care about that … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DD8")

    label("loc_2582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_268E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_262B")

    ChrTalk(
        0xFE,
        (
            "Today, alkane shell\x01",
            "There is a renewal performance on the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yet, somehow Father\x01",
            "You're making me worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What happened……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2689")

    label("loc_262B")


    ChrTalk(
        0xFE,
        (
            "Of alkane shell\x01",
            "There is a renewal performance\x01",
            "It is a congratulating day ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What happened……\x02",
    )

    CloseMessageWindow()

    label("loc_2689")

    Jump("loc_2DD8")

    label("loc_268E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2709")

    ChrTalk(
        0xFE,
        (
            "Father, Yesterday\x01",
            "Due to the derailment accident\x01",
            "It seems I was busy quite often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Please be quiet today.\x01",
            "Awesome.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DD8")

    label("loc_2709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_279E")

    ChrTalk(
        0xFE,
        (
            "Father,\x01",
            "I heard that the train accident happened\x01",
            "I jumped out in a hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard that I'm going to the station,\x01",
            "I wonder if it is OK …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DD8")

    label("loc_279E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2839")

    ChrTalk(
        0xFE,
        (
            "Oto-san,\x01",
            "Today I will show you my older sister\x01",
            "I want to go see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it's a big break.\x01",
            "I wish I could relax at home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DD8")

    label("loc_2839")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_28C6")

    ChrTalk(
        0xFE,
        (
            "Oto-san,\x01",
            "I will return from my business trip\x01",
            "I will rush into the bed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I have to change clothes\x01",
            "Sheets will get dirty.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DD8")

    label("loc_28C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_29CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2946")

    ChrTalk(
        0xFE,
        (
            "I got a picture of Maria Bell\x01",
            "I am reading a fashion magazine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, I'm longing for you ….\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_29C9")

    label("loc_2946")


    ChrTalk(
        0xFE,
        (
            "Ha, what's with Marybele?\x01",
            "I wonder if she is so beautiful and smart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "People like her\x01",
            "You say you are old-fashioned.\x01",
            "How nice……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29C9")

    Jump("loc_2DD8")

    label("loc_29CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2AE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A7A")

    ChrTalk(
        0xFE,
        (
            "……Ah!\x01",
            "On my shelf of fashion magazines\x01",
            "A railroad book is mixed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Absolute father 's work.\x01",
            "How many times have you handed your hands\x01",
            "I wonder if you intend to use it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_2AE1")

    label("loc_2A7A")


    ChrTalk(
        0xFE,
        (
            "Father, sometimes doing this\x01",
            "I try to like railroads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Because it is koshaku at all.\x02",
    )

    CloseMessageWindow()

    label("loc_2AE1")

    Jump("loc_2DD8")

    label("loc_2AE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2C99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C12")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0xFE,
        (
            "Everyone is a good boy.\x01",
            "About such a big building\x01",
            "Do not make a carous noise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, well,\x01",
            "Certainly it was amazing a bit … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From the building,\x01",
            "Who sees fashion magazines\x01",
            "It will be fun and fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Compare it.\x01",
            "I do not think so …).)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    OP_93(0xFE, 0x0, 0x0)
    Jump("loc_2C94")

    label("loc_2C12")


    ChrTalk(
        0xFE,
        (
            "(fluent……)\x01",
            "Wow, this older sister in this photo,\x01",
            "Very cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected after all,\x01",
            "Who had a constriction\x01",
            "I wonder if it is cool …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C94")

    Jump("loc_2DD8")

    label("loc_2C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2D1E")

    ChrTalk(
        0xFE,
        (
            "Father,\x01",
            "In addition, about a month on business trip\x01",
            "I am going to leave my house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As it is a train engineer,\x01",
            "It looks like various things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DD8")

    label("loc_2D1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2DCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D39")
    Call(0, 7)
    Jump("loc_2DCA")

    label("loc_2D39")


    ChrTalk(
        0xFE,
        (
            "I just like Mary Bell\x01",
            "To a cool and smart human\x01",
            "I just want to become.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As Father's expectation\x01",
            "I will not be an engineer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DCA")

    Jump("loc_2DD8")

    label("loc_2DCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2DD8")

    label("loc_2DD8")

    TalkEnd(0xFE)
    Return()

    # Function_6_22B8 end

    def Function_7_2DDC(): pass

    label("Function_7_2DDC")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x9,
        (
            "Marybele says,\x01",
            "Leading the technical department of IBC\x01",
            "It seems familiar to the power technology as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well …\x01",
            "I also do things about technology,\x01",
            "Is it better to study?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "Papacy\x01",
            "Finally on your way to the technician\x01",
            "I was interested!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "OK, this is the case.\x01",
            "The same railway engineer as your father\x01",
            "Do you want to aim?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "…. It does not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#4SWell!#3S\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 2)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_7_2DDC end

    def Function_8_2F66(): pass

    label("Function_8_2F66")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_30FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_306D")

    ChrTalk(
        0xFE,
        (
            "As a railroad technician,\x01",
            "As the transcontinental railroad is stopped,\x01",
            "Although it may be useless …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is the same power vehicle ride\x01",
            "With the maintenance of buses and driving vehicles\x01",
            "You should be able to use something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "OK, go over the city hall\x01",
            "I wonder if I will search for something.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_30F8")

    label("loc_306D")


    ChrTalk(
        0xFE,
        (
            "As a railroad technician,\x01",
            "Even with maintenance of buses and driving vehicles\x01",
            "You should be able to use something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "OK, go over the city hall\x01",
            "I wonder if I will search for something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30F8")

    Jump("loc_37CE")

    label("loc_30FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3176")

    ChrTalk(
        0xFE,
        (
            "Pans, do not go outside.\x01",
            "Like staying at home with your father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "My sister must also be okay ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_37CE")

    label("loc_3176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_32C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_324D")

    ChrTalk(
        0xFE,
        (
            "From this morning to Crossbell Station\x01",
            "I was going to help … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Trying to return home\x01",
            "A lot of foreigners came together,\x01",
            "It is quite confusing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I also cut up the break earlier\x01",
            "I have to go back to help.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_32BD")

    label("loc_324D")


    ChrTalk(
        0xFE,
        (
            "Foreigners gathered for the station\x01",
            "It is quite confusing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I also cut up the break earlier\x01",
            "I have to go back to help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32BD")

    Jump("loc_37CE")

    label("loc_32C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_32D0")
    Jump("loc_37CE")

    label("loc_32D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3338")

    ChrTalk(
        0xFE,
        (
            "Oh no!\x01",
            "No way, Mainz ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Armed groups and lions,\x01",
            "What on earth is the purpose …?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37CE")

    label("loc_3338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_335A")

    ChrTalk(
        0xFE,
        "Gangway …\x02",
    )

    CloseMessageWindow()
    Jump("loc_37CE")

    label("loc_335A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3368")
    Jump("loc_37CE")

    label("loc_3368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_34D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3456")
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Because it's painful, Wendy's\x01",
            "I would like to see a working figure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Pansa looked at her sister's appearance,\x01",
            "You should study engineers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "So, so I\x01",
            "You do not become an engineer\x01",
            "You are saying that!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_34CE")

    label("loc_3456")


    ChrTalk(
        0xFE,
        (
            "Pansa looked at her sister's appearance,\x01",
            "You should study engineers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the future to become an engineer\x01",
            "It will surely be helpful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34CE")

    Jump("loc_37CE")

    label("loc_34D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_354E")

    ChrTalk(
        0xFE,
        (
            "Mumboppy …\x01",
            "Oh, our bed is\x01",
            "It's awesome ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Like mud as it is\x01",
            "Let's be sleepy … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37CE")

    label("loc_354E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_355C")
    Jump("loc_37CE")

    label("loc_355C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_356A")
    Jump("loc_37CE")

    label("loc_356A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3578")
    Jump("loc_37CE")

    label("loc_3578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3586")
    Jump("loc_37CE")

    label("loc_3586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3627")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A1")
    Call(0, 7)
    Jump("loc_3622")

    label("loc_35A1")


    ChrTalk(
        0xFE,
        (
            "Well …\x01",
            "Well, is not it to be impatient?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because I am bleeding in my blood,\x01",
            "I am sure to be a respectable engineer in the future\x01",
            "You must be getting it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3622")

    Jump("loc_37CE")

    label("loc_3627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_37CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3757")

    ChrTalk(
        0x101,
        (
            "#00005FOh, Wendy's\x01",
            "It's my father …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FI guess you feel tired somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mumboppy …\x01",
            "I just got back from a business trip ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Panse, it's bad though\x01",
            "Rice is to eat alone … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F…… Looks like I am asleep.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHuhu, let's leave it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_37CE")

    label("loc_3757")


    ChrTalk(
        0xFE,
        (
            "…… That, PANSE\x01",
            "Where have you been ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, that's right.\x01",
            "Today was Sunday School Day … …\x01",
            "Mumboppy …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37CE")

    TalkEnd(0xFE)
    Return()

    # Function_8_2F66 end

    def Function_9_37D2(): pass

    label("Function_9_37D2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_396E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38DC")

    ChrTalk(
        0xFE,
        (
            "Ryu's fellow, just like children\x01",
            "I suppose I'm going to help with my neighborhood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Studying as a merchant today\x01",
            "I was going to have taught you.\x01",
            "Well, I ran away well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Well, if you do not do something\x01",
            "It may be that it is not calming down.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3969")

    label("loc_38DC")


    ChrTalk(
        0xFE,
        (
            "Ryu is okay, but ….\x01",
            "Chillul is Chillur, resuming his trip\x01",
            "I went to the Tangram gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Indeed,\x01",
            "My son is at home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3969")

    Jump("loc_4596")

    label("loc_396E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_39F2")

    ChrTalk(
        0xFE,
        (
            "My children are at home\x01",
            "Anyway, it is safe ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am worried about the outside situation.\x01",
            "What kind of situation is it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4596")

    label("loc_39F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3B35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AB8")

    ChrTalk(
        0xFE,
        (
            "Something like crossbell\x01",
            "A serious thing seems to happen … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… In any case, Chillul successfully\x01",
            "I came back and I was relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In such a case,\x01",
            "All my family must be together.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B30")

    label("loc_3AB8")


    ChrTalk(
        0xFE,
        (
            "Something like crossbell\x01",
            "A serious thing seems to happen … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As anything can happen,\x01",
            "I only have to prepare my mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B30")

    Jump("loc_4596")

    label("loc_3B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3BC6")

    ChrTalk(
        0xFE,
        (
            "The incident was serious … …\x01",
            "IBC's work is early\x01",
            "It was good to restore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Banks are for the merchant\x01",
            "It is the most important thing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4596")

    label("loc_3BC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3C3D")

    ChrTalk(
        0xFE,
        (
            "There is no way that such an incident will occur\x01",
            "I did not expect it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Chillle on a journey will be fine ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4596")

    label("loc_3C3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3D47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CE0")

    ChrTalk(
        0xFE,
        (
            "Again, in the rain\x01",
            "Like running around barefoot\x01",
            "He was a boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In that sense,\x01",
            "Ryu was my childhood\x01",
            "It closely resembles.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D42")

    label("loc_3CE0")


    ChrTalk(
        0xFE,
        (
            "Ryu was my childhood\x01",
            "It closely resembles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Therefore,\x01",
            "It may take extra hands.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D42")

    Jump("loc_4596")

    label("loc_3D47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3D9D")

    ChrTalk(
        0xFE,
        (
            "Hmm, something\x01",
            "The sound of a shy siren\x01",
            "I heard him … ….?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4596")

    label("loc_3D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3EFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E77")

    ChrTalk(
        0xFE,
        (
            "My daughter, Chiluru,\x01",
            "Come back from the trip.\x01",
            "Now I am out with my friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do it for Ryu Chillul,\x01",
            "A lot in my friendship\x01",
            "You seem to have been blessed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, absolutely\x01",
            "It will be appreciated.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3EF8")

    label("loc_3E77")


    ChrTalk(
        0xFE,
        (
            "Even though Chillul is almost in my house,\x01",
            "Katerina is\x01",
            "They are going out with each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, absolutely\x01",
            "It will be appreciated.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EF8")

    Jump("loc_4596")

    label("loc_3EFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3F9B")

    ChrTalk(
        0xFE,
        (
            "Today is my partner in Ryu\x01",
            "Trying to help with work\x01",
            "I thought … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Unprecedentatedly\x01",
            "You seem to have gone out.\x01",
            "I'm a fast-running guy at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4596")

    label("loc_3F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4028")

    ChrTalk(
        0xFE,
        (
            "Today Ryu also\x01",
            "To see the Orkis Tower\x01",
            "You seem to have gone out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I saw it yesterday as well\x01",
            "I do not get tired often.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4596")

    label("loc_4028")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4143")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40CA")

    ChrTalk(
        0xFE,
        (
            "Ryu will someday get the wholesale job\x01",
            "Well, I thought I wanted to make a connection … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Once upon a time\x01",
            "Remember to just play and remember.\x01",
            "Whew.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_413E")

    label("loc_40CA")


    ChrTalk(
        0xFE,
        (
            "Ryu's guys also got the results of the Sunday school\x01",
            "It's fresh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not just to play,\x01",
            "I have to learn a little bit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_413E")

    Jump("loc_4596")

    label("loc_4143")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4285")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_421E")

    ChrTalk(
        0xFE,
        (
            "I have been from about 3 years ago\x01",
            "I work as a wholesaler with a crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In accordance with the unveiling ceremony this time,\x01",
            "To a large extent from department store\x01",
            "There was an order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, the crossbell is lively,\x01",
            "It's a nice place to do business.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4280")

    label("loc_421E")


    ChrTalk(
        0xFE,
        (
            "In accordance with the unveiling ceremony this time,\x01",
            "To a large extent from department store\x01",
            "There was an order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Muho, it's a lot of prosperous.\x02",
    )

    CloseMessageWindow()

    label("loc_4280")

    Jump("loc_4596")

    label("loc_4285")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_43BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4339")

    ChrTalk(
        0xFE,
        (
            "Ryu's guy, recently\x01",
            "Momo-chan of Tully's place\x01",
            "You seem to invite you to play well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do not tell me about dangerous play,\x01",
            "I am a bit worried ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_43BA")

    label("loc_4339")


    ChrTalk(
        0xFE,
        (
            "To Momo-chan\x01",
            "If you taught dangerous play,\x01",
            "I apologize to my parents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ryu's fellow\x01",
            "I should keep my precaution.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43BA")

    Jump("loc_4596")

    label("loc_43BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4531")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44A6")

    ChrTalk(
        0xFE,
        (
            "Chilur also got on a trip soon\x01",
            "Is not it …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "While families are in order,\x01",
            "Even at my favorite fried rice\x01",
            "I suppose I will eat it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was originally from the Republic.\x01",
            "It's familiar to Oriental cuisine.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_452C")

    label("loc_44A6")


    ChrTalk(
        0xFE,
        (
            "I was originally from the Republic.\x01",
            "It's familiar to Oriental cuisine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, you can make it well\x01",
            "A monkey like a fried rice bowl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_452C")

    Jump("loc_4596")

    label("loc_4531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4596")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_454C")
    Call(0, 10)
    Jump("loc_4596")

    label("loc_454C")


    ChrTalk(
        0xFE,
        (
            "Whew ……\x01",
            "No matter what kind of danger it is\x01",
            "I do not feel like being totally discouraged.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4596")

    TalkEnd(0xFE)
    Return()

    # Function_9_37D2 end

    def Function_10_459A(): pass

    label("Function_10_459A")

    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xB,
        (
            "Ou Chilur, did you come back?\x01",
            "The trip this time was quite long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Sure, the Mainz mountain range\x01",
            "As you step over\x01",
            "Although he was saying unreasonable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yup……\x01",
            "I was distressed for a while on the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It seems that power is still insufficient.\x01",
            "I will also try the next opportunity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "You are a tragicist … …\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_10_459A end

    def Function_11_46BE(): pass

    label("Function_11_46BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_46CF")
    Jump("loc_47E6")

    label("loc_46CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_475D")

    ChrTalk(
        0xFE,
        (
            "From mine to martial law\x01",
            "If I tried to go out and play out secretly,\x01",
            "I am getting into this situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ha, I do not understand Wake.\x02",
    )

    CloseMessageWindow()
    Jump("loc_47E6")

    label("loc_475D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_47E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4778")
    Call(0, 12)
    Jump("loc_47E6")

    label("loc_4778")


    ChrTalk(
        0xFE,
        (
            "My older sister, what is it?\x01",
            "It's changing … oh ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Frequently from a self to a hen place\x01",
            "I think I should enter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47E6")

    TalkEnd(0xFE)
    Return()

    # Function_11_46BE end

    def Function_12_47EA(): pass

    label("Function_12_47EA")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xC,
        (
            "That's right, Sister,\x01",
            "Where will the next journey come?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmm……\x01",
            "For the time being,\x01",
            "I wonder whether I will walk around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I have never been there yet\x01",
            "There are many places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, my sister.\x01",
            "After all it changed, it was MON.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Frequently from a self to a hen place\x01",
            "I think I should enter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "…… I do not want you to tell me.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xC, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_12_47EA end

    def Function_13_4930(): pass

    label("Function_13_4930")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4941")
    Jump("loc_4C6F")

    label("loc_4941")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4A28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49F0")
    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Even I can not get out of town\x01",
            "Even though I am irritated ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Sad, sleep.\x01",
            "Please wake me up when the noise goes down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Right, are you sleeping ~!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 5)
    Jump("loc_4A23")

    label("loc_49F0")


    ChrTalk(
        0xFE,
        (
            "Please wake me up when the noise goes down.\x01",
            "…… I will go to bed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A23")

    Jump("loc_4C6F")

    label("loc_4A28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4B1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AB5")

    ChrTalk(
        0xFE,
        (
            "Recently, the whole crossbell\x01",
            "I feel like I'm getting strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For a while, to travel\x01",
            "Maybe he should refrain from … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4B15")

    label("loc_4AB5")


    ChrTalk(
        0xFE,
        (
            "For a while, to travel\x01",
            "Maybe he should refrain from … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… There is no other thing to do,\x01",
            "Let's sleep.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B15")

    Jump("loc_4C6F")

    label("loc_4B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4B28")
    Jump("loc_4C6F")

    label("loc_4B28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4BEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B43")
    Call(0, 12)
    Jump("loc_4BE5")

    label("loc_4B43")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xFE,
        (
            "… …. I got into Geo Front before,\x01",
            "To you who was rescued while crying\x01",
            "I do not want to be told.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xC)

    ChrTalk(
        0xC,
        "Becoming … crying!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)

    label("loc_4BE5")

    Jump("loc_4C6F")

    label("loc_4BEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4C6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C05")
    Call(0, 10)
    Jump("loc_4C6F")

    label("loc_4C05")


    ChrTalk(
        0xFE,
        (
            "Understanding the Mainz mountain range,\x01",
            "It was still stuffy for me ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next time you challenge,\x01",
            "I will definitely accomplish it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C6F")

    TalkEnd(0xFE)
    Return()

    # Function_13_4930 end

    SaveToFile()

Try(main)

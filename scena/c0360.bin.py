from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0360.bin",                # FileName
        "c0360",                    # MapName
        "c0360",                    # Location
        0x002D,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0360",                  # 0
        "Mrs. Imelda",            # 1
        "Doll",                   # 2
        "Doll",                   # 3
        "Girl",                   # 4
    ))

    AddCharChip((
        "chr/ch09000.itc",                   # 00
        "apl/ch51445.itc",                   # 01
    ))

    DeclNpc(94540,   29,      6329,    0,    453,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(94199,   1049,    8100,    180,  453,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(95099,   1049,    8100,    180,  453,  0x0, 2,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(4294966726, 0,       6100,    1200,    4294966726, 1500,    6100,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(384, 0)                                        # 0

    ScpFunction((
        "Function_0_180",          # 00, 0
        "Function_1_230",          # 01, 1
        "Function_2_2C0",          # 02, 2
        "Function_3_349",          # 03, 3
        "Function_4_402",          # 04, 4
        "Function_5_831",          # 05, 5
        "Function_6_30C2",         # 06, 6
        "Function_7_310D",         # 07, 7
        "Function_8_3158",         # 08, 8
        "Function_9_31A3",         # 09, 9
        "Function_10_31EE",        # 0A, 10
        "Function_11_3239",        # 0B, 11
        "Function_12_3284",        # 0C, 12
        "Function_13_32D9",        # 0D, 13
        "Function_14_3324",        # 0E, 14
        "Function_15_336F",        # 0F, 15
        "Function_16_33BA",        # 10, 16
        "Function_17_3405",        # 11, 17
        "Function_18_3450",        # 12, 18
        "Function_19_349B",        # 13, 19
    ))


    def Function_0_180(): pass

    label("Function_0_180")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1B8"),
        (1, "loc_1C4"),
        (2, "loc_1D0"),
        (3, "loc_1DC"),
        (4, "loc_1E8"),
        (5, "loc_1F4"),
        (6, "loc_200"),
        (SWITCH_DEFAULT, "loc_20C"),
    )


    label("loc_1B8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1C4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1D0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1DC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1E8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1F4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_200")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_20C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_218")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_22F")

    Return()

    # Function_0_180 end

    def Function_1_230(): pass

    label("Function_1_230")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_253")
    Event(0, 5)

    label("loc_253")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BF")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0xA, 0x2)
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BF")

    Return()

    # Function_1_230 end

    def Function_2_2C0(): pass

    label("Function_2_2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_309")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_348")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_348")

    Return()

    # Function_2_2C0 end

    def Function_3_349(): pass

    label("Function_3_349")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a car magazine, "Monthly Car Mania Vol.3".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x374, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FE")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "You learned the\x01\x07\x02",
            ""Deep Coloring"\x07\x00",
            " paint pattern.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x374, 1)

    label("loc_3FE")

    TalkEnd(0xFF)
    Return()

    # Function_3_349 end

    def Function_4_402(): pass

    label("Function_4_402")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A3")

    ChrTalk(
        0x8,
        (
            "Ihya hya, even so...\x01",
            "Thank you for your efforts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because of you, I'll probably be able to\x01",
            "finally find a buyer for these sisters dolls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FUhhm...Mrs. Imelda,\x01",
            "aren't you afraid?\x02\x03",
            "#00106FIf you sold haunted-like dolls,\x01",
            "wouldn't you be c-curs...\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya, how could I do such a business\x01",
            "if I were afraid of ghosts!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "After all, there're a few suspicious articles\x01",
            "I'm keeping in the store room too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you like, do you want to touch a ring with a story said\x01",
            "to bring a misfortune after the other to its owner?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_656")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_656")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_67F")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_67F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A8")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_6A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6CE")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_6CE")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#00012FI-I'll pass.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F(...It could be because such articles\x01",
            "gather in one only place that a\x01",
            "spiritual location was born.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F(T-Then in the end, the cause was this old lady...?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x179, 2)
    Jump("loc_82D")

    label("loc_7A3")


    ChrTalk(
        0x8,
        (
            "Because of you, I'll probably be able to\x01",
            "finally find a buyer for these sisters dolls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya, I must give\x01",
            "you my thanks, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82D")

    TalkEnd(0x8)
    Return()

    # Function_4_402 end

    def Function_5_831(): pass

    label("Function_5_831")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch44400.itc", 0x1E)
    OP_68(-130, 1000, -130, 0)
    MoveCamera(45, 35, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -2070, 0, -1990, 45)
    SetChrPos(0x102, -2070, 0, -1990, 45)
    SetChrPos(0x103, -2070, 0, -1990, 45)
    SetChrPos(0x104, -2070, 0, -1990, 45)
    SetChrPos(0x109, -2070, 0, -1990, 45)
    SetChrPos(0x105, -2070, 0, -1990, 45)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 6)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 7)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 8)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 9)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 10)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 11)
    OP_68(2840, 1000, 2910, 3000)
    OP_6F(0x1)
    StopBGM(0xFA0)
    WaitChrThread(0x105, 3)

    ChrTalk(
        0x101,
        (
            "#00000FExcuse us, is\x01",
            "anyone home?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    ChrTalk(
        0x104,
        (
            "#00305F...As expected, no one\x01",
            "is here, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FBut the delivery address\x01",
            "should be here for sure.\x02\x03",
            "#00103FThe entranceway\x01",
            "wasn't locked too...\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 13000, 1030, 2280, 270)

    NpcTalk(
        0xB,
        "Girl's Voice",
        "...Who are you, misters?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_BA2():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BA2)
    Sleep(50)

    def lambda_BB2():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BB2)
    Sleep(50)

    def lambda_BC2():
        TurnDirection(0x109, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BC2)
    Sleep(50)

    def lambda_BD2():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BD2)
    Sleep(50)

    def lambda_BE2():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BE2)
    Sleep(50)

    def lambda_BF2():
        TurnDirection(0x105, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BF2)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    Sleep(300)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7562", 0)
    Fade(500)
    OP_68(10720, 1000, 3550, 0)
    MoveCamera(43, 34, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    OP_68(3490, 1000, 2870, 5000)
    OP_95(0xB, 4650, 0, 2360, 2000, 0x0)
    WaitChrThread(0xB, 1)
    OP_6F(0x1)

    ChrTalk(
        0x109,
        "#10105FAh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FS-Someone is...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FE-Ehhm...\x01",
            "Little one, are you home alone now?\x02\x03",
            "#00000FWe came to deliver\x01",
            "a package...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ah, could it be...\x01",
            "That she's arrived!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hey, come in, come in!\x02",
    )

    CloseMessageWindow()
    OP_95(0xB, 9850, 1030, 2520, 2000, 0x0)

    def lambda_D6F():
        OP_95(0xFE, 9500, 1050, 10700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_D6F)
    Sleep(500)

    def lambda_D8C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D8C)
    Sleep(50)

    def lambda_D9C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D9C)
    Sleep(500)

    def lambda_DAC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DAC)
    Sleep(50)

    def lambda_DBC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DBC)
    Sleep(50)

    def lambda_DCC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DCC)
    Sleep(50)

    def lambda_DDC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DDC)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x105,
        (
            "#10309FHa ha, she didn't even\x01",
            "listen until the end.\x02\x03",
            "#10300FCould we assume it's a\x01",
            "package addressed to her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FT-That's strange...\x02\x03",
            "#00101FI've never heard that\x01",
            "such a kid was here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FStill...we ended up\x01",
            "meetin' really someone.\x02\x03",
            "#00301FWhat the heck is goin' on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI don't know, but...\x02\x03",
            "#00000FFor now, let's\x01",
            "get inside.\x02\x03",
            "Maybe we'll be able to hear,\x01",
            "something from that child.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(8870, 2000, 11100, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    OP_93(0xB, 0x10E, 0x0)
    SetChrPos(0x101, 8080, 1000, 11140, 90)
    SetChrPos(0x102, 7530, 1000, 10180, 90)
    SetChrPos(0x103, 7480, 1000, 11830, 90)
    SetChrPos(0x109, 6000, 1000, 10040, 90)
    SetChrPos(0x104, 6800, 1000, 10800, 90)
    SetChrPos(0x105, 5800, 1000, 11440, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00000FEehm, this is the package we came to deliver.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x33A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " handed over.\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x33A, 1)

    ChrTalk(
        0xB,
        "Yaay, she's finally come back home!\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xB,
        "...Oopsie-daisy.\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x3)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x2)
    SetChrPos(0xA, 10640, 1650, 10400, 270)
    Sound(802, 0, 70, 0)
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#00305F(...It looks like quite a worn out doll.)\x02\x03",
            "(Is it a Rosenberg\x01",
            "made antique doll...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F(No, it doesn't look like\x01",
            "to be that expensive...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FCould it be that\x01",
            "that doll is yours?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xB,
        "She's not a "doll"!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "She's my precious little sister.\x01",
            "Uhuhu, good girl, good girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FIs that so...?\x02\x03",
            "#00109FE-Eeehm. Thank goodness we\x01",
            "could bring her to you properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Yup, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Then, I'll just take\x01",
            "her to my room.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x87, 0x1F4)
    Sleep(300)
    Fade(500)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x2)
    Sound(802, 0, 70, 0)
    Sleep(700)
    BeginChrThread(0xB, 3, 0, 12)

    def lambda_135C():

        label("loc_135C")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_135C")

    QueueWorkItem2(0x101, 1, lambda_135C)

    def lambda_136E():

        label("loc_136E")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_136E")

    QueueWorkItem2(0x102, 1, lambda_136E)

    def lambda_1380():

        label("loc_1380")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_1380")

    QueueWorkItem2(0x103, 1, lambda_1380)

    def lambda_1392():

        label("loc_1392")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_1392")

    QueueWorkItem2(0x104, 1, lambda_1392)

    def lambda_13A4():

        label("loc_13A4")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_13A4")

    QueueWorkItem2(0x109, 1, lambda_13A4)

    def lambda_13B6():

        label("loc_13B6")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_13B6")

    QueueWorkItem2(0x105, 1, lambda_13B6)
    OP_68(2500, 2000, 15400, 5000)
    MoveCamera(45, 27, 0, 5000)
    OP_6E(440, 5000)
    SetCameraDistance(22000, 5000)
    OP_0D()
    Sleep(500)
    WaitChrThread(0xB, 3)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)

    def lambda_1413():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1413)

    def lambda_1424():
        OP_97(0xFE, 0x0, 0x0, 0x60E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1424)
    Sleep(500)
    SetChrFlags(0xB, 0x80)
    OP_0D()
    Sleep(500)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x0)
    Sleep(500)
    Fade(500)
    OP_68(6820, 2000, 11510, 0)
    MoveCamera(0, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20850, 0)
    OP_93(0x103, 0x13B, 0x0)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#10103FUhhm...\x01",
            "What's going on?\x02\x03",
            "#10100FThere's no presence of other\x01",
            "family members being at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F......?\x01",
            "Tio, what's wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...Nothing, I think it is just\x01",
            "my imagination, but...\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 410, 0, 410, 45)
    OP_4B(0x8, 0xFF)

    NpcTalk(
        0x8,
        "Elderly Woman's Voice",
        "#4S──Hey, is someone there!?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_168A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_168A)
    Sleep(50)

    def lambda_169A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_169A)
    Sleep(50)

    def lambda_16AA():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_16AA)
    Sleep(50)

    def lambda_16BA():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_16BA)
    Sleep(50)

    def lambda_16CA():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_16CA)
    Sleep(50)

    def lambda_16DA():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_16DA)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x101,
        "#00005F...A-A voice now...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FA guest...perhaps?\x02\x03",
            "It seems that her\x01",
            "parents are away, so\x01",
            "should we go answer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FY-Yeah...you're right.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(670, 1000, 1090, 0)
    MoveCamera(13, 30, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19760, 0)
    SetChrPos(0x101, 9840, 1030, 1950, 270)
    SetChrPos(0x103, 10930, 1030, 1890, 270)
    SetChrPos(0x104, 12090, 1030, 1840, 270)
    SetChrPos(0x102, 9820, 1030, 3070, 270)
    SetChrPos(0x109, 10940, 1030, 3020, 270)
    SetChrPos(0x105, 12100, 1030, 2970, 270)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(2140, 1000, 1810, 5000)
    SetCameraDistance(21780, 5000)

    def lambda_184E():
        OP_95(0xFE, 2500, 0, 1600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_184E)
    Sleep(50)

    def lambda_186B():
        OP_95(0xFE, 2500, 0, 2800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_186B)
    Sleep(50)

    def lambda_1888():
        OP_95(0xFE, 3700, 0, 1600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1888)
    Sleep(50)

    def lambda_18A5():
        OP_95(0xFE, 3700, 0, 2800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_18A5)
    Sleep(50)

    def lambda_18C2():
        OP_95(0xFE, 4900, 0, 1600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_18C2)
    Sleep(50)

    def lambda_18DF():
        OP_95(0xFE, 4900, 0, 2800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_18DF)
    WaitChrThread(0x101, 1)

    def lambda_18FD():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18FD)
    WaitChrThread(0x102, 1)

    def lambda_190E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_190E)
    WaitChrThread(0x103, 1)

    def lambda_191F():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_191F)
    WaitChrThread(0x109, 1)

    def lambda_1930():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1930)
    WaitChrThread(0x104, 1)

    def lambda_1941():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1941)
    WaitChrThread(0x105, 1)

    def lambda_1952():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1952)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00005FAh... You're from\x01",
            "the antique shop...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, it's you...\x01",
            "What're you doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, we just\x01",
            "visited due\x01",
            "to a job...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FDo you have some business here?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "...A job?\x01",
            "What're you saying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No one has moved in\x01",
            "this house for more than\x01",
            "10 years, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've been using it as\x01",
            "my antique shop store\x01",
            "room for a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    ChrTalk(
        0x8,
        (
            "...What's with the\x01",
            "puzzled faces?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B8D():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B8D)
    WaitChrThread(0x102, 1)

    def lambda_1B9E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B9E)
    WaitChrThread(0x103, 1)

    def lambda_1BAF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1BAF)
    WaitChrThread(0x109, 1)

    def lambda_1BC0():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1BC0)
    WaitChrThread(0x104, 1)

    def lambda_1BD1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1BD1)
    WaitChrThread(0x105, 1)

    def lambda_1BE2():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1BE2)

    ChrTalk(
        0x104,
        (
            "#00305F...W-What's goin' on here?\x02\x03",
            "Even if we assume that this\x01",
            "is the old lady's property...\x02\x03",
            "#00303FWe did talk to a little\x01",
            "girl just before, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10306FI suppose we did.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F...Let's ask that\x01",
            "girl from before\x01",
            "j-just in case.\x02\x03",
            "There could be some\x01",
            "circumstances...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FY-You're right...\x02\x03",
            "#00001FI'm sure she went to the room\x01",
            "in the back past the living room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I say, don't ignore me and\x01",
            "continue with your conversation.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)

    def lambda_1DB6():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DB6)
    WaitChrThread(0x102, 1)

    def lambda_1DC7():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1DC7)
    WaitChrThread(0x103, 1)

    def lambda_1DD8():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1DD8)
    WaitChrThread(0x109, 1)

    def lambda_1DE9():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1DE9)
    WaitChrThread(0x104, 1)

    def lambda_1DFA():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1DFA)
    WaitChrThread(0x105, 1)

    def lambda_1E0B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1E0B)

    ChrTalk(
        0x103,
        "#00205F............\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0xB, 0x1)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x2)
    SetChrPos(0xB, 94200, 1050, 8100, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrSubChip(0xA, 0x2)
    SetChrFlags(0xA, 0x2)
    SetChrPos(0xA, 95100, 1050, 8100, 180)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(99920, 1250, -140, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 100100, 0, -1950, 0)
    SetChrPos(0x103, 100100, 0, -1950, 0)
    SetChrPos(0x102, 100100, 0, -1950, 0)
    SetChrPos(0x104, 100100, 0, -1950, 0)
    SetChrPos(0x109, 100100, 0, -1950, 0)
    SetChrPos(0x105, 100100, 0, -1950, 0)
    SetChrPos(0x8, 100100, 0, -1950, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 13)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 14)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 15)
    Sleep(500)
    OP_68(100100, 1250, 2940, 3000)
    BeginChrThread(0x104, 3, 0, 16)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 17)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 18)
    Sleep(500)
    BeginChrThread(0x8, 3, 0, 19)
    WaitChrThread(0x105, 3)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#00005FW-What?\x01",
            "Where did that girl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FIs she hidin' somewhere...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xA, 500)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105FL-Lloyd...\x01",
            "Look at t-t-those...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHuh...\x02",
    )

    CloseMessageWindow()

    def lambda_20CD():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_20CD)
    Sleep(50)

    def lambda_20DD():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_20DD)
    Sleep(50)

    def lambda_20ED():
        TurnDirection(0x103, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_20ED)
    Sleep(50)

    def lambda_20FD():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_20FD)
    Sleep(50)

    def lambda_210D():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_210D)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    Sleep(50)

    def lambda_2134():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2134)
    OP_68(94650, 1250, 8100, 5000)
    MoveCamera(45, 24, 0, 5000)
    OP_6E(440, 5000)
    SetCameraDistance(19000, 5000)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(97220, 1250, 4330, 0)
    MoveCamera(24, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00005FThose dolls...\x01",
            "One is the one we\x01",
            "delivered, but...\x02\x03",
            "#00011FT-The other one...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10301FLike two peas in a pot with that girl.\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(100210, 1250, 1840, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    OP_93(0x8, 0x0, 0x0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "...You guys.\x01",
            "Isn't it time you explain\x01",
            "the situation to me too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Depending on the circumstances,\x01",
            "I could sue you for trespassing, you know?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2306():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2306)
    Sleep(50)

    def lambda_2316():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2316)
    Sleep(50)

    def lambda_2326():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2326)
    Sleep(50)

    def lambda_2336():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2336)
    Sleep(50)

    def lambda_2346():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2346)
    Sleep(50)

    def lambda_2356():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2356)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x101,
        (
            "#00006FI-I understand.\x01",
            "Actually, well...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained that they came to deliver a\x01",
            "package and that the girl who came to\x01",
            "receive them was identical to one of the dolls.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Ihya hya, now I see.\x01",
            "Then it means that something\x01",
            "like he said truly happened.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105FE-Eehm...what do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "One of the dolls over there\x01",
            "is something I bought abroad\x01",
            "many, many years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They're said to have been made in the\x01",
            "resemblance of the daughters of an old\x01",
            "distinguished family from somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because the girls were twin, it seems\x01",
            "they were made as a set of two, but I\x01",
            "could only acquire one of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They aren't bad articles, but\x01",
            "strangely they were dolls that\x01",
            "could not find a buyer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F...Ehm, and what relation does\x01",
            "that have with our story...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh boy, you're unexpectedly slow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The point is that the doll\x01",
            "you delivered here and the\x01",
            "strange girl who appeared...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I mean that perhaps\x01",
            "it was the doll itself\x01",
            "who came to life.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    ChrTalk(
        0x101,
        "#00011F#4S...HUUH!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's a guy who's been bragging since\x01",
            "in the past that "Life dwells in dolls"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya, maybe he\x01",
            "was unexpectedly right.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29F8")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "◆What about the Doll Studio quest in Zero? (Debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No change]\x01",         # 0
            "[Cleared]\x01",           # 1
            "[Didn't clear]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29E4")
    OP_29(0x30, 0x4, 0x10)
    Jump("loc_29F8")

    label("loc_29E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29F8")
    OP_29(0x30, 0x3, 0x10)

    label("loc_29F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2A65")

    ChrTalk(
        0x101,
        (
            "#00005FLife dwells in...\x02\x03",
            "#00003FI-Indeed, I feel like\x01",
            "Meister Jｶrg did say\x01",
            "that once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ABC")

    label("loc_2A65")


    ChrTalk(
        0x101,
        (
            "#00005FLife dwells in...\x02\x03",
            "#00006FAs you can expect,\x01",
            "I think it's an absurd story.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ABC")


    ChrTalk(
        0x102,
        (
            "#00105FT-Then...\x01",
            "It means that we saw\x01",
            "the doll's ghost!?\x02\x03",
            "#00106FN-No way...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2B13():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2B13)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00203FWell, truth or not aside...\x02\x03",
            "#00200FIt appears that this mansion\x01",
            "has become a kind of\x01",
            "spiritual "location".\x02\x03",
            "Like those "Tower" and "Temple", I can feel\x01",
            "the presence of the three higher elements...\x02\x03",
            "Those could have caused some\x01",
            "kind of spiritual phenomenon.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2C31():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C31)
    Sleep(50)

    def lambda_2C41():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2C41)
    Sleep(50)

    def lambda_2C51():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2C51)
    Sleep(50)

    def lambda_2C61():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2C61)
    Sleep(50)

    def lambda_2C71():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2C71)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x102,
        "#00105FS-Spiritual...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FSo that's why something\x01",
            "seemed off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FOn the spot I thought it\x01",
            "was an absurd story, but...\x02\x03",
            "#00306FAfter what peTiote said,\x01",
            "I think it's real.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112FAlthough it\x01",
            "feels unreal, eh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya...!\x01",
            "Yours are quite the\x01",
            "reactions to see.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2DA6():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2DA6)
    Sleep(50)

    def lambda_2DB6():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2DB6)
    Sleep(50)

    def lambda_2DC6():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2DC6)
    Sleep(50)

    def lambda_2DD6():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2DD6)
    Sleep(50)

    def lambda_2DE6():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2DE6)
    Sleep(50)

    def lambda_2DF6():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2DF6)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x8,
        (
            "Well, after all it's nonsense from\x01",
            "a recluse, so it's up to you to\x01",
            "believe it or not, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Only one thing is certain.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FA-And that is...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now that those sisters dolls\x01",
            "are together, they could\x01",
            "finally find a buyer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya...\x01",
            "What an incredible\x01",
            "bargain this is.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#00306FWhat a blunt old lady you're...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FW-Well, anyway...\x01",
            "With this, we finished delivering the packages.\x02\x03",
            "#00000FLet's go report to the\x01",
            "Capua Express guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FR-Right.\x01",
            "Let's go, quick...!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 2)
    NewScene("t3510", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_831 end

    def Function_6_30C2(): pass

    label("Function_6_30C2")


    def lambda_30C7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_30C7)

    def lambda_30D8():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30D8)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 3150, 0, 3230, 2000, 0x0)
    OP_93(0x101, 0x2D, 0x1F4)
    Return()

    # Function_6_30C2 end

    def Function_7_310D(): pass

    label("Function_7_310D")


    def lambda_3112():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3112)

    def lambda_3123():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3123)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 3000, 0, 2100, 2000, 0x0)
    OP_93(0x102, 0x2D, 0x1F4)
    Return()

    # Function_7_310D end

    def Function_8_3158(): pass

    label("Function_8_3158")


    def lambda_315D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_315D)

    def lambda_316E():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_316E)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 2140, 0, 3620, 2000, 0x0)
    OP_93(0x103, 0x2D, 0x1F4)
    Return()

    # Function_8_3158 end

    def Function_9_31A3(): pass

    label("Function_9_31A3")


    def lambda_31A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_31A8)

    def lambda_31B9():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_31B9)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 1840, 0, 2420, 2000, 0x0)
    OP_93(0x104, 0x2D, 0x1F4)
    Return()

    # Function_9_31A3 end

    def Function_10_31EE(): pass

    label("Function_10_31EE")


    def lambda_31F3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_31F3)

    def lambda_3204():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3204)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 900, 30, 2330, 2000, 0x0)
    OP_93(0x109, 0x2D, 0x1F4)
    Return()

    # Function_10_31EE end

    def Function_11_3239(): pass

    label("Function_11_3239")


    def lambda_323E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_323E)

    def lambda_324F():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_324F)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 1900, 30, 1240, 2000, 0x0)
    OP_93(0x105, 0x2D, 0x1F4)
    Return()

    # Function_11_3239 end

    def Function_12_3284(): pass

    label("Function_12_3284")

    OP_97(0xB, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_97(0xB, 0xFFFFE34A, 0x0, 0x0, 0x7D0, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    OP_97(0xB, 0x0, 0x0, 0x60E, 0x7D0, 0x0)
    Return()

    # Function_12_3284 end

    def Function_13_32D9(): pass

    label("Function_13_32D9")


    def lambda_32DE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_32DE)

    def lambda_32EF():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_32EF)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 100000, 30, 4000, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_13_32D9 end

    def Function_14_3324(): pass

    label("Function_14_3324")


    def lambda_3329():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3329)

    def lambda_333A():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_333A)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 98890, 30, 3530, 2000, 0x0)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_14_3324 end

    def Function_15_336F(): pass

    label("Function_15_336F")


    def lambda_3374():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3374)

    def lambda_3385():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3385)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 101030, 30, 3100, 2000, 0x0)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_15_336F end

    def Function_16_33BA(): pass

    label("Function_16_33BA")


    def lambda_33BF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_33BF)

    def lambda_33D0():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_33D0)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 99700, 30, 2800, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_16_33BA end

    def Function_17_3405(): pass

    label("Function_17_3405")


    def lambda_340A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_340A)

    def lambda_341B():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_341B)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 99500, 0, 1800, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_17_3405 end

    def Function_18_3450(): pass

    label("Function_18_3450")


    def lambda_3455():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3455)

    def lambda_3466():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3466)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 100860, 0, 1800, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_18_3450 end

    def Function_19_349B(): pass

    label("Function_19_349B")


    def lambda_34A0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_34A0)

    def lambda_34B1():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_34B1)
    WaitChrThread(0x8, 1)
    OP_95(0x8, 100000, 0, 500, 2000, 0x0)
    Return()

    # Function_19_349B end

    SaveToFile()

Try(main)

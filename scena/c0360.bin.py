from ScenarioHelper import *

def main():
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
        "Mrs. Imelda",           # 1
        "doll",                   # 2
        "doll",                   # 3
        "girl",                 # 4
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
        "Function_4_3F3",          # 04, 4
        "Function_5_7D7",          # 05, 5
        "Function_6_2F8C",         # 06, 6
        "Function_7_2FD7",         # 07, 7
        "Function_8_3022",         # 08, 8
        "Function_9_306D",         # 09, 9
        "Function_10_30B8",        # 0A, 10
        "Function_11_3103",        # 0B, 11
        "Function_12_314E",        # 0C, 12
        "Function_13_31A3",        # 0D, 13
        "Function_14_31EE",        # 0E, 14
        "Function_15_3239",        # 0F, 15
        "Function_16_3284",        # 10, 16
        "Function_17_32CF",        # 11, 17
        "Function_18_331A",        # 12, 18
        "Function_19_3365",        # 13, 19
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
            "There is a car magazine \"Monthly Carmania vol. 3\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('深暗色彩', 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EF")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "Paint pattern\x01\x07\x02",
            "\"Deep color\"\x07\x00",
            "I learned.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber('深暗色彩', 1)

    label("loc_3EF")

    TalkEnd(0xFF)
    Return()

    # Function_3_349 end

    def Function_4_3F3(): pass

    label("Function_4_3F3")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74F")

    ChrTalk(
        0x8,
        (
            "Hihaya, even so … …\x01",
            "You also had a hard time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "おかげさまで、この姉妹dollに\x01",
            "The buyer may finally get on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FThat … … Imelda\x01",
            "Are not you afraid?\x02\x03",
            "#00106F化けて出てくるようなdollを\x01",
            "After selling away,\x01",
            "Do not be scolded … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihyahya, I'm afraid of Obake\x01",
            "Can you do this business!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To those kept in this warehouse,\x01",
            "Because there are some strange items.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If anything, the owner will become unhappy one by one\x01",
            "Would you like to touch even the rings that are cute?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_615")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_615")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_63E")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_63E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_667")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_667")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_68D")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_68D")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#00012FOf course it is fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F(… … that kind of thing in one place\x01",
            "Because of the gathering, spiritual places\x01",
            "You may have been born. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F(___ ___ 0 ___ ___ 0\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x179, 2)
    Jump("loc_7D3")

    label("loc_74F")


    ChrTalk(
        0x8,
        (
            "おかげさまで、この姉妹dollに\x01",
            "The buyer may finally get on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihyacha, to you\x01",
            "I must give thanks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D3")

    TalkEnd(0x8)
    Return()

    # Function_4_3F3 end

    def Function_5_7D7(): pass

    label("Function_5_7D7")

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
            "#00000FExcuse me, someone\x01",
            "Do you Come?\x02",
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
            "#00305F…… Yeah everyone\x01",
            "Is not she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FBut the address of the addressee is\x01",
            "It surely is supposed to be here.\x02\x03",
            "#00103FThe key to the entrance\x01",
            "I did not take it ……\x02",
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
        "girlの声",
        "…… Granny, are not they?\x02",
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

    def lambda_B51():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B51)
    Sleep(50)

    def lambda_B61():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B61)
    Sleep(50)

    def lambda_B71():
        TurnDirection(0x109, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B71)
    Sleep(50)

    def lambda_B81():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B81)
    Sleep(50)

    def lambda_B91():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B91)
    Sleep(50)

    def lambda_BA1():
        TurnDirection(0x105, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BA1)
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
        "#10105FAh……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FHi, Who …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FLet me see……\x01",
            "Oya, are you alone at home now?\x02\x03",
            "#00000FThe older brothers\x01",
            "I came here to deliver my luggage ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, maybe ….\x01",
            "I wonder if it arrived! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hey, go up and go up!\x02",
    )

    CloseMessageWindow()
    OP_95(0xB, 9850, 1030, 2520, 2000, 0x0)

    def lambda_D2A():
        OP_95(0xFE, 9500, 1050, 10700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_D2A)
    Sleep(500)

    def lambda_D47():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D47)
    Sleep(50)

    def lambda_D57():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D57)
    Sleep(500)

    def lambda_D67():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D67)
    Sleep(50)

    def lambda_D77():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D77)
    Sleep(50)

    def lambda_D87():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D87)
    Sleep(50)

    def lambda_D97():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D97)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x105,
        (
            "#10309FHa ha, talk to her\x01",
            "I have not heard of it.\x02\x03",
            "#10300FTo be aware, it is addressed to that child\x01",
            "Is it a luggage?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FIt is strange …\x02\x03",
            "#00101FI do not know that such a child was there\x01",
            "Things I've never heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FBut … in reality like this\x01",
            "I guess I met her.\x02\x03",
            "#00301FWhat on earth is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI do not know but …\x02\x03",
            "#00000FTentatively,\x01",
            "Let's go inside.\x02\x03",
            "Something from that girl\x01",
            "You may be able to hear it.\x02",
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
        "#00000FWell, this is the luggage that came to be delivered.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '小箱子'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber('小箱子', 1)

    ChrTalk(
        0xB,
        "Wow, I finally came home!\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xB,
        "… and lads, and.\x02",
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
            "#00305F（……随分ボロそうなdollだな。）\x02\x03",
            "(This is also made by Rosenberg\x01",
            "Is it an antique doll? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F(No, that's expensive.\x01",
            "It does not seem to be … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002Fもしかして、このdollは\x01",
            "Is it yours?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xB,
        "It's not a thing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "He is a good little sister.\x01",
            "Uhufu, nice yo yo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106Fis that so……\x02\x03",
            "#00109FWell, uh.\x01",
            "I'm glad I got it properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Yes, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well then, I got this girl\x01",
            "I will bring you to my room.\x02",
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

    def lambda_1305():

        label("loc_1305")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_1305")

    QueueWorkItem2(0x101, 1, lambda_1305)

    def lambda_1317():

        label("loc_1317")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_1317")

    QueueWorkItem2(0x102, 1, lambda_1317)

    def lambda_1329():

        label("loc_1329")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_1329")

    QueueWorkItem2(0x103, 1, lambda_1329)

    def lambda_133B():

        label("loc_133B")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_133B")

    QueueWorkItem2(0x104, 1, lambda_133B)

    def lambda_134D():

        label("loc_134D")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_134D")

    QueueWorkItem2(0x109, 1, lambda_134D)

    def lambda_135F():

        label("loc_135F")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_135F")

    QueueWorkItem2(0x105, 1, lambda_135F)
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

    def lambda_13BC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_13BC)

    def lambda_13CD():
        OP_97(0xFE, 0x0, 0x0, 0x60E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_13CD)
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
            "#10103FWell …\x01",
            "I guess it is.\x02\x03",
            "#10100FThere are other families in the house\x01",
            "I do not have a sign … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F……?\x01",
            "Tio, what's wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FNo no it probably\x01",
            "I think that it is due to mind … …\x02",
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
        "Voice of an old woman",
        "#4S── Who is this person! Is it?\x02",
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

    def lambda_1626():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1626)
    Sleep(50)

    def lambda_1636():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1636)
    Sleep(50)

    def lambda_1646():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1646)
    Sleep(50)

    def lambda_1656():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1656)
    Sleep(50)

    def lambda_1666():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1666)
    Sleep(50)

    def lambda_1676():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1676)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x101,
        "#00005F…, Is your voice now …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FCustomers … … I wonder?\x02\x03",
            "Parents are\x01",
            "He seems to be out.\x01",
            "Shall we let you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, oh … That's right.\x02",
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

    def lambda_17F3():
        OP_95(0xFE, 2500, 0, 1600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17F3)
    Sleep(50)

    def lambda_1810():
        OP_95(0xFE, 2500, 0, 2800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1810)
    Sleep(50)

    def lambda_182D():
        OP_95(0xFE, 3700, 0, 1600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_182D)
    Sleep(50)

    def lambda_184A():
        OP_95(0xFE, 3700, 0, 2800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_184A)
    Sleep(50)

    def lambda_1867():
        OP_95(0xFE, 4900, 0, 1600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1867)
    Sleep(50)

    def lambda_1884():
        OP_95(0xFE, 4900, 0, 2800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1884)
    WaitChrThread(0x101, 1)

    def lambda_18A2():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18A2)
    WaitChrThread(0x102, 1)

    def lambda_18B3():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_18B3)
    WaitChrThread(0x103, 1)

    def lambda_18C4():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_18C4)
    WaitChrThread(0x109, 1)

    def lambda_18D5():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_18D5)
    WaitChrThread(0x104, 1)

    def lambda_18E6():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_18E6)
    WaitChrThread(0x105, 1)

    def lambda_18F7():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_18F7)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00005FAh……\x01",
            "Antique shop's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, you guys ……\x01",
            "What are you doing in such a place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell then,\x01",
            "Where did you hear it at work?\x01",
            "Was it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FWould you like something for this house?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "……work?\x01",
            "What are you talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In this house\x01",
            "For over 10 years ago\x01",
            "Nobody has moved in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For a while\x01",
            "Antique shop\x01",
            "It is about a storeroom.\x02",
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
            "I see …\x01",
            "The face that does not make sense to that.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B45():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B45)
    WaitChrThread(0x102, 1)

    def lambda_1B56():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B56)
    WaitChrThread(0x103, 1)

    def lambda_1B67():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1B67)
    WaitChrThread(0x109, 1)

    def lambda_1B78():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1B78)
    WaitChrThread(0x104, 1)

    def lambda_1B89():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1B89)
    WaitChrThread(0x105, 1)

    def lambda_1B9A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1B9A)

    ChrTalk(
        0x104,
        (
            "#00305F…, what does that mean?\x02\x03",
            "Owned by an old lady\x01",
            "Even if it was good that it was a property ……\x02\x03",
            "#00303FWe, certainly earlier\x01",
            "girlと話してたよな？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10306FIt should be that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F…… just to be safe\x01",
            "さっきのgirlに\x01",
            "Let's talk.\x02\x03",
            "I wonder if there are any circumstances\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThat's right.\x02\x03",
            "#00001FCertainly in the room behind the living room\x01",
            "I should have been there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This, ignoring me\x01",
            "Do not talk about it.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)

    def lambda_1D4A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D4A)
    WaitChrThread(0x102, 1)

    def lambda_1D5B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1D5B)
    WaitChrThread(0x103, 1)

    def lambda_1D6C():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1D6C)
    WaitChrThread(0x109, 1)

    def lambda_1D7D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D7D)
    WaitChrThread(0x104, 1)

    def lambda_1D8E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1D8E)
    WaitChrThread(0x105, 1)

    def lambda_1D9F():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1D9F)

    ChrTalk(
        0x103,
        "#00205F………………………………\x02",
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
            "#00005FOh, that?\x01",
            "さっきのgirlはどこに……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FIs it hiding somewhere …?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xA, 500)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105FB, Lloyd …\x01",
            "Oh, Oh, look at that … ….!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHuh……\x02",
    )

    CloseMessageWindow()

    def lambda_2078():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2078)
    Sleep(50)

    def lambda_2088():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2088)
    Sleep(50)

    def lambda_2098():
        TurnDirection(0x103, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2098)
    Sleep(50)

    def lambda_20A8():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_20A8)
    Sleep(50)

    def lambda_20B8():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_20B8)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    Sleep(50)

    def lambda_20DF():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_20DF)
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
            "#00005Fあのdoll……\x01",
            "We delivered one\x01",
            "Though it is a thing ……\x02\x03",
            "#00011FEven the other one ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10301Fさっきのgirlに瓜二つだね。\x02",
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
            "… … you guys.\x01",
            "Not even to me\x01",
            "Why do not you explain the circumstances?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Depending on things gradually,\x01",
            "You can appeal by trespassing?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_228F():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_228F)
    Sleep(50)

    def lambda_229F():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_229F)
    Sleep(50)

    def lambda_22AF():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_22AF)
    Sleep(50)

    def lambda_22BF():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_22BF)
    Sleep(50)

    def lambda_22CF():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_22CF)
    Sleep(50)

    def lambda_22DF():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_22DF)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x101,
        (
            "#00006FI understand.\x01",
            "Actually, that … …\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I visited the ship to deliver my luggage,\x01",
            "出迎えた少女がdollの片方に\x01",
            "I explained two things.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… Hihyahya, I see.\x01",
            "Things like what the guy was saying\x01",
            "That is exactly what happened.\x02",
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
        "#10105FEr, um … what does that mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "そこのdollの片方はね、\x01",
            "In the past, I attended a foreign country\x01",
            "It was Monz who was purchasing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To the daughters of old old families\x01",
            "It is said that it was made to resemble,\x01",
            "It is a kind of thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Daughters were twins\x01",
            "２体１組のdollが作られたそうだが、\x01",
            "Only one was able to get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's not a bad item,\x01",
            "Wonder and buyer not attached\x01",
            "妙なdollだったのさ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FWell, to that story\x01",
            "What on earth is it …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Well, it's unexpectedly dull.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In short,\x01",
            "dollがこの場所に届いたことや\x01",
            "What a strange girl has appeared ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "それらはdoll自身が\x01",
            "It may be made with life\x01",
            "That's it.\x02",
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
        "#00011F#4S… … Ha! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "昔から『dollには命が宿る』なんて\x01",
            "There is a lie who is lying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihyacha, unexpected real\x01",
            "It might be that it was.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28E8")
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
            "前編のdoll工房クエストを？（テスト用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【It does not change】\x01",            # 0
            "【I am clearing】\x01",        # 1
            "【Not clear】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28D4")
    OP_29(0x30, 0x4, 0x10)
    Jump("loc_28E8")

    label("loc_28D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28E8")
    OP_29(0x30, 0x3, 0x10)

    label("loc_28E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2963")

    ChrTalk(
        0x101,
        (
            "#00005FLife is dwelling ……\x02\x03",
            "#00003FYes, indeed the former Jorggua\x01",
            "It seems like I was saying such a thing\x01",
            "I think I do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29B6")

    label("loc_2963")


    ChrTalk(
        0x101,
        (
            "#00005FLife is dwelling ……\x02\x03",
            "#00006FIndeed impossible\x01",
            "話のようなI think I do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29B6")


    ChrTalk(
        0x102,
        (
            "#00105FWell then, then …\x01",
            "dollのお化けが出たって\x01",
            "Is that it! Is it?\x02\x03",
            "#00106FWell, that's like that ….\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A1D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2A1D)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00203FWell, aside from genuineness … …\x02\x03",
            "#00200FApparently this mansion is\x01",
            "With some spiritual \"place\"\x01",
            "It seems to be getting.\x02\x03",
            "Same as the example \"tower\" and \"monastery\"\x01",
            "It's a sign of the top three attributes … …\x02\x03",
            "It is a kind of spiritual phenomenon\x01",
            "It may have caused it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2B0F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B0F)
    Sleep(50)

    def lambda_2B1F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2B1F)
    Sleep(50)

    def lambda_2B2F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2B2F)
    Sleep(50)

    def lambda_2B3F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2B3F)
    Sleep(50)

    def lambda_2B4F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2B4F)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x102,
        "#00105FSpiritual ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FSo what?\x01",
            "The state was strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FI can not believe in anything.\x01",
            "I thought it was a story … …\x02\x03",
            "#00306FWhen Tio says\x01",
            "You seem to be serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112FWell, I suppose\x01",
            "I feel it, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihaya …!\x01",
            "It is quite a reaction\x01",
            "It's fine, is not it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2C87():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2C87)
    Sleep(50)

    def lambda_2C97():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2C97)
    Sleep(50)

    def lambda_2CA7():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2CA7)
    Sleep(50)

    def lambda_2CB7():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2CB7)
    Sleep(50)

    def lambda_2CC7():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2CC7)
    Sleep(50)

    def lambda_2CD7():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2CD7)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x8,
        (
            "Well, after all, it is a ploy for the recluse\x01",
            "Believe it or not\x01",
            "Even though you are selfish … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "There is definite thing only one thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FWell, that … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "あの姉妹dollが揃った今、\x01",
            "The buyer may come after a while\x01",
            "That's it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hihaya ……\x01",
            "It's alright Then picking mon\x01",
            "It was.\x02",
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
        "#00306FI'm an old lad who does not have a lid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell, anyway …\x01",
            "The package has been delivered by this.\x02\x03",
            "#00000FTo the person of Kapua express mail,\x01",
            "I will go report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FThat's right.\x01",
            "Let's go quickly …!\x02",
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

    # Function_5_7D7 end

    def Function_6_2F8C(): pass

    label("Function_6_2F8C")


    def lambda_2F91():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2F91)

    def lambda_2FA2():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FA2)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 3150, 0, 3230, 2000, 0x0)
    OP_93(0x101, 0x2D, 0x1F4)
    Return()

    # Function_6_2F8C end

    def Function_7_2FD7(): pass

    label("Function_7_2FD7")


    def lambda_2FDC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2FDC)

    def lambda_2FED():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2FED)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 3000, 0, 2100, 2000, 0x0)
    OP_93(0x102, 0x2D, 0x1F4)
    Return()

    # Function_7_2FD7 end

    def Function_8_3022(): pass

    label("Function_8_3022")


    def lambda_3027():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3027)

    def lambda_3038():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3038)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 2140, 0, 3620, 2000, 0x0)
    OP_93(0x103, 0x2D, 0x1F4)
    Return()

    # Function_8_3022 end

    def Function_9_306D(): pass

    label("Function_9_306D")


    def lambda_3072():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3072)

    def lambda_3083():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3083)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 1840, 0, 2420, 2000, 0x0)
    OP_93(0x104, 0x2D, 0x1F4)
    Return()

    # Function_9_306D end

    def Function_10_30B8(): pass

    label("Function_10_30B8")


    def lambda_30BD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_30BD)

    def lambda_30CE():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_30CE)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 900, 30, 2330, 2000, 0x0)
    OP_93(0x109, 0x2D, 0x1F4)
    Return()

    # Function_10_30B8 end

    def Function_11_3103(): pass

    label("Function_11_3103")


    def lambda_3108():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3108)

    def lambda_3119():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3119)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 1900, 30, 1240, 2000, 0x0)
    OP_93(0x105, 0x2D, 0x1F4)
    Return()

    # Function_11_3103 end

    def Function_12_314E(): pass

    label("Function_12_314E")

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

    # Function_12_314E end

    def Function_13_31A3(): pass

    label("Function_13_31A3")


    def lambda_31A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_31A8)

    def lambda_31B9():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_31B9)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 100000, 30, 4000, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_13_31A3 end

    def Function_14_31EE(): pass

    label("Function_14_31EE")


    def lambda_31F3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_31F3)

    def lambda_3204():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3204)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 98890, 30, 3530, 2000, 0x0)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_14_31EE end

    def Function_15_3239(): pass

    label("Function_15_3239")


    def lambda_323E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_323E)

    def lambda_324F():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_324F)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 101030, 30, 3100, 2000, 0x0)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_15_3239 end

    def Function_16_3284(): pass

    label("Function_16_3284")


    def lambda_3289():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3289)

    def lambda_329A():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_329A)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 99700, 30, 2800, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_16_3284 end

    def Function_17_32CF(): pass

    label("Function_17_32CF")


    def lambda_32D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_32D4)

    def lambda_32E5():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_32E5)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 99500, 0, 1800, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_17_32CF end

    def Function_18_331A(): pass

    label("Function_18_331A")


    def lambda_331F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_331F)

    def lambda_3330():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3330)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 100860, 0, 1800, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_18_331A end

    def Function_19_3365(): pass

    label("Function_19_3365")


    def lambda_336A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_336A)

    def lambda_337B():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_337B)
    WaitChrThread(0x8, 1)
    OP_95(0x8, 100000, 0, 500, 2000, 0x0)
    Return()

    # Function_19_3365 end

    SaveToFile()

Try(main)

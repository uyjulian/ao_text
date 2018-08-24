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
        "Function_4_3F8",          # 04, 4
        "Function_5_7FD",          # 05, 5
        "Function_6_2FD0",         # 06, 6
        "Function_7_301B",         # 07, 7
        "Function_8_3066",         # 08, 8
        "Function_9_30B1",         # 09, 9
        "Function_10_30FC",        # 0A, 10
        "Function_11_3147",        # 0B, 11
        "Function_12_3192",        # 0C, 12
        "Function_13_31E7",        # 0D, 13
        "Function_14_3232",        # 0E, 14
        "Function_15_327D",        # 0F, 15
        "Function_16_32C8",        # 10, 16
        "Function_17_3313",        # 11, 17
        "Function_18_335E",        # 12, 18
        "Function_19_33A9",        # 13, 19
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
            "It's a car magazine,\x01",
            ""Monthly Car Mania\x01",
            "Vol.3".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x374, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F4")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "Learned the "Deep\x01",
            "Coloring"\x07\x00",
            " paint pattern.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x374, 1)

    label("loc_3F4")

    TalkEnd(0xFF)
    Return()

    # Function_3_349 end

    def Function_4_3F8(): pass

    label("Function_4_3F8")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_782")

    ChrTalk(
        0x8,
        (
            "Ihya hya, even so...\x01",
            "Thank you for your\x01",
            "efforts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because of you, I'll might\x01",
            "finally find a buyer for\x01",
            "these doll sisters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FUmm... Mrs. Imelda,\x01",
            "aren't you afraid?\x02\x03",
            "#00106FIf you sold haunted\x01",
            "dolls, wouldn't you be\x01",
            "c-cursed or...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya, how could I be\x01",
            "in a business like mine if\x01",
            "I were afraid of ghosts!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm keeping a few suspicious\x01",
            "items in this storeroom\x01",
            "besides just those, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How would you like to touch a\x01",
            "ring said to bring misfortune\x01",
            "to one owner after the next?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62E")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_62E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_657")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_657")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_680")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_680")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A6")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_6A6")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#00012FI-I'll pass.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F(...This spiritual field could have\x01",
            "been created by many such objects\x01",
            "being gathered in one place.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F(T-Then in the end, this\x01",
            "old lady's the cause of\x01",
            "all this?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x179, 2)
    Jump("loc_7F9")

    label("loc_782")


    ChrTalk(
        0x8,
        (
            "Because of you, I'll might\x01",
            "finally find a buyer for\x01",
            "these doll sisters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya, allow me to\x01",
            "thank you, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F9")

    TalkEnd(0x8)
    Return()

    # Function_4_3F8 end

    def Function_5_7FD(): pass

    label("Function_5_7FD")

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
            "#00000FExcuse us, is anyone\x01",
            "home?\x02",
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
        "#00305FNo one's here, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FBut this is definitely\x01",
            "the delivery address.\x02\x03",
            "#00103FThe entrance wasn't\x01",
            "locked either...\x02",
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
        (
            "...Ladies and gentlemen,\x01",
            "who aaare you?\x02",
        )
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

    def lambda_B67():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B67)
    Sleep(50)

    def lambda_B77():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B77)
    Sleep(50)

    def lambda_B87():
        TurnDirection(0x109, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B87)
    Sleep(50)

    def lambda_B97():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B97)
    Sleep(50)

    def lambda_BA7():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BA7)
    Sleep(50)

    def lambda_BB7():
        TurnDirection(0x105, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BB7)
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
        "#10105FAh?\x02",
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
            "#00005FUmm... Are you home\x01",
            "alone, little lady?\x02\x03",
            "#00000FWe came to deliver a\x01",
            "package...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ah, could it be... that\x01",
            "she's arrived!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Come in, come in!\x02",
    )

    CloseMessageWindow()
    OP_95(0xB, 9850, 1030, 2520, 2000, 0x0)

    def lambda_D26():
        OP_95(0xFE, 9500, 1050, 10700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_D26)
    Sleep(500)

    def lambda_D43():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D43)
    Sleep(50)

    def lambda_D53():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D53)
    Sleep(500)

    def lambda_D63():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D63)
    Sleep(50)

    def lambda_D73():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D73)
    Sleep(50)

    def lambda_D83():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D83)
    Sleep(50)

    def lambda_D93():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D93)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x105,
        (
            "#10309FHaha, it feels like\x01",
            "she's not even listening\x01",
            "to us.\x02\x03",
            "#10300FCan we assume it's a\x01",
            "package addressed to\x01",
            "her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FT-That's strange...\x02\x03",
            "#00101FI've not heard that a\x01",
            "girl like this lives\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FStill... It's a fact\x01",
            "that we met someone\x01",
            "livin' here.\x02\x03",
            "#00301FWhat the heck is goin'\x01",
            "on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI don't know, but...\x02\x03",
            "#00000FFor now, let's enter.\x02\x03",
            "We might be able to\x01",
            "question that girl.\x02",
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
        (
            "#00000FUmm, this is the package\x01",
            "we came to deliver.\x02",
        )
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
        (
            "Yaay, she's finally come\x01",
            "back home!\x02",
        )
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
            "#00305F(...That doll looks\x01",
            "quite worn-out.)\x02\x03",
            "(Is this one of those\x01",
            "Rosenberg antique\x01",
            "dolls?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F(No, it doesn't look\x01",
            "quite that expensive...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FCould it be that this\x01",
            "doll is yours?\x02",
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
            "She's my precious, precious\x01",
            "little sister. Uhuhu, good\x01",
            "girl, good girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FI see...\x02\x03",
            "#00109FU-Umm. Thank goodness we\x01",
            "brought her to you.\x02",
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
            "Then, I'll just take her\x01",
            "to my room.\x02",
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

    def lambda_1303():

        label("loc_1303")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_1303")

    QueueWorkItem2(0x101, 1, lambda_1303)

    def lambda_1315():

        label("loc_1315")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_1315")

    QueueWorkItem2(0x102, 1, lambda_1315)

    def lambda_1327():

        label("loc_1327")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_1327")

    QueueWorkItem2(0x103, 1, lambda_1327)

    def lambda_1339():

        label("loc_1339")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_1339")

    QueueWorkItem2(0x104, 1, lambda_1339)

    def lambda_134B():

        label("loc_134B")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_134B")

    QueueWorkItem2(0x109, 1, lambda_134B)

    def lambda_135D():

        label("loc_135D")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_135D")

    QueueWorkItem2(0x105, 1, lambda_135D)
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

    def lambda_13BA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_13BA)

    def lambda_13CB():
        OP_97(0xFE, 0x0, 0x0, 0x60E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_13CB)
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
            "#10103FUmm... What's going on?\x02\x03",
            "#10100FIt doesn't look like\x01",
            "anyone else is here...\x02",
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
        "#00005F...? Tio, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...Well, I think it is\x01",
            "just my imagination,\x01",
            "but...\x02",
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
        "#4S─Hey, is someone there!?\x02",
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

    def lambda_1619():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1619)
    Sleep(50)

    def lambda_1629():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1629)
    Sleep(50)

    def lambda_1639():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1639)
    Sleep(50)

    def lambda_1649():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1649)
    Sleep(50)

    def lambda_1659():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1659)
    Sleep(50)

    def lambda_1669():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1669)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x101,
        "#00005F...This voice is...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FA guest... perhaps?\x02\x03",
            "Her parents aren't home,\x01",
            "so shall we answer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FY-Yeah... let's.\x02",
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

    def lambda_17C9():
        OP_95(0xFE, 2500, 0, 1600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17C9)
    Sleep(50)

    def lambda_17E6():
        OP_95(0xFE, 2500, 0, 2800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_17E6)
    Sleep(50)

    def lambda_1803():
        OP_95(0xFE, 3700, 0, 1600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1803)
    Sleep(50)

    def lambda_1820():
        OP_95(0xFE, 3700, 0, 2800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1820)
    Sleep(50)

    def lambda_183D():
        OP_95(0xFE, 4900, 0, 1600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_183D)
    Sleep(50)

    def lambda_185A():
        OP_95(0xFE, 4900, 0, 2800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_185A)
    WaitChrThread(0x101, 1)

    def lambda_1878():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1878)
    WaitChrThread(0x102, 1)

    def lambda_1889():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1889)
    WaitChrThread(0x103, 1)

    def lambda_189A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_189A)
    WaitChrThread(0x109, 1)

    def lambda_18AB():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_18AB)
    WaitChrThread(0x104, 1)

    def lambda_18BC():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_18BC)
    WaitChrThread(0x105, 1)

    def lambda_18CD():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_18CD)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00005FAh... You're from the\x01",
            "antique shop...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, it's all of you...\x01",
            "What are you doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FUmm, well, we're here\x01",
            "for work, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FCould you have business\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Work? What are you\x01",
            "saying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No one's lived here for\x01",
            "at least 10 years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've been using it as my\x01",
            "antique shop storeroom\x01",
            "for some time now.\x02",
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
            "What's with the puzzled\x01",
            "look on your faces?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B05():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B05)
    WaitChrThread(0x102, 1)

    def lambda_1B16():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B16)
    WaitChrThread(0x103, 1)

    def lambda_1B27():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1B27)
    WaitChrThread(0x109, 1)

    def lambda_1B38():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1B38)
    WaitChrThread(0x104, 1)

    def lambda_1B49():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1B49)
    WaitChrThread(0x105, 1)

    def lambda_1B5A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1B5A)

    ChrTalk(
        0x104,
        (
            "#00305FW-What's goin' on here?\x02\x03",
            "Even if we assume that\x01",
            "this is the old lady's\x01",
            "property...\x02\x03",
            "#00303FWe did talk to a little\x01",
            "girl just before, didn't\x01",
            "we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10306FI thought we did.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FWell just in case, let's\x01",
            "ask that girl from\x01",
            "before.\x02\x03",
            "Something might be going\x01",
            "on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FR-Right...\x02\x03",
            "#00001FI think she went into\x01",
            "the room further inside\x01",
            "past the living room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I say, don't ignore me\x01",
            "and continue your\x01",
            "conversation.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)

    def lambda_1D22():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D22)
    WaitChrThread(0x102, 1)

    def lambda_1D33():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1D33)
    WaitChrThread(0x103, 1)

    def lambda_1D44():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1D44)
    WaitChrThread(0x109, 1)

    def lambda_1D55():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D55)
    WaitChrThread(0x104, 1)

    def lambda_1D66():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1D66)
    WaitChrThread(0x105, 1)

    def lambda_1D77():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1D77)

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
            "#00005FW-What? Where did that\x01",
            "girl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FShe hidin' somewhere...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xA, 500)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105FL-Lloyd... Look at t-t-\x01",
            "those...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHuh...\x02",
    )

    CloseMessageWindow()

    def lambda_2037():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2037)
    Sleep(50)

    def lambda_2047():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2047)
    Sleep(50)

    def lambda_2057():
        TurnDirection(0x103, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2057)
    Sleep(50)

    def lambda_2067():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2067)
    Sleep(50)

    def lambda_2077():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2077)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    Sleep(50)

    def lambda_209E():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_209E)
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
            "#00005FThose dolls... One is\x01",
            "the one we delivered,\x01",
            "but...\x02\x03",
            "#00011FT-The other one...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301FThey're exactly the\x01",
            "same, aren't they.\x02",
        )
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
            "...You guys. Isn't it about\x01",
            "time you explained the\x01",
            "situation to me as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Depending on the\x01",
            "circumstances, I could sue you\x01",
            "for trespassing, you know?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_227C():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_227C)
    Sleep(50)

    def lambda_228C():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_228C)
    Sleep(50)

    def lambda_229C():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_229C)
    Sleep(50)

    def lambda_22AC():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_22AC)
    Sleep(50)

    def lambda_22BC():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_22BC)
    Sleep(50)

    def lambda_22CC():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_22CC)
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
            "Explained that they came to deliver a package\x01",
            "and that the girl who came to receive them\x01",
            "was identical to one of the dolls.\x07\x00\x02",
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
            "Something like he said\x01",
            "really did happen, then.\x02",
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
        "#10105FUmm... What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I bought one of the\x01",
            "dolls over there abroad\x01",
            "many, many years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They're said to be made in the\x01",
            "image of the daughters of an\x01",
            "old noble family somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I heard there were two in the set\x01",
            "because of the family's twin daughters,\x01",
            "but I could only acquire one of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Her quality isn't bad,\x01",
            "but strangely I couldn't\x01",
            "find a buyer for her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F...Umm, and what\x01",
            "relation does that have\x01",
            "with our story...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You're awfully slow,\x01",
            "aren't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In summary, both the doll you\x01",
            "delivered and the strange\x01",
            "girl that appeared...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Both of them may have\x01",
            "come to life.\x02",
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
            "There's a guy who's been\x01",
            "insisting for a long time that\x01",
            ""life dwells in dolls"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya, he may be\x01",
            "unexpectedly right.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2901")
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
            "◆The Doll Studio quest\x01",
            "in Zero? (Debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No Change]\x01",        # 0
            "[Cleared]\x01",          # 1
            "[Not Cleared]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28ED")
    OP_29(0x30, 0x4, 0x10)
    Jump("loc_2901")

    label("loc_28ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2901")
    OP_29(0x30, 0x3, 0x10)

    label("loc_2901")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_296B")

    ChrTalk(
        0x101,
        (
            "#00005FLife dwells in...\x02\x03",
            "#00003FI-Indeed, I feel like\x01",
            "Meister Jｶrg said that\x01",
            "once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29D2")

    label("loc_296B")


    ChrTalk(
        0x101,
        (
            "#00005FLife dwells in...\x02\x03",
            "#00006FAs you might imagine, I\x01",
            "think something like\x01",
            "that is impossible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29D2")


    ChrTalk(
        0x102,
        (
            "#00105FT-Then... It was some\x01",
            "kind of doll ghost!?\x02\x03",
            "#00106FN-No way...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A22():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2A22)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00203FWell, setting aside whether\x01",
            "the story's true...\x02\x03",
            "#00200FIt appears some kind of\x01",
            "spiritual "field" has formed\x01",
            "in this mansion.\x02\x03",
            "I feel the presence of the\x01",
            "higher elements, the same as\x01",
            "in the Tower and Temple...\x02\x03",
            "They may have caused some\x01",
            "kind of spiritual\x01",
            "phenomenon.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2B49():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B49)
    Sleep(50)

    def lambda_2B59():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2B59)
    Sleep(50)

    def lambda_2B69():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2B69)
    Sleep(50)

    def lambda_2B79():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2B79)
    Sleep(50)

    def lambda_2B89():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2B89)
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
            "#00301FI thought everything was\x01",
            "a little too\x01",
            "unbelievable, but...\x02\x03",
            "#00306FAfter what PeTiote said,\x01",
            "I think it's real.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112FIt feels unreal,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya! Those are some\x01",
            "impressive reactions.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2CBB():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2CBB)
    Sleep(50)

    def lambda_2CCB():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2CCB)
    Sleep(50)

    def lambda_2CDB():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2CDB)
    Sleep(50)

    def lambda_2CEB():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2CEB)
    Sleep(50)

    def lambda_2CFB():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2CFB)
    Sleep(50)

    def lambda_2D0B():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2D0B)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x8,
        (
            "Well in the end, it's just nonsense\x01",
            "from a recluse, so it's up to you\x01",
            "whether to believe it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "One thing is certain.\x02",
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
            "Now that those doll sisters\x01",
            "are together, I might finally\x01",
            "find a buyer for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ihya hya... What an\x01",
            "incredible find.\x02",
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
        (
            "#00306FWhat a blunt old lady\x01",
            "you are...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FW-Well, anyhow... With\x01",
            "this, we've finished\x01",
            "delivering the packages.\x02\x03",
            "#00000FLet's go report to the\x01",
            "Capua Express guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FR-Right. Let's hurry!\x02",
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

    # Function_5_7FD end

    def Function_6_2FD0(): pass

    label("Function_6_2FD0")


    def lambda_2FD5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2FD5)

    def lambda_2FE6():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FE6)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 3150, 0, 3230, 2000, 0x0)
    OP_93(0x101, 0x2D, 0x1F4)
    Return()

    # Function_6_2FD0 end

    def Function_7_301B(): pass

    label("Function_7_301B")


    def lambda_3020():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3020)

    def lambda_3031():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3031)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 3000, 0, 2100, 2000, 0x0)
    OP_93(0x102, 0x2D, 0x1F4)
    Return()

    # Function_7_301B end

    def Function_8_3066(): pass

    label("Function_8_3066")


    def lambda_306B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_306B)

    def lambda_307C():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_307C)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 2140, 0, 3620, 2000, 0x0)
    OP_93(0x103, 0x2D, 0x1F4)
    Return()

    # Function_8_3066 end

    def Function_9_30B1(): pass

    label("Function_9_30B1")


    def lambda_30B6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_30B6)

    def lambda_30C7():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_30C7)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 1840, 0, 2420, 2000, 0x0)
    OP_93(0x104, 0x2D, 0x1F4)
    Return()

    # Function_9_30B1 end

    def Function_10_30FC(): pass

    label("Function_10_30FC")


    def lambda_3101():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3101)

    def lambda_3112():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3112)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 900, 30, 2330, 2000, 0x0)
    OP_93(0x109, 0x2D, 0x1F4)
    Return()

    # Function_10_30FC end

    def Function_11_3147(): pass

    label("Function_11_3147")


    def lambda_314C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_314C)

    def lambda_315D():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_315D)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 1900, 30, 1240, 2000, 0x0)
    OP_93(0x105, 0x2D, 0x1F4)
    Return()

    # Function_11_3147 end

    def Function_12_3192(): pass

    label("Function_12_3192")

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

    # Function_12_3192 end

    def Function_13_31E7(): pass

    label("Function_13_31E7")


    def lambda_31EC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_31EC)

    def lambda_31FD():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_31FD)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 100000, 30, 4000, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_13_31E7 end

    def Function_14_3232(): pass

    label("Function_14_3232")


    def lambda_3237():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3237)

    def lambda_3248():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3248)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 98890, 30, 3530, 2000, 0x0)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_14_3232 end

    def Function_15_327D(): pass

    label("Function_15_327D")


    def lambda_3282():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3282)

    def lambda_3293():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3293)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 101030, 30, 3100, 2000, 0x0)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_15_327D end

    def Function_16_32C8(): pass

    label("Function_16_32C8")


    def lambda_32CD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_32CD)

    def lambda_32DE():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_32DE)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 99700, 30, 2800, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_16_32C8 end

    def Function_17_3313(): pass

    label("Function_17_3313")


    def lambda_3318():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3318)

    def lambda_3329():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3329)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 99500, 0, 1800, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_17_3313 end

    def Function_18_335E(): pass

    label("Function_18_335E")


    def lambda_3363():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3363)

    def lambda_3374():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3374)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 100860, 0, 1800, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_18_335E end

    def Function_19_33A9(): pass

    label("Function_19_33A9")


    def lambda_33AE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_33AE)

    def lambda_33BF():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_33BF)
    WaitChrThread(0x8, 1)
    OP_95(0x8, 100000, 0, 500, 2000, 0x0)
    Return()

    # Function_19_33A9 end

    SaveToFile()

Try(main)

from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1310_1.bin",                # FileName
        "t1310",                    # MapName
        "t1310",                    # Location
        0x00BD,                     # MapIndex
        "ed7161",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [440, 441, 705, 857, 1003, 1060, 1194, 1423, 1495, 0, 1545, 0, 3275, 3422, 3479, 3633, 0, 3690, 0, 227, 14, 0, 0],
    )

    BuildStringList((
        "t1310_1",                # 0
    ))

    ChipFrameInfo(440, 0)                                        # 0

    ScpFunction((
        "Function_0_1B8",          # 00, 0
        "Function_1_1B9",          # 01, 1
        "Function_2_2C1",          # 02, 2
        "Function_3_359",          # 03, 3
        "Function_4_3EB",          # 04, 4
        "Function_5_424",          # 05, 5
        "Function_6_4AA",          # 06, 6
        "Function_7_58F",          # 07, 7
        "Function_8_5D7",          # 08, 8
        "Function_9_609",          # 09, 9
        "Function_10_CCB",         # 0A, 10
        "Function_11_D5E",         # 0B, 11
        "Function_12_D97",         # 0C, 12
        "Function_13_E31",         # 0D, 13
        "Function_14_E6A",         # 0E, 14
        "Function_15_EE3",         # 0F, 15
        "Function_16_F7D",         # 10, 16
        "Function_17_FF2",         # 11, 17
        "Function_18_1043",        # 12, 18
        "Function_19_1115",        # 13, 19
        "Function_20_119D",        # 14, 20
        "Function_21_121C",        # 15, 21
        "Function_22_12FE",        # 16, 22
        "Function_23_1346",        # 17, 23
        "Function_24_1384",        # 18, 24
        "Function_25_1CAA",        # 19, 25
        "Function_26_1D3D",        # 1A, 26
        "Function_27_1D76",        # 1B, 27
        "Function_28_1E1C",        # 1C, 28
        "Function_29_1EB4",        # 1D, 29
        "Function_30_1EED",        # 1E, 30
        "Function_31_1F8C",        # 1F, 31
        "Function_32_1F8D",        # 20, 32
        "Function_33_1FF4",        # 21, 33
        "Function_34_208A",        # 22, 34
        "Function_35_20DC",        # 23, 35
        "Function_36_2148",        # 24, 36
        "Function_37_2163",        # 25, 37
        "Function_38_21BF",        # 26, 38
        "Function_39_21F1",        # 27, 39
        "Function_40_228E",        # 28, 40
        "Function_41_2313",        # 29, 41
        "Function_42_233E",        # 2A, 42
        "Function_43_2366",        # 2B, 43
        "Function_44_2410",        # 2C, 44
        "Function_45_246D",        # 2D, 45
        "Function_46_24F9",        # 2E, 46
        "Function_47_25DA",        # 2F, 47
        "Function_48_2622",        # 30, 48
        "Function_49_2666",        # 31, 49
        "Function_50_30D2",        # 32, 50
        "Function_51_3168",        # 33, 51
        "Function_52_31A1",        # 34, 52
        "Function_53_3223",        # 35, 53
        "Function_54_32B5",        # 36, 54
        "Function_55_32EE",        # 37, 55
        "Function_56_3356",        # 38, 56
        "Function_57_33ED",        # 39, 57
        "Function_58_3426",        # 3A, 58
        "Function_59_34A8",        # 3B, 59
        "Function_60_3543",        # 3C, 60
        "Function_61_35FC",        # 3D, 61
        "Function_62_3668",        # 3E, 62
        "Function_63_375F",        # 3F, 63
        "Function_64_37BB",        # 40, 64
        "Function_65_37F9",        # 41, 65
        "Function_66_3841",        # 42, 66
        "Function_67_38D5",        # 43, 67
        "Function_68_3913",        # 44, 68
        "Function_69_3998",        # 45, 69
        "Function_70_4296",        # 46, 70
        "Function_71_432B",        # 47, 71
        "Function_72_4364",        # 48, 72
        "Function_73_43F2",        # 49, 73
        "Function_74_448B",        # 4A, 74
        "Function_75_44BE",        # 4B, 75
        "Function_76_4507",        # 4C, 76
        "Function_77_456F",        # 4D, 77
        "Function_78_45A8",        # 4E, 78
        "Function_79_4675",        # 4F, 79
        "Function_80_4717",        # 50, 80
        "Function_81_476C",        # 51, 81
        "Function_82_47E9",        # 52, 82
        "Function_83_48D5",        # 53, 83
        "Function_84_4907",        # 54, 84
        "Function_85_4939",        # 55, 85
        "Function_86_499E",        # 56, 86
        "Function_87_4A08",        # 57, 87
        "Function_88_4AA8",        # 58, 88
    ))


    def Function_0_1B8(): pass

    label("Function_0_1B8")

    Return()

    # Function_0_1B8 end

    def Function_1_1B9(): pass

    label("Function_1_1B9")

    Call(1, 0)
    SetChrPos(0x11, 24500, -6000, -19000, 0)
    SetChrPos(0x12, 27500, -6000, -19000, 0)
    SetChrPos(0x10, 24500, -6000, -13000, 180)
    SetChrPos(0x13, 27500, -6000, -13000, 180)
    SetChrPos(0x14, 27500, -4000, -16000, 0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(330, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    OP_68(26000, -5000, -16000, 8000)
    MoveCamera(295, 30, 0, 8000)
    OP_6E(650, 8000)
    SetCameraDistance(17000, 8000)
    FadeToBright(1000, 0)
    BeginChrThread(0x12, 3, 1, 2)

    label("loc_2A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BD")
    Sleep(1)
    Jump("loc_2A6")

    label("loc_2BD")

    OP_6F(0x79)
    OP_0D()
    Return()

    # Function_1_1B9 end

    def Function_2_2C1(): pass

    label("Function_2_2C1")


    def lambda_2C6():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEC78, 0xFFFFB6F4, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2C6)
    SetChrFlags(0xFE, 0x20)

    def lambda_2E8():

        label("loc_2E8")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_2E8")

    QueueWorkItem2(0xFE, 2, lambda_2E8)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    ChrTalk(
        0x12,
        "#6P#5A─Randy!\x02",
    )


    def lambda_326():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF254, 0xFFFFBBA4, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_326)
    BeginChrThread(0x11, 3, 1, 3)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_2_2C1 end

    def Function_3_359(): pass

    label("Function_3_359")

    Sleep(500)
    Sound(809, 0, 100, 0)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    def lambda_374():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_374)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    Sound(442, 0, 90, 0)

    ChrTalk(
        0x11,
        "#5P#5AOraa!\x02",
    )


    def lambda_3AE():
        OP_96(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFCC0C, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3AE)
    BeginChrThread(0x10, 3, 1, 4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_3_359 end

    def Function_4_3EB(): pass

    label("Function_4_3EB")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_3FE():
        OP_9D(0xFE, 0x6A40, 0xFFFFEC78, 0xFFFFCD38, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3FE)
    BeginChrThread(0x13, 3, 1, 5)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_4_3EB end

    def Function_5_424(): pass

    label("Function_5_424")

    SetChrFlags(0xFE, 0x20)

    def lambda_42E():

        label("loc_42E")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_42E")

    QueueWorkItem2(0xFE, 2, lambda_42E)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    ChrTalk(
        0x13,
        "#12P#5AI leave it to you!\x02",
    )


    def lambda_477():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF254, 0xFFFFC694, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_477)
    BeginChrThread(0x10, 3, 1, 6)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_5_424 end

    def Function_6_4AA(): pass

    label("Function_6_4AA")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_4C5():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4C5)
    Sleep(600)

    ChrTalk(
        0x10,
        "#11P#4S#5AYah!!#3S\x02",
    )

    SetChrSubChip(0xFE, 0x1)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 700, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(442, 0, 100, 0)
    Sound(547, 0, 40, 0)
    BeginChrThread(0x14, 3, 1, 7)
    BeginChrThread(0x11, 3, 1, 8)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x11, 3)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_6_4AA end

    def Function_7_58F(): pass

    label("Function_7_58F")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x5AD2, 0xFFFFE890, 0xFFFFADF8, 0x4E20, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x54F6, 0xFFFFE890, 0xFFFF8FBC, 0x3E8, 0x7D0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_7_58F end

    def Function_8_5D7(): pass

    label("Function_8_5D7")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_8_5D7 end

    def Function_9_609(): pass

    label("Function_9_609")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetChrPos(0x101, 24500, -6000, -19000, 0)
    SetChrPos(0x11, 27500, -6000, -19000, 0)
    SetChrPos(0x12, 24500, -6000, -10000, 180)
    SetChrPos(0x13, 27500, -6000, -13000, 180)
    SetChrPos(0x10, 21300, -6000, -16000, 90)
    SetChrPos(0x14, 24500, -5500, -10200, 0)
    SetChrFlags(0x14, 0x8)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    OP_68(26000, -5000, -16000, 12000)
    MoveCamera(305, 30, 0, 12000)
    FadeToBright(1000, 0)
    OP_0D()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x12, 3, 1, 10)

    label("loc_701")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_718")
    Sleep(1)
    Jump("loc_701")

    label("loc_718")

    OP_4B(0x14, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Attack directly\x01",       # 0
            "Toss it to Randy\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_4C(0x14, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A04")
    MoveCamera(315, 25, 0, 1500)
    SetCameraDistance(15000, 1500)
    BeginChrThread(0x101, 3, 1, 18)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    ChrTalk(
        0x10,
        "#13400F#5P#NThere, it's out!!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12506F#6PDamn, I was too\x01",
            "impatient...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x13, 0xE1, 0x1F4)

    ChrTalk(
        0x13,
        "#12902FHehe, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#13006F#5P#NThat was close...\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        "#12500FSorry, Randy!\x02",
    )

    CloseMessageWindow()
    OP_93(0x11, 0x10E, 0x1F4)

    ChrTalk(
        0x11,
        (
            "#12800F#12PDon't worry! We'll\x01",
            "recover now!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(909, 0, 70, 0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x101, 24500, -6000, -19000, 0)
    SetChrPos(0x11, 27500, -6000, -20000, 0)
    SetChrPos(0x13, 24500, -6000, -12000, 180)
    SetChrPos(0x12, 27500, -6000, -13000, 180)
    SetChrFlags(0x14, 0x8)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x10,
        (
            "#13400F#5P...Game Set!!\x02\x03",
            "#13409FWazy and Noｱl are the\x01",
            "winners, 7 - 12!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12506F#6P*sigh*, we lost...\x02",
    )

    CloseMessageWindow()
    Jump("loc_CBF")

    label("loc_A04")

    OP_2C(0xA5, 0x1)
    MoveCamera(315, 25, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x101, 3, 1, 20)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    ChrTalk(
        0x10,
        "#13405F#5P#NOh, nice one, Randy.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)

    ChrTalk(
        0x12,
        "#13002F#11P#NGuh... Well done.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x13,
        (
            "#12906F#11PMan, it's hard being so\x01",
            "short.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0x10E, 0x1F4)

    ChrTalk(
        0x11,
        (
            "#12809F#12PNice toss Lloyd. Good\x01",
            "judgment as always.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#12509F#5PHaha. I'm just the\x01",
            "forward, though.\x02\x03",
            "#12500FAlright, let's get 'em\x01",
            "while they're down!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(909, 0, 70, 0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x101, 24500, -6000, -19000, 0)
    SetChrPos(0x11, 27500, -6000, -20000, 0)
    SetChrPos(0x13, 24500, -6000, -12000, 180)
    SetChrPos(0x12, 27500, -6000, -13000, 180)
    SetChrFlags(0x14, 0x8)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x10,
        (
            "#13400F#5P...Game Set!!\x02\x03",
            "#13409FWith a score of 12-8,\x01",
            "little bro and Randy are\x01",
            "the winners!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12500F#6PAlright, we won!!\x02",
    )

    CloseMessageWindow()

    label("loc_CBF")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_9_609 end

    def Function_10_CCB(): pass

    label("Function_10_CCB")

    ClearChrFlags(0x14, 0x8)
    Sound(802, 0, 60, 0)

    def lambda_CDB():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_CDB)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    Sound(441, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)

    ChrTalk(
        0x12,
        "#11P#5AHaa!\x02",
    )


    def lambda_D1D():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFB6F4, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_D1D)
    BeginChrThread(0x101, 3, 1, 11)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_10_CCB end

    def Function_11_D5E(): pass

    label("Function_11_D5E")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_D71():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEE6C, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_D71)
    BeginChrThread(0x11, 3, 1, 12)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_11_D5E end

    def Function_12_D97(): pass

    label("Function_12_D97")

    SetChrFlags(0xFE, 0x20)

    def lambda_DA1():

        label("loc_DA1")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_DA1")

    QueueWorkItem2(0xFE, 2, lambda_DA1)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    ChrTalk(
        0x11,
        "#6P#5AWhoa!\x02",
    )


    def lambda_DDC():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFCC0C, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_DDC)
    BeginChrThread(0x13, 3, 1, 13)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1500)
    SetChrChipByIndex(0xFE, 0x8)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_12_D97 end

    def Function_13_E31(): pass

    label("Function_13_E31")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_E44():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFCD38, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_E44)
    BeginChrThread(0x12, 3, 1, 14)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_13_E31 end

    def Function_14_E6A(): pass

    label("Function_14_E6A")

    SetChrFlags(0xFE, 0x20)

    def lambda_E74():

        label("loc_E74")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_E74")

    QueueWorkItem2(0xFE, 2, lambda_E74)
    Sleep(350)

    ChrTalk(
        0x12,
        "#11P#5AWazy!\x02",
    )

    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_EB0():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_EB0)
    BeginChrThread(0x13, 3, 1, 15)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_14_E6A end

    def Function_15_EE3(): pass

    label("Function_15_EE3")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0x13,
        "#11P#5AHmph...!\x02",
    )

    Sound(809, 0, 100, 0)

    def lambda_F12():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F12)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)

    def lambda_F3A():
        OP_98(0xFE, 0x0, 0xFFFFFCE0, 0xFFFFF830, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_F3A)
    BeginChrThread(0x11, 3, 1, 16)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sound(442, 0, 80, 0)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_15_EE3 end

    def Function_16_F7D(): pass

    label("Function_16_F7D")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)

    def lambda_F95():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F95)
    WaitChrThread(0x14, 1)

    def lambda_FB6():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFCD38, 0x3E8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_FB6)
    BeginChrThread(0x12, 3, 1, 17)
    Sound(441, 0, 80, 0)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_16_F7D end

    def Function_17_FF2(): pass

    label("Function_17_FF2")

    WaitChrThread(0x14, 1)
    SetChrFlags(0xFE, 0x20)
    OP_93(0xFE, 0xB4, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_1016():
        OP_9D(0xFE, 0x5FB4, 0xFFFFED40, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1016)
    Sleep(300)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_FF2 end

    def Function_18_1043(): pass

    label("Function_18_1043")

    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_105B():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBBA4, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_105B)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 100, 0)
    Sound(547, 0, 40, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 700, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x101,
        "#5P#5A#4SHaah!!#3S\x02",
    )

    BeginChrThread(0x14, 3, 1, 19)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x14, 3)
    Return()

    # Function_18_1043 end

    def Function_19_1115(): pass

    label("Function_19_1115")

    SetChrFlags(0x13, 0x20)

    def lambda_111F():

        label("loc_111F")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_111F")

    QueueWorkItem2(0x13, 2, lambda_111F)
    SetChrFlags(0x12, 0x20)

    def lambda_1136():

        label("loc_1136")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_1136")

    QueueWorkItem2(0x12, 2, lambda_1136)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x68F6, 0xFFFFE890, 0xFFFFDDBE, 0x4E20, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x7A76, 0xFFFFE868, 0x1B58, 0x9C4, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    EndChrThread(0x13, 0x2)
    ClearChrFlags(0x13, 0x20)
    EndChrThread(0x12, 0x2)
    ClearChrFlags(0x12, 0x20)
    Return()

    # Function_19_1115 end

    def Function_20_119D(): pass

    label("Function_20_119D")

    SetChrFlags(0xFE, 0x20)

    def lambda_11A7():

        label("loc_11A7")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_11A7")

    QueueWorkItem2(0xFE, 2, lambda_11A7)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    ChrTalk(
        0x101,
        "#5P#5APlease!!\x02",
    )


    def lambda_11E5():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFBF8C, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_11E5)
    BeginChrThread(0x11, 3, 1, 21)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x11, 3)
    Return()

    # Function_20_119D end

    def Function_21_121C(): pass

    label("Function_21_121C")

    Sleep(600)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_1237():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1237)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 100, 0)
    Sound(547, 0, 40, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 700, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x11,
        "#5P#5A#4SOraaaah!!#3S\x02",
    )

    BeginChrThread(0x14, 3, 1, 22)
    BeginChrThread(0x13, 3, 1, 23)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x13, 3)
    Return()

    # Function_21_121C end

    def Function_22_12FE(): pass

    label("Function_22_12FE")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x6F9A, 0xFFFFE890, 0xFFFFCCCA, 0x4E20, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x7F76, 0xFFFFE7F0, 0x762, 0x1388, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_22_12FE end

    def Function_23_1346(): pass

    label("Function_23_1346")

    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_23_1346 end

    def Function_24_1384(): pass

    label("Function_24_1384")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetChrPos(0x101, 27500, -6000, -19000, 0)
    SetChrPos(0x12, 24500, -6000, -19000, 0)
    SetChrPos(0x10, 24500, -6000, -10000, 180)
    SetChrPos(0x13, 27500, -6000, -13000, 180)
    SetChrPos(0x11, 21300, -6000, -16000, 90)
    SetChrPos(0x14, 24500, -5500, -10200, 0)
    SetChrFlags(0x14, 0x8)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    OP_68(26000, -5000, -16000, 13000)
    MoveCamera(305, 30, 0, 13000)
    FadeToBright(1000, 0)
    OP_0D()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x10, 3, 1, 25)

    label("loc_147C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1493")
    Sleep(1)
    Jump("loc_147C")

    label("loc_1493")

    OP_4B(0x14, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Anticipate attack and block\x01",        # 0
            "Anticipate bump and fall back\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_4C(0x14, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18C8")
    MoveCamera(315, 25, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x13, 3, 1, 39)
    WaitChrThread(0x13, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    ChrTalk(
        0x11,
        (
            "#12809F#5P#NPoint, Ilya's team!\x02\x03",
            "#12803FStill, seriously Wazy...\x01",
            "That was a crafty thing\x01",
            "you did there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    OP_93(0x13, 0x10E, 0x1F4)

    ChrTalk(
        0x13,
        (
            "#12902F#12PHehe, don't ruin my\x01",
            "reputation. This a\x01",
            "strategy too, you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x87, 0x1F4)

    ChrTalk(
        0x10,
        (
            "#13404F#5PWell, this might be the ideal\x01",
            "strategy for our opponents,\x01",
            "the "serious" team, you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_93(0x12, 0x5A, 0x1F4)

    ChrTalk(
        0x12,
        (
            "#13001F#5PLloyd... They're saying\x01",
            "that to us!?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#12510F#12PGuh... As if I'd lose here!\x02\x03",
            "#12501FThis being the situation, it's\x01",
            "guts time, Noｱl! I'm gonna\x01",
            "catch that ball at all costs!!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(909, 0, 70, 0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x101, 27500, -6000, -19000, 0)
    SetChrPos(0x12, 24500, -6000, -19000, 0)
    SetChrPos(0x10, 24500, -6000, -13000, 180)
    SetChrPos(0x13, 27500, -6000, -13000, 180)
    SetChrFlags(0x14, 0x8)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x11,
        (
            "#12800F#5P...Game Set!!\x02\x03",
            "#12809FIlya and Wazy are the\x01",
            "winners, 3 - 12!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12506F#6PGuh... No good, huh...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C9E")

    label("loc_18C8")

    OP_2C(0xA5, 0x1)
    MoveCamera(315, 25, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x13, 3, 1, 43)
    WaitChrThread(0x13, 3)
    Sleep(600)
    Sound(909, 0, 70, 0)
    Sleep(500)

    ChrTalk(
        0x11,
        (
            "#12800F#5P#NPoint, Lloyd's team!\x02\x03",
            "#12809FHaha, nice work!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)

    ChrTalk(
        0x13,
        (
            "#12906F#11PMan, to think you could\x01",
            "read us.\x02\x03",
            "#12902FThey're the serious\x01",
            "team! Can't we do\x01",
            "anything against them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12502F#6PWith your personality, Wazy,\x01",
            "I knew you'd try to outsmart\x01",
            "us in that situation.\x02\x03",
            "#12504FYou have to know your enemy.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x12, 0x5A, 0x1F4)

    ChrTalk(
        0x12,
        "#13000F#5PWe did it, Lloyd!\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0x5A, 0x1F4)

    ChrTalk(
        0x10,
        (
            "#13400F#5PHaha. Don't lay it on\x01",
            "too thick, alright?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#12904FHaha, yeah, seriously.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#12500F#12PAlright, Noｱl! Let's\x01",
            "take control of the\x01",
            "game, just like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#13009F#5PRoger that!!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(909, 0, 70, 0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x101, 27500, -6000, -19000, 0)
    SetChrPos(0x12, 24500, -6000, -19000, 0)
    SetChrPos(0x10, 24500, -6000, -13000, 180)
    SetChrPos(0x13, 27500, -6000, -13000, 180)
    SetChrFlags(0x14, 0x8)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x11,
        (
            "#12800F#5P...Game Set!!\x02\x03",
            "#12809FWith a score of 12-11,\x01",
            "Lloyd and Noｱl are the\x01",
            "winners!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12512F#6PW-We did it... We just\x01",
            "barely won!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C9E")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_24_1384 end

    def Function_25_1CAA(): pass

    label("Function_25_1CAA")

    ClearChrFlags(0x14, 0x8)
    Sound(802, 0, 60, 0)

    def lambda_1CBA():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1CBA)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    ChrTalk(
        0x10,
        "#11P#5AHop!\x02",
    )


    def lambda_1CFC():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFB6F4, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1CFC)
    BeginChrThread(0x12, 3, 1, 26)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_1CAA end

    def Function_26_1D3D(): pass

    label("Function_26_1D3D")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_1D50():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEDA4, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1D50)
    BeginChrThread(0x101, 3, 1, 27)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_26_1D3D end

    def Function_27_1D76(): pass

    label("Function_27_1D76")

    SetChrFlags(0xFE, 0x20)

    def lambda_1D80():

        label("loc_1D80")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_1D80")

    QueueWorkItem2(0xFE, 2, lambda_1D80)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 60, 0)

    ChrTalk(
        0x101,
        "#6P#5ANoｱl!\x02",
    )


    def lambda_1DBB():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFBBA4, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1DBB)
    BeginChrThread(0x12, 3, 1, 28)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1500)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_27_1D76 end

    def Function_28_1E1C(): pass

    label("Function_28_1E1C")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_1E37():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1E37)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 80, 0)

    ChrTalk(
        0x12,
        "#5P#5AHaah!!!\x02",
    )


    def lambda_1E77():
        OP_96(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFCC0C, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1E77)
    BeginChrThread(0x13, 3, 1, 29)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_28_1E1C end

    def Function_29_1EB4(): pass

    label("Function_29_1EB4")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_1EC7():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFC75C, 0xC80, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1EC7)
    BeginChrThread(0x10, 3, 1, 30)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_29_1EB4 end

    def Function_30_1EED(): pass

    label("Function_30_1EED")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0x10,
        "#11P#5AToryah!\x02",
    )

    Sound(809, 0, 100, 0)

    def lambda_1F1B():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1F1B)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 80, 0)

    def lambda_1F49():
        OP_96(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFB30C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1F49)
    BeginChrThread(0x12, 3, 1, 31)
    BeginChrThread(0x101, 3, 1, 32)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_30_1EED end

    def Function_31_1F8C(): pass

    label("Function_31_1F8C")

    Return()

    # Function_31_1F8C end

    def Function_32_1F8D(): pass

    label("Function_32_1F8D")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_1FA0():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFBD98, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1FA0)
    BeginChrThread(0x12, 3, 1, 33)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_98(0xFE, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_32_1F8D end

    def Function_33_1FF4(): pass

    label("Function_33_1FF4")

    SetChrFlags(0xFE, 0x20)

    def lambda_1FFE():

        label("loc_1FFE")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_1FFE")

    QueueWorkItem2(0xFE, 2, lambda_1FFE)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_2029():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFCC0C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2029)
    BeginChrThread(0x13, 3, 1, 34)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1700)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_98(0xFE, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_33_1FF4 end

    def Function_34_208A(): pass

    label("Function_34_208A")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    ChrTalk(
        0x13,
        "#12P#5AHere I go...!\x02",
    )


    def lambda_20B6():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFC568, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_20B6)
    BeginChrThread(0x10, 3, 1, 35)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_34_208A end

    def Function_35_20DC(): pass

    label("Function_35_20DC")

    SetChrFlags(0xFE, 0x20)

    def lambda_20E6():

        label("loc_20E6")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_20E6")

    QueueWorkItem2(0xFE, 2, lambda_20E6)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_2111():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2111)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_35_20DC end

    def Function_36_2148(): pass

    label("Function_36_2148")

    Sleep(500)
    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_36_2148 end

    def Function_37_2163(): pass

    label("Function_37_2163")

    BeginChrThread(0x10, 3, 1, 36)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_98(0xFE, 0x0, 0x0, 0x5DC, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_37_2163 end

    def Function_38_21BF(): pass

    label("Function_38_21BF")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_38_21BF end

    def Function_39_21F1(): pass

    label("Function_39_21F1")

    BeginChrThread(0x101, 3, 1, 37)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_220F():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_220F)
    Sleep(600)

    ChrTalk(
        0x13,
        "#12P#5A─Just kidding♪\x02",
    )

    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    BeginChrThread(0x14, 3, 1, 40)
    BeginChrThread(0x12, 3, 1, 38)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sound(441, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x12, 3)
    Return()

    # Function_39_21F1 end

    def Function_40_228E(): pass

    label("Function_40_228E")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_9D(0xFE, 0x639C, 0xFFFFE890, 0xFFFFAC04, 0x7D0, 0x3E8)
    Sound(443, 0, 40, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x639C, 0xFFFFE890, 0xFFFFA628, 0x3E8, 0x3E8)
    Sound(441, 0, 60, 0)
    OP_9D(0xFE, 0x639C, 0xFFFFE890, 0xFFFFA240, 0x1F4, 0x3E8)
    Sound(441, 0, 40, 0)
    OP_9D(0xFE, 0x639C, 0xFFFFE890, 0xFFFFA04C, 0xC8, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_40_228E end

    def Function_41_2313(): pass

    label("Function_41_2313")

    BeginChrThread(0x10, 3, 1, 36)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_98(0xFE, 0x0, 0x0, 0xFFFFF830, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_41_2313 end

    def Function_42_233E(): pass

    label("Function_42_233E")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_42_233E end

    def Function_43_2366(): pass

    label("Function_43_2366")

    BeginChrThread(0x101, 3, 1, 41)
    BeginChrThread(0x12, 3, 1, 42)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_238A():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_238A)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)

    ChrTalk(
        0x13,
        "#12P#5AWhat...!?\x02",
    )


    def lambda_23C7():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFB118, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_23C7)
    BeginChrThread(0x101, 3, 1, 44)
    Sleep(100)
    Sound(441, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Sleep(5500)
    Return()

    # Function_43_2366 end

    def Function_44_2410(): pass

    label("Function_44_2410")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_2423():
        OP_9D(0xFE, 0x6590, 0xFFFFEC78, 0xFFFFB9B0, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2423)
    BeginChrThread(0x12, 3, 1, 45)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_98(0xFE, 0x0, 0x0, 0x5DC, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_44_2410 end

    def Function_45_246D(): pass

    label("Function_45_246D")

    SetChrFlags(0xFE, 0x20)

    def lambda_2477():

        label("loc_2477")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_2477")

    QueueWorkItem2(0xFE, 2, lambda_2477)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_24A2():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFBBA4, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_24A2)
    BeginChrThread(0x101, 3, 1, 46)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    OP_98(0x10, 0x0, 0x0, 0x5DC, 0xFA0, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    Return()

    # Function_45_246D end

    def Function_46_24F9(): pass

    label("Function_46_24F9")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0x101,
        "#5P#5A#4SUwooooh!#3S\x02",
    )

    Sound(809, 0, 100, 0)

    def lambda_252D():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_252D)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 100, 0)
    Sound(547, 0, 40, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 700, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x14, 3, 1, 47)
    BeginChrThread(0x13, 3, 1, 48)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x13, 3)
    Return()

    # Function_46_24F9 end

    def Function_47_25DA(): pass

    label("Function_47_25DA")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x6658, 0xFFFFE890, 0xFFFFCE5A, 0x4E20, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x774C, 0xFFFFE890, 0xFFFFFA9C, 0x1388, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_47_25DA end

    def Function_48_2622(): pass

    label("Function_48_2622")

    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    Sound(441, 0, 80, 0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_48_2622 end

    def Function_49_2666(): pass

    label("Function_49_2666")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetChrPos(0x101, 24500, -6000, -19000, 0)
    SetChrPos(0x13, 27500, -6000, -22000, 0)
    SetChrPos(0x11, 24500, -6000, -13000, 180)
    SetChrPos(0x10, 27500, -6000, -13000, 180)
    SetChrPos(0x12, 21300, -6000, -16000, 90)
    SetChrPos(0x14, 27500, -5500, -21800, 0)
    SetChrFlags(0x14, 0x8)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    OP_68(26000, -5000, -16000, 15000)
    MoveCamera(305, 30, 0, 15000)
    FadeToBright(1000, 0)
    OP_0D()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x13, 3, 1, 50)

    label("loc_275E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2775")
    Sleep(1)
    Jump("loc_275E")

    label("loc_2775")

    OP_4B(0x14, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Powerful blow between Ilya and Randy\x01",      # 0
            "Drop it onto the Line\x01",                     # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_4C(0x14, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CD4")
    MoveCamera(315, 25, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x101, 3, 1, 62)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    ChrTalk(
        0x12,
        "#13002F#5P#NPoint, Ilya's team!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    OP_93(0x11, 0x5A, 0x1F4)

    ChrTalk(
        0x11,
        (
            "#12809F#5PAlright!! As expected\x01",
            "from Ilya!!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x10E, 0x1F4)

    ChrTalk(
        0x10,
        (
            "#13400F#12PAhaha, is that all\x01",
            "they've got?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12906F#12P#NOh man. Did you think you could\x01",
            "win against their team's physical\x01",
            "abilities with a frontal attack?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_2950():
        OP_93(0x11, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_2950)
    Sleep(30)

    def lambda_2960():
        OP_93(0x10, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2960)
    Sleep(30)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x10, 0)
    OP_93(0x101, 0x87, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#12506F#5PWell, I feel ashamed...\x02\x03",
            "#12505F...Even so, Wazy. What\x01",
            "did that "lie" mean just\x01",
            "now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12900F#12P#NWell, because Ilya was likely\x01",
            "coming to block, even a powerful\x01",
            "blow would've been useless.\x02\x03",
            "#12904FWith "lie" I meant "line"... In\x01",
            "short, I was telling you to drop\x01",
            "it onto the line.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12506F#5PNow look here... How could\x01",
            "I ever get that when you\x01",
            "told me all of a sudden!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12909F#12P#NAhaha, my bad, my bad.\x02\x03",
            "#12900FWell, let's pull ourselves\x01",
            "together and make a\x01",
            "comeback from behind, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(909, 0, 70, 0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x101, 24500, -6000, -19000, 0)
    SetChrPos(0x13, 27500, -6000, -20000, 0)
    SetChrPos(0x11, 24500, -6000, -12000, 180)
    SetChrPos(0x10, 27500, -6000, -13000, 180)
    SetChrFlags(0x14, 0x8)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x12,
        (
            "#13000F#5P...Game Set!!\x02\x03",
            "#13009FIlya and Randy are the\x01",
            "winners, 4 - 12!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12506F#6P*sigh*, we failed...\x02",
    )

    CloseMessageWindow()
    Jump("loc_30C6")

    label("loc_2CD4")

    OP_2C(0xA5, 0x1)
    BeginChrThread(0x101, 3, 1, 66)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    ChrTalk(
        0x12,
        "#13002F#5P#NPoint, Lloyd's team!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)

    ChrTalk(
        0x101,
        "#12500F#6PAlright!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13406F#11POh no... a feint? I\x01",
            "thought a powerful blow\x01",
            "coming for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#12806F#11PMan, they outsmarted us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12902F#6P#NHehe, that was a good\x01",
            "performance.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x87, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#12504F#11P...Yeah, thanks to your\x01",
            ""lie" signal, Wazy.\x02\x03",
            "#12502FI noticed the empty\x01",
            "sideline and suddenly\x01",
            "switched.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12904F#6P#NHehe. I was sudden, so I\x01",
            "wondered whether you'd\x01",
            "get it.\x02\x03",
            "#12909FCould it be a move made\x01",
            "possible by love?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#12506F#11PDon't be ridiculous.\x02\x03",
            "#12500FAlright, let's keep attacking\x01",
            "their weak points and quick\x01",
            "work of Ilya and Randy!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(909, 0, 70, 0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x101, 24500, -6000, -19000, 0)
    SetChrPos(0x13, 27500, -6000, -20000, 0)
    SetChrPos(0x11, 24500, -6000, -12000, 180)
    SetChrPos(0x10, 27500, -6000, -13000, 180)
    SetChrFlags(0x14, 0x8)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x12,
        (
            "#13000F#5P...Game Set!!\x02\x03",
            "#13009FLloyd and Wazy are the\x01",
            "winners, 12 - 10!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12509F#6PAlright, we managed to\x01",
            "win!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30C6")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_49_2666 end

    def Function_50_30D2(): pass

    label("Function_50_30D2")

    ClearChrFlags(0x14, 0x8)
    Sound(802, 0, 60, 0)

    def lambda_30E2():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_30E2)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    ChrTalk(
        0x13,
        "#6P#5AHmph...!\x02",
    )


    def lambda_3127():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFCC0C, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3127)
    BeginChrThread(0x10, 3, 1, 51)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0xA)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_50_30D2 end

    def Function_51_3168(): pass

    label("Function_51_3168")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_317B():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEDA4, 0xFFFFCD38, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_317B)
    BeginChrThread(0x11, 3, 1, 52)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_51_3168 end

    def Function_52_31A1(): pass

    label("Function_52_31A1")

    SetChrFlags(0xFE, 0x20)

    def lambda_31AB():

        label("loc_31AB")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_31AB")

    QueueWorkItem2(0xFE, 2, lambda_31AB)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 60, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_31D6():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_31D6)
    BeginChrThread(0x10, 3, 1, 53)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x8)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_52_31A1 end

    def Function_53_3223(): pass

    label("Function_53_3223")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_323E():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_323E)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    Sound(442, 0, 80, 0)
    EndChrThread(0x14, 0x1)

    ChrTalk(
        0x10,
        "#11P#5AThere!\x02",
    )


    def lambda_327E():
        OP_96(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFB6F4, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_327E)
    BeginChrThread(0x101, 3, 1, 54)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_53_3223 end

    def Function_54_32B5(): pass

    label("Function_54_32B5")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_32C8():
        OP_9D(0xFE, 0x6B6C, 0xFFFFED40, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_32C8)
    BeginChrThread(0x13, 3, 1, 55)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_54_32B5 end

    def Function_55_32EE(): pass

    label("Function_55_32EE")

    SetChrFlags(0xFE, 0x20)

    def lambda_32F8():

        label("loc_32F8")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_32F8")

    QueueWorkItem2(0xFE, 2, lambda_32F8)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 80, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_3323():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFBBA4, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3323)
    BeginChrThread(0x101, 3, 1, 56)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_55_32EE end

    def Function_56_3356(): pass

    label("Function_56_3356")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_3371():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3371)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 80, 0)

    ChrTalk(
        0x101,
        "#5P#5ABack at you!\x02",
    )


    def lambda_33B6():
        OP_96(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFCC0C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_33B6)
    BeginChrThread(0x11, 3, 1, 57)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_56_3356 end

    def Function_57_33ED(): pass

    label("Function_57_33ED")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_3400():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEC78, 0xFFFFC568, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3400)
    BeginChrThread(0x10, 3, 1, 58)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_57_33ED end

    def Function_58_3426(): pass

    label("Function_58_3426")

    SetChrFlags(0xFE, 0x20)

    def lambda_3430():

        label("loc_3430")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_3430")

    QueueWorkItem2(0xFE, 2, lambda_3430)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 80, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_345B():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_345B)
    BeginChrThread(0x11, 3, 1, 59)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_58_3426 end

    def Function_59_34A8(): pass

    label("Function_59_34A8")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_34C3():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_34C3)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)

    ChrTalk(
        0x11,
        "#11P#5AEat this!\x02",
    )


    def lambda_3500():
        OP_96(0xFE, 0x5FB4, 0xFFFFF254, 0xFFFFBF8C, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3500)
    BeginChrThread(0x101, 3, 1, 60)
    Sleep(100)
    Sound(442, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_59_34A8 end

    def Function_60_3543(): pass

    label("Function_60_3543")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)

    def lambda_355B():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_355B)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 60, 0)

    def lambda_3582():
        OP_9D(0xFE, 0x6B6C, 0xFFFFED40, 0xFFFFB5C8, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3582)
    BeginChrThread(0x13, 3, 1, 61)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)

    ChrTalk(
        0x13,
        "#6P#5ALie!\x02",
    )

    Sleep(500)
    SetChrFlags(0x10, 0x20)
    OP_93(0x10, 0xB4, 0x1F4)
    ClearChrFlags(0x10, 0x20)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    OP_98(0x10, 0xFFFFFA24, 0x0, 0x0, 0xFA0, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    Return()

    # Function_60_3543 end

    def Function_61_35FC(): pass

    label("Function_61_35FC")

    SetChrFlags(0xFE, 0x20)

    def lambda_3606():

        label("loc_3606")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_3606")

    QueueWorkItem2(0xFE, 2, lambda_3606)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_3631():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFBF8C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3631)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_61_35FC end

    def Function_62_3668(): pass

    label("Function_62_3668")

    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_3680():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3680)
    Sleep(600)

    ChrTalk(
        0x101,
        "#5P#5A#4S...Haah!#3S\x02",
    )

    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 100, 0)
    Sound(547, 0, 40, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 700, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3715():
        OP_96(0xFE, 0x6590, 0xFFFFF060, 0xFFFFC374, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3715)
    BeginChrThread(0x11, 3, 1, 64)
    Sleep(30)
    BeginChrThread(0x10, 3, 1, 63)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x10, 3)
    Return()

    # Function_62_3668 end

    def Function_63_375F(): pass

    label("Function_63_375F")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)

    def lambda_3777():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3777)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 80, 0)
    BeginChrThread(0x14, 3, 1, 65)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x14, 3)
    Return()

    # Function_63_375F end

    def Function_64_37BB(): pass

    label("Function_64_37BB")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x1388)
    Sound(809, 0, 100, 0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_64_37BB end

    def Function_65_37F9(): pass

    label("Function_65_37F9")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x6FB8, 0xFFFFE890, 0xFFFFBA00, 0x3A98, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 100, 0)
    OP_9D(0xFE, 0x7CC4, 0xFFFFE890, 0xFFFFAB50, 0xBB8, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_65_37F9 end

    def Function_66_3841(): pass

    label("Function_66_3841")

    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_3859():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3859)
    Sleep(600)

    ChrTalk(
        0x101,
        "#6P#5A#4S...Hah!#3S\x02",
    )

    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(441, 0, 100, 0)
    BeginChrThread(0x14, 3, 1, 68)
    BeginChrThread(0x11, 3, 1, 64)
    Sleep(30)
    BeginChrThread(0x10, 3, 1, 67)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x14, 3)
    Return()

    # Function_66_3841 end

    def Function_67_38D5(): pass

    label("Function_67_38D5")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x1388)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x18)
    Sound(30, 0, 100, 0)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_67_38D5 end

    def Function_68_3913(): pass

    label("Function_68_3913")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_9D(0xFE, 0x639C, 0xFFFFE890, 0xFFFFD508, 0x7D0, 0x3E8)
    Sound(443, 0, 50, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x639C, 0xFFFFE890, 0xFFFFDAE4, 0x3E8, 0x3E8)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x639C, 0xFFFFE890, 0xFFFFDECC, 0x1F4, 0x3E8)
    Sound(441, 0, 60, 0)
    OP_9D(0xFE, 0x639C, 0xFFFFE890, 0xFFFFE0C0, 0xC8, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_68_3913 end

    def Function_69_3998(): pass

    label("Function_69_3998")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetChrPos(0x101, 24500, -6000, -22000, 0)
    SetChrPos(0x10, 27500, -6000, -19000, 0)
    SetChrPos(0x11, 24500, -6000, -13000, 180)
    SetChrPos(0x12, 27500, -6000, -13000, 180)
    SetChrPos(0x13, 21300, -6000, -16000, 90)
    SetChrPos(0x14, 24500, -5500, -21800, 0)
    SetChrFlags(0x14, 0x8)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    OP_68(26000, -5000, -16000, 15000)
    MoveCamera(305, 30, 0, 15000)
    FadeToBright(1000, 0)
    OP_0D()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x101, 3, 1, 70)

    label("loc_3A90")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AA7")
    Sleep(1)
    Jump("loc_3A90")

    label("loc_3AA7")

    OP_4B(0x14, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Use all your strength and toss it high\x01",      # 0
            "Control your strength and toss it low\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_4C(0x14, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F02")
    OP_2C(0xA5, 0x1)
    MoveCamera(315, 25, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x101, 3, 1, 81)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    ChrTalk(
        0x13,
        "#12902F#5P#NHehe, well done.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    OP_63(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x11,
        (
            "#12806FA-As expected from Miss\x01",
            "Ilya... She's got cheating-\x01",
            "level physical abilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13006FSuch a crazy height... I\x01",
            "never could have blocked\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    ChrTalk(
        0x10,
        "#13409F#6PHehe, all too easy.\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0xE1, 0x1F4)

    ChrTalk(
        0x10,
        (
            "#13400F#12PLittle bro, that high\x01",
            "toss was well done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12500F#5PHaha. With your physical\x01",
            "abilities, I thought\x01",
            "that might work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#13409F#12PHehe, excellent,\x01",
            "excellent♪\x02\x03",
            "#13400FC'mon, let's keep it up\x01",
            "and win the game in a\x01",
            "flash!!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(909, 0, 70, 0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x101, 24500, -6000, -19000, 0)
    SetChrPos(0x10, 27500, -6000, -20000, 0)
    SetChrPos(0x11, 24500, -6000, -12000, 180)
    SetChrPos(0x12, 27500, -6000, -13000, 180)
    SetChrFlags(0x14, 0x8)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x13,
        (
            "#12900F#5P#N...Game Set!!\x02\x03",
            "#12904FLloyd and Ilya are the\x01",
            "winners, 12 - 4. Hehe,\x01",
            "good job.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#12509F#6PAlright, it's complete\x01",
            "victory!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_428A")

    label("loc_3F02")

    MoveCamera(315, 25, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x101, 3, 1, 86)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    ChrTalk(
        0x13,
        (
            "#12902F#5P#NHehe, too bad. You\x01",
            "missed that chance.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)

    ChrTalk(
        0x11,
        "#12806FWhew, that was close!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#13011FStill, what a powerful\x01",
            "jump...\x02\x03",
            "#13006FIf we had gotten attacked at\x01",
            "such a height, there's no\x01",
            "way we could have defended.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_93(0x10, 0xE1, 0x1F4)

    ChrTalk(
        0x10,
        (
            "#13406F#12POh no... Sorry, little\x01",
            "bro.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12512FNo, likewise... I didn't\x01",
            "think you'd jump that\x01",
            "high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12800FHaha, it seems the Goddess\x01",
            "is smilin' on us. Let's get\x01",
            "this done in a flash, Noｱl!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#13009FYes, sir!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(909, 0, 70, 0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x101, 24500, -6000, -19000, 0)
    SetChrPos(0x10, 27500, -6000, -20000, 0)
    SetChrPos(0x11, 24500, -6000, -12000, 180)
    SetChrPos(0x12, 27500, -6000, -13000, 180)
    SetChrFlags(0x14, 0x8)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x13,
        (
            "#12900F#5P...Game Set!!\x02\x03",
            "#12904FRandy and Noｱl are the\x01",
            "winners, 9 - 12. Hehe,\x01",
            "good job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12506F#6PGuh. We lost, huh...?\x02",
    )

    CloseMessageWindow()

    label("loc_428A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_69_3998 end

    def Function_70_4296(): pass

    label("Function_70_4296")

    ClearChrFlags(0x14, 0x8)
    Sound(802, 0, 60, 0)

    def lambda_42A6():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_42A6)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    ChrTalk(
        0x101,
        "#5P#5A...Hah!\x02",
    )


    def lambda_42EA():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFCC70, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_42EA)
    BeginChrThread(0x11, 3, 1, 71)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_70_4296 end

    def Function_71_432B(): pass

    label("Function_71_432B")

    WaitChrThread(0x14, 1)
    Sound(441, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_433E():
        OP_9D(0xFE, 0x6AA4, 0xFFFFEC78, 0xFFFFCD38, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_433E)
    BeginChrThread(0x12, 3, 1, 72)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_71_432B end

    def Function_72_4364(): pass

    label("Function_72_4364")

    SetChrFlags(0xFE, 0x20)

    def lambda_436E():

        label("loc_436E")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_436E")

    QueueWorkItem2(0xFE, 2, lambda_436E)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 80, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_4399():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4399)
    BeginChrThread(0x11, 3, 1, 73)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x1, 0x10, 0x0, 0xFFFFFA24, 0xFA0, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    Return()

    # Function_72_4364 end

    def Function_73_43F2(): pass

    label("Function_73_43F2")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0x11,
        "#11P#5AAttack!\x02",
    )

    Sound(809, 0, 100, 0)

    def lambda_4420():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4420)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)

    def lambda_4448():
        OP_96(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFB6F4, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4448)
    BeginChrThread(0x101, 3, 1, 74)
    Sleep(100)
    Sound(442, 0, 80, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_73_43F2 end

    def Function_74_448B(): pass

    label("Function_74_448B")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)

    def lambda_4498():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFB0B4, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4498)
    BeginChrThread(0x10, 3, 1, 75)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_74_448B end

    def Function_75_44BE(): pass

    label("Function_75_44BE")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    ChrTalk(
        0x10,
        "#6P#5AHere!\x02",
    )


    def lambda_44E1():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_44E1)
    BeginChrThread(0x101, 3, 1, 76)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_75_44BE end

    def Function_76_4507(): pass

    label("Function_76_4507")

    SetChrFlags(0xFE, 0x20)

    def lambda_4511():

        label("loc_4511")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_4511")

    QueueWorkItem2(0xFE, 2, lambda_4511)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 60, 0)

    def lambda_453C():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFCC0C, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_453C)
    BeginChrThread(0x12, 3, 1, 77)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_76_4507 end

    def Function_77_456F(): pass

    label("Function_77_456F")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_4582():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFC568, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4582)
    BeginChrThread(0x11, 3, 1, 78)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_77_456F end

    def Function_78_45A8(): pass

    label("Function_78_45A8")

    SetChrFlags(0xFE, 0x20)

    def lambda_45B2():

        label("loc_45B2")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_45B2")

    QueueWorkItem2(0xFE, 2, lambda_45B2)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    ChrTalk(
        0x11,
        "#11P#5AGooo!\x02",
    )


    def lambda_45EE():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_45EE)
    BeginChrThread(0x12, 3, 1, 79)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    OP_9B(0x1, 0x10, 0x0, 0x5DC, 0xFA0, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x11, 0x20)
    OP_93(0x11, 0xB4, 0x1F4)
    ClearChrFlags(0x11, 0x20)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    OP_98(0x11, 0x5DC, 0x0, 0x0, 0xFA0, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    Return()

    # Function_78_45A8 end

    def Function_79_4675(): pass

    label("Function_79_4675")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_4690():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4690)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)

    ChrTalk(
        0x12,
        "#11P#5AHow about this!?\x02",
    )

    Sound(442, 0, 80, 0)

    def lambda_46DA():
        OP_96(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFB6F4, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_46DA)
    BeginChrThread(0x10, 3, 1, 80)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_79_4675 end

    def Function_80_4717(): pass

    label("Function_80_4717")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_472A():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_472A)
    SetChrFlags(0x101, 0x20)
    OP_93(0x101, 0x5A, 0x1F4)
    ClearChrFlags(0x101, 0x20)
    Sleep(300)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    EndChrThread(0x101, 0x2)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_80_4717 end

    def Function_81_476C(): pass

    label("Function_81_476C")


    ChrTalk(
        0x101,
        "#5P#5AIlya!!\x02",
    )

    SetChrFlags(0xFE, 0x20)

    def lambda_4787():

        label("loc_4787")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_4787")

    QueueWorkItem2(0xFE, 2, lambda_4787)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_47B2():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFBBA4, 0xCE4, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_47B2)
    BeginChrThread(0x10, 3, 1, 82)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x10, 3)
    Return()

    # Function_81_476C end

    def Function_82_47E9(): pass

    label("Function_82_47E9")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0x10,
        "#5P#5A#4SHaaaaaa!!#3S\x02",
    )

    Sound(809, 0, 100, 0)

    def lambda_481E():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFBD98, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_481E)
    Sleep(700)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 100, 0)
    Sound(547, 0, 40, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 700, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x14, 3, 1, 85)
    BeginChrThread(0x11, 3, 1, 83)
    BeginChrThread(0x12, 3, 1, 84)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    Return()

    # Function_82_47E9 end

    def Function_83_48D5(): pass

    label("Function_83_48D5")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_83_48D5 end

    def Function_84_4907(): pass

    label("Function_84_4907")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_84_4907 end

    def Function_85_4939(): pass

    label("Function_85_4939")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x64D2, 0xFFFFE890, 0xFFFFD29C, 0x61A8, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x54A6, 0xFFFFE890, 0x46A, 0x7D0, 0x3E8)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x48DA, 0xFFFFE890, 0x26B6, 0x3E8, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_85_4939 end

    def Function_86_499E(): pass

    label("Function_86_499E")


    ChrTalk(
        0x101,
        "#5P#5AIlya!!\x02",
    )

    SetChrFlags(0xFE, 0x20)

    def lambda_49B9():

        label("loc_49B9")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_49B9")

    QueueWorkItem2(0xFE, 2, lambda_49B9)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 60, 0)
    BeginChrThread(0x14, 3, 1, 88)
    BeginChrThread(0x10, 3, 1, 87)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x10, 3)
    Return()

    # Function_86_499E end

    def Function_87_4A08(): pass

    label("Function_87_4A08")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0x10,
        (
            "#5P#5A#4SHaaah...#3S wait, no,\x01",
            "what!?\x02",
        )
    )

    Sound(809, 0, 100, 0)

    def lambda_4A4D():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFBD98, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A4D)
    Sleep(700)
    SetChrSubChip(0xFE, 0x1)
    Sound(590, 0, 100, 0)
    BeginChrThread(0x11, 3, 1, 83)
    BeginChrThread(0x12, 3, 1, 84)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    Return()

    # Function_87_4A08 end

    def Function_88_4AA8(): pass

    label("Function_88_4AA8")

    Sound(443, 0, 40, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFBD98, 0x898, 0x3E8)
    Sound(441, 0, 60, 0)
    OP_9D(0xFE, 0x6F54, 0xFFFFE890, 0xFFFFC091, 0x384, 0x3E8)
    Sound(441, 0, 60, 0)
    OP_9D(0xFE, 0x717A, 0xFFFFE890, 0xFFFFC1E4, 0x12C, 0x3E8)
    Return()

    # Function_88_4AA8 end

    SaveToFile()

Try(main)

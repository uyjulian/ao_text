from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t3520.bin",                # FileName
        "t3520",                    # MapName
        "t3520",                    # Location
        0x005C,                     # MapIndex
        "ed7150",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 92, 0, 1, 0, 2],
    )

    BuildStringList((
        "t3520",                  # 0
        "Princess Klaudia",       # 1
        "Captain Julia",          # 2
        "Archduke Albert",        # 3
        "Ogre Sigmund",           # 4
        "Shirley",                # 5
        "Jaeger Gareth",          # 6
        "Bodyguard",              # 7
        "Bodyguard",              # 8
        "Mechanic",               # 9
        "Mechanic",               # 10
        "Mechanic",               # 11
        "Mechanic",               # 12
        "Arseille",               # 13
        "足場",                   # 14
        "Assistant",              # 15
        "Assistant",              # 16
        "Assistant",              # 17
        "Policeman",              # 18
        "Policeman",              # 19
        "Policeman",              # 20
        "Policeman",              # 21
        "Policeman",              # 22
        "SE制御",                 # 23
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(932, 0)                                        # 0

    ScpFunction((
        "Function_0_3A4",          # 00, 0
        "Function_1_454",          # 01, 1
        "Function_2_48F",          # 02, 2
        "Function_3_4A5",          # 03, 3
        "Function_4_C07",          # 04, 4
        "Function_5_C50",          # 05, 5
        "Function_6_C8A",          # 06, 6
        "Function_7_CC6",          # 07, 7
        "Function_8_CE6",          # 08, 8
        "Function_9_CFB",          # 09, 9
        "Function_10_D37",         # 0A, 10
        "Function_11_D57",         # 0B, 11
        "Function_12_D6C",         # 0C, 12
        "Function_13_DBC",         # 0D, 13
        "Function_14_DEF",         # 0E, 14
        "Function_15_E04",         # 0F, 15
        "Function_16_E72",         # 10, 16
        "Function_17_EAF",         # 11, 17
        "Function_18_EC4",         # 12, 18
        "Function_19_F0B",         # 13, 19
        "Function_20_F52",         # 14, 20
        "Function_21_FB0",         # 15, 21
        "Function_22_FCC",         # 16, 22
        "Function_23_1961",        # 17, 23
        "Function_24_199E",        # 18, 24
        "Function_25_19E2",        # 19, 25
        "Function_26_1A47",        # 1A, 26
        "Function_27_1AAC",        # 1B, 27
        "Function_28_1B11",        # 1C, 28
        "Function_29_1B76",        # 1D, 29
        "Function_30_1BBD",        # 1E, 30
        "Function_31_2E0B",        # 1F, 31
        "Function_32_2E48",        # 20, 32
        "Function_33_2EA3",        # 21, 33
        "Function_34_2EF8",        # 22, 34
    ))


    def Function_0_3A4(): pass

    label("Function_0_3A4")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3DC"),
        (1, "loc_3E8"),
        (2, "loc_3F4"),
        (3, "loc_400"),
        (4, "loc_40C"),
        (5, "loc_418"),
        (6, "loc_424"),
        (SWITCH_DEFAULT, "loc_430"),
    )


    label("loc_3DC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_43C")

    label("loc_3E8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_43C")

    label("loc_3F4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_43C")

    label("loc_400")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_43C")

    label("loc_40C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_43C")

    label("loc_418")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_43C")

    label("loc_424")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_43C")

    label("loc_430")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_43C")

    label("loc_43C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_453")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_43C")

    label("loc_453")

    Return()

    # Function_0_3A4 end

    def Function_1_454(): pass

    label("Function_1_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_468")
    ClearScenarioFlags(0x22, 0)
    Event(0, 3)
    Jump("loc_48E")

    label("loc_468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_47C")
    ClearScenarioFlags(0x22, 1)
    Event(0, 22)
    Jump("loc_48E")

    label("loc_47C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_48E")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x0, 0)
    Event(0, 30)

    label("loc_48E")

    Return()

    # Function_1_454 end

    def Function_2_48F(): pass

    label("Function_2_48F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4A4")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_4A4")

    Return()

    # Function_2_48F end

    def Function_3_4A5(): pass

    label("Function_3_4A5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11000.itc", 0x1E)
    LoadChrToIndex("chr/ch11200.itc", 0x1F)
    LoadChrToIndex("chr/ch11800.itc", 0x20)
    LoadChrToIndex("chr/ch41600.itc", 0x21)
    LoadChrToIndex("apl/ch51213.itc", 0x22)
    LoadChrToIndex("chr/ch27800.itc", 0x23)
    LoadChrToIndex("chr/ch27600.itc", 0x24)
    LoadChrToIndex("chr/ch28600.itc", 0x25)
    LoadChrToIndex("apl/ch51231.itc", 0x26)
    SoundLoad(496)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07000.itp")
    CreatePortrait(1, 16, 200, 528, 264, 0, 0, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis517.itp")
    CreatePortrait(2, 16, 200, 528, 264, 0, 0, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis518.itp")
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x25)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x25)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x24)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x26)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x26)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x26)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x26)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0xE, 0x21)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xF, 0x21)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x14, 0x80)
    OP_78(0x2, 0x14)
    OP_49()
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x1000)
    ClearChrFlags(0x15, 0x80)
    OP_78(0x0, 0x15)
    OP_49()
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFrame(0xFF, "02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "asiba", 0x0, 0x1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x19, 9250, 6000, -24000, 0)
    SetChrPos(0x1A, 7250, 6000, -25500, 0)
    SetChrPos(0x1B, 8500, 6000, -25500, 0)
    SetChrPos(0x1C, 10000, 6000, -25500, 0)
    SetChrPos(0x1D, 11250, 6000, -25500, 0)
    SetChrPos(0x14, 2250, 12300, -7000, 270)
    OP_D5(0x14, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x15, 8250, -250, -25000, 0)
    OP_D5(0x15, 0x0, 0x0, 0x0, 0x0)
    BeginChrThread(0x14, 1, 0, 4)
    OP_68(-12250, 15000, -7000, 0)
    MoveCamera(55, 35, -5, 0)
    OP_6E(600, 0)
    SetCameraDistance(59800, 0)
    OP_68(-12250, 8000, -7000, 7500)
    MoveCamera(50, 25, -5, 7500)
    SetCameraDistance(54800, 7500)
    BeginChrThread(0x1E, 1, 0, 20)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x14, 1)
    Fade(500)
    SetChrPos(0x8, 4550, 5700, -7050, 90)
    SetChrPos(0x9, 4550, 5700, -7050, 90)
    SetChrPos(0xE, 4550, 5700, -7050, 90)
    SetChrPos(0xF, 4550, 5700, -7050, 90)
    OP_68(8250, 6700, -16250, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(28000, 0)
    OP_68(6000, 6700, -7300, 5000)
    MoveCamera(315, 20, 0, 5000)
    SetCameraDistance(25000, 5000)
    BeginChrThread(0x15, 1, 0, 5)
    Sleep(600)
    Sound(108, 0, 80, 0)
    Sound(145, 0, 100, 0)
    WaitChrThread(0x15, 1)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x14, 0x0, 0x0)
    OP_79(0x1)
    OP_6F(0x79)
    SetCameraDistance(23000, 5000)
    Sound(100, 0, 100, 0)
    OP_71(0x2, 0x749, 0x753, 0x0, 0x8)
    OP_79(0x2)
    BeginChrThread(0xE, 1, 0, 6)
    Sleep(750)
    BeginChrThread(0xF, 1, 0, 9)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xF, 1)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xE, 0x22)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xF, 0x0)
    OP_0D()
    BeginChrThread(0x9, 1, 0, 12)
    Sleep(750)
    BeginChrThread(0x8, 1, 0, 15)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x8, 1)
    OP_6F(0x79)
    BeginChrThread(0x19, 1, 0, 19)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(3500)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    EndChrThread(0x19, 0x1)
    OP_64(0x19)
    OP_64(0x8)
    BeginChrThread(0x9, 1, 0, 13)
    Sleep(100)
    BeginChrThread(0x8, 1, 0, 16)
    Sleep(1000)
    BeginChrThread(0xE, 1, 0, 7)
    BeginChrThread(0xF, 1, 0, 10)
    Sleep(3000)
    EndChrThread(0x9, 0x1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    Fade(500)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrPos(0x8, 12500, 6000, -23500, 90)
    SetChrPos(0x9, 14000, 6000, -22500, 90)
    SetChrPos(0xE, 11000, 6000, -22500, 90)
    SetChrPos(0xF, 11000, 6000, -24500, 90)
    SetChrPos(0xA, 31000, 6000, -23500, 270)
    SetChrPos(0x16, 32000, 6000, -24500, 270)
    SetChrPos(0x17, 33500, 6000, -22500, 270)
    SetChrPos(0x18, 33500, 6000, -24500, 270)
    OP_68(15500, 6700, -23500, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_68(22750, 6700, -23500, 4000)
    SetCameraDistance(15000, 10000)
    BeginChrThread(0x9, 1, 0, 14)
    BeginChrThread(0x8, 1, 0, 17)
    BeginChrThread(0xE, 1, 0, 8)
    BeginChrThread(0xF, 1, 0, 11)
    Sleep(1000)

    def lambda_B3A():
        OP_9B(0x0, 0xFE, 0x0, 0x203A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B3A)
    Sleep(50)

    def lambda_B52():
        OP_9B(0x0, 0xFE, 0x0, 0x203A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_B52)
    Sleep(50)

    def lambda_B6A():
        OP_9B(0x0, 0xFE, 0x0, 0x203A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_B6A)
    Sleep(50)

    def lambda_B82():
        OP_9B(0x0, 0xFE, 0x0, 0x203A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_B82)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x8, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xF, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x16, 1)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x18, 1)
    OP_6F(0x1)
    BeginChrThread(0x8, 1, 0, 18)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(3500)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("t3510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_4A5 end

    def Function_4_C07(): pass

    label("Function_4_C07")

    OP_71(0x2, 0x1AF, 0x319, 0x0, 0x8)
    OP_96(0xFE, 0x8CA, 0x14B4, 0xFFFFE4A8, 0x3E8, 0x0)
    OP_96(0xFE, 0x8CA, 0x10CC, 0xFFFFE4A8, 0x1F4, 0x0)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    OP_79(0x2)
    Return()

    # Function_4_C07 end

    def Function_5_C50(): pass

    label("Function_5_C50")

    OP_82(0xA, 0x0, 0xBB8, 0x1388)
    OP_96(0xFE, 0x203A, 0xFFFFFF06, 0xFFFFBF28, 0x7D0, 0x0)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sleep(500)
    Return()

    # Function_5_C50 end

    def Function_6_C8A(): pass

    label("Function_6_C8A")


    def lambda_C8F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_C8F)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
    OP_95(0xFE, 7000, 5730, -11650, 3000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_6_C8A end

    def Function_7_CC6(): pass

    label("Function_7_CC6")

    SetChrChipByIndex(0xFE, 0x21)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_95(0xFE, 8000, 6000, -22500, 2000, 0x0)
    Return()

    # Function_7_CC6 end

    def Function_8_CE6(): pass

    label("Function_8_CE6")

    OP_95(0xFE, 18750, 6000, -22500, 2000, 0x0)
    Return()

    # Function_8_CE6 end

    def Function_9_CFB(): pass

    label("Function_9_CFB")


    def lambda_D00():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_D00)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
    OP_95(0xFE, 9750, 5730, -11650, 3000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_9_CFB end

    def Function_10_D37(): pass

    label("Function_10_D37")

    SetChrChipByIndex(0xFE, 0x21)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_95(0xFE, 8750, 6000, -24500, 2000, 0x0)
    Return()

    # Function_10_D37 end

    def Function_11_D57(): pass

    label("Function_11_D57")

    OP_95(0xFE, 18750, 6000, -24500, 2000, 0x0)
    Return()

    # Function_11_D57 end

    def Function_12_D6C(): pass

    label("Function_12_D6C")


    def lambda_D71():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_D71)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
    OP_95(0xFE, 8000, 5730, -10500, 2000, 0x0)
    OP_95(0xFE, 8000, 6000, -21000, 2000, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_12_D6C end

    def Function_13_DBC(): pass

    label("Function_13_DBC")

    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1000)
    OP_95(0xFE, 10000, 6000, -22500, 2000, 0x0)
    OP_95(0xFE, 20000, 6000, -22500, 2000, 0x0)
    Return()

    # Function_13_DBC end

    def Function_14_DEF(): pass

    label("Function_14_DEF")

    OP_95(0xFE, 20250, 6000, -22500, 2000, 0x0)
    Return()

    # Function_14_DEF end

    def Function_15_E04(): pass

    label("Function_15_E04")


    def lambda_E09():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_E09)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
    OP_68(9250, 6700, -21000, 8000)
    MoveCamera(315, 25, 0, 8000)
    SetCameraDistance(16000, 8000)
    OP_95(0xFE, 8750, 5730, -11600, 2000, 0x0)
    OP_95(0xFE, 9250, 6000, -21000, 2000, 0x0)
    Return()

    # Function_15_E04 end

    def Function_16_E72(): pass

    label("Function_16_E72")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x87, 0x12C)
    Sleep(500)
    OP_95(0xFE, 11700, 6000, -23500, 2000, 0x0)
    OP_95(0xFE, 21700, 6000, -23500, 2000, 0x0)
    Return()

    # Function_16_E72 end

    def Function_17_EAF(): pass

    label("Function_17_EAF")

    OP_95(0xFE, 21250, 6000, -23500, 2000, 0x0)
    Return()

    # Function_17_EAF end

    def Function_18_EC4(): pass

    label("Function_18_EC4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F0A")
    OP_63(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x8)
    Sleep(500)
    OP_63(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xA)
    Sleep(500)
    Jump("Function_18_EC4")

    label("loc_F0A")

    Return()

    # Function_18_EC4 end

    def Function_19_F0B(): pass

    label("Function_19_F0B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F51")
    OP_63(0x19, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x19)
    Sleep(500)
    OP_63(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x8)
    Sleep(500)
    Jump("Function_19_F0B")

    label("loc_F51")

    Return()

    # Function_19_F0B end

    def Function_20_F52(): pass

    label("Function_20_F52")

    Sound(496, 2, 40, 0)
    BeginChrThread(0x1E, 2, 0, 21)
    Sleep(200)
    OP_25(0x1F0, 0x32)
    Sleep(200)
    OP_25(0x1F0, 0x3C)
    Sleep(200)
    OP_25(0x1F0, 0x46)
    Sleep(200)
    OP_25(0x1F0, 0x50)
    Sleep(200)
    OP_25(0x1F0, 0x5A)
    Sleep(200)
    OP_25(0x1F0, 0x64)
    Sleep(4800)
    Sound(942, 0, 40, 0)
    Sleep(3000)
    Sound(495, 0, 50, 0)
    Sound(833, 0, 50, 0)
    StopSound(496, 1000, 90)
    Sleep(1000)
    Sound(954, 0, 30, 0)
    Return()

    # Function_20_F52 end

    def Function_21_FB0(): pass

    label("Function_21_FB0")

    Sleep(2700)
    Sound(964, 0, 100, 0)
    Sleep(700)
    Sound(964, 0, 100, 0)
    Sleep(700)
    Sound(964, 0, 100, 0)
    Return()

    # Function_21_FB0 end

    def Function_22_FCC(): pass

    label("Function_22_FCC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11200.itc", 0x1E)
    LoadChrToIndex("apl/ch51212.itc", 0x1F)
    LoadChrToIndex("chr/ch41600.itc", 0x20)
    LoadChrToIndex("apl/ch51213.itc", 0x21)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 22500, 6000, -37400, 0)
    SetChrPos(0x101, 22500, 6000, -37400, 0)
    SetChrPos(0x102, 22500, 6000, -37400, 0)
    SetChrPos(0x104, 22500, 6000, -37400, 0)
    SetChrPos(0x109, 22500, 6000, -37400, 0)
    SetChrPos(0x105, 22500, 6000, -37400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 10300, 5730, -10500, 180)
    BeginChrThread(0xE, 0, 0, 0)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 6300, 5730, -10500, 180)
    BeginChrThread(0xF, 0, 0, 0)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0x14)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0x9A, 0x80, 0x1E, 0x12C, 0x0)
    OP_68(22500, 6900, -28500, 0)
    MoveCamera(315, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    BeginChrThread(0x9, 3, 0, 24)
    BeginChrThread(0x101, 3, 0, 25)
    BeginChrThread(0x102, 3, 0, 26)
    BeginChrThread(0x105, 3, 0, 27)
    BeginChrThread(0x109, 3, 0, 28)
    BeginChrThread(0x104, 3, 0, 29)
    FadeToBright(2000, 0)
    OP_0D()
    OP_68(5500, 7500, -10300, 9000)
    MoveCamera(309, 15, 0, 9000)
    SetCameraDistance(48000, 9000)
    OP_6F(0x79)
    WaitChrThread(0x104, 3)
    Fade(500)
    OP_68(7800, 8300, -22400, 0)
    MoveCamera(323, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_68(7800, 7300, -22400, 2000)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#6P#00002FThe Arseille... It's\x01",
            "even more beautiful up\x01",
            "close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FHehe, so this is why\x01",
            "they call her the pride\x01",
            "of Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#2SI-I can't believe we get\x01",
            "to meet the crown\x01",
            "princess...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x9, 500)
    Sleep(150)

    ChrTalk(
        0x109,
        (
            "#10108F#2SAnd, to be this close to\x01",
            "Captain Julia...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#5P#00109F#2SC-Calm down, Noｱl.\x02\x03",
            "#00102F#2SLet's ask for her\x01",
            "autograph later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#2SS-Sure! I've got to get\x01",
            "one for Fran, too!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    ChrTalk(
        0x104,
        (
            "#12P#00309FOur girls are unusually\x01",
            "hyper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#07105F#5P???\x02\x03",
            "#07104FI heard about your team. You've\x01",
            "made a considerable impact, even\x01",
            "though you're all so young.\x02\x03",
            "#07102FIt seems you were responsible\x01",
            "for the resolution of a major\x01",
            "incident several months ago?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_14B6():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_14B6)
    Sleep(50)

    def lambda_14C6():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_14C6)
    Sleep(50)

    def lambda_14D6():
        TurnDirection(0x105, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_14D6)
    Sleep(50)

    def lambda_14E6():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_14E6)
    Sleep(50)

    def lambda_14F6():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_14F6)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        (
            "#12P#00012FN-No, we have a long way to go.\x02\x03",
            "#00000FIt was only thanks to the help of\x01",
            "everyone else that we were able\x01",
            "to resolve the incident somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#07104F#5PHaha...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#07102F#5PAh, excuse me.\x02\x03",
            "I have a friend who once\x01",
            "said something similar.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_1634():

        label("loc_1634")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1634")

    QueueWorkItem2(0x101, 2, lambda_1634)

    def lambda_1646():

        label("loc_1646")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1646")

    QueueWorkItem2(0x102, 2, lambda_1646)

    def lambda_1658():

        label("loc_1658")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1658")

    QueueWorkItem2(0x109, 2, lambda_1658)

    def lambda_166A():

        label("loc_166A")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_166A")

    QueueWorkItem2(0x105, 2, lambda_166A)

    def lambda_167C():

        label("loc_167C")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_167C")

    QueueWorkItem2(0x104, 2, lambda_167C)

    def lambda_168E():
        OP_95(0xFE, 8300, 6000, -19500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_168E)
    WaitChrThread(0x9, 1)

    def lambda_16AC():
        OP_95(0xFE, 8300, 5720, -12500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_16AC)
    Sleep(1000)
    Fade(500)
    OP_68(8300, 6700, -14500, 0)
    MoveCamera(320, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetChrPos(0x101, 8800, 6000, -22000, 0)
    SetChrPos(0x102, 8800, 6000, -20800, 0)
    SetChrPos(0x104, 10900, 6000, -21400, 0)
    SetChrPos(0x109, 9900, 6000, -20600, 0)
    SetChrPos(0x105, 9900, 6000, -22200, 0)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0xB4, 0x1F4)
    Sleep(300)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0xE, 0xFF)
    SetChrChipByIndex(0xE, 0x21)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xF, 0xFF)
    SetChrChipByIndex(0xF, 0x21)
    SetChrSubChip(0xF, 0x0)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#07103F#11P─Welcome to the Arseille.\x02\x03",
            "#07102FTo preserve secrecy, wireless\x01",
            "devices do not work onboard,\x01",
            "but...\x02\x03",
            "If that's inconvenient for\x01",
            "you I can turn it off, so\x01",
            "please don't hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FU-Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FAhhh... So this is what\x01",
            "a state-of-the-art\x01",
            "warship looks like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104FWell then, excuse us.\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    BeginChrThread(0x102, 3, 0, 23)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 23)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 23)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x109, 0xFF)
    StopBGM(0xFA0)
    WaitBGM()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(500)
    SetScenarioFlags(0x22, 5)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_FCC end

    def Function_23_1961(): pass

    label("Function_23_1961")


    def lambda_1966():
        OP_95(0xFE, 8300, 5840, -18500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1966)
    WaitChrThread(0xFE, 1)

    def lambda_1984():
        OP_95(0xFE, 8300, 5720, -13500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1984)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_23_1961 end

    def Function_24_199E(): pass

    label("Function_24_199E")


    def lambda_19A3():
        OP_95(0xFE, 22500, 6000, -22400, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_19A3)
    WaitChrThread(0xFE, 1)

    def lambda_19C1():
        OP_95(0xFE, 6800, 6000, -22400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_19C1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_24_199E end

    def Function_25_19E2(): pass

    label("Function_25_19E2")

    Sleep(700)

    def lambda_19EA():
        OP_95(0xFE, 22500, 6000, -22400, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_19EA)
    WaitChrThread(0xFE, 1)

    def lambda_1A08():
        OP_95(0xFE, 10900, 6000, -22400, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1A08)
    WaitChrThread(0xFE, 1)

    def lambda_1A26():
        OP_95(0xFE, 8800, 6000, -23000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1A26)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_25_19E2 end

    def Function_26_1A47(): pass

    label("Function_26_1A47")

    Sleep(1300)

    def lambda_1A4F():
        OP_95(0xFE, 22500, 6000, -22400, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1A4F)
    WaitChrThread(0xFE, 1)

    def lambda_1A6D():
        OP_95(0xFE, 10900, 6000, -22400, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1A6D)
    WaitChrThread(0xFE, 1)

    def lambda_1A8B():
        OP_95(0xFE, 8800, 6000, -21800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1A8B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_26_1A47 end

    def Function_27_1AAC(): pass

    label("Function_27_1AAC")

    Sleep(1900)

    def lambda_1AB4():
        OP_95(0xFE, 22500, 6000, -22400, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1AB4)
    WaitChrThread(0xFE, 1)

    def lambda_1AD2():
        OP_95(0xFE, 10900, 6000, -22400, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1AD2)
    WaitChrThread(0xFE, 1)

    def lambda_1AF0():
        OP_95(0xFE, 9900, 6000, -23200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1AF0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_27_1AAC end

    def Function_28_1B11(): pass

    label("Function_28_1B11")

    Sleep(2500)

    def lambda_1B19():
        OP_95(0xFE, 22500, 6000, -22400, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1B19)
    WaitChrThread(0xFE, 1)

    def lambda_1B37():
        OP_95(0xFE, 10900, 6000, -22400, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1B37)
    WaitChrThread(0xFE, 1)

    def lambda_1B55():
        OP_95(0xFE, 9900, 6000, -21600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1B55)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_28_1B11 end

    def Function_29_1B76(): pass

    label("Function_29_1B76")

    Sleep(3100)

    def lambda_1B7E():
        OP_95(0xFE, 22500, 6000, -22400, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1B7E)
    WaitChrThread(0xFE, 1)

    def lambda_1B9C():
        OP_95(0xFE, 10900, 6000, -22400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1B9C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_29_1B76 end

    def Function_30_1BBD(): pass

    label("Function_30_1BBD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(500)
    OP_32(0xFF, 0xFE, 0x0)
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x3, 0xFF)
    OP_BC(0x1)
    OP_BC(0x2)
    OP_BC(0x3)
    LoadChrToIndex("chr/ch03400.itc", 0x1E)
    LoadChrToIndex("chr/ch03300.itc", 0x1F)
    LoadChrToIndex("chr/ch42900.itc", 0x20)
    LoadChrToIndex("apl/ch51600.itc", 0x21)
    LoadChrToIndex("chr/ch26000.itc", 0x22)
    SoundLoad(111)
    SoundLoad(109)
    CreatePortrait(0, 16, 178, 528, 242, 0, 20, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis507.itp")
    LoadEffect(0x9, "event/ev16001.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 200000, 300000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xC, 0x21)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xC, 0x20)
    SetChrPos(0xC, 6500, 10660, -3000, 180)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrBattleFlags(0xB, 0x20)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xB, 1500, 9350, -7000, 90)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrBattleFlags(0xD, 0x20)
    ClearChrFlags(0xD, 0x4)
    SetChrPos(0xD, 1500, 9350, -7000, 90)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 0x22)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -12000, 6000, -22000, 90)
    SetChrChipByIndex(0x11, 0x22)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x11, 0x4)
    SetChrPos(0x11, 21500, 6000, -27000, 0)
    SetChrChipByIndex(0x12, 0x22)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -6800, 0, -15500, 0)
    BeginChrThread(0x12, 0, 0, 0)
    SetChrChipByIndex(0x13, 0x22)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 2500, 6000, -20700, 0)
    BeginChrThread(0x13, 0, 0, 0)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    OP_70(0x3, 0x2D)
    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0x14)
    SetMapObjFrame(0xFF, "01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x1, 0x1)
    OP_68(202000, 4000, 193000, 0)
    MoveCamera(35, 31, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(55000, 0)
    Sound(111, 2, 100, 0)
    Sound(109, 1, 60, 0)
    Sleep(2000)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#30W─On that day, against a backdrop of nonaggression, the\x01",
            "Nation of Crossbell deployed a unique diplomatic\x01",
            "strategy.\x02\x03",
            "Crossbell proposed the Zemuria Continental Alliance, to\x01",
            "be led by the same.\x02\x03",
            "All millitary actions were banned, and in exchange,\x01",
            "economic freedom was guaranteed. The Empire and Republic\x01",
            "were coerced into agreeing, along with smaller states.\x02\x03",
            "At first, Liberl, Remiferia and Arteria opposed the\x01",
            "alliance, calling it too overbearing. But eventually,\x01",
            "they too had to capitulate.\x02\x03",
            "─In the Republic of Calvard, an economic crisis stemming\x01",
            "from events in Crossbell broke out, and Anti-Immigration\x01",
            "League terror activities began to intensify...\x02\x03",
            "In the Erebonian Empire, bloody civil war finally broke\x01",
            "out between noble and reformist factions. News of the\x01",
            "Blood and Iron Chancellor's assassination spread.\x02\x03",
            "And, unofficially, Ouroboros made their position as\x01",
            "allies of Crossbell known to continental governments.\x02\x03",
            "There were none who could put a stop to President\x01",
            "Dieter's ambitions.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    StopEffect(0x7, 0x2)
    StopSound(111, 1500, 100)
    StopSound(109, 1500, 60)
    Sleep(2000)
    PlayBGM("ed7356", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(2000, 4000, -7000, 0)
    MoveCamera(35, 31, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(55000, 0)
    BeginChrThread(0x10, 3, 0, 31)
    BeginChrThread(0x11, 3, 0, 32)
    OP_68(0, 4000, -7000, 9000)
    MoveCamera(57, 27, 0, 9000)
    SetCameraDistance(40000, 9000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(3500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(6500, 11660, -3000, 0)
    MoveCamera(305, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetCameraDistance(15500, 2000)
    OP_0D()
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#04606F#11PAww... It's so boring when\x01",
            "it's over this quickly.\x02\x03",
            "#04603FWe left it to those guys and\x01",
            "Shirley's turn didn't even\x01",
            "come.\x02\x03",
            "#04601FWe only got to face those\x01",
            "special forces units near\x01",
            "the border at the beginning.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(454, 0, 100, 0)
    OP_71(0x3, 0x1, 0xF, 0x0, 0x0)
    OP_79(0x3)
    Sleep(300)

    NpcTalk(
        0xB,
        "Bold Voice",
        (
            "#2SHehe... What's wrong,\x01",
            "Shirley?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(6260, 11660, -4280, 3000)
    SetCameraDistance(15160, 3000)
    BeginChrThread(0xB, 3, 0, 33)
    Sleep(900)
    BeginChrThread(0xD, 3, 0, 34)
    WaitChrThread(0xB, 3)
    OP_6F(0x79)

    ChrTalk(
        0xC,
        (
            "#11P#04605FAh, papa.\x02\x03",
            "#04606F...Hey, isn't it about\x01",
            "time?\x02\x03",
            "Crazy things are happening\x01",
            "in the Empire. Won't it be\x01",
            "more fun over there?\x02\x03",
            "#04602FLooks like interesting\x01",
            "things are happening in\x01",
            "the Republic, too.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xD, 3)

    ChrTalk(
        0xB,
        (
            "#6P#04504FWe still have a job to\x01",
            "do.\x02\x03",
            "#04500FIf you're that bored,\x01",
            "why don't you go play\x01",
            "with that boy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#04606FHmm. Demonized, Wald\x01",
            "isn't too bad.\x02\x03",
            "But in his normal state\x01",
            "he's weak and not worth\x01",
            "my time.\x02\x03",
            "#04605FAlso, it seems he's gone\x01",
            "off somewhere today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#04504FThen, what if you tried\x01",
            "a bout with those\x01",
            "Ouroboros folks?\x02\x03",
            "#04500FAt least you wouldn't be\x01",
            "bored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#04606FHmm. They're not a good\x01",
            "match for Shirley,\x01",
            "somehow...\x02\x03",
            "#04600FAnd Shirley feels like she\x01",
            "could never win against\x01",
            "that amazing lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#04504FHehe. So you get it, do\x01",
            "you.\x02\x03",
            "#04502F─Well, don't be too hard\x01",
            "on yourself.\x02\x03",
            "It appears "he" has\x01",
            "started to act in the\x01",
            "Mainz region.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "#11P#04611F...Wow.\x02\x03",
            "#04609FEven though we beat him\x01",
            "so badly, he still wants\x01",
            "to challenge us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#04504FDon't underestimate him─\x01",
            "he's strong.\x02\x03",
            "#04500FProbably stronger than\x01",
            "you think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#04600FHmm. Doesn't seem that\x01",
            "way to me.\x02\x03",
            "#04604FOh, whatever. I'll let\x01",
            "you take care of him,\x01",
            "papa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#04504FYeah, that's for the\x01",
            "best.\x02\x03",
            "#04500F─You've got your own\x01",
            "playmate after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(14400, 500)
    SetChrSubChip(0xC, 0x1)
    OP_6F(0x79)
    CancelBlur(0)

    ChrTalk(
        0xC,
        (
            "#11P#04605FEeeh─\x02\x03",
            "#04601F...Is she back from\x01",
            "Calvard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P─Heiyue movements were\x01",
            "detected in the Armorica\x01",
            "region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PIt seems Yin has been\x01",
            "hiding with them ever since\x01",
            "the attack on Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_82(0x46, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0xC,
        "#11P#04601F#4S...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#04504FHehe. So Cao is more\x01",
            "stubborn than he looks\x01",
            "too...\x02\x03",
            "#04502FLooks like we'll be able\x01",
            "to have a little more\x01",
            "more fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#04607FAh, jeez, who cares\x01",
            "about that four eyes!\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    Sound(809, 0, 50, 0)
    OP_68(6260, 11860, -4280, 800)

    def lambda_2C51():
        OP_9C(0xFE, 0x0, 0x0, 0xFFFFFED4, 0x384, 0x7D0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2C51)
    WaitChrThread(0xC, 1)
    Sound(30, 0, 80, 0)
    Sleep(10)
    Sound(54, 0, 80, 0)
    OP_63(0xC, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_93(0xC, 0x0, 0x3E8)
    OP_93(0xC, 0xB5, 0x3E8)
    Sleep(500)
    OP_64(0xC)
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xC,
        (
            "#11P#04609F#4SUwaaaah...! I'm super\x01",
            "excited!!\x02\x03",
            "#04602FIn the end, we couldn't\x01",
            "settle things at Arc-en-\x01",
            "Ciel...\x02\x03",
            "#04612FNext time, we'll have to\x01",
            "have a good fight. I'll be\x01",
            "the bestest time ever!♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#6P#04504FHehe... Oh, brother.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PI'd expect nothing less\x01",
            "from the young lady.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(15400, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x6F)
    OP_24(0x70)
    SetScenarioFlags(0x22, 1)
    NewScene("c140D", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_1BBD end

    def Function_31_2E0B(): pass

    label("Function_31_2E0B")


    def lambda_2E10():
        OP_95(0xFE, 24000, 6000, -22000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E10)
    WaitChrThread(0xFE, 1)

    def lambda_2E2E():
        OP_95(0xFE, 24000, 6000, -36500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E2E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_31_2E0B end

    def Function_32_2E48(): pass

    label("Function_32_2E48")


    def lambda_2E4D():
        OP_95(0xFE, 21500, 6000, -24000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E4D)
    WaitChrThread(0xFE, 1)

    def lambda_2E6B():
        OP_95(0xFE, 9000, 6000, -24000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E6B)
    WaitChrThread(0xFE, 1)

    def lambda_2E89():
        OP_95(0xFE, 9000, 5720, -9000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E89)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_32_2E48 end

    def Function_33_2EA3(): pass

    label("Function_33_2EA3")


    def lambda_2EA8():
        OP_95(0xFE, 5000, 10660, -7000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2EA8)

    def lambda_2EC2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2EC2)
    WaitChrThread(0xB, 1)

    def lambda_2ED7():
        OP_95(0xFE, 6700, 10660, -5400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2ED7)
    WaitChrThread(0xB, 1)
    TurnDirection(0xB, 0xC, 500)
    Return()

    # Function_33_2EA3 end

    def Function_34_2EF8(): pass

    label("Function_34_2EF8")


    def lambda_2EFD():
        OP_95(0xFE, 5000, 10660, -7000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2EFD)

    def lambda_2F17():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2F17)
    WaitChrThread(0xD, 1)

    def lambda_2F2C():
        OP_95(0xFE, 5500, 10660, -5800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2F2C)
    WaitChrThread(0xD, 1)
    TurnDirection(0xD, 0xC, 500)
    Return()

    # Function_34_2EF8 end

    SaveToFile()

Try(main)

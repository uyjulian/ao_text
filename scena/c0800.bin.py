from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0800.bin",                # FileName
        "c0800",                    # MapName
        "c0800",                    # Location
        0x0003,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 3, 0, 0, 0, 1],
    )

    BuildStringList((
        "c0800",                  # 0
        "train",                   # 1
        "train",                   # 2
        "Keya",                 # 3
        "Franc",                 # 4
        "Sergey Manager",           # 5
        "Prime Minister Osborne",         # 6
        "Rector",               # 7
        "Prince Oliver",       # 8
        "Major Muller",           # 9
        "passenger",                   # 10
        "passenger",                   # 11
        "passenger",                   # 12
        "passenger",                   # 13
        "passenger",                   # 14
        "passenger",                   # 15
        "passenger",                   # 16
        "passenger",                   # 17
        "A station attendant",                   # 18
        "Imperial Army Officer",             # 19
        "Imperial Army Officer",             # 20
        "Imperial Army Officer",             # 21
        "Imperial Army Officer",             # 22
        "Imperial Army Officer",             # 23
        "Imperial Army Officer",             # 24
        "Inspector Mahlow",         # 25
        "Raymond investigator",       # 26
        "Fake brand quotient",           # 27
        "Imperial merchant",               # 28
        "train",                   # 29
        "SE control",                 # 30
    ))

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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    449,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    449,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(10000,   0,       4294940296, 2000,    10000,   1200,    4294940996, 0x007C, 0,  43, 0x0000)

    ChipFrameInfo(1252, 0)                                       # 0

    ScpFunction((
        "Function_0_4E4",          # 00, 0
        "Function_1_58C",          # 01, 1
        "Function_2_772",          # 02, 2
        "Function_3_3143",         # 03, 3
        "Function_4_3187",         # 04, 4
        "Function_5_31DD",         # 05, 5
        "Function_6_3233",         # 06, 6
        "Function_7_328E",         # 07, 7
        "Function_8_32E1",         # 08, 8
        "Function_9_332D",         # 09, 9
        "Function_10_3381",        # 0A, 10
        "Function_11_33B1",        # 0B, 11
        "Function_12_3B1C",        # 0C, 12
        "Function_13_3B68",        # 0D, 13
        "Function_14_3BA4",        # 0E, 14
        "Function_15_3BBB",        # 0F, 15
        "Function_16_3BF7",        # 10, 16
        "Function_17_3C0E",        # 11, 17
        "Function_18_3C4A",        # 12, 18
        "Function_19_3C61",        # 13, 19
        "Function_20_3CAE",        # 14, 20
        "Function_21_3CBE",        # 15, 21
        "Function_22_3CFA",        # 16, 22
        "Function_23_3D0A",        # 17, 23
        "Function_24_3D21",        # 18, 24
        "Function_25_3D5D",        # 19, 25
        "Function_26_3D74",        # 1A, 26
        "Function_27_3DB0",        # 1B, 27
        "Function_28_3DC7",        # 1C, 28
        "Function_29_3E03",        # 1D, 29
        "Function_30_3E1A",        # 1E, 30
        "Function_31_3E67",        # 1F, 31
        "Function_32_3E77",        # 20, 32
        "Function_33_3EB3",        # 21, 33
        "Function_34_3EC3",        # 22, 34
        "Function_35_3EDF",        # 23, 35
        "Function_36_3EF6",        # 24, 36
        "Function_37_3F3D",        # 25, 37
        "Function_38_3F84",        # 26, 38
        "Function_39_6650",        # 27, 39
        "Function_40_6681",        # 28, 40
        "Function_41_6B81",        # 29, 41
        "Function_42_7BEE",        # 2A, 42
        "Function_43_849F",        # 2B, 43
        "Function_44_86EA",        # 2C, 44
        "Function_45_8727",        # 2D, 45
        "Function_46_AF4A",        # 2E, 46
        "Function_47_AF73",        # 2F, 47
        "Function_48_AF9F",        # 30, 48
        "Function_49_AFCB",        # 31, 49
        "Function_50_AFFB",        # 32, 50
        "Function_51_B059",        # 33, 51
        "Function_52_B0B7",        # 34, 52
        "Function_53_B113",        # 35, 53
        "Function_54_B185",        # 36, 54
        "Function_55_B1B1",        # 37, 55
        "Function_56_B2AF",        # 38, 56
    ))


    def Function_0_4E4(): pass

    label("Function_0_4E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_4FB")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 2)
    Jump("loc_57A")

    label("loc_4FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_50F")
    ClearScenarioFlags(0x22, 1)
    Event(0, 11)
    Jump("loc_57A")

    label("loc_50F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_526")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x0, 3)
    Event(0, 38)
    Jump("loc_57A")

    label("loc_526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_53D")
    ClearScenarioFlags(0x22, 3)
    SetScenarioFlags(0x0, 4)
    Event(0, 40)
    Jump("loc_57A")

    label("loc_53D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_554")
    ClearScenarioFlags(0x22, 4)
    SetScenarioFlags(0x0, 4)
    Event(0, 41)
    Jump("loc_57A")

    label("loc_554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_56B")
    ClearScenarioFlags(0x22, 5)
    SetScenarioFlags(0x0, 5)
    Event(0, 45)
    Jump("loc_57A")

    label("loc_56B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_57A")
    ClearScenarioFlags(0x22, 6)
    Event(0, 55)

    label("loc_57A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58B")
    Event(0, 42)

    label("loc_58B")

    Return()

    # Function_0_4E4 end

    def Function_1_58C(): pass

    label("Function_1_58C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5A6")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)
    Jump("loc_5BE")

    label("loc_5A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 0)), scpexpr(EXPR_END)), "loc_5BE")
    SetScenarioFlags(0x0, 2)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x25, 0)

    label("loc_5BE")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D4")
    OP_66(0x0, 0x1)

    label("loc_5D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5E8")
    OP_24(0x343)
    ClearScenarioFlags(0x0, 2)
    Jump("loc_604")

    label("loc_5E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FE")
    OP_24(0x343)
    Jump("loc_604")

    label("loc_5FE")

    Sound(835, 1, 100, 0)

    label("loc_604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62F")
    OP_7D(0xD2, 0xD2, 0xFF, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_62F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_664")
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_664")

    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x3, 0x1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 6)), scpexpr(EXPR_END)), "loc_702")
    ClearChrFlags(0x8, 0x80)
    OP_78(0x0, 0x8)
    SetChrPos(0x8, 2000, -1550, -24100, 0)
    OP_D5(0x8, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x1, 0x9)
    SetChrPos(0x9, 54000, -1550, 8100, 0)
    OP_D5(0x9, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    Jump("loc_771")

    label("loc_702")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_71C")
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    Jump("loc_771")

    label("loc_71C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_730")
    ClearMapObjFlags(0x3, 0x4)
    Jump("loc_771")

    label("loc_730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_771")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    OP_78(0x0, 0x8)
    SetChrPos(0x8, 38000, -1550, 8100, 0)
    OP_D5(0x8, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)

    label("loc_771")

    Return()

    # Function_1_58C end

    def Function_2_772(): pass

    label("Function_2_772")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    OP_32(0x1, 0x0, 0x32)
    OP_32(0x1, 0x5, 0x64)
    OP_42(0x1, 0x3FD, 0xFF)
    OP_42(0x1, 0x5DD, 0xFF)
    OP_42(0x1, 0x641, 0xFF)
    RemoveCraft(0x1, 0xFFFF)
    OP_38(0x1, 0x80, 0x2)
    OP_38(0x1, 0x83, 0x1)
    OP_38(0x1, 0x84, 0x1)
    OP_42(0x1, 0x80, 0x4)
    AddCraft(0x1, 0xA0)
    AddCraft(0x1, 0xA1)
    AddCraft(0x1, 0xA7)
    AddCraft(0x1, 0xA3)
    AddCraft(0x1, 0xA4)
    AddCraft(0x1, 0x11D)
    AddCraft(0x1, 0x11E)
    SetChrChipPat(0x1, 0x6, 0x11D)
    SetChrChipPat(0x1, 0x6, 0x11E)
    SetChrChipPat(0x1, 0x6, 0x120)
    SetChrChipPat(0x1, 0x6, 0x121)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_806")
    AddCraft(0x1, 0x1AE)
    AddCraft(0x0, 0x1AE)
    Jump("loc_824")

    label("loc_806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_81C")
    AddCraft(0x1, 0x19A)
    AddCraft(0x0, 0x19A)
    Jump("loc_824")

    label("loc_81C")

    AddCraft(0x1, 0x186)
    AddCraft(0x0, 0x186)

    label("loc_824")

    OP_32(0x4, 0x0, 0x32)
    OP_32(0x4, 0x5, 0x64)
    OP_42(0x4, 0x439, 0xFF)
    OP_42(0x4, 0x5DD, 0xFF)
    OP_42(0x4, 0x641, 0xFF)
    RemoveCraft(0x4, 0xFFFF)
    OP_38(0x4, 0x80, 0x2)
    OP_38(0x4, 0x82, 0x1)
    OP_38(0x4, 0x83, 0x1)
    OP_42(0x4, 0x7C, 0x3)
    AddCraft(0x4, 0xBE)
    AddCraft(0x4, 0xBF)
    AddCraft(0x4, 0xC0)
    AddCraft(0x4, 0x12C)
    SetChrChipPat(0x4, 0x6, 0x12C)
    SetChrChipPat(0x4, 0x6, 0x12F)
    OP_32(0xFF, 0xFE, 0x0)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("chr/ch08201.itc", 0x1F)
    LoadChrToIndex("chr/ch06900.itc", 0x20)
    LoadChrToIndex("chr/ch02500.itc", 0x21)
    LoadChrToIndex("apl/ch50380.itc", 0x22)
    LoadChrToIndex("chr/ch28300.itc", 0x23)
    LoadChrToIndex("chr/ch20102.itc", 0x24)
    LoadChrToIndex("chr/ch22002.itc", 0x25)
    LoadChrToIndex("chr/ch33002.itc", 0x26)
    LoadChrToIndex("chr/ch20000.itc", 0x27)
    LoadChrToIndex("chr/ch44000.itc", 0x28)
    LoadChrToIndex("chr/ch24400.itc", 0x29)
    LoadChrToIndex("chr/ch24500.itc", 0x2A)
    LoadChrToIndex("chr/ch27600.itc", 0x2B)
    LoadChrToIndex("apl/ch51020.itc", 0x2C)
    LoadChrToIndex("apl/ch51027.itc", 0x2D)
    LoadChrToIndex("apl/ch51712.itc", 0x2E)
    SoundLoad(452)
    SoundLoad(453)
    SoundLoad(3315)
    SoundLoad(3316)
    SoundLoad(3317)
    SoundLoad(3385)
    SoundLoad(3386)
    SoundLoad(3387)
    SoundLoad(3388)
    SoundLoad(3389)
    SoundLoad(3390)
    SoundLoad(2904)
    SoundLoad(2905)
    SoundLoad(2906)
    SoundLoad(2907)
    SoundLoad(2901)
    SoundLoad(3513)
    SoundLoad(3514)
    SoundLoad(3595)
    SoundLoad(3596)
    SoundLoad(3597)
    SoundLoad(2708)
    SoundLoad(2709)
    SoundLoad(2710)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis401.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01103.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00100.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00101.itp")
    CreatePortrait(4, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10301.itp")
    CreatePortrait(5, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01000.itp")
    CreatePortrait(6, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01902.itp")
    SetChrPos(0x101, -10000, 0, 15000, 0)
    SetChrPos(0x109, -10000, 0, 15000, 0)
    SetChrPos(0x102, -10000, 0, 15000, 0)
    SetChrPos(0x105, -10000, 0, 15000, 0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x20)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x21)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 33100, 100, -14700, 0)
    SetChrChipByIndex(0x12, 0x25)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 20500, 100, -17200, 180)
    SetChrChipByIndex(0x13, 0x26)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 37300, 100, -14700, 0)
    SetChrChipByIndex(0x14, 0x27)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x14, 19700, 100, -9700, 180)
    SetChrChipByIndex(0x15, 0x28)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x15, 19700, 100, -9700, 180)
    SetChrChipByIndex(0x16, 0x29)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x16, 22700, 0, -9700, 180)
    SetChrChipByIndex(0x17, 0x2A)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x17, 22700, 0, -9700, 180)
    SetChrChipByIndex(0x18, 0x2B)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x18, 32500, 0, -9700, 180)
    SetChrChipByIndex(0x19, 0x23)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 52500, 0, -13300, 45)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x1, 0x8)
    OP_49()
    SetChrPos(0x8, 7000, -1550, -8100, 0)
    OP_D5(0x8, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x0, 0x9)
    OP_49()
    SetChrPos(0x9, 54000, -1550, 8100, 0)
    OP_D5(0x9, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    OP_68(65000, 10000, -11000, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(30000, 0)
    OP_F0(0x0, 0x1)
    OP_68(25000, 1500, -11000, 15000)
    MoveCamera(47, 17, 0, 15000)
    SetCameraDistance(50000, 15000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(3000)
    Sound(801, 0, 100, 0)
    Sleep(2500)
    PlaceName2(340, 200, "c_plac00", 0x0, 0)
    Sleep(2500)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x169, 0x294, 0x0, 0x0)
    Sound(453, 0, 100, 0)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(57000, 1500, -8500, 0)
    MoveCamera(53, 2, 0, 0)
    OP_6E(780, 0)
    SetCameraDistance(21000, 0)
    OP_68(10000, 500, -8500, 10000)
    MoveCamera(57, 12, 0, 10000)
    ClearMapObjFlags(0x1, 0x4)
    BeginChrThread(0x8, 3, 0, 3)
    WaitChrThread(0x8, 3)
    Sleep(300)
    Fade(500)
    OP_68(20500, 1300, -12800, 0)
    MoveCamera(39, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x8, 2000, -1550, -8100, 0)
    OP_0D()
    SetCameraDistance(19000, 6000)
    Sound(454, 0, 100, 0)
    OP_71(0x1, 0x0, 0x14, 0x0, 0x0)
    OP_79(0x1)
    BeginChrThread(0x14, 3, 0, 6)
    Sleep(1000)
    BeginChrThread(0x16, 3, 0, 7)
    Sleep(500)
    BeginChrThread(0x15, 3, 0, 6)
    Sleep(500)
    BeginChrThread(0x17, 3, 0, 8)
    Sleep(2000)
    BeginChrThread(0x18, 3, 0, 9)
    Sleep(4000)
    BeginChrThread(0x101, 3, 0, 4)
    Sleep(800)
    BeginChrThread(0x109, 3, 0, 5)
    Sleep(1000)
    OP_68(7900, 1300, -12800, 8000)
    MoveCamera(39, 17, 0, 8000)
    SetCameraDistance(18000, 8000)
    WaitChrThread(0x101, 3)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -11000, 600, -16000, 270)
    OP_C9(0x0, 0x80000000)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    NpcTalk(
        0xA,
        "Voice of a girl",
        "#4S#3595V#12A#30WLloyd ─ ─ ─ ─! It is!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#11P#00005F#3315V#30WAh……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xCF3)
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(-8000, 1500, -16000, 0)
    MoveCamera(317, 27, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13000, 0)
    OP_68(3400, 900, -15400, 3000)
    MoveCamera(327, 27, 0, 3000)
    SetCameraDistance(14000, 3000)
    ClearChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_F9E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F9E)

    def lambda_FAF():
        OP_95(0xFE, 3250, 0, -15450, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_FAF)
    Sleep(2000)

    def lambda_FCC():
        OP_96(0xFE, 0xE74, 0x0, 0xFFFFC3D8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FCC)
    Sleep(50)
    Sound(3037, 255, 100, 0)
    BeginChrThread(0x109, 3, 0, 10)
    WaitChrThread(0xA, 1)
    SetChrChipByIndex(0xA, 0x22)
    SetChrSubChip(0xA, 0x0)

    def lambda_1001():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1001)
    Sound(811, 0, 100, 0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x101,
        (
            "#12P#00002F#3316V#30WKa aa …!\x01",
            "Did you come and pick me up?\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xCF4)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)

    def lambda_1072():
        OP_96(0xFE, 0xB54, 0x0, 0xFFFFC3D8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1072)
    WaitChrThread(0xA, 1)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_82(0x32, 0x0, 0x7D0, 0x12C)

    AnonymousTalk(
        0xA,
        (
            "#3596V#30WWow!\x01",
            "I heard that I am coming home today!\x02\x03",
            "#3597VI am gonna be alright! Is it?\x01",
            "I have not injured anywhere! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xE0D)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x101,
        (
            "#12P#00004FOh, that's fine.\x02\x03",
            "#00002FI'm back, Ka'a.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01109F#5PWelcome back, Lloyd!\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#01121F#5PErr …\x01",
            "Welcome back to Noel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10109FHaha ……\x01",
            "I'm back, Ka'aa.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0xB, -8200, 600, -16400, 270)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x8)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0xB,
        "Daughter's voice",
        "#2708V#12A#30WOlder sister! It is!\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    ClearChrFlags(0xB, 0x8)

    def lambda_12DE():
        OP_95(0xFE, 4350, 0, -16650, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_12DE)
    Sleep(300)

    def lambda_12FB():

        label("loc_12FB")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_12FB")

    QueueWorkItem2(0xA, 2, lambda_12FB)

    def lambda_130D():

        label("loc_130D")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_130D")

    QueueWorkItem2(0x101, 2, lambda_130D)
    WaitChrThread(0xB, 1)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xB, 0x20)
    SetChrChipByIndex(0xB, 0x2D)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0x109, 0x10)
    SetChrFlags(0x109, 0x2)
    SetChrFlags(0x109, 0x20)
    SetChrChipByIndex(0x109, 0x2E)
    SetChrSubChip(0x109, 0x0)
    EndChrThread(0xA, 0x2)
    EndChrThread(0x101, 0x2)

    def lambda_1359():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1359)
    Sound(811, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x109,
        "#12P#10111F#3513V#30WWow, franc! Is it?\x02",
    )

    CloseMessageWindow()
    OP_24(0xDB9)
    OP_CB(0x6, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x6, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x6, 0x3)
    OP_CC(0x0, 0x6, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(150)

    AnonymousTalk(
        0xB,
        (
            "#2709V#30WDamn it …!\x01",
            "My sister was fine and it was good!\x02\x03",
            "#2710VWelcome back!\x01",
            "I do not injure you either ~! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xA96)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x6, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x6, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x6, 0x3)
    OP_CC(0x0, 0x6, 0x0)

    ChrTalk(
        0x109,
        (
            "#12P#10102FYes, as you can see, it's okay.\x02\x03",
            "#10106FI mean, just a few days\x01",
            "Even if you do not make that exaggeration ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0xB, 0x20)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xB, 0x2)
    ClearChrFlags(0xB, 0x20)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    ClearChrFlags(0x109, 0x10)
    ClearChrFlags(0x109, 0x2)
    ClearChrFlags(0x109, 0x20)

    def lambda_1532():
        OP_96(0xFE, 0xFA0, 0x0, 0xFFFFBEC4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1532)
    WaitChrThread(0xB, 1)
    Sleep(150)

    ChrTalk(
        0xB,
        (
            "#01903F#5PMy older sister does not understand!\x01",
            "Time has nothing to do ~.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)
    Sleep(150)

    ChrTalk(
        0xB,
        "#6P#01909FNo, Kaewa-chan?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5P#01101FOh yeah, that's right!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00012Fmy mother……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10112FSomehow it came back\x01",
            "I have a real feeling …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x102, -9000, 600, -15600, 90)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x4)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xC, -9700, 600, -16800, 90)
    OP_C9(0x0, 0x80000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_16FE")

    NpcTalk(
        0x102,
        "Daughter's voice",
        "#3385VLloyd#30W……Welcome back.\x02",
    )

    CloseMessageWindow()
    OP_24(0xD39)
    OP_C9(0x1, 0x80000000)
    Jump("loc_1743")

    label("loc_16FE")


    NpcTalk(
        0x102,
        "Daughter's voice",
        (
            "#3386V#30WHehu ……\x01",
            "Both of you cheers for good work.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xD3A)
    OP_C9(0x1, 0x80000000)

    label("loc_1743")

    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1778():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1778)
    Sleep(50)

    def lambda_1788():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1788)
    Sleep(50)

    def lambda_1798():
        OP_93(0xA, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_1798)
    Sleep(50)

    def lambda_17A8():
        OP_93(0xB, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_17A8)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)

    ChrTalk(
        0x101,
        "#12P#00002FAh……\x02",
    )

    CloseMessageWindow()
    OP_68(-6900, 1400, -16000, 3000)
    MoveCamera(321, 21, 0, 3000)
    SetCameraDistance(14500, 3000)
    Sleep(1300)

    def lambda_1807():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1807)

    def lambda_1818():
        OP_96(0xFE, 0xFFFFE124, 0x258, 0xFFFFC374, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1818)
    Sleep(100)

    def lambda_1835():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1835)

    def lambda_1846():
        OP_96(0xFE, 0xFFFFDE68, 0x258, 0xFFFFBF8C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1846)
    WaitChrThread(0x102, 1)
    WaitChrThread(0xC, 1)
    OP_6F(0x79)
    Sleep(300)

    def lambda_186D():
        OP_96(0xFE, 0x6A4, 0x0, 0xFFFFC374, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_186D)
    Sleep(100)

    def lambda_188A():
        OP_96(0xFE, 0x3E8, 0x0, 0xFFFFBF8C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_188A)
    Sleep(2500)
    Fade(500)
    OP_68(2600, 900, -15600, 0)
    MoveCamera(325, 23, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetCameraDistance(14000, 1500)

    def lambda_18E3():
        OP_96(0xFE, 0x1004, 0x0, 0xFFFFC5CC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_18E3)
    Sleep(50)

    def lambda_1900():
        OP_96(0xFE, 0x1130, 0x0, 0xFFFFBBA4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1900)
    WaitChrThread(0xA, 1)

    def lambda_191E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_191E)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x101,
        (
            "#12P#00002FEli!\x01",
            "Have you already returned? Is it?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_1EB1")
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x102,
        (
            "#3387V#30WWell, yes, on yesterday.\x02\x03",
            "#3389VMy grandfather's help ended,\x01",
            "I can return from today.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xD3D)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)

    ChrTalk(
        0x101,
        (
            "#12P#00002F#30WI see……\x01",
            "……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xA, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0xA,
        (
            "#01105F#11PHey, why.\x02\x03",
            "Lloyd and Eli,\x01",
            "What's wrong with staring?\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    OP_64(0x102)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1B58():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1B58)

    def lambda_1B65():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1B65)
    TurnDirection(0x101, 0xA, 700)

    ChrTalk(
        0x101,
        (
            "#6P#00011FNo!\x01",
            "It is nothing special!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#5PThat's right.\x01",
            "Because it was a long time ago\x01",
            "It is nostalgic about me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01100F#11PHmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#01902F(Well ….\x01",
            "Something is lovey. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10114F(Hey, after all these two people\x01",
            "Is that kind of relationship …? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#01900F(If it's my opinion\x01",
            "It seems not a definitive relationship. )\x02\x03",
            "#01909F(Eh, if you are interested\x01",
            "There is still the chance, is not it ~? )\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x109, 0xB, 700)
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x109,
        "#11P#10111F(Oh, I … such a thing!\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00109F#5POh, thanks also to Noel.\x02\x03",
            "#00102FDid you not have any danger?\x01",
            "Lloyd, occasionally doing something unreasonable\x01",
            "Because there are things to do … …\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)
    Sleep(150)

    ChrTalk(
        0x109,
        (
            "#12P#10112FNo, no.\x01",
            "Thank you Ellie.\x02\x03",
            "#10100FCertainly Mr. McDaely's relationship\x01",
            "You were traveling around the country, were not you?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1E94():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1E94)
    Sleep(50)

    def lambda_1EA4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1EA4)
    Jump("loc_2027")

    label("loc_1EB1")

    OP_C9(0x0, 0x80000000)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x102,
        (
            "#3388V#30WWell, yesterday.\x02\x03",
            "#3389VMy grandfather's help ended,\x01",
            "I can return from today.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xD3D)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    ChrTalk(
        0x101,
        "#12P#00002FI see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10109FCongratulations, Ellie.\x02\x03",
            "#10100FCertainly Mr. McDaely's relationship\x01",
            "You were traveling around the country, were not you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2027")


    ChrTalk(
        0x102,
        (
            "#00104F#5PYeah, great help\x01",
            "I did not get it though.\x02\x03",
            "#00100FBut, I have various interesting information\x01",
            "I was able to purchase it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FI see……\x01",
            "I will let you hear it later.\x02\x03",
            "#00006FBut with this\x01",
            "Tio and Randy will return\x01",
            "I have not to say ….\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x5, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x5, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x5, 0x3)
    OP_CC(0x0, 0x5, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0xC,
        (
            "Well, during this month\x01",
            "Both of you will come back.\x02\x03",
            "More than that, Lloyd.\x01",
            "Have you properly applied Keli?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x5, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x5, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x5, 0x3)
    OP_CC(0x0, 0x5, 0x0)

    ChrTalk(
        0x101,
        (
            "#12P#00003F……Yes.\x01",
            "Safely, we arrested both.\x02\x03",
            "#00001FMr. Dudley and Mr. Arios\x01",
            "We are protecting you to the detention center.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01003F#5PReally……\x02\x03",
            "#01002FWell, this incident involving a cult\x01",
            "It would be nice to see it settled down.\x02\x03",
            "I think that I know … …\x01",
            "You will have a changeover head.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, that's it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01002F#5PIf you are Noel\x01",
            "Again I beg you to say hello.\x02\x03",
            "Was it okay with today?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2389():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2389)
    Sleep(100)

    def lambda_2399():
        TurnDirection(0xB, 0x109, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_2399)
    Sleep(100)

    def lambda_23A9():
        TurnDirection(0xA, 0x109, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_23A9)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xA, 0)
    Sleep(300)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x109, 0x2C)
    SetChrSubChip(0x109, 0x1)
    OP_0D()
    Sleep(100)
    Sound(2491, 255, 100, 0)
    Sleep(500)

    ChrTalk(
        0x109,
        (
            "#12P#10103FNoel · Seeker!\x02\x03",
            "#10101FFrom today to the Special Affairs Support Division\x01",
            "I will be on my account!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11P#01105FBarking ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#01909FErr …\x01",
            "Your older sister is also a friend in this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01006F#5POh, so much\x01",
            "Awe#2RWhether#You do not have to worry.\x02\x03",
            "#01000FI heard that from Sonya\x01",
            "There is a pace of ours in our place.\x02\x03",
            "Military ceremony#8RA date#Is\x01",
            "Let's just throw it away.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_0D()

    ChrTalk(
        0x109,
        "#12P#10105FWell, I will make an effort.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x105, -9000, 600, -16000, 90)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x105,
        "Voice of a boy",
        (
            "#2904V#30WWhatching\x01",
            "It seems to be complete.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xB58)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-2000, 900, -15600, 3000)
    SetCameraDistance(13500, 3000)

    def lambda_2631():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2631)
    Sleep(50)

    def lambda_2641():
        TurnDirection(0xA, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_2641)
    Sleep(50)

    def lambda_2651():
        TurnDirection(0xB, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_2651)
    Sleep(50)

    def lambda_2661():
        TurnDirection(0xC, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_2661)
    Sleep(50)

    def lambda_2671():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2671)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x102, 0)

    def lambda_2695():

        label("loc_2695")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_2695")

    QueueWorkItem2(0x102, 2, lambda_2695)

    def lambda_26A7():

        label("loc_26A7")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_26A7")

    QueueWorkItem2(0xC, 2, lambda_26A7)

    def lambda_26B9():

        label("loc_26B9")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_26B9")

    QueueWorkItem2(0xB, 2, lambda_26B9)
    Sleep(500)

    def lambda_26CE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_26CE)

    def lambda_26DF():
        OP_95(0xFE, -3000, 0, -16000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_26DF)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        "#10100FAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWadi …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01110FOh, it's you!\x02",
    )

    CloseMessageWindow()

    def lambda_2744():
        OP_95(0xFE, 1700, 0, -15500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2744)
    Sleep(800)
    Fade(500)
    OP_68(2600, 900, -15600, 0)
    MoveCamera(325, 23, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    Sleep(500)

    def lambda_2797():
        OP_96(0xFE, 0x802, 0x0, 0xFFFFC856, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2797)
    WaitChrThread(0x105, 1)

    def lambda_27B5():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_27B5)
    WaitChrThread(0x102, 1)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x105,
        (
            "#10304F#2905V#5P#30WHuh, I work hard for you.\x02\x03",
            "#10300F#2906VWith that condition\x01",
            "You seem to have done well?\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xB5A)

    ChrTalk(
        0x101,
        (
            "#12P#00000FOh, because there was information about Wadi\x01",
            "Also in the information store in Altair City\x01",
            "I managed to get in touch … …\x02\x03",
            "#00006F…… Where on earth?\x01",
            "Did you buy such information?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309F#5PHuh … … The snake's way is a snake.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(3150, 900, -15230, 1500)

    def lambda_2912():
        OP_95(0xFE, 3150, 0, -15400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2912)
    WaitChrThread(0x105, 1)
    EndChrThread(0x102, 0x2)
    EndChrThread(0xC, 0x2)

    def lambda_2938():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2938)
    EndChrThread(0xB, 0x2)
    OP_6F(0x79)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x4, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CC(0x0, 0x4, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(150)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x105,
        (
            "#2901V#30W── It is for the other you never.\x01",
            "I'm glad if it helps.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xB55)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x4, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CC(0x0, 0x4, 0x0)

    ChrTalk(
        0x102,
        "#5P#00105FIt is! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#6P#01905FWow …!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#12P#00011FCha, close!\x02\x03",
            "Why are you going around! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10309FHaha, that's a complaint.\x02\x03",
            "Because your reaction is interesting\x01",
            "Is not it decided?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00013FOh, that …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00111FWas you, you …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10112FHaha ……\x01",
            "(It is a mysterious child after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#01109F#11PHehe.\x01",
            "Something funny.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#01906FOkay, the Special Affairs Division ……\x02\x03",
            "Both my sister and Keia are there,\x01",
            "I can see Mr. Lloyd in need.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 500)

    ChrTalk(
        0x101,
        (
            "#00012F#11PDisagreeable!\x01",
            "Even if envy is troubled!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01006F#5PWhew ……\x01",
            "Try to avoid being so jaaled.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(2400, 1100, -16300, 0)
    MoveCamera(55, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    SetChrPos(0xC, 1100, 0, -17200, 0)
    SetChrPos(0xA, 4000, 0, -14700, 0)
    SetChrPos(0x101, 3700, 0, -15400, 0)
    SetChrPos(0x109, 3900, 0, -16900, 0)
    SetChrPos(0xB, 4400, 0, -17500, 0)
    SetChrPos(0x102, 2000, 0, -14100, 0)
    SetChrPos(0x105, 3150, 0, -15400, 90)
    TurnDirection(0xC, 0x101, 0)

    def lambda_2D26():
        TurnDirection(0x101, 0xC, 0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D26)
    Sleep(0)

    def lambda_2D36():
        TurnDirection(0x109, 0xC, 0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2D36)
    Sleep(0)

    def lambda_2D46():
        TurnDirection(0x102, 0xC, 0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2D46)
    Sleep(0)

    def lambda_2D56():
        TurnDirection(0xB, 0xC, 0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_2D56)
    Sleep(0)

    def lambda_2D66():
        TurnDirection(0xA, 0xC, 0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_2D66)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xA, 0)

    def lambda_2D8A():
        OP_96(0xFE, 0x9C4, 0x0, 0xFFFFC504, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2D8A)
    WaitChrThread(0x105, 1)
    TurnDirection(0x105, 0xC, 500)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#6P#01003F── Anyway.\x01",
            "This is the\x01",
            "It is a starting member.\x02\x03",
            "#01000FAs a leader,\x01",
            "Lloyd Bannings.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00000F#3317V#30W……Yes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#01000FAssistant Leader,\x01",
            "Ely McDael.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00102F#3390V#5P#30WYes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#01003FDeployment from the guard,\x01",
            "Noel · Seeker.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10102F#3514V#11P#30WYes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#01000FAs a temporary associate member\x01",
            "Wadi Hemisphere.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        "#10304F#2907V#5P#30WJa#4RYa#.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#01004FToday, with 18:30\x01",
            "Proclaim the restart of the Special Affairs Support Division.\x02\x03",
            "#01002FMore fun work than before\x01",
            "Because it is supposed to fly in\x01",
            "You should look forward to it - ─\x02",
        )
    )

    CloseMessageWindow()
    StopSound(835, 2000, 100)
    SetCameraDistance(14500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_F0(0x0, 0xA)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_op.pmf", 0x34, 0x0)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    StopBGM(0x1F4)
    WaitBGM()
    OP_29(0xA0, 0x1, 0x3)
    OP_29(0xA0, 0x4, 0x10)
    OP_E5(0xA)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E5(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_E0(0x1C, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C9(0x0, 0x10)
    OP_C9(0x0, 0x10000)
    SetScenarioFlags(0x25, 0)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x25, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    OP_C9(0x1, 0x10)
    OP_E5(0xB)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_772 end

    def Function_3_3143(): pass

    label("Function_3_3143")

    Sound(452, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x3D, 0x168, 0x0, 0x0)
    Sleep(2000)

    def lambda_3161():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3161)
    OP_79(0x1)
    Sound(143, 0, 100, 0)
    OP_82(0x96, 0x96, 0xBB8, 0x1F4)
    Sleep(500)
    Return()

    # Function_3_3143 end

    def Function_4_3187(): pass

    label("Function_4_3187")

    SetChrPos(0xFE, 22700, 0, -9700, 180)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_31A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_31A8)
    OP_95(0xFE, 22700, 0, -12800, 2000, 0x0)
    OP_95(0xFE, 7300, 0, -12800, 2000, 0x0)
    Return()

    # Function_4_3187 end

    def Function_5_31DD(): pass

    label("Function_5_31DD")

    SetChrPos(0xFE, 22700, 0, -9700, 180)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_31FE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_31FE)
    OP_95(0xFE, 22700, 0, -12800, 2000, 0x0)
    OP_95(0xFE, 8500, 0, -12800, 2000, 0x0)
    Return()

    # Function_5_31DD end

    def Function_6_3233(): pass

    label("Function_6_3233")

    SetChrPos(0xFE, 19700, 100, -9700, 180)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3254():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3254)
    OP_95(0xFE, 19700, 0, -12800, 2000, 0x0)
    OP_95(0xFE, 0, 0, -12800, 2000, 0x0)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_6_3233 end

    def Function_7_328E(): pass

    label("Function_7_328E")

    ClearScenarioFlags(0x0, 0)

    def lambda_3296():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3296)
    OP_95(0xFE, 22700, 0, -13700, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_AD(0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, 0, 0, -13700, 2000, 0x0)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_7_328E end

    def Function_8_32E1(): pass

    label("Function_8_32E1")


    def lambda_32E6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_32E6)
    OP_95(0xFE, 22700, 0, -12700, 2000, 0x0)
    Sleep(500)
    SetScenarioFlags(0x0, 0)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, 0, 0, -12700, 2000, 0x0)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_8_32E1 end

    def Function_9_332D(): pass

    label("Function_9_332D")


    def lambda_3332():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3332)
    OP_95(0xFE, 32500, 0, -12700, 4000, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0xFE, 0, 0, -12700, 4000, 0x0)
    OP_64(0xFE)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_9_332D end

    def Function_10_3381(): pass

    label("Function_10_3381")

    OP_95(0xFE, 7500, 0, -13700, 2000, 0x0)
    OP_95(0xFE, 4800, 0, -16700, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_10_3381 end

    def Function_11_33B1(): pass

    label("Function_11_33B1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10900.itc", 0x1E)
    LoadChrToIndex("chr/ch12400.itc", 0x1F)
    LoadChrToIndex("chr/ch11100.itc", 0x20)
    LoadChrToIndex("chr/ch11300.itc", 0x21)
    LoadChrToIndex("chr/ch41000.itc", 0x22)
    LoadChrToIndex("chr/ch41100.itc", 0x23)
    LoadChrToIndex("apl/ch51231.itc", 0x24)
    LoadChrToIndex("chr/ch27600.itc", 0x25)
    LoadChrToIndex("chr/ch27800.itc", 0x26)
    LoadChrToIndex("chr/ch28400.itc", 0x27)
    SoundLoad(963)
    SoundLoad(825)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07400.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07200.itp")
    CreatePortrait(2, 16, 200, 528, 264, 0, 0, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis514.itp")
    CreatePortrait(3, 16, 200, 528, 264, 0, 0, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis515.itp")
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x11, 0x25)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x26)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x27)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x24)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x24)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x24)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x1A, 0x23)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    OP_A7(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1B, 0x23)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1C, 0x22)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x24, 0x80)
    OP_78(0x3, 0x24)
    OP_49()
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x1000)
    OP_74(0x3, 0x1E)
    OP_70(0x3, 0x5A)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x1, 0x1000)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x11, 33000, 0, 3300, 0)
    SetChrPos(0x12, 20500, 0, 3300, 0)
    SetChrPos(0x13, -2900, 0, 3450, 315)
    SetChrPos(0x14, 40000, 0, 1500, 315)
    SetChrPos(0x15, 40750, 0, 2250, 315)
    SetChrPos(0x16, 22500, 0, 1000, 0)
    SetChrPos(0x17, 23500, 0, 1000, 0)
    SetChrPos(0x24, 38000, -1500, 8000, 90)
    OP_D5(0x24, 0x0, 0x15F90, 0x0, 0x0)
    OP_68(-7250, 1500, 8000, 0)
    MoveCamera(315, 5, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(24000, 0)
    OP_F0(0x0, 0x1)
    OP_68(41000, 1500, 8000, 8500)
    MoveCamera(310, 5, 0, 8500)
    SetCameraDistance(20000, 8500)
    BeginChrThread(0x24, 1, 0, 12)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x24, 1)
    Fade(500)
    SetChrPos(0xD, 37000, 0, 6800, 180)
    SetChrPos(0xE, 37000, 0, 6800, 180)
    SetChrPos(0x1A, 37000, 0, 6800, 180)
    SetChrPos(0x1B, 37000, 0, 6800, 180)
    SetChrPos(0x1C, 37000, 0, 6800, 180)
    SetChrPos(0xF, 24000, 0, 6800, 180)
    SetChrPos(0x10, 24000, 0, 6800, 180)
    SetChrPos(0x1D, 24000, 0, 6800, 180)
    SetChrPos(0x11, 33000, 0, 3300, 90)
    SetChrPos(0x12, 20500, 0, 2000, 0)
    SetChrPos(0x24, 45000, -1500, 8000, 90)
    OP_D5(0x24, 0x0, 0x15F90, 0x0, 0x0)
    OP_68(37000, 700, 3800, 0)
    MoveCamera(35, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    MoveCamera(40, 13, 0, 5000)
    SetCameraDistance(16000, 5000)
    OP_0D()
    Sound(454, 0, 100, 0)
    OP_71(0x3, 0x1, 0x1E, 0x0, 0x8)
    OP_79(0x3)
    BeginChrThread(0x1A, 1, 0, 13)
    Sleep(750)
    BeginChrThread(0x1B, 1, 0, 15)
    Sleep(750)
    BeginChrThread(0x1C, 1, 0, 17)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x1B, 1)
    WaitChrThread(0x1C, 1)
    OP_6F(0x79)
    BeginChrThread(0xD, 1, 0, 19)
    Sleep(750)
    BeginChrThread(0xE, 1, 0, 21)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    OP_6F(0x79)
    BeginChrThread(0x11, 1, 0, 36)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(3500)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    EndChrThread(0x11, 0x1)
    OP_64(0x11)
    OP_64(0xD)
    BeginChrThread(0x11, 1, 0, 23)
    Sleep(750)
    BeginChrThread(0xD, 1, 0, 20)
    Sleep(100)
    BeginChrThread(0xE, 1, 0, 22)
    Sleep(100)
    BeginChrThread(0x1C, 1, 0, 18)
    Sleep(100)
    BeginChrThread(0x1B, 1, 0, 16)
    Sleep(100)
    BeginChrThread(0x1A, 1, 0, 14)
    OP_68(24000, 700, 3800, 10000)
    MoveCamera(45, 33, 0, 10000)
    Sleep(8000)
    Sleep(1500)
    BeginChrThread(0x1D, 1, 0, 28)
    Sleep(100)
    BeginChrThread(0x12, 1, 0, 34)
    WaitChrThread(0x1D, 1)
    WaitChrThread(0x12, 1)
    OP_6F(0x79)
    BeginChrThread(0xF, 1, 0, 30)
    Sleep(750)
    BeginChrThread(0x10, 1, 0, 32)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x10, 1)
    OP_6F(0x79)
    BeginChrThread(0x12, 1, 0, 37)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(3500)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    EndChrThread(0x12, 0x1)
    OP_64(0x12)
    OP_64(0xF)
    OP_68(15000, 700, 3800, 10000)
    BeginChrThread(0x12, 1, 0, 35)
    Sleep(750)
    BeginChrThread(0xF, 1, 0, 31)
    Sleep(100)
    BeginChrThread(0x10, 1, 0, 33)
    Sleep(100)
    BeginChrThread(0x1D, 1, 0, 25)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 2)
    NewScene("c1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_33B1 end

    def Function_12_3B1C(): pass

    label("Function_12_3B1C")

    Sound(963, 0, 100, 0)
    Sound(825, 2, 50, 0)
    OP_71(0x3, 0x5A, 0x168, 0x0, 0x8)
    Sleep(2000)

    def lambda_3B3C():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3B3C)
    OP_79(0x3)
    OP_82(0x96, 0x96, 0xBB8, 0x1F4)
    Sound(143, 0, 100, 0)
    StopSound(825, 500, 50)
    Sleep(500)
    Return()

    # Function_12_3B1C end

    def Function_13_3B68(): pass

    label("Function_13_3B68")


    def lambda_3B6D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3B6D)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 40000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_13_3B68 end

    def Function_14_3BA4(): pass

    label("Function_14_3BA4")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_14_3BA4 end

    def Function_15_3BBB(): pass

    label("Function_15_3BBB")


    def lambda_3BC0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3BC0)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 39000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_15_3BBB end

    def Function_16_3BF7(): pass

    label("Function_16_3BF7")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_16_3BF7 end

    def Function_17_3C0E(): pass

    label("Function_17_3C0E")


    def lambda_3C13():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3C13)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 38000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_17_3C0E end

    def Function_18_3C4A(): pass

    label("Function_18_3C4A")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_18_3C4A end

    def Function_19_3C61(): pass

    label("Function_19_3C61")


    def lambda_3C66():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3C66)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_68(35000, 700, 3300, 2000)
    OP_95(0xFE, 35000, 0, 3300, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_19_3C61 end

    def Function_20_3CAE(): pass

    label("Function_20_3CAE")

    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_20_3CAE end

    def Function_21_3CBE(): pass

    label("Function_21_3CBE")


    def lambda_3CC3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3CC3)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 35750, 0, 2500, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_21_3CBE end

    def Function_22_3CFA(): pass

    label("Function_22_3CFA")

    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_22_3CFA end

    def Function_23_3D0A(): pass

    label("Function_23_3D0A")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_23_3D0A end

    def Function_24_3D21(): pass

    label("Function_24_3D21")


    def lambda_3D26():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3D26)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 27000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_24_3D21 end

    def Function_25_3D5D(): pass

    label("Function_25_3D5D")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_25_3D5D end

    def Function_26_3D74(): pass

    label("Function_26_3D74")


    def lambda_3D79():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3D79)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 26000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_26_3D74 end

    def Function_27_3DB0(): pass

    label("Function_27_3DB0")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_27_3DB0 end

    def Function_28_3DC7(): pass

    label("Function_28_3DC7")


    def lambda_3DCC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3DCC)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 25000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_28_3DC7 end

    def Function_29_3E03(): pass

    label("Function_29_3E03")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_29_3E03 end

    def Function_30_3E1A(): pass

    label("Function_30_3E1A")


    def lambda_3E1F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3E1F)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_68(22000, 700, 3300, 2000)
    OP_95(0xFE, 22000, 0, 3300, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_30_3E1A end

    def Function_31_3E67(): pass

    label("Function_31_3E67")

    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_31_3E67 end

    def Function_32_3E77(): pass

    label("Function_32_3E77")


    def lambda_3E7C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3E7C)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 22750, 0, 2500, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_32_3E77 end

    def Function_33_3EB3(): pass

    label("Function_33_3EB3")

    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_33_3EB3 end

    def Function_34_3EC3(): pass

    label("Function_34_3EC3")

    OP_95(0xFE, 20500, 0, 3300, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_34_3EC3 end

    def Function_35_3EDF(): pass

    label("Function_35_3EDF")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_35_3EDF end

    def Function_36_3EF6(): pass

    label("Function_36_3EF6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F3C")
    OP_63(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x11)
    Sleep(500)
    OP_63(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xD)
    Sleep(500)
    Jump("Function_36_3EF6")

    label("loc_3F3C")

    Return()

    # Function_36_3EF6 end

    def Function_37_3F3D(): pass

    label("Function_37_3F3D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F83")
    OP_63(0x12, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x12)
    Sleep(500)
    OP_63(0xF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xF)
    Sleep(500)
    Jump("Function_37_3F3D")

    label("loc_3F83")

    Return()

    # Function_37_3F3D end

    def Function_38_3F84(): pass

    label("Function_38_3F84")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch46400.itc", 0x1E)
    OP_68(-1390, 2700, -10, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, -10000, 600, 700, 90)
    SetChrPos(0x102, -10000, 600, -600, 90)
    SetChrPos(0x103, -11500, 600, -700, 90)
    SetChrPos(0x104, -11500, 600, 650, 90)
    SetChrPos(0x109, -13000, 600, -600, 90)
    SetChrPos(0x105, -13000, 600, 700, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x20, 0x1E)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, -9500, 600, 40, 90)

    def lambda_405D():
        OP_95(0x20, 1000, 600, 40, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_405D)
    Sleep(800)

    def lambda_407A():
        OP_95(0x101, 200, 0, 700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_407A)
    Sleep(200)

    def lambda_4097():
        OP_95(0x102, 300, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4097)
    Sleep(300)

    def lambda_40B4():
        OP_95(0x103, -1000, 0, -950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_40B4)
    Sleep(100)

    def lambda_40D1():
        OP_95(0x104, -1100, 0, 1100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_40D1)
    Sleep(200)

    def lambda_40EE():
        OP_95(0x109, -2500, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_40EE)
    Sleep(50)

    def lambda_410B():
        OP_95(0x105, -2400, 0, 700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_410B)
    OP_68(-1390, 1500, -10, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x20, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_4200():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4200)
    Sleep(50)

    def lambda_4210():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4210)
    Sleep(50)

    def lambda_4220():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4220)
    Sleep(10)

    def lambda_4230():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4230)
    Sleep(30)

    def lambda_4240():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4240)
    Sleep(10)

    def lambda_4250():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4250)
    Sleep(10)

    def lambda_4260():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_4260)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x20, 2)

    ChrTalk(
        0x101,
        "#00005Fthis is……\x02",
    )

    CloseMessageWindow()
    OP_68(-1120, 1500, -24350, 5000)
    MoveCamera(45, 30, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(24120, 5000)
    OP_6F(0x79)
    OP_68(6950, 1500, -25730, 5000)
    MoveCamera(11, 16, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(19540, 5000)
    OP_6F(0x79)
    SetMessageWindowPos(50, 50, -1, -1)

    AnonymousTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00100FPrivate train of the Imperial government,\x01",
            "\"Eisengraf issue\".\x02\x03",
            "#00103FThis luxurious appearance ……\x01",
            "It looks like it symbolizes the empire.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 50, -1, -1)

    AnonymousTalk(
        0x109,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10103Fsurely……\x01",
            "It is exactly like a dignified enthusiast.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 50, -1, -1)

    AnonymousTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00300FThat 's \"Iron Blood Chancellor\" is a guy\x01",
            "I entered the crossbell.\x02\x03",
            "#00306FIt certainly has enough impact,\x01",
            "Donbling outstanding\x01",
            "It is a story to get along well.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 50, -1, -1)

    AnonymousTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10300FOh, and how to apply Mira\x01",
            "It seems not to be half end.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(-160, 1500, 410, 0)
    MoveCamera(42, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16250, 0)
    OP_93(0x101, 0xB4, 0x0)
    OP_93(0x102, 0xB4, 0x0)
    OP_93(0x103, 0xB4, 0x0)
    OP_93(0x104, 0xB4, 0x0)
    OP_93(0x109, 0xB4, 0x0)
    OP_93(0x105, 0xB4, 0x0)
    OP_93(0x20, 0x10E, 0x0)
    OP_0D()

    ChrTalk(
        0x103,
        (
            "#00203F…… What is amazing\x01",
            "It seems that it is not just looks.\x02\x03",
            "#00200FAnything this train,\x01",
            "Even in the presence train which is now\x01",
            "It seems to boast of the highest speed.\x02\x03",
            "Clear information\x01",
            "Because it is not published\x01",
            "I can not say for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FWell, maybe ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FTruly throughout the country\x01",
            "Erebonia Empire laying the railway network … …\x02\x03",
            "#00101FRegarding the field of railway\x01",
            "I do not care for other things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FOh, do not know again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "- Gwong.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "So, I'd like to talk about work\x01",
            "Are you ready?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4706():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4706)
    Sleep(50)

    def lambda_4716():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4716)
    Sleep(30)

    def lambda_4726():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4726)
    Sleep(20)

    def lambda_4736():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4736)
    Sleep(40)

    def lambda_4746():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4746)
    Sleep(20)

    def lambda_4756():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4756)
    WaitChrThread(0x105, 2)

    ChrTalk(
        0x101,
        (
            "#00005FWell, sorry.\x01",
            "I was surprised by too much prostitution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, of course it is OK.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "Well, fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Well, as I said earlier\x01",
            "I would like to ask you guys\x01",
            "I'm helping the train inspection work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Specifically, all of the passengers\x01",
            "Entry application and baggage check.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Then, the train itself\x01",
            "We will carry out safety check sharing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FUm, the train's\x01",
            "What is a safety check?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Oh, this is my help.\x01",
            "Just follow the instructions\x01",
            "I would like you to perform various inspection work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Hmm, you guys\x01",
            "Were there six people in all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Then, all three pairs of two people -\x01",
            "Guest room Sharing inspection of the vehicle by two sets,\x01",
            "I want one pair to help me.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4B06")

    ChrTalk(
        0x101,
        (
            "#00005FAre you looking over at pairs of two?\x01",
            "Surely it used to be like a single person ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYeah, at least before\x01",
            "It was so when I helped out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "Oh, you guys were experienced people.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Definitely always\x01",
            "I am doing it by one person,\x01",
            "Now the alert level is rising.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "For a more rigorous check,\x01",
            "This time I will ask you for this posture.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BDD")

    label("loc_4B06")


    ChrTalk(
        0x101,
        (
            "#00005FExamination by two pairs … …\x01",
            "Is that always like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "No, as usual\x01",
            "I am doing it by one person,\x01",
            "Now the alert level is rising.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "For a more rigorous check,\x01",
            "This time I will ask you for this posture.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BDD")


    ChrTalk(
        0x101,
        "#00000FIndeed, I understood the circumstances.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Well then, immediately\x01",
            "Will it be divided into three groups?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "Whatever you can decide with Janken.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FIs it Ja, Janken?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Well honest stories, not so individual\x01",
            "It's not a question of suitability.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "As here\x01",
            "I want to get to work as soon as possible,\x01",
            "You ought to be quick as well as you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, if that's the case\x01",
            "That's fine, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHuh, if that's a rule.\x01",
            "I hope it will be fun ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FBut, specifically\x01",
            "How do you decide?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Oh, then.\x01",
            "How about these rules?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Together with the way of Janken all at once,\x01",
            "If only two people had the same hand\x01",
            "They will become a \"set\" and they pass through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "It is iteration until it is decided.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FEr …\x01",
            "How you say, are not you familiar?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "Well, well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Actually, among the republic examiners\x01",
            "To occasionally take a break, occasionally like this\x01",
            "We decide on sharing etc.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "There are no hardworking imperial inspectors\x01",
            "It's a flexible idea.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00106FWhether it is a flexible idea or not\x01",
            "I do not know but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FTentatively,\x01",
            "Is this also a difference in your country?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FHello, maybe.\x02\x03",
            "Well, anyway\x01",
            "Let's try it quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, would you?\x02",
    )

    CloseMessageWindow()

    def lambda_50F5():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_50F5)
    Sleep(10)

    def lambda_5105():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5105)
    Sleep(10)

    def lambda_5115():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5115)
    Sleep(10)

    def lambda_5125():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5125)
    Sleep(30)

    def lambda_5135():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5135)
    Sleep(10)

    def lambda_5145():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5145)
    WaitChrThread(0x105, 2)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00003FWell, everyone.\x01",
            "\"I will go with you\" will go.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "To put out goo\x01",        # 0
            "Give out a choke\x01",      # 1
            "Put out par\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 39)
    BeginChrThread(0x102, 3, 0, 39)
    BeginChrThread(0x103, 3, 0, 39)
    BeginChrThread(0x104, 3, 0, 39)
    BeginChrThread(0x109, 3, 0, 39)
    BeginChrThread(0x105, 3, 0, 39)
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("All of us")

    AnonymousTalk(
        0xFF,
        "#4S#11AAnything … …\x02",
    )

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)

    def lambda_525D():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_525D)

    def lambda_5272():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5272)

    def lambda_5287():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5287)

    def lambda_529C():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_529C)

    def lambda_52B1():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_52B1)

    def lambda_52C6():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_52C6)
    Sound(802, 0, 100, 0)
    SetChrName("All of us")

    AnonymousTalk(
        0xFF,
        "#4S#11ATo\x02",
    )

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59B6")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_533F():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_533F)

    def lambda_5354():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5354)

    def lambda_5369():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5369)

    def lambda_537E():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_537E)

    def lambda_5393():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5393)

    def lambda_53A8():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_53A8)
    WaitChrThread(0x101, 1)

    def lambda_53C1():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_53C1)
    Sleep(50)

    def lambda_53D1():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_53D1)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00100FHuhu, only me and Tio\x01",
            "It's chocolate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThat means,\x01",
            "I am a pair with Eri.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FSo, the rest are three guo and one par.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FThen,\x01",
            "It is redoing with the remaining four people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, let's keep going then.\x02",
    )

    CloseMessageWindow()

    def lambda_54DB():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_54DB)
    Sleep(50)

    def lambda_54EB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_54EB)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "To put out goo\x01",        # 0
            "Give out a choke\x01",      # 1
            "Put out par\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 39)
    BeginChrThread(0x104, 3, 0, 39)
    BeginChrThread(0x109, 3, 0, 39)
    BeginChrThread(0x105, 3, 0, 39)
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("All of us")

    AnonymousTalk(
        0xFF,
        "#4S#11AAnything\x02",
    )

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x101, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)

    def lambda_55AD():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_55AD)

    def lambda_55C2():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_55C2)

    def lambda_55D7():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_55D7)

    def lambda_55EC():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_55EC)
    Sound(802, 0, 100, 0)
    SetChrName("All of us")

    AnonymousTalk(
        0xFF,
        "#4S#11ATo\x02",
    )

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_567A():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_567A)

    def lambda_568F():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_568F)

    def lambda_56A4():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_56A4)

    def lambda_56B9():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_56B9)
    WaitChrThread(0x101, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57CC")

    def lambda_56E1():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_56E1)
    Sleep(50)

    def lambda_56F1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_56F1)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00005FIs me and Noel Goo?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FHehe, Mr. Lloyd.\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_575A():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_575A)
    Sleep(50)

    def lambda_576A():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_576A)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00300FThen,\x01",
            "It is a pair of me and wadi that remained.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHuh, good luck.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 4)
    Jump("loc_59B1")

    label("loc_57CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58C0")

    def lambda_57E0():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57E0)
    Sleep(50)

    def lambda_57F0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_57F0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00005FI and I are choppers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHuh, good luck.\x02",
    )

    CloseMessageWindow()

    def lambda_5840():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5840)
    Sleep(50)

    def lambda_5850():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5850)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00300FThen,\x01",
            "The remaining me and Noel are a pair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FThat's fine, thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 5)
    Jump("loc_59B1")

    label("loc_58C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59B1")

    def lambda_58D4():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_58D4)
    Sleep(50)

    def lambda_58E4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_58E4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00005FAre you and Randy a par.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FOh, I'm begging for you.\x02",
    )

    CloseMessageWindow()

    def lambda_593A():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_593A)
    Sleep(50)

    def lambda_594A():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_594A)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10100FThat means,\x01",
            "I remained and Waji are you a pair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FYou know, Yoshi.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 3)

    label("loc_59B1")

    Jump("loc_61F1")

    label("loc_59B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6060")
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_59F1():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_59F1)

    def lambda_5A06():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5A06)

    def lambda_5A1B():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5A1B)

    def lambda_5A30():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5A30)

    def lambda_5A45():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5A45)

    def lambda_5A5A():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5A5A)
    WaitChrThread(0x101, 1)

    def lambda_5A73():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5A73)
    Sleep(50)

    def lambda_5A83():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5A83)
    Sleep(300)

    ChrTalk(
        0x104,
        "#00305FHmm, is only me and Noel goo?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FThat means,\x01",
            "I am a pair with Randy-senpai.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FAnd the rest to 3 guys, Park 1 and.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThat means,\x01",
            "I tried again with the remaining four people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, let's keep going then.\x02",
    )

    CloseMessageWindow()

    def lambda_5B88():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5B88)
    Sleep(50)

    def lambda_5B98():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5B98)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "To put out goo\x01",        # 0
            "Give out a choke\x01",      # 1
            "Put out par\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 39)
    BeginChrThread(0x102, 3, 0, 39)
    BeginChrThread(0x103, 3, 0, 39)
    BeginChrThread(0x105, 3, 0, 39)
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("All of us")

    AnonymousTalk(
        0xFF,
        "#4S#11AAnything\x02",
    )

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    EndChrThread(0x105, 0x3)

    def lambda_5C5A():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C5A)

    def lambda_5C6F():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5C6F)

    def lambda_5C84():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5C84)

    def lambda_5C99():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5C99)
    Sound(802, 0, 100, 0)
    SetChrName("All of us")

    AnonymousTalk(
        0xFF,
        "#4S#11ATo\x02",
    )

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5D27():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D27)

    def lambda_5D3C():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D3C)

    def lambda_5D51():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5D51)

    def lambda_5D66():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5D66)
    WaitChrThread(0x101, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E73")

    def lambda_5D8E():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D8E)
    Sleep(50)

    def lambda_5D9E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5D9E)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00005FAre you and Tio Goo?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FMr. Lloyd.\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5DFF():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5DFF)
    Sleep(50)

    def lambda_5E0F():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5E0F)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00100FThat means,\x01",
            "The remaining me and Wajima pair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FYou know, Yoshi.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 2)
    Jump("loc_605B")

    label("loc_5E73")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F6E")

    def lambda_5E87():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E87)
    Sleep(50)

    def lambda_5E97():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5E97)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00005FI and I are choppers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHuh, good luck.\x02",
    )

    CloseMessageWindow()

    def lambda_5EE7():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5EE7)
    Sleep(50)

    def lambda_5EF7():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5EF7)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00100FThat means,\x01",
            "It is a combination of me and Tio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FEllie.\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 5)
    Jump("loc_605B")

    label("loc_5F6E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_605B")

    def lambda_5F82():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F82)
    Sleep(50)

    def lambda_5F92():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5F92)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00005FAre you and Ellie Par?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHehe, please.\x02",
    )

    CloseMessageWindow()

    def lambda_5FE2():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5FE2)
    Sleep(50)

    def lambda_5FF2():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5FF2)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00200FThat means that I left\x01",
            "Was this pair?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FYou know, Yoshi.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 1)

    label("loc_605B")

    Jump("loc_61F1")

    label("loc_6060")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61F1")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_60E9():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_60E9)

    def lambda_60FE():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_60FE)

    def lambda_6113():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6113)

    def lambda_6128():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6128)

    def lambda_613D():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_613D)

    def lambda_6152():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6152)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#00005FOh, it was splendidly splendid again.\x02\x03",
            "#00000FWadi and I, Eli and Tio,\x01",
            "Besides, is Randy and Noel a pair?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHuh, good luck.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 5)

    label("loc_61F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 1)), scpexpr(EXPR_END)), "loc_6208")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_625F")

    label("loc_6208")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 2)), scpexpr(EXPR_END)), "loc_621F")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_625F")

    label("loc_621F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 3)), scpexpr(EXPR_END)), "loc_6236")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_625F")

    label("loc_6236")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 4)), scpexpr(EXPR_END)), "loc_624D")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_625F")

    label("loc_624D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 5)), scpexpr(EXPR_END)), "loc_625F")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_625F")


    ChrTalk(
        0x20,
        "Hmm, apparently it seems.\x02",
    )

    CloseMessageWindow()

    def lambda_628C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_628C)
    Sleep(10)

    def lambda_629C():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_629C)
    Sleep(10)

    def lambda_62AC():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_62AC)
    Sleep(10)

    def lambda_62BC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_62BC)
    Sleep(30)

    def lambda_62CC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_62CC)
    Sleep(10)

    def lambda_62DC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_62DC)
    WaitChrThread(0x105, 2)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00000FWhat shall we do to share it?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 4)), scpexpr(EXPR_END)), "loc_6413")

    ChrTalk(
        0x20,
        "That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Because I'm going to have something move\x01",
            "This is where I want men's hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FTsutomu, do you name me a wadi?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FWhew.\x01",
            "It is a story that is likely to be used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Well, that's wrong.\x01",
            "I will use it for the full eye.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64E4")

    label("loc_6413")


    ChrTalk(
        0x109,
        (
            "#10105FOh, why?\x01",
            "Shall I help you?\x02\x03",
            "#10100FIf you inspect the vehicle\x01",
            "Because I have experience with the guard\x01",
            "I think that I can help you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x20,
        (
            "Indeed, is that so?\x01",
            "Hmm, would you be able to ask for it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64E4")


    ChrTalk(
        0x20,
        (
            "Okay baby\x01",
            "Let's start the business at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Guest room vehicle check\x01",
            "I left it to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "I have already announced it,\x01",
            "If you name \"assistant inspector\"\x01",
            "You should be able to do business without delay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, that's OK.\x02",
    )

    CloseMessageWindow()
    StopSound(835, 1000, 90)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x20, 0x0)
    SetChrFlags(0x20, 0x80)
    OP_D7(0x1E)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 1)), scpexpr(EXPR_END)), "loc_65F7")
    AddParty(0x1, 0xFF, 0xFF)
    Jump("loc_6643")

    label("loc_65F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 2)), scpexpr(EXPR_END)), "loc_6609")
    AddParty(0x2, 0xFF, 0xFF)
    Jump("loc_6643")

    label("loc_6609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 3)), scpexpr(EXPR_END)), "loc_661B")
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_6643")

    label("loc_661B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 4)), scpexpr(EXPR_END)), "loc_662D")
    AddParty(0x8, 0xFF, 0xFF)
    Jump("loc_6643")

    label("loc_662D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 5)), scpexpr(EXPR_END)), "loc_663F")
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_6643")

    label("loc_663F")

    AddParty(0x1, 0xFF, 0xFF)

    label("loc_6643")

    SetScenarioFlags(0x22, 3)
    NewScene("e0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_38_3F84 end

    def Function_39_6650(): pass

    label("Function_39_6650")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6680")

    def lambda_6660():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6660)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    Jump("Function_39_6650")

    label("loc_6680")

    Return()

    # Function_39_6650 end

    def Function_40_6681(): pass

    label("Function_40_6681")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch46400.itc", 0x1E)
    OP_68(520, 1500, 270, 0)
    MoveCamera(42, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16250, 0)
    SetChrPos(0x101, 200, 0, 700, 90)
    SetChrPos(0x102, 300, 0, -600, 90)
    SetChrPos(0x103, -1000, 0, -950, 90)
    SetChrPos(0x104, -1100, 0, 1100, 90)
    SetChrPos(0x109, -2500, 0, -600, 90)
    SetChrPos(0x105, -2400, 0, 700, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x20, 0x1E)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, 2200, 600, 40, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x20,
        "Hmm, everyone good worked.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Especially for tickets\x01",
            "The one who stole the riot would have been serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, so much too\x01",
            "Because I could not do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FBy the way, thieves\x01",
            "Is it possible to identify it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "Oh, it's possible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "For this kind of occasion\x01",
            "Ticket purchaser information\x01",
            "Because I refrain from it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "If theft is found by investigation,\x01",
            "You will catch it at the station.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FI see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FHowever, the victim's grandfather\x01",
            "What happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Oh, because the old man rushed\x01",
            "Once the ticket is taken\x01",
            "I bought you back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "If thieves are caught safely\x01",
            "Do not make the criminal compensate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHuh, the old man is also a disaster.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FWell, immediately\x01",
            "It seems possible to solve it, than anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Oh, anyway you guys\x01",
            "He did everything I do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "Thanks, I was saved, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, this is it.\x01",
            "You can say that.\x01",
            "It was good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIf there is something again,\x01",
            "Please feel free to contact us.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Work assistance of Republic examiner】\x07\x00",
            "Achieved!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x79, 0x1, 0xE)
    OP_29(0x79, 0x4, 0x10)
    StopSound(835, 1000, 90)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    SetScenarioFlags(0x22, 2)
    NewScene("c0010", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_40_6681 end

    def Function_41_6B81(): pass

    label("Function_41_6B81")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch46400.itc", 0x1E)
    OP_68(520, 1500, 270, 0)
    MoveCamera(42, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16250, 0)
    SetChrPos(0x101, 200, 0, 700, 90)
    SetChrPos(0x102, 300, 0, -600, 90)
    SetChrPos(0x103, -1000, 0, -950, 90)
    SetChrPos(0x104, -1100, 0, 1100, 90)
    SetChrPos(0x109, -2500, 0, -600, 90)
    SetChrPos(0x105, -2400, 0, 700, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x20, 0x1E)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, 2200, 600, 40, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x20,
        "All the stories were heard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Those who are stolen\x01",
            "It was a really nice day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FNo, so much\x01",
            "Because I have not done anything serious.\x02\x03",
            "#00000FSo, after all, I committed theft\x01",
            "What about the youth?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Oh, that is\x01",
            "I did not feel guilty at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FEr, what is that …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Oh, that's right\x01",
            "An old man who should be a victim\x01",
            "Please tell me you did not steal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Youth is an admission ticket to the last\x01",
            "After entering home, afterwards\x01",
            "Just forget to buy a ticket -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "In such a story,\x01",
            "More than that, we are also pursuing\x01",
            "It has gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FHa, that guy ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWell, this too\x01",
            "I wonder if Sin has put it in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHuh, is not it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FBy the way, if you are a merchant\x01",
            "What happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Oh, actually this one is\x01",
            "It's a big catch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "The identity of the guy is a counterfeit ticket\x01",
            "It was a broker.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FWell, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FBut why on a train?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Oh, apparently\x01",
            "Actually using our products\x01",
            "It seems I was trying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "It is a totally bold guy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FI see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "No, but your success is\x01",
            "It was wonderful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "Thanks, I was saved, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, this is it.\x01",
            "You can say that.\x01",
            "It was good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIf there is something again,\x01",
            "Please feel free to contact us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "Oh, see you again.\x02",
    )

    CloseMessageWindow()
    OP_93(0x20, 0x2D, 0x1F4)
    OP_95(0x20, 5760, 0, 2550, 2000, 0x0)

    def lambda_71D9():
        OP_95(0x20, 24940, 0, 2810, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_71D9)
    Sleep(500)
    OP_68(-1190, 1500, -230, 2000)
    MoveCamera(45, 34, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(15430, 2000)
    Sleep(1500)

    def lambda_7227():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7227)
    Sleep(10)

    def lambda_7237():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7237)
    Sleep(10)

    def lambda_7247():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7247)
    Sleep(10)

    def lambda_7257():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7257)
    Sleep(30)

    def lambda_7267():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7267)
    Sleep(10)

    def lambda_7277():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7277)
    WaitChrThread(0x105, 2)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 1)), scpexpr(EXPR_END)), "loc_7455")

    ChrTalk(
        0x109,
        (
            "#10100FEven so, Shin\x01",
            "It sounds like a big success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHuhu, you can not be at this place\x01",
            "I did not think we would meet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FOh, once again\x01",
            "I was aware of the scales of the big bowl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FI want to go\x01",
            "It is a terrible idiot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FHmm, I wanted to see at first sight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHuff, looks like\x01",
            "It's a cute little boy, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha, for sure.\x02\x03",
            "#00003FAnyway, this is one incident.\x02\x03",
            "#00000FAfter a breather is entered,\x01",
            "Let's face the next job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B63")

    label("loc_7455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 2)), scpexpr(EXPR_END)), "loc_760E")

    ChrTalk(
        0x102,
        (
            "#00100FEven so, Shin\x01",
            "You seem to have been a big success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYeah, I'm still a little young\x01",
            "I was surprised variously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, I will redefine the big bowl again\x01",
            "It is a strange feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FI want to go\x01",
            "It is a terrible idiot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYeah, really.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHuff, looks like\x01",
            "It's a cute little boy, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha, for sure.\x02\x03",
            "#00003FAnyway, this is one incident.\x02\x03",
            "#00000FAfter a breather is entered,\x01",
            "Let's face the next job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B63")

    label("loc_760E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 3)), scpexpr(EXPR_END)), "loc_77C6")

    ChrTalk(
        0x102,
        (
            "#00100FEven so, Shin\x01",
            "You seem to have been a big success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FOh, it feels the same as ever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FBut again, I'm sorry\x01",
            "It is a strange feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FI mean,\x01",
            "It is really terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FHmm, I wanted to see at first sight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHuff, looks like\x01",
            "It's a cute little boy, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha, for sure.\x02\x03",
            "#00003FAnyway, this is one incident.\x02\x03",
            "#00000FAfter a breather is entered,\x01",
            "Let's face the next job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B63")

    label("loc_77C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 4)), scpexpr(EXPR_END)), "loc_7993")

    ChrTalk(
        0x102,
        (
            "#00100FEven so, Shin\x01",
            "You seem to have been a big success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FWell, no way No way\x01",
            "I did not think we would meet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, once again\x01",
            "I was aware of the scales of the big bowl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FI want to go\x01",
            "It is a terrible idiot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FHmm, I wanted to see at first sight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHuff, looks like\x01",
            "It's a cute little boy, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha, for sure.\x02\x03",
            "#00003FAnyway, this is one incident.\x02\x03",
            "#00000FAfter a breather is entered,\x01",
            "Let's face the next job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B63")

    label("loc_7993")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 5)), scpexpr(EXPR_END)), "loc_7B63")

    ChrTalk(
        0x102,
        (
            "#00100FEven so, Shin\x01",
            "You seem to have been a big success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHuh, no doubt like this\x01",
            "I did not think we would meet again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, once again\x01",
            "I was aware of the scales of the big bowl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FI want to go\x01",
            "It is a terrible idiot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FHmm, I wanted to see at first sight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FHuhu, looks pretty\x01",
            "It is a boy, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha, for sure.\x02\x03",
            "#00003FAnyway, this is one incident.\x02\x03",
            "#00000FAfter a breather is entered,\x01",
            "Let's face the next job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B63")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Work assistance of Republic examiner】\x07\x00",
            "Achieved!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x79, 0x1, 0xF)
    OP_29(0x79, 0x4, 0x10)
    StopSound(835, 1000, 90)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    SetScenarioFlags(0x22, 2)
    NewScene("c0010", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_41_6B81 end

    def Function_42_7BEE(): pass

    label("Function_42_7BEE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C87")
    SetChrPos(0x101, -8000, 600, -850, 90)
    SetChrPos(0x102, -8000, 600, 500, 90)
    SetChrPos(0x103, -9150, 600, -1350, 90)
    SetChrPos(0x104, -9150, 600, 1000, 90)
    SetChrPos(0xF4, -10300, 600, -850, 90)
    SetChrPos(0xF5, -10300, 600, 500, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_7D01")

    label("loc_7C87")

    SetChrPos(0x101, -8000, 600, -16850, 90)
    SetChrPos(0x102, -8000, 600, -15500, 90)
    SetChrPos(0x103, -9150, 600, -17350, 90)
    SetChrPos(0x104, -9150, 600, -15000, 90)
    SetChrPos(0xF4, -10300, 600, -16850, 90)
    SetChrPos(0xF5, -10300, 600, -15500, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_7D01")

    OP_68(27000, 1500, 1000, 0)
    MoveCamera(54, 5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(28000, 0)
    OP_F0(0x0, 0x1)
    MoveCamera(60, 5, 0, 8000)
    SetCameraDistance(38000, 8000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    PlaceName2(340, 200, "c_plac00", 0x0, 0)
    OP_6F(0x79)
    Fade(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DB6")
    OP_68(-1150, 1000, 0, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(16500, 4000)
    Jump("loc_7DED")

    label("loc_7DB6")

    OP_68(-1150, 1000, -16000, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(16500, 4000)

    label("loc_7DED")


    def lambda_7DF2():
        OP_97(0x101, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7DF2)
    Sleep(50)

    def lambda_7E0F():
        OP_97(0x102, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7E0F)
    Sleep(50)

    def lambda_7E2C():
        OP_97(0x103, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7E2C)
    Sleep(50)

    def lambda_7E49():
        OP_97(0x104, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7E49)
    Sleep(50)

    def lambda_7E66():
        OP_97(0xF4, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_7E66)
    Sleep(50)

    def lambda_7E83():
        OP_97(0xF5, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_7E83)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    ChrTalk(
        0x104,
        (
            "#00306F#5PHowever, there is no home\x01",
            "What a sad thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206F…… The train of the transverse railway is also\x01",
            "I want to keep stopped forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00108FTrue…\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0xB4, 0x1F4)
    Sleep(150)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FB6")

    ChrTalk(
        0x102,
        (
            "#5P#00101F…… When I say the third home train\x01",
            "Amazing?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FF1")

    label("loc_7FB6")


    ChrTalk(
        0x102,
        (
            "#5P#00101F…… When I say the third home train\x01",
            "I wonder?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FF1")

    OP_68(-1150, 1000, -24100, 3000)
    MoveCamera(63, 27, 0, 3000)
    SetCameraDistance(25500, 3000)

    def lambda_801B():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_801B)
    Sleep(50)

    def lambda_802B():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_802B)
    Sleep(50)

    def lambda_803B():
        OP_93(0xF4, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_803B)
    Sleep(50)

    def lambda_804B():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_804B)
    Sleep(50)

    def lambda_805B():
        OP_93(0xF5, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_805B)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_811B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80DC")

    ChrTalk(
        0x10A,
        (
            "#00601FHun, that train's\x01",
            "It was the second car from the front.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8116")

    label("loc_80DC")


    ChrTalk(
        0x10A,
        (
            "#00601FHun, that train's\x01",
            "It was the second car from the front.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8116")

    Jump("loc_824E")

    label("loc_811B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_81B7")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8178")

    ChrTalk(
        0x109,
        (
            "#10101FYeah, that train's\x01",
            "It was the second car from the front.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81B2")

    label("loc_8178")


    ChrTalk(
        0x109,
        (
            "#10101FYeah, that train's\x01",
            "It was the second car from the front.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81B2")

    Jump("loc_824E")

    label("loc_81B7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_824E")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8214")

    ChrTalk(
        0x105,
        (
            "#10400FOh, that train's\x01",
            "It was the second car from the front.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_824E")

    label("loc_8214")


    ChrTalk(
        0x105,
        (
            "#10400FOh, that train's\x01",
            "It was the second car from the front.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_824E")

    OP_57(0x0)
    OP_5A()
    Fade(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8297")
    OP_68(-1150, 1000, 0, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    Jump("loc_82C5")

    label("loc_8297")

    OP_68(-1150, 1000, -16000, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)

    label("loc_82C5")

    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8317")
    OP_93(0x106, 0x5A, 0x1F4)

    ChrTalk(
        0x106,
        (
            "#6P#10701FFrom the connecting bridge over there\x01",
            "I'm going to cross.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83B2")

    label("loc_8317")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8368")
    OP_93(0x105, 0x5A, 0x1F4)

    ChrTalk(
        0x105,
        (
            "#6P#10400FFrom the connecting bridge over there\x01",
            "I think he will be able to pass.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83B2")

    label("loc_8368")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_83B2")
    OP_93(0x109, 0x5A, 0x1F4)

    ChrTalk(
        0x109,
        (
            "#6P#10101FFrom the connecting bridge over there\x01",
            "You can cross.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83B2")


    def lambda_83B7():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_83B7)
    Sleep(50)

    def lambda_83C7():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_83C7)
    Sleep(50)

    def lambda_83D7():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_83D7)
    Sleep(50)

    def lambda_83E7():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_83E7)
    Sleep(50)

    def lambda_83F7():
        OP_93(0xF4, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_83F7)
    Sleep(50)

    def lambda_8407():
        OP_93(0xF5, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_8407)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x101,
        "#5P#00001FOk, let's check it out\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8474")
    SetChrPos(0x0, -2500, 0, 0, 90)
    Jump("loc_8485")

    label("loc_8474")

    SetChrPos(0x0, -2500, 0, -16000, 90)

    label("loc_8485")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1A5, 7)
    EventEnd(0x5)
    Return()

    # Function_42_7BEE end

    def Function_43_849F(): pass

    label("Function_43_849F")

    EventBegin(0x0)
    Fade(500)
    OP_68(10000, 1200, -27200, 0)
    MoveCamera(30, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17530, 0)
    SetChrPos(0x101, 10000, 0, -28000, 0)
    SetChrPos(0x102, 9000, 0, -29500, 0)
    SetChrPos(0x103, 10200, 0, -29500, 0)
    SetChrPos(0x104, 10900, 0, -30100, 0)
    SetChrPos(0xF4, 8500, 0, -30600, 0)
    SetChrPos(0xF5, 9700, 0, -30600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#11P#00008F(3rd Home, 2nd Car … ….\x01",
            "And it is not locked. )\x02\x03",
            "#00013F(What do we do?)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Open the door and go inside\x01",      # 0
            "Leave the spot\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8612"),
        (1, "loc_86B9"),
        (SWITCH_DEFAULT, "loc_86E9"),
    )


    label("loc_8612")

    Sound(454, 0, 100, 0)
    OP_71(0x0, 0x295, 0x2B2, 0x0, 0x0)
    OP_79(0x0)
    OP_68(10190, 1200, -25980, 4000)

    def lambda_863D():
        OP_95(0xFE, 10000, 0, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_863D)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 44)
    Sleep(900)
    BeginChrThread(0x103, 3, 0, 44)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 44)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    BeginChrThread(0xF4, 3, 0, 44)
    Sleep(900)
    BeginChrThread(0xF5, 3, 0, 44)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0xF4, 0xFF)
    EndChrThread(0xF5, 0xFF)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 4)
    NewScene("e0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_86E9")

    label("loc_86B9")

    SetChrPos(0x0, 8710, 0, -29420, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Jump("loc_86E9")

    label("loc_86E9")

    Return()

    # Function_43_849F end

    def Function_44_86EA(): pass

    label("Function_44_86EA")


    def lambda_86EF():
        OP_95(0xFE, 10000, 0, -28000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_86EF)
    WaitChrThread(0xFE, 1)

    def lambda_870D():
        OP_95(0xFE, 10000, 0, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_870D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_44_86EA end

    def Function_45_8727(): pass

    label("Function_45_8727")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30200.itc", 0x1E)
    LoadChrToIndex("chr/ch24100.itc", 0x1F)
    LoadChrToIndex("chr/ch21800.itc", 0x20)
    LoadChrToIndex("apl/ch51216.itc", 0x21)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8766")
    LoadChrToIndex("apl/ch51217.itc", 0x22)
    Jump("loc_87CD")

    label("loc_8766")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8781")
    LoadChrToIndex("apl/ch51218.itc", 0x22)
    Jump("loc_87CD")

    label("loc_8781")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_879C")
    LoadChrToIndex("apl/ch51219.itc", 0x22)
    Jump("loc_87CD")

    label("loc_879C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87B7")
    LoadChrToIndex("apl/ch51220.itc", 0x22)
    Jump("loc_87CD")

    label("loc_87B7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87CD")
    LoadChrToIndex("apl/ch51221.itc", 0x22)

    label("loc_87CD")

    LoadChrToIndex("chr/ch24153.itc", 0x23)
    LoadChrToIndex("chr/ch30253.itc", 0x24)
    SoundLoad(453)
    SoundLoad(451)
    SoundLoad(825)
    OP_68(-2990, 1510, -16460, 0)
    MoveCamera(43, 38, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17100, 0)
    SetChrPos(0x101, -13640, 590, -15080, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8847")
    SetChrPos(0x102, -14410, 590, -16430, 90)
    Jump("loc_88DA")

    label("loc_8847")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_886D")
    SetChrPos(0x103, -14410, 590, -16430, 90)
    Jump("loc_88DA")

    label("loc_886D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8893")
    SetChrPos(0x104, -14410, 590, -16430, 90)
    Jump("loc_88DA")

    label("loc_8893")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_88B9")
    SetChrPos(0x109, -14410, 590, -16430, 90)
    Jump("loc_88DA")

    label("loc_88B9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_88DA")
    SetChrPos(0x105, -14410, 590, -16430, 90)

    label("loc_88DA")

    SetChrChipByIndex(0x21, 0x1E)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -12200, 590, -15670, 90)
    SetChrChipByIndex(0x22, 0x1F)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, 12210, 0, -13360, 270)
    SetChrChipByIndex(0x23, 0x20)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, 10060, 0, -13390, 90)

    def lambda_893C():
        OP_95(0xFE, -1500, 10, -16020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_893C)

    def lambda_8956():
        OP_95(0xFE, -3000, 10, -15160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8956)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_899A")

    def lambda_8980():
        OP_95(0xFE, -3600, 10, -17180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8980)
    Jump("loc_8A51")

    label("loc_899A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89C9")

    def lambda_89AF():
        OP_95(0xFE, -3600, 10, -17180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_89AF)
    Jump("loc_8A51")

    label("loc_89C9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89F8")

    def lambda_89DE():
        OP_95(0xFE, -3600, 10, -17180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_89DE)
    Jump("loc_8A51")

    label("loc_89F8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A27")

    def lambda_8A0D():
        OP_95(0xFE, -3600, 10, -17180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8A0D)
    Jump("loc_8A51")

    label("loc_8A27")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A51")

    def lambda_8A3C():
        OP_95(0xFE, -3600, 10, -17180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8A3C)

    label("loc_8A51")

    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x21, 1)
    WaitChrThread(0x101, 1)
    Sound(801, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("announcement")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Soon, the train to the Republic\x01",
            "The inspection will be terminated.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "For the time being, within the train\x01",
            "Please do not enter.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00005FTo the Republic\x01",
            "Is it about to depart soon …?\x02\x03",
            "#00003FNow……\x01",
            "Where is the fake brand name?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "When I peeked in earlier,\x01",
            "Certainly …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BD0")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00101F… ….\x02",
    )

    CloseMessageWindow()
    Jump("loc_8CFD")

    label("loc_8BD0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C15")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#00201F…… There was.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8CFD")

    label("loc_8C15")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C5C")
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#00301F…… I heard that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8CFD")

    label("loc_8C5C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8CB1")
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105F… … Maybe, is that it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8CFD")

    label("loc_8CB1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8CFD")
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x105,
        "#10305F… … Maybe, is that it?\x02",
    )

    CloseMessageWindow()

    label("loc_8CFD")

    Fade(500)
    OP_68(11100, 1200, -13380, 0)
    MoveCamera(40, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14210, 0)
    OP_0D()

    ChrTalk(
        0x23,
        (
            "── Ho ho ho,\x01",
            "Were you a peer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "So, at the crossbell\x01",
            "How was business?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x22,
        "old woman",
        "#11PHuhu, that is unfortunate … …\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x22,
        "old woman",
        (
            "#11PA bit from a business villain\x01",
            "There is something like a business disturbance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Mu …\x01",
            "It was a disaster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "That's exactly like that\x01",
            "I can not put it on the merchant's wind.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x22,
        "old woman",
        (
            "#11PNo, my lack of power\x01",
            "I think it was there.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x22,
        "old woman",
        (
            "#11PThat's why I changed my mind this time,\x01",
            "I thought about going to the empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Ha ha ha,\x01",
            "It's looking up at the business guts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Hmm, I also saw that\x01",
            "It will be the edge of something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "If you do not mind the empire\x01",
            "Let me introduce you a nice tree\x01",
            "I will get it.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x22,
        "old woman",
        "#11POh, really?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x22,
        "old woman",
        (
            "#11PHoho …\x01",
            "It is somewhat bad,\x01",
            "I wonder if I will give it up to your words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F…… I will not go that way.\x02",
    )

    CloseMessageWindow()
    OP_63(0x22, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x22,
        "old woman",
        "#11PHuh……\x02",
    )

    CloseMessageWindow()
    OP_68(7590, 1700, -13830, 3000)
    MoveCamera(45, 12, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(14960, 3000)
    SetChrPos(0x101, 1130, 0, -14460, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9086")
    SetChrPos(0x102, -1220, 0, -14540, 90)
    Jump("loc_9119")

    label("loc_9086")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90AC")
    SetChrPos(0x103, -1220, 0, -14540, 90)
    Jump("loc_9119")

    label("loc_90AC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90D2")
    SetChrPos(0x104, -1220, 0, -14540, 90)
    Jump("loc_9119")

    label("loc_90D2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90F8")
    SetChrPos(0x109, -1220, 0, -14540, 90)
    Jump("loc_9119")

    label("loc_90F8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9119")
    SetChrPos(0x105, -1220, 0, -14540, 90)

    label("loc_9119")

    SetChrPos(0x21, -140, 0, -16200, 90)

    def lambda_912F():
        OP_95(0xFE, 6590, 0, -12750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_912F)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9173")

    def lambda_9159():
        OP_95(0xFE, 5030, 0, -12420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9159)
    Jump("loc_922A")

    label("loc_9173")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91A2")

    def lambda_9188():
        OP_95(0xFE, 5030, 0, -12420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9188)
    Jump("loc_922A")

    label("loc_91A2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91D1")

    def lambda_91B7():
        OP_95(0xFE, 5030, 0, -12420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_91B7)
    Jump("loc_922A")

    label("loc_91D1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9200")

    def lambda_91E6():
        OP_95(0xFE, 5030, 0, -12420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_91E6)
    Jump("loc_922A")

    label("loc_9200")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_922A")

    def lambda_9215():
        OP_95(0xFE, 5030, 0, -12420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9215)

    label("loc_922A")


    def lambda_922F():
        OP_95(0xFE, 5280, 0, -14060, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_922F)
    Sleep(1000)

    def lambda_924C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_924C)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_927F")
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x5A, 0x0)
    Jump("loc_92FA")

    label("loc_927F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_929F")
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x5A, 0x0)
    Jump("loc_92FA")

    label("loc_929F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_92BF")
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x5A, 0x0)
    Jump("loc_92FA")

    label("loc_92BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_92DF")
    WaitChrThread(0x109, 1)
    OP_93(0x109, 0x5A, 0x0)
    Jump("loc_92FA")

    label("loc_92DF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_92FA")
    WaitChrThread(0x105, 1)
    OP_93(0x105, 0x5A, 0x0)

    label("loc_92FA")

    WaitChrThread(0x21, 1)
    OP_93(0x21, 0x5A, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00003FCrossbell Police,\x01",
            "It belongs to the Special Affairs Support Division.\x02\x03",
            "#00000FOka, it's been a long time.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x22,
        "old woman",
        "#11POh, you guys ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93DF")

    ChrTalk(
        0x102,
        (
            "#00100FWhatching\x01",
            "It seems I remembered,\x01",
            "A fake brand dealer's grandmother.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9529")

    label("loc_93DF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_942E")

    ChrTalk(
        0x103,
        (
            "#00200FDid you remember …?\x01",
            "A fake brand dealer's grandmother.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9529")

    label("loc_942E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9496")

    ChrTalk(
        0x104,
        (
            "#00300FHello, apparently\x01",
            "I wish I could remember it properly,\x01",
            "Bar fake brand dealer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9529")

    label("loc_9496")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_94E1")

    ChrTalk(
        0x109,
        (
            "#10101FThis person listens to the story\x01",
            "Is it a fake brand name ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9529")

    label("loc_94E1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9529")

    ChrTalk(
        0x105,
        (
            "#10304FIndeed, this madam\x01",
            "Rumor fake brand merchant?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9529")


    ChrTalk(
        0x21,
        (
            "Apparently we\x01",
            "If you sow it completely\x01",
            "It looks like he was thinking ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "Huhuu, I will not escape this time ~!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Hat …\x01",
            "What on earth is going on?\x01",
            "You have it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "How about a fake brand ……\x01",
            "What kind of story is that?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x22,
        "old woman",
        "#11P……Uuu……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FBased on the revision items of autonomous state law,\x01",
            "Under suspicion of illegal trade\x01",
            "I will carry you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "The siege of the station is done.\x01",
            "There is no escape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "I will not escape any more\x01",
            "Those who do not think\x01",
            "Is not it okay ~?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x22,
        "old woman",
        (
            "#11P………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x22,
        "old woman",
        (
            "#11P………………………………\x01",
            "……… Wow … … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F……!\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x22,
        (
            "#11P#5Sno kidding,\x01",
            "This damn thing is bad! It is!#3S\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x23, 0x22, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_97F1")

    ChrTalk(
        0x102,
        "#00105FCare!\x02",
    )

    CloseMessageWindow()
    Jump("loc_98A4")

    label("loc_97F1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_981F")

    ChrTalk(
        0x103,
        "#00210F… ….!\x02",
    )

    CloseMessageWindow()
    Jump("loc_98A4")

    label("loc_981F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9849")

    ChrTalk(
        0x104,
        "#00305FA whip\x02",
    )

    CloseMessageWindow()
    Jump("loc_98A4")

    label("loc_9849")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_987B")

    ChrTalk(
        0x109,
        "#10105FYeah yeah yeah! Is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_98A4")

    label("loc_987B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_98A4")

    ChrTalk(
        0x105,
        "#10305F…… Hu ♪\x02",
    )

    CloseMessageWindow()

    label("loc_98A4")


    ChrTalk(
        0x21,
        "Hit!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "Nananaa … …! Is it?\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x22,
        (
            "#11P#5SDriving into such a place,\x01",
            "I can not escape … ….#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x22,
        (
            "#11P#5SNot only once but twice,\x01",
            "Well, this stuff\x01",
            "It was a funny thing!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x22,
        (
            "#11P#5SDo not just manage clever man!\x01",
            "That's why I do not like the police!#3S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FNo, no, it's clever ……\x01",
            "I ran into the station\x01",
            "In your mistake ……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x22,
        "#11P#5SLuckily!#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#11P…… Hun, oh well.\x01",
            "Is it a siege?\x01",
            "I do not know but ….\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_96(0x22, 0x3458, 0x0, 0xFFFFCBD0, 0x3E8, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x22,
        (
            "#11P#5S#15A#NIf you can catch it\x01",
            "Try to catch ah ah ah! It is!#3S\x02",
        )
    )

    OP_93(0x22, 0x5A, 0x1F4)
    Sound(250, 0, 100, 0)
    OP_95(0x22, 25000, 0, -13360, 5000, 0x0)
    OP_57(0x0)
    OP_5A()
    SetChrFlags(0x22, 0x80)
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x21, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FNo matter how many times it is seen\x01",
            "It's amazing force …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9BFB")

    ChrTalk(
        0x102,
        (
            "#00107FLloyd!\x01",
            "In case you are distressed, …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D1B")

    label("loc_9BFB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9C42")

    ChrTalk(
        0x103,
        (
            "#00205F…… Lloyd!\x01",
            "In a case of disorder ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D1B")

    label("loc_9C42")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9C89")

    ChrTalk(
        0x104,
        (
            "#00307FHey Lloyd!\x01",
            "It is not a time of disorder!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D1B")

    label("loc_9C89")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9CD9")

    ChrTalk(
        0x109,
        (
            "#10105FHa ha\x01",
            "B, Mr. Lloyd!\x01",
            "In case you are distressed, …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D1B")

    label("loc_9CD9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D1B")

    ChrTalk(
        0x105,
        (
            "#10301F…… In a case of disorder\x01",
            "Is not it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D1B")


    ChrTalk(
        0x21,
        "That's right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FOh, let's chase!\x02\x03",
            "#00000FEntrance is everyone\x01",
            "It is consolidating … ….\x01",
            "Just catch that! It is!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 46)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9DBC")
    BeginChrThread(0x102, 1, 0, 47)
    Jump("loc_9E23")

    label("loc_9DBC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9DD7")
    BeginChrThread(0x103, 1, 0, 47)
    Jump("loc_9E23")

    label("loc_9DD7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9DF2")
    BeginChrThread(0x104, 1, 0, 47)
    Jump("loc_9E23")

    label("loc_9DF2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E0D")
    BeginChrThread(0x109, 1, 0, 47)
    Jump("loc_9E23")

    label("loc_9E0D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E23")
    BeginChrThread(0x105, 1, 0, 47)

    label("loc_9E23")

    BeginChrThread(0x21, 1, 0, 48)
    Sleep(3500)
    OP_63(0x23, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x23)

    ChrTalk(
        0x23,
        "Pocahn …\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E7E")
    EndChrThread(0x102, 0x1)
    Jump("loc_9EDD")

    label("loc_9E7E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E97")
    EndChrThread(0x103, 0x1)
    Jump("loc_9EDD")

    label("loc_9E97")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9EB0")
    EndChrThread(0x104, 0x1)
    Jump("loc_9EDD")

    label("loc_9EB0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9EC9")
    EndChrThread(0x109, 0x1)
    Jump("loc_9EDD")

    label("loc_9EC9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9EDD")
    EndChrThread(0x105, 0x1)

    label("loc_9EDD")

    EndChrThread(0x101, 0x1)
    OP_68(36050, 1500, -13190, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrPos(0x22, 54750, 0, -15970, 90)
    OP_6B(0x22)
    Sleep(100)
    BeginChrThread(0x22, 1, 0, 49)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(3000)

    ChrTalk(
        0x22,
        "Chi, that damned widow … …\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x22, 1)

    ChrTalk(
        0x22,
        (
            "If you are in the station premises,\x01",
            "I have to find another route ……\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x1F4)
    Sound(801, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("announcement")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "── We kept you waiting.\x01",
            "Train to Republic,\x01",
            "I will depart soon.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Because it is dangerous,\x01",
            "Please forgive me.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    VolumeBGM(0x64, 0x3E8)
    OP_63(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x22,
        "……This is it!\x02",
    )

    Sleep(1500)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrFlags(0x22, 0x80)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x21, 0x80)
    OP_6B(0xFF)
    OP_68(65349, 7430, -15360, 0)
    MoveCamera(63, 32, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14220, 0)
    SetChrPos(0x101, 55180, 0, -15400, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A127")
    SetChrPos(0x102, 54450, 0, -16550, 90)
    Jump("loc_A1BA")

    label("loc_A127")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A14D")
    SetChrPos(0x103, 54450, 0, -16550, 90)
    Jump("loc_A1BA")

    label("loc_A14D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A173")
    SetChrPos(0x104, 54450, 0, -16550, 90)
    Jump("loc_A1BA")

    label("loc_A173")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A199")
    SetChrPos(0x109, 54450, 0, -16550, 90)
    Jump("loc_A1BA")

    label("loc_A199")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A1BA")
    SetChrPos(0x105, 54450, 0, -16550, 90)

    label("loc_A1BA")

    SetChrPos(0x21, 53420, 0, -15670, 90)

    def lambda_A1D0():
        OP_95(0xFE, 66750, 6000, -15280, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A1D0)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A217")

    def lambda_A1FD():
        OP_95(0xFE, 66090, 6000, -16660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A1FD)
    Jump("loc_A2CE")

    label("loc_A217")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A246")

    def lambda_A22C():
        OP_95(0xFE, 66090, 6000, -16660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A22C)
    Jump("loc_A2CE")

    label("loc_A246")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A275")

    def lambda_A25B():
        OP_95(0xFE, 66090, 6000, -16660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A25B)
    Jump("loc_A2CE")

    label("loc_A275")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A2A4")

    def lambda_A28A():
        OP_95(0xFE, 66090, 6000, -16660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A28A)
    Jump("loc_A2CE")

    label("loc_A2A4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A2CE")

    def lambda_A2B9():
        OP_95(0xFE, 66090, 6000, -16660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A2B9)

    label("loc_A2CE")

    Sleep(100)

    def lambda_A2D6():
        OP_95(0xFE, 65090, 6000, -15890, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_A2D6)
    OP_0D()
    WaitChrThread(0x101, 1)

    def lambda_A2F5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A2F5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A323")
    WaitChrThread(0x102, 1)

    def lambda_A316():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A316)
    Jump("loc_A3B6")

    label("loc_A323")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A349")
    WaitChrThread(0x103, 1)

    def lambda_A33C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A33C)
    Jump("loc_A3B6")

    label("loc_A349")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A36F")
    WaitChrThread(0x104, 1)

    def lambda_A362():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A362)
    Jump("loc_A3B6")

    label("loc_A36F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A395")
    WaitChrThread(0x109, 1)

    def lambda_A388():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A388)
    Jump("loc_A3B6")

    label("loc_A395")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A3B6")
    WaitChrThread(0x105, 1)

    def lambda_A3AE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A3AE)

    label("loc_A3B6")

    WaitChrThread(0x21, 1)

    def lambda_A3BF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_A3BF)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x101,
        "#00005F#5SOh, that is …!#3S\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(34280, 1500, 9060, 0)
    MoveCamera(43, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(30010, 0)
    ClearChrFlags(0x22, 0x80)
    OP_0D()
    Sound(490, 0, 100, 0)
    Sleep(500)
    Sound(453, 0, 100, 0)
    Sound(825, 2, 50, 0)
    OP_82(0x96, 0x96, 0xBB8, 0x1F4)
    BeginChrThread(0x8, 1, 0, 53)
    OP_68(69980, 1500, 7190, 5000)
    MoveCamera(43, 28, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(30010, 5000)
    SetChrPos(0x22, 66310, 6000, -6920, 0)
    SetChrFlags(0x22, 0x40)
    Sleep(2200)
    OP_95(0x22, 66280, 6000, 140, 4000, 0x0)
    Sound(844, 0, 80, 0)
    OP_9D(0x22, 0x10306, 0x1770, 0x1E96, 0x5DC, 0xBB8)
    Sound(326, 0, 70, 0)
    SetChrChipByIndex(0x22, 0x23)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x22, 0x20)

    def lambda_A53B():
        OP_96(0xFE, 0x33450, 0xFFFFF9F2, 0x1FA4, 0x251C, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_A53B)
    Sleep(2000)

    ChrTalk(
        0x21,
        "#5S#6AEeeeeeey yeah yeah! It is!#3S\x02",
    )

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    Sound(451, 2, 50, 0)
    Fade(500)
    OP_68(65349, 7430, -15360, 0)
    MoveCamera(63, 32, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14220, 0)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x22, 0x1)
    SetChrFlags(0x22, 0x80)
    OP_0D()

    ChrTalk(
        0x101,
        "#00011FWell, no way …!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A61B")

    ChrTalk(
        0x102,
        "#00105FIt is a lie, is not it! Is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A6EE")

    label("loc_A61B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A64D")

    ChrTalk(
        0x103,
        "#00205FWell … that!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A6EE")

    label("loc_A64D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A685")

    ChrTalk(
        0x104,
        "#00305FHey hey, are you serious! Is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A6EE")

    label("loc_A685")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A6BD")

    ChrTalk(
        0x109,
        "#10101FCut … what means!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A6EE")

    label("loc_A6BD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A6EE")

    ChrTalk(
        0x105,
        "#10305F… … It's quite easy.\x02",
    )

    CloseMessageWindow()

    label("loc_A6EE")


    ChrTalk(
        0x21,
        "Well, at the last end ……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "Oh, to the Donovan police\x01",
            "What shall I say …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F……………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A7C5")

    ChrTalk(
        0x101,
        "#00001FLet's go … Eli!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F……!\x01",
            "Well, well, I understood!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A92A")

    label("loc_A7C5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A819")

    ChrTalk(
        0x101,
        "#00001FLet's go, Tio!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F……!\x01",
            "I understand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A92A")

    label("loc_A819")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A875")

    ChrTalk(
        0x101,
        "#00001FLet's go … Randy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F……!\x01",
            "Officer, leave it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A92A")

    label("loc_A875")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A8CD")

    ChrTalk(
        0x101,
        "#00001FLet's go, Noel!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10107F……!\x01",
            "Yes, sir!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A92A")

    label("loc_A8CD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A92A")

    ChrTalk(
        0x101,
        "#00001FLet's go, Wadi!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FGiggle\x01",
            "You have not lost.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A92A")

    OP_93(0x21, 0x5A, 0x1F4)
    OP_63(0x21, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x21,
        "… … … Did you mean ……\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x21,
        "#5S… …. Eh! Is it?#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "U, is that a lie …?\x01",
            "Are you going to follow me? Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007FTo catch her\x01",
            "There is no choice but to follow!\x02\x03",
            "#00003Fno time……\x01",
            "Pardon me, I have to go now!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    def lambda_AA36():
        OP_95(0xFE, 66750, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AA36)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA7D")

    def lambda_AA63():
        OP_95(0xFE, 66090, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AA63)
    Jump("loc_AB34")

    label("loc_AA7D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AAAC")

    def lambda_AA92():
        OP_95(0xFE, 66090, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AA92)
    Jump("loc_AB34")

    label("loc_AAAC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AADB")

    def lambda_AAC1():
        OP_95(0xFE, 66090, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AAC1)
    Jump("loc_AB34")

    label("loc_AADB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB0A")

    def lambda_AAF0():
        OP_95(0xFE, 66090, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AAF0)
    Jump("loc_AB34")

    label("loc_AB0A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB34")

    def lambda_AB1F():
        OP_95(0xFE, 66090, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AB1F)

    label("loc_AB34")

    OP_63(0x21, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(2000)
    OP_64(0x21)

    ChrTalk(
        0x21,
        (
            "How shall I do …?\x01",
            "We can leave it to the support section … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x21)

    ChrTalk(
        0x21,
        "#5S… … … Wow Aaaa!#3S\x02",
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0x21, 65890, 6000, -15300, 4000, 0x0)

    def lambda_ABEC():
        OP_95(0xFE, 66750, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_ABEC)
    Sleep(1000)
    Fade(500)
    EndChrThread(0x101, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC26")
    EndChrThread(0x102, 0x1)
    Jump("loc_AC85")

    label("loc_AC26")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC3F")
    EndChrThread(0x103, 0x1)
    Jump("loc_AC85")

    label("loc_AC3F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC58")
    EndChrThread(0x104, 0x1)
    Jump("loc_AC85")

    label("loc_AC58")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC71")
    EndChrThread(0x109, 0x1)
    Jump("loc_AC85")

    label("loc_AC71")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC85")
    EndChrThread(0x105, 0x1)

    label("loc_AC85")

    EndChrThread(0x21, 0x1)
    OP_68(69980, 1500, 7190, 0)
    MoveCamera(43, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(30010, 0)
    SetChrPos(0x101, 66310, 6000, -9500, 0)
    SetChrFlags(0x101, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ACF8")
    SetChrPos(0x102, 66090, 6000, -10500, 0)
    SetChrFlags(0x102, 0x40)
    Jump("loc_AD9F")

    label("loc_ACF8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD23")
    SetChrPos(0x103, 66090, 6000, -10500, 0)
    SetChrFlags(0x103, 0x40)
    Jump("loc_AD9F")

    label("loc_AD23")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD4E")
    SetChrPos(0x104, 66090, 6000, -10500, 0)
    SetChrFlags(0x104, 0x40)
    Jump("loc_AD9F")

    label("loc_AD4E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD79")
    SetChrPos(0x109, 66090, 6000, -10500, 0)
    SetChrFlags(0x109, 0x40)
    Jump("loc_AD9F")

    label("loc_AD79")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD9F")
    SetChrPos(0x105, 66090, 6000, -10500, 0)
    SetChrFlags(0x105, 0x40)

    label("loc_AD9F")

    SetChrPos(0x21, 66310, 6000, -11500, 0)
    SetChrFlags(0x21, 0x40)
    Sound(456, 0, 100, 0)
    StopSound(835, 1000, 100)
    BeginChrThread(0x8, 1, 0, 54)
    OP_0D()
    BeginChrThread(0x101, 1, 0, 50)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ADEC")
    BeginChrThread(0x102, 1, 0, 51)
    Jump("loc_AE53")

    label("loc_ADEC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE07")
    BeginChrThread(0x103, 1, 0, 51)
    Jump("loc_AE53")

    label("loc_AE07")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE22")
    BeginChrThread(0x104, 1, 0, 51)
    Jump("loc_AE53")

    label("loc_AE22")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE3D")
    BeginChrThread(0x109, 1, 0, 51)
    Jump("loc_AE53")

    label("loc_AE3D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE53")
    BeginChrThread(0x105, 1, 0, 51)

    label("loc_AE53")

    Sleep(500)
    BeginChrThread(0x21, 1, 0, 52)
    Sleep(2000)
    Sleep(4000)
    StopSound(451, 1000, 50)
    StopSound(825, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AEAC")
    ClearChrFlags(0x102, 0x40)
    ClearChrFlags(0x102, 0x20)
    ClearChrFlags(0x102, 0x1000)
    Jump("loc_AF37")

    label("loc_AEAC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AED0")
    ClearChrFlags(0x103, 0x40)
    ClearChrFlags(0x103, 0x20)
    ClearChrFlags(0x103, 0x1000)
    Jump("loc_AF37")

    label("loc_AED0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AEF4")
    ClearChrFlags(0x104, 0x40)
    ClearChrFlags(0x104, 0x20)
    ClearChrFlags(0x104, 0x1000)
    Jump("loc_AF37")

    label("loc_AEF4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF18")
    ClearChrFlags(0x109, 0x40)
    ClearChrFlags(0x109, 0x20)
    ClearChrFlags(0x109, 0x1000)
    Jump("loc_AF37")

    label("loc_AF18")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF37")
    ClearChrFlags(0x105, 0x40)
    ClearChrFlags(0x105, 0x20)
    ClearChrFlags(0x105, 0x1000)

    label("loc_AF37")

    StopBGM(0xBB8)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("e4800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_45_8727 end

    def Function_46_AF4A(): pass

    label("Function_46_AF4A")

    OP_95(0xFE, 8430, 0, -12130, 4000, 0x0)
    OP_95(0xFE, 25430, 0, -12130, 4000, 0x0)
    Return()

    # Function_46_AF4A end

    def Function_47_AF73(): pass

    label("Function_47_AF73")

    Sleep(200)
    OP_95(0xFE, 8430, 0, -12130, 4000, 0x0)
    OP_95(0xFE, 25430, 0, -12130, 4000, 0x0)
    Return()

    # Function_47_AF73 end

    def Function_48_AF9F(): pass

    label("Function_48_AF9F")

    Sleep(800)
    OP_95(0xFE, 8430, 0, -12130, 4000, 0x0)
    OP_95(0xFE, 25430, 0, -12130, 4000, 0x0)
    Return()

    # Function_48_AF9F end

    def Function_49_AFCB(): pass

    label("Function_49_AFCB")

    OP_95(0xFE, 66190, 6000, -15970, 4000, 0x0)
    OP_95(0xFE, 66190, 6000, -5060, 4000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_49_AFCB end

    def Function_50_AFFB(): pass

    label("Function_50_AFFB")

    OP_95(0xFE, 66280, 6000, 140, 4000, 0x0)
    Sound(844, 0, 80, 0)
    OP_9D(0xFE, 0x102E8, 0x1770, 0x1E96, 0x5DC, 0xBB8)
    Sound(326, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    OP_96(0xFE, 0x33450, 0xFFFFF9F2, 0x1FA4, 0x251C, 0x0)
    Return()

    # Function_50_AFFB end

    def Function_51_B059(): pass

    label("Function_51_B059")

    OP_95(0xFE, 66090, 6000, 140, 4000, 0x0)
    Sound(844, 0, 80, 0)
    OP_9D(0xFE, 0x1022A, 0x1770, 0x1E96, 0x5DC, 0xBB8)
    Sound(326, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    OP_96(0xFE, 0x33450, 0xFFFFF9F2, 0x1FA4, 0x251C, 0x0)
    Return()

    # Function_51_B059 end

    def Function_52_B0B7(): pass

    label("Function_52_B0B7")

    OP_95(0xFE, 66280, 6000, 140, 4000, 0x0)
    Sound(844, 0, 80, 0)
    OP_9D(0xFE, 0x102E8, 0x1770, 0x1E96, 0x5DC, 0xBB8)
    Sound(326, 0, 70, 0)
    OP_64(0xFE)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    OP_96(0xFE, 0x33450, 0xFFFFF9F2, 0x1FA4, 0x251C, 0x0)
    Return()

    # Function_52_B0B7 end

    def Function_53_B113(): pass

    label("Function_53_B113")


    def lambda_B118():
        OP_95(0xFE, 210000, -1550, 8100, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B118)
    Sleep(500)

    def lambda_B135():
        OP_95(0xFE, 210000, -1550, 8100, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B135)
    Sleep(700)

    def lambda_B152():
        OP_95(0xFE, 210000, -1550, 8100, 8500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B152)
    Sleep(800)

    def lambda_B16F():
        OP_95(0xFE, 210000, -1550, 8100, 9500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B16F)
    Return()

    # Function_53_B113 end

    def Function_54_B185(): pass

    label("Function_54_B185")

    SetChrPos(0x8, 70000, -1550, 8100, 0)

    def lambda_B19B():
        OP_95(0xFE, 210000, -1550, 8100, 9500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B19B)
    Return()

    # Function_54_B185 end

    def Function_55_B1B1(): pass

    label("Function_55_B1B1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x1, 0x8)
    OP_49()
    SetChrPos(0x8, 7000, -1550, -8100, 0)
    OP_D5(0x8, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_68(65000, 10000, -11000, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(30000, 0)
    OP_F0(0x0, 0x1)
    OP_71(0x1, 0x3D, 0x3D, 0x0, 0x0)
    SoundLoad(452)
    OP_68(25000, 1500, -11000, 15000)
    MoveCamera(47, 17, 0, 15000)
    SetCameraDistance(50000, 15000)
    Sound(801, 0, 100, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)
    Sound(452, 0, 100, 0)
    BeginChrThread(0x25, 1, 0, 56)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x3D, 0x168, 0x0, 0x0)
    OP_6F(0x79)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x17B, 5)
    SetScenarioFlags(0x22, 1)
    NewScene("c0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_55_B1B1 end

    def Function_56_B2AF(): pass

    label("Function_56_B2AF")

    Sleep(11000)
    Sound(143, 0, 50, 0)
    Return()

    # Function_56_B2AF end

    SaveToFile()

Try(main)

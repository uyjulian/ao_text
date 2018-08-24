from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "列車",                   # 1
        "列車",                   # 2
        "KeA",                    # 3
        "Fran",                   # 4
        "Chief Sergei",           # 5
        "Chancellor Osborne",     # 6
        "Lechter",                # 7
        "Prince Olivert",         # 8
        "Major Mueller",          # 9
        "Passenger",              # 10
        "Passenger",              # 11
        "Passenger",              # 12
        "Passenger",              # 13
        "Passenger",              # 14
        "Passenger",              # 15
        "Passenger",              # 16
        "Passenger",              # 17
        "Station Attendant",      # 18
        "Imperial Army Officer",  # 19
        "Imperial Army Officer",  # 20
        "Imperial Army Officer",  # 21
        "Imperial Army Officer",  # 22
        "Imperial Army Officer",  # 23
        "Imperial Army Officer",  # 24
        "Inspector Marlowe",      # 25
        "Detective Raymond",      # 26
        "Fake Brand Trader",      # 27
        "Imperial Trader",        # 28
        "列車",                   # 29
        "SE制御",                 # 30
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
        "Function_3_3213",         # 03, 3
        "Function_4_3257",         # 04, 4
        "Function_5_32AD",         # 05, 5
        "Function_6_3303",         # 06, 6
        "Function_7_335E",         # 07, 7
        "Function_8_33B1",         # 08, 8
        "Function_9_33FD",         # 09, 9
        "Function_10_3451",        # 0A, 10
        "Function_11_3481",        # 0B, 11
        "Function_12_3BEC",        # 0C, 12
        "Function_13_3C38",        # 0D, 13
        "Function_14_3C74",        # 0E, 14
        "Function_15_3C8B",        # 0F, 15
        "Function_16_3CC7",        # 10, 16
        "Function_17_3CDE",        # 11, 17
        "Function_18_3D1A",        # 12, 18
        "Function_19_3D31",        # 13, 19
        "Function_20_3D7E",        # 14, 20
        "Function_21_3D8E",        # 15, 21
        "Function_22_3DCA",        # 16, 22
        "Function_23_3DDA",        # 17, 23
        "Function_24_3DF1",        # 18, 24
        "Function_25_3E2D",        # 19, 25
        "Function_26_3E44",        # 1A, 26
        "Function_27_3E80",        # 1B, 27
        "Function_28_3E97",        # 1C, 28
        "Function_29_3ED3",        # 1D, 29
        "Function_30_3EEA",        # 1E, 30
        "Function_31_3F37",        # 1F, 31
        "Function_32_3F47",        # 20, 32
        "Function_33_3F83",        # 21, 33
        "Function_34_3F93",        # 22, 34
        "Function_35_3FAF",        # 23, 35
        "Function_36_3FC6",        # 24, 36
        "Function_37_400D",        # 25, 37
        "Function_38_4054",        # 26, 38
        "Function_39_6922",        # 27, 39
        "Function_40_6953",        # 28, 40
        "Function_41_6E9E",        # 29, 41
        "Function_42_8116",        # 2A, 42
        "Function_43_8A07",        # 2B, 43
        "Function_44_8C4E",        # 2C, 44
        "Function_45_8C8B",        # 2D, 45
        "Function_46_B605",        # 2E, 46
        "Function_47_B62E",        # 2F, 47
        "Function_48_B65A",        # 30, 48
        "Function_49_B686",        # 31, 49
        "Function_50_B6B6",        # 32, 50
        "Function_51_B714",        # 33, 51
        "Function_52_B772",        # 34, 52
        "Function_53_B7CE",        # 35, 53
        "Function_54_B840",        # 36, 54
        "Function_55_B86C",        # 37, 55
        "Function_56_B96A",        # 38, 56
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
        "Young Girl's Voice",
        "#4S#3595V#12A#30WLlooooooyd!\x02",
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
        "#11P#00005F#3315V#30WAh...\x02",
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
            "#12P#00002F#3316V#30WKeA! So you're here to\x01",
            "pick me up.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xCF4)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)

    def lambda_1071():
        OP_96(0xFE, 0xB54, 0x0, 0xFFFFC3D8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1071)
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
            "#3596V#30WYeah! Because I heard you'd be\x01",
            "coming home today!\x02\x03",
            "#3597VAre you okay!? Aren't you hurt\x01",
            "anywhere!?\x02",
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
            "#12P#00004FNo, I'm fine.\x02\x03",
            "#00002FI'm back, KeA.\x02",
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
            "#01121F#5PEhehe... Welcome back\x01",
            "too, Noｱl!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10109FAhaha... I'm back, KeA.\x02",
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
        "Girl's Voice",
        "#2708V#12A#30WSiiiiiiiiis!!\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    ClearChrFlags(0xB, 0x8)

    def lambda_12D0():
        OP_95(0xFE, 4350, 0, -16650, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_12D0)
    Sleep(300)

    def lambda_12ED():

        label("loc_12ED")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_12ED")

    QueueWorkItem2(0xA, 2, lambda_12ED)

    def lambda_12FF():

        label("loc_12FF")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_12FF")

    QueueWorkItem2(0x101, 2, lambda_12FF)
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

    def lambda_134B():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_134B)
    Sound(811, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x109,
        "#12P#10111F#3513V#30WF-Fran!?\x02",
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
            "#2709V#30WUeeeeh...! I'm glad you're all in\x01",
            "one piece, Noｱl!\x02\x03",
            "#2710VWelcome back! You aren't hurt,\x01",
            "right!?\x02",
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
            "#12P#10102FNo, as you can see I'm\x01",
            "fine.\x02\x03",
            "#10106FAnd by the way, only a\x01",
            "few days have passed.\x01",
            "Isn't that a bit much?\x02",
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

    def lambda_152A():
        OP_96(0xFE, 0xFA0, 0x0, 0xFFFFBEC4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_152A)
    WaitChrThread(0xB, 1)
    Sleep(150)

    ChrTalk(
        0xB,
        (
            "#01903F#5PYou don't get it, Noｱl!\x01",
            "It's not a matter of\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)
    Sleep(150)

    ChrTalk(
        0xB,
        "#6P#01909FRight, KeA?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5P#01101FYeah, yeah, exactly!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00012FHaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10112FThe fact that we're back\x01",
            "has sunk in somehow...\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_16F0")

    NpcTalk(
        0x102,
        "Girl's Voice",
        (
            "#3385VLloyd#30W...... Welcome\x01",
            "back.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xD39)
    OP_C9(0x1, 0x80000000)
    Jump("loc_1738")

    label("loc_16F0")


    NpcTalk(
        0x102,
        "Girl's Voice",
        (
            "#3386V#30W*giggle*...... Good\x01",
            "work, you two.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xD3A)
    OP_C9(0x1, 0x80000000)

    label("loc_1738")

    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_176D():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_176D)
    Sleep(50)

    def lambda_177D():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_177D)
    Sleep(50)

    def lambda_178D():
        OP_93(0xA, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_178D)
    Sleep(50)

    def lambda_179D():
        OP_93(0xB, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_179D)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)

    ChrTalk(
        0x101,
        "#12P#00002FAh...\x02",
    )

    CloseMessageWindow()
    OP_68(-6900, 1400, -16000, 3000)
    MoveCamera(321, 21, 0, 3000)
    SetCameraDistance(14500, 3000)
    Sleep(1300)

    def lambda_17FB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_17FB)

    def lambda_180C():
        OP_96(0xFE, 0xFFFFE124, 0x258, 0xFFFFC374, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_180C)
    Sleep(100)

    def lambda_1829():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1829)

    def lambda_183A():
        OP_96(0xFE, 0xFFFFDE68, 0x258, 0xFFFFBF8C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_183A)
    WaitChrThread(0x102, 1)
    WaitChrThread(0xC, 1)
    OP_6F(0x79)
    Sleep(300)

    def lambda_1861():
        OP_96(0xFE, 0x6A4, 0x0, 0xFFFFC374, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1861)
    Sleep(100)

    def lambda_187E():
        OP_96(0xFE, 0x3E8, 0x0, 0xFFFFBF8C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_187E)
    Sleep(2500)
    Fade(500)
    OP_68(2600, 900, -15600, 0)
    MoveCamera(325, 23, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetCameraDistance(14000, 1500)

    def lambda_18D7():
        OP_96(0xFE, 0x1004, 0x0, 0xFFFFC5CC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_18D7)
    Sleep(50)

    def lambda_18F4():
        OP_96(0xFE, 0x1130, 0x0, 0xFFFFBBA4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_18F4)
    WaitChrThread(0xA, 1)

    def lambda_1912():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1912)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x101,
        (
            "#12P#00002FElie! You're back\x01",
            "already!?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_1ED0")
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
            "#3387V#30WY-Yes, I just got back yesterday.\x02\x03",
            "#3389VI also finished helping\x01",
            "grandfather, so I can resume my\x01",
            "duties today as well.\x02",
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
        "#12P#00002F#30WI see............\x02",
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
            "#01105F#11PHey, hey.\x02\x03",
            "Lloyd, Elie, why are you\x01",
            "staring at each other?\x02",
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

    def lambda_1B50():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1B50)

    def lambda_1B5D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1B5D)
    TurnDirection(0x101, 0xA, 700)

    ChrTalk(
        0x101,
        "#6P#00011FN-No! It's nothing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#5PT-That's right. I missed\x01",
            "him because we haven't seen\x01",
            "each other for a while!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01100F#11PHm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#01902F(Hmm... Looks like\x01",
            "they're in love.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10114F(I thought they had that\x01",
            "kind of relationship.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#01900F(From what I can see,\x01",
            "their relationship\x01",
            "doesn't seem final.)\x02\x03",
            "#01909F(Ehehe. If you're worried\x01",
            "about it, maybe you still\x01",
            "have a chance?)\x02",
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
        "#11P#10111F(I-I'm not interested!)\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00109F#5POh, Noｱl, you did good work\x01",
            "as well.\x02\x03",
            "#00102FDid anything dangerous\x01",
            "happen? Occasionally, Lloyd\x01",
            "does some reckless things...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)
    Sleep(150)

    ChrTalk(
        0x109,
        (
            "#12P#10112FN-No, no. And good work\x01",
            "yourself, Elie.\x02\x03",
            "#10100FIf I remember correctly, you\x01",
            "were on an international tour\x01",
            "with Chairman MacDowell, right?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1EB3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1EB3)
    Sleep(50)

    def lambda_1EC3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1EC3)
    Jump("loc_2074")

    label("loc_1ED0")

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
            "#3388V#30WYes, I just got back yesterday.\x02\x03",
            "#3389VI also finished helping\x01",
            "grandfather, so I can resume my\x01",
            "duties today as well.\x02",
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
        "#12P#00002FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10109FGood work, Elie.\x02\x03",
            "#10100FIf I remember correctly, you\x01",
            "were on an international tour\x01",
            "with Chairman MacDowell, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2074")


    ChrTalk(
        0x102,
        (
            "#00104F#5PYes, although I wasn't\x01",
            "much help.\x02\x03",
            "#00100FBut, I learned many\x01",
            "interesting things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FI see... Let me hear\x01",
            "about them later.\x02\x03",
            "#00006FBut it would be even\x01",
            "better if Tio and Randy\x01",
            "were back as well...\x02",
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
            "Well, they'll probably be back\x01",
            "before the month is out.\x02\x03",
            "More importantly, Lloyd. Did you\x01",
            "settle things properly?\x02",
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
            "#12P#00003F...Yes. We arrested both\x01",
            "of them.\x02\x03",
            "#00001FDudley and Arios are\x01",
            "escorting them to\x01",
            "prison.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01003F#5PI see...\x02\x03",
            "#01002FWell with this, the cult\x01",
            "incident case is closed.\x02\x03",
            "I think you already know,\x01",
            "but... I'll have you take\x01",
            "it easy for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes sir, I plan to.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01002F#5PAs for Noｱl, it's nice\x01",
            "to officially meet you.\x02\x03",
            "You can start today,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_23CA():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_23CA)
    Sleep(100)

    def lambda_23DA():
        TurnDirection(0xB, 0x109, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_23DA)
    Sleep(100)

    def lambda_23EA():
        TurnDirection(0xA, 0x109, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_23EA)
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
            "#12P#10103FNoｱl Seeker, reporting\x01",
            "for duty!\x02\x03",
            "#10101FMy temporary transfer to\x01",
            "the Special Support\x01",
            "Section starts today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11P#01105FWhoa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#01909FEhehe... Now Noｱl is\x01",
            "your colleague too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01006F#5PAh, you don't have to be\x01",
            "so formal.\x02\x03",
            "#01000FYou've probably heard\x01",
            "from Sonya, but we do\x01",
            "things our own way here.\x02\x03",
            "For now, you'll do away\x01",
            "with the army-style\x01",
            "hierarchy.\x02",
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
        "#12P#10105FI-I'll try.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x105, -9000, 600, -16000, 90)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x105,
        "Young Man's Voice",
        (
            "#2904V#30WHehe... It looks like\x01",
            "you're all here.\x02",
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

    def lambda_2694():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2694)
    Sleep(50)

    def lambda_26A4():
        TurnDirection(0xA, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_26A4)
    Sleep(50)

    def lambda_26B4():
        TurnDirection(0xB, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_26B4)
    Sleep(50)

    def lambda_26C4():
        TurnDirection(0xC, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_26C4)
    Sleep(50)

    def lambda_26D4():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_26D4)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x102, 0)

    def lambda_26F8():

        label("loc_26F8")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_26F8")

    QueueWorkItem2(0x102, 2, lambda_26F8)

    def lambda_270A():

        label("loc_270A")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_270A")

    QueueWorkItem2(0xC, 2, lambda_270A)

    def lambda_271C():

        label("loc_271C")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_271C")

    QueueWorkItem2(0xB, 2, lambda_271C)
    Sleep(500)

    def lambda_2731():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2731)

    def lambda_2742():
        OP_95(0xFE, -3000, 0, -16000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2742)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        "#10100FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWazy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01110FOh, it's Wazy!\x02",
    )

    CloseMessageWindow()

    def lambda_27A1():
        OP_95(0xFE, 1700, 0, -15500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_27A1)
    Sleep(800)
    Fade(500)
    OP_68(2600, 900, -15600, 0)
    MoveCamera(325, 23, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    Sleep(500)

    def lambda_27F4():
        OP_96(0xFE, 0x802, 0x0, 0xFFFFC856, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_27F4)
    WaitChrThread(0x105, 1)

    def lambda_2812():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2812)
    WaitChrThread(0x102, 1)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x105,
        (
            "#10304F#2905V#5P#30WHehe, good work.\x02\x03",
            "#10300F#2906VBy the looks of things,\x01",
            "it went well, I guess?\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xB5A)

    ChrTalk(
        0x101,
        (
            "#12P#00000FYeah. Because of your intel, we\x01",
            "managed to get in contact with\x01",
            "an informant in Altair City...\x02\x03",
            "#00006F...Where in the world did you\x01",
            "get it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#5PHeh... It takes a thief\x01",
            "to catch a thief, they\x01",
            "say.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(3150, 900, -15230, 1500)

    def lambda_298C():
        OP_95(0xFE, 3150, 0, -15400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_298C)
    WaitChrThread(0x105, 1)
    EndChrThread(0x102, 0x2)
    EndChrThread(0xC, 0x2)

    def lambda_29B2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_29B2)
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
            "#2901V#30W...I did it just for you, of\x01",
            "course. I'm glad you found it\x01",
            "useful.\x02",
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
        "#5P#00105F!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#6P#01905FWuawah...!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#12P#00011FHey, you're too close!\x02\x03",
            "Why are you standing so\x01",
            "close to me!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10309FAhaha, what a silly\x01",
            "question.\x02\x03",
            "It's because your\x01",
            "reaction was funny, what\x01",
            "else?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00013FH-Hey...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00111FNow look here, Wazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10112FAhaha... (Mysterious,\x01",
            "just like I thought.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01109F#11PEhehe. Looks fun!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#01906FWhat a nice place the\x01",
            "Special Support Section\x01",
            "must be...\x02\x03",
            "There's Noｱl, and KeA, and\x01",
            "you get to see Lloyd\x01",
            "looking all flustered too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 500)

    ChrTalk(
        0x101,
        (
            "#00012F#11PNo! That's not something\x01",
            "you should be jealous\x01",
            "of!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01006F#5PSeriously... Let's stop\x01",
            "joking around.\x02",
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

    def lambda_2DEB():
        TurnDirection(0x101, 0xC, 0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2DEB)
    Sleep(0)

    def lambda_2DFB():
        TurnDirection(0x109, 0xC, 0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2DFB)
    Sleep(0)

    def lambda_2E0B():
        TurnDirection(0x102, 0xC, 0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2E0B)
    Sleep(0)

    def lambda_2E1B():
        TurnDirection(0xB, 0xC, 0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_2E1B)
    Sleep(0)

    def lambda_2E2B():
        TurnDirection(0xA, 0xC, 0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_2E2B)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xA, 0)

    def lambda_2E4F():
        OP_96(0xFE, 0x9C4, 0x0, 0xFFFFC504, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2E4F)
    WaitChrThread(0x105, 1)
    TurnDirection(0x105, 0xC, 500)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#6P#01003F...Anyhow. These are the\x01",
            "starting members of the new\x01",
            "Special Support Section.\x02\x03",
            "#01000FLloyd Bannings, as leader.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00000F#3317V#30W...Sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#01000FElie MacDowell, as\x01",
            "second in command.\x02",
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
            "#6P#01003FNoｱl Seeker, CGF\x01",
            "transferee.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10102F#3514V#11P#30WYes, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#01000FAnd Wazy Hemisphere,\x01",
            "temporary associate\x01",
            "member.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        "#10304F#2907V#5P#30WJa.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#01004FAs of today at 18:30, I\x01",
            "declare the Special Support\x01",
            "Section officially reinstated.\x02\x03",
            "#01002FEven more fun jobs than before\x01",
            "are going to come in. Look\x01",
            "forward to them...\x02",
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

    def Function_3_3213(): pass

    label("Function_3_3213")

    Sound(452, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x3D, 0x168, 0x0, 0x0)
    Sleep(2000)

    def lambda_3231():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3231)
    OP_79(0x1)
    Sound(143, 0, 100, 0)
    OP_82(0x96, 0x96, 0xBB8, 0x1F4)
    Sleep(500)
    Return()

    # Function_3_3213 end

    def Function_4_3257(): pass

    label("Function_4_3257")

    SetChrPos(0xFE, 22700, 0, -9700, 180)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3278():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3278)
    OP_95(0xFE, 22700, 0, -12800, 2000, 0x0)
    OP_95(0xFE, 7300, 0, -12800, 2000, 0x0)
    Return()

    # Function_4_3257 end

    def Function_5_32AD(): pass

    label("Function_5_32AD")

    SetChrPos(0xFE, 22700, 0, -9700, 180)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_32CE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_32CE)
    OP_95(0xFE, 22700, 0, -12800, 2000, 0x0)
    OP_95(0xFE, 8500, 0, -12800, 2000, 0x0)
    Return()

    # Function_5_32AD end

    def Function_6_3303(): pass

    label("Function_6_3303")

    SetChrPos(0xFE, 19700, 100, -9700, 180)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3324():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3324)
    OP_95(0xFE, 19700, 0, -12800, 2000, 0x0)
    OP_95(0xFE, 0, 0, -12800, 2000, 0x0)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_6_3303 end

    def Function_7_335E(): pass

    label("Function_7_335E")

    ClearScenarioFlags(0x0, 0)

    def lambda_3366():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3366)
    OP_95(0xFE, 22700, 0, -13700, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_AD(0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, 0, 0, -13700, 2000, 0x0)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_7_335E end

    def Function_8_33B1(): pass

    label("Function_8_33B1")


    def lambda_33B6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_33B6)
    OP_95(0xFE, 22700, 0, -12700, 2000, 0x0)
    Sleep(500)
    SetScenarioFlags(0x0, 0)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, 0, 0, -12700, 2000, 0x0)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_8_33B1 end

    def Function_9_33FD(): pass

    label("Function_9_33FD")


    def lambda_3402():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3402)
    OP_95(0xFE, 32500, 0, -12700, 4000, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0xFE, 0, 0, -12700, 4000, 0x0)
    OP_64(0xFE)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_9_33FD end

    def Function_10_3451(): pass

    label("Function_10_3451")

    OP_95(0xFE, 7500, 0, -13700, 2000, 0x0)
    OP_95(0xFE, 4800, 0, -16700, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_10_3451 end

    def Function_11_3481(): pass

    label("Function_11_3481")

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

    # Function_11_3481 end

    def Function_12_3BEC(): pass

    label("Function_12_3BEC")

    Sound(963, 0, 100, 0)
    Sound(825, 2, 50, 0)
    OP_71(0x3, 0x5A, 0x168, 0x0, 0x8)
    Sleep(2000)

    def lambda_3C0C():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3C0C)
    OP_79(0x3)
    OP_82(0x96, 0x96, 0xBB8, 0x1F4)
    Sound(143, 0, 100, 0)
    StopSound(825, 500, 50)
    Sleep(500)
    Return()

    # Function_12_3BEC end

    def Function_13_3C38(): pass

    label("Function_13_3C38")


    def lambda_3C3D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3C3D)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 40000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_13_3C38 end

    def Function_14_3C74(): pass

    label("Function_14_3C74")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_14_3C74 end

    def Function_15_3C8B(): pass

    label("Function_15_3C8B")


    def lambda_3C90():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3C90)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 39000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_15_3C8B end

    def Function_16_3CC7(): pass

    label("Function_16_3CC7")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_16_3CC7 end

    def Function_17_3CDE(): pass

    label("Function_17_3CDE")


    def lambda_3CE3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3CE3)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 38000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_17_3CDE end

    def Function_18_3D1A(): pass

    label("Function_18_3D1A")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_18_3D1A end

    def Function_19_3D31(): pass

    label("Function_19_3D31")


    def lambda_3D36():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3D36)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_68(35000, 700, 3300, 2000)
    OP_95(0xFE, 35000, 0, 3300, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_19_3D31 end

    def Function_20_3D7E(): pass

    label("Function_20_3D7E")

    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_20_3D7E end

    def Function_21_3D8E(): pass

    label("Function_21_3D8E")


    def lambda_3D93():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3D93)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 35750, 0, 2500, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_21_3D8E end

    def Function_22_3DCA(): pass

    label("Function_22_3DCA")

    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_22_3DCA end

    def Function_23_3DDA(): pass

    label("Function_23_3DDA")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_23_3DDA end

    def Function_24_3DF1(): pass

    label("Function_24_3DF1")


    def lambda_3DF6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3DF6)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 27000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_24_3DF1 end

    def Function_25_3E2D(): pass

    label("Function_25_3E2D")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_25_3E2D end

    def Function_26_3E44(): pass

    label("Function_26_3E44")


    def lambda_3E49():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3E49)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 26000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_26_3E44 end

    def Function_27_3E80(): pass

    label("Function_27_3E80")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_27_3E80 end

    def Function_28_3E97(): pass

    label("Function_28_3E97")


    def lambda_3E9C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3E9C)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 25000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_28_3E97 end

    def Function_29_3ED3(): pass

    label("Function_29_3ED3")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_29_3ED3 end

    def Function_30_3EEA(): pass

    label("Function_30_3EEA")


    def lambda_3EEF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3EEF)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_68(22000, 700, 3300, 2000)
    OP_95(0xFE, 22000, 0, 3300, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_30_3EEA end

    def Function_31_3F37(): pass

    label("Function_31_3F37")

    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_31_3F37 end

    def Function_32_3F47(): pass

    label("Function_32_3F47")


    def lambda_3F4C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3F4C)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 22750, 0, 2500, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_32_3F47 end

    def Function_33_3F83(): pass

    label("Function_33_3F83")

    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_33_3F83 end

    def Function_34_3F93(): pass

    label("Function_34_3F93")

    OP_95(0xFE, 20500, 0, 3300, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_34_3F93 end

    def Function_35_3FAF(): pass

    label("Function_35_3FAF")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_35_3FAF end

    def Function_36_3FC6(): pass

    label("Function_36_3FC6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_400C")
    OP_63(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x11)
    Sleep(500)
    OP_63(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xD)
    Sleep(500)
    Jump("Function_36_3FC6")

    label("loc_400C")

    Return()

    # Function_36_3FC6 end

    def Function_37_400D(): pass

    label("Function_37_400D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4053")
    OP_63(0x12, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x12)
    Sleep(500)
    OP_63(0xF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xF)
    Sleep(500)
    Jump("Function_37_400D")

    label("loc_4053")

    Return()

    # Function_37_400D end

    def Function_38_4054(): pass

    label("Function_38_4054")

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

    def lambda_412D():
        OP_95(0x20, 1000, 600, 40, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_412D)
    Sleep(800)

    def lambda_414A():
        OP_95(0x101, 200, 0, 700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_414A)
    Sleep(200)

    def lambda_4167():
        OP_95(0x102, 300, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4167)
    Sleep(300)

    def lambda_4184():
        OP_95(0x103, -1000, 0, -950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4184)
    Sleep(100)

    def lambda_41A1():
        OP_95(0x104, -1100, 0, 1100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_41A1)
    Sleep(200)

    def lambda_41BE():
        OP_95(0x109, -2500, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_41BE)
    Sleep(50)

    def lambda_41DB():
        OP_95(0x105, -2400, 0, 700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_41DB)
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

    def lambda_42D0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_42D0)
    Sleep(50)

    def lambda_42E0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_42E0)
    Sleep(50)

    def lambda_42F0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_42F0)
    Sleep(10)

    def lambda_4300():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4300)
    Sleep(30)

    def lambda_4310():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4310)
    Sleep(10)

    def lambda_4320():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4320)
    Sleep(10)

    def lambda_4330():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_4330)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x20, 2)

    ChrTalk(
        0x101,
        "#00005FThis is...\x02",
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
            "#00100FThe Eisengraf, for\x01",
            "exclusive use by the\x01",
            "Imperial government.\x02\x03",
            "#00103FWhat a magnificent\x01",
            "appearance... It's like\x01",
            "a symbol of the Empire.\x02",
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
            "#10103FDefinitely... It feels\x01",
            "truly majestic.\x02",
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
            "#00300FThat Blood and Iron\x01",
            "Chancellor came to Crossbell\x01",
            "on this thing, didn't he.\x02\x03",
            "#00306FThough it had a big impact,\x01",
            "I wonder how much it had to\x01",
            "stand out to satisfy him.\x02",
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
            "#10300FYeah, and it looks like\x01",
            "no mira was spared\x01",
            "constructing it either.\x02",
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
            "#00203F...Its appearance isn't the\x01",
            "only amazing part.\x02\x03",
            "#00200FI heard this train boasts the\x01",
            "highest top speed among all\x01",
            "orbal trains.\x02\x03",
            "However, that information\x01",
            "wasn't disclosed to the public,\x01",
            "so I can't say for certain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FThat's just what you'd expect\x01",
            "from Erebonia. A rail network\x01",
            "covers their entire nation.\x02\x03",
            "#00101FIn the field of rail\x01",
            "transport, they have no\x01",
            "equal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah, I get that feeling\x01",
            "now, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "―Ahem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "I'd like to explain the\x01",
            "job then. Are you all\x01",
            "ready?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_484D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_484D)
    Sleep(50)

    def lambda_485D():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_485D)
    Sleep(30)

    def lambda_486D():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_486D)
    Sleep(20)

    def lambda_487D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_487D)
    Sleep(40)

    def lambda_488D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_488D)
    Sleep(20)

    def lambda_489D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_489D)
    WaitChrThread(0x105, 2)

    ChrTalk(
        0x101,
        (
            "#00005FS-Sorry. We were\x01",
            "startled by its majesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "Yes, very well then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "As I said earlier, you'll\x01",
            "be assisting me with\x01",
            "inspection of this train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Specifically, you're to\x01",
            "check each passenger's\x01",
            "entry permit and luggage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "There's also the safety\x01",
            "check of the train\x01",
            "itself to perform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FUmm, what's a train\x01",
            "safety check?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "You'll help me with it. You'll\x01",
            "follow my instructions and\x01",
            "perform various checks for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Hmm, so there's six of\x01",
            "you in all, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "In that case, you'll form three teams of\x01",
            "two― Two teams will inspect the cabin\x01",
            "and the last will be assisting me.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4C84")

    ChrTalk(
        0x101,
        (
            "#00005FInspection in groups of\x01",
            "two? I remember doing it\x01",
            "alone before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, at least that's how\x01",
            "it was when we assisted\x01",
            "before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "That's right, you have\x01",
            "experience doing this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "It's true we usually inspect\x01",
            "alone, but the security\x01",
            "level's been raised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "For stricter checks,\x01",
            "we'll do it this way\x01",
            "this time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D47")

    label("loc_4C84")


    ChrTalk(
        0x101,
        (
            "#00005FTwo to a group... Do you\x01",
            "always inspect like\x01",
            "this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Well it's normally done\x01",
            "alone, but the security\x01",
            "level's been raised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "For stricter checks,\x01",
            "we'll do it this way\x01",
            "this time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D47")


    ChrTalk(
        0x101,
        "#00000FI see. That makes sense.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Then, will you divide\x01",
            "the teams for me\x01",
            "immediately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "You can even use rock-\x01",
            "paper-scissors if you\x01",
            "like.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FR-Rock-paper-scissors?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Well, honestly speaking, this\x01",
            "isn't a job where individual\x01",
            "aptitude matters all that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "I personally would like to\x01",
            "start this job quickly and\x01",
            "you guys do too, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, well, if that's the\x01",
            "case, I don't have any\x01",
            "objections...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHaha, it's settled then.\x01",
            "It seems fun, so why\x01",
            "not?♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FBut, how are we going to\x01",
            "decide who wins?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Alright, how about these\x01",
            "rules:\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Play as in rock-paper-scissors, and everyone\x01",
            "throws their hand simultaneously. If only two have\x01",
            "the same hand, those form a team and are out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Just repeat that until\x01",
            "the teams are decided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FUmm, I'm not sure how to\x01",
            "put this, but you seem\x01",
            "familiar with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "Haha, I guess so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Actually, when I was a Republican Inspector,\x01",
            "we decided how to divide work like this\x01",
            "occasionally, when we couldn't take a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "It's a flexible concept\x01",
            "all of the straight-laced\x01",
            "Imperial inspectors lack.\x02",
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
            "#00106FI don't know about it\x01",
            "being a flexible\x01",
            "concept, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FAnyway, it's probably a\x01",
            "nationality difference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FHaha, could be.\x02\x03",
            "Anyway, let's try it\x01",
            "out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, let's.\x02",
    )

    CloseMessageWindow()

    def lambda_5320():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5320)
    Sleep(10)

    def lambda_5330():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5330)
    Sleep(10)

    def lambda_5340():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5340)
    Sleep(10)

    def lambda_5350():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5350)
    Sleep(30)

    def lambda_5360():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5360)
    Sleep(10)

    def lambda_5370():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5370)
    WaitChrThread(0x105, 2)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00003FEveryone ready?\x02",
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
            "Throw rock\x01",          # 0
            "Throw scissors\x01",      # 1
            "Throw paper\x01",         # 2
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
    SetChrName("All")

    AnonymousTalk(
        0xFF,
        "#4S#11ARock, paper...\x02",
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

    def lambda_546A():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_546A)

    def lambda_547F():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_547F)

    def lambda_5494():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5494)

    def lambda_54A9():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_54A9)

    def lambda_54BE():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_54BE)

    def lambda_54D3():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_54D3)
    Sound(802, 0, 100, 0)
    SetChrName("All")

    AnonymousTalk(
        0xFF,
        "#4S#11AScissors!\x02",
    )

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BF4")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5550():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5550)

    def lambda_5565():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5565)

    def lambda_557A():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_557A)

    def lambda_558F():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_558F)

    def lambda_55A4():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_55A4)

    def lambda_55B9():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_55B9)
    WaitChrThread(0x101, 1)

    def lambda_55D2():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_55D2)
    Sleep(50)

    def lambda_55E2():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_55E2)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00100F*gigge*, only Tio and I\x01",
            "played scissors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThen Elie and I will\x01",
            "form a group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FThat leaves three rock\x01",
            "and one paper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FThen, the four of us\x01",
            "will play again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, let's keep going.\x02",
    )

    CloseMessageWindow()

    def lambda_56DE():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_56DE)
    Sleep(50)

    def lambda_56EE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_56EE)
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
            "Throw rock\x01",          # 0
            "Throw scissors\x01",      # 1
            "Throw paper\x01",         # 2
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
    SetChrName("All")

    AnonymousTalk(
        0xFF,
        "#4S#11ARock, paper...\x02",
    )

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x101, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)

    def lambda_57B4():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57B4)

    def lambda_57C9():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_57C9)

    def lambda_57DE():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_57DE)

    def lambda_57F3():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_57F3)
    Sound(802, 0, 100, 0)
    SetChrName("All")

    AnonymousTalk(
        0xFF,
        "#4S#11AScissors!\x02",
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

    def lambda_5885():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5885)

    def lambda_589A():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_589A)

    def lambda_58AF():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_58AF)

    def lambda_58C4():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_58C4)
    WaitChrThread(0x101, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59E5")

    def lambda_58EC():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_58EC)
    Sleep(50)

    def lambda_58FC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_58FC)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00005FNoｱl and I played rock,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FHaha. I'm counting on\x01",
            "you, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5963():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5963)
    Sleep(50)

    def lambda_5973():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5973)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00300FWazy and I are left, so\x01",
            "we'll form a group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHehe. I'm counting on\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 4)
    Jump("loc_5BEF")

    label("loc_59E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AF0")

    def lambda_59F9():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_59F9)
    Sleep(50)

    def lambda_5A09():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5A09)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00005FWazy and I played\x01",
            "scissors, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHehe. I'm counting on\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5A6D():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5A6D)
    Sleep(50)

    def lambda_5A7D():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5A7D)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00300FNoｱl and I are left, so\x01",
            "we'll form a group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FRight. I'm counting on\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 5)
    Jump("loc_5BEF")

    label("loc_5AF0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BEF")

    def lambda_5B04():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B04)
    Sleep(50)

    def lambda_5B14():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5B14)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00005FRandy and I had paper,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FYeah. I'm countin' on\x01",
            "ya, buddy.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5B79():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5B79)
    Sleep(50)

    def lambda_5B89():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5B89)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10100FWazy and I are left, so\x01",
            "we'll form a group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FRight. Sounds good.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 3)

    label("loc_5BEF")

    Jump("loc_644C")

    label("loc_5BF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62AF")
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5C2F():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C2F)

    def lambda_5C44():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5C44)

    def lambda_5C59():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5C59)

    def lambda_5C6E():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5C6E)

    def lambda_5C83():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5C83)

    def lambda_5C98():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5C98)
    WaitChrThread(0x101, 1)

    def lambda_5CB1():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5CB1)
    Sleep(50)

    def lambda_5CC1():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5CC1)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00305FHmm, only Noｱl and I\x01",
            "have rock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FSo Randy and I are a\x01",
            "group then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FThen what's left is\x01",
            "three scissors and one\x01",
            "paper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThen the four of us\x01",
            "remaining with repeat\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, let's keep going.\x02",
    )

    CloseMessageWindow()

    def lambda_5DC6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5DC6)
    Sleep(50)

    def lambda_5DD6():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5DD6)
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
            "Throw rock\x01",          # 0
            "Throw scissors\x01",      # 1
            "Throw paper\x01",         # 2
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
    SetChrName("All")

    AnonymousTalk(
        0xFF,
        "#4S#11ARock, paper...\x02",
    )

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    EndChrThread(0x105, 0x3)

    def lambda_5E9C():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E9C)

    def lambda_5EB1():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5EB1)

    def lambda_5EC6():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5EC6)

    def lambda_5EDB():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5EDB)
    Sound(802, 0, 100, 0)
    SetChrName("All")

    AnonymousTalk(
        0xFF,
        "#4S#11AScissors!\x02",
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

    def lambda_5F6D():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F6D)

    def lambda_5F82():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5F82)

    def lambda_5F97():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5F97)

    def lambda_5FAC():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5FAC)
    WaitChrThread(0x101, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60BF")

    def lambda_5FD4():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5FD4)
    Sleep(50)

    def lambda_5FE4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5FE4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00005FTio and I played rock,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FLloyd. I'm counting on\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6044():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6044)
    Sleep(50)

    def lambda_6054():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6054)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00100FWazy and I are left, so\x01",
            "we'll form a group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FRight. Sounds good.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 2)
    Jump("loc_62AA")

    label("loc_60BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61BE")

    def lambda_60D3():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_60D3)
    Sleep(50)

    def lambda_60E3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_60E3)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00005FWazy and I played\x01",
            "scissors, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHehe. I'm counting on\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6147():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6147)
    Sleep(50)

    def lambda_6157():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6157)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00100FThen I'll form a group\x01",
            "with Tio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FElie. I'm counting on\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 5)
    Jump("loc_62AA")

    label("loc_61BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62AA")

    def lambda_61D2():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_61D2)
    Sleep(50)

    def lambda_61E2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_61E2)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00005FElie and I played paper.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHaha, I'm counting you.\x02",
    )

    CloseMessageWindow()

    def lambda_623B():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_623B)
    Sleep(50)

    def lambda_624B():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_624B)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00200FThen Wazy and I are a\x01",
            "group as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FRight. Sounds good.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 1)

    label("loc_62AA")

    Jump("loc_644C")

    label("loc_62AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_644C")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6338():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6338)

    def lambda_634D():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_634D)

    def lambda_6362():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6362)

    def lambda_6377():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6377)

    def lambda_638C():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_638C)

    def lambda_63A1():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_63A1)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#00005FAlright, we've split up.\x02\x03",
            "#00000FWazy and I, Elie and\x01",
            "Tio, and Randy and Noｱl\x01",
            "are the teams, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHehe. I'm counting on\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 5)

    label("loc_644C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 1)), scpexpr(EXPR_END)), "loc_6463")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_64BA")

    label("loc_6463")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 2)), scpexpr(EXPR_END)), "loc_647A")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_64BA")

    label("loc_647A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 3)), scpexpr(EXPR_END)), "loc_6491")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_64BA")

    label("loc_6491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 4)), scpexpr(EXPR_END)), "loc_64A8")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_64BA")

    label("loc_64A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 5)), scpexpr(EXPR_END)), "loc_64BA")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_64BA")


    ChrTalk(
        0x20,
        (
            "Hmm, it looks like\x01",
            "you've decided.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_64E7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_64E7)
    Sleep(10)

    def lambda_64F7():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_64F7)
    Sleep(10)

    def lambda_6507():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6507)
    Sleep(10)

    def lambda_6517():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6517)
    Sleep(30)

    def lambda_6527():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6527)
    Sleep(10)

    def lambda_6537():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6537)
    WaitChrThread(0x105, 2)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00000FWhat about the team\x01",
            "assignments?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 4)), scpexpr(EXPR_END)), "loc_669F")

    ChrTalk(
        0x20,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "I'll having you move\x01",
            "some things, so I'd like\x01",
            "men to help me with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FThat means me and Wazy,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FOh man. If he says it\x01",
            "like that, he means to\x01",
            "work us hard, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Haha. Since you're here, I\x01",
            "intend to use you to the\x01",
            "fullest extent possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_678B")

    label("loc_669F")


    ChrTalk(
        0x109,
        (
            "#10105FOh, would you mind if my group\x01",
            "helped with the safety check?\x02\x03",
            "#10100FI have experience doing vehicle\x01",
            "inspections for the Guardian Force,\x01",
            "so I think I'll be of help to you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x20,
        (
            "I see. Please do so\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_678B")


    ChrTalk(
        0x20,
        (
            "Alright then. Let's\x01",
            "begin work at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "I'm leaving the cabin\x01",
            "check to all of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "The announcement has already been made, so\x01",
            "if you say you're "Assistant Inspectors",\x01",
            "you'll be able to perform your job smoothly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, roger.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 1)), scpexpr(EXPR_END)), "loc_68C9")
    AddParty(0x1, 0xFF, 0xFF)
    Jump("loc_6915")

    label("loc_68C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 2)), scpexpr(EXPR_END)), "loc_68DB")
    AddParty(0x2, 0xFF, 0xFF)
    Jump("loc_6915")

    label("loc_68DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 3)), scpexpr(EXPR_END)), "loc_68ED")
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_6915")

    label("loc_68ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 4)), scpexpr(EXPR_END)), "loc_68FF")
    AddParty(0x8, 0xFF, 0xFF)
    Jump("loc_6915")

    label("loc_68FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 5)), scpexpr(EXPR_END)), "loc_6911")
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_6915")

    label("loc_6911")

    AddParty(0x1, 0xFF, 0xFF)

    label("loc_6915")

    SetScenarioFlags(0x22, 3)
    NewScene("e0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_38_4054 end

    def Function_39_6922(): pass

    label("Function_39_6922")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6952")

    def lambda_6932():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6932)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    Jump("Function_39_6922")

    label("loc_6952")

    Return()

    # Function_39_6922 end

    def Function_40_6953(): pass

    label("Function_40_6953")

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
        (
            "Yes, that was good work\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "That argument over ticket\x01",
            "theft must've been\x01",
            "especially difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, it wasn't such a big\x01",
            "deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIncidentally, it seems\x01",
            "you can identify thefts?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "Yes, it's possible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "We keep information\x01",
            "about the ticket buyers\x01",
            "for times like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "If a theft is detected during\x01",
            "an inspection, the thief can be\x01",
            "arrested at the next station.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FAnyway, what happened to\x01",
            "that old man, the\x01",
            "victim?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "That old man said he was in a\x01",
            "hurry, so we had him\x01",
            "repurchase his ticket for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Once the thief is\x01",
            "caught, he'll be forced\x01",
            "to pay for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHehe, too bad for that\x01",
            "old man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FWell, at least it seems\x01",
            "like it'll be able to be\x01",
            "solved immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Yeah. Anyway, you did\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "You really helped me a\x01",
            "lot, so thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSame here. We're glad we\x01",
            "could help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIf something comes up\x01",
            "again, please feel free\x01",
            "to contact us.\x02",
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
            "Quest [Republican\x01",
            "Inspector Assistance]\x07\x00\x01",
            "completed!\x02",
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

    # Function_40_6953 end

    def Function_41_6E9E(): pass

    label("Function_41_6E9E")

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
        "I heard everything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "That was good work\x01",
            "solving the theft.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIt was no big deal.\x02\x03",
            "#00000FSo, what'll happen to\x01",
            "the young man who\x01",
            "committed the theft?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Ah, well that crime is\x01",
            "irrelevant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHuh? What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Yes, well you see, the old man\x01",
            "that was the victim declared\x01",
            "that no theft occurred.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "And the young man said only\x01",
            "that he forgot to buy a ticket\x01",
            "after entering the platform...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "If the parties are saying\x01",
            "that, there's no crime\x01",
            "for us to go after.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F*sigh*, this again,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FHmm. Maybe Shing told\x01",
            "him how to handle this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHehe. Could be.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FThen, what about the\x01",
            "trader?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Yeah, actually, he was a\x01",
            "big arrest for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "He's actually a broker\x01",
            "who sells forged\x01",
            "tickets.\x02",
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
        "#00005FR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FBut, why was he on the\x01",
            "train, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Yeah, it seems he was\x01",
            "testing his own goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Honestly, the audacity\x01",
            "of this guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Ah, but you guys did\x01",
            "amazing work out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "You really helped me a\x01",
            "lot, so thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSame here. We're glad we\x01",
            "could help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIf something comes up\x01",
            "again, please feel free\x01",
            "to contact us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Alright. See you later,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x20, 0x2D, 0x1F4)
    OP_95(0x20, 5760, 0, 2550, 2000, 0x0)

    def lambda_74E1():
        OP_95(0x20, 24940, 0, 2810, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_74E1)
    Sleep(500)
    OP_68(-1190, 1500, -230, 2000)
    MoveCamera(45, 34, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(15430, 2000)
    Sleep(1500)

    def lambda_752F():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_752F)
    Sleep(10)

    def lambda_753F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_753F)
    Sleep(10)

    def lambda_754F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_754F)
    Sleep(10)

    def lambda_755F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_755F)
    Sleep(30)

    def lambda_756F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_756F)
    Sleep(10)

    def lambda_757F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_757F)
    WaitChrThread(0x105, 2)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 1)), scpexpr(EXPR_END)), "loc_77D7")

    ChrTalk(
        0x109,
        (
            "#10100FAll things considered, it\x01",
            "looked like Shing played a\x01",
            "big part in all of this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHaha. I never thought\x01",
            "we'd see him again in a\x01",
            "place like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah, and once again I\x01",
            "was made acutely aware\x01",
            "of his great talent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FDamn. And he's only\x01",
            "gonna be worse when he\x01",
            "grows up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FHmm, we only caught a\x01",
            "glimpse of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHaha, he's a cute little\x01",
            "boy in appearance,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha, you're certainly\x01",
            "right about that.\x02\x03",
            "#00003FAnyhow, the case is\x01",
            "closed.\x02\x03",
            "#00000FLet's move on to the\x01",
            "next job after a short\x01",
            "break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8087")

    label("loc_77D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 2)), scpexpr(EXPR_END)), "loc_79F2")

    ChrTalk(
        0x102,
        (
            "#00100FBe that as it may, it\x01",
            "seems that Shing played\x01",
            "an active role.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYes, he is still very\x01",
            "young but I was\x01",
            "surprised in many ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, once again I was\x01",
            "made acutely aware of\x01",
            "his great talent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FDamn. And he's only\x01",
            "gonna be worse when he\x01",
            "grows up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYes, indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHaha, he's a cute little\x01",
            "boy in appearance,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha, you're certainly\x01",
            "right about that.\x02\x03",
            "#00003FAnyhow, the case is\x01",
            "closed.\x02\x03",
            "#00000FLet's move on to the\x01",
            "next job after a short\x01",
            "break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8087")

    label("loc_79F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 3)), scpexpr(EXPR_END)), "loc_7C0D")

    ChrTalk(
        0x102,
        (
            "#00100FBe that as it may, it\x01",
            "seems that Shing played\x01",
            "an active role.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FYeah. The same as ever,\x01",
            "I'd say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FRight? Once again I was\x01",
            "made acutely aware of\x01",
            "his great talent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FWhat can I say? He's\x01",
            "only going to get worse,\x01",
            "isn't he.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FHmm, we only caught a\x01",
            "glimpse of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHaha, he's a cute little\x01",
            "boy in appearance,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha, you're certainly\x01",
            "right about that.\x02\x03",
            "#00003FAnyhow, the case is\x01",
            "closed.\x02\x03",
            "#00000FLet's move on to the\x01",
            "next job after a short\x01",
            "break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8087")

    label("loc_7C0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 4)), scpexpr(EXPR_END)), "loc_7E4C")

    ChrTalk(
        0x102,
        (
            "#00100FBe that as it may, it\x01",
            "seems that Shing played\x01",
            "an active role.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes. Who would have\x01",
            "thought we'd see him again\x01",
            "in a place like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, and once again I\x01",
            "was made acutely aware\x01",
            "of his great talent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FDamn. And he's only\x01",
            "gonna be worse when he\x01",
            "grows up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FHmm, we only caught a\x01",
            "glimpse of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHaha, he's a cute little\x01",
            "boy in appearance,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha, you're certainly\x01",
            "right about that.\x02\x03",
            "#00003FAnyhow, the case is\x01",
            "closed.\x02\x03",
            "#00000FLet's move on to the\x01",
            "next job after a short\x01",
            "break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8087")

    label("loc_7E4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 5)), scpexpr(EXPR_END)), "loc_8087")

    ChrTalk(
        0x102,
        (
            "#00100FBe that as it may, it\x01",
            "seems that Shing played\x01",
            "an active role.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHehe. Who would have\x01",
            "thought we'd see him again\x01",
            "in a place like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, and once again I\x01",
            "was made acutely aware\x01",
            "of his great talent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FDamn. And he's only\x01",
            "gonna be worse when he\x01",
            "grows up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FHmm, we only caught a\x01",
            "glimpse of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FHaha, he's a cute little\x01",
            "boy in appearance,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha, you're certainly\x01",
            "right about that.\x02\x03",
            "#00003FAnyhow, the case is\x01",
            "closed.\x02\x03",
            "#00000FLet's move on to the\x01",
            "next job after a short\x01",
            "break.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8087")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Republican\x01",
            "Inspector Assistance]\x07\x00\x01",
            "completed!\x02",
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

    # Function_41_6E9E end

    def Function_42_8116(): pass

    label("Function_42_8116")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81AF")
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
    Jump("loc_8229")

    label("loc_81AF")

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

    label("loc_8229")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82DE")
    OP_68(-1150, 1000, 0, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(16500, 4000)
    Jump("loc_8315")

    label("loc_82DE")

    OP_68(-1150, 1000, -16000, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(16500, 4000)

    label("loc_8315")


    def lambda_831A():
        OP_97(0x101, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_831A)
    Sleep(50)

    def lambda_8337():
        OP_97(0x102, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8337)
    Sleep(50)

    def lambda_8354():
        OP_97(0x103, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8354)
    Sleep(50)

    def lambda_8371():
        OP_97(0x104, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8371)
    Sleep(50)

    def lambda_838E():
        OP_97(0xF4, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_838E)
    Sleep(50)

    def lambda_83AB():
        OP_97(0xF5, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_83AB)
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
            "#00306F#5PStill, platforms with no\x01",
            "people are quite the sad\x01",
            "thing, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206F...The trains seem to\x01",
            "have been out of service\x01",
            "for a long time as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00108FRight...\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0xB4, 0x1F4)
    Sleep(150)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84F5")

    ChrTalk(
        0x102,
        (
            "#5P#00101F...The No. 3 platform\x01",
            "train... Is it that one?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8533")

    label("loc_84F5")


    ChrTalk(
        0x102,
        (
            "#5P#00101F...The No. 3 platform\x01",
            "train... Is it this one?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8533")

    OP_68(-1150, 1000, -24100, 3000)
    MoveCamera(63, 27, 0, 3000)
    SetCameraDistance(25500, 3000)

    def lambda_855D():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_855D)
    Sleep(50)

    def lambda_856D():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_856D)
    Sleep(50)

    def lambda_857D():
        OP_93(0xF4, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_857D)
    Sleep(50)

    def lambda_858D():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_858D)
    Sleep(50)

    def lambda_859D():
        OP_93(0xF5, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_859D)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8653")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8619")

    ChrTalk(
        0x10A,
        (
            "#00601FHmph, it was the 2nd car\x01",
            "from the front.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_864E")

    label("loc_8619")


    ChrTalk(
        0x10A,
        (
            "#00601FHmph, it was the 2nd car\x01",
            "from the front.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_864E")

    Jump("loc_8770")

    label("loc_8653")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_86E3")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86AA")

    ChrTalk(
        0x109,
        (
            "#10101FYes, it was the 2nd car\x01",
            "from the front.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86DE")

    label("loc_86AA")


    ChrTalk(
        0x109,
        (
            "#10101FYes, it was the 2nd car\x01",
            "from the front.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86DE")

    Jump("loc_8770")

    label("loc_86E3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8770")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_873B")

    ChrTalk(
        0x105,
        (
            "#10400FYeah, it was the 2nd car\x01",
            "from the front.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8770")

    label("loc_873B")


    ChrTalk(
        0x105,
        (
            "#10400FYeah, it was the 2nd car\x01",
            "from the front.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8770")

    OP_57(0x0)
    OP_5A()
    Fade(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87B9")
    OP_68(-1150, 1000, 0, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    Jump("loc_87E7")

    label("loc_87B9")

    OP_68(-1150, 1000, -16000, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)

    label("loc_87E7")

    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8855")
    OP_93(0x106, 0x5A, 0x1F4)

    ChrTalk(
        0x106,
        (
            "#6P#10701FIt looks like we can\x01",
            "cross from the connecting\x01",
            "bridge over there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_891C")

    label("loc_8855")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_88C2")
    OP_93(0x105, 0x5A, 0x1F4)

    ChrTalk(
        0x105,
        (
            "#6P#10400FIt looks like we can\x01",
            "cross from the connecting\x01",
            "bridge over there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_891C")

    label("loc_88C2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_891C")
    OP_93(0x109, 0x5A, 0x1F4)

    ChrTalk(
        0x109,
        (
            "#6P#10101FWe can cross from the\x01",
            "connecting bridge over\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_891C")


    def lambda_8921():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8921)
    Sleep(50)

    def lambda_8931():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8931)
    Sleep(50)

    def lambda_8941():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8941)
    Sleep(50)

    def lambda_8951():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8951)
    Sleep(50)

    def lambda_8961():
        OP_93(0xF4, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_8961)
    Sleep(50)

    def lambda_8971():
        OP_93(0xF5, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_8971)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x101,
        "#5P#00001FAlright... Let's go.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89DC")
    SetChrPos(0x0, -2500, 0, 0, 90)
    Jump("loc_89ED")

    label("loc_89DC")

    SetChrPos(0x0, -2500, 0, -16000, 90)

    label("loc_89ED")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1A5, 7)
    EventEnd(0x5)
    Return()

    # Function_42_8116 end

    def Function_43_8A07(): pass

    label("Function_43_8A07")

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
            "#11P#00008F(Platform No. 3, the 2nd\x01",
            "car... and the door's\x01",
            "unlocked.)\x02\x03",
            "#00013F(...What to do?)\x02",
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
            "Open the door and enter\x01",      # 0
            "Step away\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8B76"),
        (1, "loc_8C1D"),
        (SWITCH_DEFAULT, "loc_8C4D"),
    )


    label("loc_8B76")

    Sound(454, 0, 100, 0)
    OP_71(0x0, 0x295, 0x2B2, 0x0, 0x0)
    OP_79(0x0)
    OP_68(10190, 1200, -25980, 4000)

    def lambda_8BA1():
        OP_95(0xFE, 10000, 0, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8BA1)
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
    Jump("loc_8C4D")

    label("loc_8C1D")

    SetChrPos(0x0, 8710, 0, -29420, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Jump("loc_8C4D")

    label("loc_8C4D")

    Return()

    # Function_43_8A07 end

    def Function_44_8C4E(): pass

    label("Function_44_8C4E")


    def lambda_8C53():
        OP_95(0xFE, 10000, 0, -28000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8C53)
    WaitChrThread(0xFE, 1)

    def lambda_8C71():
        OP_95(0xFE, 10000, 0, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8C71)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_44_8C4E end

    def Function_45_8C8B(): pass

    label("Function_45_8C8B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30200.itc", 0x1E)
    LoadChrToIndex("chr/ch24100.itc", 0x1F)
    LoadChrToIndex("chr/ch21800.itc", 0x20)
    LoadChrToIndex("apl/ch51216.itc", 0x21)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8CCA")
    LoadChrToIndex("apl/ch51217.itc", 0x22)
    Jump("loc_8D31")

    label("loc_8CCA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8CE5")
    LoadChrToIndex("apl/ch51218.itc", 0x22)
    Jump("loc_8D31")

    label("loc_8CE5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D00")
    LoadChrToIndex("apl/ch51219.itc", 0x22)
    Jump("loc_8D31")

    label("loc_8D00")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D1B")
    LoadChrToIndex("apl/ch51220.itc", 0x22)
    Jump("loc_8D31")

    label("loc_8D1B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D31")
    LoadChrToIndex("apl/ch51221.itc", 0x22)

    label("loc_8D31")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8DAB")
    SetChrPos(0x102, -14410, 590, -16430, 90)
    Jump("loc_8E3E")

    label("loc_8DAB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8DD1")
    SetChrPos(0x103, -14410, 590, -16430, 90)
    Jump("loc_8E3E")

    label("loc_8DD1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8DF7")
    SetChrPos(0x104, -14410, 590, -16430, 90)
    Jump("loc_8E3E")

    label("loc_8DF7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8E1D")
    SetChrPos(0x109, -14410, 590, -16430, 90)
    Jump("loc_8E3E")

    label("loc_8E1D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8E3E")
    SetChrPos(0x105, -14410, 590, -16430, 90)

    label("loc_8E3E")

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

    def lambda_8EA0():
        OP_95(0xFE, -1500, 10, -16020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_8EA0)

    def lambda_8EBA():
        OP_95(0xFE, -3000, 10, -15160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8EBA)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8EFE")

    def lambda_8EE4():
        OP_95(0xFE, -3600, 10, -17180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8EE4)
    Jump("loc_8FB5")

    label("loc_8EFE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F2D")

    def lambda_8F13():
        OP_95(0xFE, -3600, 10, -17180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8F13)
    Jump("loc_8FB5")

    label("loc_8F2D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F5C")

    def lambda_8F42():
        OP_95(0xFE, -3600, 10, -17180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8F42)
    Jump("loc_8FB5")

    label("loc_8F5C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F8B")

    def lambda_8F71():
        OP_95(0xFE, -3600, 10, -17180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8F71)
    Jump("loc_8FB5")

    label("loc_8F8B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8FB5")

    def lambda_8FA0():
        OP_95(0xFE, -3600, 10, -17180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8FA0)

    label("loc_8FB5")

    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x21, 1)
    WaitChrThread(0x101, 1)
    Sound(801, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Announcement")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Inspection of the\x01",
            "Republic-bound will be\x01",
            "concluding shortly.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "We ask you to please\x01",
            "remain outside the train\x01",
            "for a little while longer.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00005FThe Republic-bound train\x01",
            "is going to depart\x01",
            "soon...\x02\x03",
            "#00003FWell then... I wonder\x01",
            "where the fake brand\x01",
            "trader is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "When I popped in before,\x01",
            "I'm sure she was around\x01",
            "there...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_918E")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00101F...There she is.\x02",
    )

    CloseMessageWindow()
    Jump("loc_92AA")

    label("loc_918E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91D2")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#00201F...Found her.\x02",
    )

    CloseMessageWindow()
    Jump("loc_92AA")

    label("loc_91D2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9212")
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#00301F...Bingo.\x02",
    )

    CloseMessageWindow()
    Jump("loc_92AA")

    label("loc_9212")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_925F")
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105F...She the one, right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_92AA")

    label("loc_925F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_92AA")
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x105,
        (
            "#10305F...I guess she's the\x01",
            "one?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92AA")

    Fade(500)
    OP_68(11100, 1200, -13380, 0)
    MoveCamera(40, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14210, 0)
    OP_0D()

    ChrTalk(
        0x23,
        (
            "─Hoho, a fellow trader,\x01",
            "I see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "And, how was business in\x01",
            "Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x22,
        "Elderly Woman",
        (
            "#11PHaha. It's really too\x01",
            "bad...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x22,
        "Elderly Woman",
        (
            "#11PThere was some\x01",
            "interference due to a\x01",
            "business rivalry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Mrrr... That's\x01",
            "unfortunate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Honestly, guys like them\x01",
            "are a disgrace to us\x01",
            "traders.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x22,
        "Elderly Woman",
        (
            "#11PNo, I think it was also\x01",
            "a lack of power on my\x01",
            "part.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x22,
        "Elderly Woman",
        (
            "#11PThat's why I'm thinking of\x01",
            "making a fresh start and\x01",
            "heading for the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Hah hah ha, that's an\x01",
            "admirable business\x01",
            "spirit you have there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Hmm. Even us meeting\x01",
            "like this might be some\x01",
            "kind of fate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "If you like, I could\x01",
            "introduce you to some good\x01",
            "connections in the Empire.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x22,
        "Elderly Woman",
        "#11POh my, really?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x22,
        "Elderly Woman",
        (
            "#11POhoho... Thank you then,\x01",
            "I think I'll take up on\x01",
            "your offer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F...Actually, you won't.\x02",
    )

    CloseMessageWindow()
    OP_63(0x22, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x22,
        "Elderly Woman",
        "#11PHuh...\x02",
    )

    CloseMessageWindow()
    OP_68(7590, 1700, -13830, 3000)
    MoveCamera(45, 12, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(14960, 3000)
    SetChrPos(0x101, 1130, 0, -14460, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_96C4")
    SetChrPos(0x102, -1220, 0, -14540, 90)
    Jump("loc_9757")

    label("loc_96C4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_96EA")
    SetChrPos(0x103, -1220, 0, -14540, 90)
    Jump("loc_9757")

    label("loc_96EA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9710")
    SetChrPos(0x104, -1220, 0, -14540, 90)
    Jump("loc_9757")

    label("loc_9710")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9736")
    SetChrPos(0x109, -1220, 0, -14540, 90)
    Jump("loc_9757")

    label("loc_9736")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9757")
    SetChrPos(0x105, -1220, 0, -14540, 90)

    label("loc_9757")

    SetChrPos(0x21, -140, 0, -16200, 90)

    def lambda_976D():
        OP_95(0xFE, 6590, 0, -12750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_976D)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_97B1")

    def lambda_9797():
        OP_95(0xFE, 5030, 0, -12420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9797)
    Jump("loc_9868")

    label("loc_97B1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_97E0")

    def lambda_97C6():
        OP_95(0xFE, 5030, 0, -12420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_97C6)
    Jump("loc_9868")

    label("loc_97E0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_980F")

    def lambda_97F5():
        OP_95(0xFE, 5030, 0, -12420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_97F5)
    Jump("loc_9868")

    label("loc_980F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_983E")

    def lambda_9824():
        OP_95(0xFE, 5030, 0, -12420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9824)
    Jump("loc_9868")

    label("loc_983E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9868")

    def lambda_9853():
        OP_95(0xFE, 5030, 0, -12420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9853)

    label("loc_9868")


    def lambda_986D():
        OP_95(0xFE, 5280, 0, -14060, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_986D)
    Sleep(1000)

    def lambda_988A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_988A)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_98BD")
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x5A, 0x0)
    Jump("loc_9938")

    label("loc_98BD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_98DD")
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x5A, 0x0)
    Jump("loc_9938")

    label("loc_98DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_98FD")
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x5A, 0x0)
    Jump("loc_9938")

    label("loc_98FD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_991D")
    WaitChrThread(0x109, 1)
    OP_93(0x109, 0x5A, 0x0)
    Jump("loc_9938")

    label("loc_991D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9938")
    WaitChrThread(0x105, 1)
    OP_93(0x105, 0x5A, 0x0)

    label("loc_9938")

    WaitChrThread(0x21, 1)
    OP_93(0x21, 0x5A, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00003FCrossbell Police,\x01",
            "Special Support Section.\x02\x03",
            "#00000FMadam, long time no see.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x22,
        "Elderly Woman",
        "#11PY-You are...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A25")

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*... It looks\x01",
            "like you remember us,\x01",
            "fake brand trader lady.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B7F")

    label("loc_9A25")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A74")

    ChrTalk(
        0x103,
        (
            "#00200FSo you remembered us,\x01",
            "fake brand trader lady.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B7F")

    label("loc_9A74")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9AD2")

    ChrTalk(
        0x104,
        (
            "#00300FHehe, looks like you\x01",
            "remember us, fake brand\x01",
            "trader grandma.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B7F")

    label("loc_9AD2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9B2A")

    ChrTalk(
        0x109,
        (
            "#10101FIs she the fake brand\x01",
            "trader I've heard so\x01",
            "much about?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B7F")

    label("loc_9B2A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9B7F")

    ChrTalk(
        0x105,
        (
            "#10304FI see, this madame is\x01",
            "the rumored fake brand\x01",
            "trader, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B7F")


    ChrTalk(
        0x21,
        (
            "You thought you\x01",
            "completely lost us, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "Haha, you won't get away\x01",
            "this time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "W-Wait... What the heck\x01",
            "is going on here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Fake brand...? What are\x01",
            "you talking about?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x22,
        "Elderly Woman",
        "#11P...Uh... Uuuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FBased on changes to state\x01",
            "law, we're taking you in on\x01",
            "suspicion of illegal trading.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "We've got the station\x01",
            "surrounded. There'll be\x01",
            "no escape this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "You're not still\x01",
            "thinking of escaping,\x01",
            "are you?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x22,
        "Elderly Woman",
        (
            "#11P............\x01",
            "............\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x22,
        "Elderly Woman",
        (
            "#11P............\x01",
            "......n't...... joke...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F......!\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x22,
        (
            "#11P#5SThis isn't a joke you\x01",
            "damn shitty\x01",
            "braaaaaats!!#3S\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x23, 0x22, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E37")

    ChrTalk(
        0x102,
        "#00105FEeek!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9EDA")

    label("loc_9E37")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E60")

    ChrTalk(
        0x103,
        "#00210F......!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9EDA")

    label("loc_9E60")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E87")

    ChrTalk(
        0x104,
        "#00305FWhoa!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9EDA")

    label("loc_9E87")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9EB2")

    ChrTalk(
        0x109,
        "#10105FEeeeeeh!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9EDA")

    label("loc_9EB2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9EDA")

    ChrTalk(
        0x105,
        "#10305F...*whoo*♪\x02",
    )

    CloseMessageWindow()

    label("loc_9EDA")


    ChrTalk(
        0x21,
        "Eek!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "W-W-W-W-What!?\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x22,
        (
            "#11P#5SCornering me in a place\x01",
            "like this so I can't\x01",
            "escape...#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x22,
        (
            "#11P#5SNot once, but twice\x01",
            "even!! How dare you\x01",
            "arrest meee!!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x22,
        (
            "#11P#5SYou're always sneaking\x01",
            "around like this! That's\x01",
            "why I hate you police!!#3S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FW-Well, "sneaking" you say...\x01",
            "Wasn't taking refuge into the\x01",
            "station your own mista...\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x22,
        "#11P#5SSilence!#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#11P...Hmph, whatever. I\x01",
            "don't care if I'm\x01",
            "surrounded or whatever...\x02",
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
            "#11P#5S#15A#NIf you want to catch me,\x01",
            "then just go ahead and\x01",
            "tryyy!!#3S\x02",
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
            "#00006FMo matter how many times\x01",
            "I see it, she makes\x01",
            "quite the impact...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A280")

    ChrTalk(
        0x102,
        (
            "#00107F...Wait, Lloyd! This is\x01",
            "no time to be spacing\x01",
            "out...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3BB")

    label("loc_A280")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A2D0")

    ChrTalk(
        0x103,
        (
            "#00205F...Lloyd! This is no\x01",
            "time to be spacing\x01",
            "out...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3BB")

    label("loc_A2D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A31C")

    ChrTalk(
        0x104,
        (
            "#00307FHey, Lloyd! What're you\x01",
            "spacin' out about?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3BB")

    label("loc_A31C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A370")

    ChrTalk(
        0x109,
        (
            "#10105FHah... Lloyd! This is no\x01",
            "time to be spacing\x01",
            "out...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3BB")

    label("loc_A370")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A3BB")

    ChrTalk(
        0x105,
        (
            "#10301F...It's not the time to\x01",
            "be spacing out, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3BB")


    ChrTalk(
        0x21,
        "R-Right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FY-Yeah, let's chase\x01",
            "after her!\x02\x03",
            "#00000FExits and entrances are\x01",
            "all secure... We just\x01",
            "need to catch her!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 46)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A45E")
    BeginChrThread(0x102, 1, 0, 47)
    Jump("loc_A4C5")

    label("loc_A45E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A479")
    BeginChrThread(0x103, 1, 0, 47)
    Jump("loc_A4C5")

    label("loc_A479")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A494")
    BeginChrThread(0x104, 1, 0, 47)
    Jump("loc_A4C5")

    label("loc_A494")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A4AF")
    BeginChrThread(0x109, 1, 0, 47)
    Jump("loc_A4C5")

    label("loc_A4AF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A4C5")
    BeginChrThread(0x105, 1, 0, 47)

    label("loc_A4C5")

    BeginChrThread(0x21, 1, 0, 48)
    Sleep(3500)
    OP_63(0x23, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x23)

    ChrTalk(
        0x23,
        "Whaaaa...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A51D")
    EndChrThread(0x102, 0x1)
    Jump("loc_A57C")

    label("loc_A51D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A536")
    EndChrThread(0x103, 0x1)
    Jump("loc_A57C")

    label("loc_A536")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A54F")
    EndChrThread(0x104, 0x1)
    Jump("loc_A57C")

    label("loc_A54F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A568")
    EndChrThread(0x109, 0x1)
    Jump("loc_A57C")

    label("loc_A568")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A57C")
    EndChrThread(0x105, 0x1)

    label("loc_A57C")

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
        (
            "Tch, those damn shitty\x01",
            "brats...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x22, 1)

    ChrTalk(
        0x22,
        (
            "If they're ambushing me in\x01",
            "the station premises, I\x01",
            "have to find a way out...\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x1F4)
    Sound(801, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Announcement")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "─Thank you for waiting. The\x01",
            "Republic-bound train will\x01",
            "be departing momentarily.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Since it is dangerous,\x01",
            "please refrain from\x01",
            "rushing to get onboard.\x02",
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
        "...This is it!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A7FB")
    SetChrPos(0x102, 54450, 0, -16550, 90)
    Jump("loc_A88E")

    label("loc_A7FB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A821")
    SetChrPos(0x103, 54450, 0, -16550, 90)
    Jump("loc_A88E")

    label("loc_A821")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A847")
    SetChrPos(0x104, 54450, 0, -16550, 90)
    Jump("loc_A88E")

    label("loc_A847")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A86D")
    SetChrPos(0x109, 54450, 0, -16550, 90)
    Jump("loc_A88E")

    label("loc_A86D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A88E")
    SetChrPos(0x105, 54450, 0, -16550, 90)

    label("loc_A88E")

    SetChrPos(0x21, 53420, 0, -15670, 90)

    def lambda_A8A4():
        OP_95(0xFE, 66750, 6000, -15280, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A8A4)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A8EB")

    def lambda_A8D1():
        OP_95(0xFE, 66090, 6000, -16660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A8D1)
    Jump("loc_A9A2")

    label("loc_A8EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A91A")

    def lambda_A900():
        OP_95(0xFE, 66090, 6000, -16660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A900)
    Jump("loc_A9A2")

    label("loc_A91A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A949")

    def lambda_A92F():
        OP_95(0xFE, 66090, 6000, -16660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A92F)
    Jump("loc_A9A2")

    label("loc_A949")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A978")

    def lambda_A95E():
        OP_95(0xFE, 66090, 6000, -16660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A95E)
    Jump("loc_A9A2")

    label("loc_A978")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A9A2")

    def lambda_A98D():
        OP_95(0xFE, 66090, 6000, -16660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A98D)

    label("loc_A9A2")

    Sleep(100)

    def lambda_A9AA():
        OP_95(0xFE, 65090, 6000, -15890, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_A9AA)
    OP_0D()
    WaitChrThread(0x101, 1)

    def lambda_A9C9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A9C9)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A9F7")
    WaitChrThread(0x102, 1)

    def lambda_A9EA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A9EA)
    Jump("loc_AA8A")

    label("loc_A9F7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA1D")
    WaitChrThread(0x103, 1)

    def lambda_AA10():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AA10)
    Jump("loc_AA8A")

    label("loc_AA1D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA43")
    WaitChrThread(0x104, 1)

    def lambda_AA36():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AA36)
    Jump("loc_AA8A")

    label("loc_AA43")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA69")
    WaitChrThread(0x109, 1)

    def lambda_AA5C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AA5C)
    Jump("loc_AA8A")

    label("loc_AA69")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA8A")
    WaitChrThread(0x105, 1)

    def lambda_AA82():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AA82)

    label("loc_AA8A")

    WaitChrThread(0x21, 1)

    def lambda_AA93():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_AA93)
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
        "#00005F#5ST-That's...#3S\x02",
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

    def lambda_AC0A():
        OP_96(0xFE, 0x33450, 0xFFFFF9F2, 0x1FA4, 0x251C, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_AC0A)
    Sleep(2000)

    ChrTalk(
        0x21,
        "#5S#6AWHAAAAAAAT!!?#3S\x02",
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
        "#00011FI- Did she just...!?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ACE6")

    ChrTalk(
        0x102,
        (
            "#00105FI-I don't believe\x01",
            "it...!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ADB1")

    label("loc_ACE6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD11")

    ChrTalk(
        0x103,
        "#00205FN-No way!\x02",
    )

    CloseMessageWindow()
    Jump("loc_ADB1")

    label("loc_AD11")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD46")

    ChrTalk(
        0x104,
        "#00305FHey now, for real!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_ADB1")

    label("loc_AD46")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD80")

    ChrTalk(
        0x109,
        "#10101FUgh... what a way to...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_ADB1")

    label("loc_AD80")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ADB1")

    ChrTalk(
        0x105,
        "#10305F...She's quite good.\x02",
    )

    CloseMessageWindow()

    label("loc_ADB1")


    ChrTalk(
        0x21,
        "R-Right at the very end!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "Aah, what am I gonna say\x01",
            "to Inspector Donovan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F............\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE7D")

    ChrTalk(
        0x101,
        "#00001F...Let's go, Elie!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F...! R-Right,\x01",
            "understood!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFCE")

    label("loc_AE7D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AEC8")

    ChrTalk(
        0x101,
        "#00001F...Let's go, Tio!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F...! Roger!\x02",
    )

    CloseMessageWindow()
    Jump("loc_AFCE")

    label("loc_AEC8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF1C")

    ChrTalk(
        0x101,
        "#00001F...Let's go, Randy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302F...! Yeah, got it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_AFCE")

    label("loc_AF1C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF6B")

    ChrTalk(
        0x101,
        "#00001F...Let's go, Noｱl!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F...! Yes, sir!\x02",
    )

    CloseMessageWindow()
    Jump("loc_AFCE")

    label("loc_AF6B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AFCE")

    ChrTalk(
        0x101,
        "#00001F...Let's go, Wazy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHehe... You too don't\x01",
            "want to lose, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFCE")

    OP_93(0x21, 0x5A, 0x1F4)
    OP_63(0x21, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x21,
        (
            "...Huh... Don't tell\x01",
            "me...\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x21,
        "#5S...WHAT!?#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "A-Are you kidding me?\x01",
            "You're not gonna chase\x01",
            "her, are you!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007FIf we're going to arrest\x01",
            "her, we have no choice!\x02\x03",
            "#00003FThere's no time! We're\x01",
            "going on ahead!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    def lambda_B0EF():
        OP_95(0xFE, 66750, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B0EF)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B136")

    def lambda_B11C():
        OP_95(0xFE, 66090, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B11C)
    Jump("loc_B1ED")

    label("loc_B136")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B165")

    def lambda_B14B():
        OP_95(0xFE, 66090, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B14B)
    Jump("loc_B1ED")

    label("loc_B165")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B194")

    def lambda_B17A():
        OP_95(0xFE, 66090, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B17A)
    Jump("loc_B1ED")

    label("loc_B194")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B1C3")

    def lambda_B1A9():
        OP_95(0xFE, 66090, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B1A9)
    Jump("loc_B1ED")

    label("loc_B1C3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B1ED")

    def lambda_B1D8():
        OP_95(0xFE, 66090, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B1D8)

    label("loc_B1ED")

    OP_63(0x21, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(2000)
    OP_64(0x21)

    ChrTalk(
        0x21,
        (
            "W-What to do... I can't\x01",
            "just leave it to the\x01",
            "Support Section...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x21)

    ChrTalk(
        0x21,
        "#5S...U-UWAAAAAH!#3S\x02",
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0x21, 65890, 6000, -15300, 4000, 0x0)

    def lambda_B2A7():
        OP_95(0xFE, 66750, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_B2A7)
    Sleep(1000)
    Fade(500)
    EndChrThread(0x101, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B2E1")
    EndChrThread(0x102, 0x1)
    Jump("loc_B340")

    label("loc_B2E1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B2FA")
    EndChrThread(0x103, 0x1)
    Jump("loc_B340")

    label("loc_B2FA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B313")
    EndChrThread(0x104, 0x1)
    Jump("loc_B340")

    label("loc_B313")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B32C")
    EndChrThread(0x109, 0x1)
    Jump("loc_B340")

    label("loc_B32C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B340")
    EndChrThread(0x105, 0x1)

    label("loc_B340")

    EndChrThread(0x21, 0x1)
    OP_68(69980, 1500, 7190, 0)
    MoveCamera(43, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(30010, 0)
    SetChrPos(0x101, 66310, 6000, -9500, 0)
    SetChrFlags(0x101, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B3B3")
    SetChrPos(0x102, 66090, 6000, -10500, 0)
    SetChrFlags(0x102, 0x40)
    Jump("loc_B45A")

    label("loc_B3B3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B3DE")
    SetChrPos(0x103, 66090, 6000, -10500, 0)
    SetChrFlags(0x103, 0x40)
    Jump("loc_B45A")

    label("loc_B3DE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B409")
    SetChrPos(0x104, 66090, 6000, -10500, 0)
    SetChrFlags(0x104, 0x40)
    Jump("loc_B45A")

    label("loc_B409")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B434")
    SetChrPos(0x109, 66090, 6000, -10500, 0)
    SetChrFlags(0x109, 0x40)
    Jump("loc_B45A")

    label("loc_B434")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B45A")
    SetChrPos(0x105, 66090, 6000, -10500, 0)
    SetChrFlags(0x105, 0x40)

    label("loc_B45A")

    SetChrPos(0x21, 66310, 6000, -11500, 0)
    SetChrFlags(0x21, 0x40)
    Sound(456, 0, 100, 0)
    StopSound(835, 1000, 100)
    BeginChrThread(0x8, 1, 0, 54)
    OP_0D()
    BeginChrThread(0x101, 1, 0, 50)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B4A7")
    BeginChrThread(0x102, 1, 0, 51)
    Jump("loc_B50E")

    label("loc_B4A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B4C2")
    BeginChrThread(0x103, 1, 0, 51)
    Jump("loc_B50E")

    label("loc_B4C2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B4DD")
    BeginChrThread(0x104, 1, 0, 51)
    Jump("loc_B50E")

    label("loc_B4DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B4F8")
    BeginChrThread(0x109, 1, 0, 51)
    Jump("loc_B50E")

    label("loc_B4F8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B50E")
    BeginChrThread(0x105, 1, 0, 51)

    label("loc_B50E")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B567")
    ClearChrFlags(0x102, 0x40)
    ClearChrFlags(0x102, 0x20)
    ClearChrFlags(0x102, 0x1000)
    Jump("loc_B5F2")

    label("loc_B567")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B58B")
    ClearChrFlags(0x103, 0x40)
    ClearChrFlags(0x103, 0x20)
    ClearChrFlags(0x103, 0x1000)
    Jump("loc_B5F2")

    label("loc_B58B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B5AF")
    ClearChrFlags(0x104, 0x40)
    ClearChrFlags(0x104, 0x20)
    ClearChrFlags(0x104, 0x1000)
    Jump("loc_B5F2")

    label("loc_B5AF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B5D3")
    ClearChrFlags(0x109, 0x40)
    ClearChrFlags(0x109, 0x20)
    ClearChrFlags(0x109, 0x1000)
    Jump("loc_B5F2")

    label("loc_B5D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B5F2")
    ClearChrFlags(0x105, 0x40)
    ClearChrFlags(0x105, 0x20)
    ClearChrFlags(0x105, 0x1000)

    label("loc_B5F2")

    StopBGM(0xBB8)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("e4800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_45_8C8B end

    def Function_46_B605(): pass

    label("Function_46_B605")

    OP_95(0xFE, 8430, 0, -12130, 4000, 0x0)
    OP_95(0xFE, 25430, 0, -12130, 4000, 0x0)
    Return()

    # Function_46_B605 end

    def Function_47_B62E(): pass

    label("Function_47_B62E")

    Sleep(200)
    OP_95(0xFE, 8430, 0, -12130, 4000, 0x0)
    OP_95(0xFE, 25430, 0, -12130, 4000, 0x0)
    Return()

    # Function_47_B62E end

    def Function_48_B65A(): pass

    label("Function_48_B65A")

    Sleep(800)
    OP_95(0xFE, 8430, 0, -12130, 4000, 0x0)
    OP_95(0xFE, 25430, 0, -12130, 4000, 0x0)
    Return()

    # Function_48_B65A end

    def Function_49_B686(): pass

    label("Function_49_B686")

    OP_95(0xFE, 66190, 6000, -15970, 4000, 0x0)
    OP_95(0xFE, 66190, 6000, -5060, 4000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_49_B686 end

    def Function_50_B6B6(): pass

    label("Function_50_B6B6")

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

    # Function_50_B6B6 end

    def Function_51_B714(): pass

    label("Function_51_B714")

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

    # Function_51_B714 end

    def Function_52_B772(): pass

    label("Function_52_B772")

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

    # Function_52_B772 end

    def Function_53_B7CE(): pass

    label("Function_53_B7CE")


    def lambda_B7D3():
        OP_95(0xFE, 210000, -1550, 8100, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B7D3)
    Sleep(500)

    def lambda_B7F0():
        OP_95(0xFE, 210000, -1550, 8100, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B7F0)
    Sleep(700)

    def lambda_B80D():
        OP_95(0xFE, 210000, -1550, 8100, 8500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B80D)
    Sleep(800)

    def lambda_B82A():
        OP_95(0xFE, 210000, -1550, 8100, 9500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B82A)
    Return()

    # Function_53_B7CE end

    def Function_54_B840(): pass

    label("Function_54_B840")

    SetChrPos(0x8, 70000, -1550, 8100, 0)

    def lambda_B856():
        OP_95(0xFE, 210000, -1550, 8100, 9500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B856)
    Return()

    # Function_54_B840 end

    def Function_55_B86C(): pass

    label("Function_55_B86C")

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

    # Function_55_B86C end

    def Function_56_B96A(): pass

    label("Function_56_B96A")

    Sleep(11000)
    Sound(143, 0, 50, 0)
    Return()

    # Function_56_B96A end

    SaveToFile()

Try(main)

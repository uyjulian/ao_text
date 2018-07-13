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
        "Function_3_3375",         # 03, 3
        "Function_4_33B9",         # 04, 4
        "Function_5_340F",         # 05, 5
        "Function_6_3465",         # 06, 6
        "Function_7_34C0",         # 07, 7
        "Function_8_3513",         # 08, 8
        "Function_9_355F",         # 09, 9
        "Function_10_35B3",        # 0A, 10
        "Function_11_35E3",        # 0B, 11
        "Function_12_3D4E",        # 0C, 12
        "Function_13_3D9A",        # 0D, 13
        "Function_14_3DD6",        # 0E, 14
        "Function_15_3DED",        # 0F, 15
        "Function_16_3E29",        # 10, 16
        "Function_17_3E40",        # 11, 17
        "Function_18_3E7C",        # 12, 18
        "Function_19_3E93",        # 13, 19
        "Function_20_3EE0",        # 14, 20
        "Function_21_3EF0",        # 15, 21
        "Function_22_3F2C",        # 16, 22
        "Function_23_3F3C",        # 17, 23
        "Function_24_3F53",        # 18, 24
        "Function_25_3F8F",        # 19, 25
        "Function_26_3FA6",        # 1A, 26
        "Function_27_3FE2",        # 1B, 27
        "Function_28_3FF9",        # 1C, 28
        "Function_29_4035",        # 1D, 29
        "Function_30_404C",        # 1E, 30
        "Function_31_4099",        # 1F, 31
        "Function_32_40A9",        # 20, 32
        "Function_33_40E5",        # 21, 33
        "Function_34_40F5",        # 22, 34
        "Function_35_4111",        # 23, 35
        "Function_36_4128",        # 24, 36
        "Function_37_416F",        # 25, 37
        "Function_38_41B6",        # 26, 38
        "Function_39_6CBA",        # 27, 39
        "Function_40_6CEB",        # 28, 40
        "Function_41_7279",        # 29, 41
        "Function_42_8584",        # 2A, 42
        "Function_43_8EB1",        # 2B, 43
        "Function_44_90FD",        # 2C, 44
        "Function_45_913A",        # 2D, 45
        "Function_46_BB95",        # 2E, 46
        "Function_47_BBBE",        # 2F, 47
        "Function_48_BBEA",        # 30, 48
        "Function_49_BC16",        # 31, 49
        "Function_50_BC46",        # 32, 50
        "Function_51_BCA4",        # 33, 51
        "Function_52_BD02",        # 34, 52
        "Function_53_BD5E",        # 35, 53
        "Function_54_BDD0",        # 36, 54
        "Function_55_BDFC",        # 37, 55
        "Function_56_BEFA",        # 38, 56
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
            "#12P#00002F#3316V#30WKeA...!\x01",
            "Have you come to pick me up?\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xCF4)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)

    def lambda_1073():
        OP_96(0xFE, 0xB54, 0x0, 0xFFFFC3D8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1073)
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
            "#3596V#30WYes!\x01",
            "Because I heard you'd\x01",
            "be coming home today!\x02\x03",
            "#3597VAre you okay!?\x01",
            "Aren't you hurt anywhere!?\x02",
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
            "#01121F#5PEhehe...\x01",
            "Welcome back too, Noｱl!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10109FAhaha...\x01",
            "I'm back, KeA.\x02",
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
        "Girl's Voice",
        "#2708V#12A#30WBig siiiiiiiiis!!\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    ClearChrFlags(0xB, 0x8)

    def lambda_12D5():
        OP_95(0xFE, 4350, 0, -16650, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_12D5)
    Sleep(300)

    def lambda_12F2():

        label("loc_12F2")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_12F2")

    QueueWorkItem2(0xA, 2, lambda_12F2)

    def lambda_1304():

        label("loc_1304")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_1304")

    QueueWorkItem2(0x101, 2, lambda_1304)
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

    def lambda_1350():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1350)
    Sound(811, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x109,
        "#12P#10111F#3513V#30WW-What, Fran!?\x02",
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
            "#2709V#30WUeeeeh...!\x01",
            "I'm glad you're all in\x01",
            "one piece, big sis!\x02\x03",
            "#2710VWelcome back!\x01",
            "You aren't hurt, right!?\x02",
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
            "#12P#10102FNo, as you can see I'm fine.\x02\x03",
            "#10106FAnd by the way, only a few days have passed,\x01",
            "you shouldn't exaggerating this much...\x02",
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

    def lambda_1549():
        OP_96(0xFE, 0xFA0, 0x0, 0xFFFFBEC4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1549)
    WaitChrThread(0xB, 1)
    Sleep(150)

    ChrTalk(
        0xB,
        (
            "#01903F#5PYou don't get it, big sis!\x01",
            "It's not a matter of time.\x02",
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
        "#00012FHa ha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10112FSomehow now it's sank\x01",
            "in that we came back...\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_1710")

    NpcTalk(
        0x102,
        "Girl's Voice",
        "#3385VLloyd#30W......welcome back.\x02",
    )

    CloseMessageWindow()
    OP_24(0xD39)
    OP_C9(0x1, 0x80000000)
    Jump("loc_176B")

    label("loc_1710")


    NpcTalk(
        0x102,
        "Girl's Voice",
        (
            "#3386V#30W*giggle*......\x01",
            "Thank you for your hard work, you two.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xD3A)
    OP_C9(0x1, 0x80000000)

    label("loc_176B")

    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_17A0():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_17A0)
    Sleep(50)

    def lambda_17B0():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_17B0)
    Sleep(50)

    def lambda_17C0():
        OP_93(0xA, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_17C0)
    Sleep(50)

    def lambda_17D0():
        OP_93(0xB, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_17D0)
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

    def lambda_182E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_182E)

    def lambda_183F():
        OP_96(0xFE, 0xFFFFE124, 0x258, 0xFFFFC374, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_183F)
    Sleep(100)

    def lambda_185C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_185C)

    def lambda_186D():
        OP_96(0xFE, 0xFFFFDE68, 0x258, 0xFFFFBF8C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_186D)
    WaitChrThread(0x102, 1)
    WaitChrThread(0xC, 1)
    OP_6F(0x79)
    Sleep(300)

    def lambda_1894():
        OP_96(0xFE, 0x6A4, 0x0, 0xFFFFC374, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1894)
    Sleep(100)

    def lambda_18B1():
        OP_96(0xFE, 0x3E8, 0x0, 0xFFFFBF8C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_18B1)
    Sleep(2500)
    Fade(500)
    OP_68(2600, 900, -15600, 0)
    MoveCamera(325, 23, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetCameraDistance(14000, 1500)

    def lambda_190A():
        OP_96(0xFE, 0x1004, 0x0, 0xFFFFC5CC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_190A)
    Sleep(50)

    def lambda_1927():
        OP_96(0xFE, 0x1130, 0x0, 0xFFFFBBA4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1927)
    WaitChrThread(0xA, 1)

    def lambda_1945():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1945)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x101,
        (
            "#12P#00002FElie!\x01",
            "Are you already back!?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_1F63")
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
            "#3387V#30WY-Yes, I came back just yesterday.\x02\x03",
            "#3389VI also finished helping\x01",
            "grandfather, so I can be\x01",
            "reinstated from today too.\x02",
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
            "#12P#00002F#30WI see...\x01",
            "............\x02",
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
            "#01105F#11PHey, hey.\x02\x03",
            "Lloyd, Elie, why're you\x01",
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

    def lambda_1B86():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1B86)

    def lambda_1B93():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1B93)
    TurnDirection(0x101, 0xA, 700)

    ChrTalk(
        0x101,
        (
            "#6P#00011FN-No!\x01",
            "It's nothing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#5PT-That's right.\x01",
            "Because we didn't see each other for some time,\x01",
            "it unintentionally felt nostalgic and so on.\x02",
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
            "#6P#01902F(Eeeh...\x01",
            "They're so lovey dovey.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10114F(Hey, as I thought, these two\x01",
            "have that kind of relationship...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#01900F(According to my diagnosis, it doesn't\x01",
            "look like a definite relationship.)\x02\x03",
            "#01909F(Ehehe, if you're interested,\x01",
            "you could still have a chance?)\x02",
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
        "#11P#10111F(I-I wouldn't do such a...!)\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00109F#5POh, Miss Noｱl too, thank you for your hard work.\x02\x03",
            "#00102FHas anything dangerous happened?\x01",
            "Occasionally, Lloyd does some\x01",
            "reckless things...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)
    Sleep(150)

    ChrTalk(
        0x109,
        (
            "#12P#10112FN-No, no.\x01",
            "Miss Elie too, thank you for your hard work.\x02\x03",
            "#10100FIf I remember correctly you were touring\x01",
            "all countries accompanying Chairman\x01",
            "MacDowell, right?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1F46():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F46)
    Sleep(50)

    def lambda_1F56():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1F56)
    Jump("loc_2122")

    label("loc_1F63")

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
            "#3388V#30WYes, I just came back yesterday.\x02\x03",
            "#3389VI also finished helping\x01",
            "grandfather, so I can be\x01",
            "reinstated from today too.\x02",
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
            "#12P#10109FThank you for your hard work, Miss Elie.\x02\x03",
            "#10100FIf I remember correctly you were\x01",
            "touring all countries accompanying\x01",
            "Chairman MacDowell, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2122")


    ChrTalk(
        0x102,
        (
            "#00104F#5PYes, although it's not that\x01",
            "I gave him a great help.\x02\x03",
            "#00100FHowever, I could get many kinds\x01",
            "of interesting information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FI see...\x01",
            "Let me hear about them later.\x02\x03",
            "#00006FAnyway, now there would be\x01",
            "nothing better if Tio and\x01",
            "Randy came back too...\x02",
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
            "Well, those two are probably going\x01",
            "to come back by this month.\x02\x03",
            "More importantly, Lloyd.\x01",
            "Were you able to settle\x01",
            "things properly?\x02",
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
            "#12P#00003F......Yes.\x01",
            "We arrested both of them safely.\x02\x03",
            "#00001FMr. Dudley and Mr. Arios\x01",
            "are escorting them to prison.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01003F#5PI see...\x02\x03",
            "#01002FWell, with this it can be said that the incident\x01",
            "about the Cult has been settled for the time being.\x02\x03",
            "I think you know this, but...\x01",
            "See that you change your way\x01",
            "of thinking little by little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, I intend to do that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01002F#5PAs for Noｱl, it's nice to\x01",
            "meet you officially.\x02\x03",
            "You can start from today, right?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2519():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2519)
    Sleep(100)

    def lambda_2529():
        TurnDirection(0xB, 0x109, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_2529)
    Sleep(100)

    def lambda_2539():
        TurnDirection(0xA, 0x109, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_2539)
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
            "#12P#10103FNoｱl Seeker!\x02\x03",
            "#10101FStarting today, it will be my honor to be\x01",
            "transferred to the Special Support Section!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11P#01105FHoeee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#01909FEhehe...\x01",
            "Now big sis is your colleague too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01006F#5PAah, you can be less\x01",
            "formal, I don't mind.\x02\x03",
            "#01000FYou've probably heard it from Sonya too,\x01",
            "but we have our own pace.\x02\x03",
            "For the time, you'll do away\x01",
            "with the military style hierarchy.\x02",
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
        "#12P#10105FI-I will try.\x02",
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
            "#2904V#30WHu hu...\x01",
            "It looks like you're all here.\x02",
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

    def lambda_27F7():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_27F7)
    Sleep(50)

    def lambda_2807():
        TurnDirection(0xA, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_2807)
    Sleep(50)

    def lambda_2817():
        TurnDirection(0xB, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_2817)
    Sleep(50)

    def lambda_2827():
        TurnDirection(0xC, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_2827)
    Sleep(50)

    def lambda_2837():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2837)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x102, 0)

    def lambda_285B():

        label("loc_285B")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_285B")

    QueueWorkItem2(0x102, 2, lambda_285B)

    def lambda_286D():

        label("loc_286D")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_286D")

    QueueWorkItem2(0xC, 2, lambda_286D)

    def lambda_287F():

        label("loc_287F")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_287F")

    QueueWorkItem2(0xB, 2, lambda_287F)
    Sleep(500)

    def lambda_2894():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2894)

    def lambda_28A5():
        OP_95(0xFE, -3000, 0, -16000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_28A5)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        "#10100FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWazy......!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01110FOh, it's Wazy!\x02",
    )

    CloseMessageWindow()

    def lambda_290A():
        OP_95(0xFE, 1700, 0, -15500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_290A)
    Sleep(800)
    Fade(500)
    OP_68(2600, 900, -15600, 0)
    MoveCamera(325, 23, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    Sleep(500)

    def lambda_295D():
        OP_96(0xFE, 0x802, 0x0, 0xFFFFC856, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_295D)
    WaitChrThread(0x105, 1)

    def lambda_297B():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_297B)
    WaitChrThread(0x102, 1)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x105,
        (
            "#10304F#2905V#5P#30WHu hu, thank you for all your hard work.\x02\x03",
            "#10300F#2906VJudging by the look of things,\x01",
            "it seems it went well?\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xB5A)

    ChrTalk(
        0x101,
        (
            "#12P#00000FYeah, because of your intel, we\x01",
            "somehow managed to get in touch \x01",
            "with an informant at Altair City...\x02\x03",
            "#00006F...Where in the world did\x01",
            "you get such intel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309F#5PHu hu...it needs a thief to catch a thief, they say.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(3150, 900, -15230, 1500)

    def lambda_2B24():
        OP_95(0xFE, 3150, 0, -15400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2B24)
    WaitChrThread(0x105, 1)
    EndChrThread(0x102, 0x2)
    EndChrThread(0xC, 0x2)

    def lambda_2B4A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2B4A)
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
            "#2901V#30W──I did it just for you.\x01",
            "I'm happy if I was useful.\x02",
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
        "#6P#01905FWow wow...!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#12P#00011FHey, you're too close!\x02\x03",
            "Why're you edging up!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10309FAhaha, what a silly question.\x02\x03",
            "It's because your reaction would\x01",
            "have been funny, what else?\x02",
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
        "#5P#00111FWazy, listen here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10112FAhaha...\x01",
            "(A really puzzling kid.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#01109F#11PEheheh.\x01",
            "Somehow it seems fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#01906FHow nice the Special Support Section is...\x02\x03",
            "There're big sis, and KeA, and you\x01",
            "can see a Mr. Lloyd in trouble too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 500)

    ChrTalk(
        0x101,
        (
            "#00012F#11PNo!\x01",
            "Being envied is the problem!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01006F#5POh boy...\x01",
            "Leave the jokes at that.\x02",
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

    def lambda_2F4C():
        TurnDirection(0x101, 0xC, 0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2F4C)
    Sleep(0)

    def lambda_2F5C():
        TurnDirection(0x109, 0xC, 0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2F5C)
    Sleep(0)

    def lambda_2F6C():
        TurnDirection(0x102, 0xC, 0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2F6C)
    Sleep(0)

    def lambda_2F7C():
        TurnDirection(0xB, 0xC, 0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_2F7C)
    Sleep(0)

    def lambda_2F8C():
        TurnDirection(0xA, 0xC, 0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_2F8C)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xA, 0)

    def lambda_2FB0():
        OP_96(0xFE, 0x9C4, 0x0, 0xFFFFC504, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2FB0)
    WaitChrThread(0x105, 1)
    TurnDirection(0x105, 0xC, 500)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#6P#01003F──At any rate.\x01",
            "These are the starting members of\x01",
            "the renewed Special Support Section.\x02\x03",
            "#01000FLloyd Bannings,\x01",
            "as the leader.\x02",
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
            "#6P#01000FElie MacDowell,\x01",
            "as leader assistant.\x02",
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
            "#6P#01003FNoｱl Seeker,\x01",
            "from the CGF.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10102F#3514V#11P#30WYes sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#01000FWazy Hemisphere, as a\x01",
            "special associate member.\x02",
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
            "#6P#01004FToday, at 18:30 I declare the \x01",
            "Special Support Section restart.\x02\x03",
            "#01002FBecause funnier jobs than\x01",
            "before are going to drop in,\x01",
            "you can look forward to them──\x02",
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

    def Function_3_3375(): pass

    label("Function_3_3375")

    Sound(452, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x3D, 0x168, 0x0, 0x0)
    Sleep(2000)

    def lambda_3393():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3393)
    OP_79(0x1)
    Sound(143, 0, 100, 0)
    OP_82(0x96, 0x96, 0xBB8, 0x1F4)
    Sleep(500)
    Return()

    # Function_3_3375 end

    def Function_4_33B9(): pass

    label("Function_4_33B9")

    SetChrPos(0xFE, 22700, 0, -9700, 180)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_33DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_33DA)
    OP_95(0xFE, 22700, 0, -12800, 2000, 0x0)
    OP_95(0xFE, 7300, 0, -12800, 2000, 0x0)
    Return()

    # Function_4_33B9 end

    def Function_5_340F(): pass

    label("Function_5_340F")

    SetChrPos(0xFE, 22700, 0, -9700, 180)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3430():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3430)
    OP_95(0xFE, 22700, 0, -12800, 2000, 0x0)
    OP_95(0xFE, 8500, 0, -12800, 2000, 0x0)
    Return()

    # Function_5_340F end

    def Function_6_3465(): pass

    label("Function_6_3465")

    SetChrPos(0xFE, 19700, 100, -9700, 180)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3486():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3486)
    OP_95(0xFE, 19700, 0, -12800, 2000, 0x0)
    OP_95(0xFE, 0, 0, -12800, 2000, 0x0)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_6_3465 end

    def Function_7_34C0(): pass

    label("Function_7_34C0")

    ClearScenarioFlags(0x0, 0)

    def lambda_34C8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_34C8)
    OP_95(0xFE, 22700, 0, -13700, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_AD(0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, 0, 0, -13700, 2000, 0x0)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_7_34C0 end

    def Function_8_3513(): pass

    label("Function_8_3513")


    def lambda_3518():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3518)
    OP_95(0xFE, 22700, 0, -12700, 2000, 0x0)
    Sleep(500)
    SetScenarioFlags(0x0, 0)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, 0, 0, -12700, 2000, 0x0)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_8_3513 end

    def Function_9_355F(): pass

    label("Function_9_355F")


    def lambda_3564():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3564)
    OP_95(0xFE, 32500, 0, -12700, 4000, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0xFE, 0, 0, -12700, 4000, 0x0)
    OP_64(0xFE)
    SetChrFlags(0xFE, 0x8)
    Return()

    # Function_9_355F end

    def Function_10_35B3(): pass

    label("Function_10_35B3")

    OP_95(0xFE, 7500, 0, -13700, 2000, 0x0)
    OP_95(0xFE, 4800, 0, -16700, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_10_35B3 end

    def Function_11_35E3(): pass

    label("Function_11_35E3")

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

    # Function_11_35E3 end

    def Function_12_3D4E(): pass

    label("Function_12_3D4E")

    Sound(963, 0, 100, 0)
    Sound(825, 2, 50, 0)
    OP_71(0x3, 0x5A, 0x168, 0x0, 0x8)
    Sleep(2000)

    def lambda_3D6E():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3D6E)
    OP_79(0x3)
    OP_82(0x96, 0x96, 0xBB8, 0x1F4)
    Sound(143, 0, 100, 0)
    StopSound(825, 500, 50)
    Sleep(500)
    Return()

    # Function_12_3D4E end

    def Function_13_3D9A(): pass

    label("Function_13_3D9A")


    def lambda_3D9F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3D9F)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 40000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_13_3D9A end

    def Function_14_3DD6(): pass

    label("Function_14_3DD6")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_14_3DD6 end

    def Function_15_3DED(): pass

    label("Function_15_3DED")


    def lambda_3DF2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3DF2)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 39000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_15_3DED end

    def Function_16_3E29(): pass

    label("Function_16_3E29")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_16_3E29 end

    def Function_17_3E40(): pass

    label("Function_17_3E40")


    def lambda_3E45():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3E45)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 38000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_17_3E40 end

    def Function_18_3E7C(): pass

    label("Function_18_3E7C")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_18_3E7C end

    def Function_19_3E93(): pass

    label("Function_19_3E93")


    def lambda_3E98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3E98)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_68(35000, 700, 3300, 2000)
    OP_95(0xFE, 35000, 0, 3300, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_19_3E93 end

    def Function_20_3EE0(): pass

    label("Function_20_3EE0")

    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_20_3EE0 end

    def Function_21_3EF0(): pass

    label("Function_21_3EF0")


    def lambda_3EF5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3EF5)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 35750, 0, 2500, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_21_3EF0 end

    def Function_22_3F2C(): pass

    label("Function_22_3F2C")

    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_22_3F2C end

    def Function_23_3F3C(): pass

    label("Function_23_3F3C")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_23_3F3C end

    def Function_24_3F53(): pass

    label("Function_24_3F53")


    def lambda_3F58():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3F58)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 27000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_24_3F53 end

    def Function_25_3F8F(): pass

    label("Function_25_3F8F")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_25_3F8F end

    def Function_26_3FA6(): pass

    label("Function_26_3FA6")


    def lambda_3FAB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3FAB)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 26000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_26_3FA6 end

    def Function_27_3FE2(): pass

    label("Function_27_3FE2")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_27_3FE2 end

    def Function_28_3FF9(): pass

    label("Function_28_3FF9")


    def lambda_3FFE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3FFE)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 25000, 0, 3800, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_28_3FF9 end

    def Function_29_4035(): pass

    label("Function_29_4035")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_29_4035 end

    def Function_30_404C(): pass

    label("Function_30_404C")


    def lambda_4051():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4051)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_68(22000, 700, 3300, 2000)
    OP_95(0xFE, 22000, 0, 3300, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_30_404C end

    def Function_31_4099(): pass

    label("Function_31_4099")

    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_31_4099 end

    def Function_32_40A9(): pass

    label("Function_32_40A9")


    def lambda_40AE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_40AE)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0xFE, 22750, 0, 2500, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_32_40A9 end

    def Function_33_40E5(): pass

    label("Function_33_40E5")

    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_33_40E5 end

    def Function_34_40F5(): pass

    label("Function_34_40F5")

    OP_95(0xFE, 20500, 0, 3300, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_34_40F5 end

    def Function_35_4111(): pass

    label("Function_35_4111")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
    Return()

    # Function_35_4111 end

    def Function_36_4128(): pass

    label("Function_36_4128")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_416E")
    OP_63(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x11)
    Sleep(500)
    OP_63(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xD)
    Sleep(500)
    Jump("Function_36_4128")

    label("loc_416E")

    Return()

    # Function_36_4128 end

    def Function_37_416F(): pass

    label("Function_37_416F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41B5")
    OP_63(0x12, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x12)
    Sleep(500)
    OP_63(0xF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xF)
    Sleep(500)
    Jump("Function_37_416F")

    label("loc_41B5")

    Return()

    # Function_37_416F end

    def Function_38_41B6(): pass

    label("Function_38_41B6")

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

    def lambda_428F():
        OP_95(0x20, 1000, 600, 40, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_428F)
    Sleep(800)

    def lambda_42AC():
        OP_95(0x101, 200, 0, 700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_42AC)
    Sleep(200)

    def lambda_42C9():
        OP_95(0x102, 300, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_42C9)
    Sleep(300)

    def lambda_42E6():
        OP_95(0x103, -1000, 0, -950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_42E6)
    Sleep(100)

    def lambda_4303():
        OP_95(0x104, -1100, 0, 1100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4303)
    Sleep(200)

    def lambda_4320():
        OP_95(0x109, -2500, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4320)
    Sleep(50)

    def lambda_433D():
        OP_95(0x105, -2400, 0, 700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_433D)
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

    def lambda_4432():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4432)
    Sleep(50)

    def lambda_4442():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4442)
    Sleep(50)

    def lambda_4452():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4452)
    Sleep(10)

    def lambda_4462():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4462)
    Sleep(30)

    def lambda_4472():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4472)
    Sleep(10)

    def lambda_4482():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4482)
    Sleep(10)

    def lambda_4492():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_4492)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x20, 2)

    ChrTalk(
        0x101,
        "#00005FThat's...\x02",
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
            "#00100FIt's the "Eisengraf", a train of the\x01",
            "Imperial government for exclusive use.\x02\x03",
            "#00103FIts magnificent exterior...\x01",
            "It's like it symbolizes the Empire.\x02",
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
            "#10103FIndeed...\x01",
            "It truly feels majestic.\x02",
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
            "#00300FThat "Blood and Iron Chancellor"\x01",
            "entered Crossbell with that thing.\x02\x03",
            "#00306FIts impact was indeed big and the\x01",
            "common talk is that people felt\x01",
            "nice for how much it stood out.\x02",
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
            "#10300FYeah, it also seems that\x01",
            "its cost is enormous.\x02",
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
            "#00203F...It seems that what is amazing\x01",
            "is not just its appearance.\x02\x03",
            "#00200FIt appears that that train boast\x01",
            "the highest speed among the\x01",
            "current orbal trains.\x02\x03",
            "Although, since the precise information\x01",
            "weren't disclosed to the public, I can't\x01",
            "say it for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FI-Is that so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FAs expected from the Erebonian Empire which\x01",
            "has a railway net spreaded on the entire nation...\x02\x03",
            "#00101FIn regards of the railroad field itself,\x01",
            "they have no equals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FYeah, I was forced to realize that once again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "...*cough*.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "So, I would like to talk about the job,\x01",
            "have you done your preparations?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4A0B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4A0B)
    Sleep(50)

    def lambda_4A1B():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4A1B)
    Sleep(30)

    def lambda_4A2B():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4A2B)
    Sleep(20)

    def lambda_4A3B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4A3B)
    Sleep(40)

    def lambda_4A4B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4A4B)
    Sleep(20)

    def lambda_4A5B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4A5B)
    WaitChrThread(0x105, 2)

    ChrTalk(
        0x101,
        (
            "#00005FI-I'm sorry.\x01",
            "We were astonished by its majestic appearance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, of course we're fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "Hm, very well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Well then, like I said before,\x01",
            "what I want to ask you is a hand with\x01",
            "the train on-the-spot inspection duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Concretely, to check all passengers' entry\x01",
            "written applications and hand luggages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "After that, to take part in the safety\x01",
            "check of the train itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FUhhm, what do you intend with\x01",
            "the train safety check?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Oh, I will help you with that.\x01",
            "At any rate, I want you to follow the orders\x01",
            "and to perform all sort of inspection work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Hm, there're six\x01",
            "of you all together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Then, three groups of two people each.\x01",
            "I want two groups to take part in the on-the-spot\x01",
            "cabins inspection and one to help me.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4F08")

    ChrTalk(
        0x101,
        (
            "#00005FOn-the-spot inspection in groups of two?\x01",
            "I remember having it done alone before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, at least when we helped\x01",
            "before it was like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "Oh, you have experience with this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "It's true that it's a duty that\x01",
            "we always perform alone, but the\x01",
            "warning level has being raised now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "In order to have way stricter checks,\x01",
            "this time circumstance requires this attitude.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_501B")

    label("loc_4F08")


    ChrTalk(
        0x101,
        (
            "#00005FOn-the-spot inspection in groups of two...\x01",
            "Has it always been done like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "No, it's a duty that\x01",
            "we always perform alone, but the\x01",
            "warning level has being raised now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "In order to have way stricter checks,\x01",
            "this time circumstance requires this attitude.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_501B")


    ChrTalk(
        0x101,
        "#00000FI see, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Then, can I ask you to split\x01",
            "in three groups immediately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "You can even use rock-scissors-paper if you like.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FR-Rock-scissors-paper?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Well, honestly speaking, it's not a job\x01",
            "requiring that much of individual attitude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "I personally would like to start this\x01",
            "job quickly and it would be good for you\x01",
            "to finish it expeditiously too, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, well, that being the case,\x01",
            "we don't mind it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, then it's settled.\x01",
            "Seems fun, so why not?♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FHowever, how are we going\x01",
            "to decide concretely?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Oh, then, what about\x01",
            "rules like these?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "In rock-scissors-paper you all stick out your\x01",
            "hands at once, so if only two play the same\x01",
            "hand, those will go to form a "group".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "What remains is to repeat that until it's settled.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FEhhm...\x01",
            "What can I say, aren't you used to it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "Ha ha, more or less.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Actually, in my time as a Republican\x01",
            "Inspector we decided how to divide work\x01",
            "like this occasionally, to take a breather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "It's a flexible concept that all of the\x01",
            "straight-laced Imperial Inspectors lack.\x02",
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
            "#00106FI don't know if it's a flexible\x01",
            "concept or not, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FAt any rate, it is probably\x01",
            "a nationality difference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FHa ha, could be.\x02\x03",
            "Well, anyhow, let's\x01",
            "give it a spin now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, let's do that.\x02",
    )

    CloseMessageWindow()

    def lambda_561A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_561A)
    Sleep(10)

    def lambda_562A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_562A)
    Sleep(10)

    def lambda_563A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_563A)
    Sleep(10)

    def lambda_564A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_564A)
    Sleep(30)

    def lambda_565A():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_565A)
    Sleep(10)

    def lambda_566A():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_566A)
    WaitChrThread(0x105, 2)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00003FAlright, everyone.\x01",
            "Let's do it with a "ready, set, go!".\x02",
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
            "Play Rock\x01",          # 0
            "Play Scissors\x01",      # 1
            "Play Paper\x01",         # 2
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
        "#4S#11AReady, set...\x02",
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

    def lambda_5789():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5789)

    def lambda_579E():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_579E)

    def lambda_57B3():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_57B3)

    def lambda_57C8():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_57C8)

    def lambda_57DD():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_57DD)

    def lambda_57F2():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_57F2)
    Sound(802, 0, 100, 0)
    SetChrName("All")

    AnonymousTalk(
        0xFF,
        "#4S#11A...go!\x02",
    )

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F40")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_586C():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_586C)

    def lambda_5881():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5881)

    def lambda_5896():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5896)

    def lambda_58AB():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_58AB)

    def lambda_58C0():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_58C0)

    def lambda_58D5():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_58D5)
    WaitChrThread(0x101, 1)

    def lambda_58EE():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_58EE)
    Sleep(50)

    def lambda_58FE():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_58FE)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00100F*gigge*, only Tio and\x01",
            "I played paper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThat means Miss Elie\x01",
            "and I will for a group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FSo, what remains are three rocks and one paper?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FIn this case, the remaining\x01",
            "four will do it again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, then let's continue!\x02",
    )

    CloseMessageWindow()

    def lambda_5A1B():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5A1B)
    Sleep(50)

    def lambda_5A2B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5A2B)
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
            "Play Rock\x01",          # 0
            "Play Scissors\x01",      # 1
            "Play Paper\x01",         # 2
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
        "#4S#11AReady, set...\x02",
    )

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x101, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)

    def lambda_5AED():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5AED)

    def lambda_5B02():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5B02)

    def lambda_5B17():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5B17)

    def lambda_5B2C():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5B2C)
    Sound(802, 0, 100, 0)
    SetChrName("All")

    AnonymousTalk(
        0xFF,
        "#4S#11A...go!\x02",
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

    def lambda_5BBB():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5BBB)

    def lambda_5BD0():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5BD0)

    def lambda_5BE5():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5BE5)

    def lambda_5BFA():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5BFA)
    WaitChrThread(0x101, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D28")

    def lambda_5C22():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C22)
    Sleep(50)

    def lambda_5C32():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5C32)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00005FNoｱl and I played rock, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FUh uh, Mr. Lloyd, please\x01",
            "take good care of me.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5CA5():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5CA5)
    Sleep(50)

    def lambda_5CB5():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5CB5)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00300FThen, me and Wazy\x01",
            "will form a group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHu hu, it's nice working with you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 4)
    Jump("loc_5F3B")

    label("loc_5D28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E3B")

    def lambda_5D3C():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D3C)
    Sleep(50)

    def lambda_5D4C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5D4C)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00005FWazy and I played scissors, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHu hu, it's nice working with you.\x02",
    )

    CloseMessageWindow()

    def lambda_5DB7():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5DB7)
    Sleep(50)

    def lambda_5DC7():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5DC7)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00300FThen, me and Noｱl\x01",
            "will form a group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FRight, please take good care of me.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 5)
    Jump("loc_5F3B")

    label("loc_5E3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F3B")

    def lambda_5E4F():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E4F)
    Sleep(50)

    def lambda_5E5F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5E5F)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00005FRandy and I played paper, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FYeah, nice to work with ya.\x02",
    )

    CloseMessageWindow()

    def lambda_5EC1():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5EC1)
    Sleep(50)

    def lambda_5ED1():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5ED1)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10100FAnd so, Wazy and\x01",
            "I will form a group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FRight, nice working with you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 3)

    label("loc_5F3B")

    Jump("loc_6810")

    label("loc_5F40")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6662")
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5F7B():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F7B)

    def lambda_5F90():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5F90)

    def lambda_5FA5():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5FA5)

    def lambda_5FBA():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5FBA)

    def lambda_5FCF():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5FCF)

    def lambda_5FE4():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5FE4)
    WaitChrThread(0x101, 1)

    def lambda_5FFD():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5FFD)
    Sleep(50)

    def lambda_600D():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_600D)
    Sleep(300)

    ChrTalk(
        0x104,
        "#00305FHm, only me and Noｱl played rock, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FAnd so, senior Randy \x01",
            "and I will form a group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FSo, what remains are three scissors and one paper?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIn this case, the remaining\x01",
            "four will do it again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, then let's continue!\x02",
    )

    CloseMessageWindow()

    def lambda_6130():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6130)
    Sleep(50)

    def lambda_6140():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6140)
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
            "Play Rock\x01",          # 0
            "Play Scissors\x01",      # 1
            "Play Paper\x01",         # 2
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
        "#4S#11AReady, set...\x02",
    )

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    EndChrThread(0x105, 0x3)

    def lambda_6202():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6202)

    def lambda_6217():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6217)

    def lambda_622C():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_622C)

    def lambda_6241():
        OP_9B(0x1, 0xFE, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6241)
    Sound(802, 0, 100, 0)
    SetChrName("All")

    AnonymousTalk(
        0xFF,
        "#4S#11A...go!\x02",
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

    def lambda_62D0():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62D0)

    def lambda_62E5():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_62E5)

    def lambda_62FA():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_62FA)

    def lambda_630F():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_630F)
    WaitChrThread(0x101, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6433")

    def lambda_6337():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6337)
    Sleep(50)

    def lambda_6347():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6347)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00005FTio and I played rock.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FMr. Lloyd, it is nice\x01",
            "to be working with you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_63B4():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_63B4)
    Sleep(50)

    def lambda_63C4():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_63C4)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00100FAnd so, Wazy and\x01",
            "I will form a group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FRight, nice to work with you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 2)
    Jump("loc_665D")

    label("loc_6433")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6550")

    def lambda_6447():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6447)
    Sleep(50)

    def lambda_6457():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6457)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00005FWazy and I played scissors, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHu hu, it's nice working with you.\x02",
    )

    CloseMessageWindow()

    def lambda_64C2():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_64C2)
    Sleep(50)

    def lambda_64D2():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_64D2)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00100FAnd so, Tio and I\x01",
            "will form a group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FMiss Elie, it is nice\x01",
            "to be working with you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 5)
    Jump("loc_665D")

    label("loc_6550")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_665D")

    def lambda_6564():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6564)
    Sleep(50)

    def lambda_6574():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6574)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00005FElie and I played paper, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F*giggle*, it's nice to work with you.\x02",
    )

    CloseMessageWindow()

    def lambda_65DF():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_65DF)
    Sleep(50)

    def lambda_65EF():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_65EF)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00200FAnd so, Mr. Wazy and\x01",
            "I will form a group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FRight, nice working with you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 1)

    label("loc_665D")

    Jump("loc_6810")

    label("loc_6662")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6810")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_66EB():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_66EB)

    def lambda_6700():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6700)

    def lambda_6715():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6715)

    def lambda_672A():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_672A)

    def lambda_673F():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_673F)

    def lambda_6754():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6754)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#00005FOh, we splitted perfectly again.\x02\x03",
            "#00000FWazy and I, Elie and Tio, and\x01",
            "Randy and Noｱl are the groups, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHu hu, it's nice working with you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x158, 5)

    label("loc_6810")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 1)), scpexpr(EXPR_END)), "loc_6827")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_687E")

    label("loc_6827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 2)), scpexpr(EXPR_END)), "loc_683E")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_687E")

    label("loc_683E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 3)), scpexpr(EXPR_END)), "loc_6855")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_687E")

    label("loc_6855")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 4)), scpexpr(EXPR_END)), "loc_686C")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_687E")

    label("loc_686C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 5)), scpexpr(EXPR_END)), "loc_687E")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_687E")


    ChrTalk(
        0x20,
        "Hm, it looks like you're settled.\x02",
    )

    CloseMessageWindow()

    def lambda_68AA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_68AA)
    Sleep(10)

    def lambda_68BA():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_68BA)
    Sleep(10)

    def lambda_68CA():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_68CA)
    Sleep(10)

    def lambda_68DA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_68DA)
    Sleep(30)

    def lambda_68EA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_68EA)
    Sleep(10)

    def lambda_68FA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_68FA)
    WaitChrThread(0x105, 2)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00000FHow do we divide work?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 4)), scpexpr(EXPR_END)), "loc_6A53")

    ChrTalk(
        0x20,
        "Let's see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Because I want to move something,\x01",
            "I'd like a male help here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FAnd that means me and Wazy, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FOh boy, from the choice of his words\x01",
            "it looks like we will be worked hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Ha ha, since you're here, I'll\x01",
            "use you as much as possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B27")

    label("loc_6A53")


    ChrTalk(
        0x109,
        (
            "#10105FOh, if you don't mind,\x01",
            "shall I help you?\x02\x03",
            "#10100FSince I have CGF experience\x01",
            "in inspecting railroad vehicles\x01",
            "I think I could be useful to you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x20,
        (
            "I see.\x01",
            "Hm, then can you do it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B27")


    ChrTalk(
        0x20,
        (
            "Alright, then let's start\x01",
            "our duties at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "I leave the cabins\x01",
            "check to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "The announcement has already been made,\x01",
            "so if you say you're "Inspector Assistants",\x01",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 1)), scpexpr(EXPR_END)), "loc_6C61")
    AddParty(0x1, 0xFF, 0xFF)
    Jump("loc_6CAD")

    label("loc_6C61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 2)), scpexpr(EXPR_END)), "loc_6C73")
    AddParty(0x2, 0xFF, 0xFF)
    Jump("loc_6CAD")

    label("loc_6C73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 3)), scpexpr(EXPR_END)), "loc_6C85")
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_6CAD")

    label("loc_6C85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 4)), scpexpr(EXPR_END)), "loc_6C97")
    AddParty(0x8, 0xFF, 0xFF)
    Jump("loc_6CAD")

    label("loc_6C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 5)), scpexpr(EXPR_END)), "loc_6CA9")
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_6CAD")

    label("loc_6CA9")

    AddParty(0x1, 0xFF, 0xFF)

    label("loc_6CAD")

    SetScenarioFlags(0x22, 3)
    NewScene("e0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_38_41B6 end

    def Function_39_6CBA(): pass

    label("Function_39_6CBA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6CEA")

    def lambda_6CCA():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6CCA)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    Jump("Function_39_6CBA")

    label("loc_6CEA")

    Return()

    # Function_39_6CBA end

    def Function_40_6CEB(): pass

    label("Function_40_6CEB")

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
        "Hm, thank you for your hard work, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "It must've been hard, especially\x01",
            "for the ticket theft disturbance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, it wasn't such\x01",
            "a big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIncidentally, it seems that\x01",
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
            "Even for times like this,\x01",
            "we keep information about\x01",
            "the tickets purchasers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "If a theft comes to light because of an inspection,\x01",
            "it is possible to arrest the culprit at the next station.\x02",
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
            "#00300FAnyway, what's happened\x01",
            "to the old man victim?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Oh, since the old man was in a hurry,\x01",
            "we had him buy a ticket again for now.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "When the culprit of the theft is safely\x01",
            "caught, he'll be forced to pay for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHu hu, that old man too was unlucky.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FWell, I'm glad that is seems it'll\x01",
            "be able to be solved immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Yeah, at any rate, \x01",
            "you did well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "You really helped me, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, we too are\x01",
            "glad to hear you\x01",
            "say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIf something comes up again,\x01",
            "please feel free to contact us.\x02",
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
            "Quest [Republican Inspector Assistance]\x07\x00",
            " completed!\x02",
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

    # Function_40_6CEB end

    def Function_41_7279(): pass

    label("Function_41_7279")

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
            "Thank you very much for your hard\x01",
            "work with the theft disturbance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FNo, it wasn't\x01",
            "such a big deal.\x02\x03",
            "#00000FSo, in the end, what will happen to\x01",
            "the youth who committed the theft?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Oh, well, that crime has\x01",
            "been completely ignored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FEhm, what does that mean...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Well, you see, the old man who\x01",
            "should be the victim declared\x01",
            "that no theft took place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "After all, the youth, after entering\x01",
            "the ticket admission platform,\x01",
            "just forgot to buy the ticket...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "That said, even us\x01",
            "can't investigate\x01",
            "further than that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FHah, again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FHmm, could Shing have given\x01",
            "him detailed information?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHu hu, why not?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FIncidentally, what happened\x01",
            "to the trader?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Oh, actually that\x01",
            "was a big catch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "That guy's real identity is that\x01",
            "of a broker who forges tickets.\x02",
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
        "#00100FHowever, what was his reason to be on the train?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Oh, it seems that he was\x01",
            "testing in practice one\x01",
            "of his goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "Honestly, what a daring guy.\x02",
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
            "Well, at any rate you\x01",
            "did really great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "You really helped me, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, we too are\x01",
            "glad to hear you\x01",
            "say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIf something comes up again,\x01",
            "please feel free to contact us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "Yes, then, see you again.\x02",
    )

    CloseMessageWindow()
    OP_93(0x20, 0x2D, 0x1F4)
    OP_95(0x20, 5760, 0, 2550, 2000, 0x0)

    def lambda_791F():
        OP_95(0x20, 24940, 0, 2810, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_791F)
    Sleep(500)
    OP_68(-1190, 1500, -230, 2000)
    MoveCamera(45, 34, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(15430, 2000)
    Sleep(1500)

    def lambda_796D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_796D)
    Sleep(10)

    def lambda_797D():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_797D)
    Sleep(10)

    def lambda_798D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_798D)
    Sleep(10)

    def lambda_799D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_799D)
    Sleep(30)

    def lambda_79AD():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_79AD)
    Sleep(10)

    def lambda_79BD():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_79BD)
    WaitChrThread(0x105, 2)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 1)), scpexpr(EXPR_END)), "loc_7C15")

    ChrTalk(
        0x109,
        (
            "#10100FBe that as it may, it seems that\x01",
            "Shing played a very active part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F*giggle*, who could've thought we'd\x01",
            "meet him again in such a place, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah, and once again I was made acutely\x01",
            "aware of only a portion of his great talent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FJeez, I really wonder how\x01",
            "that brat will grow up to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FHm, I wish I had seen him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, he's a cute little\x01",
            "boy in appearance, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHa ha, indeed.\x02\x03",
            "#00003FAnyhow, the case is closed.\x02\x03",
            "#00000FAfter we have taken a short breath,\x01",
            "let's move towards the next job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84F5")

    label("loc_7C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 2)), scpexpr(EXPR_END)), "loc_7E44")

    ChrTalk(
        0x102,
        (
            "#00100FBe that as it may, it seems that\x01",
            "Shing played a very active part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYes, he is still very young but\x01",
            "I was surprised in many ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, once again I was made acutely\x01",
            "aware of only a portion of his great talent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FJeez, I really wonder how\x01",
            "that brat will grow up to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYes, for real.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, he's a cute little\x01",
            "boy in appearance, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHa ha, indeed.\x02\x03",
            "#00003FAnyhow, the case is closed.\x02\x03",
            "#00000FAfter we have taken a short breath,\x01",
            "let's move towards the next job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84F5")

    label("loc_7E44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 3)), scpexpr(EXPR_END)), "loc_8066")

    ChrTalk(
        0x102,
        (
            "#00100FBe that as it may, it seems that\x01",
            "Shing played a very active part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FYeah, he never changes, I'd say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FRight? Once again I was made acutely\x01",
            "aware of only a portion of his great talent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FWhat can I say, I really wonder\x01",
            "how he will grow up to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FHm, I wish I had seen him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, he's a cute little\x01",
            "boy in appearance, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHa ha, indeed.\x02\x03",
            "#00003FAnyhow, the case is closed.\x02\x03",
            "#00000FAfter we have taken a short breath,\x01",
            "let's move towards the next job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84F5")

    label("loc_8066")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 4)), scpexpr(EXPR_END)), "loc_82AD")

    ChrTalk(
        0x102,
        (
            "#00100FBe that as it may, it seems that\x01",
            "Shing played a very active part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes, though who could've thought we'd\x01",
            "meet him again in such a place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, and once again I was made acutely\x01",
            "aware of only a portion of his great talent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FJeez, I really wonder how\x01",
            "that brat will grow up to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FHm, I wish I had seen him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, he's a cute little\x01",
            "boy in appearance, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHa ha, indeed.\x02\x03",
            "#00003FAnyhow, the case is closed.\x02\x03",
            "#00000FAfter we have taken a short breath,\x01",
            "let's move towards the next job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84F5")

    label("loc_82AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 5)), scpexpr(EXPR_END)), "loc_84F5")

    ChrTalk(
        0x102,
        (
            "#00100FBe that as it may, it seems that\x01",
            "Shing played a very active part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, though who could've thought we'd\x01",
            "meet him again in such a place, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, and once again I was made acutely\x01",
            "aware of only a portion of his great talent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FJeez, I really wonder how\x01",
            "that brat will grow up to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FHm, I wish I had seen him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FHu hu, he's a cute little\x01",
            "boy in appearance, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHa ha, indeed.\x02\x03",
            "#00003FAnyhow, the case is closed.\x02\x03",
            "#00000FAfter we have taken a short breath,\x01",
            "let's move towards the next job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84F5")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Republican Inspector Assistance]\x07\x00",
            " completed!\x02",
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

    # Function_41_7279 end

    def Function_42_8584(): pass

    label("Function_42_8584")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_861D")
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
    Jump("loc_8697")

    label("loc_861D")

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

    label("loc_8697")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_874C")
    OP_68(-1150, 1000, 0, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(16500, 4000)
    Jump("loc_8783")

    label("loc_874C")

    OP_68(-1150, 1000, -16000, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(16500, 4000)

    label("loc_8783")


    def lambda_8788():
        OP_97(0x101, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8788)
    Sleep(50)

    def lambda_87A5():
        OP_97(0x102, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_87A5)
    Sleep(50)

    def lambda_87C2():
        OP_97(0x103, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_87C2)
    Sleep(50)

    def lambda_87DF():
        OP_97(0x104, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_87DF)
    Sleep(50)

    def lambda_87FC():
        OP_97(0xF4, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_87FC)
    Sleep(50)

    def lambda_8819():
        OP_97(0xF5, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_8819)
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
            "#00306F#5PStill, platforms with no persons\x01",
            "are quite the sad thing, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206F...The transcontinental railway trains too seem\x01",
            "to have been stopped like that for a long time.\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8982")

    ChrTalk(
        0x102,
        (
            "#5P#00101F...The No. 3 platform train...\x01",
            "Could it be that way?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89C6")

    label("loc_8982")


    ChrTalk(
        0x102,
        (
            "#5P#00101F...The No. 3 platform train...\x01",
            "Could it be this way?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89C6")

    OP_68(-1150, 1000, -24100, 3000)
    MoveCamera(63, 27, 0, 3000)
    SetCameraDistance(25500, 3000)

    def lambda_89F0():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_89F0)
    Sleep(50)

    def lambda_8A00():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8A00)
    Sleep(50)

    def lambda_8A10():
        OP_93(0xF4, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_8A10)
    Sleep(50)

    def lambda_8A20():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8A20)
    Sleep(50)

    def lambda_8A30():
        OP_93(0xF5, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_8A30)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8AEE")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AB0")

    ChrTalk(
        0x10A,
        (
            "#00601FHmph, it was the 2nd vehicle\x01",
            "from the front.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AE9")

    label("loc_8AB0")


    ChrTalk(
        0x10A,
        (
            "#00601FHmph, it was the 2nd vehicle\x01",
            "from the front.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AE9")

    Jump("loc_8C1B")

    label("loc_8AEE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B86")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B49")

    ChrTalk(
        0x109,
        (
            "#10101FYes, it was the 2nd vehicle\x01",
            "from the front.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B81")

    label("loc_8B49")


    ChrTalk(
        0x109,
        (
            "#10101FYes, it was the 2nd vehicle\x01",
            "from the front.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B81")

    Jump("loc_8C1B")

    label("loc_8B86")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C1B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BE2")

    ChrTalk(
        0x105,
        (
            "#10400FYeah, it was the 2nd vehicle\x01",
            "from the front.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C1B")

    label("loc_8BE2")


    ChrTalk(
        0x105,
        (
            "#10400FYeah, it was the 2nd vehicle\x01",
            "from the front.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C1B")

    OP_57(0x0)
    OP_5A()
    Fade(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C64")
    OP_68(-1150, 1000, 0, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    Jump("loc_8C92")

    label("loc_8C64")

    OP_68(-1150, 1000, -16000, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)

    label("loc_8C92")

    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D00")
    OP_93(0x106, 0x5A, 0x1F4)

    ChrTalk(
        0x106,
        (
            "#6P#10701FIt looks like we can cross from\x01",
            "the connecting bridge over there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DC7")

    label("loc_8D00")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D6D")
    OP_93(0x105, 0x5A, 0x1F4)

    ChrTalk(
        0x105,
        (
            "#6P#10400FIt looks like we can cross from\x01",
            "the connecting bridge over there?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DC7")

    label("loc_8D6D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8DC7")
    OP_93(0x109, 0x5A, 0x1F4)

    ChrTalk(
        0x109,
        (
            "#6P#10101FWe can cross from the\x01",
            "connecting bridge over there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DC7")


    def lambda_8DCC():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8DCC)
    Sleep(50)

    def lambda_8DDC():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8DDC)
    Sleep(50)

    def lambda_8DEC():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8DEC)
    Sleep(50)

    def lambda_8DFC():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8DFC)
    Sleep(50)

    def lambda_8E0C():
        OP_93(0xF4, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_8E0C)
    Sleep(50)

    def lambda_8E1C():
        OP_93(0xF5, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_8E1C)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x101,
        "#5P#00001FAlright...let's go.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E86")
    SetChrPos(0x0, -2500, 0, 0, 90)
    Jump("loc_8E97")

    label("loc_8E86")

    SetChrPos(0x0, -2500, 0, -16000, 90)

    label("loc_8E97")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1A5, 7)
    EventEnd(0x5)
    Return()

    # Function_42_8584 end

    def Function_43_8EB1(): pass

    label("Function_43_8EB1")

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
            "#11P#00008F(Platform No. 3, 2nd vehicle...\x01",
            "Also, the door is not locked.)\x02\x03",
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
            "Open the Door and Enter\x01",      # 0
            "Walk Away\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9025"),
        (1, "loc_90CC"),
        (SWITCH_DEFAULT, "loc_90FC"),
    )


    label("loc_9025")

    Sound(454, 0, 100, 0)
    OP_71(0x0, 0x295, 0x2B2, 0x0, 0x0)
    OP_79(0x0)
    OP_68(10190, 1200, -25980, 4000)

    def lambda_9050():
        OP_95(0xFE, 10000, 0, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9050)
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
    Jump("loc_90FC")

    label("loc_90CC")

    SetChrPos(0x0, 8710, 0, -29420, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Jump("loc_90FC")

    label("loc_90FC")

    Return()

    # Function_43_8EB1 end

    def Function_44_90FD(): pass

    label("Function_44_90FD")


    def lambda_9102():
        OP_95(0xFE, 10000, 0, -28000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9102)
    WaitChrThread(0xFE, 1)

    def lambda_9120():
        OP_95(0xFE, 10000, 0, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9120)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_44_90FD end

    def Function_45_913A(): pass

    label("Function_45_913A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30200.itc", 0x1E)
    LoadChrToIndex("chr/ch24100.itc", 0x1F)
    LoadChrToIndex("chr/ch21800.itc", 0x20)
    LoadChrToIndex("apl/ch51216.itc", 0x21)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9179")
    LoadChrToIndex("apl/ch51217.itc", 0x22)
    Jump("loc_91E0")

    label("loc_9179")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9194")
    LoadChrToIndex("apl/ch51218.itc", 0x22)
    Jump("loc_91E0")

    label("loc_9194")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91AF")
    LoadChrToIndex("apl/ch51219.itc", 0x22)
    Jump("loc_91E0")

    label("loc_91AF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91CA")
    LoadChrToIndex("apl/ch51220.itc", 0x22)
    Jump("loc_91E0")

    label("loc_91CA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91E0")
    LoadChrToIndex("apl/ch51221.itc", 0x22)

    label("loc_91E0")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_925A")
    SetChrPos(0x102, -14410, 590, -16430, 90)
    Jump("loc_92ED")

    label("loc_925A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9280")
    SetChrPos(0x103, -14410, 590, -16430, 90)
    Jump("loc_92ED")

    label("loc_9280")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_92A6")
    SetChrPos(0x104, -14410, 590, -16430, 90)
    Jump("loc_92ED")

    label("loc_92A6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_92CC")
    SetChrPos(0x109, -14410, 590, -16430, 90)
    Jump("loc_92ED")

    label("loc_92CC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_92ED")
    SetChrPos(0x105, -14410, 590, -16430, 90)

    label("loc_92ED")

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

    def lambda_934F():
        OP_95(0xFE, -1500, 10, -16020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_934F)

    def lambda_9369():
        OP_95(0xFE, -3000, 10, -15160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9369)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93AD")

    def lambda_9393():
        OP_95(0xFE, -3600, 10, -17180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9393)
    Jump("loc_9464")

    label("loc_93AD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93DC")

    def lambda_93C2():
        OP_95(0xFE, -3600, 10, -17180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_93C2)
    Jump("loc_9464")

    label("loc_93DC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_940B")

    def lambda_93F1():
        OP_95(0xFE, -3600, 10, -17180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_93F1)
    Jump("loc_9464")

    label("loc_940B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_943A")

    def lambda_9420():
        OP_95(0xFE, -3600, 10, -17180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9420)
    Jump("loc_9464")

    label("loc_943A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9464")

    def lambda_944F():
        OP_95(0xFE, -3600, 10, -17180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_944F)

    label("loc_9464")

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
            "Soon, the on-the-spot inspection of\x01",
            "the Republic-bound train will be over.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Please, we ask you to not enter inside\x01",
            "the train for a little while longer.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00005FThe Republic-bound train  \x01",
            "is going to depart soon...\x02\x03",
            "#00003FWell then...\x01",
            "I wonder where the fake brand trader is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "When she popped in before,\x01",
            "I'm sure she was around there...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9652")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00101F...There she is.\x02",
    )

    CloseMessageWindow()
    Jump("loc_976C")

    label("loc_9652")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9696")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#00201F...Found her.\x02",
    )

    CloseMessageWindow()
    Jump("loc_976C")

    label("loc_9696")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_96D6")
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#00301F...Bingo.\x02",
    )

    CloseMessageWindow()
    Jump("loc_976C")

    label("loc_96D6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9726")
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105F...Could she be that one?\x02",
    )

    CloseMessageWindow()
    Jump("loc_976C")

    label("loc_9726")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_976C")
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x105,
        "#10305F...Could she be her?\x02",
    )

    CloseMessageWindow()

    label("loc_976C")

    Fade(500)
    OP_68(11100, 1200, -13380, 0)
    MoveCamera(40, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14210, 0)
    OP_0D()

    ChrTalk(
        0x23,
        (
            "──Hoh ho, you're someone\x01",
            "in the same business, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "So, how was business\x01",
            "over in Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x22,
        "Elderly Woman",
        "#11PHu hu, well, I'm afraid to say that...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x22,
        "Elderly Woman",
        (
            "#11PI had a little interference\x01",
            "due to business rivalry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Mrrr...\x01",
            "That's unfortunate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Honestly, fellows like them are\x01",
            "a disgrace to the traders.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x22,
        "Elderly Woman",
        (
            "#11PNo, I think that it was also some\x01",
            "lack of power on my part.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x22,
        "Elderly Woman",
        (
            "#11PThat is why this time I'm having a change of\x01",
            "attitude, trying to go the Empire region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Hah hah ha, that's an admirable\x01",
            "business temper you have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Hm, even having met like this\x01",
            "could be some kind of fate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "If you wish, I could introduce\x01",
            "you to some good connections\x01",
            "in the Empire region.\x02",
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
            "#11POh ho ho...\x01",
            "Thank you then, I think\x01",
            "I'll take up on your offer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F...It won't go that way.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9BC2")
    SetChrPos(0x102, -1220, 0, -14540, 90)
    Jump("loc_9C55")

    label("loc_9BC2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9BE8")
    SetChrPos(0x103, -1220, 0, -14540, 90)
    Jump("loc_9C55")

    label("loc_9BE8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9C0E")
    SetChrPos(0x104, -1220, 0, -14540, 90)
    Jump("loc_9C55")

    label("loc_9C0E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9C34")
    SetChrPos(0x109, -1220, 0, -14540, 90)
    Jump("loc_9C55")

    label("loc_9C34")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9C55")
    SetChrPos(0x105, -1220, 0, -14540, 90)

    label("loc_9C55")

    SetChrPos(0x21, -140, 0, -16200, 90)

    def lambda_9C6B():
        OP_95(0xFE, 6590, 0, -12750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9C6B)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9CAF")

    def lambda_9C95():
        OP_95(0xFE, 5030, 0, -12420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9C95)
    Jump("loc_9D66")

    label("loc_9CAF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9CDE")

    def lambda_9CC4():
        OP_95(0xFE, 5030, 0, -12420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9CC4)
    Jump("loc_9D66")

    label("loc_9CDE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D0D")

    def lambda_9CF3():
        OP_95(0xFE, 5030, 0, -12420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9CF3)
    Jump("loc_9D66")

    label("loc_9D0D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D3C")

    def lambda_9D22():
        OP_95(0xFE, 5030, 0, -12420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9D22)
    Jump("loc_9D66")

    label("loc_9D3C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D66")

    def lambda_9D51():
        OP_95(0xFE, 5030, 0, -12420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9D51)

    label("loc_9D66")


    def lambda_9D6B():
        OP_95(0xFE, 5280, 0, -14060, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_9D6B)
    Sleep(1000)

    def lambda_9D88():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_9D88)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9DBB")
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x5A, 0x0)
    Jump("loc_9E36")

    label("loc_9DBB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9DDB")
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x5A, 0x0)
    Jump("loc_9E36")

    label("loc_9DDB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9DFB")
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x5A, 0x0)
    Jump("loc_9E36")

    label("loc_9DFB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E1B")
    WaitChrThread(0x109, 1)
    OP_93(0x109, 0x5A, 0x0)
    Jump("loc_9E36")

    label("loc_9E1B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E36")
    WaitChrThread(0x105, 1)
    OP_93(0x105, 0x5A, 0x0)

    label("loc_9E36")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F24")

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*...\x01",
            "It looks like you remember us,\x01",
            "fake brand trader madam.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A08A")

    label("loc_9F24")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F76")

    ChrTalk(
        0x103,
        (
            "#00200FDid you remember us...?\x01",
            "fake brand trader madam.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A08A")

    label("loc_9F76")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9FDD")

    ChrTalk(
        0x104,
        (
            "#00300FEh he, it looks like you\x01",
            "remember us well,\x01",
            "fake brand trader grandma.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A08A")

    label("loc_9FDD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A035")

    ChrTalk(
        0x109,
        (
            "#10101FIs this person the fake brand\x01",
            "trader I heard about...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A08A")

    label("loc_A035")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A08A")

    ChrTalk(
        0x105,
        (
            "#10304FI see, this madame is the rumored\x01",
            "fake brand trader, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A08A")


    ChrTalk(
        0x21,
        (
            "It seems that you thought\x01",
            "to have completely\x01",
            "scattered us, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "Uh uh, this time you won't get away!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "W-Wait...\x01",
            "What the heck is\x01",
            "going on here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Fake brand...?\x01",
            "What're you talking about?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x22,
        "Elderly Woman",
        "#11P...Uh...uuuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FBased on a law amended article of the\x01",
            "autonomous state, we are taking you to the\x01",
            "police for questioning about illegal trades.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "We have finished to siege the station.\x01",
            "You don't have a place to escape anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "What about thinking\x01",
            "to not escape more\x01",
            "than this?\x02",
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
            "......n't......joke...\x02",
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
            "#11P#5SDon't joke you damn\x01",
            "shitty braaaaaats!!#3S\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x23, 0x22, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A38A")

    ChrTalk(
        0x102,
        "#00105FEeek!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A42F")

    label("loc_A38A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A3B4")

    ChrTalk(
        0x103,
        "#00210F...h...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A42F")

    label("loc_A3B4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A3DB")

    ChrTalk(
        0x104,
        "#00305FWhoa!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A42F")

    label("loc_A3DB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A406")

    ChrTalk(
        0x109,
        "#10105FEeeeeeh!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A42F")

    label("loc_A406")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A42F")

    ChrTalk(
        0x105,
        "#10305F...*pheew*♪\x02",
    )

    CloseMessageWindow()

    label("loc_A42F")


    ChrTalk(
        0x21,
        "Eek!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "W-W-W-W-What...!?\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x22,
        (
            "#11P#5SDriving me to a corner where I\x01",
            "can't escape in such a place...#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x22,
        (
            "#11P#5SNot once, but two times too...\x01",
            "How dare you to screw with me!#3S\x01",
            " \x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x22,
        (
            "#11P#5SYou keep doing nothing but sly things!\x01",
            "That's why I hate the police!#3S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FW-Well, "sly" you say...\x01",
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
            "#11P...Hmph, whatever.\x01",
            "I don't care if I am\x01",
            "sieged or whatever...\x02",
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
            "then tryyyyyyyyy!!#3S\x02",
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
            "#00006FN-No matter how often I see that,\x01",
            "she's got quite the presence...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A7CC")

    ChrTalk(
        0x102,
        (
            "#00107F...Wait, Lloyd!\x01",
            "It's no time to space out...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A908")

    label("loc_A7CC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A81E")

    ChrTalk(
        0x103,
        (
            "#00205F...Mr. Lloyd!\x01",
            "It is not the time to space out...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A908")

    label("loc_A81E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A866")

    ChrTalk(
        0x104,
        (
            "#00307FHey, Lloyd!\x01",
            "What're you spacin' about?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A908")

    label("loc_A866")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A8BD")

    ChrTalk(
        0x109,
        (
            "#10105FHah...\x01",
            "M-Mr. Lloyd!\x01",
            "It's not the time to space out...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A908")

    label("loc_A8BD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A908")

    ChrTalk(
        0x105,
        (
            "#10301F...It's not the time to\x01",
            "be spacing out, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A908")


    ChrTalk(
        0x21,
        "R-Right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FY-Yeah, let's chase after her!\x02\x03",
            "#00000FExit and entrances \x01",
            "are all under watch...\x01",
            "We just need to catch her!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 46)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A9B0")
    BeginChrThread(0x102, 1, 0, 47)
    Jump("loc_AA17")

    label("loc_A9B0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A9CB")
    BeginChrThread(0x103, 1, 0, 47)
    Jump("loc_AA17")

    label("loc_A9CB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A9E6")
    BeginChrThread(0x104, 1, 0, 47)
    Jump("loc_AA17")

    label("loc_A9E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA01")
    BeginChrThread(0x109, 1, 0, 47)
    Jump("loc_AA17")

    label("loc_AA01")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA17")
    BeginChrThread(0x105, 1, 0, 47)

    label("loc_AA17")

    BeginChrThread(0x21, 1, 0, 48)
    Sleep(3500)
    OP_63(0x23, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x23)

    ChrTalk(
        0x23,
        "*speechless*...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA75")
    EndChrThread(0x102, 0x1)
    Jump("loc_AAD4")

    label("loc_AA75")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA8E")
    EndChrThread(0x103, 0x1)
    Jump("loc_AAD4")

    label("loc_AA8E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AAA7")
    EndChrThread(0x104, 0x1)
    Jump("loc_AAD4")

    label("loc_AAA7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AAC0")
    EndChrThread(0x109, 0x1)
    Jump("loc_AAD4")

    label("loc_AAC0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AAD4")
    EndChrThread(0x105, 0x1)

    label("loc_AAD4")

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
        "Tsk, those damn shitty brats...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x22, 1)

    ChrTalk(
        0x22,
        (
            "If they're ambushing me in the station premises, \x01",
            "I must find out a different route...\x02",
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
            "──We are sorry to have made you wait.\x01",
            "The Republic-bound train is going to\x01",
            "depart soon. \x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Since it is dangerous, please refrain\x01",
            "to rush to get into the train.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD69")
    SetChrPos(0x102, 54450, 0, -16550, 90)
    Jump("loc_ADFC")

    label("loc_AD69")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD8F")
    SetChrPos(0x103, 54450, 0, -16550, 90)
    Jump("loc_ADFC")

    label("loc_AD8F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ADB5")
    SetChrPos(0x104, 54450, 0, -16550, 90)
    Jump("loc_ADFC")

    label("loc_ADB5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ADDB")
    SetChrPos(0x109, 54450, 0, -16550, 90)
    Jump("loc_ADFC")

    label("loc_ADDB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ADFC")
    SetChrPos(0x105, 54450, 0, -16550, 90)

    label("loc_ADFC")

    SetChrPos(0x21, 53420, 0, -15670, 90)

    def lambda_AE12():
        OP_95(0xFE, 66750, 6000, -15280, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AE12)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE59")

    def lambda_AE3F():
        OP_95(0xFE, 66090, 6000, -16660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AE3F)
    Jump("loc_AF10")

    label("loc_AE59")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE88")

    def lambda_AE6E():
        OP_95(0xFE, 66090, 6000, -16660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AE6E)
    Jump("loc_AF10")

    label("loc_AE88")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AEB7")

    def lambda_AE9D():
        OP_95(0xFE, 66090, 6000, -16660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AE9D)
    Jump("loc_AF10")

    label("loc_AEB7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AEE6")

    def lambda_AECC():
        OP_95(0xFE, 66090, 6000, -16660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AECC)
    Jump("loc_AF10")

    label("loc_AEE6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF10")

    def lambda_AEFB():
        OP_95(0xFE, 66090, 6000, -16660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AEFB)

    label("loc_AF10")

    Sleep(100)

    def lambda_AF18():
        OP_95(0xFE, 65090, 6000, -15890, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_AF18)
    OP_0D()
    WaitChrThread(0x101, 1)

    def lambda_AF37():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AF37)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF65")
    WaitChrThread(0x102, 1)

    def lambda_AF58():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AF58)
    Jump("loc_AFF8")

    label("loc_AF65")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF8B")
    WaitChrThread(0x103, 1)

    def lambda_AF7E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AF7E)
    Jump("loc_AFF8")

    label("loc_AF8B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AFB1")
    WaitChrThread(0x104, 1)

    def lambda_AFA4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AFA4)
    Jump("loc_AFF8")

    label("loc_AFB1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AFD7")
    WaitChrThread(0x109, 1)

    def lambda_AFCA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AFCA)
    Jump("loc_AFF8")

    label("loc_AFD7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AFF8")
    WaitChrThread(0x105, 1)

    def lambda_AFF0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AFF0)

    label("loc_AFF8")

    WaitChrThread(0x21, 1)

    def lambda_B001():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_B001)
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

    def lambda_B178():
        OP_96(0xFE, 0x33450, 0xFFFFF9F2, 0x1FA4, 0x251C, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_B178)
    Sleep(2000)

    ChrTalk(
        0x21,
        "#5S#6AEEEEEEEEEEH!!#3S\x02",
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
        "#00011FI-Impossible...!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B250")

    ChrTalk(
        0x102,
        "#00105FI-I don't believe it...!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_B31C")

    label("loc_B250")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B27E")

    ChrTalk(
        0x103,
        "#00205FN-No way...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_B31C")

    label("loc_B27E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B2B3")

    ChrTalk(
        0x104,
        "#00305FHey now, for real!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_B31C")

    label("loc_B2B3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B2EB")

    ChrTalk(
        0x109,
        "#10101FKh...what a way to...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_B31C")

    label("loc_B2EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B31C")

    ChrTalk(
        0x105,
        "#10305F...She's quite good.\x02",
    )

    CloseMessageWindow()

    label("loc_B31C")


    ChrTalk(
        0x21,
        "A-At the very end...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "Aah, what am I gonna\x01",
            "say to Inspector Donovan...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F............\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B3EE")

    ChrTalk(
        0x101,
        "#00001F......Let's go, Elie!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F......!\x01",
            "R-Right, understood!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B553")

    label("loc_B3EE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B43F")

    ChrTalk(
        0x101,
        "#00001F......Let's go, Tio!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F......!\x01",
            "Roger!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B553")

    label("loc_B43F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B499")

    ChrTalk(
        0x101,
        "#00001F......Let's go, Randy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F......!\x01",
            "Yeah, got it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B553")

    label("loc_B499")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B4EC")

    ChrTalk(
        0x101,
        "#00001F......Let's go, Noｱl!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10107F......!\x01",
            "Yessir!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B553")

    label("loc_B4EC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B553")

    ChrTalk(
        0x101,
        "#00001F......Let's go, Wazy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu...\x01",
            "You too don't want to lose, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B553")

    OP_93(0x21, 0x5A, 0x1F4)
    OP_63(0x21, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x21,
        "...Huh...don't tell me that...\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x21,
        "#5S......EEH!?#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "A-Are you kidding me...?\x01",
            "Are you going to give chase!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007FThe only way we can arrest her\x01",
            "is to chase after her!\x02\x03",
            "#00003FIt can't be helped...\x01",
            "We're going on ahead!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    def lambda_B67F():
        OP_95(0xFE, 66750, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B67F)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B6C6")

    def lambda_B6AC():
        OP_95(0xFE, 66090, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B6AC)
    Jump("loc_B77D")

    label("loc_B6C6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B6F5")

    def lambda_B6DB():
        OP_95(0xFE, 66090, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B6DB)
    Jump("loc_B77D")

    label("loc_B6F5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B724")

    def lambda_B70A():
        OP_95(0xFE, 66090, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B70A)
    Jump("loc_B77D")

    label("loc_B724")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B753")

    def lambda_B739():
        OP_95(0xFE, 66090, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B739)
    Jump("loc_B77D")

    label("loc_B753")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B77D")

    def lambda_B768():
        OP_95(0xFE, 66090, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B768)

    label("loc_B77D")

    OP_63(0x21, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(2000)
    OP_64(0x21)

    ChrTalk(
        0x21,
        (
            "W-What to do...\x01",
            "I can't leave it to the Support Section only...\x02",
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

    def lambda_B837():
        OP_95(0xFE, 66750, 6000, 350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_B837)
    Sleep(1000)
    Fade(500)
    EndChrThread(0x101, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B871")
    EndChrThread(0x102, 0x1)
    Jump("loc_B8D0")

    label("loc_B871")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B88A")
    EndChrThread(0x103, 0x1)
    Jump("loc_B8D0")

    label("loc_B88A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B8A3")
    EndChrThread(0x104, 0x1)
    Jump("loc_B8D0")

    label("loc_B8A3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B8BC")
    EndChrThread(0x109, 0x1)
    Jump("loc_B8D0")

    label("loc_B8BC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B8D0")
    EndChrThread(0x105, 0x1)

    label("loc_B8D0")

    EndChrThread(0x21, 0x1)
    OP_68(69980, 1500, 7190, 0)
    MoveCamera(43, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(30010, 0)
    SetChrPos(0x101, 66310, 6000, -9500, 0)
    SetChrFlags(0x101, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B943")
    SetChrPos(0x102, 66090, 6000, -10500, 0)
    SetChrFlags(0x102, 0x40)
    Jump("loc_B9EA")

    label("loc_B943")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B96E")
    SetChrPos(0x103, 66090, 6000, -10500, 0)
    SetChrFlags(0x103, 0x40)
    Jump("loc_B9EA")

    label("loc_B96E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B999")
    SetChrPos(0x104, 66090, 6000, -10500, 0)
    SetChrFlags(0x104, 0x40)
    Jump("loc_B9EA")

    label("loc_B999")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B9C4")
    SetChrPos(0x109, 66090, 6000, -10500, 0)
    SetChrFlags(0x109, 0x40)
    Jump("loc_B9EA")

    label("loc_B9C4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B9EA")
    SetChrPos(0x105, 66090, 6000, -10500, 0)
    SetChrFlags(0x105, 0x40)

    label("loc_B9EA")

    SetChrPos(0x21, 66310, 6000, -11500, 0)
    SetChrFlags(0x21, 0x40)
    Sound(456, 0, 100, 0)
    StopSound(835, 1000, 100)
    BeginChrThread(0x8, 1, 0, 54)
    OP_0D()
    BeginChrThread(0x101, 1, 0, 50)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BA37")
    BeginChrThread(0x102, 1, 0, 51)
    Jump("loc_BA9E")

    label("loc_BA37")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BA52")
    BeginChrThread(0x103, 1, 0, 51)
    Jump("loc_BA9E")

    label("loc_BA52")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BA6D")
    BeginChrThread(0x104, 1, 0, 51)
    Jump("loc_BA9E")

    label("loc_BA6D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BA88")
    BeginChrThread(0x109, 1, 0, 51)
    Jump("loc_BA9E")

    label("loc_BA88")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BA9E")
    BeginChrThread(0x105, 1, 0, 51)

    label("loc_BA9E")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BAF7")
    ClearChrFlags(0x102, 0x40)
    ClearChrFlags(0x102, 0x20)
    ClearChrFlags(0x102, 0x1000)
    Jump("loc_BB82")

    label("loc_BAF7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB1B")
    ClearChrFlags(0x103, 0x40)
    ClearChrFlags(0x103, 0x20)
    ClearChrFlags(0x103, 0x1000)
    Jump("loc_BB82")

    label("loc_BB1B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB3F")
    ClearChrFlags(0x104, 0x40)
    ClearChrFlags(0x104, 0x20)
    ClearChrFlags(0x104, 0x1000)
    Jump("loc_BB82")

    label("loc_BB3F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB63")
    ClearChrFlags(0x109, 0x40)
    ClearChrFlags(0x109, 0x20)
    ClearChrFlags(0x109, 0x1000)
    Jump("loc_BB82")

    label("loc_BB63")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB82")
    ClearChrFlags(0x105, 0x40)
    ClearChrFlags(0x105, 0x20)
    ClearChrFlags(0x105, 0x1000)

    label("loc_BB82")

    StopBGM(0xBB8)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("e4800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_45_913A end

    def Function_46_BB95(): pass

    label("Function_46_BB95")

    OP_95(0xFE, 8430, 0, -12130, 4000, 0x0)
    OP_95(0xFE, 25430, 0, -12130, 4000, 0x0)
    Return()

    # Function_46_BB95 end

    def Function_47_BBBE(): pass

    label("Function_47_BBBE")

    Sleep(200)
    OP_95(0xFE, 8430, 0, -12130, 4000, 0x0)
    OP_95(0xFE, 25430, 0, -12130, 4000, 0x0)
    Return()

    # Function_47_BBBE end

    def Function_48_BBEA(): pass

    label("Function_48_BBEA")

    Sleep(800)
    OP_95(0xFE, 8430, 0, -12130, 4000, 0x0)
    OP_95(0xFE, 25430, 0, -12130, 4000, 0x0)
    Return()

    # Function_48_BBEA end

    def Function_49_BC16(): pass

    label("Function_49_BC16")

    OP_95(0xFE, 66190, 6000, -15970, 4000, 0x0)
    OP_95(0xFE, 66190, 6000, -5060, 4000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_49_BC16 end

    def Function_50_BC46(): pass

    label("Function_50_BC46")

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

    # Function_50_BC46 end

    def Function_51_BCA4(): pass

    label("Function_51_BCA4")

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

    # Function_51_BCA4 end

    def Function_52_BD02(): pass

    label("Function_52_BD02")

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

    # Function_52_BD02 end

    def Function_53_BD5E(): pass

    label("Function_53_BD5E")


    def lambda_BD63():
        OP_95(0xFE, 210000, -1550, 8100, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BD63)
    Sleep(500)

    def lambda_BD80():
        OP_95(0xFE, 210000, -1550, 8100, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BD80)
    Sleep(700)

    def lambda_BD9D():
        OP_95(0xFE, 210000, -1550, 8100, 8500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BD9D)
    Sleep(800)

    def lambda_BDBA():
        OP_95(0xFE, 210000, -1550, 8100, 9500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BDBA)
    Return()

    # Function_53_BD5E end

    def Function_54_BDD0(): pass

    label("Function_54_BDD0")

    SetChrPos(0x8, 70000, -1550, 8100, 0)

    def lambda_BDE6():
        OP_95(0xFE, 210000, -1550, 8100, 9500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BDE6)
    Return()

    # Function_54_BDD0 end

    def Function_55_BDFC(): pass

    label("Function_55_BDFC")

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

    # Function_55_BDFC end

    def Function_56_BEFA(): pass

    label("Function_56_BEFA")

    Sleep(11000)
    Sound(143, 0, 50, 0)
    Return()

    # Function_56_BEFA end

    SaveToFile()

Try(main)

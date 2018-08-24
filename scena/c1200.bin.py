from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1200.bin",                # FileName
        "c1200",                    # MapName
        "c1200",                    # Location
        0x001A,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("c1200", "c1000_1", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x07',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 2000, 0, 0, 0, 0, 1, 26, 0, 8, 0, 9],
    )

    BuildStringList((
        "c1200",                  # 0
        "Cunha",                  # 1
        "Hauser",                 # 2
        "Bishop",                 # 3
        "Old Man Quine",          # 4
        "Amisaah",                # 5
        "Nikol",                  # 6
        "Celine",                 # 7
        "Michey",                 # 8
        "MWL Staff",              # 9
        "MWL Staff",              # 10
        "Citizen",                # 11
        "Citizen",                # 12
        "Citizen",                # 13
        "Citizen",                # 14
        "Tourist",                # 15
        "Tourist",                # 16
        "Mechanic",               # 17
        "Roy",                    # 18
        "Meiling",                # 19
        "Zeit",                   # 20
        "KeA",                    # 21
        "Shizuku",                # 22
        "Tourist",                # 23
        "Boy",                    # 24
        "Citizen",                # 25
        "Section Chief Joe Ridge",# 26
        "Policeman",              # 27
        "Policeman",              # 28
        "Water Bus Guide",        # 29
        "Patrol Car",             # 30
        "Nielsen",                # 31
        "Cao",                    # 32
        "Lau",                    # 33
        "Yuri",                   # 34
        "Sykes",                  # 35
        "Reggie",                 # 36
        "暴走車",                 # 37
        "Patrol Car",             # 38
        "水上バス",               # 39
        "SE制御",                 # 40
        "Clyde",                  # 41
        "Young Man",              # 42
        "車",                     # 43
        "ボート",                 # 44
        "Olivier",                # 45
        "Central Square",         # 46
        "West Street",            # 47
        "Governmental District",  # 48
        "Residential Street",     # 49
        "Entertainment District", # 50
        "East Street",            # 51
        "Downtown",               # 52
        "Waterfront Area",        # 53
        "IBC",                    # 54
        "Station Street",         # 55
        "Back Street",            # 56
        "St. Ursula Byroad",      # 57
        "East Crossbell Highway", # 58
        "West Crossbell HIghway", # 59
        "Mainz Mountain Road",    # 60
        "Orchis Tower",           # 61
    ))

    AddCharChip((
        "chr/ch26000.itc",                   # 00
        "chr/ch49600.itc",                   # 01
        "chr/ch49700.itc",                   # 02
        "chr/ch10200.itc",                   # 03
        "chr/ch44500.itc",                   # 04
        "chr/ch44600.itc",                   # 05
        "chr/ch23000.itc",                   # 06
        "chr/ch20700.itc",                   # 07
        "chr/ch20300.itc",                   # 08
        "chr/ch24400.itc",                   # 09
        "chr/ch20500.itc",                   # 0A
        "chr/ch22100.itc",                   # 0B
        "chr/ch25200.itc",                   # 0C
        "chr/ch26000.itc",                   # 0D
        "apl/ch50168.itc",                   # 0E
        "chr/ch21500.itc",                   # 0F
        "chr/ch28900.itc",                   # 10
        "chr/ch29100.itc",                   # 11
        "chr/ch24000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch21902.itc",                   # 14
        "chr/ch22200.itc",                   # 15
        "chr/ch49500.itc",                   # 16
        "chr/ch49100.itc",                   # 17
        "chr/ch02707.itc",                   # 18
        "chr/ch08200.itc",                   # 19
        "chr/ch08700.itc",                   # 1A
        "chr/ch30100.itc",                   # 1B
        "chr/ch30000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
        "chr/ch00000.itc",                   # 1E
        "chr/ch00000.itc",                   # 1F
        "chr/ch00000.itc",                   # 20
        "chr/ch46500.itc",                   # 21
        "apl/ch51272.itc",                   # 22
        "chr/ch21900.itc",                   # 23
        "chr/ch26600.itc",                   # 24
        "chr/ch45102.itc",                   # 25
    ))

    DeclNpc(4294954097, 0,       11500,   90,   257,  0x0, 0,   11,  0,   0,   1,   0,   11,  255,  0)
    DeclNpc(4294956826, 0,       13340,   180,  257,  0x0, 0,   12,  0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294914826, 2000,    21149,   90,   257,  0x0, 0,   13,  0,   0,   2,   0,   13,  255,  0)
    DeclNpc(39669,   4294964796, 4294947917, 180,  257,  0x0, 0,   18,  0,   255, 255, 0,   14,  255,  0)
    DeclNpc(38439,   4294964806, 4294949217, 135,  257,  0x0, 0,   15,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(4294949296, 0,       4294961546, 90,   385,  0x0, 0,   16,  0,   0,   4,   0,   18,  255,  0)
    DeclNpc(13000,   0,       4294957296, 0,    385,  0x0, 0,   17,  0,   0,   5,   0,   19,  255,  0)
    DeclNpc(9479,    4294966597, 159,     270,  389,  0x0, 0,   3,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(6550,    4294966597, 4294964937, 315,  389,  0x0, 0,   4,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(5989,    4294966597, 2119,    225,  389,  0x0, 0,   5,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(4449,    4294966597, 4294966486, 90,   389,  0x0, 0,   6,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(4940,    4294966597, 4294965096, 90,   389,  0x0, 0,   7,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(3809,    4294966597, 4294963927, 45,   389,  0x0, 0,   8,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(39900,   4294964796, 3650,    270,  389,  0x0, 0,   11,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(4190,    4294966597, 1529,    135,  389,  0x0, 0,   9,   0,   0,   0,   0,   27,  255,  0)
    DeclNpc(3809,    4294966597, 250,     90,   389,  0x0, 0,   10,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   29,  255,  0)
    DeclNpc(4294967206, 4294966597, 4294965647, 90,   389,  0x0, 0,   1,   0,   0,   0,   0,   30,  255,  0)
    DeclNpc(86480,   4294964796, 19430,   0,    389,  0x0, 0,   2,   0,   0,   0,   0,   31,  255,  0)
    DeclNpc(8659,    4294966597, 670,     225,  405,  0x0, 0,   24,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(7190,    4294966597, 379,     90,   389,  0x0, 0,   25,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(8119,    4294966597, 4294966566, 0,    389,  0x0, 0,   26,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(7239,    4294966746, 3190,    180,  389,  0x0, 0,   20,  0,   0,   0,   0,   36,  255,  0)
    DeclNpc(7239,    4294966597, 1580,    0,    385,  0x0, 0,   21,  0,   0,   0,   0,   37,  255,  0)
    DeclNpc(47909,   4294964796, 16530,   180,  389,  0x0, 0,   23,  0,   0,   0,   0,   38,  255,  0)
    DeclNpc(4294949497, 0,       13369,   0,    389,  0x0, 0,   27,  0,   0,   0,   0,   39,  255,  0)
    DeclNpc(4294949296, 0,       4294961546, 90,   385,  0x0, 0,   28,  0,   0,   6,   0,   40,  255,  0)
    DeclNpc(4294949497, 0,       13369,   180,  389,  0x0, 0,   28,  0,   0,   0,   0,   41,  255,  0)
    DeclNpc(42450,   4294964796, 2329,    235,  389,  0x0, 0,   36,  0,   0,   0,   0,   42,  255,  0)
    DeclNpc(4294946057, 0,       14350,   90,   196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(7820,    4294966896, 3200,    180,  389,  0x0, 0,   37,  0,   255, 255, 0,   43,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   33,  0,   0,   0,   255, 255, 255,  0)

    DeclEvent(0x0000, 0, 65,  -13.5,                 27.5,                  1.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   6.75,                  -13.75,                -0.20000000298023224,  1.0])
    DeclEvent(0x0000, 0, 66,  5.0,                   33.0,                  1.0,                   324.0,                 [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    0.0,                   -0.4166666865348816,   -11.0,                 -0.1428571492433548,   1.0])
    DeclEvent(0x0000, 0, 67,  -20.0,                 -29.0,                 -0.5,                  324.0,                 [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    0.0,                   1.6666667461395264,    9.666666984558105,     0.0714285746216774,    1.0])
    DeclEvent(0x0000, 0, 68,  -29.0,                 23.329999923706055,    1.0,                   324.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    0.0,                   9.666666984558105,     -1.944166660308838,    -0.1428571492433548,   1.0])
    DeclEvent(0x0000, 0, 78,  -0.23999999463558197,  6.5,                   -0.28999999165534973,  324.0,                 [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    0.0,                   0.019999999552965164,  -2.1666667461395264,   0.0414285734295845,    1.0])
    DeclEvent(0x0000, 0, 79,  -0.09000000357627869,  -6.5,                  -0.20999999344348907,  324.0,                 [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    0.0,                   0.007500000298023224,  2.1666667461395264,    0.030000001192092896,  1.0])
    DeclEvent(0x0000, 0, 93,  33.08000183105469,     0.07999999821186066,   -2.5,                  324.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -11.026667594909668,   -0.006666666828095913, 0.625,                 1.0])

    DeclActor(16750,   4294966296, 4294951556, 1200,    16750,   0,       4294951556, 0x007C, 0,  10, 0x0000)
    DeclActor(82470,   4294964796, 15010,   1200,    79890,   4294963796, 8810,    0x007C, 0,  46, 0x0000)
    DeclActor(19200,   250,     20500,   2000,    19200,   1250,    20500,   0x007C, 0,  44, 0x0000)
    DeclActor(34000,   4294964796, 3400,    1500,    34000,   4294965796, 3400,    0x007C, 0,  105, 0x0000)
    DeclActor(7470,    4294966596, 3250,    1500,    7470,    4294966746, 3250,    0x007C, 0,  62, 0x0000)
    DeclActor(4294960156, 0,       13580,   1500,    4294960156, 1250,    13580,   0x007C, 0,  63, 0x0000)
    DeclActor(39300,   4294964796, 19050,   1500,    39300,   4294966046, 19050,   0x007C, 0,  64, 0x0000)
    DeclActor(4294953796, 1000,    27500,   2000,    4294953796, 3000,    27500,   0x007C, 0,  45, 0x0000)
    DeclActor(77220,   4294964796, 20290,   2000,    77220,   4294966296, 20290,   0x007C, 0,  106, 0x0000)

    PlaceName(-123.13999938964844, 0.0, -85.1500015258789, 0x0000, 0x0000, "Central Square")
    PlaceName(-209.27000427246094, 0.0, -79.26000213623047, 0x0000, 0x0000, "West Street")
    PlaceName(-87.7699966430664, 0.0, 31.440000534057617, 0x0000, 0x0000, "Governmental District")
    PlaceName(-289.17999267578125, 0.0, 18.34000015258789, 0x0000, 0x0000, "Residential Street")
    PlaceName(-193.5500030517578, 0.0, 7.860000133514404, 0x0000, 0x0000, "Entertainment District")
    PlaceName(-16.700000762939453, 0.0, -115.27999877929688, 0x0000, 0x0000, "East Street")
    PlaceName(29.799999237060547, 0.0, -187.3300018310547, 0x0000, 0x0000, "Downtown")
    PlaceName(19.979999542236328, 0.0, -28.81999969482422, 0x0000, 0x0000, "Waterfront Area")
    PlaceName(-14.079999923706055, 0.0, 94.31999969482422, 0x0000, 0x0000, "IBC")
    PlaceName(-108.4000015258789, 0.0, -175.5399932861328, 0x0000, 0x0000, "Station Street")
    PlaceName(-169.97000122070312, 0.0, -39.29999923706055, 0x0000, 0x0000, "Back Street")
    PlaceName(-112.33000183105469, 0.0, -216.14999389648438, 0x0000, 0x0000, "St. Ursula Byroad")
    PlaceName(54.040000915527344, 0.0, -96.94000244140625, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-276.0799865722656, 0.0, -81.22000122070312, 0x0000, 0x0000, "West Crossbell HIghway")
    PlaceName(-268.2200012207031, 0.0, 49.779998779296875, 0x0000, 0x0000, "Mainz Mountain Road")
    PlaceName(-96.5, 0.0, 203.75, 0x0000, 0x0000, "Orchis Tower")
    PlaceName(-151.9600067138672, 0.0, -103.48999786376953, 0x0000, 0x0051, "")
    PlaceName(-81.55000305175781, 0.0, -69.43000030517578, 0x0000, 0x0054, "")
    PlaceName(-119.87000274658203, 0.0, -113.97000122070312, 0x0000, 0x0057, "")
    PlaceName(-152.94000244140625, 0.0, -65.5, 0x0000, 0x0053, "")
    PlaceName(-126.08999633789062, 0.0, -34.060001373291016, 0x0000, 0x0053, "")
    PlaceName(-192.57000732421875, 0.0, -72.05000305175781, 0x0000, 0x0053, "")
    PlaceName(-205.33999633789062, 0.0, -44.540000915527344, 0x0000, 0x0053, "")
    PlaceName(-173.89999389648438, 0.0, -2.619999885559082, 0x0000, 0x0052, "")
    PlaceName(-167.67999267578125, 0.0, -19.649999618530273, 0x0000, 0x0053, "")
    PlaceName(-156.22000122070312, 0.0, -30.790000915527344, 0x0000, 0x0053, "")
    PlaceName(-118.87999725341797, 0.0, 62.22999954223633, 0x0000, 0x0051, "")
    PlaceName(27.84000015258789, 0.0, -115.27999877929688, 0x0000, 0x0052, "")
    PlaceName(5.570000171661377, 0.0, -233.83999633789062, 0x0000, 0x0053, "")
    PlaceName(-11.460000038146973, 0.0, -209.60000610351562, 0x0000, 0x0053, "")

    ChipFrameInfo(3584, 0)                                       # 0

    ScpFunction((
        "Function_0_E00",          # 00, 0
        "Function_1_EB0",          # 01, 1
        "Function_2_F61",          # 02, 2
        "Function_3_109B",         # 03, 3
        "Function_4_11D5",         # 04, 4
        "Function_5_1286",         # 05, 5
        "Function_6_1337",         # 06, 6
        "Function_7_13E8",         # 07, 7
        "Function_8_14AC",         # 08, 8
        "Function_9_1C86",         # 09, 9
        "Function_10_2092",        # 0A, 10
        "Function_11_21E3",        # 0B, 11
        "Function_12_34E8",        # 0C, 12
        "Function_13_4C4F",        # 0D, 13
        "Function_14_5627",        # 0E, 14
        "Function_15_5E33",        # 0F, 15
        "Function_16_5F6D",        # 10, 16
        "Function_17_60A5",        # 11, 17
        "Function_18_64F0",        # 12, 18
        "Function_19_66CE",        # 13, 19
        "Function_20_67B0",        # 14, 20
        "Function_21_68C7",        # 15, 21
        "Function_22_69CF",        # 16, 22
        "Function_23_6B15",        # 17, 23
        "Function_24_6BC6",        # 18, 24
        "Function_25_6C7A",        # 19, 25
        "Function_26_6D43",        # 1A, 26
        "Function_27_6D76",        # 1B, 27
        "Function_28_6F06",        # 1C, 28
        "Function_29_7032",        # 1D, 29
        "Function_30_7050",        # 1E, 30
        "Function_31_7086",        # 1F, 31
        "Function_32_70AA",        # 20, 32
        "Function_33_7113",        # 21, 33
        "Function_34_71F7",        # 22, 34
        "Function_35_7311",        # 23, 35
        "Function_36_73B9",        # 24, 36
        "Function_37_74DE",        # 25, 37
        "Function_38_7594",        # 26, 38
        "Function_39_77AC",        # 27, 39
        "Function_40_796F",        # 28, 40
        "Function_41_7BB7",        # 29, 41
        "Function_42_7F78",        # 2A, 42
        "Function_43_80D9",        # 2B, 43
        "Function_44_8272",        # 2C, 44
        "Function_45_87CD",        # 2D, 45
        "Function_46_8A1E",        # 2E, 46
        "Function_47_8AE5",        # 2F, 47
        "Function_48_93DB",        # 30, 48
        "Function_49_94D5",        # 31, 49
        "Function_50_94F4",        # 32, 50
        "Function_51_9915",        # 33, 51
        "Function_52_9960",        # 34, 52
        "Function_53_99C1",        # 35, 53
        "Function_54_9A22",        # 36, 54
        "Function_55_9A52",        # 37, 55
        "Function_56_9A80",        # 38, 56
        "Function_57_A36C",        # 39, 57
        "Function_58_A46C",        # 3A, 58
        "Function_59_A48A",        # 3B, 59
        "Function_60_A4BE",        # 3C, 60
        "Function_61_A4F2",        # 3D, 61
        "Function_62_AA7F",        # 3E, 62
        "Function_63_AAD6",        # 3F, 63
        "Function_64_AB0E",        # 40, 64
        "Function_65_AB5A",        # 41, 65
        "Function_66_ABAF",        # 42, 66
        "Function_67_AC25",        # 43, 67
        "Function_68_AC9B",        # 44, 68
        "Function_69_AD11",        # 45, 69
        "Function_70_B12E",        # 46, 70
        "Function_71_B2E3",        # 47, 71
        "Function_72_BAA8",        # 48, 72
        "Function_73_C586",        # 49, 73
        "Function_74_C5BD",        # 4A, 74
        "Function_75_C608",        # 4B, 75
        "Function_76_D7D0",        # 4C, 76
        "Function_77_DA70",        # 4D, 77
        "Function_78_DAB3",        # 4E, 78
        "Function_79_DB63",        # 4F, 79
        "Function_80_DC13",        # 50, 80
        "Function_81_EBB3",        # 51, 81
        "Function_82_EBD0",        # 52, 82
        "Function_83_EBED",        # 53, 83
        "Function_84_EC0A",        # 54, 84
        "Function_85_EC7D",        # 55, 85
        "Function_86_ECF0",        # 56, 86
        "Function_87_EE04",        # 57, 87
        "Function_88_EF18",        # 58, 88
        "Function_89_EF3D",        # 59, 89
        "Function_90_EF8B",        # 5A, 90
        "Function_91_1004D",       # 5B, 91
        "Function_92_108A1",       # 5C, 92
        "Function_93_108F7",       # 5D, 93
        "Function_94_10C16",       # 5E, 94
        "Function_95_11003",       # 5F, 95
        "Function_96_11031",       # 60, 96
        "Function_97_1179E",       # 61, 97
        "Function_98_11830",       # 62, 98
        "Function_99_1187B",       # 63, 99
        "Function_100_118C6",      # 64, 100
        "Function_101_11911",      # 65, 101
        "Function_102_1195C",      # 66, 102
        "Function_103_119A7",      # 67, 103
        "Function_104_119F2",      # 68, 104
        "Function_105_11B48",      # 69, 105
        "Function_106_11C9F",      # 6A, 106
    ))


    def Function_0_E00(): pass

    label("Function_0_E00")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_E38"),
        (1, "loc_E44"),
        (2, "loc_E50"),
        (3, "loc_E5C"),
        (4, "loc_E68"),
        (5, "loc_E74"),
        (6, "loc_E80"),
        (SWITCH_DEFAULT, "loc_E8C"),
    )


    label("loc_E38")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_E44")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_E50")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_E5C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_E68")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_E74")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_E80")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_E8C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_E98")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EAF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_EAF")

    Return()

    # Function_0_E00 end

    def Function_1_EB0(): pass

    label("Function_1_EB0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F60")
    OP_95(0xFE, 14600, 0, 11500, 1000, 0x0)
    OP_95(0xFE, 20200, 0, 8200, 1000, 0x0)
    OP_95(0xFE, 20200, 0, -6200, 1000, 0x0)
    OP_95(0xFE, 14000, 0, -11700, 1000, 0x0)
    OP_95(0xFE, -14000, 0, -11700, 1000, 0x0)
    OP_95(0xFE, -20000, 0, -6400, 1000, 0x0)
    OP_95(0xFE, -20000, 0, 6000, 1000, 0x0)
    OP_95(0xFE, -13200, 0, 11500, 1000, 0x0)
    Jump("Function_1_EB0")

    label("loc_F60")

    Return()

    # Function_1_EB0 end

    def Function_2_F61(): pass

    label("Function_2_F61")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_109A")
    Sleep(3000)
    OP_95(0xFE, -13000, 2000, 21150, 5000, 0x0)
    OP_95(0xFE, -13000, 2000, 24150, 5000, 0x0)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_95(0xFE, 1760, 2000, 24150, 5000, 0x0)
    OP_95(0xFE, 1760, 5080, 38700, 8000, 0x0)
    Sleep(3000)
    OP_95(0xFE, 1760, 2000, 24150, 5000, 0x0)
    OP_95(0xFE, -13000, 2000, 24150, 5000, 0x0)
    OP_95(0xFE, -13000, 0, 14240, 5000, 0x0)
    OP_95(0xFE, -22130, 0, 5860, 5000, 0x0)
    OP_95(0xFE, -22020, 0, -46700, 5000, 0x0)
    Sleep(3000)
    OP_95(0xFE, -22130, 0, 5860, 5000, 0x0)
    OP_95(0xFE, -15540, 0, 14240, 5000, 0x0)
    OP_95(0xFE, -15540, 2000, 21150, 5000, 0x0)
    OP_95(0xFE, -52470, 2000, 21150, 5000, 0x0)
    Jump("Function_2_F61")

    label("loc_109A")

    Return()

    # Function_2_F61 end

    def Function_3_109B(): pass

    label("Function_3_109B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11D4")
    Sleep(3000)
    OP_95(0xFE, -13000, 2000, 21150, 8000, 0x0)
    OP_95(0xFE, -13000, 2000, 24150, 8000, 0x0)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_95(0xFE, 1760, 2000, 24150, 8000, 0x0)
    OP_95(0xFE, 1760, 5080, 38700, 10000, 0x0)
    Sleep(3000)
    OP_95(0xFE, 1760, 2000, 24150, 8000, 0x0)
    OP_95(0xFE, -13000, 2000, 24150, 8000, 0x0)
    OP_95(0xFE, -13000, 0, 14240, 8000, 0x0)
    OP_95(0xFE, -22130, 0, 5860, 8000, 0x0)
    OP_95(0xFE, -22020, 0, -46700, 8000, 0x0)
    Sleep(3000)
    OP_95(0xFE, -22130, 0, 5860, 8000, 0x0)
    OP_95(0xFE, -15540, 0, 14240, 8000, 0x0)
    OP_95(0xFE, -15540, 2000, 21150, 8000, 0x0)
    OP_95(0xFE, -52470, 2000, 21150, 8000, 0x0)
    Jump("Function_3_109B")

    label("loc_11D4")

    Return()

    # Function_3_109B end

    def Function_4_11D5(): pass

    label("Function_4_11D5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1285")
    OP_95(0xFE, -13000, 0, -10000, 4000, 0x0)
    OP_95(0xFE, 13000, 0, -10000, 4000, 0x0)
    OP_95(0xFE, 18000, 0, -4300, 4000, 0x0)
    OP_95(0xFE, 18000, 0, 7040, 4000, 0x0)
    OP_95(0xFE, 13000, 0, 10000, 4000, 0x0)
    OP_95(0xFE, -12700, 0, 10000, 4000, 0x0)
    OP_95(0xFE, -18000, 0, 5200, 4000, 0x0)
    OP_95(0xFE, -18000, 0, -5750, 4000, 0x0)
    Jump("Function_4_11D5")

    label("loc_1285")

    Return()

    # Function_4_11D5 end

    def Function_5_1286(): pass

    label("Function_5_1286")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1336")
    OP_95(0xFE, 18000, 0, -4300, 4000, 0x0)
    OP_95(0xFE, 18000, 0, 7040, 4000, 0x0)
    OP_95(0xFE, 13000, 0, 10000, 4000, 0x0)
    OP_95(0xFE, -12700, 0, 10000, 4000, 0x0)
    OP_95(0xFE, -18000, 0, 5200, 4000, 0x0)
    OP_95(0xFE, -18000, 0, -5750, 4000, 0x0)
    OP_95(0xFE, -13000, 0, -10000, 4000, 0x0)
    OP_95(0xFE, 13000, 0, -10000, 4000, 0x0)
    Jump("Function_5_1286")

    label("loc_1336")

    Return()

    # Function_5_1286 end

    def Function_6_1337(): pass

    label("Function_6_1337")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13E7")
    OP_95(0xFE, -13000, 0, -10000, 1000, 0x0)
    OP_95(0xFE, 13000, 0, -10000, 1000, 0x0)
    OP_95(0xFE, 18000, 0, -4300, 1000, 0x0)
    OP_95(0xFE, 18000, 0, 7040, 1000, 0x0)
    OP_95(0xFE, 13000, 0, 10000, 1000, 0x0)
    OP_95(0xFE, -12700, 0, 10000, 1000, 0x0)
    OP_95(0xFE, -18000, 0, 5200, 1000, 0x0)
    OP_95(0xFE, -18000, 0, -5750, 1000, 0x0)
    Jump("Function_6_1337")

    label("loc_13E7")

    Return()

    # Function_6_1337 end

    def Function_7_13E8(): pass

    label("Function_7_13E8")

    SetMapObjFlags(0x5, 0x2000000)
    SetMapObjFlags(0x7, 0x2000000)
    SetMapObjFlags(0xA, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0xD, 0x2000000)
    SetMapObjFlags(0xF, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1435")
    ClearMapObjFlags(0x5, 0x2000000)
    ClearMapObjFlags(0x7, 0x2000000)

    label("loc_1435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1449")
    ClearMapObjFlags(0xD, 0x2000000)

    label("loc_1449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1458")
    ClearMapObjFlags(0xD, 0x2000000)

    label("loc_1458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_1467")
    ClearMapObjFlags(0xA, 0x2000000)

    label("loc_1467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_1488")
    ClearMapObjFlags(0xB, 0x2000000)
    ClearMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0x5, 0x2000000)
    SetMapObjFlags(0x7, 0x2000000)

    label("loc_1488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1497")
    ClearMapObjFlags(0xF, 0x2000000)

    label("loc_1497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14AB")
    ClearMapObjFlags(0xB, 0x2000000)

    label("loc_14AB")

    Return()

    # Function_7_13E8 end

    def Function_8_14AC(): pass

    label("Function_8_14AC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E7")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_156E")
    SetChrPos(0x0, 4870, 3350, 31570, 180)
    SetChrPos(0x1, 4870, 3350, 31570, 180)
    SetChrPos(0x2, 4870, 3350, 31570, 180)
    SetChrPos(0x3, 4870, 3350, 31570, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1541")
    SetChrPos(0x4, 4870, 3350, 31570, 180)
    SetChrPos(0x5, 4870, 3350, 31570, 180)
    Jump("loc_1560")

    label("loc_1541")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1560")
    SetChrPos(0x4, 4870, 3350, 31570, 180)

    label("loc_1560")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16E7")

    label("loc_156E")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1646")
    SetChrPos(0x0, -28110, 2000, 23520, 90)
    SetChrPos(0x1, -28110, 2000, 23520, 90)
    SetChrPos(0x2, -28110, 2000, 23520, 90)
    SetChrPos(0x3, -28110, 2000, 23520, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1619")
    SetChrPos(0x4, -28110, 2000, 23520, 90)
    SetChrPos(0x5, -28110, 2000, 23520, 90)
    Jump("loc_1638")

    label("loc_1619")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1638")
    SetChrPos(0x4, -28110, 2000, 23520, 90)

    label("loc_1638")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16E7")

    label("loc_1646")

    SetChrPos(0x0, -19600, 0, -27950, 0)
    SetChrPos(0x1, -19600, 0, -27950, 0)
    SetChrPos(0x2, -19600, 0, -27950, 0)
    SetChrPos(0x3, -19600, 0, -27950, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16BF")
    SetChrPos(0x4, -19600, 0, -27950, 0)
    SetChrPos(0x5, -19600, 0, -27950, 0)
    Jump("loc_16DE")

    label("loc_16BF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16DE")
    SetChrPos(0x4, -19600, 0, -27950, 0)

    label("loc_16DE")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_16E7")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_16FE")
    Jump("loc_1B60")

    label("loc_16FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_170C")
    Jump("loc_1B60")

    label("loc_170C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 1)), scpexpr(EXPR_END)), "loc_171A")
    Jump("loc_1B60")

    label("loc_171A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1750")
    SetChrPos(0xB, 39670, -2500, -19380, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, 38440, -2490, -18080, 180)
    Jump("loc_1B60")

    label("loc_1750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1786")
    SetChrFlags(0x8, 0x80)
    BeginChrThread(0xA, 0, 0, 3)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0x9, 0x16)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_1B60")

    label("loc_1786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_17AF")
    SetChrChipByIndex(0xB, 0xE)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    Jump("loc_1B60")

    label("loc_17AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_186B")
    SetChrChipByIndex(0xB, 0xE)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0x24, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1815")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x16, 40740, -2500, -2330, 180)
    SetChrPos(0x17, 40630, -2500, -3760, 0)
    Jump("loc_1866")

    label("loc_1815")

    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x15, 0x10)
    SetChrPos(0x16, 38970, -2500, 3640, 90)
    SetChrPos(0x12, 39450, -2500, -2530, 90)
    SetChrPos(0x14, 39750, -2500, -1190, 90)

    label("loc_1866")

    Jump("loc_1B60")

    label("loc_186B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1883")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_1B60")

    label("loc_1883")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_190D")
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x10)
    ClearChrFlags(0x26, 0x4)
    SetChrPos(0xB, -7150, 0, 12300, 0)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C1")
    SetChrFlags(0xB, 0x10)

    label("loc_18C1")

    SetChrPos(0xC, -8150, 0, 12300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18E1")
    SetChrFlags(0xC, 0x10)

    label("loc_18E1")

    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    OP_93(0x23, 0xB4, 0x0)
    SetChrPos(0x23, -17800, 0, 15000, 180)
    ClearChrFlags(0x21, 0x80)
    Jump("loc_1B60")

    label("loc_190D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1A1A")
    BeginChrThread(0xA, 0, 0, 3)
    SetChrPos(0xB, -4350, 0, -8570, 45)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, -5350, 0, -8570, 45)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1999")
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_1999")

    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x22, 0x80)
    BeginChrThread(0x22, 0, 0, 0)
    SetChrPos(0x22, -1800, -310, 6250, 135)
    ClearChrFlags(0x23, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A15")
    ClearChrFlags(0x34, 0x80)
    SetChrPos(0x34, 9330, -690, -1000, 270)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 9330, -690, 600, 270)

    label("loc_1A15")

    Jump("loc_1B60")

    label("loc_1A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1A7E")
    SetChrChipByIndex(0xB, 0xE)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A43")
    SetChrFlags(0xB, 0x10)

    label("loc_1A43")

    SetChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_1A6F")
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x10)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x10)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x10)

    label("loc_1A6F")

    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    Jump("loc_1B60")

    label("loc_1A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1AD4")
    BeginChrThread(0xA, 0, 0, 3)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AC6")
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x10)

    label("loc_1AC6")

    SetChrChipByIndex(0x9, 0x16)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_1B60")

    label("loc_1AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1B60")
    SetChrChipByIndex(0xB, 0xE)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AFD")
    SetChrFlags(0xB, 0x10)

    label("loc_1AFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B0C")
    SetChrFlags(0xC, 0x10)

    label("loc_1B0C")

    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_END)), "loc_1B4F")
    ClearChrFlags(0x24, 0x80)
    SetChrChipByIndex(0x1E, 0x23)
    SetChrPos(0x1E, 41500, -2500, 160, 90)
    SetChrPos(0x1F, 41500, -2500, -1440, 90)
    Jump("loc_1B60")

    label("loc_1B4F")

    SetChrChipByIndex(0x1E, 0x14)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)

    label("loc_1B60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B84")
    SetChrPos(0x18, 42400, -2500, -18000, 270)
    ClearChrFlags(0x18, 0x80)

    label("loc_1B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_END)), "loc_1BB1")
    ClearChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1BB1")
    ClearChrFlags(0xC, 0x10)

    label("loc_1BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1BC5")
    ClearScenarioFlags(0x22, 0)
    Event(0, 50)
    Jump("loc_1C49")

    label("loc_1BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1BD9")
    ClearScenarioFlags(0x22, 1)
    Event(0, 96)
    Jump("loc_1C49")

    label("loc_1BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1BED")
    ClearScenarioFlags(0x22, 2)
    Event(0, 95)
    Jump("loc_1C49")

    label("loc_1BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_1C01")
    ClearScenarioFlags(0x22, 3)
    Event(0, 91)
    Jump("loc_1C49")

    label("loc_1C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_1C18")
    ClearScenarioFlags(0x22, 4)
    SetScenarioFlags(0x3, 0)
    Event(0, 56)
    Jump("loc_1C49")

    label("loc_1C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_1C2C")
    ClearScenarioFlags(0x22, 5)
    Event(0, 76)
    Jump("loc_1C49")

    label("loc_1C2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_1C49")
    ClearScenarioFlags(0x22, 6)
    SetChrPos(0x0, 19290, 0, 17220, 180)

    label("loc_1C49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C5A")
    Event(0, 75)

    label("loc_1C5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C85")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_1C85")

    Return()

    # Function_8_14AC end

    def Function_9_1C86(): pass

    label("Function_9_1C86")

    SoundDistance(0x7E, 0x13E3E, 0x0, 0xFFFF8972, 0x13880, 0xC350, 0x64, 0x0)
    OP_E3(0x13DE4, 0x0, 0x71E8)
    OP_E3(0x13C54, 0x0, 0xD1B0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D65")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x190, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_1D65")

    ClearMapObjFlags(0x4, 0x10)
    OP_70(0x4, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 4)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DB8")
    SetMapObjFlags(0x4, 0x10)
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DB8")
    ClearMapObjFlags(0x4, 0x10)
    OP_70(0x4, 0x0)
    OP_66(0x2, 0x1)

    label("loc_1DB8")

    OP_65(0x7, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DEF")
    OP_1B(0x2, 0x0, 0x68)
    OP_66(0x7, 0x1)
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)

    label("loc_1DEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1E11")
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    SetMapObjFrame(0xF, "light", 0x0, 0x1)

    label("loc_1E11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E65")
    ClearChrFlags(0x25, 0x80)
    OP_78(0xB, 0x25)
    SetChrPos(0x25, -21240, 0, 14350, 90)
    OP_D5(0x25, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)

    label("loc_1E65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EA6")
    ClearChrFlags(0x33, 0x80)
    OP_78(0xD, 0x33)
    SetChrPos(0x33, 40000, -4000, -22500, 90)
    OP_D5(0x33, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xD, 0x4)

    label("loc_1EA6")

    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x7, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1EFC")
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EFC")
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xF1, 0x12C, 0x0, 0x20)

    label("loc_1EFC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F15")
    ClearMapObjFlags(0x9, 0x4)
    Jump("loc_1F1B")

    label("loc_1F15")

    SetMapObjFlags(0x9, 0x4)

    label("loc_1F1B")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    ModifyEventFlags(0, 5, 0x80)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_END)), "loc_1F6E")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    OP_66(0x4, 0x1)
    OP_66(0x5, 0x1)
    OP_66(0x6, 0x1)

    label("loc_1F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1FA6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FA6")
    ModifyEventFlags(1, 4, 0x80)
    ModifyEventFlags(1, 5, 0x80)

    label("loc_1FA6")

    ModifyEventFlags(0, 6, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FCA")
    ModifyEventFlags(1, 6, 0x80)

    label("loc_1FCA")

    OP_52(0x1B, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x18, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2030")
    OP_65(0x1, 0x1)

    label("loc_2030")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 79890, -3500, 8810, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_208D")
    OP_70(0x8, 0x0)
    Jump("loc_2091")

    label("loc_208D")

    OP_70(0x8, 0x1E)

    label("loc_2091")

    Return()

    # Function_9_1C86 end

    def Function_10_2092(): pass

    label("Function_10_2092")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_218E")
    Sound(14, 0, 100, 0)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1D7, 1)"), scpexpr(EXPR_END)), "loc_2117")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_2189")

    label("loc_2117")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many,\x01",
            "you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2189")

    Jump("loc_21D7")

    label("loc_218E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the\x01",
            "chest.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_21D7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_2092 end

    def Function_11_21E3(): pass

    label("Function_11_21E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_23AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_231D")

    ChrTalk(
        0xFE,
        (
            "I was surprised by this sudden development,\x01",
            "but... If we don't make a show of strength,\x01",
            "won't the major powers make fun of us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why I strongly\x01",
            "support President\x01",
            "Dieter!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Secretary Arios is there... The\x01",
            "major powers won't be able to\x01",
            "do whatever they want any more!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_23AA")

    label("loc_231D")


    ChrTalk(
        0xFE,
        (
            "Of course I'm anxious.\x01",
            "But, I strongly support\x01",
            "President Dieter!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The major powers won't\x01",
            "be able to do whatever\x01",
            "they want any more!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23AA")

    Jump("loc_34E4")

    label("loc_23AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_25BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24FE")

    ChrTalk(
        0xFE,
        (
            "The riverside office was completely\x01",
            "destroyed... Rumor has it that it was because\x01",
            "of their connections to the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of that, I wonder if\x01",
            "the attack was by a jaeger\x01",
            "group employed by the Empire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That doesn't matter, but...\x01",
            "Anyway, I hope nothing\x01",
            "unnecessary happens to Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_25B6")

    label("loc_24FE")


    ChrTalk(
        0xFE,
        (
            "It's become like this because\x01",
            "Crossbell has always been a\x01",
            "subordinate state... right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why it's necessary to\x01",
            "show the surrounding countries\x01",
            "our will to be independent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25B6")

    Jump("loc_34E4")

    label("loc_25BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_27B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26EC")

    ChrTalk(
        0xFE,
        (
            "The CGF are having a tough\x01",
            "time fighting against that\x01",
            "armed group, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rumor has it that if Crossbell becomes independent,\x01",
            "the military will be strengthened so as to deal\x01",
            "with a situation like this without difficulty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell should be\x01",
            "independent ...right?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_27B3")

    label("loc_26EC")


    ChrTalk(
        0xFE,
        (
            "Rumor has it that if Crossbell becomes independent,\x01",
            "the military will be strengthened so as to deal\x01",
            "with a situation like this without difficulty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell should be\x01",
            "independent ...right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27B3")

    Jump("loc_34E4")

    label("loc_27B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_27C6")
    Jump("loc_34E4")

    label("loc_27C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_29CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2927")

    ChrTalk(
        0xFE,
        (
            "There are already a lot\x01",
            "of people who approve of\x01",
            "independence, even now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Hmm, but I still\x01",
            "don't know much about\x01",
            "the pros and cons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come to think of it, I heard a citizen's\x01",
            "forum with the theme of independence will be\x01",
            "held at City Meeting Hall tomorrow, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I should start\x01",
            "asking questions now?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_29C8")

    label("loc_2927")


    ChrTalk(
        0xFE,
        (
            "I heard a citizen's forum with the\x01",
            "theme of independence will be held at\x01",
            "City Meeting Hall tomorrow, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I should start\x01",
            "asking questions now?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29C8")

    Jump("loc_34E4")

    label("loc_29CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2A79")

    ChrTalk(
        0xFE,
        (
            "Come to think of it, the referendum\x01",
            "on independence will be held just a\x01",
            "week from today, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, what to do. I'll\x01",
            "have to make up my mind\x01",
            "soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34E4")

    label("loc_2A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2BBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B38")

    ChrTalk(
        0xFE,
        (
            "Uhuhu, the Arc-en-Ciel\x01",
            "renewal performance is\x01",
            "finally opening soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The additional cast was\x01",
            "finally revealed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can no longer take my\x01",
            "eyes off it!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2BB8")

    label("loc_2B38")


    ChrTalk(
        0xFE,
        (
            "The additional cast\x01",
            "member is a girl named\x01",
            "Sully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though she's still\x01",
            "Sunday School age...\x01",
            "Honestly, I'm shocked!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BB8")

    Jump("loc_34E4")

    label("loc_2BBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2D01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CAB")

    ChrTalk(
        0xFE,
        (
            "I hardly saw her, but Captain\x01",
            "Julia's awesomeness is such that\x01",
            "you wouldn't think she's military.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't mean it like\x01",
            "that, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to be hugged\x01",
            "tightly by an awesome\x01",
            "person like that㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2CFC")

    label("loc_2CAB")


    ChrTalk(
        0xFE,
        (
            "*sigh*, Captain Julia is\x01",
            "really lovely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want her to hug me\x01",
            "tightly㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CFC")

    Jump("loc_34E4")

    label("loc_2D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_32DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DA8")

    ChrTalk(
        0xFE,
        (
            "Earlier, an Eastern\x01",
            "woman walked toward East\x01",
            "Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She looked good in her\x01",
            "flowing long black hair and\x01",
            "suit. She was so cool...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32D6")

    label("loc_2DA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F29")

    ChrTalk(
        0xFE,
        (
            "I saw an Eastern woman\x01",
            "pass by just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She looked good in her\x01",
            "flowing long black hair and\x01",
            "suit. She was so cool...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(An Eastern woman with\x01",
            "black hair...?)\x02\x03",
            "#00001FUmm, which way did she\x01",
            "go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Um, I think she went to\x01",
            "East Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FEast Street...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F(I'm not sure if it's\x01",
            ""her" or not, but we\x01",
            "should check it out.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    SetScenarioFlags(0x1C6, 6)
    Jump("loc_32D6")

    label("loc_2F29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3257")

    ChrTalk(
        0xFE,
        (
            "She came from Liberl\x01",
            "Kingdom... Um, yeah,\x01",
            "Captain Julia Schwartz!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I saw a pin-up photo of\x01",
            "her, and instantly\x01",
            "became her fan!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm told she has a fan\x01",
            "club in Liberl... I wonder\x01",
            "if foreigners can join.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105FF-Fan club? That's the\x01",
            "first I've heard of it,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes, a certain magazine called\x01",
            "for it. Although it's unofficial,\x01",
            "I think it formed recently?\x02\x03",
            "#10102FThey send fan club members\x01",
            "Captain Julia's duty schedule as\x01",
            "well as precious photos!\x02\x03",
            "#10106FBut, it's too bad... It seems you\x01",
            "have to live in Liberl to join.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Aw, really!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FHmm. It really is too\x01",
            "bad.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x104)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00005F(Noｱl really knows her\x01",
            "stuff.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F(Yeah. Probably even\x01",
            "more than we think.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14B, 0)
    Jump("loc_32D6")

    label("loc_3257")


    ChrTalk(
        0xFE,
        (
            "I wanted to join Captain\x01",
            "Julia's fan club, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I-I wonder if I have any\x01",
            "distant relatives or\x01",
            "something in Liberl!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32D6")

    Jump("loc_34E4")

    label("loc_32DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3373")

    ChrTalk(
        0xFE,
        (
            "The trade conference is\x01",
            "finally tomorrow, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've only seen the VIPs in\x01",
            "magazines. They must have a\x01",
            "different aura in person.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34E4")

    label("loc_3373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3381")
    Jump("loc_34E4")

    label("loc_3381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_34E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3468")

    ChrTalk(
        0xFE,
        (
            "Mayor Dieter never\x01",
            "misses a beat, does he.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He is wise, just, dynamic and\x01",
            "full of ideas, and on top of that\x01",
            "he's wealthy and handsome...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, just saying that\x01",
            "made my head spin,\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_34E4")

    label("loc_3468")


    ChrTalk(
        0xFE,
        (
            "Mayor Dieter never\x01",
            "misses a beat, does he.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if he's worried\x01",
            "about things outside of\x01",
            "politics and finance?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34E4")

    TalkEnd(0xFE)
    Return()

    # Function_11_21E3 end

    def Function_12_34E8(): pass

    label("Function_12_34E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_351F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_351F")
    Call(0, 90)
    Return()

    label("loc_351F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A08")

    ChrTalk(
        0x1A2,
        "*sniff*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Hmm, this is a pretty\x01",
            "nice smell!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "Oh, young man! I see\x01",
            "that you understand the\x01",
            "goodness of our noodles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Yeah, more or less.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "I think it's on the\x01",
            "level of B-class\x01",
            "gourmet.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "Y-You would identify our\x01",
            "noodles as B-class!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Out with you! I've no\x01",
            "noodles to feed he\x01",
            "without a sense of value!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "Elie, did I say\x01",
            "something wrong?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_3810")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_3773():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3773)
    Sleep(50)

    def lambda_3783():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3783)
    Sleep(50)

    def lambda_3793():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3793)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00106FShing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FSaying things like this\x01",
            "will make everyone think\x01",
            "you're ignorant, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FD")

    label("loc_3810")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_3906")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_3869():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3869)
    Sleep(50)

    def lambda_3879():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3879)
    Sleep(50)

    def lambda_3889():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3889)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00106FShing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FSaying things like this\x01",
            "will make everyone think\x01",
            "you're ignorant, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FD")

    label("loc_3906")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_39FD")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_395F():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_395F)
    Sleep(50)

    def lambda_396F():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_396F)
    Sleep(50)

    def lambda_397F():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_397F)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00106FShing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHaha, saying things like this\x01",
            "will make everyone think\x01",
            "you're ignorant, you know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39FD")

    TalkEnd(0x9)
    SetScenarioFlags(0x1DC, 1)
    Jump("loc_3A8B")

    label("loc_3A08")


    ChrTalk(
        0x9,
        (
            "To think someone would\x01",
            "say my noodles are\x01",
            "B-class!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Out with you! I've no\x01",
            "noodles to feed he\x01",
            "without a sense of value!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)

    label("loc_3A8B")

    Return()

    label("loc_3A8C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3A96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C4B")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Shop\x01",        # 1
            "Cancel\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AE8")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3AE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B08")
    OP_AF(0x7B)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C46")

    label("loc_3B08")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B1C")
    Jump("loc_4C46")

    label("loc_3B1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C46")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_3BF7")

    ChrTalk(
        0xFE,
        (
            "Hehe. Among young men,\x01",
            "there are those with\x01",
            "promise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Use that recipe I gave\x01",
            "you, and set your sights\x01",
            "on supreme noodles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will be secretly\x01",
            "cheering for all of you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C46")

    label("loc_3BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3C93")

    ChrTalk(
        0xFE,
        (
            "Hmm, so it's finally\x01",
            "come to this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm already prepared for whatever\x01",
            "happens. Now that it's come to\x01",
            "this, we can only push ahead!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C46")

    label("loc_3C93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3D99")

    ChrTalk(
        0xFE,
        (
            "Over many years, my cart and I have experienced many\x01",
            "joys and sorrows, so it's quite a shock for it to be\x01",
            "destroyed. It can't be helped if I can't stay positive!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With this newly purchased\x01",
            "cart, I plan to do my best\x01",
            "to make a fresh start!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C46")

    label("loc_3D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3E24")

    ChrTalk(
        0xFE,
        (
            "It seems a bunch of\x01",
            "complete fools have\x01",
            "appeared at Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph, I want to splash\x01",
            "them with this piping\x01",
            "hot broth!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C46")

    label("loc_3E24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3F29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E8F")
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0xFE,
        "...Achoo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, it seems I'm coming\x01",
            "down with a cold.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3F24")

    label("loc_3E8F")


    ChrTalk(
        0xFE,
        (
            "Alright then, I suppose\x01",
            "I'll make a portion for\x01",
            "myself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By slurping noodles, both\x01",
            "body and soul become warm...\x01",
            "No, they become piping hot!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F24")

    Jump("loc_4C46")

    label("loc_3F29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_406C")

    ChrTalk(
        0xFE,
        (
            "Hmm? It seems my crushed\x01",
            "pepper supply has run\x01",
            "low.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. I've got to go buy\x01",
            "more somewhere when I\x01",
            "find a suitable time.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4067")

    ChrTalk(
        0x101,
        (
            "#00008F(I think we can get\x01",
            "coverage for the gourmet\x01",
            "guide here, but...)\x02\x03",
            "#00003F(Now's not the time.\x01",
            "Let's not forget to stop\x01",
            "by later.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4067")

    Jump("loc_4C46")

    label("loc_406C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_40DD")

    ChrTalk(
        0xFE,
        (
            "Hmm, today's noodles are\x01",
            "well made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've put my all into\x01",
            "them. Each as much as\x01",
            "you like!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C46")

    label("loc_40DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4258")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41D6")

    ChrTalk(
        0xFE,
        (
            "An independence proposal\x01",
            "is a drastic measure,\x01",
            "even for Mayor Dieter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, I see the\x01",
            "mayor's stance as\x01",
            "proactive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Right, in other words, survival\x01",
            "in everything one does is to\x01",
            "have just the bold mindset.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4253")

    label("loc_41D6")


    ChrTalk(
        0xFE,
        (
            "Without challenge, there is no success...\x01",
            "Hmm, so the essence of the worlds of\x01",
            "politics and noodles are the same, then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4253")

    Jump("loc_4C46")

    label("loc_4258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4364")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4326")

    ChrTalk(
        0xFE,
        (
            "A thousand customers\x01",
            "have a thousand stories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Through contact with customers, one part\x01",
            "of their story is revealed... This too is\x01",
            "one of the pleasures of running a cart.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_435F")

    label("loc_4326")


    ChrTalk(
        0xFE,
        (
            "An old man and his\x01",
            "granddaughter... How\x01",
            "harmonious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_435F")

    Jump("loc_4C46")

    label("loc_4364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_47FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4421")

    ChrTalk(
        0xFE,
        (
            "Just now, a bright suited\x01",
            "young man with red hair\x01",
            "had some of my noodles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Saying "Maybe I'll have\x01",
            "some dessert," he headed\x01",
            "for Entertainment District.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47F9")

    label("loc_4421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4694")

    ChrTalk(
        0xFE,
        (
            "Just now, a bright suited\x01",
            "young man with red hair had\x01",
            "some of my noodles, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He entered my cart from\x01",
            "behind, saying he'd disclose\x01",
            "my secret soup recipe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I almost succeeded in\x01",
            "driving him off, but...\x01",
            "What an unthinkable guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(A bright suited young\x01",
            "man...)\x02\x03",
            "#00006F(...His actions aside, I\x01",
            "feel like I'm reminded of a\x01",
            "certain character I know.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FWhere did he go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, he said "I think I'll\x01",
            "have some dessert" and headed\x01",
            "for Entertainment District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FEntertainment District.\x02\x03",
            "#00003F(...Though I can't be\x01",
            "sure it's him, shall we\x01",
            "chase after him?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 6)
    SetScenarioFlags(0x1C7, 1)
    Jump("loc_47F9")

    label("loc_4694")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4765")

    ChrTalk(
        0xFE,
        (
            "Hmm, now that the heads of state\x01",
            "have come to Crossbell, the\x01",
            "atmosphere is showy yet strict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know it's for security\x01",
            "reasons, but I can't help but be\x01",
            "concerned at officers' gazes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_47F9")

    label("loc_4765")


    ChrTalk(
        0xFE,
        (
            "The police stare at my cart\x01",
            "every so often. I wonder if\x01",
            "that's for security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goodness. If it's like\x01",
            "this, I can't\x01",
            "concentrate on my work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47F9")

    Jump("loc_4C46")

    label("loc_47FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_497D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48DE")

    ChrTalk(
        0xFE,
        (
            "Noodles have firmness!\x01",
            "And mouthfeel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let me just say this. My\x01",
            "noodles absolutely need\x01",
            "not be eaten elegantly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it is only by a\x01",
            "hearty slurp that their\x01",
            "flavor can be enjoyed!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4978")

    label("loc_48DE")


    ChrTalk(
        0xFE,
        (
            "Let me just say this. My\x01",
            "noodles absolutely need\x01",
            "not be eaten elegantly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it is only by a\x01",
            "hearty slurp that their\x01",
            "flavor can be enjoyed!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4978")

    Jump("loc_4C46")

    label("loc_497D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4AEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_END)), "loc_49E2")

    ChrTalk(
        0xFE,
        (
            "A girl with a pink\x01",
            "umbrella?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, I don't think she's\x01",
            "come this way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AE6")

    label("loc_49E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A86")

    ChrTalk(
        0xFE,
        (
            "The path of noodles is\x01",
            "perseverance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I shall not lose to this\x01",
            "trifling rain!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(I'm worried the rain\x01",
            "will get into his food.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4AE6")

    label("loc_4A86")


    ChrTalk(
        0xFE,
        (
            "Come now. Since you're here,\x01",
            "why not have a portion. It'll\x01",
            "warm your cold bodies right up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AE6")

    Jump("loc_4C46")

    label("loc_4AEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4C46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BEB")

    ChrTalk(
        0xFE,
        (
            "The path of noodles is\x01",
            "one day at a time... And\x01",
            "that path is unending.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And so, through research,\x01",
            "I'm finally able to offer my\x01",
            "new noodles at this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And its name? "Heavenly\x01",
            "Noodles <Sun>". You\x01",
            "should have some!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4C46")

    label("loc_4BEB")


    ChrTalk(
        0xFE,
        (
            "I have absolute pride in\x01",
            "my noodles this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am certain you'll be\x01",
            "satisfied.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C46")

    Jump("loc_3A96")

    label("loc_4C4B")

    TalkEnd(0xFE)
    Return()

    # Function_12_34E8 end

    def Function_13_4C4F(): pass

    label("Function_13_4C4F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4E01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D60")

    ChrTalk(
        0xFE,
        (
            "Because the trains were halted\x01",
            "this morning, I have\x01",
            "considerably fewer deliveries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Or rather, if things continue\x01",
            "like this, I wonder what's going\x01",
            "to happen to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's a lot more\x01",
            "important than some job,\x01",
            "isn't it...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4DFC")

    label("loc_4D60")


    ChrTalk(
        0xFE,
        (
            "Really. If things continue at\x01",
            "this rate, I don't know what's\x01",
            "going to happen to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's a lot more\x01",
            "important than some job,\x01",
            "isn't it...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DFC")

    Jump("loc_5623")

    label("loc_4E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4EB6")

    ChrTalk(
        0xFE,
        (
            "It's already been a week since the\x01",
            "attack, huh... I guess things are\x01",
            "finally settling down around here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, I hope nothing\x01",
            "like that ever happens\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5623")

    label("loc_4EB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4FD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F80")

    ChrTalk(
        0xFE,
        (
            "The CGF are fighting the armed\x01",
            "group at Mainz, but it looks like\x01",
            "they're having a tough time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Being independent with\x01",
            "our own military... I\x01",
            "suppose that's important.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4FCC")

    label("loc_4F80")


    ChrTalk(
        0xFE,
        (
            "Being independent with\x01",
            "our own military... I\x01",
            "suppose that's important.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FCC")

    Jump("loc_5623")

    label("loc_4FD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5107")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_506D")

    ChrTalk(
        0xFE,
        (
            "Wah!? The letters on the\x01",
            "address label disappeared\x01",
            "because of the rain!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "B-But well, I can make\x01",
            "them out somehow, yeah.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5102")

    label("loc_506D")


    ChrTalk(
        0xFE,
        (
            "Returning to HQ to check the\x01",
            "address for each one would be\x01",
            "a considerable loss of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, but rainy days\x01",
            "are tough in a lot of\x01",
            "ways.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5102")

    Jump("loc_5623")

    label("loc_5107")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5197")

    ChrTalk(
        0xFE,
        (
            "I looks like several ambulances\x01",
            "are going back and forth between\x01",
            "the station and West Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What could have\x01",
            "happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5623")

    label("loc_5197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_51E7")

    ChrTalk(
        0xFE,
        (
            "Alright, I'm fired up\x01",
            "today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "An efficient route,\x01",
            "hmm...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5623")

    label("loc_51E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_52C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5289")

    ChrTalk(
        0xFE,
        (
            "Now then, I'll think\x01",
            "I'll deliver two of\x01",
            "them, then have lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Alright, thinking about\x01",
            "it that way gives me\x01",
            "energy somehow!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_52BF")

    label("loc_5289")


    ChrTalk(
        0xFE,
        (
            "Just two more until\x01",
            "lunch! Two more until\x01",
            "lunch!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52BF")

    Jump("loc_5623")

    label("loc_52C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_53B6")

    ChrTalk(
        0xFE,
        (
            "During the trade conference, the police\x01",
            "said no deliveries for the new City\x01",
            "Hall building area would be allowed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because if there was a bomb or\x01",
            "something in a package, that wouldn't\x01",
            "be funny. Perfectly understandable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5623")

    label("loc_53B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_548C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5470")

    ChrTalk(
        0xFE,
        (
            "I couldn't deliver my\x01",
            "packages due to the VIPs'\x01",
            "visit this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But my workload is the same\x01",
            "a usual today... I've got\x01",
            "to make up the difference!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5487")

    label("loc_5470")


    ChrTalk(
        0xFE,
        "Dash! Dash! Dash!\x02",
    )

    CloseMessageWindow()

    label("loc_5487")

    Jump("loc_5623")

    label("loc_548C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5506")

    ChrTalk(
        0xFE,
        (
            "There's a lot of police\x01",
            "officers on patrol, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I've got to be\x01",
            "careful not to bump into\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5623")

    label("loc_5506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_55D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_END)), "loc_5553")

    ChrTalk(
        0xFE,
        (
            "Sorry, but I'm working.\x01",
            "I haven't seen any girl.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55CC")

    label("loc_5553")


    ChrTalk(
        0xFE,
        (
            "Hehe. Rain or a storm?\x01",
            "Bring it on!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...That's what I want to\x01",
            "say, but I wish this storm\x01",
            "would give me a break.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55CC")

    Jump("loc_5623")

    label("loc_55D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5623")

    ChrTalk(
        0xFE,
        (
            "*sigh*, busy, busy...\x01",
            "Being a deliveryman\x01",
            "challenges one's stamina.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5623")

    TalkEnd(0xFE)
    Return()

    # Function_13_4C4F end

    def Function_14_5627(): pass

    label("Function_14_5627")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5774")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5712")

    ChrTalk(
        0xFE,
        (
            "What a foolish address...\x01",
            "The world may be deceived,\x01",
            "but I shall not be!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Independent nation this, State Guard that!\x01",
            "Does he really believe we can hold on\x01",
            "against the threat of the major powers!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_576F")

    label("loc_5712")


    ChrTalk(
        0xFE,
        (
            "Goddess... Someone like\x01",
            "me matters not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But please, save my\x01",
            "granddaughter Amisaah!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_576F")

    Jump("loc_5E2F")

    label("loc_5774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_581A")

    ChrTalk(
        0xFE,
        (
            "Back then, if Amisaah and\x01",
            "I had been just a little\x01",
            "too late in escaping...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I can't help but feel\x01",
            "afraid when I think\x01",
            "about that, even now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E2F")

    label("loc_581A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_587B")

    ChrTalk(
        0xFE,
        (
            "Goodness, how sad. Just what\x01",
            "will tormenting the people\x01",
            "of Mainz accomplish!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E2F")

    label("loc_587B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_591B")

    ChrTalk(
        0xFE,
        (
            "Hmm, so that thing I see\x01",
            "in the distance is called\x01",
            "a ferris wheel, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Say, Amisaah. Want to\x01",
            "go to the theme park\x01",
            "with your old man?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E2F")

    label("loc_591B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_597B")

    ChrTalk(
        0xFE,
        (
            "Wahahaha, what do you\x01",
            "think of that, Amisaah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Isn't your grandpa\x01",
            "great?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E2F")

    label("loc_597B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_59CA")

    ChrTalk(
        0xFE,
        "Wait! Amisaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This old man caught a\x01",
            "big one just now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E2F")

    label("loc_59CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_59D8")
    Jump("loc_5E2F")

    label("loc_59D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5A47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59F3")
    Call(0, 15)
    Jump("loc_5A42")

    label("loc_59F3")


    ChrTalk(
        0xFE,
        (
            "Amisaah is truly a kind\x01",
            "and good child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...It makes my cry,\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A42")

    Jump("loc_5E2F")

    label("loc_5A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5BBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B1D")

    ChrTalk(
        0xFE,
        (
            "The police said to refrain\x01",
            "from fishing during the\x01",
            "trade conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, it's fun viewing the city\x01",
            "with my granddaughter like\x01",
            "this every once in a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_93(0xB, 0x2D, 0x0)
    SetChrFlags(0xB, 0x10)
    Jump("loc_5B57")

    label("loc_5B1D")


    ChrTalk(
        0xFE,
        (
            "Oh, what have we here.\x01",
            "So that's called a\x01",
            "Mishy, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B57")

    Jump("loc_5BB8")

    label("loc_5B5C")


    ChrTalk(
        0xFE,
        (
            "Hmm. It must be fun,\x01",
            "dancing like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It would be fine if I\x01",
            "was younger, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BB8")

    Jump("loc_5E2F")

    label("loc_5BBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5D67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CA4")

    ChrTalk(
        0xFE,
        (
            "I don't know if it's for the\x01",
            "trade conference, but those\x01",
            "police really stand out.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        "...Ah, I mustn't.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Amisaah told me not to\x01",
            "complain again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_5D62")

    label("loc_5CA4")


    ChrTalk(
        0xFE,
        (
            "According to Amisaah,\x01",
            "complaining isn't good\x01",
            "for your health.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Setting aside whether it's correct, I\x01",
            "don't want to see Amisaah's sad face.\x01",
            "I'll try not to say anything unnecessary.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D62")

    Jump("loc_5E2F")

    label("loc_5D67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5D75")
    Jump("loc_5E2F")

    label("loc_5D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5E2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D90")
    Call(0, 16)
    Jump("loc_5E2F")

    label("loc_5D90")


    ChrTalk(
        0xFE,
        (
            "I detest both the world\x01",
            "and hospitals... I love\x01",
            "only my granddaughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of that, I've decided\x01",
            "to listen to what she says as\x01",
            "much as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E2F")

    TalkEnd(0xFE)
    Return()

    # Function_14_5627 end

    def Function_15_5E33(): pass

    label("Function_15_5E33")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xB,
        (
            "*blowing*... These\x01",
            "noodles are hard to eat\x01",
            "when they're hot.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 500)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "C'mon grandpa! Don't be\x01",
            "in such a rush.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Oh yeah! Amisaah will\x01",
            "blow on them for you.\x01",
            "One moment please♪\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xC, 500)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "*blowing*... Alright,\x01",
            "eat up♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh... Thank you,\x01",
            "Amisaah.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x0, 0x0)
    OP_93(0xC, 0x0, 0x0)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_15_5E33 end

    def Function_16_5F6D(): pass

    label("Function_16_5F6D")


    ChrTalk(
        0xC,
        (
            "Grandpa, I brought your\x01",
            "medicine today, ok.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmm, thank you as\x01",
            "always. I'll take it\x01",
            "later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That won't do. I know you\x01",
            "don't take it sometimes when\x01",
            "I take my eyes off you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'll watch you take it\x01",
            "with your meal today,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I-I see... You always\x01",
            "see things through,\x01",
            "Amisaah.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_16_5F6D end

    def Function_17_60A5(): pass

    label("Function_17_60A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6120")

    ChrTalk(
        0xFE,
        (
            "Like my grandfather\x01",
            "says, this has become a\x01",
            "real war, I guess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hate that! And I'm\x01",
            "scared...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64EC")

    label("loc_6120")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_616C")

    ChrTalk(
        0xFE,
        (
            "The red building that\x01",
            "was there... It's\x01",
            "completely gone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64EC")

    label("loc_616C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_61B0")

    ChrTalk(
        0xFE,
        (
            "Grandpa, getting\x01",
            "irritated isn't good for\x01",
            "you...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64EC")

    label("loc_61B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_61F8")

    ChrTalk(
        0xFE,
        (
            "Eh? Are you sure,\x01",
            "grandpa!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yay! I'm so happy♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_64EC")

    label("loc_61F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6252")

    ChrTalk(
        0xFE,
        "Yup!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And that fish was a big\x01",
            "one. I'm looking forward\x01",
            "to dinner♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64EC")

    label("loc_6252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_62CA")

    ChrTalk(
        0xFE,
        (
            "There was a big movement\x01",
            "on grandpa's rod just\x01",
            "now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So excited... I wonder\x01",
            "if he'll get a fish.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64EC")

    label("loc_62CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_62D8")
    Jump("loc_64EC")

    label("loc_62D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6336")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62F3")
    Call(0, 15)
    Jump("loc_6331")

    label("loc_62F3")


    ChrTalk(
        0xFE,
        "Grandpa, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are you sad about\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6331")

    Jump("loc_64EC")

    label("loc_6336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_63DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6384")

    ChrTalk(
        0xFE,
        "Look at this, grandpa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Mishy's in the park!\x02",
    )

    CloseMessageWindow()
    Jump("loc_63D6")

    label("loc_6384")

    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Grandpa, dance with\x01",
            "Amisaah!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "H-Hmm... That would be\x01",
            "hard on me.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)

    label("loc_63D6")

    Jump("loc_64EC")

    label("loc_63DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_63E9")
    Jump("loc_64EC")

    label("loc_63E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_63F7")
    Jump("loc_64EC")

    label("loc_63F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_64EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6412")
    Call(0, 16)
    Jump("loc_64EC")

    label("loc_6412")


    ChrTalk(
        0xFE,
        (
            "I kept asking him, and recently\x01",
            "my stubborn grandpa finally\x01",
            "started taking his medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are times when he\x01",
            "doesn't if I don't watch\x01",
            "him, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ehehe. I'm glad I didn't\x01",
            "give up and kept asking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64EC")

    TalkEnd(0xFE)
    Return()

    # Function_17_60A5 end

    def Function_18_64F0(): pass

    label("Function_18_64F0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_65C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65A8")

    ChrTalk(
        0xFE,
        "Eh, oh! Eh, oh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Renewal performance\x01",
            "opening night is finally\x01",
            "tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not the case that I\x01",
            "can calm down because of\x01",
            "the rain, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_65BD")

    label("loc_65A8")


    ChrTalk(
        0xFE,
        "Eh, oh! Eh, oh!\x02",
    )

    CloseMessageWindow()

    label("loc_65BD")

    Jump("loc_66CA")

    label("loc_65C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6671")

    ChrTalk(
        0xFE,
        "Eh, oh! Eh, oh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say it's important\x01",
            "to rest, but I just\x01",
            "can't sit still.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And when I move my body,\x01",
            "I don't think about\x01",
            "unnecessary things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_66CA")

    label("loc_6671")


    ChrTalk(
        0xFE,
        "Eh, oh! Eh, oh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, whenever I run\x01",
            "outside lately, it's\x01",
            "been with Celine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66CA")

    TalkEnd(0xFE)
    Return()

    # Function_18_64F0 end

    def Function_19_66CE(): pass

    label("Function_19_66CE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6775")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6734")

    ChrTalk(
        0xFE,
        "I-I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't intend to lose.\x01",
            "Neither to Nikol nor to\x01",
            "Sully.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6770")

    label("loc_6734")


    ChrTalk(
        0xFE,
        (
            "I don't intend to lose.\x01",
            "Neither to Nikol nor to\x01",
            "Sully.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6770")

    Jump("loc_67AC")

    label("loc_6775")


    ChrTalk(
        0xFE,
        (
            "That Nikol... I can't\x01",
            "let him get the jump on\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67AC")

    TalkEnd(0xFE)
    Return()

    # Function_19_66CE end

    def Function_20_67B0(): pass

    label("Function_20_67B0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_684D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6816")

    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Hi everyone~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi! Let's have fun\x01",
            "today everyone~☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6848")

    label("loc_6816")


    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi! Let's have fun\x01",
            "today everyone~☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6848")

    Jump("loc_68C3")

    label("loc_684D")


    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi! That guy was a\x01",
            "lot of fun, huh~☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "I'd love it if he danced\x01",
            "with me at Wonderland\x01",
            "next time~☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68C3")

    TalkEnd(0xFE)
    Return()

    # Function_20_67B0 end

    def Function_21_68C7(): pass

    label("Function_21_68C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6953")

    ChrTalk(
        0xFE,
        (
            "Be brought Mishy to\x01",
            "Crossbell today~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've got a lot of events\x01",
            "ready for you, so please\x01",
            "enjoy them, everyone~!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69CB")

    label("loc_6953")


    ChrTalk(
        0xFE,
        (
            "Ah, I'm surprised. To\x01",
            "think he danced so well\x01",
            "with Mishy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I should try\x01",
            "scouting him while we're\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69CB")

    TalkEnd(0xFE)
    Return()

    # Function_21_68C7 end

    def Function_22_69CF(): pass

    label("Function_22_69CF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A6F")

    ChrTalk(
        0xFE,
        (
            "Uhuhu, Mishy's dance\x01",
            "show will begin\x01",
            "shortly~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And in today's special event,\x01",
            "you can dance next to Mishy!\x01",
            "Please participate, ok~!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B11")

    label("loc_6A6F")


    ChrTalk(
        0xFE,
        (
            "That blond man started by\x01",
            "playing Mishy's dance BGM\x01",
            "with his violin, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the middle of it, he\x01",
            "danced with Mishy personally.\x01",
            "Haha, what a fun guy!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B11")

    TalkEnd(0xFE)
    Return()

    # Function_22_69CF end

    def Function_23_6B15(): pass

    label("Function_23_6B15")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6B63")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B5E")

    ChrTalk(
        0xFE,
        (
            "Beach, beach! I want to\x01",
            "swim on the beach!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B5E")

    Jump("loc_6BC2")

    label("loc_6B63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B93")

    ChrTalk(
        0xFE,
        (
            "Uwah~, it's the real\x01",
            "Mishy!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BC2")

    label("loc_6B93")


    ChrTalk(
        0xFE,
        (
            "I want to dance with\x01",
            "Mishy too this time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BC2")

    TalkEnd(0xFE)
    Return()

    # Function_23_6B15 end

    def Function_24_6BC6(): pass

    label("Function_24_6BC6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C17")

    ChrTalk(
        0xFE,
        (
            "So excited... I wonder\x01",
            "if the dance show's\x01",
            "starting soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C76")

    label("loc_6C17")


    ChrTalk(
        0xFE,
        (
            "That blond guy was\x01",
            "pretty cool, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But he doesn't hold a\x01",
            "candle to Mishy! Uhuhu.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C76")

    TalkEnd(0xFE)
    Return()

    # Function_24_6BC6 end

    def Function_25_6C7A(): pass

    label("Function_25_6C7A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6CD3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CCE")

    NpcTalk(
        0xFE,
        "Passenger",
        (
            "I'm looking forward to\x01",
            "the arcade boutique.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CCE")

    Jump("loc_6D3F")

    label("loc_6CD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D0A")

    ChrTalk(
        0xFE,
        (
            "Hey! Calm down and look\x01",
            "over here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D3F")

    label("loc_6D0A")


    ChrTalk(
        0xFE,
        (
            "It looks like the kids\x01",
            "are having a lot of fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D3F")

    TalkEnd(0xFE)
    Return()

    # Function_25_6C7A end

    def Function_26_6D43(): pass

    label("Function_26_6D43")

    TalkBegin(0xFE)

    NpcTalk(
        0xFE,
        "Passenger",
        (
            "Haha, you're a kid too,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_6D43 end

    def Function_27_6D76(): pass

    label("Function_27_6D76")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6E27")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6DCF")

    ChrTalk(
        0xFE,
        (
            "It looked like she loved\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm so glad we came.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E22")

    label("loc_6DCF")


    NpcTalk(
        0xFE,
        "Citizen",
        (
            "Ah, I'm looking forward\x01",
            "to this. I want to visit\x01",
            "the theme park soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E22")

    Jump("loc_6F02")

    label("loc_6E27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E99")

    ChrTalk(
        0xFE,
        (
            "So this is the rumored\x01",
            "Mishy, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "His loose facial\x01",
            "expression is simply\x01",
            "irresistible!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F02")

    label("loc_6E99")


    ChrTalk(
        0xFE,
        (
            "Mishy can really dance\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought he looked like\x01",
            "a stuffed animal and\x01",
            "looked down on him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F02")

    TalkEnd(0xFE)
    Return()

    # Function_27_6D76 end

    def Function_28_6F06(): pass

    label("Function_28_6F06")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6F4D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6F48")

    ChrTalk(
        0xFE,
        (
            "Uhuhu, I bought a lot of\x01",
            "souvenirs☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F48")

    Jump("loc_702E")

    label("loc_6F4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FD0")

    ChrTalk(
        0xFE,
        (
            "Even though Wonderland's\x01",
            "closed, I'm lucky to see\x01",
            "him in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like I've\x01",
            "become a Mishy fan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_702E")

    label("loc_6FD0")


    ChrTalk(
        0xFE,
        (
            "I've become a complete\x01",
            "Mishy fan!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have to buy a lot\x01",
            "of souvenirs to take\x01",
            "home!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_702E")

    TalkEnd(0xFE)
    Return()

    # Function_28_6F06 end

    def Function_29_7032(): pass

    label("Function_29_7032")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7049")
    Call(0, 47)
    Return()

    label("loc_7049")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_29_7032 end

    def Function_30_7050(): pass

    label("Function_30_7050")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7085")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7082")
    Call(0, 61)
    Jump("loc_7085")

    label("loc_7082")

    Call(0, 69)

    label("loc_7085")

    Return()

    # Function_30_7050 end

    def Function_31_7086(): pass

    label("Function_31_7086")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70A9")
    Call(0, 70)

    label("loc_70A9")

    Return()

    # Function_31_7086 end

    def Function_32_70AA(): pass

    label("Function_32_70AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_70E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70C8")
    Call(0, 34)
    Jump("loc_70DF")

    label("loc_70C8")


    ChrTalk(
        0x1B,
        "#01200FGrrrowl...\x02",
    )

    CloseMessageWindow()

    label("loc_70DF")

    Jump("loc_710F")

    label("loc_70E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_70F5")
    Jump("loc_710F")

    label("loc_70F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_7106")
    Jump("loc_710F")

    label("loc_7106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_710F")

    label("loc_710F")

    TalkEnd(0xFE)
    Return()

    # Function_32_70AA end

    def Function_33_7113(): pass

    label("Function_33_7113")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_71C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7131")
    Call(0, 34)
    Jump("loc_71C3")

    label("loc_7131")


    ChrTalk(
        0x1C,
        (
            "#01109FOkay, Zeit. Jump over\x01",
            "Shizuku this time!\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x1B, 0xFF)

    ChrTalk(
        0x1B,
        "#01203FGrrrowl... Woof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#01106F..."It's dangerous so I\x01",
            "won't"? Hmm, I see.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1B, 0xFF)

    label("loc_71C3")

    Jump("loc_71F3")

    label("loc_71C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_71D9")
    Jump("loc_71F3")

    label("loc_71D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_71EA")
    Jump("loc_71F3")

    label("loc_71EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_71F3")

    label("loc_71F3")

    TalkEnd(0xFE)
    Return()

    # Function_33_7113 end

    def Function_34_71F7(): pass

    label("Function_34_71F7")

    OP_4B(0x1C, 0xFF)
    OP_4B(0x1D, 0xFF)
    OP_4B(0x1B, 0xFF)

    ChrTalk(
        0x1C,
        (
            "#01100FAlright Shizuku, go\x01",
            "ahead and try it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#06005FYeah, umm...\x02\x03",
            "#06000F...Zeit, give me your\x01",
            "hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#01200FWoof. (*paws*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#06005FWah... Zeit is really\x01",
            "smart.\x02\x03",
            "#06002FHaha, and his paw pads\x01",
            "are really soft.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#01109FI know, right?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    OP_4C(0x1C, 0xFF)
    OP_4C(0x1D, 0xFF)
    OP_4C(0x1B, 0xFF)
    Return()

    # Function_34_71F7 end

    def Function_35_7311(): pass

    label("Function_35_7311")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_738A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_732F")
    Call(0, 34)
    Jump("loc_7385")

    label("loc_732F")


    ChrTalk(
        0x1D,
        (
            "#06002FHaha, you're really\x01",
            "smart, aren't you, Zeit?\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x1B, 0xFF)

    ChrTalk(
        0x1B,
        "#01200F...Woof.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x1B, 0xFF)

    label("loc_7385")

    Jump("loc_73B5")

    label("loc_738A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_739B")
    Jump("loc_73B5")

    label("loc_739B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_73AC")
    Jump("loc_73B5")

    label("loc_73AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_73B5")

    label("loc_73B5")

    TalkEnd(0xFE)
    Return()

    # Function_35_7311 end

    def Function_36_73B9(): pass

    label("Function_36_73B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_END)), "loc_7439")

    ChrTalk(
        0xFE,
        (
            "Since we're here we\x01",
            "decided to stop by\x01",
            "Michelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I wonder how much\x01",
            "of it we'll be able to\x01",
            "see.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74DA")

    label("loc_7439")


    ChrTalk(
        0xFE,
        (
            "Haha. Crossbell has a\x01",
            "totally different atmosphere\x01",
            "depending on the location.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was noisy over in\x01",
            "Entertainment District, but\x01",
            "it's pretty chill here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74DA")

    TalkEnd(0xFE)
    Return()

    # Function_36_73B9 end

    def Function_37_74DE(): pass

    label("Function_37_74DE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_END)), "loc_7538")

    ChrTalk(
        0xFE,
        (
            "We decided to go to\x01",
            "Michelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to ride the\x01",
            "Ferris wheel!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7590")

    label("loc_7538")


    ChrTalk(
        0xFE,
        (
            "Hey mom... This place is\x01",
            "boring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's hurry and go back\x01",
            "to that shiny place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7590")

    TalkEnd(0xFE)
    Return()

    # Function_37_74DE end

    def Function_38_7594(): pass

    label("Function_38_7594")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_76E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_765E")

    ChrTalk(
        0xFE,
        (
            "There's no such thing as\x01",
            "unending rain... And no such\x01",
            "thing as a forever cloudy sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Things won't be\x01",
            "settled just by saying\x01",
            "positive things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_76DF")

    label("loc_765E")


    ChrTalk(
        0xFE,
        (
            "There is no such thing as\x01",
            "unending rain... And no such\x01",
            "thing as an ever-full stomach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Hey, that made it\x01",
            "even worse.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76DF")

    Jump("loc_77A8")

    label("loc_76E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_77A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_END)), "loc_774C")

    ChrTalk(
        0xFE,
        (
            "A girl with an\x01",
            "umbrella...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I saw one just\x01",
            "now... or maybe not.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77A8")

    label("loc_774C")


    ChrTalk(
        0xFE,
        (
            "Just what shape do\x01",
            "raindrops have, I\x01",
            "wonder...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Maybe I can see it if\x01",
            "I squint?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77A8")

    TalkEnd(0xFE)
    Return()

    # Function_38_7594 end

    def Function_39_77AC(): pass

    label("Function_39_77AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78CA")

    ChrTalk(
        0xFE,
        (
            "Before long, the heads of\x01",
            "state will depart for\x01",
            "Michelam from right here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're now going over our\x01",
            "blockade structure for when\x01",
            "they're in the tower again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have business in\x01",
            "the business district,\x01",
            "finish it quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, understood.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_796B")

    label("loc_78CA")


    ChrTalk(
        0xFE,
        (
            "We'll re-renter our blockade\x01",
            "formation once the heads of\x01",
            "state arrive from Michelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have business in\x01",
            "the business district,\x01",
            "finish it quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_796B")

    TalkEnd(0xFE)
    Return()

    # Function_39_77AC end

    def Function_40_796F(): pass

    label("Function_40_796F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7A1E")

    ChrTalk(
        0xFE,
        (
            "Terrorists, huh... Though we\x01",
            "thought about them before,\x01",
            "it's likely they'll come here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well anyway, all we can\x01",
            "do is proceed per\x01",
            "direction from HQ.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BB3")

    label("loc_7A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7AE2")

    ChrTalk(
        0xFE,
        (
            "An event featuring\x01",
            "Mishy, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well they got proper\x01",
            "permission from the city,\x01",
            "so I don't see a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But this must be what\x01",
            "they call the MWL\x01",
            "service spirit, huh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BB3")

    label("loc_7AE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7BB3")

    ChrTalk(
        0xFE,
        (
            "Investigation into the actions of Heiyue is\x01",
            "outside the jurisdiction of the Patrol Division,\x01",
            "but... We of course need to remain on guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I don't think\x01",
            "they'll do anything\x01",
            "publically.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BB3")

    TalkEnd(0xFE)
    Return()

    # Function_40_796F end

    def Function_41_7BB7(): pass

    label("Function_41_7BB7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7D03")

    ChrTalk(
        0xFE,
        (
            "Though the Heiyue office was completely\x01",
            "destroyed, it looks like this place was\x01",
            "mostly repaired in just a week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And because of the upcoming\x01",
            "referendum, it seems not that\x01",
            "many citizens are depressed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think we'll feel the power of\x01",
            "those who make up their minds at\x01",
            "the last minute, for some reason.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F74")

    label("loc_7D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7DB5")

    ChrTalk(
        0xFE,
        (
            "Some of them are in the city,\x01",
            "but most of the heads of\x01",
            "state are still at Michelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's talk of terrorists\x01",
            "too. We need to pay\x01",
            "attention to security.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F74")

    label("loc_7DB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7E7B")

    ChrTalk(
        0xFE,
        (
            "It seems Chancellor Osborne is\x01",
            "visiting Michelam and President\x01",
            "Rocksmith is visiting IBC...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're each under heavy\x01",
            "guard. No need to worry about\x01",
            "either for now, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F74")

    label("loc_7E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7F74")

    ChrTalk(
        0xFE,
        (
            "I'm standing by here so I\x01",
            "can rush in with my patrol\x01",
            "car if anything happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though it won't stand up to the\x01",
            "CGF's armored cars, it's tough and\x01",
            "equipped with bulletproof glass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If necessary, it can\x01",
            "also be used as a\x01",
            "shield.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F74")

    TalkEnd(0xFE)
    Return()

    # Function_41_7BB7 end

    def Function_42_7F78(): pass

    label("Function_42_7F78")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_804B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7FEE")

    ChrTalk(
        0x24,
        (
            "Thank you for using the\x01",
            "water bus today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "We'll be waiting for\x01",
            "your next visit!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8046")

    label("loc_7FEE")


    ChrTalk(
        0x24,
        (
            "Water bus bound for\x01",
            "Michelam, departing\x01",
            "shooortlyyy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        "All passengers aboooard!\x02",
    )

    CloseMessageWindow()

    label("loc_8046")

    Jump("loc_80D5")

    label("loc_804B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_END)), "loc_80D5")

    ChrTalk(
        0xFE,
        (
            "The Michelam-bound water\x01",
            "bus will be arriving\x01",
            "shortly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll now begin the\x01",
            "boarding process. Line\x01",
            "up and wait, please.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80D5")

    TalkEnd(0xFE)
    Return()

    # Function_42_7F78 end

    def Function_43_80D9(): pass

    label("Function_43_80D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_826E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81D5")

    ChrTalk(
        0xFE,
        (
            "The city's on high alert,\x01",
            "but... It's strangely\x01",
            "calm like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just what kind of storm\x01",
            "will the heat of the\x01",
            "trade conference create?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It might not be too bad\x01",
            "to spend the day lost in\x01",
            "idle thought like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_826E")

    label("loc_81D5")


    ChrTalk(
        0xFE,
        (
            "Just what kind of storm\x01",
            "will the heat of the\x01",
            "trade conference create?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It might not be too bad\x01",
            "to spend the day lost in\x01",
            "idle thought like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_826E")

    TalkEnd(0xFE)
    Return()

    # Function_43_80D9 end

    def Function_44_8272(): pass

    label("Function_44_8272")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_836F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8367")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked and\x01",
            "there's a message plate.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Heiyue Trading Company - Crossbell Branch\x01",
            "※Please knock if you have business.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_836A")

    label("loc_8367")

    Call(0, 72)

    label("loc_836A")

    Jump("loc_87C9")

    label("loc_836F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_86BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85EE")
    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(20370, 0, 19380, 0)
    MoveCamera(44, 25, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(20290, 0)
    SetChrPos(0x101, 18600, 0, 17800, 0)
    SetChrPos(0x102, 19700, 0, 17800, 0)
    SetChrPos(0x109, 18600, 0, 16600, 0)
    SetChrPos(0x105, 19700, 0, 16600, 0)
    SetChrPos(0x104, 19100, 0, 15400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked and\x01",
            "there's a message plate.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Heiyue Trading Company - Crossbell Branch\x01",
            "※Please knock if you have business.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00003F...Looks like we're out\x01",
            "of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FGuess so. Let's give up\x01",
            "and go somewhere else.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CB, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest "Showing Shing\x01",
            "Around"\x07\x00",
            " failed...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x73, 0x1, 0xF)
    OP_29(0x73, 0x4, 0x40)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 18910, 0, 13080, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Jump("loc_86B5")

    label("loc_85EE")

    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked and\x01",
            "there's a message plate.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Heiyue Trading Company - Crossbell Branch\x01",
            "※Please knock if you have business.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_86B5")

    Jump("loc_87C9")

    label("loc_86BA")

    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked and\x01",
            "there's a message plate.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Heiyue Trading Company - Crossbell Branch\x01",
            "※Please knock if you have business.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_87C9")

    ChrTalk(
        0x101,
        (
            "#00003FWe can't really enter a\x01",
            "place like this...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87C9")

    TalkEnd(0xFF)
    Return()

    # Function_44_8272 end

    def Function_45_87CD(): pass

    label("Function_45_87CD")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89CD")

    ChrTalk(
        0x1A2,
        (
            "Hmm, Crossbell Times,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "...Oh yeah, our company\x01",
            "is in this same\x01",
            "Waterfront Area.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_885D():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_885D)

    def lambda_886A():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_886A)

    ChrTalk(
        0x101,
        "#00005F? Did you say something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Hmph, not really.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "If pushed, I'd say I really\x01",
            "can't like the reporters\x01",
            "who snoop around our place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Even Republic financiers\x01",
            "order their finance magazine,\x01",
            "so that of course has value.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F(Hmm, what to say...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(For a boy his age, he\x01",
            "has a good sense for\x01",
            "such things.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_8A1A")

    label("loc_89CD")


    ChrTalk(
        0x1A2,
        (
            "Crossbell News will\x01",
            "probably turn us away,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Let's get going.\x02",
    )

    CloseMessageWindow()

    label("loc_8A1A")

    TalkEnd(0xFF)
    Return()

    # Function_45_87CD end

    def Function_46_8A1E(): pass

    label("Function_46_8A1E")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            "#0000FIt seems we can fish\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(75920, 0, 7460, 1500)
    MoveCamera(45, 24, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(11500, 1500)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fish?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Fish\x01",        # 0
            "Cancel\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AE0")
    OP_E2(0x2)
    MiniGame(0x6, 0x1, 0x14226, 0xFFFFF63C, 0x3AA2, 0xB4, 0x13812, 0xFFFFF254, 0x226A)

    label("loc_8AE0")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_46_8A1E end

    def Function_47_8AE5(): pass

    label("Function_47_8AE5")

    EventBegin(0x0)
    SoundLoad(483)
    Fade(500)
    OP_68(41500, -1500, -18000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, 40400, -2500, -18600, 90)
    SetChrPos(0x102, 40200, -2500, -17400, 90)
    SetChrPos(0x103, 39300, -2500, -18600, 90)
    SetChrPos(0x104, 39100, -2500, -17400, 90)
    SetChrPos(0x109, 41400, -2500, -15600, 135)
    SetChrPos(0x105, 40200, -2500, -15600, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x18, 0xFF)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F68")

    ChrTalk(
        0x18,
        (
            "#11POh, you're the Special\x01",
            "Support Section, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYes. Thanks for your\x01",
            "hard work in this rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#6PThanks for getting this\x01",
            "ready for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PNo, no, this is my job,\x01",
            "you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11POh yeah, are you all\x01",
            "right operating it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PI can operate it for you\x01",
            "if necessary, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00008FOh right, I forgot about\x01",
            "that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#6PWell, if you can drive a\x01",
            "car, I don't think you'd\x01",
            "have much trouble with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00200FShould we contact chief?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        (
            "#5P#10105FNo, it's fine.\x02\x03",
            "#10100FI have experience\x01",
            "operating this kind of\x01",
            "boat, you see.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8E05():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8E05)
    Sleep(50)

    def lambda_8E15():
        TurnDirection(0x104, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8E15)
    Sleep(50)

    def lambda_8E25():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8E25)
    Sleep(50)

    def lambda_8E35():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8E35)
    Sleep(50)

    def lambda_8E45():
        TurnDirection(0x103, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8E45)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x101,
        "#12P#00002FOh really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00309FHaha, that's our Noｱl!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FLooks like cars and\x01",
            "boats aren't all that\x01",
            "different, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10112FHaha, this too is thanks\x01",
            "to Commander Sonya's\x01",
            "training.\x02\x03",
            "#10100FSo what do we do? Is it\x01",
            "time to board?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x165, 1)
    Jump("loc_8FAC")

    label("loc_8F68")

    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        (
            "#5P#10100FSo what do we do? Is it\x01",
            "time to board?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    label("loc_8FAC")


    ChrTalk(
        0x101,
        (
            "#12P#00003FLet's see...\x02\x03",
            "#00008F(We have no idea what's out\x01",
            "there. Also, I wonder if we've\x01",
            "left anything undone here.)\x02",
        )
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Once you board the boat for\x01",
            "Marshlands, you will not be able to\x01",
            "leave for the rest of the chapter.\x02\x03",
            "Quests and activities will close,\x01",
            "so please be aware of that.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[We Have Other Things to Do]\x01",      # 0
            "[Head for the marshlands]\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_9163"),
        (0, "loc_9354"),
        (SWITCH_DEFAULT, "loc_93DA"),
    )


    label("loc_9163")


    ChrTalk(
        0x109,
        "#5P#10102FRoger that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell then, be careful\x01",
            "out there.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("apl/ch51104.itc", 0x28)
    LoadEffect(0x0, "event\\ev315_00.eff")
    SetChrChipByIndex(0x109, 0x28)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x109, 41600, -3700, -22500, 90)
    SetChrPos(0x101, 41200, -3700, -23500, 90)
    SetChrPos(0x102, 40200, -3100, -21700, 90)
    SetChrPos(0x103, 39200, -3100, -23700, 90)
    SetChrPos(0x104, 38400, -3100, -22500, 90)
    SetChrPos(0x105, 38400, -3100, -21500, 90)
    SetChrFlags(0x18, 0x8000)

    def lambda_9246():

        label("loc_9246")

        TurnDirection(0xFE, 0x33, 500)
        Yield()
        Jump("loc_9246")

    QueueWorkItem2(0x18, 2, lambda_9246)
    OP_68(40000, -2500, -22500, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(17500, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_82(0x32, 0x0, 0xBB8, 0x7D0)
    BeginChrThread(0x33, 3, 0, 51)
    BeginChrThread(0x2F, 1, 0, 49)
    Sleep(2000)
    OP_68(50000, -2500, -22500, 5000)
    MoveCamera(70, 10, 0, 5000)
    SetCameraDistance(27500, 5000)
    BeginChrThread(0x33, 0, 0, 48)
    OP_6F(0x79)
    WaitChrThread(0x33, 0)
    StopBGM(0x1B58)
    OP_68(22140, 4000, 20700, 6000)
    MoveCamera(37, 21, 0, 6000)
    SetCameraDistance(26000, 6000)
    OP_6F(0x79)
    Sleep(300)
    SetCameraDistance(22000, 3000)
    Sleep(2000)
    StopSound(126, 1000, 50)
    StopSound(128, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x18, 0x2)
    WaitBGM()
    OP_24(0x1E3)
    SetScenarioFlags(0x22, 0)
    NewScene("c1210", 0, 0, 0)
    IdleLoop()
    Jump("loc_93DA")

    label("loc_9354")


    ChrTalk(
        0x109,
        "#5P#10100FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PAlright then, just let\x01",
            "me know when you're\x01",
            "ready.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 40000, -2500, -18000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x18, 0xFF)
    EventEnd(0x5)
    Jump("loc_93DA")

    label("loc_93DA")

    Return()

    # Function_47_8AE5 end

    def Function_48_93DB(): pass

    label("Function_48_93DB")

    OP_96(0x33, 0xA410, 0xFFFFF060, 0xFFFFA81C, 0xBB8, 0x0)

    def lambda_93F4():
        OP_9E(0xFE, 0xA410, 0xFFFE96AC, 0x7530, 0xFA0, 0x1)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_93F4)
    Sleep(1000)

    def lambda_9412():
        OP_9E(0xFE, 0xA410, 0xFFFE96AC, 0x7530, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_9412)
    Sleep(1000)

    def lambda_9430():
        OP_9E(0xFE, 0xA410, 0xFFFE96AC, 0x7530, 0x1770, 0x1)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_9430)
    Sleep(1000)

    def lambda_944E():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_944E)

    def lambda_945B():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_945B)

    def lambda_9468():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9468)

    def lambda_9475():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9475)

    def lambda_9482():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9482)

    def lambda_948F():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_948F)

    def lambda_949C():
        OP_9E(0xFE, 0xA410, 0xFFFE96AC, 0x7530, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_949C)
    Sleep(1000)

    def lambda_94BA():
        OP_9E(0xFE, 0xA410, 0xFFFE96AC, 0x7530, 0x1F40, 0x1)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_94BA)
    WaitChrThread(0x33, 1)
    Return()

    # Function_48_93DB end

    def Function_49_94D5(): pass

    label("Function_49_94D5")

    Sound(470, 0, 100, 0)
    Sound(482, 0, 60, 0)
    Sleep(5000)
    Sound(483, 2, 100, 0)
    Sleep(4000)
    StopSound(483, 2000, 90)
    Return()

    # Function_49_94D5 end

    def Function_50_94F4(): pass

    label("Function_50_94F4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(483)
    SetMapObjFlags(0x5, 0x4)
    LoadChrToIndex("apl/ch51104.itc", 0x28)
    LoadChrToIndex("chr/ch00001.itc", 0x29)
    LoadChrToIndex("chr/ch00101.itc", 0x2A)
    LoadEffect(0x0, "event\\ev315_00.eff")
    OP_68(39650, -1200, -36850, 0)
    MoveCamera(56, 4, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16610, 0)
    SetChrChipByIndex(0x109, 0x28)
    SetChrSubChip(0x109, 0x0)
    ClearChrFlags(0x33, 0x80)
    ClearMapObjFlags(0xD, 0x4)
    OP_78(0xD, 0x33)
    SetChrPos(0x33, 50980, -4000, -30210, 270)
    OP_D5(0x33, 0x0, 0x41EB0, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x18, 0xFF)
    SetChrPos(0x109, 49200, -3700, -30160, 270)
    SetChrPos(0x101, 53730, -3100, -29070, 1)
    SetChrPos(0x102, 51850, -3100, -29370, 270)
    SetChrPos(0x103, 52260, -3100, -30360, 300)
    SetChrPos(0x104, 50980, -3100, -30930, 270)
    SetChrPos(0x105, 53510, -3100, -31010, 280)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 42410, -2500, -18000, 180)
    OP_68(38240, -1200, -24640, 6000)
    MoveCamera(26, 25, 0, 6000)
    OP_6E(600, 5000)
    SetCameraDistance(16610, 5000)
    BeginChrThread(0x33, 0, 0, 54)
    BeginChrThread(0x33, 3, 0, 51)
    BeginChrThread(0x2F, 1, 0, 55)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(4000)
    TurnDirection(0x104, 0x18, 0)
    Sleep(120)
    TurnDirection(0x102, 0x18, 0)
    Sleep(120)
    TurnDirection(0x105, 0x18, 0)
    Sleep(90)
    TurnDirection(0x103, 0x18, 0)
    Sleep(900)
    OP_93(0x102, 0x1E, 0x0)
    Sleep(300)
    Sleep(300)
    Sleep(150)
    EndChrThread(0x33, 0x3)
    WaitChrThread(0x33, 0)
    Sleep(500)
    BeginChrThread(0x101, 1, 0, 52)
    Sleep(400)
    BeginChrThread(0x102, 1, 0, 53)
    Sleep(300)

    def lambda_96D9():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_96D9)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x18, 0)
    Sleep(120)
    TurnDirection(0x18, 0x101, 0)

    def lambda_9703():
        OP_9B(0x0, 0xFE, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9703)
    Sleep(100)

    def lambda_971B():
        OP_9B(0x0, 0xFE, 0x5, 0x258, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_971B)
    WaitChrThread(0x102, 1)

    def lambda_9734():
        OP_9B(0x0, 0xFE, 0xF, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9734)
    Sleep(800)
    Fade(1000)
    OP_68(38180, 0, -21930, 0)
    MoveCamera(39, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11490, 0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x105, 0x1)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x101, 41000, -2500, -17960, 91)
    SetChrPos(0x102, 42180, -2500, -14850, 172)
    SetChrPos(0x103, 40190, -2500, -15950, 127)
    SetChrPos(0x104, 37640, -2500, -16670, 127)
    SetChrPos(0x109, 39080, -2500, -19420, 80)
    SetChrPos(0x105, 38110, -2500, -18360, 81)
    TurnDirection(0x18, 0x101, 0)
    OP_0D()
    Sleep(600)
    Sleep(300)
    OP_93(0x101, 0x0, 0x0)
    Sleep(300)
    OP_68(36420, 0, -4160, 6000)
    MoveCamera(39, 25, 0, 8000)
    OP_6E(600, 8000)
    SetCameraDistance(31000, 8000)

    def lambda_9847():
        OP_95(0xFE, 38490, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9847)
    Sleep(60)

    def lambda_9864():
        OP_95(0xFE, 37490, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9864)
    Sleep(30)
    TurnDirection(0x18, 0x101, 500)

    def lambda_9888():
        OP_95(0xFE, 38490, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9888)
    Sleep(30)

    def lambda_98A5():
        OP_95(0xFE, 37990, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_98A5)

    def lambda_98BF():
        OP_95(0xFE, 39490, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_98BF)
    Sleep(30)

    def lambda_98DC():
        OP_95(0xFE, 38290, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_98DC)
    Sleep(600)
    Sleep(300)
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x1E3)
    SetScenarioFlags(0x22, 2)
    NewScene("c0500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_50_94F4 end

    def Function_51_9915(): pass

    label("Function_51_9915")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_995F")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, -500, -5000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(233)
    Jump("Function_51_9915")

    label("loc_995F")

    Return()

    # Function_51_9915 end

    def Function_52_9960(): pass

    label("Function_52_9960")

    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x4)
    ClearChrBattleFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrSubChip(0xFE, 0x2)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x2)
    OP_9C(0xFE, 0xFFFFFE0C, 0xFFFFFC18, 0x9C4, 0x3E8, 0x5DC)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_52_9960 end

    def Function_53_99C1(): pass

    label("Function_53_99C1")

    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x4)
    ClearChrBattleFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrSubChip(0xFE, 0x2)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x102, 0x2A)
    SetChrSubChip(0x102, 0x2)
    OP_9C(0xFE, 0xFFFFFE0C, 0xFFFFFC18, 0x9C4, 0x3E8, 0x9C4)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(31, 0, 100, 0)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_53_99C1 end

    def Function_54_9A22(): pass

    label("Function_54_9A22")

    OP_96(0x33, 0x9858, 0xFFFFF060, 0xFFFFA36C, 0x7D0, 0x0)
    TurnDirection(0x18, 0x33, 0)
    OP_96(0x33, 0x96C8, 0xFFFFF060, 0xFFFFA81C, 0x3E8, 0x0)
    Return()

    # Function_54_9A22 end

    def Function_55_9A52(): pass

    label("Function_55_9A52")

    Sound(483, 2, 100, 0)
    Sleep(3000)
    StopSound(483, 500, 100)
    Sound(481, 0, 100, 0)
    Sound(477, 0, 50, 0)
    Sleep(1000)
    Sound(484, 0, 70, 0)
    Sleep(4000)
    Sound(478, 0, 50, 0)
    Return()

    # Function_55_9A52 end

    def Function_56_9A80(): pass

    label("Function_56_9A80")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch44100.itc", 0x28)
    LoadChrToIndex("chr/ch47500.itc", 0x29)
    LoadChrToIndex("chr/ch23600.itc", 0x2A)
    SetChrChipByIndex(0x29, 0x28)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, 0, 0, 11000, 180)
    SetChrChipByIndex(0x2A, 0x29)
    SetChrSubChip(0x2A, 0x0)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, -1000, 0, 9000, 45)
    SetChrChipByIndex(0x2B, 0x2A)
    SetChrSubChip(0x2B, 0x0)
    ClearChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x8000)
    SetChrPos(0x2B, 1000, 0, 9000, 270)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x8000)
    SetMapObjFlags(0xC, 0x1000)
    ClearMapObjFlags(0xC, 0x4)
    OP_78(0xC, 0x2C)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x2C, 4000, 0, 11000, 90)
    OP_D5(0x2C, 0x0, 0x15F90, 0x0, 0x0)
    ClearChrFlags(0x2D, 0x80)
    SetChrFlags(0x2D, 0x8000)
    OP_78(0xB, 0x2D)
    OP_49()
    SetChrPos(0x2D, -48000, 2000, 23520, 90)
    OP_D5(0x2D, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x79, 0xB4, 0x1, 0x20)
    OP_68(-6940, 5850, 2500, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(6780, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x2A,
        (
            "Maaan, flying around\x01",
            "this vast city is the\x01",
            "best, huh.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x2B, 500)
    Sleep(50)

    ChrTalk(
        0x2A,
        (
            "Your driving has\x01",
            "improved a lot, you know\x01",
            "that Reggie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        "Hehe, I know, right?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x29, 500)
    Sleep(50)

    ChrTalk(
        0x2B,
        (
            "Well, it's also because\x01",
            "of the high performance\x01",
            "of Yuri's car, though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x29, 500)
    Sleep(50)

    ChrTalk(
        0x29,
        (
            "Heheh, damn straight. It's\x01",
            "Verne Co.'s latest model,\x01",
            "if I do say so myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "...More importantly, Reggie.\x01",
            "You almost hit that middle-aged\x01",
            "man on the highway, didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "Y-Yeah... I just barely\x01",
            "missed him somehow,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "But... Did you see the\x01",
            "look on his face!?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x29, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x29)
    OP_64(0x2A)
    OP_64(0x2B)

    ChrTalk(
        0x29,
        "#4S#1K#1P...Awesome!\x02",
    )


    ChrTalk(
        0x2A,
        "#4S#1K#3PYeah, awesome!!\x02",
    )


    ChrTalk(
        0x2B,
        "#4S#1K#2PYeah, awesome!!\x02",
    )

    OP_57(0x1)
    OP_5A()
    OP_63(0x29, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x2A, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x2B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x29)
    OP_64(0x2A)
    OP_64(0x2B)

    ChrTalk(
        0x2A,
        (
            "Wahahaha! That old man\x01",
            "was scared silly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "Y-You'll run me over!!\x01",
            "Save me!! Right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x2A, 500)
    Sleep(50)

    ChrTalk(
        0x2B,
        (
            "Ahahaha! S-Stop it\x01",
            "Sykes! My belly's going\x01",
            "to burst!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "Hehe... Well, we'll be\x01",
            "here a while, so might\x01",
            "as well enjoy it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "Our new playground...\x01",
            "That's this Crossbell\x01",
            "City.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x29, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(-34730, 5840, 17160, 0)
    MoveCamera(332, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(9710, 0)
    Sound(457, 0, 100, 0)

    def lambda_A07D():
        OP_98(0xFE, 0x61A8, 0x0, 0x0, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_A07D)
    OP_68(-29600, 5840, 16660, 2000)
    OP_71(0xB, 0x79, 0xB4, 0x0, 0x20)
    OP_6F(0x1)
    OP_0D()
    Sleep(1200)
    StopSound(457, 1000, 100)
    Fade(500)
    OP_68(-6940, 5850, 2500, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(6780, 0)
    OP_93(0x29, 0x13B, 0x0)
    OP_93(0x2A, 0x13B, 0x0)
    OP_93(0x2B, 0x13B, 0x0)
    OP_0D()
    Sleep(50)

    ChrTalk(
        0x29,
        (
            "Whoops... Looks like the\x01",
            "cops are here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x2B, 500)
    Sleep(50)

    ChrTalk(
        0x2A,
        "Reggie, the car!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x2A, 500)
    Sleep(50)

    ChrTalk(
        0x2B,
        (
            "Okay, it'll shake them\x01",
            "off!\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    BeginChrThread(0x2B, 1, 0, 58)
    Sleep(100)
    BeginChrThread(0x29, 1, 0, 59)
    Sleep(100)
    BeginChrThread(0x2A, 1, 0, 60)
    Sleep(800)
    Sound(485, 0, 100, 0)
    Sleep(50)
    Sound(100, 0, 50, 0)
    OP_71(0xC, 0x1, 0x1E, 0x1, 0x0)
    OP_79(0xA)
    Sleep(500)
    WaitChrThread(0x2B, 1)

    def lambda_A1C9():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_A1C9)

    def lambda_A1DE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_A1DE)
    WaitChrThread(0x2B, 2)
    Sleep(100)
    WaitChrThread(0x29, 1)

    def lambda_A1FA():
        OP_9B(0x0, 0xFE, 0xB4, 0xFFFFF830, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_A1FA)

    def lambda_A20F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_A20F)
    Sleep(100)
    WaitChrThread(0x2A, 1)

    def lambda_A227():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_A227)

    def lambda_A23C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_A23C)
    Sleep(100)
    WaitChrThread(0x29, 1)
    WaitChrThread(0x29, 2)
    WaitChrThread(0x2A, 1)
    WaitChrThread(0x2A, 2)
    Sound(100, 0, 50, 0)
    OP_71(0xC, 0x1F, 0x3C, 0x1, 0x0)
    Sleep(500)
    Sound(485, 0, 100, 0)
    OP_79(0xA)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1C3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x2C, 0x80)
    OP_78(0xC, 0x2C)
    OP_49()
    SetChrPos(0x2C, 4000, 0, 11000, 90)
    OP_D5(0x2C, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x1000)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    OP_74(0xC, 0x1E)
    Sound(470, 0, 50, 0)
    OP_71(0xC, 0x79, 0xB4, 0x1, 0x20)
    OP_0D()
    Sleep(800)
    BeginChrThread(0x2C, 1, 0, 57)
    Sleep(100)
    OP_68(18560, 1210, 10040, 1500)
    SetCameraDistance(30470, 1500)
    OP_6F(0x79)
    Sleep(50)
    OP_68(17250, 1210, -8950, 1200)
    OP_6F(0x1)
    Sleep(50)
    OP_68(-17400, 1210, -12130, 2500)
    OP_6F(0x1)
    WaitChrThread(0x2C, 1)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    OP_0D()
    Sleep(200)
    SetScenarioFlags(0x22, 6)
    NewScene("c1000", 112, 0, 0)
    IdleLoop()
    Return()

    # Function_56_9A80 end

    def Function_57_A36C(): pass

    label("Function_57_A36C")

    Sound(494, 0, 100, 0)
    OP_98(0x2C, 0x3A98, 0x0, 0x0, 0x2710, 0x0)
    OP_9F(0x0, 0x2C)
    OP_9F(0x1, 19020, 0, 10300)
    OP_9F(0x1, 19750, 0, 6120)
    OP_9F(0x2, 0x2C, 11000, 0x6)
    Sound(458, 0, 100, 0)
    OP_98(0x2C, 0x0, 0x0, 0xFFFFC568, 0x3A98, 0x0)
    Sound(492, 0, 100, 0)
    OP_9F(0x0, 0x2C)
    OP_9F(0x1, 18580, 0, -9470)
    OP_9F(0x1, 14650, 0, -11440)
    OP_9F(0x1, 10980, 0, -11590)
    OP_9F(0x2, 0x2C, 11000, 0x6)
    OP_98(0x2C, 0xFFFF9688, 0x0, 0x0, 0x4E20, 0x0)
    Sound(492, 0, 100, 0)
    OP_9F(0x0, 0x2C)
    OP_9F(0x1, -18160, 0, -11990)
    OP_9F(0x1, -19820, 0, -15120)
    OP_9F(0x1, -19650, 0, -17640)
    OP_9F(0x2, 0x2C, 11000, 0x6)
    OP_98(0x2C, 0x0, 0x0, 0xFFFFB1E0, 0x3A98, 0x0)
    Return()

    # Function_57_A36C end

    def Function_58_A46C(): pass

    label("Function_58_A46C")

    OP_93(0x2B, 0x5A, 0x3E8)
    OP_9B(0x0, 0x2B, 0x0, 0x9C4, 0xBB8, 0x0)
    OP_93(0x2B, 0x0, 0x1F4)
    Return()

    # Function_58_A46C end

    def Function_59_A48A(): pass

    label("Function_59_A48A")

    OP_93(0x29, 0x0, 0x3E8)
    OP_9B(0x0, 0x29, 0x0, 0x9C4, 0xBB8, 0x0)
    OP_93(0x29, 0x5A, 0x3E8)
    OP_9B(0x0, 0x29, 0x0, 0xFA0, 0xBB8, 0x0)
    OP_93(0x29, 0xB4, 0x1F4)
    Return()

    # Function_59_A48A end

    def Function_60_A4BE(): pass

    label("Function_60_A4BE")

    OP_93(0x2A, 0x0, 0x3E8)
    OP_9B(0x0, 0x2A, 0x0, 0xFA0, 0xBB8, 0x0)
    OP_93(0x2A, 0x5A, 0x3E8)
    OP_9B(0x0, 0x2A, 0x0, 0x1388, 0xBB8, 0x0)
    OP_93(0x2A, 0xB4, 0x1F4)
    Return()

    # Function_60_A4BE end

    def Function_61_A4F2(): pass

    label("Function_61_A4F2")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1470, 1330, -4340, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12810, 0)
    SetChrPos(0x101, -750, -690, -3500, 0)
    SetChrPos(0x102, 250, -700, -3730, 0)
    SetChrPos(0x109, -750, -480, -5190, 0)
    SetChrPos(0x105, 250, -520, -5100, 0)
    OP_4B(0x19, 0xFF)
    OP_0D()

    ChrTalk(
        0x19,
        (
            "That Meiling... I wonder\x01",
            "where she went...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FUmm, excuse us, are you\x01",
            "Meiling's brother?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x19, 0xB4, 0x1F4)

    ChrTalk(
        0x19,
        (
            "Yeah that's me... You\x01",
            "need something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FUmm, we're Crossbell\x01",
            "Police's Special Support\x01",
            "Section.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained about\x01",
            "the umbrella swap.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x19,
        "...Oh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Meiling took the wrong\x01",
            "umbrella, and I didn't\x01",
            "realize it either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "My bad. I'd like to\x01",
            "return it as soon as\x01",
            "possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FOn that note... Where's\x01",
            "Meiling?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FWasn't she taking a walk\x01",
            "with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Actually, Meiling and I\x01",
            "just started playing\x01",
            "hide and seek.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Though it's a pain in this\x01",
            "rain, she insisted and I\x01",
            "went along with it, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x19, 0x10E, 0x1F4)
    Sleep(1000)
    OP_93(0x19, 0x5A, 0x1F4)
    Sleep(1000)
    OP_93(0x19, 0xB4, 0x1F4)
    OP_63(0x19, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x19,
        (
            "She's an expert at\x01",
            "hiding...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "I'm not great at\x01",
            "searching, so I'm not sure\x01",
            "how soon I'll find her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FI-I see...\x02\x03",
            "#00000FWell in that case, how\x01",
            "about we help you find\x01",
            "her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Oh, that would be great!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "I think she's hiding\x01",
            "somewhere in Waterfront\x01",
            "Area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Probably somewhere well\x01",
            "hidden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "It might not be that\x01",
            "easy to find her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FAlright, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHaha. Shall we take a\x01",
            "look around, then?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -330, -700, -3820, 0)
    OP_93(0x19, 0xB4, 0x0)
    OP_4C(0x19, 0xFF)
    ClearChrFlags(0x19, 0x10)
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    OP_66(0x4, 0x1)
    OP_66(0x5, 0x1)
    OP_66(0x6, 0x1)
    ClearChrFlags(0x1A, 0x80)
    SetScenarioFlags(0x133, 4)
    OP_29(0x6B, 0x1, 0x2)
    OP_C9(0x0, 0x1000)
    EventEnd(0x5)
    Return()

    # Function_61_A4F2 end

    def Function_62_AA7F(): pass

    label("Function_62_AA7F")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00012FUnder the bench... She's\x01",
            "not there, no matter how\x01",
            "I think about it.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_62_AA7F end

    def Function_63_AAD6(): pass

    label("Function_63_AAD6")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000F...She's not behind the\x01",
            "cart either.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_63_AAD6 end

    def Function_64_AB0E(): pass

    label("Function_64_AB0E")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00006FBehind the shipping\x01",
            "container! ...Guess\x01",
            "she's not there.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_64_AB0E end

    def Function_65_AB5A(): pass

    label("Function_65_AB5A")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FIt's hide-and-seek, so\x01",
            "she wouldn't be indoors.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -14030, 2000, 24980, 180)
    EventEnd(0x4)
    Return()

    # Function_65_AB5A end

    def Function_66_ABAF(): pass

    label("Function_66_ABAF")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FMeiling should be somewhere\x01",
            "in Waterfront Area. ...Let's\x01",
            "search a litter harder.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 4500, 3050, 30320, 180)
    EventEnd(0x4)
    Return()

    # Function_66_ABAF end

    def Function_67_AC25(): pass

    label("Function_67_AC25")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FMeiling should be somewhere\x01",
            "in Waterfront Area. ...Let's\x01",
            "search a litter harder.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -19940, 0, -25710, 359)
    EventEnd(0x4)
    Return()

    # Function_67_AC25 end

    def Function_68_AC9B(): pass

    label("Function_68_AC9B")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FMeiling should be somewhere\x01",
            "in Waterfront Area. ...Let's\x01",
            "search a litter harder.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -25570, 2000, 23250, 90)
    EventEnd(0x4)
    Return()

    # Function_68_AC9B end

    def Function_69_AD11(): pass

    label("Function_69_AD11")

    TalkBegin(0x19)

    ChrTalk(
        0x19,
        (
            "You guys. It looks like\x01",
            "you haven't found\x01",
            "Meiling yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "If you really can't find her,\x01",
            "I'll give the give up signal\x01",
            "and ask her to come out, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "...What do you want to\x01",
            "do?\x02",
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
        1,
        (
            "Give up\x01",      # 0
            "Refuse\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B082")
    EventBegin(0x0)
    Fade(500)
    OP_68(-1470, 1330, -4340, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12810, 0)
    SetChrPos(0x101, -750, -690, -3500, 0)
    SetChrPos(0x102, 250, -700, -3730, 0)
    SetChrPos(0x109, -750, -480, -5190, 0)
    SetChrPos(0x105, 250, -520, -5100, 0)
    OP_93(0x19, 0xB4, 0x0)
    OP_4B(0x19, 0xFF)
    OP_0D()

    ChrTalk(
        0x101,
        "#12P#00006F...Sorry. If you please?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Well, we're out of\x01",
            "options.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "In that case...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x19,
        (
            "#4SMEILING, I GIVE\x01",
            "UUUP!!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_93(0x19, 0x5A, 0x0)
    OP_93(0x101, 0x5A, 0x0)
    OP_93(0x102, 0x5A, 0x0)
    OP_93(0x109, 0x2D, 0x0)
    OP_93(0x105, 0x2D, 0x0)
    SetChrPos(0x1A, 2590, -700, -2880, 270)
    OP_4B(0x1A, 0xFF)
    Sleep(1500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x1A,
        (
            "...Ehehe, Meiling's the\x01",
            "winner~!♪\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Then, Meiling appeared\x01",
            "before Lloyd and the\x01",
            "others who had given up...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "And Lloyd told Meiling\x01",
            "that she had grabbed\x01",
            "Momo's umbrella.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Call(0, 71)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B12A")

    label("loc_B082")


    ChrTalk(
        0x101,
        (
            "#00000FNo, we want to search a\x01",
            "little more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "I see. Good luck, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "By the way, don't count on\x01",
            "me. ...It's probably\x01",
            "because it's getting late.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B12A")

    TalkEnd(0x19)
    Return()

    # Function_69_AD11 end

    def Function_70_B12E(): pass

    label("Function_70_B12E")

    EventBegin(0x0)
    Fade(500)
    OP_68(87940, -800, 17550, 0)
    MoveCamera(307, 32, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14760, 0)
    SetChrPos(0x101, 86200, -2500, 17950, 37)
    SetChrPos(0x102, 85470, -2500, 16990, 37)
    SetChrPos(0x109, 84630, -2500, 16160, 37)
    SetChrPos(0x105, 83750, -2500, 15320, 37)
    OP_4B(0x1A, 0xFF)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00002FYou wouldn't happen to\x01",
            "be Meiling, would you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FHaha, found her!\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x1A, 0x101, 500)
    Sleep(50)

    ChrTalk(
        0x1A,
        "Eek, I was found!\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A,
        (
            "Wait, you're not my\x01",
            "brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Who are you guys?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FHaha, finally.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FWell then, let's report\x01",
            "to Roy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Call(0, 71)
    EventEnd(0x5)
    Return()

    # Function_70_B12E end

    def Function_71_B2E3(): pass

    label("Function_71_B2E3")

    EventBegin(0x0)
    ClearScenarioFlags(0x133, 4)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch21500.itc", 0x28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_B70F")
    OP_2C(0x6B, 0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The team called Roy to\x01",
            "Meiling's hiding spot.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "And Lloyd told Meiling\x01",
            "that she had grabbed\x01",
            "Momo's umbrella.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(67920, -400, 17980, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13970, 0)
    SetChrPos(0x101, 68760, -2500, 19500, 90)
    SetChrPos(0x102, 68760, -2500, 18300, 90)
    SetChrPos(0x109, 67600, -2500, 18300, 90)
    SetChrPos(0x105, 67600, -2500, 19500, 90)
    SetChrPos(0x19, 70770, -2500, 19500, 270)
    SetChrPos(0x1A, 70700, -2500, 18300, 270)
    OP_4B(0x19, 0xFF)
    OP_4B(0x1A, 0xFF)
    OP_29(0x6B, 0x1, 0x3)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#00000F....So that's what\x01",
            "happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "I see... I screwed up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Meiling, let's return\x01",
            "the umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Okay, brother.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Here you go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FThen, this one's yours.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x1A, 0x28)
    SetChrSubChip(0x1A, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(500)
    OP_9B(0x1, 0x1A, 0x0, 0x320, 0x5DC, 0x0)
    Sleep(1000)
    OP_9B(0x1, 0x1A, 0xB4, 0x320, 0x5DC, 0x0)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x1A, 0x2)
    SetChrSubChip(0x1A, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Gave Meiling her\x01",
            "umbrella, and received\x01",
            "Momo's.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#6P#00100FHaha, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Nuh-uh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Can you guys tell Momo\x01",
            "I'm sorry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FHaha. She's very clever\x01",
            "for a girl her age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Hmph, you can say that\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "If I were as clever as\x01",
            "her, I'd have one or two\x01",
            "jobs by now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FW-Well anyway, thanks\x01",
            "for your help.\x02\x03",
            "#00000FPlease allow us to\x01",
            "return the other\x01",
            "umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Alright, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Please do~.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Jump("loc_BA9B")

    label("loc_B70F")

    OP_68(-1470, 1230, -4340, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12830, 0)
    SetChrPos(0x101, -750, -690, -3500, 0)
    SetChrPos(0x102, 250, -700, -3730, 0)
    SetChrPos(0x109, -750, -480, -5190, 0)
    SetChrPos(0x105, 250, -520, -5100, 0)
    SetChrPos(0x19, 250, -700, -1650, 180)
    SetChrPos(0x1A, -750, -700, -1650, 180)
    OP_4B(0x19, 0xFF)
    OP_4B(0x1A, 0xFF)
    OP_29(0x6B, 0x1, 0x4)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#00000F....So that's what\x01",
            "happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "I see... I screwed up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Meiling, let's return\x01",
            "the umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Okay, brother.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Here you go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10100FThen, this one's yours.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x1A, 0x28)
    SetChrSubChip(0x1A, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(500)
    OP_9B(0x1, 0x1A, 0x0, 0x320, 0x5DC, 0x0)
    Sleep(1000)
    OP_9B(0x1, 0x1A, 0xB4, 0x320, 0x5DC, 0x0)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x1A, 0x2)
    SetChrSubChip(0x1A, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Gave Meiling her\x01",
            "umbrella, and received\x01",
            "Momo's.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#12P#00100FHaha, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Nuh-uh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Can you guys tell Momo\x01",
            "I'm sorry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10309FHaha. She's very clever\x01",
            "for a girl her age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Hmph, you can say that\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "If I were as clever as\x01",
            "her, I'd have one or two\x01",
            "jobs by now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FW-Well anyway, thanks\x01",
            "for your help.\x02\x03",
            "#00000FPlease allow us to\x01",
            "return the other\x01",
            "umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Alright, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Please do~.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)

    label("loc_BA9B")

    SetScenarioFlags(0x22, 0)
    NewScene("c0210", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_71_B2E3 end

    def Function_72_BAA8(): pass

    label("Function_72_BAA8")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch06300.itc", 0x28)
    LoadChrToIndex("chr/ch31400.itc", 0x29)
    OP_68(20370, 0, 19380, 0)
    MoveCamera(44, 25, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(19230, 0)
    SetChrPos(0x101, 18600, 0, 17800, 0)
    SetChrPos(0x102, 19700, 0, 17800, 0)
    SetChrPos(0x109, 18600, 0, 16600, 0)
    SetChrPos(0x105, 19700, 0, 16600, 0)
    SetChrPos(0x104, 19100, 0, 15400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x27, 0x28)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x27, 0x4)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, 19100, 0, 21700, 180)
    OP_A7(0x27, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x28, 0x29)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x28, 0x4)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 19100, 0, 21700, 180)
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked and\x01",
            "there's a message plate.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Heiyue Trading Company - Crossbell Branch\x01",
            "※Please knock if you have business.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x109,
        (
            "#6P#10101FHeiyue Trading\x01",
            "Company...\x02\x03",
            "#10103FA man named Cao runs\x01",
            "this office, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FCao Lee, also known as the White\x01",
            "Orchid Dragon, is the sharpest and\x01",
            "most capable person in Heiyue.\x02\x03",
            "#10300FShall we pay him a visit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FWell, even if we want\x01",
            "to, he may not be able\x01",
            "to see us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FHmm...\x02\x03",
            "#00301FI wanted to ask him\x01",
            "about the old Revache\x01",
            "building, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FThat's right. Heiyue must have had\x01",
            "their eyes on it...\x02\x03",
            "#00001FBut in the end, it looks like they\x01",
            "were outmaneuvered by Crimson & Co.\x01",
            "I wonder what they were thinking.\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 0, 100, 0)
    Sleep(500)
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x4)
    Sleep(500)

    ChrTalk(
        0x27,
        (
            "─Haha. It was awful and\x01",
            "really regrettable, I\x01",
            "tell you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0x27, 3, 0, 73)
    Sleep(700)
    BeginChrThread(0x28, 3, 0, 74)
    Sleep(300)

    def lambda_BFC1():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BFC1)
    Sleep(50)

    def lambda_BFD9():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BFD9)
    Sleep(50)

    def lambda_BFF1():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BFF1)
    Sleep(50)

    def lambda_C009():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C009)
    Sleep(50)

    def lambda_C021():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C021)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#12P#00005FB-Branch Manager Cao...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#03200FGood day, ladies and\x01",
            "gentlemen of the Special\x01",
            "Support Section.\x02\x03",
            "#03209FYour timing is perfect!\x02\x03",
            "Actually, I'd like to\x01",
            "ask a small favor of all\x01",
            "of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FA favor...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#03200FIf you don't mind, could\x01",
            "you hear me out?\x02\x03",
            "#03204FThough I won't force you\x01",
            "to, of course.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x27, 0x0, 0x1F4)

    def lambda_C1A5():
        OP_97(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_C1A5)
    Sleep(500)

    def lambda_C1C2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_C1C2)
    WaitChrThread(0x27, 1)
    OP_9B(0x1, 0x101, 0x0, 0x1F4, 0x7D0, 0x0)

    ChrTalk(
        0x101,
        "#12P#00005FW-What the...!?\x02",
    )

    CloseMessageWindow()
    OP_97(0x28, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    OP_93(0x28, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x28,
        (
            "...We're deeply sorry\x01",
            "about this. We're in a\x01",
            "bit of a pickle, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "But if you do have some\x01",
            "spare time, we would very\x01",
            "much like you to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "We've unlocked our door\x01",
            "for you, so please do\x01",
            "come inside.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x28, 0x0, 0x1F4)

    def lambda_C305():
        OP_97(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_C305)
    Sleep(500)

    def lambda_C322():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_C322)
    WaitChrThread(0x28, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x4, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x4)
    Sleep(500)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0x104)

    ChrTalk(
        0x105,
        (
            "#12P#10309FAhaha. They're real man-\x01",
            "eaters, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FI don't think you're one\x01",
            "to talk, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FSo, what should we do\x01",
            "now? It doesn't seem\x01",
            "like a trap...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FShould we play along with\x01",
            "their request? We might end\x01",
            "up gaining some more intel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI wonder... (We're kind of busy at\x01",
            "the moment, so I don't feel like\x01",
            "we have to help them, though.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x153, 4)
    SetMapObjFlags(0x4, 0x10)
    OP_65(0x2, 0x1)
    OP_D7(0x28)
    OP_D7(0x29)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 18600, 0, 17800, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_72_BAA8 end

    def Function_73_C586(): pass

    label("Function_73_C586")


    def lambda_C58B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_C58B)

    def lambda_C59C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_C59C)
    WaitChrThread(0x27, 1)
    OP_93(0x27, 0xB4, 0x1F4)
    Return()

    # Function_73_C586 end

    def Function_74_C5BD(): pass

    label("Function_74_C5BD")


    def lambda_C5C2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_C5C2)

    def lambda_C5D3():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_C5D3)
    WaitChrThread(0x28, 1)
    OP_95(0x28, 18100, 0, 19500, 2000, 0x0)
    OP_93(0x28, 0xB4, 0x1F4)
    Return()

    # Function_74_C5BD end

    def Function_75_C608(): pass

    label("Function_75_C608")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_32(0xFF, 0xF9, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    OP_68(20340, 100, 18050, 0)
    MoveCamera(42, 24, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(16510, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_C78B")
    SetChrPos(0x1A2, 18700, 0, 16660, 180)
    SetChrPos(0x102, 19540, 0, 16660, 180)
    SetChrPos(0x101, 18440, 0, 18250, 180)
    SetChrPos(0x104, 19680, 0, 18250, 180)
    SetChrPos(0x109, 18460, 0, 19360, 180)
    SetChrPos(0x105, 19600, 0, 19360, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_C6E3():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_C6E3)

    def lambda_C6FD():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C6FD)
    Sleep(100)

    def lambda_C71A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C71A)
    Sleep(50)

    def lambda_C737():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C737)
    Sleep(100)

    def lambda_C754():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C754)
    Sleep(50)

    def lambda_C771():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C771)
    Jump("loc_C9D2")

    label("loc_C78B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_C8B1")
    SetChrPos(0x1A2, 18700, 0, 16660, 180)
    SetChrPos(0x102, 19540, 0, 16660, 180)
    SetChrPos(0x101, 18440, 0, 18250, 180)
    SetChrPos(0x109, 19680, 0, 18250, 180)
    SetChrPos(0x104, 18460, 0, 19360, 180)
    SetChrPos(0x105, 19600, 0, 19360, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_C809():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_C809)

    def lambda_C823():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C823)
    Sleep(100)

    def lambda_C840():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C840)
    Sleep(50)

    def lambda_C85D():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C85D)
    Sleep(100)

    def lambda_C87A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C87A)
    Sleep(50)

    def lambda_C897():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C897)
    Jump("loc_C9D2")

    label("loc_C8B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_C9D2")
    SetChrPos(0x1A2, 18700, 0, 16660, 180)
    SetChrPos(0x102, 19540, 0, 16660, 180)
    SetChrPos(0x101, 18440, 0, 18250, 180)
    SetChrPos(0x105, 19680, 0, 18250, 180)
    SetChrPos(0x104, 19600, 0, 19360, 180)
    SetChrPos(0x109, 18460, 0, 19360, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_C92F():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_C92F)

    def lambda_C949():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C949)
    Sleep(100)

    def lambda_C966():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C966)
    Sleep(50)

    def lambda_C983():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C983)
    Sleep(100)

    def lambda_C9A0():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C9A0)
    Sleep(50)

    def lambda_C9BD():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C9BD)

    label("loc_C9D2")

    OP_68(20080, 600, 15520, 3000)
    MoveCamera(40, 20, 0, 3000)
    OP_6E(560, 3000)
    SetCameraDistance(16390, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    def lambda_CA11():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_CA11)
    Sleep(50)

    def lambda_CA21():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CA21)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#12PAlright then, I'll get\x01",
            "started with the details,\x01",
            "so pay attention!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FS-Sure...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306F(This brat, he's trying\x01",
            "to act tough in front of\x01",
            "the princess.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10100F(Yeah, it feels quite\x01",
            "natural though.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10302F(Haha. He really likes\x01",
            "Elie, doesn't he?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        (
            "#12PWhat, got somethin' to\x01",
            "say to me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FOh, no. Everything's\x01",
            "fine.\x02\x03",
            "#00000FPlease go ahead with\x01",
            "your explanation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PHehe. Then I'll get\x01",
            "straight to the point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PAs I was saying before, I'd like\x01",
            "you guys to be my tour guides\x01",
            "and show me around the city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PBut walking around this vast\x01",
            "Crossbell without any objective\x01",
            "would just tire me out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PAnd so, I want to aim\x01",
            "for a certain place to\x01",
            "begin with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10105FA certain place?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PYeah, the roof of Times\x01",
            "Department Store in Central\x01",
            "Square to be precise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PAnyway, take me there\x01",
            "last. Then I'll call it\x01",
            "mission complete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00300FI see. That's easy to\x01",
            "understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10300FBy the way, are we free\x01",
            "to decide the route to\x01",
            "take you there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PNo. It'd be a problem if\x01",
            "you took me to boring\x01",
            "areas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PTake me to the\x01",
            "department store by way\x01",
            "of East Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FHow to say this... You\x01",
            "have this all planned\x01",
            "out, don't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PHehe. It's a special\x01",
            "trip. This degree of\x01",
            "planning is only natural.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PBut, I don't have any\x01",
            "plans besides that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12POnly, take different\x01",
            "side trips and show Elie\x01",
            "and I a good time.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#11P#00109FAh, well I'm your guide\x01",
            "too, you see...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#6PNonsense, that's out of\x01",
            "the question.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PYou've got to enjoy this\x01",
            "experience too, milady, even\x01",
            "for just a little while!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#5P#10109FAhaha, he's totally\x01",
            "fallen for her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell, I get the general idea,\x01",
            "but...\x02\x03",
            "#00000FBased on what you said, we're\x01",
            "basically just normally\x01",
            "walking around town.\x02\x03",
            "Are you okay with that,\x01",
            "Shing?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D22A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_D22A)
    Sleep(50)

    def lambda_D23A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D23A)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#5P#00305FWell, are there any\x01",
            "other options?\x02\x03",
            "#00300FSuch as going to Arc-en-\x01",
            "Ciel or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10300FYeah, or the Michelam\x01",
            "theme park.\x02\x03",
            "#10304FWell, they're closed\x01",
            "right now, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12P―Hmph. I've already been\x01",
            "to famous places like\x01",
            "that, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PThose places are certainly fun, and\x01",
            "I think it'd be fun to go again,\x01",
            "but― That's not my goal this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PI need to know lots more\x01",
            "about Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PFor that reason, I must look\x01",
            "not at tourist attractions, but\x01",
            "at how Crossbell really is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FCrossbell's true face...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FYou thought about this\x01",
            "that much, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FMan oh man. And he's\x01",
            "only going to get worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#12P―Anyway, understand?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PTime is short, so begin\x01",
            "the tour right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUnderstood. Let's get\x01",
            "going, then.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_D627")
    OP_29(0x73, 0x1, 0x1)
    OP_93(0x104, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#12P#00300FThen, we'll go on ahead\x01",
            "and stand guard behind\x01",
            "the scenes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10100FRoger.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#5P#10300FHaha, later.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x4, 0xFF)
    Jump("loc_D782")

    label("loc_D627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_D6DB")
    OP_29(0x73, 0x1, 0x2)
    OP_93(0x109, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#12P#10100FThen, we'll go on ahead.\x01",
            "You guys handle the rear\x01",
            "guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00300FSure, got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#5P#10300FHaha, later.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x4, 0xFF)
    Jump("loc_D782")

    label("loc_D6DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_D782")
    OP_29(0x73, 0x1, 0x3)
    OP_93(0x105, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#12P#10300FThen, we'll go on ahead.\x01",
            "You guys are on rear\x01",
            "guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10100FRoger.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00300FBe careful, ok?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x8, 0xFF)

    label("loc_D782")

    OP_C9(0x0, 0x1000)
    OP_1B(0x2, 0x0, 0x68)
    SetScenarioFlags(0x153, 5)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 18910, 0, 13080, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_75_C608 end

    def Function_76_D7D0(): pass

    label("Function_76_D7D0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31400.itc", 0x28)
    SetChrChipByIndex(0x28, 0x28)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x28, 0x4)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 19190, -10, 14710, 180)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    OP_68(19890, 4500, 11900, 0)
    MoveCamera(37, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(27560, 0)
    SetChrPos(0x1A2, 18620, -10, 3410, 0)
    SetChrPos(0x102, 19450, -10, 3400, 0)
    SetChrPos(0x101, 18970, -10, 1840, 0)
    SetChrPos(0x104, 17790, -10, 610, 0)
    SetChrPos(0x109, 20110, -10, 910, 0)
    SetChrPos(0x105, 19260, -10, -170, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x4)
    OP_68(19890, 2500, 11900, 3000)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_D901():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_D901)

    def lambda_D91B():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D91B)
    Sleep(50)

    def lambda_D938():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D938)
    Sleep(50)

    def lambda_D955():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D955)
    Sleep(50)

    def lambda_D972():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D972)
    Sleep(50)

    def lambda_D98F():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D98F)
    WaitChrThread(0x105, 1)
    OP_93(0x28, 0x5A, 0x0)
    OP_9B(0x1, 0x28, 0xB4, 0x3E8, 0x7D0, 0x0)
    BeginChrThread(0x1A2, 3, 0, 77)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 77)
    Sleep(300)
    BeginChrThread(0x101, 3, 0, 77)
    Sleep(200)
    BeginChrThread(0x104, 3, 0, 77)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 77)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 77)
    Sleep(3000)
    BeginChrThread(0x28, 3, 0, 77)
    WaitChrThread(0x28, 3)
    Sleep(700)
    Sound(104, 0, 80, 0)
    OP_71(0x4, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x4)
    Sleep(500)
    OP_68(19890, 4500, 11900, 3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    SetScenarioFlags(0x22, 1)
    NewScene("c1210", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_76_D7D0 end

    def Function_77_DA70(): pass

    label("Function_77_DA70")

    OP_95(0xFE, 19190, -10, 14710, 2000, 0x0)

    def lambda_DA89():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DA89)
    Sleep(3000)

    def lambda_DAA6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DAA6)
    Return()

    # Function_77_DA70 end

    def Function_78_DAB3(): pass

    label("Function_78_DAB3")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x101, -150, -310, 6250, 135)
    SetChrPos(0x102, -1300, -470, 5330, 135)
    SetChrPos(0x109, -1630, -240, 6620, 135)
    SetChrPos(0x105, -510, -80, 7550, 135)
    SetChrPos(0x104, -2890, -500, 5170, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(-330, 1870, 1930, 0)
    MoveCamera(46, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14900, 0)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x34, 0x8000)
    OP_0D()
    SoundLoad(821)
    Call(0, 80)
    Return()

    # Function_78_DAB3 end

    def Function_79_DB63(): pass

    label("Function_79_DB63")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x101, -260, -190, -6920, 45)
    SetChrPos(0x102, -1180, -350, -6000, 45)
    SetChrPos(0x109, -1910, -70, -7580, 45)
    SetChrPos(0x105, -720, -10, -8490, 45)
    SetChrPos(0x104, -2890, -260, -6510, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(510, 1150, -6710, 0)
    MoveCamera(25, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14220, 0)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x34, 0x8000)
    OP_0D()
    SoundLoad(821)
    Call(0, 80)
    Return()

    # Function_79_DB63 end

    def Function_80_DC13(): pass

    label("Function_80_DC13")

    Sound(821, 2, 40, 0)

    ChrTalk(
        0x101,
        "#12P#00000FWow, so many people...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FThat Mishy event is being held today.\x02\x03",
            "#00104FMichelam is closed for the duration\x01",
            "of the conference. They must be doing\x01",
            "this instead of running the park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FHaha, I bet Tio would've\x01",
            "wanted to see this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FHaha. The dance show is\x01",
            "about to start. Since\x01",
            "we're here...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005FWait, that's...!\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_68(5070, 1800, -2680, 4000)
    MoveCamera(42, 27, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(12260, 4000)
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7160", 0)
    SetScenarioFlags(0x2, 3)
    ClearChrFlags(0xF, 0x20)
    ClearChrFlags(0x34, 0x20)
    BeginChrThread(0xF, 1, 0, 86)
    BeginChrThread(0x34, 1, 0, 87)
    OP_63(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x12, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x13, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    ChrTalk(
        0x17,
        "#6P#11AAhhh!!! It's Mishy!!!\x02",
    )

    Sleep(1500)
    OP_57(0x0)
    OP_5A()
    Sleep(1700)
    ClearScenarioFlags(0x2, 3)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x34, 1)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0x34, 0x20)
    SetScenarioFlags(0x2, 4)
    SetScenarioFlags(0x2, 3)
    BeginChrThread(0xF, 0, 0, 81)
    BeginChrThread(0x34, 0, 0, 81)
    BeginChrThread(0x34, 2, 0, 84)
    BeginChrThread(0xF, 2, 0, 85)
    WaitChrThread(0x34, 2)
    WaitChrThread(0xF, 2)
    ClearChrFlags(0xF, 0x20)
    ClearChrFlags(0x34, 0x20)
    ClearScenarioFlags(0x2, 4)
    OP_93(0xF, 0xB4, 0x0)
    OP_93(0x34, 0xB4, 0x0)
    Sleep(200)
    BeginChrThread(0xF, 1, 0, 87)
    BeginChrThread(0x34, 1, 0, 86)
    OP_63(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x12, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x13, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    ChrTalk(
        0x16,
        (
            "#6P#11AHaha, that guy at the\x01",
            "open mic is pretty good\x01",
            "too.\x02",
        )
    )

    Sleep(1500)
    OP_57(0x0)
    OP_5A()
    Sleep(1700)
    ClearScenarioFlags(0x2, 3)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x34, 1)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0x34, 0x20)
    SetScenarioFlags(0x2, 4)
    SetScenarioFlags(0x2, 3)
    BeginChrThread(0xF, 0, 0, 81)
    BeginChrThread(0x34, 0, 0, 81)
    BeginChrThread(0x34, 2, 0, 85)
    BeginChrThread(0xF, 2, 0, 84)
    OP_63(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x12, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x13, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    Sleep(3200)
    ClearScenarioFlags(0x2, 3)
    SetScenarioFlags(0x2, 3)

    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Alright, heeere we go,\x01",
            "everyone!!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#4SEnjoy, Mishy☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x34, 0x2)
    SetChrFlags(0x34, 0x10)
    SetChrFlags(0x34, 0x20)
    SetChrChipByIndex(0x34, 0x22)
    SetChrSubChip(0x34, 0x0)
    OP_0D()
    ClearScenarioFlags(0x2, 4)
    SetScenarioFlags(0x2, 4)
    BeginChrThread(0xF, 0, 0, 83)
    BeginChrThread(0xF, 2, 0, 88)
    BeginChrThread(0x34, 2, 0, 89)
    WaitChrThread(0xF, 2)
    WaitChrThread(0x34, 2)
    ClearScenarioFlags(0x2, 3)
    ClearScenarioFlags(0x2, 4)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(30, 140, -1, -1)
    SetChrName("Spectators")

    AnonymousTalk(
        0xFF,
        "#4SEnjoy!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetChrName("Spectators")

    AnonymousTalk(
        0xFF,
        "#4SMishy☆\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x12, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x13, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    Sleep(1200)
    OP_64(0x34)
    OP_63(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x12, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x13, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    Fade(1000)
    OP_68(8000, 1800, -1810, 0)
    MoveCamera(42, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12910, 0)
    ClearChrFlags(0x34, 0x2)
    ClearChrFlags(0x34, 0x10)
    ClearChrFlags(0x34, 0x20)
    SetChrChipByIndex(0x34, 0x21)
    SetChrSubChip(0x34, 0x0)
    OP_93(0x34, 0x10E, 0x0)
    SetChrPos(0x101, 2520, -700, -410, 90)
    SetChrPos(0x102, 2520, -700, -1650, 90)
    SetChrPos(0x109, 1430, -700, -2270, 90)
    SetChrPos(0x105, 1410, -700, -1020, 90)
    SetChrPos(0x104, 1440, -700, 200, 90)
    OP_0D()
    Sleep(500)

    def lambda_E2E0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_E2E0)
    Sleep(10)

    def lambda_E2F0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_E2F0)
    WaitChrThread(0x34, 1)

    def lambda_E301():
        OP_9B(0x0, 0xFE, 0x0, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_E301)
    Sleep(10)

    def lambda_E319():
        OP_9B(0x0, 0xFE, 0x0, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_E319)
    WaitChrThread(0x34, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Mishy and Olivier firmly\x01",
            "shook each other's\x01",
            "hands.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x34,
        (
            "#12P#13909FHa ha ha... Well done,\x01",
            "Mishy.\x02\x03",
            "#13902FYour dancing sense...\x01",
            "I'll be blunt. My hat's\x01",
            "off to you, my friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, you're pretty\x01",
            "good too, mister☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Where did you learn to\x01",
            "dance like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        (
            "#12P#13904FI'm quite fond of ballroom\x01",
            "dancing.\x02\x03",
            "Normally I prefer an elegant\x01",
            "dance with a lady, but it was\x01",
            "pretty fun dancing with you too.\x02\x03",
            "#13902FI would expect no less from\x01",
            "Crossbell's greatest mascot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, I'm so\x01",
            "embarrassed～☆\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(1760, 1600, -3500, 0)
    MoveCamera(44, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12200, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00006F(W-What the hell is he\x01",
            "doing?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300F(Looks like he barged\x01",
            "onto the stage.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106F(Mueller asked us to do this as\x01",
            "inconspicuously as possible, but\x01",
            "it seems impossible like this...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x34, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_E6F0():
        OP_9B(0x1, 0xFE, 0xB4, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_E6F0)
    Sleep(10)

    def lambda_E708():
        OP_9B(0x1, 0xFE, 0xB4, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_E708)
    WaitChrThread(0x34, 1)
    OP_93(0x34, 0x10E, 0x1F4)
    Fade(500)
    OP_68(8000, 1800, -1810, 0)
    MoveCamera(42, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12910, 0)
    OP_0D()

    ChrTalk(
        0x34,
        (
            "#12P#13905FWhat's this... It seems\x01",
            "there's someone here for\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x34, 0x0, 0x1F4)
    OP_6F(0x79)

    ChrTalk(
        0x34,
        (
            "#12P#13900FI'm sorry Mishy, but\x01",
            "we'll part ways here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Awww, too baaad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, come to\x01",
            "Wonderland next time\x01",
            "too, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        (
            "#12P#13902FYour wish... I will carry\x01",
            "it out someday. This I\x01",
            "swear.\x02\x03",
            "#13904FI cannot bear to be apart\x01",
            "from you. That is why\x01",
            "bonds are irreplaceable.\x02\x03",
            "#13913FAdios, amigo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Bye bye～☆\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrFlags(0x34, 0x2)
    SetChrFlags(0x34, 0x10)
    SetChrFlags(0x34, 0x20)
    SetChrChipByIndex(0x34, 0x22)
    SetChrSubChip(0x34, 0x0)
    OP_0D()
    BeginChrThread(0x34, 2, 0, 89)
    WaitChrThread(0x34, 2)
    OP_64(0x34)
    Fade(500)
    ClearChrFlags(0x34, 0x2)
    ClearChrFlags(0x34, 0x10)
    ClearChrFlags(0x34, 0x20)
    SetChrFlags(0x34, 0x40)
    SetChrChipByIndex(0x34, 0x21)
    SetChrSubChip(0x34, 0x0)
    OP_93(0x34, 0x0, 0x0)
    OP_0D()

    def lambda_E94A():

        label("loc_E94A")

        TurnDirection(0xFE, 0x34, 500)
        Yield()
        Jump("loc_E94A")

    QueueWorkItem2(0xF, 2, lambda_E94A)
    OP_68(8890, 1800, 4180, 2000)
    OP_95(0x34, 10730, -700, 580, 4000, 0x0)
    OP_95(0x34, 10620, -700, 3010, 5000, 0x0)
    Sound(809, 0, 70, 0)
    OP_9D(0x34, 0x28DC, 0x0, 0x2440, 0xBB8, 0xBB8)
    Sound(30, 0, 100, 0)
    EndChrThread(0xF, 0x2)
    OP_95(0x34, 4950, 0, 15760, 4000, 0x0)
    SetChrFlags(0x34, 0x80)
    OP_6F(0x1)
    StopBGM(0xFA0)
    OP_93(0x101, 0x0, 0x0)
    OP_93(0x102, 0x0, 0x0)
    OP_93(0x104, 0x0, 0x0)
    OP_93(0x109, 0x0, 0x0)
    OP_93(0x105, 0x0, 0x0)
    Fade(1000)
    OP_68(2820, 1800, -3080, 0)
    MoveCamera(42, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12910, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#12P#00011FH-He got away again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10306FMan. Looks like he's used\x01",
            "to this sort of thing.\x02\x03",
            "#10300FHe escaped from here too.\x01",
            "That narrows the places\x01",
            "he's likely to be further.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FA-Anyway, let's chase\x01",
            "after him!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 1570, -700, -240, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ModifyEventFlags(0, 4, 0x80)
    ModifyEventFlags(0, 5, 0x80)
    SetScenarioFlags(0x156, 3)
    OP_29(0x76, 0x1, 0x3)
    SetChrPos(0xF, 9480, -700, 160, 270)
    ClearChrFlags(0xF, 0x10)
    OP_4C(0xF, 0xFF)
    BeginChrThread(0xF, 0, 0, 0)
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x10)
    ClearChrFlags(0x14, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x8, 0x80)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)
    StopSound(821, 1000, 30)
    EventEnd(0x5)
    Return()

    # Function_80_DC13 end

    def Function_81_EBB3(): pass

    label("Function_81_EBB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_EBCF")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(100)
    Jump("Function_81_EBB3")

    label("loc_EBCF")

    Return()

    # Function_81_EBB3 end

    def Function_82_EBD0(): pass

    label("Function_82_EBD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_EBEC")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(50)
    Jump("Function_82_EBD0")

    label("loc_EBEC")

    Return()

    # Function_82_EBD0 end

    def Function_83_EBED(): pass

    label("Function_83_EBED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_EC09")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_83_EBED")

    label("loc_EC09")

    Return()

    # Function_83_EBED end

    def Function_84_EC0A(): pass

    label("Function_84_EC0A")

    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0xFFFFF5D8, 0x7D0, 0x0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0xBB8)
    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0xFFFFFC18, 0x7D0, 0x0)
    OP_96(0xFE, 0x1FF4, 0xFFFFFD44, 0xFFFFFF06, 0x7D0, 0x0)
    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0x258, 0x7D0, 0x0)
    Return()

    # Function_84_EC0A end

    def Function_85_EC7D(): pass

    label("Function_85_EC7D")

    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0x834, 0x7D0, 0x0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0xBB8)
    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0x258, 0x7D0, 0x0)
    OP_96(0xFE, 0x28F0, 0xFFFFFD44, 0xFFFFFF06, 0x7D0, 0x0)
    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0xFFFFFC18, 0x7D0, 0x0)
    Return()

    # Function_85_EC7D end

    def Function_86_ECF0(): pass

    label("Function_86_ECF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_EE03")
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(100)
    SetScenarioFlags(0x2, 4)
    BeginChrThread(0xFE, 0, 0, 82)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    ClearScenarioFlags(0x2, 4)
    OP_93(0xFE, 0x10E, 0x0)
    Sleep(100)
    OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    OP_97(0xFE, 0x1F4, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    SetScenarioFlags(0x2, 4)
    BeginChrThread(0xFE, 0, 0, 82)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    ClearScenarioFlags(0x2, 4)
    Jump("Function_86_ECF0")

    label("loc_EE03")

    Return()

    # Function_86_ECF0 end

    def Function_87_EE04(): pass

    label("Function_87_EE04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_EF17")
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(100)
    SetScenarioFlags(0x2, 4)
    BeginChrThread(0xFE, 0, 0, 82)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    ClearScenarioFlags(0x2, 4)
    OP_93(0xFE, 0x5A, 0x0)
    Sleep(100)
    OP_97(0xFE, 0x1F4, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    SetScenarioFlags(0x2, 4)
    BeginChrThread(0xFE, 0, 0, 82)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    ClearScenarioFlags(0x2, 4)
    Jump("Function_87_EE04")

    label("loc_EF17")

    Return()

    # Function_87_EE04 end

    def Function_88_EF18(): pass

    label("Function_88_EF18")

    Sound(809, 0, 80, 0)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0xBB8)
    OP_93(0xFE, 0x10E, 0x0)
    Return()

    # Function_88_EF18 end

    def Function_89_EF3D(): pass

    label("Function_89_EF3D")

    OP_63(0xFE, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(130)
    Sound(822, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(130)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    SetChrSubChip(0xFE, 0x3)
    Sleep(130)
    SetChrSubChip(0xFE, 0x4)
    Sleep(130)
    SetChrSubChip(0xFE, 0x5)
    Sleep(130)
    SetChrSubChip(0xFE, 0x6)
    Sleep(130)
    SetChrSubChip(0xFE, 0x7)
    Return()

    # Function_89_EF3D end

    def Function_90_EF8B(): pass

    label("Function_90_EF8B")

    EventBegin(0x0)
    Fade(500)
    OP_68(-12070, 2500, 10460, 0)
    MoveCamera(45, 29, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(15780, 0)
    SetChrPos(0x101, -9870, 0, 11840, 0)
    SetChrPos(0x102, -11070, 0, 11840, 0)
    SetChrPos(0x103, -9870, 0, 10640, 0)
    SetChrPos(0x104, -11070, 0, 10640, 0)
    SetChrPos(0x109, -11070, 0, 9440, 0)
    SetChrPos(0x105, -9870, 0, 9440, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F06A")
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    Jump("loc_F07E")

    label("loc_F06A")

    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)

    label("loc_F07E")

    OP_0D()

    ChrTalk(
        0x9,
        (
            "So you've come. Come on,\x01",
            "come eat my noodles!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FU-Umm, we're from the\x01",
            "Special Support\x01",
            "Section...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained that you came\x01",
            "for "gourmet\x01",
            "recommendations" coverage.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "Ah, that, eh? I heard\x01",
            "about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You're in luck. And that's because\x01",
            "you'll be able to fully appreciate\x01",
            "my supreme noodles for free!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Come on, eat. These are\x01",
            "my "Heavenly Noodles\x01",
            "<Sun>"!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FHm, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FThe deep red soup looks\x01",
            "very spicy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hehe. Eat it, and\x01",
            "without complaining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You'll be tempted by the\x01",
            "heavenly taste that lies\x01",
            "beyond that spiciness!!\x02",
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
        0x101,
        (
            "#00003F(His enthusiasm concerns\x01",
            "me, but...) I-In any case,\x01",
            "let's try eating it.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-9560, 2500, 11630, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(15700, 0)
    SetChrPos(0x9, -9810, 0, 13520, 135)
    SetChrPos(0x104, -8390, 0, 12300, 0)
    SetChrPos(0x101, -8250, 0, 11290, 0)
    SetChrPos(0x102, -7150, 0, 12270, 315)
    SetChrPos(0x103, -6100, 0, 12250, 315)
    SetChrPos(0x105, -9920, 0, 11790, 45)
    SetChrPos(0x109, -6860, 0, 11350, 315)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others ate\x01",
            "the Heavenly Noodles\x01",
            "<Sun>.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
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
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F*slurp slurp*... Indeed,\x01",
            "they aren't just spicy, they\x01",
            "have a deep taste as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FYes, they really are\x01",
            "delicious...\x02\x03",
            "#00106FHowever, the soup\x01",
            "splashes are a concern,\x01",
            "aren't they.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112FI-Indeed... It'd be\x01",
            "tough to remove the\x01",
            "stains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Mrrr... My female customers\x01",
            "are always thinking along\x01",
            "those lines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you get to eat first-rate\x01",
            "noodles, soup splashes are\x01",
            "an insignificant problem!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F...Yeah, exactly.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#00205F...Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FThe world of rich flavors expanding\x01",
            "beyond this soup's exquisite\x01",
            "spiciness...\x02\x03",
            "Then, the springy, curly noodles coiling\x01",
            "around in that soup... This quality is\x01",
            "something only a man could understand.\x02\x03",
            "#00302FSomehow I feel like I too understand the\x01",
            "ol'man's strong feelings toward these\x01",
            "noodles.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F9F2")

    ChrTalk(
        0x9,
        (
            "Ooh... That's right, that's\x01",
            "right! Then there was a\x01",
            "promising youngster among you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Fine, I'll specially\x01",
            "teach you the base\x01",
            "recipe of these noodles!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Devote all your self to\x01",
            "it!!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the \x07\x02",
            ""Spicy Hot\x01",
            "Flat Noodles"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_FAE4")

    label("loc_F9F2")


    ChrTalk(
        0x9,
        (
            "Ooh... That's right, that's\x01",
            "right! Then there was a\x01",
            "promising youngster among you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Alright, I'll give you\x01",
            "another helping of my\x01",
            "special!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Please enjoy it!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x190),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x190, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_FAE4")

    TurnDirection(0x104, 0x9, 500)

    ChrTalk(
        0x104,
        "#00309FOhh, thanks ol'man!\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00009F(Randy... It seems he\x01",
            "liked them a lot.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F(Hehe, then we should\x01",
            "leave this place's\x01",
            "introduction to him, eh?)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x2, 7)
    SetScenarioFlags(0x172, 2)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_FC73")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FC73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_FC90")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FC90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_FCA3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FCA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_FCB6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FCB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_FCD3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FCD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_FCE6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FCE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_FD03")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FD03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_FD16")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FD16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_FD33")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FD33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_FD46")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FD46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_FD63")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FD63")

    OP_29(0x80, 0x1, 0x3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FE6E")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Finished covering 6\x01",
            "restaurants!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_FE65")

    AnonymousTalk(
        0x101,
        (
            "#00003FIt seems we could go report to\x01",
            "Grace immediately, but...\x02\x03",
            "#00000FWe haven't found all 6\x01",
            "members' favorites yet, so why\x01",
            "don't we try a little harder?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_FE65")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_FE6E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FF63")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Found all SSS members'\x01",
            "favorites!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00004FWith this, we found all 6\x01",
            "members' favorites.\x02\x03",
            "#00000FWe've got plenty of coverage with\x01",
            "this. Let's head to the news\x01",
            "agency right away and report.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_FF63")

    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0xB4, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_FFDF")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, -52470, 2000, 21150, 90)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xD, -18000, 0, -5750, 90)
    BeginChrThread(0xD, 0, 0, 4)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrPos(0xE, 13000, 0, -10000, 0)
    BeginChrThread(0xE, 0, 0, 5)
    Jump("loc_10021")

    label("loc_FFDF")

    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, -13200, 0, 11500, 90)
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, -52470, 2000, 21150, 90)
    BeginChrThread(0xA, 0, 0, 2)

    label("loc_10021")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -10470, 0, 11840, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_90_EF8B end

    def Function_91_1004D(): pass

    label("Function_91_1004D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    LoadChrToIndex("chr/ch47500.itc", 0x28)
    LoadChrToIndex("chr/ch27800.itc", 0x29)
    SoundLoad(462)
    SoundLoad(461)
    SoundLoad(470)
    SoundLoad(457)
    ClearChrFlags(0x32, 0x80)
    SetChrFlags(0x32, 0x8000)
    SetMapObjFlags(0xA, 0x1000)
    ClearMapObjFlags(0xA, 0x4)
    OP_78(0xA, 0x32)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x32, -3570, 2000, 21710, 270)
    OP_D5(0x32, 0x0, 0x41EB0, 0x0, 0x0)
    OP_68(17650, 0, -4330, 0)
    MoveCamera(42, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26020, 0)
    SetChrChipByIndex(0x30, 0x28)
    SetChrSubChip(0x30, 0x0)
    ClearChrFlags(0x30, 0x80)
    SetChrFlags(0x30, 0x8000)
    SetChrChipByIndex(0x31, 0x29)
    SetChrSubChip(0x31, 0x0)
    ClearChrFlags(0x31, 0x80)
    SetChrFlags(0x31, 0x8000)
    SetChrPos(0x30, 16050, 0, -6150, 270)
    SetChrPos(0x31, 19620, -10, 4000, 180)
    SetChrPos(0x101, 340, -470, 5300, 315)
    SetChrPos(0x104, 1700, -620, 4480, 315)
    SetChrPos(0x105, 150, -700, 3820, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_10187():
        OP_9B(0x0, 0x31, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_10187)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_93(0x30, 0xB4, 0x1F4)
    Sleep(1000)
    OP_93(0x30, 0x10E, 0x1F4)
    Sleep(1000)
    OP_93(0x30, 0xB4, 0x1F4)
    Sleep(800)
    OP_93(0x30, 0x10E, 0x1F4)
    WaitChrThread(0x31, 1)
    TurnDirection(0x31, 0x30, 500)

    ChrTalk(
        0x31,
        (
            "Clyde, sorry to have\x01",
            "kept you waiting.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x30, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x30, 0x31, 500)
    Sleep(500)
    OP_68(20210, 0, -4730, 2000)
    OP_9B(0x0, 0x30, 0x0, 0x7D0, 0x5DC, 0x0)
    WaitChrThread(0x30, 1)
    OP_6F(0x1)
    Sleep(500)

    ChrTalk(
        0x31,
        (
            "I brought what we talked\x01",
            "about.\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x30, 0x0, 0x1F4, 0x5DC, 0x0)
    WaitChrThread(0x30, 1)
    Sleep(200)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Clyde received an\x01",
            "attachｳ case\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_9B(0x1, 0x30, 0xB4, 0x1F4, 0x5DC, 0x0)
    WaitChrThread(0x30, 1)

    ChrTalk(
        0x30,
        "Thanks, and nice work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        "And... How did it go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        (
            "Well, it seems she's\x01",
            "quite interested in it\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        (
            "It's going to be decided\x01",
            "for sure at Neue-Blanc\x01",
            "later!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        "Haha, that's perfect.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "...Oh, it's about time for\x01",
            "the water bus to leave. I'll\x01",
            "go finish the preparations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "Then, I'm counting on you. If you\x01",
            "can secure this contract, the top\x01",
            "spot is as good as yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        (
            "Yes, please leave it to\x01",
            "me!!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x31, 1, 0, 92)
    OP_68(22840, 0, -4880, 3000)
    Sleep(1500)

    def lambda_104AF():
        OP_9B(0x0, 0x30, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_104AF)
    WaitChrThread(0x30, 1)

    def lambda_104C8():

        label("loc_104C8")

        TurnDirection(0xFE, 0x31, 500)
        Yield()
        Jump("loc_104C8")

    QueueWorkItem2(0x30, 1, lambda_104C8)
    Sleep(4000)
    EndChrThread(0x30, 0x1)

    ChrTalk(
        0x30,
        (
            "Alright... Let's do\x01",
            "this!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x30, 0x0, 2000, 0x8, 0x9, 0xFA, 0x6)
    Sound(27, 0, 100, 0)

    def lambda_10518():
        OP_9B(0x0, 0x30, 0x10E, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_10518)
    Sleep(2000)
    Fade(500)
    OP_68(-2520, 0, 26110, 0)
    MoveCamera(42, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(31670, 0)
    SetChrPos(0x30, 1100, 2000, 23760, 270)
    OP_63(0x30, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)

    def lambda_1058C():
        OP_9B(0x0, 0x30, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_1058C)
    WaitChrThread(0x30, 1)

    def lambda_105A5():
        OP_93(0x30, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_105A5)
    WaitChrThread(0x30, 1)
    OP_71(0xA, 0xF1, 0x10E, 0x1, 0x0)
    Sound(462, 0, 100, 0)
    OP_79(0xA)
    OP_64(0x30)

    def lambda_105CE():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_105CE)

    def lambda_105E3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x30, 2, lambda_105E3)
    WaitChrThread(0x30, 1)
    WaitChrThread(0x30, 2)
    OP_71(0xA, 0x10F, 0x12C, 0x1, 0x0)
    Sound(461, 0, 100, 0)
    OP_79(0xA)
    ClearChrFlags(0x32, 0x80)
    OP_78(0xA, 0x32)
    OP_49()
    SetChrPos(0x32, -3570, 2000, 21710, 270)
    OP_D5(0x32, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x79, 0xB4, 0x1, 0x20)
    OP_0D()
    Sound(470, 0, 100, 0)
    SetCameraDistance(30470, 3000)
    OP_0D()
    Sleep(800)
    Sleep(800)
    OP_68(-15880, 0, 26510, 3000)
    Sound(457, 0, 100, 0)

    def lambda_10696():
        OP_98(0xFE, 0xFFFF8AD0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_10696)
    OP_71(0xA, 0x79, 0xB4, 0x0, 0x20)
    WaitChrThread(0x32, 1)
    OP_6F(0x11)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x32, 0x80)
    ClearChrFlags(0x32, 0x8000)
    ClearMapObjFlags(0xA, 0x1000)
    SetMapObjFlags(0xA, 0x4)
    OP_0D()
    Sleep(500)
    OP_68(2060, 0, 7960, 5000)
    MoveCamera(39, 19, 0, 5000)
    OP_6E(400, 5000)
    SetCameraDistance(27560, 5000)
    OP_0D()
    OP_6F(0x1)
    Sleep(500)

    ChrTalk(
        0x104,
        (
            "#00305FHe went off somewhere in high\x01",
            "spirits, eh?\x02\x03",
            "#00303FIt seems he has an appointment\x01",
            "with that vice chief's wife at\x01",
            "Neue-Blanc, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHehe, what do we do?\x01",
            "There's no point in\x01",
            "tailing him further.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWe'll contact Elie and\x01",
            "the others and return to\x01",
            "police HQ for now.\x02\x03",
            "#00001FI think I have a rough\x01",
            "idea of Clyde's true\x01",
            "identity.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("c1160", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_91_1004D end

    def Function_92_108A1(): pass

    label("Function_92_108A1")

    ClearChrFlags(0x31, 0x4)
    OP_9B(0x0, 0x31, 0x10E, 0xFA0, 0x7D0, 0x0)
    OP_9B(0x0, 0x31, 0x10E, 0x1770, 0x7D0, 0x0)
    OP_9B(0x0, 0x31, 0x10E, 0x1B58, 0x7D0, 0x0)
    OP_9B(0x0, 0x31, 0x5A, 0x1B58, 0x7D0, 0x0)
    OP_9B(0x0, 0x31, 0x0, 0x2710, 0x7D0, 0x0)
    SetChrFlags(0x31, 0x4)
    Return()

    # Function_92_108A1 end

    def Function_93_108F7(): pass

    label("Function_93_108F7")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(35980, -1400, 370, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17240, 0)
    SetChrPos(0x101, 35590, -2500, 10, 90)
    SetChrPos(0x102, 35400, -2500, 980, 90)
    SetChrPos(0x103, 34850, -2500, -1070, 90)
    SetChrPos(0x104, 34050, -2500, -40, 90)
    SetChrPos(0x109, 33500, -2500, 960, 90)
    SetChrPos(0x105, 33050, -2500, -730, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x24, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10C12")
    SetScenarioFlags(0x176, 2)

    ChrTalk(
        0x24,
        (
            "Water bus bound for\x01",
            "Michelam, departing\x01",
            "shooortlyyy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        "All passengers aboooard!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FThat's right... We got a\x01",
            "request from the theme\x01",
            "park, didn't we.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FI think it was something\x01",
            "about helping Mishy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10103FHmm. Just what kind of\x01",
            "job is it, I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203F...Anyway, let's head\x01",
            "there ASAP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FHaha, you sure look\x01",
            "eager, PeTiote.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHaha, I get the feeling\x01",
            "this is going to be fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F(If we cross to Michelam, we should\x01",
            "accept the request unless there's a\x01",
            "very good reason not to.)\x02\x03",
            "(Should we go now?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10C12")

    Call(0, 94)
    Return()

    # Function_93_108F7 end

    def Function_94_10C16(): pass

    label("Function_94_10C16")

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
            "Go to the theme park\x01",      # 0
            "Cancel\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_10C82"),
        (1, "loc_10F19"),
        (SWITCH_DEFAULT, "loc_11002"),
    )


    label("loc_10C82")


    ChrTalk(
        0x101,
        (
            "#6P#00000FAlright then, let's head\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x14, 0x80)
    SoundLoad(479)
    ClearChrFlags(0x2E, 0x80)
    OP_78(0x5, 0x2E)
    OP_49()
    OP_D5(0x2E, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    SetChrPos(0x2E, 51800, -3850, -4000, 0)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    OP_68(35920, 400, -3820, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16670, 0)
    OP_70(0x5, 0x1F)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrPos(0x2E, 126220, -3850, -50690, 315)
    OP_D5(0x2E, 0x0, 0x4CE78, 0x0, 0x0)
    OP_D5(0x2E, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x2E, 51800, -3850, -4000, 0)
    OP_71(0x5, 0x1F, 0x5A, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(1000)
    Sound(478, 0, 100, 0)
    OP_79(0x9)
    Sound(477, 0, 100, 0)
    Sleep(200)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)

    def lambda_10E0F():
        OP_98(0xFE, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_10E0F)
    WaitChrThread(0x2E, 1)

    def lambda_10E2D():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_10E2D)
    Sleep(2000)
    StopSound(126, 1000, 50)
    FadeToDark(1000, 0, -1)
    WaitChrThread(0x2E, 1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_24(0x1DF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others\x01",
            "boarded the water bus and\x01",
            "headed for Michelam...\x02\x03",
            "They approached the client\x01",
            "who was waiting for them in\x01",
            "front of the theme park.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 2)
    NewScene("t1030", 0, 0, 0)
    IdleLoop()
    Jump("loc_11002")

    label("loc_10F19")


    ChrTalk(
        0x101,
        (
            "#6P#00003F...Let's come back\x01",
            "another time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When heading to Michelam\x01",
            "for the quest, please\x01",
            "check the schedule.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 33190, -2500, 0, 270)
    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x24, 0xFF)
    ModifyEventFlags(0, 6, 0x80)
    EventEnd(0x5)
    Jump("loc_11002")

    label("loc_11002")

    Return()

    # Function_94_10C16 end

    def Function_95_11003(): pass

    label("Function_95_11003")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x0, 38840, -2500, -460, 270)
    OP_69(0xFF, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_95_11003 end

    def Function_96_11031(): pass

    label("Function_96_11031")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(479)
    OP_68(35920, 400, -3820, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16670, 0)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x2E, 0x80)
    OP_78(0x5, 0x2E)
    OP_49()
    OP_D5(0x2E, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    SetChrPos(0x2E, 51800, -3850, -4000, 0)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    SetChrPos(0x2E, 126220, -3850, -50690, 315)
    OP_D5(0x2E, 0x0, 0x4CE78, 0x0, 0x0)
    BeginChrThread(0x2F, 1, 0, 97)
    SetMapObjFrame(0xFF, "yuragi01_add", 0x0, 0x1)
    OP_68(59280, 17600, -8870, 0)
    MoveCamera(90, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(51010, 0)
    OP_68(59280, 8000, -8870, 10000)

    def lambda_11166():
        OP_9B(0x1, 0xFE, 0x0, 0xC350, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_11166)
    Sound(475, 0, 100, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(7000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    SetMapObjFrame(0xFF, "yuragi01_add", 0x1, 0x1)
    OP_68(35920, 400, -3820, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16670, 0)
    OP_D5(0x2E, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x2E, 54800, -3850, -4000, 0)
    Sound(476, 0, 100, 0)
    Sound(477, 0, 100, 0)

    def lambda_11217():
        OP_98(0xFE, 0xFFFFF448, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_11217)
    WaitChrThread(0x2E, 1)
    OP_82(0x32, 0x0, 0xBB8, 0x1F4)
    Sound(478, 0, 100, 0)
    Sleep(2000)
    Fade(500)
    SetMapObjFlags(0x7, 0x4)
    OP_68(40510, 400, -3870, 0)
    MoveCamera(56, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11290, 0)
    OP_0D()
    OP_71(0x5, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x5)
    OP_71(0x5, 0x12D, 0x168, 0x0, 0x20)
    OP_71(0x5, 0x1, 0x1E, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x5)
    OP_71(0x5, 0xF1, 0x12C, 0x0, 0x20)
    Sleep(500)
    SetChrPos(0x101, 49180, -2500, -1680, 270)
    SetChrPos(0x102, 49180, -2500, -1680, 270)
    SetChrPos(0x104, 49180, -2500, -1680, 270)
    SetChrPos(0x109, 49180, -2500, -1680, 270)
    SetChrPos(0x105, 49180, -2500, -1680, 270)
    SetChrPos(0x103, 49180, -2500, -1680, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 98)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 99)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 100)
    Sleep(700)
    OP_68(36510, 400, -1860, 5000)
    BeginChrThread(0x109, 3, 0, 101)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 102)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 103)
    WaitChrThread(0x103, 3)
    OP_6F(0x1)

    ChrTalk(
        0x103,
        "#00200F............\x02",
    )

    CloseMessageWindow()

    def lambda_113E8():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_113E8)
    Sleep(50)

    def lambda_113F8():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_113F8)
    Sleep(50)

    def lambda_11408():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11408)
    Sleep(50)

    def lambda_11418():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11418)
    Sleep(50)

    def lambda_11428():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11428)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00305FUh, Lloyd? I think you\x01",
            "broke Tio.\x02\x03",
            "She's been like that\x01",
            "ever since we got on the\x01",
            "water bus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FYes... She's been\x01",
            "staring off into space\x01",
            "this whole time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FShe looks lonely,\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FH-Hmm... I'm not sure\x01",
            "how to put it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FUmm, Tio? Are you\x01",
            "feeling sick?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...No. I'm fine.\x02\x03",
            "#00202FI'm just a little\x01",
            "confused. I'll have things\x01",
            "sorted out momentarily.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x5A, 0x1F4)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00208F...So this is how a\x01",
            "person becomes an adult,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Theme Park Part-\x01",
            "Time Job]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x86, 0x1, 0x9)
    OP_29(0x86, 0x1, 0xA)
    OP_29(0x86, 0x4, 0x10)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x3, 0x1)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearMapObjFlags(0x7, 0x4)
    SetChrPos(0x2E, 51800, -3850, -2300, 0)
    SetChrFlags(0x2E, 0x80)
    ClearChrFlags(0x16, 0x10)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x16, 40740, -2500, -2330, 180)
    SetChrPos(0x17, 40630, -2500, -3760, 0)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x0, 36990, -2500, 190, 270)
    OP_69(0xFF, 0x0)
    OP_24(0x1DF)
    EventEnd(0x5)
    Return()

    # Function_96_11031 end

    def Function_97_1179E(): pass

    label("Function_97_1179E")

    Sound(479, 2, 0, 0)
    Sleep(100)
    OP_25(0x1DF, 0xA)
    Sleep(100)
    OP_25(0x1DF, 0x14)
    Sleep(100)
    OP_25(0x1DF, 0x1E)
    Sleep(100)
    OP_25(0x1DF, 0x28)
    Sleep(100)
    OP_25(0x1DF, 0x32)
    Sleep(100)
    OP_25(0x1DF, 0x3C)
    Sleep(100)
    OP_25(0x1DF, 0x46)
    Sleep(100)
    OP_25(0x1DF, 0x50)
    Sleep(100)
    OP_25(0x1DF, 0x5A)
    Sleep(100)
    OP_25(0x1DF, 0x64)
    Sleep(8000)
    OP_25(0x1DF, 0x5A)
    Sleep(100)
    OP_25(0x1DF, 0x50)
    Sleep(100)
    OP_25(0x1DF, 0x46)
    Sleep(100)
    OP_25(0x1DF, 0x3C)
    Sleep(100)
    OP_25(0x1DF, 0x32)
    Sleep(100)
    OP_25(0x1DF, 0x28)
    Sleep(100)
    OP_25(0x1DF, 0x1E)
    Sleep(100)
    OP_25(0x1DF, 0x14)
    Sleep(100)
    OP_25(0x1DF, 0xA)
    Sleep(100)
    OP_24(0x1DF)
    Return()

    # Function_97_1179E end

    def Function_98_11830(): pass

    label("Function_98_11830")


    def lambda_11835():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11835)

    def lambda_11846():
        OP_95(0xFE, 41760, -2500, -1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11846)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 37640, -2500, 320, 2000, 0x0)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_98_11830 end

    def Function_99_1187B(): pass

    label("Function_99_1187B")


    def lambda_11880():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11880)

    def lambda_11891():
        OP_95(0xFE, 41760, -2500, -1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11891)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 37640, -2500, -1280, 2000, 0x0)
    OP_93(0x102, 0x2D, 0x1F4)
    Return()

    # Function_99_1187B end

    def Function_100_118C6(): pass

    label("Function_100_118C6")


    def lambda_118CB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_118CB)

    def lambda_118DC():
        OP_95(0xFE, 41760, -2500, -1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_118DC)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 38890, -2500, 1500, 2000, 0x0)
    OP_93(0x104, 0xB4, 0x1F4)
    Return()

    # Function_100_118C6 end

    def Function_101_11911(): pass

    label("Function_101_11911")


    def lambda_11916():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_11916)

    def lambda_11927():
        OP_95(0xFE, 41760, -2500, -1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11927)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 39690, -2500, -1720, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_101_11911 end

    def Function_102_1195C(): pass

    label("Function_102_1195C")


    def lambda_11961():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_11961)

    def lambda_11972():
        OP_95(0xFE, 41760, -2500, -1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11972)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 40640, -2500, 1110, 2000, 0x0)
    OP_93(0x105, 0xE1, 0x1F4)
    Return()

    # Function_102_1195C end

    def Function_103_119A7(): pass

    label("Function_103_119A7")


    def lambda_119AC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_119AC)

    def lambda_119BD():
        OP_95(0xFE, 41760, -2500, -1910, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_119BD)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 41340, -2500, -150, 1500, 0x0)
    OP_93(0x103, 0x10E, 0x1F4)
    Return()

    # Function_103_119A7 end

    def Function_104_119F2(): pass

    label("Function_104_119F2")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11ABF")

    ChrTalk(
        0x1A2,
        "Is East Street this way?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWell, no...\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "Thought so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "...I think I told you to\x01",
            "go via East Street...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FYou're right... Sorry.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_11B34")

    label("loc_11ABF")


    ChrTalk(
        0x1A2,
        (
            "Hey, making stops along\x01",
            "the way is fine, but spare\x01",
            "me the detours, got it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Take me to East Street\x01",
            "at once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11B34")

    SetChrPos(0x0, -28110, 2000, 23520, 90)
    EventEnd(0x4)
    Return()

    # Function_104_119F2 end

    def Function_105_11B48(): pass

    label("Function_105_11B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11BFA")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003F(If we cross to Michelam, we should\x01",
            "accept the request unless there's a\x01",
            "very good reason not to.)\x02\x03",
            "(Should we go now?)\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 94)
    Jump("loc_11C9E")

    label("loc_11BFA")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Michelam-Bound Water Bus - Schedule\x01",
            " \x01",
            "※The "Wonderland" theme park,\x01",
            "  pride of Michelam, is open!\x01",
            "  Please enjoy some fun moments!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)

    label("loc_11C9E")

    Return()

    # Function_105_11B48 end

    def Function_106_11C9F(): pass

    label("Function_106_11C9F")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　Lupinus River - No. 1 Lighthouse\x01",
            " \x01",
            "Authorized personnel only.\x01",
            "　　　　　～Crossbell City～\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_106_11C9F end

    SaveToFile()

Try(main)

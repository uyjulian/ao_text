from ScenarioHelper import *

def main():
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
        "Cunha",               # 1
        "Ozel",               # 2
        "Bishop",             # 3
        "Quinn old man",           # 4
        "Amisa",                 # 5
        "Nicole",                 # 6
        "Celine",               # 7
        "Missi",               # 8
        "MWL staff",         # 9
        "MWL staff",         # 10
        "Citizen",                   # 11
        "Citizen",                   # 12
        "Citizen",                   # 13
        "Citizen",                   # 14
        "tourist",                 # 15
        "tourist",                 # 16
        "A mechanic",                 # 17
        "Roy",                   # 18
        "Meyrin",               # 19
        "Zeit",               # 20
        "Keya",                 # 21
        "Suzuku",                 # 22
        "tourist",                 # 23
        "boy",                 # 24
        "Citizen",                   # 25
        "Mr. Joe Ridge",       # 26
        "Policeman",                   # 27
        "Policeman",                   # 28
        "Water bus guide",         # 29
        "Police car",               # 30
        "Nielsen",             # 31
        "Tsao",                 # 32
        "Row",                   # 33
        "Yuri",                 # 34
        "Sykes",               # 35
        "Reggie",                 # 36
        "Runaway vehicle",                 # 37
        "Police car",               # 38
        "Water-bus",               # 39
        "SE control",                 # 40
        "Clyde",               # 41
        "male",                   # 42
        "car",                     # 43
        "boat",                 # 44
        "Olivier",               # 45
        "Central square",               # 46
        "Nishi dori",                 # 47
        "Administrative district",                 # 48
        "Residential area",                 # 49
        "Entertainment district",                 # 50
        "East Street",                 # 51
        "old Town",                 # 52
        "Harbor district",                 # 53
        "IBC",                 # 54
        "Beside the station",               # 55
        "Back street",                 # 56
        "Ursula interchange",           # 57
        "East Crossbell Highway",       # 58
        "West Crossbell Highway",       # 59
        "Mainz Mountain Road",           # 60
        "Orchis Tower",         # 61
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

    PlaceName(-123.13999938964844, 0.0, -85.1500015258789, 0x0000, 0x0000, "Central square")
    PlaceName(-209.27000427246094, 0.0, -79.26000213623047, 0x0000, 0x0000, "Nishi dori")
    PlaceName(-87.7699966430664, 0.0, 31.440000534057617, 0x0000, 0x0000, "Administrative district")
    PlaceName(-289.17999267578125, 0.0, 18.34000015258789, 0x0000, 0x0000, "Residential area")
    PlaceName(-193.5500030517578, 0.0, 7.860000133514404, 0x0000, 0x0000, "Entertainment district")
    PlaceName(-16.700000762939453, 0.0, -115.27999877929688, 0x0000, 0x0000, "East Street")
    PlaceName(29.799999237060547, 0.0, -187.3300018310547, 0x0000, 0x0000, "old Town")
    PlaceName(19.979999542236328, 0.0, -28.81999969482422, 0x0000, 0x0000, "Harbor district")
    PlaceName(-14.079999923706055, 0.0, 94.31999969482422, 0x0000, 0x0000, "IBC")
    PlaceName(-108.4000015258789, 0.0, -175.5399932861328, 0x0000, 0x0000, "Beside the station")
    PlaceName(-169.97000122070312, 0.0, -39.29999923706055, 0x0000, 0x0000, "Back street")
    PlaceName(-112.33000183105469, 0.0, -216.14999389648438, 0x0000, 0x0000, "Ursula interchange")
    PlaceName(54.040000915527344, 0.0, -96.94000244140625, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-276.0799865722656, 0.0, -81.22000122070312, 0x0000, 0x0000, "West Crossbell Highway")
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
        "Function_12_33A3",        # 0C, 12
        "Function_13_48BB",        # 0D, 13
        "Function_14_5127",        # 0E, 14
        "Function_15_58E9",        # 0F, 15
        "Function_16_5A49",        # 10, 16
        "Function_17_5B92",        # 11, 17
        "Function_18_6005",        # 12, 18
        "Function_19_61ED",        # 13, 19
        "Function_20_62FE",        # 14, 20
        "Function_21_6406",        # 15, 21
        "Function_22_6521",        # 16, 22
        "Function_23_6662",        # 17, 23
        "Function_24_6709",        # 18, 24
        "Function_25_67BF",        # 19, 25
        "Function_26_6882",        # 1A, 26
        "Function_27_68B2",        # 1B, 27
        "Function_28_6A1E",        # 1C, 28
        "Function_29_6B5F",        # 1D, 29
        "Function_30_6B7D",        # 1E, 30
        "Function_31_6BB3",        # 1F, 31
        "Function_32_6BD7",        # 20, 32
        "Function_33_6C42",        # 21, 33
        "Function_34_6D31",        # 22, 34
        "Function_35_6E56",        # 23, 35
        "Function_36_6EF9",        # 24, 36
        "Function_37_7005",        # 25, 37
        "Function_38_70D1",        # 26, 38
        "Function_39_72C0",        # 27, 39
        "Function_40_7455",        # 28, 40
        "Function_41_764E",        # 29, 41
        "Function_42_795D",        # 2A, 42
        "Function_43_7AD8",        # 2B, 43
        "Function_44_7C38",        # 2C, 44
        "Function_45_81A4",        # 2D, 45
        "Function_46_83F7",        # 2E, 46
        "Function_47_84CB",        # 2F, 47
        "Function_48_8D64",        # 30, 48
        "Function_49_8E5E",        # 31, 49
        "Function_50_8E7D",        # 32, 50
        "Function_51_929E",        # 33, 51
        "Function_52_92E9",        # 34, 52
        "Function_53_934A",        # 35, 53
        "Function_54_93AB",        # 36, 54
        "Function_55_93DB",        # 37, 55
        "Function_56_9409",        # 38, 56
        "Function_57_9D2F",        # 39, 57
        "Function_58_9E2F",        # 3A, 58
        "Function_59_9E4D",        # 3B, 59
        "Function_60_9E81",        # 3C, 60
        "Function_61_9EB5",        # 3D, 61
        "Function_62_A4D0",        # 3E, 62
        "Function_63_A511",        # 3F, 63
        "Function_64_A545",        # 40, 64
        "Function_65_A579",        # 41, 65
        "Function_66_A5CA",        # 42, 66
        "Function_67_A638",        # 43, 67
        "Function_68_A6A6",        # 44, 68
        "Function_69_A714",        # 45, 69
        "Function_70_AB39",        # 46, 70
        "Function_71_AD1C",        # 47, 71
        "Function_72_B591",        # 48, 72
        "Function_73_BFEB",        # 49, 73
        "Function_74_C022",        # 4A, 74
        "Function_75_C06D",        # 4B, 75
        "Function_76_D1DD",        # 4C, 76
        "Function_77_D47D",        # 4D, 77
        "Function_78_D4C0",        # 4E, 78
        "Function_79_D570",        # 4F, 79
        "Function_80_D620",        # 50, 80
        "Function_81_E63A",        # 51, 81
        "Function_82_E657",        # 52, 82
        "Function_83_E674",        # 53, 83
        "Function_84_E691",        # 54, 84
        "Function_85_E704",        # 55, 85
        "Function_86_E777",        # 56, 86
        "Function_87_E88B",        # 57, 87
        "Function_88_E99F",        # 58, 88
        "Function_89_E9C4",        # 59, 89
        "Function_90_EA12",        # 5A, 90
        "Function_91_F9A1",        # 5B, 91
        "Function_92_101C5",       # 5C, 92
        "Function_93_1021B",       # 5D, 93
        "Function_94_10561",       # 5E, 94
        "Function_95_10920",       # 5F, 95
        "Function_96_1094E",       # 60, 96
        "Function_97_110E7",       # 61, 97
        "Function_98_11179",       # 62, 98
        "Function_99_111C4",       # 63, 99
        "Function_100_1120F",      # 64, 100
        "Function_101_1125A",      # 65, 101
        "Function_102_112A5",      # 66, 102
        "Function_103_112F0",      # 67, 103
        "Function_104_1133B",      # 68, 104
        "Function_105_11484",      # 69, 105
        "Function_106_115D0",      # 6A, 106
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('初级竿', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetItemNumber('小巧射手', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('竹竿', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢竿侵略者', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('水中支配者', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2030")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2192")
    Sound(14, 0, 100, 0)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('粉红液体', 1)"), scpexpr(EXPR_END)), "loc_211B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '粉红液体'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_218D")

    label("loc_211B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '粉红液体'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '粉红液体'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_218D")

    Jump("loc_21D7")

    label("loc_2192")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the treasure box.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_239A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2308")

    ChrTalk(
        0xFE,
        (
            "I was surprised by the sudden deployment to drift … ….\x01",
            "If you do not say it as strongly as this,\x01",
            "It is just being licked by two major powers, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So I, decidedly\x01",
            "I will support President Dieter!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I also have Director Arios … …\x01",
            "Already in the 2 biggest countries\x01",
            "Things I do not want only to do selfish!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2395")

    label("loc_2308")


    ChrTalk(
        0xFE,
        (
            "Of course I am worried … …\x01",
            "I am firm\x01",
            "I will support President Dieter!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Already in the 2 biggest countries\x01",
            "Things I do not want only to do selfish!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2395")

    Jump("loc_339F")

    label("loc_239A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2544")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2493")

    ChrTalk(
        0xFE,
        (
            "A completely destroyed company along the river ……\x01",
            "It is rumored that we have relations with the Republic government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because I understood it Empire hired\x01",
            "They were hit by a hunting corps … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Such circumstances do not matter … …\x01",
            "Anyway, with this crossbell\x01",
            "You do not want to do extra things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_253F")

    label("loc_2493")


    ChrTalk(
        0xFE,
        (
            "This was the situation that\x01",
            "Cross Bells forever\x01",
            "Because it is a dependent state … what is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, after all,\x01",
            "We clearly state the will of independence\x01",
            "I think it should be shown to neighboring countries.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_253F")

    Jump("loc_339F")

    label("loc_2544")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_26DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_263D")

    ChrTalk(
        0xFE,
        (
            "A guard engaged with an armed group,\x01",
            "It's pretty struggling …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the crossbell is independent\x01",
            "Armor can be strengthened, even in such a situation\x01",
            "It is a rumor that we can deal with it without any reason ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all … Cross Bell\x01",
            "I wonder if I should be independent … … …?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_26D8")

    label("loc_263D")


    ChrTalk(
        0xFE,
        (
            "If the crossbell is independent\x01",
            "Armor can be strengthened, even in such a situation\x01",
            "It is a rumor that we can deal with it without any reason ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all … Cross Bell\x01",
            "I wonder if I should be independent … … …?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26D8")

    Jump("loc_339F")

    label("loc_26DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_26EB")
    Jump("loc_339F")

    label("loc_26EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_288D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2817")

    ChrTalk(
        0xFE,
        (
            "At the present moment, already independent\x01",
            "There are many people who agree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Well, but I,\x01",
            "About the good or bad that still agrees or disagrees\x01",
            "I do not understand so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way tomorrow,\x01",
            "The theme of independence at the city hall\x01",
            "It seems there is a citizen forum …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Shall I ask you even now?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2888")

    label("loc_2817")


    ChrTalk(
        0xFE,
        (
            "Tomorrow, independence is the theme at the municipal hall\x01",
            "It seems there is a citizen forum …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Shall I ask you even now?\x02",
    )

    CloseMessageWindow()

    label("loc_2888")

    Jump("loc_339F")

    label("loc_288D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2932")

    ChrTalk(
        0xFE,
        (
            "Come to think of it, ask about the independence\x01",
            "Residents' vote is about a week later\x01",
            "Was it done?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, what shall I do.\x01",
            "I have to decide my position soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_339F")

    label("loc_2932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2A73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29F6")

    ChrTalk(
        0xFE,
        (
            "Ufufu, of alkane shell\x01",
            "Renewal stage,\x01",
            "It will be open soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The presence of additional casts\x01",
            "Finally became clear … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can not take my eyes off this already!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2A6E")

    label("loc_29F6")


    ChrTalk(
        0xFE,
        (
            "Additional cast girls,\x01",
            "You say it is Shri-chan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I still have an age to attend Sunday school ……\x01",
            "It's really amazing!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A6E")

    Jump("loc_339F")

    label("loc_2A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2BBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B66")

    ChrTalk(
        0xFE,
        (
            "I have not actually seen it,\x01",
            "Assurance of Yuria Associa\x01",
            "I do not really think it is a soldier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Separately, I never have such a hobby\x01",
            "I do not mean that ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're a dignified person\x01",
            "I want to be cuddly and hugged\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2BB5")

    label("loc_2B66")


    ChrTalk(
        0xFE,
        (
            "Haa ~, Assistant Yulia\x01",
            "It's really nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I want to be cuddly and hugged\x02",
    )

    CloseMessageWindow()

    label("loc_2BB5")

    Jump("loc_339F")

    label("loc_2BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_31AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C5B")

    ChrTalk(
        0xFE,
        (
            "A little early woman\x01",
            "I walked toward the east side of the street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With flowing long black hair\x01",
            "The appearance of the suit was decided,\x01",
            "I thought it was cool …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31A9")

    label("loc_2C5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DD6")

    ChrTalk(
        0xFE,
        (
            "Now, the eastern side of the women\x01",
            "Go through here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With flowing long black hair\x01",
            "The appearance of the suit was decided,\x01",
            "I thought it was cool …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(Oriental style woman, black hair ……?)\x02\x03",
            "#00001FWell, which one is that person?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, to the east side of the street\x01",
            "It seems they walked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FEast Street ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F(It is uncertain whether it is \"she\"\x01",
            "You might as well look for it. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    SetScenarioFlags(0x1C6, 6)
    Jump("loc_31A9")

    label("loc_2DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3131")

    ChrTalk(
        0xFE,
        (
            "I came from Liber … …\x01",
            "Um …… Yes,\x01",
            "Assistant to Julia · Schwarzu!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was on the street\x01",
            "I saw a pinup photo,\x01",
            "I became a fan at a glance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anything Liber is a fan club\x01",
            "There seems to be something that will be … …\x01",
            "I wonder if foreigners can put in it, too?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105FFa, Fan Club\x01",
            "I am a first-eyer ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes, there is a magazine company\x01",
            "While informal but informal\x01",
            "You seem to have been formed lately?\x02\x03",
            "#10102FTo members of the fan club,\x01",
            "Every month the official occasions of Associate Julia\x01",
            "Schedule or treasured pictures will arrive … or!\x02\x03",
            "#10106FHowever, unfortunately …\x01",
            "If you do not live in Libert\x01",
            "It seems I can not enter.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Well, is that so! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FWell, it is regrettable.\x02",
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
        "#00005F(Noel is also pretty detailed.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F(Oh, how kind,\x01",
            "It may be more than we think. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14B, 0)
    Jump("loc_31A9")

    label("loc_3131")


    ChrTalk(
        0xFE,
        (
            "Fan club of Assistant Yulia,\x01",
            "I wanted to enter it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, even some of the distant relatives\x01",
            "I wonder who is Libert! Is it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31A9")

    Jump("loc_339F")

    label("loc_31AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3240")

    ChrTalk(
        0xFE,
        "The trade meeting will finally be tomorrow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "VIP of each country so far\x01",
            "Although I have only seen it in a magazine,\x01",
            "Everyone has different aura.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_339F")

    label("loc_3240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_324E")
    Jump("loc_339F")

    label("loc_324E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_339F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3331")

    ChrTalk(
        0xFE,
        (
            "Mayor Dieter is really\x01",
            "It is a faultless person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is smart and has a sense of justice,\x01",
            "There are also action power and ideas,\x01",
            "Besides, he is an asset and handsome ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha, please say something\x01",
            "My eyes are about to turn.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_339F")

    label("loc_3331")


    ChrTalk(
        0xFE,
        (
            "Mayor Dieter is really\x01",
            "It is a faultless person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Outside politics and economy\x01",
            "Does something bother you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_339F")

    TalkEnd(0xFE)
    Return()

    # Function_11_21E3 end

    def Function_12_33A3(): pass

    label("Function_12_33A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_33DA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33DA")
    Call(0, 90)
    Return()

    label("loc_33DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3849")

    ChrTalk(
        0x1A2,
        "sniff……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Hm, you smell good!\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "Oh, boy!\x01",
            "Do you know the goodness of our noodles too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Oh, well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "For class B gourmet,\x01",
            "I think he's going to say Isisen.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "Wow, pointing to my noodle and class B …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Eh, return home!\x01",
            "To eat people who do not know the value\x01",
            "There are no noodles!\x02",
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
            "older sister,\x01",
            "Did I say something wrong?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_3687")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_3606():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3606)
    Sleep(50)

    def lambda_3616():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3616)
    Sleep(50)

    def lambda_3626():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3626)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00106FShin kun ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FSome kind of place like this\x01",
            "You are ignorant of the world.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_383E")

    label("loc_3687")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_3765")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_36E0():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36E0)
    Sleep(50)

    def lambda_36F0():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_36F0)
    Sleep(50)

    def lambda_3700():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3700)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00106FShin kun ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FI mean, such a place is\x01",
            "You are ignorant of the world.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_383E")

    label("loc_3765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_383E")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_37BE():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37BE)
    Sleep(50)

    def lambda_37CE():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_37CE)
    Sleep(50)

    def lambda_37DE():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_37DE)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00106FShin kun ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, apparently like this place\x01",
            "It sounds like people are ignorant.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_383E")

    TalkEnd(0x9)
    SetScenarioFlags(0x1DC, 1)
    Jump("loc_38B4")

    label("loc_3849")


    ChrTalk(
        0x9,
        "Well, to say that it is inconvenient B class and … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Eh, return home!\x01",
            "To eat people who do not know the value\x01",
            "There are no noodles!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)

    label("loc_38B4")

    Return()

    label("loc_38B5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_38BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48B7")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_391D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_391D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_393D")
    OP_AF(0x7B)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48B2")

    label("loc_393D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3951")
    Jump("loc_48B2")

    label("loc_3951")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48B2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_3A1F")

    ChrTalk(
        0xFE,
        (
            "Huff, among young people\x01",
            "There is a prospective person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Utilizing the delivered recipe,\x01",
            "You should definitely aim for the supreme noodles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will hold you as well.\x01",
            "I will support you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48B2")

    label("loc_3A1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3A9C")

    ChrTalk(
        0xFE,
        "Hmm, I finally came here … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I intended to do it as it was.\x01",
            "If we do this, we will just push forward!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48B2")

    label("loc_3A9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3B5F")

    ChrTalk(
        0xFE,
        (
            "For many years, food stalls that have been accompanied by hardships\x01",
            "When it was destroyed it was quite a shock … …\x01",
            "It can not be helped not to look forward!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Along with this newly bought stall\x01",
            "I will change my mind again and I will try my best!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48B2")

    label("loc_3B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3BEB")

    ChrTalk(
        0xFE,
        (
            "It is ridiculous in Mainz\x01",
            "It seems that the big idiots have appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hun, this boiled hot weather\x01",
            "I want to buy boiled juice!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48B2")

    label("loc_3BEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3CCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C5C")
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0xFE,
        "… …. え っ っ lock letter!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hello, a little\x01",
            "It seems that my body is getting cold.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3CCA")

    label("loc_3C5C")


    ChrTalk(
        0xFE,
        (
            "Alright\x01",
            "Let's make a cup for yourself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you squeeze noodles, your body and mind will also be shaky … …\x01",
            "No, it's Atsuatsu!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CCA")

    Jump("loc_48B2")

    label("loc_3CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3E06")

    ChrTalk(
        0xFE,
        (
            "Hmm? Apparently for condiments\x01",
            "Pepper powder is Oita\x01",
            "It seems that it is decreasing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, somewhere\x01",
            "Find the time properly\x01",
            "I should go buy it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E01")

    ChrTalk(
        0x101,
        (
            "#00008F(The gourmet guide coverage here\x01",
            "It looks like it could be done … …)\x02\x03",
            "#00003F(It is not right now.\x01",
            "Let's not forget to come later. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E01")

    Jump("loc_48B2")

    label("loc_3E06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3E69")

    ChrTalk(
        0xFE,
        "Hmm, today's noodles are also the best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "One cup of my whole body,\x01",
            "You should taste it in full!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48B2")

    label("loc_3E69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3FC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F65")

    ChrTalk(
        0xFE,
        (
            "To advocate independence as a country,\x01",
            "Mayor Dieter also\x01",
            "It is what we do daring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, I, such a mayor's\x01",
            "You are positively evaluating your posture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, in other words, in anything\x01",
            "An active path is a bold idea\x01",
            "Because it exists on the top.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3FBB")

    label("loc_3F65")


    ChrTalk(
        0xFE,
        (
            "Without a challenge and no success … ….\x01",
            "Hmm, political world and noodle world\x01",
            "The essence is the same.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FBB")

    Jump("loc_48B2")

    label("loc_3FC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_408B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4055")

    ChrTalk(
        0xFE,
        "A thousand customers have a thousand dramas.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Through customer interaction\x01",
            "Touching one end of such a drama …\x01",
            "This is another great pleasure of stalls again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4086")

    label("loc_4055")


    ChrTalk(
        0xFE,
        (
            "Old man and granddaughter ……\x01",
            "It is a good thing to be frustrated.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4086")

    Jump("loc_48B2")

    label("loc_408B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_44DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4134")

    ChrTalk(
        0xFE,
        (
            "I did a bright redhead a while ago.\x01",
            "A young man in suit shape\x01",
            "He wanted to eat my noodles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "\"Do you want to go out for dessert?\"\x01",
            "I went towards the entertainment district.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44D9")

    label("loc_4134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_438F")

    ChrTalk(
        0xFE,
        (
            "I did a bright redhead a while ago.\x01",
            "A young man in suit shape\x01",
            "I was eating my noodles … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Trying to reveal secret soup recipe,\x01",
            "Come in behind the stalls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In a moment\x01",
            "I succeeded in kicking out … …\x01",
            "There was a ridiculous man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(Young man with bright red hair suit … …)\x02\x03",
            "#00006F(… this action and say,\x01",
            "Somehow the person who thinks is\x01",
            "I do not feel like I knew you. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FWhere did the person go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, \"Would you like to go to dessert?\"\x01",
            "I went towards the entertainment district.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FRed light district ……\x02\x03",
            "#00003F(… … as yet \"he\"\x01",
            "I can not affirm,\x01",
            "Let's chase … ….? )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 6)
    SetScenarioFlags(0x1C7, 1)
    Jump("loc_44D9")

    label("loc_438F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4446")

    ChrTalk(
        0xFE,
        (
            "Hmm, today's heads of state leaders\x01",
            "Just as I entered the crossbell,\x01",
            "It is a gorgeous atmosphere thoughtful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know I'm wary, but,\x01",
            "I can not help guessing the gaze of the policeman.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_44D9")

    label("loc_4446")


    ChrTalk(
        0xFE,
        (
            "Police officers for alert,\x01",
            "A glimmer of glance on our stall\x01",
            "It sends it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can not concentrate on my work at all.\x01",
            "I want you to return to daily life as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44D9")

    Jump("loc_48B2")

    label("loc_44DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_461A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4599")

    ChrTalk(
        0xFE,
        "Noodles are KOSHI! And it's through the throat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will tell you that my noodles are\x01",
            "There is absolutely no necessity to eat elegantly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Noodles should be thoroughly squeezed\x01",
            "You can enjoy that taste!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4615")

    label("loc_4599")


    ChrTalk(
        0xFE,
        (
            "I will tell you that my noodles are\x01",
            "There is absolutely no necessity to eat elegantly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Noodles should be thoroughly squeezed\x01",
            "You can enjoy that taste!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4615")

    Jump("loc_48B2")

    label("loc_461A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4765")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_END)), "loc_467E")

    ChrTalk(
        0xFE,
        "Pink umbrella girl … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, here is\x01",
            "I think that he did not come.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4760")

    label("loc_467E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4706")

    ChrTalk(
        0xFE,
        "The way of noodles is patience!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I will lose to this rain!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(If rain does not enter the vessel,\x01",
            "I'm worried about how it works. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4760")

    label("loc_4706")


    ChrTalk(
        0xFE,
        (
            "Come now because it came\x01",
            "Why do not you have a meal at all?\x01",
            "The cold body will warm up quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4760")

    Jump("loc_48B2")

    label("loc_4765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_48B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4858")

    ChrTalk(
        0xFE,
        (
            "The road of noodles is not made in a day … …\x01",
            "And again, there is no end to that road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, after repeated research,\x01",
            "New noodles at last\x01",
            "I got into offering it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The name is also \"Tenkami noodle≪ sunflower ≫.\x01",
            "Please do eat it once by all means!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_48B2")

    label("loc_4858")


    ChrTalk(
        0xFE,
        (
            "To this new noodle\x01",
            "I have absolute confidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Surely you guys\x01",
            "You should be satisfied.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48B2")

    Jump("loc_38BF")

    label("loc_48B7")

    TalkEnd(0xFE)
    Return()

    # Function_12_33A3 end

    def Function_13_48BB(): pass

    label("Function_13_48BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4A09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4999")

    ChrTalk(
        0xFE,
        (
            "Because rail services stopped this morning,\x01",
            "The number that can be delivered has also decreased considerably.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rather than going …\x01",
            "I wonder what the crossbell really becomes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It is more important than work … …\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4A04")

    label("loc_4999")


    ChrTalk(
        0xFE,
        (
            "Really, if you go this way\x01",
            "I wonder what the crossbell really becomes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It is more important than work … …\x02",
    )

    CloseMessageWindow()

    label("loc_4A04")

    Jump("loc_5123")

    label("loc_4A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4A99")

    ChrTalk(
        0xFE,
        (
            "As early as a week from the attack incident ……\x01",
            "Have you finally calmed down here as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, such a case\x01",
            "I do not want you to get up again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5123")

    label("loc_4A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4B89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B45")

    ChrTalk(
        0xFE,
        (
            "The guard is in Mainz\x01",
            "To hold armed groups,\x01",
            "You seem to be pretty troubled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Independently own army, or …\x01",
            "It may be necessary after all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4B84")

    label("loc_4B45")


    ChrTalk(
        0xFE,
        (
            "Independently own army, or …\x01",
            "It may be necessary after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B84")

    Jump("loc_5123")

    label("loc_4B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4C8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C12")

    ChrTalk(
        0xFE,
        (
            "Ho! Is it? Because of the rain\x01",
            "The letter of the slip is going to disappear!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, well, somehow\x01",
            "I think I can decipher it, yeah.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4C89")

    label("loc_4C12")


    ChrTalk(
        0xFE,
        (
            "To check each delivery destination\x01",
            "I was back to headquarters\x01",
            "It's a lot of time loss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wow, but\x01",
            "On rainy days it is hard to do a lot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C89")

    Jump("loc_5123")

    label("loc_4C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4CFE")

    ChrTalk(
        0xFE,
        (
            "Between the station and West Street\x01",
            "There are many ambulances\x01",
            "It seems to be going back and forth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, what happened?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5123")

    label("loc_4CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4D54")

    ChrTalk(
        0xFE,
        "Now, I will work harder today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The efficient route is ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5123")

    label("loc_4D54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4E1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DDF")

    ChrTalk(
        0xFE,
        (
            "Well, if we turn around two more\x01",
            "I wish I could do it for the daytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well then, after thinking so\x01",
            "Somehow the power has come to pass!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4E16")

    label("loc_4DDF")


    ChrTalk(
        0xFE,
        (
            "After two more cases, Messi,\x01",
            "Messages after two more rounds …!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E16")

    Jump("loc_5123")

    label("loc_4E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4EEB")

    ChrTalk(
        0xFE,
        (
            "During the trade meeting,\x01",
            "Delivery of private requests to the new city hall building direction\x01",
            "It is stopped by the police at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, even if it is a suspicious thing to be misplaced\x01",
            "It will not be fancy in every way.\x01",
            "I think that it is the most natural treatment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5123")

    label("loc_4EEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4FC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F99")

    ChrTalk(
        0xFE,
        (
            "In the morning at the VIP visit\x01",
            "I did not deliver it to running water.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, well, today as well\x01",
            "Do as usual work amount ….\x01",
            "This place is eating wrinkle right now!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4FBB")

    label("loc_4F99")


    ChrTalk(
        0xFE,
        "Dash Dash Dash!\x02",
    )

    CloseMessageWindow()

    label("loc_4FBB")

    Jump("loc_5123")

    label("loc_4FC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_501C")

    ChrTalk(
        0xFE,
        "A police officer is pretty good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… I have to be careful not to bump.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5123")

    label("loc_501C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_50DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_END)), "loc_506A")

    ChrTalk(
        0xFE,
        (
            "I'm sorry, but I am at work now.\x01",
            "I have not seen a girl.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50DA")

    label("loc_506A")


    ChrTalk(
        0xFE,
        (
            "Hello, rain or storm,\x01",
            "I'm coming with Don!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it was said that ……,\x01",
            "Although the storm is kamenben to fluffy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50DA")

    Jump("loc_5123")

    label("loc_50DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5123")

    ChrTalk(
        0xFE,
        (
            "Busy, busy ……\x01",
            "After all the delivery shop is a physical match.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5123")

    TalkEnd(0xFE)
    Return()

    # Function_13_48BB end

    def Function_14_5127(): pass

    label("Function_14_5127")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5260")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51ED")

    ChrTalk(
        0xFE,
        (
            "What a stupid speech ……\x01",
            "Even if the world can be fooled,\x01",
            "This eagle will not be deceived!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is an independent country, what is a defense army!\x01",
            "Truly from us the threat of the two great countries\x01",
            "Do you even think that you can protect it!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_525B")

    label("loc_51ED")


    ChrTalk(
        0xFE,
        (
            "Goddess ……\x01",
            "I do not care about Eagle etc.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well then, please have a granddaughter,\x01",
            "Please save Amisa … …!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_525B")

    Jump("loc_58E5")

    label("loc_5260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_52DE")

    ChrTalk(
        0xFE,
        (
            "At that time, if I was a little late for escape\x01",
            "Eagle and Amisa ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… I think so\x01",
            "Even now it is terrible and can not be helped.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58E5")

    label("loc_52DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5350")

    ChrTalk(
        0xFE,
        (
            "It is quite lamentable.\x01",
            "Struggling people in Mainz\x01",
            "What on earth are you going to say … …!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58E5")

    label("loc_5350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_53E5")

    ChrTalk(
        0xFE,
        (
            "Hmm, what I can see in the distance\x01",
            "It's a Ferris wheel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… No, amisa.\x01",
            "Next time Grandpa and 2 people\x01",
            "Are you going to a theme park?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58E5")

    label("loc_53E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_543E")

    ChrTalk(
        0xFE,
        (
            "Waahahah,\x01",
            "How do you see it, Amisa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Grandpa is amazing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_58E5")

    label("loc_543E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_54A1")

    ChrTalk(
        0xFE,
        "Please wait, Amisa ~!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My grandfather is now\x01",
            "I'll catch a big bite.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58E5")

    label("loc_54A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_54AF")
    Jump("loc_58E5")

    label("loc_54AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_551C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54CA")
    Call(0, 15)
    Jump("loc_5517")

    label("loc_54CA")


    ChrTalk(
        0xFE,
        (
            "Amisa is really kind,\x01",
            "He is a good girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… I'm afraid I can cry.\x02",
    )

    CloseMessageWindow()

    label("loc_5517")

    Jump("loc_58E5")

    label("loc_551C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_567C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5621")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55E7")

    ChrTalk(
        0xFE,
        (
            "During the trade meeting\x01",
            "It seems to refrain from fishing at a wharf\x01",
            "The police said to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Potato, occasionally like this\x01",
            "You can also see the granddaughter and the state of the city\x01",
            "It's fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_93(0xB, 0x2D, 0x0)
    SetChrFlags(0xB, 0x10)
    Jump("loc_561C")

    label("loc_55E7")


    ChrTalk(
        0xFE,
        (
            "How old are you?\x01",
            "That is what Micchi is saying.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_561C")

    Jump("loc_5677")

    label("loc_5621")


    ChrTalk(
        0xFE,
        (
            "Hmm, until that time\x01",
            "Let's enjoy it if you can dance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be young is\x01",
            "Well yeah … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5677")

    Jump("loc_58E5")

    label("loc_567C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5820")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5774")

    ChrTalk(
        0xFE,
        (
            "Although I do not know what it is a trade meeting,\x01",
            "Police are on business trip\x01",
            "It is annoying.\x02",
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
        "…… Ha ha.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am stopped by Amisa\x01",
            "I said complaints again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_581B")

    label("loc_5774")


    ChrTalk(
        0xFE,
        (
            "As Amisa says, my complaints are\x01",
            "It is not good for the body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Regardless of the truth, Amisa's\x01",
            "I do not want to see a sad face.\x01",
            "I'm trying hard to say as much as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_581B")

    Jump("loc_58E5")

    label("loc_5820")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_582E")
    Jump("loc_58E5")

    label("loc_582E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_58E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5849")
    Call(0, 16)
    Jump("loc_58E5")

    label("loc_5849")


    ChrTalk(
        0xFE,
        (
            "Eagle is the world now\x01",
            "I hate the hospital ……\x01",
            "I love only granddaughters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well then, what this girl says\x01",
            "To listen to it as obedient as possible\x01",
            "You did it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58E5")

    TalkEnd(0xFE)
    Return()

    # Function_14_5127 end

    def Function_15_58E9(): pass

    label("Function_15_58E9")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xB,
        (
            "Slaughter, slaughter ……\x01",
            "This Tanmen is\x01",
            "It is hot and hard to eat.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 500)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "Already, grandpa\x01",
            "It is because it eats in haste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That's right, Amisa\x01",
            "I will give you Hu Hu\x01",
            "Wait a moment.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xC, 500)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "Hu Hu, Fu ……\x01",
            "Yes, please eat it ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Huh …\x01",
            "Thank you, Amisa.\x02",
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

    # Function_15_58E9 end

    def Function_16_5A49(): pass

    label("Function_16_5A49")


    ChrTalk(
        0xC,
        (
            "Grandpa,\x01",
            "Today I got some medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmm, I am always sorry.\x01",
            "I will have you drink later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Da - ma, say that.\x01",
            "When I take my eyes off, sometimes\x01",
            "Because I know I will not drink it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Today I will also have dinner together,\x01",
            "I will let you see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "That's right.\x01",
            "Amisa is looking forward to anything.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_16_5A49 end

    def Function_17_5B92(): pass

    label("Function_17_5B92")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5C0A")

    ChrTalk(
        0xFE,
        (
            "Like Grandpa says\x01",
            "I wonder if it really is going to be a war ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "… Yeah, I'm scared ………\x02",
    )

    CloseMessageWindow()
    Jump("loc_6001")

    label("loc_5C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5C55")

    ChrTalk(
        0xFE,
        (
            "A red building over there … …\x01",
            "It's totally gone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6001")

    label("loc_5C55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5C96")

    ChrTalk(
        0xFE,
        (
            "Grandpa,\x01",
            "It's irritating to your body … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6001")

    label("loc_5C96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5CEB")

    ChrTalk(
        0xFE,
        (
            "Er, really nice,\x01",
            "Grandpa! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "yay! I am really looking forward to it ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_6001")

    label("loc_5CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5D4B")

    ChrTalk(
        0xFE,
        "Wow!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Besides, the fish just before,\x01",
            "It was truly reckless.\x01",
            "I am looking forward to dinner ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6001")

    label("loc_5D4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5DB7")

    ChrTalk(
        0xFE,
        (
            "Grandpa,\x01",
            "Right now the pole has moved!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Throb……\x01",
            "Fish, I wonder if it hangs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6001")

    label("loc_5DB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5DC5")
    Jump("loc_6001")

    label("loc_5DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5E27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DE0")
    Call(0, 15)
    Jump("loc_5E22")

    label("loc_5DE0")


    ChrTalk(
        0xFE,
        "Grandpa, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Was there something even sad?\x02",
    )

    CloseMessageWindow()

    label("loc_5E22")

    Jump("loc_6001")

    label("loc_5E27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5F02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E7B")

    ChrTalk(
        0xFE,
        "Look at it, GrandPa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "There is an amazing place in the park!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5EFD")

    label("loc_5E7B")

    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Grandpa,\x01",
            "Now with Amisa\x01",
            "Please participate in the dance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, yeah ….\x01",
            "Indeed for Eagle\x01",
            "I feel that it is tough.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)

    label("loc_5EFD")

    Jump("loc_6001")

    label("loc_5F02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5F10")
    Jump("loc_6001")

    label("loc_5F10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5F1E")
    Jump("loc_6001")

    label("loc_5F1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6001")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F39")
    Call(0, 16)
    Jump("loc_6001")

    label("loc_5F39")


    ChrTalk(
        0xFE,
        (
            "If you ask patiently,\x01",
            "Recently obstinate grandpa finally finally\x01",
            "I got to take medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have not seen it\x01",
            "There are times when I'm going down, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, do not give up.\x01",
            "I am glad I could keep asking you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6001")

    TalkEnd(0xFE)
    Return()

    # Function_17_5B92 end

    def Function_18_6005(): pass

    label("Function_18_6005")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_60CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60AB")

    ChrTalk(
        0xFE,
        "Eh … ___ ___ 0\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is time tomorrow is finally here.\x01",
            "Renewal It's a public day of the stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it's raining\x01",
            "You can not be calm.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_60C9")

    label("loc_60AB")


    ChrTalk(
        0xFE,
        "Eh … ___ ___ 0\x02",
    )

    CloseMessageWindow()

    label("loc_60C9")

    Jump("loc_61E9")

    label("loc_60CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6180")

    ChrTalk(
        0xFE,
        "Eh … ___ ___ 0\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whether taking a rest is important,\x01",
            "I can not keep staring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The person who moved the body to it\x01",
            "You do not need to think about extra things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_61E9")

    label("loc_6180")


    ChrTalk(
        0xFE,
        "Eh … ___ ___ 0\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, recently I was running outside\x01",
            "Always sure to be with Celine senpai.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61E9")

    TalkEnd(0xFE)
    Return()

    # Function_18_6005 end

    def Function_19_61ED(): pass

    label("Function_19_61ED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_62B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_626A")

    ChrTalk(
        0xFE,
        "I, I …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To Nicole and to Shuri\x01",
            "I do not mean to lose.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_62AD")

    label("loc_626A")


    ChrTalk(
        0xFE,
        (
            "To Nicole and to Shuri\x01",
            "I do not mean to lose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62AD")

    Jump("loc_62FA")

    label("loc_62B2")


    ChrTalk(
        0xFE,
        (
            "Nicole …\x01",
            "I wanted to get out of my way\x01",
            "That's not going to happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62FA")

    TalkEnd(0xFE)
    Return()

    # Function_19_61ED end

    def Function_20_62FE(): pass

    label("Function_20_62FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6398")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6368")

    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Hello everyone~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Misashi, today\x01",
            "Have fun all day ~ ☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6393")

    label("loc_6368")


    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Misashi, today\x01",
            "Have fun all day ~ ☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6393")

    Jump("loc_6402")

    label("loc_6398")


    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Misashi,\x01",
            "It was a fun older brother ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Next is Wonderland\x01",
            "I would be delightful if you danced with me ~ ☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6402")

    TalkEnd(0xFE)
    Return()

    # Function_20_62FE end

    def Function_21_6406(): pass

    label("Function_21_6406")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_649C")

    ChrTalk(
        0xFE,
        (
            "Today Michishi special\x01",
            "It came from Michelin ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because I prepared various events,\x01",
            "Have fun with everyone ~!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_651D")

    label("loc_649C")


    ChrTalk(
        0xFE,
        (
            "No, I was surprised.\x01",
            "Until to Mitsui dance\x01",
            "I can not fit it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it's no problem\x01",
            "I wish I had a scout.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_651D")

    TalkEnd(0xFE)
    Return()

    # Function_21_6406 end

    def Function_22_6521(): pass

    label("Function_22_6521")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65D3")

    ChrTalk(
        0xFE,
        (
            "Uhufu, a little more\x01",
            "Mitsushi dance show\x01",
            "Because it starts!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What's more, today\x01",
            "A special event that you can dance next to Misashi!\x01",
            "Come and join us by all means ~!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_665E")

    label("loc_65D3")


    ChrTalk(
        0xFE,
        (
            "A blonde person now, first with an instrument\x01",
            "BGM of Miss Dance\x01",
            "I was playing, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dance yourself even on your own way.\x01",
            "Hehe he was a fun person.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_665E")

    TalkEnd(0xFE)
    Return()

    # Function_22_6521 end

    def Function_23_6662(): pass

    label("Function_23_6662")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_66AB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66A6")

    ChrTalk(
        0xFE,
        (
            "Beach, beach!\x01",
            "I want to swim at the beach ~!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66A6")

    Jump("loc_6705")

    label("loc_66AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66DC")

    ChrTalk(
        0xFE,
        "Wow ~, only genuine thing ~!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6705")

    label("loc_66DC")


    ChrTalk(
        0xFE,
        (
            "Now I\x01",
            "I want to dance Miss you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6705")

    TalkEnd(0xFE)
    Return()

    # Function_23_6662 end

    def Function_24_6709(): pass

    label("Function_24_6709")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6757")

    ChrTalk(
        0xFE,
        (
            "Throb……\x01",
            "His dance show promptly\x01",
            "I guess it will not start.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67BB")

    label("loc_6757")


    ChrTalk(
        0xFE,
        (
            "That blonde elder brother as well\x01",
            "It was pretty cool!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it can not be miserable!\x01",
            "Uhufu.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67BB")

    TalkEnd(0xFE)
    Return()

    # Function_24_6709 end

    def Function_25_67BF(): pass

    label("Function_25_67BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6817")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6812")

    NpcTalk(
        0xFE,
        "passenger",
        (
            "I am in the arcade\x01",
            "I am looking forward to the boutique too ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6812")

    Jump("loc_687E")

    label("loc_6817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_684D")

    ChrTalk(
        0xFE,
        (
            "Hey Hey,\x01",
            "Please look calm down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_687E")

    label("loc_684D")


    ChrTalk(
        0xFE,
        (
            "Children too much\x01",
            "It seems I enjoyed it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_687E")

    TalkEnd(0xFE)
    Return()

    # Function_25_67BF end

    def Function_26_6882(): pass

    label("Function_26_6882")

    TalkBegin(0xFE)

    NpcTalk(
        0xFE,
        "passenger",
        "Huh, you are also a codomo ~.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_6882 end

    def Function_27_68B2(): pass

    label("Function_27_68B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_695F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_691A")

    ChrTalk(
        0xFE,
        (
            "She is pretty\x01",
            "It seems they were pleased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I am glad I went after all.\x02",
    )

    CloseMessageWindow()
    Jump("loc_695A")

    label("loc_691A")


    NpcTalk(
        0xFE,
        "Citizen",
        (
            "Oh, I'm looking forward to it.\x01",
            "I want to play at the theme park at last.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_695A")

    Jump("loc_6A1A")

    label("loc_695F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69B7")

    ChrTalk(
        0xFE,
        "Is this only rumor …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This ugly expression\x01",
            "It is terrible!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A1A")

    label("loc_69B7")


    ChrTalk(
        0xFE,
        (
            "Mr.,\x01",
            "Pretty brilliant dance\x01",
            "I can dance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought it was a stuffed animal\x01",
            "I was thrown away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A1A")

    TalkEnd(0xFE)
    Return()

    # Function_27_68B2 end

    def Function_28_6A1E(): pass

    label("Function_28_6A1E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6A68")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6A63")

    ChrTalk(
        0xFE,
        (
            "Ufufu, souvenirs\x01",
            "I bought lots of ☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A63")

    Jump("loc_6B5B")

    label("loc_6A68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AF9")

    ChrTalk(
        0xFE,
        (
            "Although wonder land is closed,\x01",
            "I am lucky to see you in the town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I, this as a trigger\x01",
            "It seems to become a fan of Mitsui.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B5B")

    label("loc_6AF9")


    ChrTalk(
        0xFE,
        (
            "I, it's all Mitsui's\x01",
            "I became a fan!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goods for souvenirs\x01",
            "You buy a lot and get back home!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B5B")

    TalkEnd(0xFE)
    Return()

    # Function_28_6A1E end

    def Function_29_6B5F(): pass

    label("Function_29_6B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B76")
    Call(0, 47)
    Return()

    label("loc_6B76")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_29_6B5F end

    def Function_30_6B7D(): pass

    label("Function_30_6B7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BAF")
    Call(0, 61)
    Jump("loc_6BB2")

    label("loc_6BAF")

    Call(0, 69)

    label("loc_6BB2")

    Return()

    # Function_30_6B7D end

    def Function_31_6BB3(): pass

    label("Function_31_6BB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BD6")
    Call(0, 70)

    label("loc_6BD6")

    Return()

    # Function_31_6BB3 end

    def Function_32_6BD7(): pass

    label("Function_32_6BD7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_6C13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BF5")
    Call(0, 34)
    Jump("loc_6C0E")

    label("loc_6BF5")


    ChrTalk(
        0x1B,
        "#01200FGurururu …\x02",
    )

    CloseMessageWindow()

    label("loc_6C0E")

    Jump("loc_6C3E")

    label("loc_6C13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6C24")
    Jump("loc_6C3E")

    label("loc_6C24")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_6C35")
    Jump("loc_6C3E")

    label("loc_6C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6C3E")

    label("loc_6C3E")

    TalkEnd(0xFE)
    Return()

    # Function_32_6BD7 end

    def Function_33_6C42(): pass

    label("Function_33_6C42")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_6D02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C60")
    Call(0, 34)
    Jump("loc_6CFD")

    label("loc_6C60")


    ChrTalk(
        0x1C,
        (
            "#01109FAlright Zeitou,\x01",
            "Now jump over Shizuku!\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x1B, 0xFF)

    ChrTalk(
        0x1B,
        "#01203FGurururu …… won.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#01106F… …. \"Do not get in danger\"?\x01",
            "Well, that is not it.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1B, 0xFF)

    label("loc_6CFD")

    Jump("loc_6D2D")

    label("loc_6D02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6D13")
    Jump("loc_6D2D")

    label("loc_6D13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_6D24")
    Jump("loc_6D2D")

    label("loc_6D24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6D2D")

    label("loc_6D2D")

    TalkEnd(0xFE)
    Return()

    # Function_33_6C42 end

    def Function_34_6D31(): pass

    label("Function_34_6D31")

    OP_4B(0x1C, 0xFF)
    OP_4B(0x1D, 0xFF)
    OP_4B(0x1B, 0xFF)

    ChrTalk(
        0x1C,
        (
            "#01100FWell then, then\x01",
            "Try shizuku -.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#06005FWell, er …\x02\x03",
            "#06000F…… Mr. Zeit, hand it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#01200Fwon. (Puhu)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#06005FWow … after all it is smart.\x02\x03",
            "#06002FHuh, and also meat balls\x01",
            "It is very soft.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#01109FDoes not it?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    OP_4C(0x1C, 0xFF)
    OP_4C(0x1D, 0xFF)
    OP_4C(0x1B, 0xFF)
    Return()

    # Function_34_6D31 end

    def Function_35_6E56(): pass

    label("Function_35_6E56")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_6ECA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E74")
    Call(0, 34)
    Jump("loc_6EC5")

    label("loc_6E74")


    ChrTalk(
        0x1D,
        (
            "#06002FHehu, Zeit is\x01",
            "It is really clever.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x1B, 0xFF)

    ChrTalk(
        0x1B,
        "#01200F……won.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x1B, 0xFF)

    label("loc_6EC5")

    Jump("loc_6EF5")

    label("loc_6ECA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6EDB")
    Jump("loc_6EF5")

    label("loc_6EDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_6EEC")
    Jump("loc_6EF5")

    label("loc_6EEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6EF5")

    label("loc_6EF5")

    TalkEnd(0xFE)
    Return()

    # Function_35_6E56 end

    def Function_36_6EF9(): pass

    label("Function_36_6EF9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_END)), "loc_6F7A")

    ChrTalk(
        0xFE,
        (
            "Because it's so hard, Michelam\x01",
            "I decided to peek a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, from now\x01",
            "I wonder how much I can turn around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7001")

    label("loc_6F7A")


    ChrTalk(
        0xFE,
        (
            "Huhu, crossbell\x01",
            "It really depends on the location\x01",
            "It will change with glittering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The people in the entertainment district were noisy,\x01",
            "I can relax here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7001")

    TalkEnd(0xFE)
    Return()

    # Function_36_6EF9 end

    def Function_37_7005(): pass

    label("Function_37_7005")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_END)), "loc_707A")

    ChrTalk(
        0xFE,
        (
            "From now on Michelin\x01",
            "I decided to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My mind is an older car\x01",
            "I'm gonna ride it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70CD")

    label("loc_707A")


    ChrTalk(
        0xFE,
        (
            "Hey, Mama …\x01",
            "Such a place, boring yo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Let's get back to the glittering early.\x02",
    )

    CloseMessageWindow()

    label("loc_70CD")

    TalkEnd(0xFE)
    Return()

    # Function_37_7005 end

    def Function_38_70D1(): pass

    label("Function_38_70D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_71F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_718C")

    ChrTalk(
        0xFE,
        (
            "There is no stopping rain ……\x01",
            "…… And there is no sunny sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Now, good things\x01",
            "I tried to say, but\x01",
            "I did not get together.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_71EB")

    label("loc_718C")


    ChrTalk(
        0xFE,
        (
            "There is no stopping rain ……\x01",
            "…… And I do not get hungry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "… … it became increasingly severe.\x02",
    )

    CloseMessageWindow()

    label("loc_71EB")

    Jump("loc_72BC")

    label("loc_71F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_72BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_END)), "loc_7263")

    ChrTalk(
        0xFE,
        "A girl with an umbrella … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, just a while ago\x01",
            "It seems like …\x01",
            "It is not like that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72BC")

    label("loc_7263")


    ChrTalk(
        0xFE,
        (
            "What kind of raindrops are they?\x01",
            "I guess you are … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… Can you see it when you stared your eyes?\x02",
    )

    CloseMessageWindow()

    label("loc_72BC")

    TalkEnd(0xFE)
    Return()

    # Function_38_70D1 end

    def Function_39_72C0(): pass

    label("Function_39_72C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73C3")

    ChrTalk(
        0xFE,
        (
            "The Michelin-based leaders\x01",
            "I heard that I will leave here soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "While they enter the tower,\x01",
            "I will enter the blockade again here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have business in the business area\x01",
            "I'd like to finish it promptly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, I understand.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_7451")

    label("loc_73C3")


    ChrTalk(
        0xFE,
        (
            "When the leaders arrived from the Michelin,\x01",
            "I will enter the blockade again here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have business in the business area\x01",
            "I'd like to finish it promptly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7451")

    TalkEnd(0xFE)
    Return()

    # Function_39_72C0 end

    def Function_40_7455(): pass

    label("Function_40_7455")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_74FD")

    ChrTalk(
        0xFE,
        (
            "Is it a terrorist …?\x01",
            "Even though I had originally assumed it,\x01",
            "The possibility increases as you come here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well anyway, for a while\x01",
            "There is no choice but to move according to the direction of the headquarters.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_764A")

    label("loc_74FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_75BE")

    ChrTalk(
        0xFE,
        "Is Michishi's business trip event …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, well for the city\x01",
            "It seems that we have taken permission\x01",
            "There seems to be no problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But well, M · W · L as well\x01",
            "Service spirit is vigorous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_764A")

    label("loc_75BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_764A")

    ChrTalk(
        0xFE,
        (
            "A survey on trends of \"Black Moon\"\x01",
            "It is outside the jurisdiction of the wide area security office … …\x01",
            "Of course, vigilance is necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, let's do something\x01",
            "I do not think they are guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_764A")

    TalkEnd(0xFE)
    Return()

    # Function_40_7455 end

    def Function_41_764E(): pass

    label("Function_41_764E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_773E")

    ChrTalk(
        0xFE,
        (
            "Although the black month office was completely destroyed,\x01",
            "In this week as well in this week\x01",
            "It seems that it was oddly calm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of the soon-to-be referendum ballot\x01",
            "Thanks, citizens who are depressed\x01",
            "It seems to be relatively small … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Something like this at the last minute\x01",
            "I feel something like powerfulness.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7959")

    label("loc_773E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_77D5")

    ChrTalk(
        0xFE,
        (
            "Even those already entering the city\x01",
            "There seems to be, many of the leaders\x01",
            "I am still in Michelin direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There is also a story of terrorists.\x01",
            "I also care about security.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7959")

    label("loc_77D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_788A")

    ChrTalk(
        0xFE,
        (
            "Osborne's Prime Minister took Michelam,\x01",
            "And President Locksmith made IBC\x01",
            "It seems to be calling … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Both neighbors are stone guards.\x01",
            "Well, do not worry about it first.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7959")

    label("loc_788A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7959")

    ChrTalk(
        0xFE,
        (
            "As soon as there is something\x01",
            "To be able to rush with a police car\x01",
            "I am waiting here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I lose to the guard's vehicle,\x01",
            "This guy is also bulletproof and sturdy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In times of emergency,\x01",
            "It will become a shield.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7959")

    TalkEnd(0xFE)
    Return()

    # Function_41_764E end

    def Function_42_795D(): pass

    label("Function_42_795D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7A49")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_79D8")

    ChrTalk(
        0x24,
        (
            "Use of water bus,\x01",
            "Thank you very much~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "For further use\x01",
            "We are waiting for you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A44")

    label("loc_79D8")


    ChrTalk(
        0x24,
        (
            "Water bus to Michelin,\x01",
            "We will not be off soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "If you use\x01",
            "Please board early!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A44")

    Jump("loc_7AD4")

    label("loc_7A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_END)), "loc_7AD4")

    ChrTalk(
        0xFE,
        (
            "A water bus for Michelin\x01",
            "I'm arriving now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We will start boarding guide from this.\x01",
            "Please wait in line.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AD4")

    TalkEnd(0xFE)
    Return()

    # Function_42_795D end

    def Function_43_7AD8(): pass

    label("Function_43_7AD8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7C34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BB8")

    ChrTalk(
        0xFE,
        (
            "The town is alert but … ….\x01",
            "With this\x01",
            "What a calm one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The fever produced by the trade council\x01",
            "What kind of whirlpools will be created? …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thus, here relaxing\x01",
            "It is not bad to indulge in thought.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_7C34")

    label("loc_7BB8")


    ChrTalk(
        0xFE,
        (
            "The fever produced by the trade council\x01",
            "What kind of whirlpools will be created? …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thus, here relaxing\x01",
            "It is not bad to indulge in thought.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C34")

    TalkEnd(0xFE)
    Return()

    # Function_43_7AD8 end

    def Function_44_7C38(): pass

    label("Function_44_7C38")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D34")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D2C")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a key on the door,\x01",
            "It has a message plate.\x07\x00\x02",
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
            "\"Black Municipal Trading Company · Crossbell Branch\"\x01",
            "* Please knock the direction of the order.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_7D2F")

    label("loc_7D2C")

    Call(0, 72)

    label("loc_7D2F")

    Jump("loc_81A0")

    label("loc_7D34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_808D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FC2")
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
            "There is a key on the door,\x01",
            "It has a message plate.\x07\x00\x02",
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
            "\"Black Municipal Trading Company · Crossbell Branch\"\x01",
            "* Please knock the direction of the order.\x07\x00\x02",
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
            "#00003FIt seems like\x01",
            "It looks like time has run out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWaaaaaaaaaaaaaa.\x01",
            "Let's give up and destroy other errands.\x02",
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
            "Quest 【City Guide to Shin Boy】\x07\x00",
            "I failed ……\x02",
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
    Jump("loc_8088")

    label("loc_7FC2")

    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a key on the door,\x01",
            "It has a message plate.\x07\x00\x02",
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
            "\"Black Municipal Trading Company · Crossbell Branch\"\x01",
            "* Please knock the direction of the order.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_8088")

    Jump("loc_81A0")

    label("loc_808D")

    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a key on the door,\x01",
            "It has a message plate.\x07\x00\x02",
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
            "\"Black Municipal Trading Company · Crossbell Branch\"\x01",
            "* Please knock the direction of the order.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_81A0")

    ChrTalk(
        0x101,
        (
            "#00003FIn this place,\x01",
            "I'm not getting into a fossil …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81A0")

    TalkEnd(0xFF)
    Return()

    # Function_44_7C38 end

    def Function_45_81A4(): pass

    label("Function_45_81A4")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_83F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83A8")

    ChrTalk(
        0x1A2,
        "Hmm, is the crossbell times?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "By the way, in the same port area\x01",
            "It was the headquarters.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8233():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8233)

    def lambda_8240():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8240)

    ChrTalk(
        0x101,
        "#00005FIs it? You said something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Hun, apart ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "If it says so strongly,\x01",
            "Reporters who like to go around\x01",
            "It is tokoro that you can not like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "The economic magazine here is the Republic of\x01",
            "I will also get business people,\x01",
            "Of course I am evaluating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F(Well, what I should say … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Yeah, really well at this age\x01",
            "You can feel it like that. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_83F3")

    label("loc_83A8")


    ChrTalk(
        0x1A2,
        (
            "Telecommunications company\x01",
            "Even if it enters it will only be repelled?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "I will go on to the next one.\x02",
    )

    CloseMessageWindow()

    label("loc_83F3")

    TalkEnd(0xFF)
    Return()

    # Function_45_81A4 end

    def Function_46_83F7(): pass

    label("Function_46_83F7")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FI'm going to catch you here.\x02",
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
            "Do you fish?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "To fish\x01",      # 0
            "quit\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84C6")
    OP_E2(0x2)
    MiniGame(0x6, 0x1, 0x14226, 0xFFFFF63C, 0x3AA2, 0xB4, 0x13812, 0xFFFFF254, 0x226A)

    label("loc_84C6")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_46_83F7 end

    def Function_47_84CB(): pass

    label("Function_47_84CB")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8905")

    ChrTalk(
        0x18,
        "#11POh, you're from the SSS right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYes.\x01",
            "Good day everywhere during the rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#6PPlease arrange\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PNo,\x01",
            "This is from my work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PCan you drive it though?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWhat?\x01",
            "I am flying, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00008FOh right I forgot about that\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#6PWell, if the car can drive\x01",
            "I guess it's not a difficult Mon … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FThis is Enigma\x01",
            "Shall I contact the section chief?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        (
            "#5P#10105FOh, it's fine\x02\x03",
            "#10100FWith this type of boat\x01",
            "I have experience of maneuvering.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_87AA():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_87AA)
    Sleep(50)

    def lambda_87BA():
        TurnDirection(0x104, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_87BA)
    Sleep(50)

    def lambda_87CA():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_87CA)
    Sleep(50)

    def lambda_87DA():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_87DA)
    Sleep(50)

    def lambda_87EA():
        TurnDirection(0x103, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_87EA)
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
        "#6P#00309FHaha that's our Noel\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FAfter all the kind of driving and maneuvering\x01",
            "You seem to be a hand?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10112FHuhu, this is also Sonja's command\x01",
            "It is a preparation, but ….\x02\x03",
            "#10100FWhat do you do?\x01",
            "Do you board a boat immediately?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x165, 1)
    Jump("loc_894C")

    label("loc_8905")

    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        (
            "#5P#10100FWhat do you do?\x01",
            "Do you board a boat immediately?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    label("loc_894C")


    ChrTalk(
        0x101,
        (
            "#12P#00003FThat's right.\x02\x03",
            "#00008F(I do not know what is at the destination.\x01",
            "Is not there anything else left behind? )\x02",
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
            "Taking the boat and heading to the destination\x01",
            "In this chapter you will find Crossbell outside the city\x01",
            "I will not be able to leave.\x02\x03",
            "In quests such as quests etc.\x01",
            "be careful.\x07\x00\x02",
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
            "【There are still other things to do】\x01",                # 0
            "【Toward wetland belt by boat】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_8AD9"),
        (0, "loc_8CDA"),
        (SWITCH_DEFAULT, "loc_8D63"),
    )


    label("loc_8AD9")


    ChrTalk(
        0x109,
        "#5P#10102FUnderstood!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PThen, by all means then\x01",
            "Take care.\x02",
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

    def lambda_8BCC():

        label("loc_8BCC")

        TurnDirection(0xFE, 0x33, 500)
        Yield()
        Jump("loc_8BCC")

    QueueWorkItem2(0x18, 2, lambda_8BCC)
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
    Jump("loc_8D63")

    label("loc_8CDA")


    ChrTalk(
        0x109,
        "#5P#10100FI understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PThen when you're ready\x01",
            "Please speak to me.\x02",
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
    Jump("loc_8D63")

    label("loc_8D63")

    Return()

    # Function_47_84CB end

    def Function_48_8D64(): pass

    label("Function_48_8D64")

    OP_96(0x33, 0xA410, 0xFFFFF060, 0xFFFFA81C, 0xBB8, 0x0)

    def lambda_8D7D():
        OP_9E(0xFE, 0xA410, 0xFFFE96AC, 0x7530, 0xFA0, 0x1)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_8D7D)
    Sleep(1000)

    def lambda_8D9B():
        OP_9E(0xFE, 0xA410, 0xFFFE96AC, 0x7530, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_8D9B)
    Sleep(1000)

    def lambda_8DB9():
        OP_9E(0xFE, 0xA410, 0xFFFE96AC, 0x7530, 0x1770, 0x1)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_8DB9)
    Sleep(1000)

    def lambda_8DD7():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8DD7)

    def lambda_8DE4():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8DE4)

    def lambda_8DF1():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8DF1)

    def lambda_8DFE():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8DFE)

    def lambda_8E0B():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8E0B)

    def lambda_8E18():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8E18)

    def lambda_8E25():
        OP_9E(0xFE, 0xA410, 0xFFFE96AC, 0x7530, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_8E25)
    Sleep(1000)

    def lambda_8E43():
        OP_9E(0xFE, 0xA410, 0xFFFE96AC, 0x7530, 0x1F40, 0x1)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_8E43)
    WaitChrThread(0x33, 1)
    Return()

    # Function_48_8D64 end

    def Function_49_8E5E(): pass

    label("Function_49_8E5E")

    Sound(470, 0, 100, 0)
    Sound(482, 0, 60, 0)
    Sleep(5000)
    Sound(483, 2, 100, 0)
    Sleep(4000)
    StopSound(483, 2000, 90)
    Return()

    # Function_49_8E5E end

    def Function_50_8E7D(): pass

    label("Function_50_8E7D")

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

    def lambda_9062():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9062)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x18, 0)
    Sleep(120)
    TurnDirection(0x18, 0x101, 0)

    def lambda_908C():
        OP_9B(0x0, 0xFE, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_908C)
    Sleep(100)

    def lambda_90A4():
        OP_9B(0x0, 0xFE, 0x5, 0x258, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_90A4)
    WaitChrThread(0x102, 1)

    def lambda_90BD():
        OP_9B(0x0, 0xFE, 0xF, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_90BD)
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

    def lambda_91D0():
        OP_95(0xFE, 38490, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_91D0)
    Sleep(60)

    def lambda_91ED():
        OP_95(0xFE, 37490, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_91ED)
    Sleep(30)
    TurnDirection(0x18, 0x101, 500)

    def lambda_9211():
        OP_95(0xFE, 38490, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9211)
    Sleep(30)

    def lambda_922E():
        OP_95(0xFE, 37990, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_922E)

    def lambda_9248():
        OP_95(0xFE, 39490, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9248)
    Sleep(30)

    def lambda_9265():
        OP_95(0xFE, 38290, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9265)
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

    # Function_50_8E7D end

    def Function_51_929E(): pass

    label("Function_51_929E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_92E8")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, -500, -5000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(233)
    Jump("Function_51_929E")

    label("loc_92E8")

    Return()

    # Function_51_929E end

    def Function_52_92E9(): pass

    label("Function_52_92E9")

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

    # Function_52_92E9 end

    def Function_53_934A(): pass

    label("Function_53_934A")

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

    # Function_53_934A end

    def Function_54_93AB(): pass

    label("Function_54_93AB")

    OP_96(0x33, 0x9858, 0xFFFFF060, 0xFFFFA36C, 0x7D0, 0x0)
    TurnDirection(0x18, 0x33, 0)
    OP_96(0x33, 0x96C8, 0xFFFFF060, 0xFFFFA81C, 0x3E8, 0x0)
    Return()

    # Function_54_93AB end

    def Function_55_93DB(): pass

    label("Function_55_93DB")

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

    # Function_55_93DB end

    def Function_56_9409(): pass

    label("Function_56_9409")

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
            "Wow, this large city\x01",
            "It's awesome to kill you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x2B, 500)
    Sleep(50)

    ChrTalk(
        0x2A,
        (
            "Reggie, even if you drive\x01",
            "You have improved considerably.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        "Hey, is not it?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x29, 500)
    Sleep(50)

    ChrTalk(
        0x2B,
        (
            "Well, Yuri's prepared\x01",
            "Even the performance of the car is good\x01",
            "I wonder if there are any.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x29, 500)
    Sleep(50)

    ChrTalk(
        0x29,
        (
            "Huhun, of course.\x01",
            "Even if it says Vernu\x01",
            "It is the latest model.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "…… Register than that.\x01",
            "In the middle aged who was standing on the road earlier\x01",
            "It seemed it was going to hit him at stake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "Oh, ah ……\x01",
            "I managed to dodge anyhow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "As expected to be ……\x01",
            "If that surprised face of that man came … …\x02",
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
        "#4S#1K#1P…… It was a masterpiece!\x02",
    )


    ChrTalk(
        0x2A,
        "#4S#1K#3PIt was a masterpiece! It is!\x02",
    )


    ChrTalk(
        0x2B,
        "#4S#1K#2PIt was a masterpiece! It is!\x02",
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
            "Waah!\x01",
            "That old man, seriously\x01",
            "I was disappointed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "Hina, I will run over! It is!\x01",
            "Help me, Mom, I?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x2A, 500)
    Sleep(50)

    ChrTalk(
        0x2B,
        (
            "Ahahahaha! It is!\x01",
            "Or stop it, Sykes!\x01",
            "My stomach is twisted ~ ~! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "Giggle\x01",
            "Well, it's a long stay.\x01",
            "Let's have some fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "Our new playground ……\x01",
            "This crossbar is the city.\x02",
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

    def lambda_9A26():
        OP_98(0xFE, 0x61A8, 0x0, 0x0, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_9A26)
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
            "Oops ……\x01",
            "It seems like the police are coming.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x2B, 500)
    Sleep(50)

    ChrTalk(
        0x2A,
        "Reggie, leave the car!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x2A, 500)
    Sleep(50)

    ChrTalk(
        0x2B,
        (
            "Okay, those guys\x01",
            "Please shake it off shortly!\x02",
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

    def lambda_9B8C():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_9B8C)

    def lambda_9BA1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_9BA1)
    WaitChrThread(0x2B, 2)
    Sleep(100)
    WaitChrThread(0x29, 1)

    def lambda_9BBD():
        OP_9B(0x0, 0xFE, 0xB4, 0xFFFFF830, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_9BBD)

    def lambda_9BD2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_9BD2)
    Sleep(100)
    WaitChrThread(0x2A, 1)

    def lambda_9BEA():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_9BEA)

    def lambda_9BFF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_9BFF)
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

    # Function_56_9409 end

    def Function_57_9D2F(): pass

    label("Function_57_9D2F")

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

    # Function_57_9D2F end

    def Function_58_9E2F(): pass

    label("Function_58_9E2F")

    OP_93(0x2B, 0x5A, 0x3E8)
    OP_9B(0x0, 0x2B, 0x0, 0x9C4, 0xBB8, 0x0)
    OP_93(0x2B, 0x0, 0x1F4)
    Return()

    # Function_58_9E2F end

    def Function_59_9E4D(): pass

    label("Function_59_9E4D")

    OP_93(0x29, 0x0, 0x3E8)
    OP_9B(0x0, 0x29, 0x0, 0x9C4, 0xBB8, 0x0)
    OP_93(0x29, 0x5A, 0x3E8)
    OP_9B(0x0, 0x29, 0x0, 0xFA0, 0xBB8, 0x0)
    OP_93(0x29, 0xB4, 0x1F4)
    Return()

    # Function_59_9E4D end

    def Function_60_9E81(): pass

    label("Function_60_9E81")

    OP_93(0x2A, 0x0, 0x3E8)
    OP_9B(0x0, 0x2A, 0x0, 0xFA0, 0xBB8, 0x0)
    OP_93(0x2A, 0x5A, 0x3E8)
    OP_9B(0x0, 0x2A, 0x0, 0x1388, 0xBB8, 0x0)
    OP_93(0x2A, 0xB4, 0x1F4)
    Return()

    # Function_60_9E81 end

    def Function_61_9EB5(): pass

    label("Function_61_9EB5")

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
            "Meilin 's guy,\x01",
            "Where are you going ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FExcuse me.\x01",
            "Is it Meirin's older brother?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x19, 0xB4, 0x1F4)

    ChrTalk(
        0x19,
        (
            "That's right, but …\x01",
            "Is it for something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FWell, we are the crossbell police\x01",
            "I am a person in the mission support department … …\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd is\x01",
            "I am looking for umbrella of peach\x01",
            "I explained the circumstances.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x19,
        (
            "……Ah, I see.\x01",
            "Is that something like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Meilin uses a different child's umbrella\x01",
            "I thought I was taking it.\x01",
            "I did not even notice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "I thought you went up, if that's the case\x01",
            "I want to return it even soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105Fby the way……\x01",
            "Where is Meirin chan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FWith you\x01",
            "Were not you going out for a walk?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "To tell the truth, with Meirin earlier\x01",
            "I just started playing hide-and-seek.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "I was troubled with such rain,\x01",
            "I just want to do it\x01",
            "I am going out with you ….\x02",
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
            "……you,\x01",
            "I'm good at hiding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "I'm worried about searching,\x01",
            "Whether you can find it immediately ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FIs that so …?\x02\x03",
            "#00000FBut if that's the case …\x01",
            "We also have Meirin chan\x01",
            "May I look for it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Oh, then\x01",
            "It will be a pleasure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Maybe, Mayrin\x01",
            "Somewhere in this port area\x01",
            "You should be hiding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Because it's hide and seek,\x01",
            "I think that it is not in the building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Although it might be difficult\x01",
            "Look for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FYes, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHuh, then\x01",
            "Let's search for it.\x02",
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

    # Function_61_9EB5 end

    def Function_62_A4D0(): pass

    label("Function_62_A4D0")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00012FUnder the bench ……\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_62_A4D0 end

    def Function_63_A511(): pass

    label("Function_63_A511")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        "#00000F…… It seems that it is not behind the stall.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_63_A511 end

    def Function_64_A545(): pass

    label("Function_64_A545")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        "#00006FBehind the container! Are not you …?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_64_A545 end

    def Function_65_A579(): pass

    label("Function_65_A579")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FHide and seek,\x01",
            "It should not be in the building.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -14030, 2000, 24980, 180)
    EventEnd(0x4)
    Return()

    # Function_65_A579 end

    def Function_66_A5CA(): pass

    label("Function_66_A5CA")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FMeilin is\x01",
            "You should be somewhere in the port area.\x01",
            "…… Do you want to find out more?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 4500, 3050, 30320, 180)
    EventEnd(0x4)
    Return()

    # Function_66_A5CA end

    def Function_67_A638(): pass

    label("Function_67_A638")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FMeilin is\x01",
            "You should be somewhere in the port area.\x01",
            "…… Do you want to find out more?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -19940, 0, -25710, 359)
    EventEnd(0x4)
    Return()

    # Function_67_A638 end

    def Function_68_A6A6(): pass

    label("Function_68_A6A6")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FMeilin is\x01",
            "You should be somewhere in the port area.\x01",
            "…… Do you want to find out more?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -25570, 2000, 23250, 90)
    EventEnd(0x4)
    Return()

    # Function_68_A6A6 end

    def Function_69_A714(): pass

    label("Function_69_A714")

    TalkBegin(0x19)

    ChrTalk(
        0x19,
        (
            "You, Meilin is still\x01",
            "Does not seem to be found?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "If you can not find it by all means,\x01",
            "If you declare a give-up\x01",
            "I think that it will come out … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "……what will you do?\x02",
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
            "To give up\x01",      # 0
            "To give up\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA88")
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
        "#12P#00006F… …. I'm sorry, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Well, it can not be helped.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Well then……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x19,
        "#4SMailly, Gibea ~~~! It is!#3S\x02",
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
        "…… Eh, the winner of Meirin ~ ♪\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "And I gave up\x01",
            "Meilin appears under Lloyd's … …………\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Meilin gives umbrella of peach\x01",
            "Make a mistake bringing it out\x01",
            "I explained it again.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Call(0, 71)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AB35")

    label("loc_AA88")


    ChrTalk(
        0x101,
        "#00000FNo, I will try to find it a little more.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Well then, good luck.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "By the way, my people are not\x01",
            "Do not expect me.\x01",
            "… … Maybe the sun will fall down.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AB35")

    TalkEnd(0x19)
    Return()

    # Function_69_A714 end

    def Function_70_AB39(): pass

    label("Function_70_AB39")

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
            "#00002FDid you mean ……\x01",
            "Are you a Maylin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FHuhu, I found it.\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x1A, 0x101, 500)
    Sleep(50)

    ChrTalk(
        0x1A,
        "Kyat, I found it!\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A,
        "Okay … it was my brother ~?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Onii-chan, are not they?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FHaha, it is finally nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FWell then, to Roy\x01",
            "Let's go report it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Call(0, 71)
    EventEnd(0x5)
    Return()

    # Function_70_AB39 end

    def Function_71_AD1C(): pass

    label("Function_71_AD1C")

    EventBegin(0x0)
    ClearScenarioFlags(0x133, 4)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch21500.itc", 0x28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_B1B5")
    OP_2C(0x6B, 0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Thus Lloyd's,\x01",
            "Call Roy in the place I found Maillin ……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Meilin gives umbrella of peach\x01",
            "Make a mistake bringing it out\x01",
            "I explained it again.\x07\x00\x02",
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
        "#6P#00000F…… That's why.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "I see~……\x01",
            "Meilin, I made a mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Maylin, do not return the umbrella.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Yes, my older brother.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Yes, this ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FWell then, it's an exchange.\x02",
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
            "Give an umbrella to Meirin,\x01",
            "I received a peach umbrella.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#6P#00100FHehe, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "I mean.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Besides that, after a while\x01",
            "Momo-chan is a child\x01",
            "I'm sorry I do not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FHuff, although small, unexpectedly\x01",
            "You are solid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Well, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "I'm also solid about this\x01",
            "One time or two of work …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FEr, Uh …… Anyway\x01",
            "Thank you very much.\x02\x03",
            "#00000FHere is our umbrella\x01",
            "To be responsible\x01",
            "I will deliver it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Oh, I'm counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Please.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Jump("loc_B584")

    label("loc_B1B5")

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
        "#12P#00000F…… That's why.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "I see~……\x01",
            "Meilin, I made a mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Maylin, do not return the umbrella.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Yes, my older brother.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Yes, this ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10100FWell then, it's an exchange.\x02",
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
            "Give an umbrella to Meirin,\x01",
            "I got a peach umbrella.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#12P#00100FHehe, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "I mean.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Besides that, after a while\x01",
            "Momo-chan is a child\x01",
            "I'm sorry I do not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10309FHuff, although small, unexpectedly\x01",
            "You are solid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Well, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "I'm also solid about this\x01",
            "One time or two of work …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FEr, Uh …… Anyway\x01",
            "Thank you very much.\x02\x03",
            "#00000FHere is our umbrella\x01",
            "To be responsible\x01",
            "I will deliver it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Oh, I'm counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Please.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)

    label("loc_B584")

    SetScenarioFlags(0x22, 0)
    NewScene("c0210", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_71_AD1C end

    def Function_72_B591(): pass

    label("Function_72_B591")

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
            "There is a key on the door,\x01",
            "It has a message plate.\x07\x00\x02",
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
            "\"Black Municipal Trading Company · Crossbell Branch\"\x01",
            "* Please knock the direction of the order.\x07\x00\x02",
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
            "#6P#10101F\"Black Municipal Trading Company\" … …\x02\x03",
            "#10103FUmm, a person called Tsao\x01",
            "Is the office in charge?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FTsao Lee.\x01",
            "Having a synonym for \"white olive dragon\"\x01",
            "\"Black moon#4RHayuue#It's a perfect getaway.\x02\x03",
            "#10300FWould you like to say hello to you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FWell, though,\x01",
            "He said that he will do his partner properly\x01",
            "It will not be limited … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FHM……\x02\x03",
            "#00301FAbout one case of Rubathe's site\x01",
            "I wanted to ask you a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FBy the way, that site\x01",
            "I was also aiming for a black moon ……\x02\x03",
            "#00001FAfter all, to \"Crimson Shokai\"\x01",
            "It looks like it was outstanding\x01",
            "What do you think?\x02",
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
            "── Huh, you too,\x01",
            "I am very sorry.\x02",
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

    def lambda_BA95():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BA95)
    Sleep(50)

    def lambda_BAAD():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BAAD)
    Sleep(50)

    def lambda_BAC5():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BAC5)
    Sleep(50)

    def lambda_BADD():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BADD)
    Sleep(50)

    def lambda_BAF5():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BAF5)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#12P#00005FTsa, Tsao branch manager ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#03200FHave a nice day.\x01",
            "Everyone in the Special Affairs Division.\x02\x03",
            "#03209FNo, I was just right.\x02\x03",
            "Actually, a bit for everyone,\x01",
            "There is something I'd like to ask you to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FWhat……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FHave a thing that I want to ask for……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#03200FIf you do not mind,\x01",
            "Would you please listen to the story?\x02\x03",
            "#03204FHuh, of course\x01",
            "I will not say it is impossible.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x27, 0x0, 0x1F4)

    def lambda_BC6C():
        OP_97(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_BC6C)
    Sleep(500)

    def lambda_BC89():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_BC89)
    WaitChrThread(0x27, 1)
    OP_9B(0x1, 0x101, 0x0, 0x1F4, 0x7D0, 0x0)

    ChrTalk(
        0x101,
        "#12P#00005FWait a minute … …! Is it?\x02",
    )

    CloseMessageWindow()
    OP_97(0x28, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    OP_93(0x28, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x28,
        (
            "……I'm sorry.\x01",
            "It became a little troubled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "If you have time\x01",
            "By all means getting help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "I will keep the key open\x01",
            "Please do not hesitate to enter inside.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x28, 0x0, 0x1F4)

    def lambda_BDAA():
        OP_97(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_BDAA)
    Sleep(500)

    def lambda_BDC7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_BDC7)
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
            "#12P#10309FHaha.\x01",
            "They really took people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FWaji is about people\x01",
            "I do not think I can say it at all …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FBut what do you do?\x01",
            "I do not think it is a trap or something ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FThere may be some information,\x01",
            "Do you want to ride here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThat's right.\x01",
            "(Because I am too busy, forcibly\x01",
            "I do not need to go out with you. )\x02",
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

    # Function_72_B591 end

    def Function_73_BFEB(): pass

    label("Function_73_BFEB")


    def lambda_BFF0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_BFF0)

    def lambda_C001():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_C001)
    WaitChrThread(0x27, 1)
    OP_93(0x27, 0xB4, 0x1F4)
    Return()

    # Function_73_BFEB end

    def Function_74_C022(): pass

    label("Function_74_C022")


    def lambda_C027():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_C027)

    def lambda_C038():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_C038)
    WaitChrThread(0x28, 1)
    OP_95(0x28, 18100, 0, 19500, 2000, 0x0)
    OP_93(0x28, 0xB4, 0x1F4)
    Return()

    # Function_74_C022 end

    def Function_75_C06D(): pass

    label("Function_75_C06D")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_C1F0")
    SetChrPos(0x1A2, 18700, 0, 16660, 180)
    SetChrPos(0x102, 19540, 0, 16660, 180)
    SetChrPos(0x101, 18440, 0, 18250, 180)
    SetChrPos(0x104, 19680, 0, 18250, 180)
    SetChrPos(0x109, 18460, 0, 19360, 180)
    SetChrPos(0x105, 19600, 0, 19360, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_C148():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_C148)

    def lambda_C162():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C162)
    Sleep(100)

    def lambda_C17F():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C17F)
    Sleep(50)

    def lambda_C19C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C19C)
    Sleep(100)

    def lambda_C1B9():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C1B9)
    Sleep(50)

    def lambda_C1D6():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C1D6)
    Jump("loc_C437")

    label("loc_C1F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_C316")
    SetChrPos(0x1A2, 18700, 0, 16660, 180)
    SetChrPos(0x102, 19540, 0, 16660, 180)
    SetChrPos(0x101, 18440, 0, 18250, 180)
    SetChrPos(0x109, 19680, 0, 18250, 180)
    SetChrPos(0x104, 18460, 0, 19360, 180)
    SetChrPos(0x105, 19600, 0, 19360, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_C26E():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_C26E)

    def lambda_C288():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C288)
    Sleep(100)

    def lambda_C2A5():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C2A5)
    Sleep(50)

    def lambda_C2C2():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C2C2)
    Sleep(100)

    def lambda_C2DF():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C2DF)
    Sleep(50)

    def lambda_C2FC():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C2FC)
    Jump("loc_C437")

    label("loc_C316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_C437")
    SetChrPos(0x1A2, 18700, 0, 16660, 180)
    SetChrPos(0x102, 19540, 0, 16660, 180)
    SetChrPos(0x101, 18440, 0, 18250, 180)
    SetChrPos(0x105, 19680, 0, 18250, 180)
    SetChrPos(0x104, 19600, 0, 19360, 180)
    SetChrPos(0x109, 18460, 0, 19360, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_C394():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_C394)

    def lambda_C3AE():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C3AE)
    Sleep(100)

    def lambda_C3CB():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C3CB)
    Sleep(50)

    def lambda_C3E8():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C3E8)
    Sleep(100)

    def lambda_C405():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C405)
    Sleep(50)

    def lambda_C422():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C422)

    label("loc_C437")

    OP_68(20080, 600, 15520, 3000)
    MoveCamera(40, 20, 0, 3000)
    OP_6E(560, 3000)
    SetCameraDistance(16390, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    def lambda_C476():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_C476)
    Sleep(50)

    def lambda_C486():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C486)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#12PAlright, then.\x01",
            "I will start explaining at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FOh, ah ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306F(That little boy, shit\x01",
            "I'm setting a girl next door. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10100F(Yeah, that too naturally.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10302F(Huh, really\x01",
            "Ellie liked it too. )\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "#12PWhat is it that you want to say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FOh no, it's okay.\x02\x03",
            "#00000FThan that\x01",
            "Please give me the explanation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#12PHuh, it's pretty obvious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PWell, as you said earlier,\x01",
            "I will tell you the city from now\x01",
            "I will show you around … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PThis wide crossbell\x01",
            "Even if walking around without a goal\x01",
            "I just get tired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PI have decided in advance\x01",
            "You will be aiming for the goal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10105FGoal spot … …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12POh, the Zubari central square\x01",
            "It is the rooftop of the Times department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PAnyway, eventually I will\x01",
            "If you take me there,\x01",
            "I decided to have completed the mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00300FIndeed, it is easy to understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10300FBy the way, until you go there\x01",
            "Can I decide the route freely?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PNo, I am not interested\x01",
            "I will not be bothered by being wandering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PFrom here to the department store,\x01",
            "Always pass via east street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWhat I should say …\x01",
            "I've had a lot of arrangements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PHuhun, pains\x01",
            "I bother to go.\x01",
            "It will be natural to plan that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PHowever, regarding other things\x01",
            "Everything is a no plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PAt best, I'm going down a lot\x01",
            "Please entertain me and Elie sister.\x02",
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
        "#11P#00109FNo, because I am also in a position to guide you ….\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#6PNo, not at all -\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PTo your older sister, on this occasion\x01",
            "I have to take a rest even a bit!\x02",
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
            "#5P#10109FHaha, something already\x01",
            "I feel like Zokcon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell, I knew most of the things … …\x02\x03",
            "#00000FIf it's the current story, it is comparatively normal\x01",
            "I think that it will feel like turning around the city.\x02\x03",
            "Was Shin good with that?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CC0C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_CC0C)
    Sleep(50)

    def lambda_CC1C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CC1C)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#5P#00305FOh, how kind,\x01",
            "Is there anything else than that?\x02\x03",
            "#00300FFor example in alkane shell\x01",
            "Try going, or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10300FOh yeah, to it\x01",
            "Michelin 's theme park.\x02\x03",
            "#10304FAlthough it is closed now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12P- Hun, that famous dicoro\x01",
            "You already decided to go out of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PIndeed it was a lot of fun,\x01",
            "I think it's fun no matter how many times I go -\x01",
            "The purpose of this time is not like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PI have a lot more,\x01",
            "I need to know the crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12Pfor that purpose,\x01",
            "Not just the face as a sightseeing spot,\x01",
            "That's why I have to look after my face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FCrossbell 's true face …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FIs he thinking so far …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FWhew.\x01",
            "How kind of terrible it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12P--Anyways,\x01",
            "Did you understand why this is incredible?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PTime is also regrettable,\x01",
            "Start guiding quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOkay, let's get started.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_D014")
    OP_29(0x73, 0x1, 0x1)
    OP_93(0x104, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#12P#00300FThen, we'll go ahead.\x01",
            "I asked for vigilance behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10100FIt is okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#5P#10300FHuh, let's go.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x4, 0xFF)
    Jump("loc_D18F")

    label("loc_D014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_D0D8")
    OP_29(0x73, 0x1, 0x2)
    OP_93(0x109, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#12P#10100FSo, as we go first\x01",
            "Please give me vigilance behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00300FOkay, okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#5P#10300FHuh, let's go.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x4, 0xFF)
    Jump("loc_D18F")

    label("loc_D0D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_D18F")
    OP_29(0x73, 0x1, 0x3)
    OP_93(0x105, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#12P#10300FWell then, we'll go first.\x01",
            "I left the vigilance behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10100FIt is okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00300FWell, at most, be careful.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x8, 0xFF)

    label("loc_D18F")

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

    # Function_75_C06D end

    def Function_76_D1DD(): pass

    label("Function_76_D1DD")

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

    def lambda_D30E():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_D30E)

    def lambda_D328():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D328)
    Sleep(50)

    def lambda_D345():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D345)
    Sleep(50)

    def lambda_D362():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D362)
    Sleep(50)

    def lambda_D37F():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D37F)
    Sleep(50)

    def lambda_D39C():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D39C)
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

    # Function_76_D1DD end

    def Function_77_D47D(): pass

    label("Function_77_D47D")

    OP_95(0xFE, 19190, -10, 14710, 2000, 0x0)

    def lambda_D496():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D496)
    Sleep(3000)

    def lambda_D4B3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D4B3)
    Return()

    # Function_77_D47D end

    def Function_78_D4C0(): pass

    label("Function_78_D4C0")

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

    # Function_78_D4C0 end

    def Function_79_D570(): pass

    label("Function_79_D570")

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

    # Function_79_D570 end

    def Function_80_D620(): pass

    label("Function_80_D620")

    Sound(821, 2, 40, 0)

    ChrTalk(
        0x101,
        "#12P#00000FIt seems quite lively …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FToday Michishi's event\x01",
            "You seem to be hosting.\x02\x03",
            "#00104FDuring the trade meeting\x01",
            "Because Michelin is closed,\x01",
            "It seems to be held instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FHuhu, if you have Tio\x01",
            "You seem to want to see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FHaha, just dance show\x01",
            "It seems to be doing,\x01",
            "Even if you look at it because it's awesome ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005FWhat is that …?! Is it?\x02",
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
        "#6P#11AWell, Missi ~!\x02",
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
            "#6P#11AThe brother who jumps in\x01",
            "You do pretty much do it!\x02",
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
            "Well, everyone else!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#4SEnjoei, Missi ☆\x07\x00\x02",
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
    SetChrName("The audience")

    AnonymousTalk(
        0xFF,
        "#4SEnjoy!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetChrName("The audience")

    AnonymousTalk(
        0xFF,
        "#4SMitsushi ー ☆ ☆\x02",
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

    def lambda_DD0F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_DD0F)
    Sleep(10)

    def lambda_DD1F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_DD1F)
    WaitChrThread(0x34, 1)

    def lambda_DD30():
        OP_9B(0x0, 0xFE, 0x0, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_DD30)
    Sleep(10)

    def lambda_DD48():
        OP_9B(0x0, 0xFE, 0x0, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_DD48)
    WaitChrThread(0x34, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Olivier and Mitsui\x01",
            "I gave a firm handshake with Gassiri.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x34,
        (
            "#12P#13909FHa ha ha ……\x01",
            "Sounds true, Missi.\x02\x03",
            "#13902FYour dancing sense ……\x01",
            "I took it off hat clearly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Misashi, old boy, too\x01",
            "It was very good Yo ~ ☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Were you learning to dance somewhere ~?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        (
            "#12P#13904FHuh, about ballroom dance\x01",
            "I'm pretty sure.\x02\x03",
            "Originally ladies and elegant\x01",
            "I'd like to take a step,\x01",
            "It was fun to dance with you too.\x02\x03",
            "#13902FFlowstones are crossbell one\x01",
            "I said that it was a mascot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Misashi, shivering cha ~ ☆\x02",
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
        "#6P#00006F(Wha, what are you doing that person … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300F(Apparently on stage\x01",
            "It seems that the insurgence has come down. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106F(Try not to make it as conspicuous as possible\x01",
            "Muller asked me,\x01",
            "This is impossible to imitate …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x34, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_E12A():
        OP_9B(0x1, 0xFE, 0xB4, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_E12A)
    Sleep(10)

    def lambda_E142():
        OP_9B(0x1, 0xFE, 0xB4, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_E142)
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
            "#12P#13905FGee\x01",
            "Apparently it seems the pickup came.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x34, 0x0, 0x1F4)
    OP_6F(0x79)

    ChrTalk(
        0x34,
        (
            "#12P#13900FMiss you, sorry\x01",
            "I will let you go away here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Well, well, that is Zannen ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Misashi, this time\x01",
            "Come also to Wonderland!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        (
            "#12P#13902FHu, that request …\x01",
            "Let me always let it go.\x02\x03",
            "#13904FThis parting is too painful.\x01",
            "That's why we are\x01",
            "It will be irreplaceable.\x02\x03",
            "#13913F……Let's meet again#10RAdios#,#2R·#Close friend#4RAmigo#It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Yes yes\x02",
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

    def lambda_E3D5():

        label("loc_E3D5")

        TurnDirection(0xFE, 0x34, 500)
        Yield()
        Jump("loc_E3D5")

    QueueWorkItem2(0xF, 2, lambda_E3D5)
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
        (
            "#12P#00011FAhh ……\x01",
            "Well, I ran away again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10306FWhew.\x01",
            "Somehow I'm accustomed to the situation.\x02\x03",
            "#10300FIf you come this far,\x01",
            "There are also places where he is likely to run away\x01",
            "I think that it will squeeze to a certain extent … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00106FAnd, let's chase anyway!\x02",
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

    # Function_80_D620 end

    def Function_81_E63A(): pass

    label("Function_81_E63A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_E656")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(100)
    Jump("Function_81_E63A")

    label("loc_E656")

    Return()

    # Function_81_E63A end

    def Function_82_E657(): pass

    label("Function_82_E657")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_E673")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(50)
    Jump("Function_82_E657")

    label("loc_E673")

    Return()

    # Function_82_E657 end

    def Function_83_E674(): pass

    label("Function_83_E674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_E690")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_83_E674")

    label("loc_E690")

    Return()

    # Function_83_E674 end

    def Function_84_E691(): pass

    label("Function_84_E691")

    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0xFFFFF5D8, 0x7D0, 0x0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0xBB8)
    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0xFFFFFC18, 0x7D0, 0x0)
    OP_96(0xFE, 0x1FF4, 0xFFFFFD44, 0xFFFFFF06, 0x7D0, 0x0)
    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0x258, 0x7D0, 0x0)
    Return()

    # Function_84_E691 end

    def Function_85_E704(): pass

    label("Function_85_E704")

    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0x834, 0x7D0, 0x0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0xBB8)
    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0x258, 0x7D0, 0x0)
    OP_96(0xFE, 0x28F0, 0xFFFFFD44, 0xFFFFFF06, 0x7D0, 0x0)
    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0xFFFFFC18, 0x7D0, 0x0)
    Return()

    # Function_85_E704 end

    def Function_86_E777(): pass

    label("Function_86_E777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_E88A")
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
    Jump("Function_86_E777")

    label("loc_E88A")

    Return()

    # Function_86_E777 end

    def Function_87_E88B(): pass

    label("Function_87_E88B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_E99E")
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
    Jump("Function_87_E88B")

    label("loc_E99E")

    Return()

    # Function_87_E88B end

    def Function_88_E99F(): pass

    label("Function_88_E99F")

    Sound(809, 0, 80, 0)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0xBB8)
    OP_93(0xFE, 0x10E, 0x0)
    Return()

    # Function_88_E99F end

    def Function_89_E9C4(): pass

    label("Function_89_E9C4")

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

    # Function_89_E9C4 end

    def Function_90_EA12(): pass

    label("Function_90_EA12")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_EAF1")
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    Jump("loc_EB05")

    label("loc_EAF1")

    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)

    label("loc_EB05")

    OP_0D()

    ChrTalk(
        0x9,
        (
            "You came a lot.\x01",
            "Now, go eat my noodles!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FLet me see, we are\x01",
            "I am a person in the mission support department … …\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the interview with \"One push gourmet\"\x01",
            "I explained what came.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "Oh, that matter?\x01",
            "I'm listening to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You guys are in luck.\x01",
            "This my noble noodle\x01",
            "You can enjoy it for free!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Now, please eat.\x01",
            "This is \"Tenkami noodle≪ sunflower ≫!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FHmm, this is also ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FA bright red soup\x01",
            "It looks very spicy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Huff, you should eat it without saying the fifth five.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "To the taste of Taizen Town which is ahead of hotness,\x01",
            "Invite you guys#2RSorry#I will do it!\x02",
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
            "#00003F(I'm curious about this stuff, but …).\x01",
            "Well, why do not you eat it anyway.\x02",
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
            "Lloyd 's ate Tenko noodle ≪sun rings≫.\x07\x00\x02",
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
            "#00005FSlurp … …\x01",
            "Certainly, it's not just painful\x01",
            "It is a deep taste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FNo, it is delicious, but …\x02\x03",
            "#00106FAs us,\x01",
            "The soup bounces is\x01",
            "You know, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112FWell, indeed …\x01",
            "It will be tough to become a stain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Mumu …… Female customers\x01",
            "It is such a comment all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Soup honey etc.\x01",
            "If you can eat exquisite noodles\x01",
            "It is not a problem to be a problem!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F…… Oh, that's right.\x02",
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
        "#00205F…… Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FOf this exquisite spicy soup\x01",
            "A world of rich taste spreading behind … …\x02\x03",
            "And the soup is entangled\x01",
            "Tiny noodles with elasticity ……\x01",
            "It is good that he does not understand only this man.\x02\x03",
            "#00302FA strong feeling for Osan noodles,\x01",
            "I feel like I understand it somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F38B")

    ChrTalk(
        0x9,
        (
            "Huh … … Is that so!\x01",
            "It seems there were promising young people too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Okay, this special noodle for you\x01",
            "Let's tell you the basic recipe!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Please bye bye by all means!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Recipes for Pirate Bowls Noodle\x07\x00",
            "I was taught.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_F460")

    label("loc_F38B")


    ChrTalk(
        0x9,
        (
            "Huh … … Is that so!\x01",
            "It seems there were promising young people too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Okay, to you specially\x01",
            "Let's make another one!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Please enjoy it by all means!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '天上面『日轮』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('天上面『日轮』', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_F460")

    TurnDirection(0x104, 0x9, 500)

    ChrTalk(
        0x104,
        "#00309FOh, thank you, Osan!\x02",
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
            "#00009F(Randy ……\x01",
            "It seems like you liked it a lot. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F(Huh, here is the introduction\x01",
            "It looks like he may leave it to me. )\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x2, 7)
    SetScenarioFlags(0x172, 2)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_F5EC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F5EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_F609")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_F61C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F61C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_F62F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F62F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_F64C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F64C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_F65F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F65F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_F67C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F67C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_F68F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F68F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_F6AC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F6AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_F6BF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F6BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_F6DC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F6DC")

    OP_29(0x80, 0x1, 0x3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F7DF")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I finished interviewing 6 dining places!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F7D6")

    AnonymousTalk(
        0x101,
        (
            "#00003FMr. Grace right away\x01",
            "It seems I can go to the report … but …\x02\x03",
            "#00000FThe favorite of all six people still\x01",
            "It was not found.\x01",
            "Maybe I'll try harder?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_F7D6")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_F7DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F8B7")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "All members of the Special Affairs Support Division\x01",
            "I found a favorite!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00004FWith this all six people\x01",
            "I found a favorite.\x02\x03",
            "#00000FThis is enough for the interview.\x01",
            "Let's go report to the airlines immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_F8B7")

    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0xB4, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F933")
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
    Jump("loc_F975")

    label("loc_F933")

    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, -13200, 0, 11500, 90)
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, -52470, 2000, 21150, 90)
    BeginChrThread(0xA, 0, 0, 2)

    label("loc_F975")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -10470, 0, 11840, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_90_EA12 end

    def Function_91_F9A1(): pass

    label("Function_91_F9A1")

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

    def lambda_FADB():
        OP_9B(0x0, 0x31, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_FADB)
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
        "Clyde, I kept you waiting.\x02",
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
        "I brought some examples.\x02",
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
            "Clyde is an attache case\x07\x00",
            "Received.\x02",
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
        "Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        "So … how about the success?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        (
            "Yeah, she's also\x01",
            "I'm pretty riding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        (
            "After this, \"Neue-Blanc\" in\x01",
            "I will decide it perfectly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        "Well, that's fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "…… Well, OK.\x01",
            "It is time for a water bus to go out.\x01",
            "Let's say you are preparing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "Well then, I asked for your best regards.\x01",
            "Even if this contract is attached,\x01",
            "Your top is safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        "Please, leave it to me! It is!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x31, 1, 0, 92)
    OP_68(22840, 0, -4880, 3000)
    Sleep(1500)

    def lambda_FDE3():
        OP_9B(0x0, 0x30, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_FDE3)
    WaitChrThread(0x30, 1)

    def lambda_FDFC():

        label("loc_FDFC")

        TurnDirection(0xFE, 0x31, 500)
        Yield()
        Jump("loc_FDFC")

    QueueWorkItem2(0x30, 1, lambda_FDFC)
    Sleep(4000)
    EndChrThread(0x30, 0x1)

    ChrTalk(
        0x30,
        "All right … I will do it!\x02",
    )

    CloseMessageWindow()
    OP_63(0x30, 0x0, 2000, 0x8, 0x9, 0xFA, 0x6)
    Sound(27, 0, 100, 0)

    def lambda_FE49():
        OP_9B(0x0, 0x30, 0x10E, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_FE49)
    Sleep(2000)
    Fade(500)
    OP_68(-2520, 0, 26110, 0)
    MoveCamera(42, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(31670, 0)
    SetChrPos(0x30, 1100, 2000, 23760, 270)
    OP_63(0x30, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)

    def lambda_FEBD():
        OP_9B(0x0, 0x30, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_FEBD)
    WaitChrThread(0x30, 1)

    def lambda_FED6():
        OP_93(0x30, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_FED6)
    WaitChrThread(0x30, 1)
    OP_71(0xA, 0xF1, 0x10E, 0x1, 0x0)
    Sound(462, 0, 100, 0)
    OP_79(0xA)
    OP_64(0x30)

    def lambda_FEFF():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_FEFF)

    def lambda_FF14():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x30, 2, lambda_FF14)
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

    def lambda_FFC7():
        OP_98(0xFE, 0xFFFF8AD0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_FFC7)
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
            "#00305FSomehow it's in Gokigen\x01",
            "I went somewhere.\x02\x03",
            "#00303FWith the wife of that deputy director\x01",
            "\"Neue-Blanc\" in\x01",
            "I guess we are waiting for you … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHuh, what are you gonna do?\x01",
            "To anything more than this\x01",
            "I do not have a train of trails, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F… … Contact Ellie,\x01",
            "Let's go back to the police headquarters once.\x02\x03",
            "#00001FThe identity of the man named Clyde … …\x01",
            "I feel I can grasp it somewhat.\x02",
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

    # Function_91_F9A1 end

    def Function_92_101C5(): pass

    label("Function_92_101C5")

    ClearChrFlags(0x31, 0x4)
    OP_9B(0x0, 0x31, 0x10E, 0xFA0, 0x7D0, 0x0)
    OP_9B(0x0, 0x31, 0x10E, 0x1770, 0x7D0, 0x0)
    OP_9B(0x0, 0x31, 0x10E, 0x1B58, 0x7D0, 0x0)
    OP_9B(0x0, 0x31, 0x5A, 0x1B58, 0x7D0, 0x0)
    OP_9B(0x0, 0x31, 0x0, 0x2710, 0x7D0, 0x0)
    SetChrFlags(0x31, 0x4)
    Return()

    # Function_92_101C5 end

    def Function_93_1021B(): pass

    label("Function_93_1021B")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1055D")
    SetScenarioFlags(0x176, 2)

    ChrTalk(
        0x24,
        (
            "Water bus to Michelin,\x01",
            "We will not be off soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "If you use\x01",
            "Please board early!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000Fby the way……\x01",
            "From the theme park\x01",
            "The request came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FI want you to help Missi,\x01",
            "It was like what it looks like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10103FHmm, what kind of job I wonder\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203F…………………………\x01",
            "Anyway, as soon as possible\x01",
            "Let's face the scene.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FHaha, Tio Sukue,\x01",
            "I am motivated to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHuh, it seems like somehow fun\x01",
            "I had a feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F(Once you cross Michelam,\x01",
            "Unless there is a reasonable circumstance\x01",
            "It seems better to take over. )\x02\x03",
            "(But should we head there anyway)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1055D")

    Call(0, 94)
    Return()

    # Function_93_1021B end

    def Function_94_10561(): pass

    label("Function_94_10561")

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
            "Go to a theme park\x01",      # 0
            "quit\x01",                  # 1
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
        (0, "loc_105CB"),
        (1, "loc_10838"),
        (SWITCH_DEFAULT, "loc_1091F"),
    )


    label("loc_105CB")


    ChrTalk(
        0x101,
        (
            "#6P#00000FWell then,\x01",
            "Let's face it immediately.\x02",
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

    def lambda_1075C():
        OP_98(0xFE, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_1075C)
    WaitChrThread(0x2E, 1)

    def lambda_1077A():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_1077A)
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
            "Thus Lloyd's\x01",
            "Heading to Michelin by a water bus ……\x02\x03",
            "To the theme park waiting for the client\x01",
            "He was carrying legs.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 2)
    NewScene("t1030", 0, 0, 0)
    IdleLoop()
    Jump("loc_1091F")

    label("loc_10838")


    ChrTalk(
        0x101,
        "#6P#00003F…… I suppose I should retype for the moment.\x02",
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
            "For the quest\x01",
            "When heading to Michelam,\x01",
            "Please check the timetable.\x07\x00\x02",
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
    Jump("loc_1091F")

    label("loc_1091F")

    Return()

    # Function_94_10561 end

    def Function_95_10920(): pass

    label("Function_95_10920")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x0, 38840, -2500, -460, 270)
    OP_69(0xFF, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_95_10920 end

    def Function_96_1094E(): pass

    label("Function_96_1094E")

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

    def lambda_10A83():
        OP_9B(0x1, 0xFE, 0x0, 0xC350, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_10A83)
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

    def lambda_10B34():
        OP_98(0xFE, 0xFFFFF448, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_10B34)
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
        "#00200F….\x02",
    )

    CloseMessageWindow()

    def lambda_10D11():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10D11)
    Sleep(50)

    def lambda_10D21():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10D21)
    Sleep(50)

    def lambda_10D31():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10D31)
    Sleep(50)

    def lambda_10D41():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10D41)
    Sleep(50)

    def lambda_10D51():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10D51)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00305F…… Hey Lloyd.\x01",
            "Thio sake 's guy,\x01",
            "Did something happen?\x02\x03",
            "After joining\x01",
            "Until the water bus\x01",
            "You'll be feeling that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FGeez …\x01",
            "Look somewhere far away\x01",
            "Hold it … ___ ___ 0\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FI am somewhat lonely\x01",
            "It's atmosphere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell, hmm … ….\x01",
            "I wonder what I should say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FUm, Tio.\x01",
            "Is somewhere sick?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F………………House.\x01",
            "I am okay.\x02\x03",
            "#00202FI was a bit confused … …\x01",
            "We are getting sorted out.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x5A, 0x1F4)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00208F…… People like this,\x01",
            "It is becoming an adult …\x02",
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
            "Quest 【Part-time job at theme park】\x07\x00",
            "Achieved!\x02",
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

    # Function_96_1094E end

    def Function_97_110E7(): pass

    label("Function_97_110E7")

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

    # Function_97_110E7 end

    def Function_98_11179(): pass

    label("Function_98_11179")


    def lambda_1117E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1117E)

    def lambda_1118F():
        OP_95(0xFE, 41760, -2500, -1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1118F)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 37640, -2500, 320, 2000, 0x0)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_98_11179 end

    def Function_99_111C4(): pass

    label("Function_99_111C4")


    def lambda_111C9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_111C9)

    def lambda_111DA():
        OP_95(0xFE, 41760, -2500, -1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_111DA)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 37640, -2500, -1280, 2000, 0x0)
    OP_93(0x102, 0x2D, 0x1F4)
    Return()

    # Function_99_111C4 end

    def Function_100_1120F(): pass

    label("Function_100_1120F")


    def lambda_11214():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_11214)

    def lambda_11225():
        OP_95(0xFE, 41760, -2500, -1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11225)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 38890, -2500, 1500, 2000, 0x0)
    OP_93(0x104, 0xB4, 0x1F4)
    Return()

    # Function_100_1120F end

    def Function_101_1125A(): pass

    label("Function_101_1125A")


    def lambda_1125F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1125F)

    def lambda_11270():
        OP_95(0xFE, 41760, -2500, -1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11270)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 39690, -2500, -1720, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_101_1125A end

    def Function_102_112A5(): pass

    label("Function_102_112A5")


    def lambda_112AA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_112AA)

    def lambda_112BB():
        OP_95(0xFE, 41760, -2500, -1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_112BB)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 40640, -2500, 1110, 2000, 0x0)
    OP_93(0x105, 0xE1, 0x1F4)
    Return()

    # Function_102_112A5 end

    def Function_103_112F0(): pass

    label("Function_103_112F0")


    def lambda_112F5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_112F5)

    def lambda_11306():
        OP_95(0xFE, 41760, -2500, -1910, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11306)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 41340, -2500, -150, 1500, 0x0)
    OP_93(0x103, 0x10E, 0x1F4)
    Return()

    # Function_103_112F0 end

    def Function_104_1133B(): pass

    label("Function_104_1133B")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11413")

    ChrTalk(
        0x1A2,
        "Is this you east?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FNo, but it's different …\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "that's right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "…… Certainly, Me is OK\x01",
            "I think I told you to go through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FThat's right … it was bad.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_11470")

    label("loc_11413")


    ChrTalk(
        0x1A2,
        (
            "Hey, the way back is good, but\x01",
            "The detour is a camper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Take me to Eastern Street quickly.\x02",
    )

    CloseMessageWindow()

    label("loc_11470")

    SetChrPos(0x0, -28110, 2000, 23520, 90)
    EventEnd(0x4)
    Return()

    # Function_104_1133B end

    def Function_105_11484(): pass

    label("Function_105_11484")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1152E")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003F(Once you cross Michelam,\x01",
            "Unless there is a reasonable circumstance\x01",
            "It seems better to take over. )\x02\x03",
            "(But should we head there anyway)\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 94)
    Jump("loc_115CF")

    label("loc_1152E")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Water bus and timetable for \"Michelin\"\x01\x01",
            "※ Michelin boasts a theme park\x01",
            "\"Wonderland\" is opening!\x01",
            "Enjoy a fun time!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)

    label("loc_115CF")

    Return()

    # Function_105_11484 end

    def Function_106_115D0(): pass

    label("Function_106_115D0")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "\"Lupinas river and first lighthouse\"\x01\x01",
            "Do not enter other than stakeholders.\x01",
            "~ Cross Bell City ~\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_106_115D0 end

    SaveToFile()

Try(main)

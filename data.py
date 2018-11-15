class Data:
    axis = {"BD": 2, "BE": 82, "BG": 48, "BA": 2, "BM": 1, "JP": 521, "JM": 4, "JO": 1, "BR": 125, "JE": 1, "BY": 1, "BZ": 7, "RU": 808, "RS": 23, "RE": 1, "RO": 93, "GU": 1, "GT": 18, "GR": 35, "GP": 9, "BH": 1, "GG": 8, "GF": 2, "GE": 1, "GB": 361, "HR": 7, "HT": 1, "HU": 52, "HK": 56, "HN": 10, "AD": 3, "PR": 15, "PT": 40, "PY": 3, "IQ": 42, "PA": 26, "PF": 1, "PE": 11, "PK": 3, "PH": 6, "PL": 96, "PM": 2, "ZM": 1, "EE": 14, "EG": 10, "ZA": 18, "EC": 7, "AL": 1, "AO": 1, "ES": 248, "MD": 2, "UY": 3, "MC": 1, "MO": 2, "US": 7350, "MU": 1, "MT": 1, "MV": 1, "MQ": 5, "MY": 19, "MX": 426, "AT": 163, "FR": 1573, "MA": 2, "FI": 136, "FO": 1, "NI": 23, "NL": 266, "NO": 160, "NA": 1, "NC": 1, "NZ": 16, "CH": 144, "CO": 94, "CN": 381, "CL": 12, "CA": 665, "CZ": 153, "CR": 10, "CU": 5, "SY": 1, "KE": 3, "SR": 1, "SV": 32, "SK": 36, "KR": 236, "SI": 2, "KW": 5, "SN": 5, "SM": 1, "KZ": 7, "SA": 23, "SG": 9, "SE": 253, "DO": 8, "DK": 43, "DE": 674, "DZ": 9, "MK": 2, "TZ": 3, "TW": 389, "TT": 1, "TR": 77, "LK": 2, "LI": 1, "LV": 22, "LT": 25, "LU": 14, "LS": 1, "TH": 61, "AE": 11, "VE": 6, "AF": 13, "AI": 12, "IS": 14, "IR": 5, "AM": 2, "IT": 684, "VN": 27, "AR": 63, "AU": 186, "IL": 8, "AW": 4, "IN": 304, "LB": 1, "AZ": 1, "IE": 54, "ID": 39, "UA": 60}
    cisco = {"BD": 4320, "BE": 3335, "BF": 298, "BG": 3337, "BA": 4267, "BB": 367, "WF": 1, "BL": 1, "BM": 174, "BN": 99, "BO": 1641, "JP": 10296, "BI": 78, "BJ": 500, "BT": 883, "JM": 730, "BW": 1285, "WS": 38, "BQ": 7, "BR": 21952, "BS": 431, "JE": 144, "BY": 815, "BZ": 718, "RU": 49888, "RW": 704, "RS": 3220, "TL": 10, "RE": 127, "TM": 44, "LR": 63, "RO": 5158, "GW": 144, "GU": 140, "GT": 1182, "GR": 5764, "GQ": 143, "GP": 95, "BH": 1120, "GY": 157, "GG": 146, "GF": 32, "GE": 1672, "GD": 62, "GB": 27243, "GA": 720, "GN": 338, "GM": 539, "GL": 34, "GI": 93, "GH": 1452, "OM": 714, "JO": 658, "HR": 1712, "HT": 977, "HU": 2884, "HK": 7854, "HN": 998, "AD": 44, "PR": 1440, "PS": 588, "PW": 2, "PT": 2729, "KN": 57, "PY": 716, "AI": 18, "PA": 2160, "PF": 27, "PG": 739, "PE": 3895, "PK": 3753, "PH": 7891, "A2": 22, "PL": 10170, "PM": 4, "ZM": 2568, "EE": 344, "EG": 4877, "ZA": 7532, "EC": 3289, "AL": 479, "AO": 1149, "SB": 52, "EU": 943, "ET": 476, "SO": 122, "ZW": 2067, "KY": 243, "ES": 11158, "ER": 4, "ME": 128, "MD": 339, "MG": 255, "MF": 12, "MA": 7349, "MC": 163, "UZ": 115, "MM": 638, "ML": 455, "MO": 205, "MN": 809, "MH": 32, "MK": 2618, "MU": 2409, "MT": 319, "MW": 252, "MV": 122, "MQ": 82, "MP": 11, "MS": 4, "MR": 126, "IM": 248, "UG": 1102, "UA": 8062, "MX": 34023, "AT": 3091, "FR": 16076, "IO": 2, "FX": 43, "AX": 3, "FI": 985, "FJ": 409, "FM": 7, "FO": 22, "NI": 656, "NL": 9661, "NO": 2643, "NA": 762, "VU": 22, "NC": 153, "NE": 230, "NG": 5970, "NZ": 1561, "NP": 512, "NR": 6, "CK": 9, "CI": 740, "CH": 2594, "CO": 5951, "CN": 38118, "CM": 2077, "CL": 10484, "CA": 440087, "CG": 190, "CF": 74, "CD": 259, "CZ": 3788, "CY": 1052, "CR": 1884, "CV": 56, "CU": 80, "SZ": 108, "SY": 121, "KG": 286, "KE": 6567, "SS": 18, "SR": 46, "KI": 163, "KH": 1037, "SV": 1252, "KM": 20, "ST": 35, "SK": 1927, "KR": 22022, "SI": 1061, "KP": 1, "KW": 2624, "SN": 1661, "SM": 4, "SL": 108, "SC": 196, "KZ": 1804, "SA": 12785, "SG": 10868, "SE": 2814, "SD": 978, "DO": 2635, "DM": 25, "DJ": 274, "DK": 17226, "VG": 203, "DE": 12594, "YE": 67, "DZ": 1315, "US": 660557, "LV": 561, "UY": 663, "YT": 5, "TZ": 1442, "LC": 114, "LA": 362, "TV": 9, "TW": 7076, "TT": 374, "TR": 7338, "LK": 979, "LI": 45, "TN": 2223, "TO": 6, "LT": 713, "LU": 199, "TJ": 99, "LS": 73, "TH": 17841, "TG": 187, "TD": 121, "TC": 66, "LY": 872, "VA": 2, "VC": 115, "AE": 6082, "VE": 5191, "AG": 592, "AF": 2264, "IQ": 1295, "VI": 273, "IS": 482, "IR": 3752, "AM": 172, "IT": 22463, "VN": 6240, "AN": 175, "AP": 40, "AS": 21, "AR": 702379, "AU": 19035, "IL": 2846, "AW": 64, "IN": 30480, "LB": 1034, "AZ": 1093, "IE": 1940, "ID": 6861, "MY": 4606, "QA": 1649, "MZ": 1047}
    dahua = {"BD": 1776, "BE": 1398, "BG": 9989, "BA": 588, "BB": 9, "BM": 11, "BN": 19, "BO": 2792, "BH": 140, "BJ": 1, "BT": 1, "JM": 37, "JO": 603, "BQ": 2, "BR": 91378, "BS": 49, "BY": 208, "BZ": 13, "RU": 6516, "RS": 3556, "RE": 350, "LR": 1, "RO": 18685, "GU": 34, "GT": 591, "GR": 2280, "GQ": 3, "GP": 347, "JP": 54, "GY": 21, "GF": 159, "GE": 156, "GD": 3, "GB": 2486, "GN": 1, "GL": 2, "GI": 6, "GH": 43, "OM": 154, "BW": 3, "HR": 273, "HT": 5, "HU": 1995, "HK": 3224, "HN": 659, "AD": 15, "PR": 380, "PS": 217, "PT": 5156, "KN": 4, "PY": 421, "AI": 1, "PA": 1689, "PF": 8, "PE": 708, "PK": 3009, "PH": 285, "PL": 13494, "ZM": 6, "EE": 156, "EG": 5435, "ZA": 1174, "EC": 817, "AL": 1299, "AO": 44, "EU": 3, "ET": 1, "ZW": 3, "KY": 26, "ES": 8123, "ME": 369, "MD": 928, "MG": 3, "MF": 3, "UY": 693, "MC": 7, "UZ": 71, "LV": 615, "MO": 293, "MN": 16, "MK": 1240, "MU": 197, "MT": 151, "MV": 5, "MQ": 172, "MR": 15, "UG": 13, "MY": 3013, "MX": 16281, "AT": 145, "FR": 13610, "MA": 1470, "FX": 4, "FI": 471, "FJ": 10, "FO": 4, "NI": 11, "NL": 973, "NO": 56, "NA": 25, "NC": 10, "NG": 12, "NZ": 197, "NP": 32, "CI": 15, "CH": 76, "CO": 18127, "CN": 46027, "CM": 1, "CL": 10602, "CA": 2081, "CZ": 794, "CY": 336, "CR": 3326, "CV": 1, "SZ": 2, "SY": 28, "KG": 7, "KE": 118, "SR": 19, "KH": 3560, "SV": 37, "ST": 1, "SK": 849, "KR": 19025, "SI": 505, "KW": 1893, "SN": 22, "SC": 2, "KZ": 479, "SA": 286, "SG": 1146, "SE": 245, "SD": 5, "DO": 739, "DM": 3, "DK": 139, "DE": 507, "YE": 17, "DZ": 611, "US": 12373, "YT": 99, "LB": 73, "LC": 6, "LA": 45, "TW": 23893, "TT": 75, "TR": 5694, "LK": 294, "TN": 1389, "LT": 913, "LU": 23, "TJ": 234, "TH": 8210, "TC": 12, "LY": 9, "VC": 11, "AE": 1514, "VE": 1663, "AG": 4, "AF": 22, "IQ": 37, "VI": 5, "IS": 14, "IR": 6751, "AM": 775, "IT": 3223, "VN": 53884, "AN": 61, "AR": 16203, "AU": 1093, "IL": 5446, "AW": 24, "IN": 9940, "TZ": 66, "AZ": 364, "IE": 1024, "ID": 1161, "UA": 9543, "QA": 264, "MZ": 96}
    huawei = {"BD": 214, "BE": 31, "BF": 11, "BG": 1229, "BA": 102, "BB": 5, "BM": 5, "BN": 24, "BO": 1347, "BH": 138, "BI": 23, "BT": 2, "JM": 867, "JO": 108, "WS": 1, "BR": 5748, "CR": 34, "JE": 1, "BY": 173, "BZ": 1419, "RU": 2457, "RW": 9, "RS": 394, "TL": 2, "PA": 67, "RO": 532, "GU": 2, "GT": 71, "GR": 143, "JP": 22, "GE": 151, "GB": 402, "GA": 36, "GN": 8, "GM": 6, "GI": 1, "GH": 308, "OM": 340, "IL": 7, "BW": 3, "HR": 123, "HT": 3, "HU": 24656, "HK": 8539, "HN": 2, "PR": 296, "PT": 272, "PY": 567, "AI": 5, "LV": 70, "PG": 16, "PE": 436, "PK": 563, "PH": 330, "TM": 1, "PL": 1159, "ZM": 432, "EE": 83, "EG": 349, "ZA": 770, "EC": 463, "AL": 1105, "AO": 19, "SB": 6, "EU": 2, "ET": 30, "ZW": 91, "ES": 1839, "ER": 3, "ME": 121, "MD": 35, "MG": 1, "UY": 158, "MC": 2, "UZ": 207, "MM": 23, "ML": 26, "MO": 57, "MN": 10, "MK": 146, "MU": 1081, "MW": 35, "MV": 27, "MR": 4, "IM": 3, "UG": 212, "MY": 396, "MX": 13868, "MZ": 73, "FR": 687, "FI": 29, "FJ": 5, "FO": 2, "NI": 13, "NL": 206, "NO": 44, "SO": 25, "NE": 9, "NG": 138, "NZ": 7076, "NP": 82, "CI": 12, "CH": 104, "CO": 1991, "CN": 301779, "CM": 35, "CL": 1159, "CA": 138, "CG": 8, "NA": 2, "CD": 71, "CZ": 409, "CY": 9, "MA": 1013, "CV": 12, "CU": 76, "SZ": 64, "SY": 15, "KG": 5, "KE": 270, "SS": 26, "SR": 1, "KH": 44, "SV": 5, "KM": 6, "SK": 141, "KR": 165, "SI": 13, "KW": 103, "SN": 14, "SL": 17, "KZ": 189, "SA": 1793, "SG": 150, "SE": 44, "SD": 295, "DO": 39, "DM": 1, "DK": 40, "DE": 390, "YE": 10, "DZ": 940, "US": 832, "TZ": 87, "LA": 470, "TW": 105, "TT": 56, "TR": 932, "LK": 113, "LI": 1, "TN": 367, "TO": 1, "LT": 10, "LU": 2, "TJ": 66, "TH": 9372, "TG": 23, "TD": 14, "LY": 59, "AE": 134, "VE": 1405, "IQ": 54, "IS": 6, "IR": 312, "AM": 6, "IT": 1822, "VN": 2566, "AN": 2, "AR": 7052, "AU": 295, "AT": 96, "IN": 3035, "LB": 10, "AZ": 218, "IE": 44, "ID": 2904, "UA": 1574, "QA": 136}
    mikrotik = {"BD": 36317, "BE": 1816, "BF": 114, "BG": 15897, "BA": 6769, "BB": 22, "BL": 9, "BM": 1, "BN": 1, "BO": 2622, "JP": 636, "BI": 269, "BJ": 1143, "BT": 10, "JM": 169, "BW": 1029, "WS": 205, "BQ": 2, "BR": 303708, "BS": 47, "JE": 2, "BY": 2953, "BZ": 76, "RU": 142024, "RW": 213, "RS": 15619, "TL": 303, "RE": 22, "A2": 4, "LR": 161, "RO": 11869, "GW": 1, "GT": 1209, "GR": 9749, "GQ": 88, "GP": 5, "BH": 95, "GY": 68, "GG": 4, "GF": 13, "GE": 4276, "GD": 26, "GB": 7737, "GA": 134, "GN": 405, "GM": 44, "GL": 4, "KW": 101, "GI": 9, "GH": 664, "OM": 247, "TN": 41, "JO": 61, "HR": 8243, "HT": 16, "HU": 20131, "HK": 3769, "HN": 3634, "AD": 195, "PR": 4518, "PS": 3042, "PW": 4, "PT": 2033, "KN": 26, "PY": 2386, "AI": 2, "PA": 1795, "PF": 15, "PG": 465, "PE": 9122, "PK": 7398, "PH": 2695, "TM": 2, "PL": 69615, "ZM": 660, "EE": 2231, "EG": 4915, "ZA": 54186, "EC": 17334, "AL": 6306, "AO": 138, "SB": 19, "EU": 211, "ET": 23, "ZW": 803, "KY": 5, "ES": 40499, "ER": 1, "ME": 751, "MD": 8226, "MG": 425, "MF": 424, "UY": 4808, "MC": 11, "UZ": 228, "MM": 306, "ML": 174, "MO": 118, "MN": 1349, "MK": 3418, "MU": 992, "MT": 1681, "MW": 1307, "MV": 160, "MQ": 22, "MR": 6, "IM": 39, "UG": 834, "MY": 4726, "MX": 15172, "IL": 1007, "FR": 3426, "MA": 246, "FX": 514, "SJ": 1, "FI": 511, "FJ": 3, "FO": 1, "NI": 1287, "NL": 4727, "NO": 2346, "NA": 481, "VU": 34, "NC": 230, "NE": 6, "NG": 4991, "NZ": 3434, "NP": 4387, "NU": 2, "CK": 42, "CI": 272, "CH": 1333, "CO": 23642, "CN": 159455, "CM": 3411, "CL": 8161, "CA": 12733, "CG": 481, "CD": 619, "CZ": 44599, "CY": 1666, "CR": 4246, "CV": 11, "CU": 1, "SZ": 348, "SY": 287, "KG": 1064, "KE": 6488, "SS": 231, "SR": 11, "KH": 20599, "SV": 326, "KM": 3, "SK": 10849, "KR": 34238, "SI": 4044, "SO": 487, "SN": 35, "SM": 10, "SL": 168, "SC": 277, "KZ": 5904, "SA": 1934, "SG": 1116, "SE": 4177, "SD": 37, "DO": 1948, "DM": 9, "DJ": 11, "DK": 1572, "VG": 11, "DE": 8750, "YE": 8827, "DZ": 144, "US": 103792, "YT": 8, "LB": 4531, "LC": 10, "LA": 140, "TW": 12879, "TT": 45, "TR": 16006, "LK": 420, "LI": 3, "LV": 11759, "TO": 3, "LT": 6356, "LU": 159, "TJ": 223, "LS": 448, "TH": 53222, "TG": 66, "TD": 647, "TC": 1, "LY": 1601, "VC": 12, "AE": 1759, "VE": 8556, "AG": 5, "AF": 712, "IQ": 8881, "VI": 195, "IS": 128, "IR": 100548, "AM": 1832, "IT": 45899, "VN": 8107, "AN": 47, "AP": 10, "AR": 47759, "AU": 6972, "AT": 7842, "AW": 14, "IN": 104568, "TZ": 1608, "AZ": 910, "IE": 3865, "ID": 162391, "UA": 66743, "QA": 46, "MZ": 806}
    panasonic = {"BD": 2, "BE": 47, "BG": 10, "BA": 3, "BO": 5, "JP": 16998, "JO": 1, "BR": 402, "BY": 4, "RU": 146, "RO": 9, "GT": 11, "GR": 2, "GP": 5, "GY": 1, "GE": 4, "GB": 285, "HU": 15, "HK": 299, "HN": 2, "PS": 1, "PT": 20, "PY": 5, "PA": 125, "UY": 25, "PE": 8, "PH": 5, "PL": 81, "EG": 37, "ZA": 54, "EC": 29, "ES": 104, "MD": 1, "MA": 2, "MC": 1, "UZ": 2, "MM": 2, "MO": 1, "MK": 1, "UG": 1, "UA": 30, "MX": 173, "AT": 35, "FR": 88, "FI": 36, "FJ": 1, "NI": 1, "NL": 68, "NO": 11, "NZ": 20, "NP": 8, "CH": 48, "CO": 89, "CN": 81, "CL": 4, "CA": 35, "CZ": 30, "CR": 21, "KG": 1, "KE": 3, "KH": 1, "SV": 5, "SK": 11, "KR": 27, "SI": 1, "KW": 1, "KZ": 10, "SA": 4, "SG": 10, "SE": 54, "DK": 10, "DE": 761, "US": 516, "TZ": 1, "TW": 223, "TR": 41, "LV": 5, "LT": 1, "TH": 180, "TC": 1, "LY": 1, "AE": 3, "VE": 9, "IS": 1, "IR": 12, "IT": 197, "VN": 192, "AN": 1, "AR": 80, "AU": 51, "IL": 6, "IN": 173, "LB": 1, "IE": 4, "ID": 39, "MY": 35}
    realtek = {"BD": 35, "BE": 12, "BG": 608, "BA": 27, "BN": 1, "BO": 1, "JP": 31999, "BJ": 1, "JM": 1, "JO": 75, "BR": 2511, "BS": 145, "BY": 223, "RU": 16002, "RW": 3, "RS": 26, "RE": 1, "LR": 1, "RO": 3514, "GT": 6, "GR": 17, "GY": 1, "GE": 55, "GB": 81, "GA": 1, "GI": 2, "GH": 1, "OM": 1, "TN": 4, "BW": 12, "HR": 51, "HU": 197, "HK": 160, "HN": 13, "AD": 3, "PR": 1, "PS": 20, "PT": 49, "KN": 3, "PA": 20, "PF": 1, "PE": 11, "PK": 2283, "PH": 92, "PL": 3373, "ZM": 9, "EE": 32, "EG": 5, "ZA": 94, "EC": 9, "AL": 41, "AO": 3, "EU": 1, "ZW": 5, "KY": 2, "ES": 30165, "MD": 72, "UY": 151, "UZ": 59, "MM": 7, "ML": 2, "MO": 4, "MN": 9, "MK": 19, "MT": 12, "MQ": 1, "MY": 138, "MX": 30, "IL": 1446, "FR": 120, "MA": 308, "FX": 1, "FI": 8, "NI": 3, "NL": 5, "NO": 26, "VU": 2, "NE": 3, "NG": 3, "NZ": 105, "NP": 15, "CI": 2, "CH": 89, "CO": 10, "CN": 29133, "CM": 14, "CL": 75, "CA": 243, "CG": 1, "CZ": 648, "CY": 59, "CR": 69, "SY": 49, "KG": 142, "KE": 1, "KH": 1, "SV": 6, "SK": 365, "KR": 2937, "SI": 128, "KW": 292, "SC": 14, "KZ": 190, "SA": 18, "SG": 35, "SE": 189, "SD": 8, "DO": 3, "DK": 34, "DE": 632, "DZ": 7, "US": 1316, "LB": 20, "LA": 2, "TW": 40361, "TT": 1, "TR": 97, "LK": 949, "LV": 738, "LT": 741, "TJ": 3, "TH": 4877, "LY": 3, "AE": 405, "VE": 612, "VI": 1, "IS": 96, "IR": 59, "AM": 18, "IT": 569, "VN": 206, "AR": 234, "AU": 794, "AT": 52, "AW": 4, "IN": 25153, "TZ": 4, "AZ": 5, "IE": 35, "ID": 61, "UA": 10365, "QA": 2, "MZ": 21}
    samsung = {"BD": 7, "BE": 49, "BG": 91, "BO": 15, "JP": 646, "JO": 2, "BR": 563, "BY": 8, "RU": 542, "RS": 7, "TL": 1, "RE": 3, "RO": 81, "GU": 6, "GT": 4, "GR": 163, "BH": 4, "GY": 4, "GF": 4, "GE": 1, "GB": 855, "OM": 9, "TN": 6, "HR": 8, "HT": 1, "HU": 59, "HK": 467, "HN": 1, "AD": 3, "PR": 5, "PS": 5, "PT": 51, "PY": 2, "PA": 11, "PE": 7, "PK": 14, "PH": 7, "PL": 225, "EE": 7, "EG": 49, "ZA": 180, "EC": 38, "AL": 2, "AO": 4, "ES": 355, "MD": 2, "UY": 44, "UZ": 9, "MM": 1, "MO": 1, "MK": 6, "MU": 1, "IM": 1, "UG": 1, "MY": 74, "MX": 316, "IL": 339, "FR": 337, "MA": 54, "FI": 95, "NL": 200, "NO": 43, "NC": 1, "NG": 7, "NZ": 39, "CI": 2, "CH": 51, "CO": 85, "CN": 467, "CL": 154, "CA": 354, "CZ": 74, "CY": 7, "CR": 5, "CU": 1, "SY": 5, "KG": 4, "KE": 3, "KH": 4, "SK": 65, "KR": 12402, "SI": 7, "KW": 4, "SN": 1, "KZ": 12, "SA": 34, "SG": 62, "SE": 145, "DO": 49, "DK": 14, "DE": 534, "DZ": 1, "US": 4002, "LB": 8, "LC": 2, "LA": 1, "TW": 1719, "TT": 4, "TR": 172, "LK": 1, "LV": 20, "LT": 29, "TM": 1, "LR": 2, "TH": 218, "LY": 1, "AE": 123, "VE": 346, "AG": 1, "IQ": 1, "IR": 70, "AM": 4, "IT": 930, "VN": 217, "AR": 94, "AU": 484, "AT": 44, "IN": 110, "TZ": 2, "AZ": 5, "IE": 29, "ID": 117, "UA": 138, "QA": 12, "MZ": 1}
    ubiquiti = {"BD": 27, "BE": 142, "BF": 9, "BG": 2629, "BA": 1489, "BB": 2, "WF": 76, "BM": 2, "BO": 45, "JP": 102, "BI": 1, "BJ": 200, "JM": 27, "BW": 912, "WS": 51, "BQ": 105, "BR": 510422, "BS": 24, "JE": 1, "BY": 12, "BZ": 12, "RU": 8877, "RW": 29, "RS": 15500, "TL": 2, "RE": 1, "LR": 4, "RO": 1754, "GU": 4, "GT": 55, "GR": 375, "GQ": 10, "GP": 6, "GY": 11, "GF": 2, "GE": 1723, "GD": 9, "GB": 8174, "GA": 12, "GM": 9, "KW": 22, "GH": 122, "OM": 3, "TN": 7, "HR": 158, "HT": 45, "HU": 5131, "HK": 40, "HN": 324, "AD": 140, "PR": 3954, "PS": 760, "PT": 87, "KN": 2, "PY": 612, "PA": 345, "PF": 2, "PG": 328, "PE": 97, "PK": 915, "PH": 84, "PL": 28558, "ZM": 45, "EE": 190, "EG": 11, "ZA": 2796, "EC": 323, "AL": 1787, "AO": 6, "SB": 3, "EU": 57, "ZW": 49, "KY": 3, "ES": 54061, "ME": 73, "MD": 479, "MG": 4, "UY": 126, "UZ": 3, "MM": 18, "ML": 24, "MO": 1, "MN": 10, "MH": 2, "MK": 272, "MU": 29, "MT": 8, "MW": 13, "MV": 4, "MQ": 15, "MR": 6, "IM": 10, "UG": 186, "MY": 90, "MX": 1734, "IL": 13, "FR": 1994, "FX": 7, "FI": 63, "FO": 45, "NI": 70, "NL": 448, "NO": 451, "NA": 4, "VU": 6, "NC": 2, "NE": 2, "NG": 230, "NZ": 22440, "NP": 291, "NR": 4, "CK": 3, "CI": 4, "CH": 133, "CO": 886, "CN": 819, "CM": 15, "CL": 1551, "CA": 18707, "CG": 2, "CD": 14, "CZ": 10093, "CY": 241, "CR": 74, "CU": 3, "SZ": 10, "KG": 5, "KE": 128, "SR": 15, "KH": 25, "SV": 9, "KM": 1, "SK": 9872, "KR": 30, "SI": 260, "SO": 30, "SN": 3, "SL": 5, "SC": 48, "KZ": 95, "SA": 19, "SG": 546, "SE": 1044, "SD": 10, "DO": 67, "DM": 5, "DK": 224, "DE": 3685, "YE": 2, "DZ": 1, "US": 81321, "TZ": 225, "LC": 2, "LA": 1, "TW": 38, "TT": 9, "TR": 1225, "LK": 28, "LV": 1112, "LT": 650, "LU": 3, "TJ": 5, "LS": 29, "TH": 3768, "TG": 109, "TC": 2, "LY": 66, "VC": 1, "AE": 34, "VE": 381, "AG": 2, "AF": 41, "IQ": 10683, "VI": 5, "IS": 69, "IR": 26550, "AM": 233, "IT": 20925, "VN": 108, "AN": 35, "AP": 1, "AS": 2, "AR": 40670, "AU": 2641, "AT": 910, "AW": 1, "IN": 15376, "LB": 8, "AZ": 158, "IE": 1047, "ID": 1220, "UA": 12377, "MZ": 6}
    zte = {"BD": 180, "BE": 4, "BG": 2937, "BA": 743, "BO": 1452, "JP": 1182, "BJ": 2, "JO": 6630, "BR": 34039, "JE": 3, "BY": 2102, "BZ": 154, "RU": 18003, "RS": 262, "TL": 1, "RE": 121, "PA": 2, "RO": 2736, "GT": 566, "GR": 7940, "GP": 1, "BH": 33, "GE": 148, "GB": 98, "GH": 4, "IL": 8, "HR": 302, "HT": 4, "HU": 881, "HK": 507, "HN": 47, "PS": 4, "PT": 244, "PY": 17, "LV": 34, "PE": 8, "PK": 290, "PH": 19, "PL": 3027, "ZM": 15, "EE": 178, "EG": 146171, "ZA": 1037, "EC": 91, "IT": 1660, "AO": 17, "EU": 1, "ET": 115, "SO": 2, "ZW": 4, "ES": 1458, "ME": 36, "MD": 92, "MG": 4, "UY": 45, "UZ": 49, "MM": 29, "ML": 686, "MO": 3, "MN": 8, "US": 1634, "MU": 249, "MT": 26, "MW": 8, "MR": 2, "UA": 270, "MX": 26, "MZ": 43, "FR": 2838, "FI": 28, "FJ": 3, "NI": 64, "NL": 1858, "NO": 15, "NA": 6, "VU": 7, "NG": 1003, "NP": 32, "CI": 2, "CH": 9, "CO": 52938, "CN": 31381, "CL": 93, "CA": 22494, "CD": 4, "CZ": 1059, "CY": 58, "MA": 1202, "SY": 21, "KG": 9, "KE": 166, "KH": 21, "SV": 260, "SK": 246, "KR": 9, "SI": 22, "KW": 117, "SN": 22, "SL": 1, "KZ": 86, "SA": 1030, "SG": 43, "SE": 41, "DO": 20, "DK": 4, "VG": 15, "DE": 53, "YE": 1, "DZ": 2292, "MK": 23, "LB": 1961, "LA": 1, "TW": 38, "TR": 457, "LK": 227, "LI": 1, "TN": 83, "LT": 1894, "LU": 1, "TJ": 6, "LS": 10, "TH": 69179, "LY": 558, "AE": 5, "VE": 534, "AF": 60, "IR": 260, "AM": 266, "AL": 5244, "VN": 3004, "AP": 3, "AR": 4487, "AU": 944, "AT": 1705, "IN": 7531, "TZ": 14, "AZ": 103, "IE": 2, "ID": 4399, "MY": 981}
    zyxel = {"BD": 6, "BE": 265, "BG": 16, "BA": 84, "BB": 1, "BN": 3, "BO": 223, "JP": 39, "BJ": 1, "BT": 1, "JM": 259, "JO": 22, "BR": 143, "BS": 1, "BY": 575, "RU": 41997, "RW": 1, "RS": 6, "RE": 12, "RO": 65, "GU": 4, "GT": 37, "GR": 123, "GP": 22, "BH": 1, "GF": 2, "GE": 4, "GB": 1079, "GA": 2, "GN": 2, "GL": 1, "OM": 3, "TN": 1, "HR": 38, "HT": 1, "HU": 84, "HK": 120, "HN": 152, "AD": 3, "PR": 1, "PT": 62, "PA": 12, "UY": 2, "PE": 1091, "PK": 6, "PH": 1602, "PL": 448, "ZM": 1, "EE": 11, "EG": 14, "ZA": 1354, "EC": 20, "AL": 6, "AO": 8, "EU": 1, "ET": 2, "ES": 722, "ME": 38, "MD": 8, "MG": 4, "MF": 2, "MA": 117, "MC": 6, "UZ": 37, "MO": 2, "MK": 31, "MU": 4, "MT": 1, "MW": 8, "MV": 1, "MQ": 12, "MR": 1, "UG": 6, "MY": 27, "MX": 4, "AT": 467, "FR": 2634, "AX": 1, "FI": 126, "FO": 1, "NL": 713, "NO": 712, "NA": 7, "NG": 3, "NZ": 3, "CH": 942, "CO": 38, "CN": 895, "CM": 1, "CL": 59, "CA": 265, "CD": 2, "CZ": 1523, "CY": 9, "CR": 21, "CV": 1, "CU": 6, "SY": 5, "KG": 53, "KH": 3, "SV": 9, "SK": 353, "KR": 175, "SI": 55, "KW": 3, "SN": 2, "KZ": 758, "SG": 38, "SE": 326, "DO": 3, "DM": 2, "DK": 672, "DE": 973556, "US": 2814, "TZ": 9, "LA": 2, "TW": 11524, "TT": 1, "TR": 1361, "LI": 3, "LV": 13, "LT": 12, "LU": 11, "TJ": 24, "LS": 1, "TH": 1526, "AE": 24, "VE": 89, "IS": 4, "IR": 472, "AM": 9, "IT": 1829, "VN": 39, "AR": 1248, "AU": 5, "IL": 7, "AW": 1, "IN": 130, "LB": 3, "AZ": 155, "IE": 65, "ID": 22, "UA": 2619, "QA": 1, "MZ": 1}
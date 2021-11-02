import time
import random


def bubbleSort(array):
    swapped = False
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return array


# Сортировка вставками
def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while array[j] > key and j >= 0:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


# Сортировка выбором
def selectionSort(array):
    for i in range(len(array) - 1):
        min_idx = i
        for idx in range(i + 1, len(array) - 1):
            if array[idx] < array[min_idx]:
                min_idx = idx
        array[i], array[min_idx] = array[min_idx], array[i]
    return array


# Пирамидальная сортировка
def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heapSort(array):
    n = len(array)
    for i in range(n // 2, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array


# Сортировка слиянием
def mergeSort(nums):
    if len(nums) == 1:
        return nums
    mid = (len(nums) - 1) // 2
    lst1 = mergeSort(nums[:mid + 1])
    lst2 = mergeSort(nums[mid + 1:])
    result = merge(lst1, lst2)
    return result


def merge(lst1, lst2):
    lst = []
    i = 0
    j = 0
    while (i <= len(lst1) - 1 and j <= len(lst2) - 1):
        if lst1[i] < lst2[j]:
            lst.append(lst1[i])
            i += 1
        else:
            lst.append(lst2[j])
            j += 1
    if i > len(lst1) - 1:
        while (j <= len(lst2) - 1):
            lst.append(lst2[j])
            j += 1
    else:
        while (i <= len(lst1) - 1):
            lst.append(lst1[i])
            i += 1
    return lst

    # Быстрая сортировка


def quickSort(array):
    if len(array) > 1:
        pivot = array.pop()
        grtr_lst, equal_lst, smlr_lst = [], [pivot], []
        for item in array:
            if item == pivot:
                equal_lst.append(item)
            elif item > pivot:
                grtr_lst.append(item)
            else:
                smlr_lst.append(item)
        return quickSort(smlr_lst) + equal_lst + quickSort(grtr_lst)
    else:
        return array


# Сортировка Шелла
def shellSort(array):
    startTime = time.time()
    n = len(array)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        interval //= 2
    endTime = time.time()

    return array


array = [
    [800, 901, 888, 791, 297, 334, 729, 818, 889, 683, 828, 146, 8, 359, 56, 941, 419, 662, 961, 679, 907, 394, 528,
     468, 431, 216, 848, 819, 227, 190, 490, 400, 434, 608, 217, 534, 366, 639, 445, 77, 286, 646, 497, 895, 491, 247,
     975, 236, 219, 269, 80, 560, 757, 798, 833, 682, 908, 925, 801, 127, 112, 87, 707, 674, 796, 310, 526, 990, 436,
     62, 571, 641, 727, 401, 656, 764, 850, 108, 317, 969, 73, 302, 413, 917, 404, 487, 99, 44, 928, 343, 584, 905, 94,
     292, 554, 471, 133, 700, 615, 736, 715, 340, 777, 257, 900, 929, 881, 737, 437, 769, 805, 119, 204, 739, 986, 450,
     352, 718, 326, 315, 797, 192, 259, 640, 790, 931, 2, 880, 643, 109, 978, 553, 846, 513, 810, 239, 756, 698, 187,
     740, 373, 184, 447, 362, 967, 845, 223, 316, 294, 744, 251, 132, 308, 327, 176, 345, 633, 738, 896, 12, 279, 185,
     175, 30, 202, 337, 564, 723, 82, 282, 817, 72, 500, 903, 696, 503, 635, 783, 98, 851, 592, 870, 766, 171, 520, 839,
     549, 303, 617, 709, 940, 163, 3, 602, 726, 81, 389, 789, 281, 834, 537, 937, 18, 649, 180, 722, 208, 983, 59, 507,
     618, 248, 743, 446, 691, 397, 457, 154, 330, 263, 249, 482, 713, 581, 265, 63, 758, 393, 972, 706, 725, 433, 284,
     655, 944, 959, 711, 361, 128, 567, 841, 919, 170, 753, 290, 563, 745, 989, 21, 53, 814, 532, 57, 228, 162, 911,
     466, 93, 631, 309, 392, 524, 398, 582, 11, 438, 893, 840, 637, 428, 370, 647, 342, 16, 938, 311, 530, 52, 926, 515,
     74, 274, 962, 432, 734, 386, 454, 519, 193, 448, 353, 728, 742, 365, 667, 661, 669, 970, 624, 201, 31, 621, 4, 653,
     668, 942, 150, 139, 189, 636, 781, 981, 806, 451, 222, 591, 114, 885, 467, 458, 439, 660, 609, 191, 416, 922, 498,
     322, 773, 958, 821, 847, 699, 982, 465, 762, 562, 785, 179, 508, 719, 39, 252, 155, 264, 992, 183, 724, 654, 952,
     476, 344, 368, 866, 874, 411, 1, 499, 174, 570, 999, 844, 234, 226, 266, 869, 897, 484, 523, 129, 377, 169, 996,
     364, 666, 587, 64, 673, 854, 652, 939, 280, 376, 75, 369, 86, 678, 794, 717, 629, 536, 260, 935, 650, 346, 759,
     157, 677, 203, 321, 779, 67, 772, 66, 915, 868, 92, 950, 258, 877, 379, 932, 254, 853, 703, 898, 811, 910, 795,
     712, 423, 307, 479, 141, 630, 200, 117, 589, 750, 751, 914, 716, 995, 90, 293, 299, 275, 115, 813, 277, 469, 835,
     360, 107, 577, 485, 440, 767, 231, 774, 663, 463, 291, 873, 181, 341, 160, 708, 319, 245, 787, 559, 765, 521, 47,
     971, 372, 347, 555, 145, 957, 328, 953, 619, 994, 420, 435, 538, 271, 105, 688, 285, 356, 694, 378, 195, 37, 24,
     540, 607, 233, 143, 473, 788, 824, 235, 924, 158, 45, 963, 382, 250, 721, 350, 407, 701, 632, 799, 255, 596, 493,
     444, 692, 131, 22, 710, 496, 388, 211, 993, 535, 51, 626, 137, 965, 14, 865, 830, 232, 749, 246, 803, 78, 531, 597,
     648, 475, 218, 182, 852, 590, 118, 312, 857, 610, 240, 578, 472, 283, 287, 61, 887, 144, 207, 510, 988, 544, 17,
     384, 26, 820, 486, 966, 261, 332, 501, 876, 573, 576, 96, 95, 268, 339, 906, 502, 603, 333, 89, 300, 68, 301, 103,
     55, 755, 863, 20, 442, 229, 792, 778, 38, 730, 804, 768, 985, 686, 161, 215, 456, 516, 918, 832, 946, 909, 864,
     558, 827, 104, 478, 336, 188, 464, 29, 168, 808, 822, 685, 462, 956, 41, 25, 916, 13, 15, 130, 149, 306, 658, 256,
     732, 136, 902, 213, 933, 470, 0, 525, 242, 214, 296, 173, 40, 826, 776, 657, 522, 680, 449, 565, 186, 557, 156,
     289, 253, 720, 948, 623, 960, 27, 348, 270, 363, 84, 83, 594, 410, 625, 120, 611, 754, 33, 424, 494, 355, 474, 412,
     102, 527, 495, 391, 402, 6, 125, 511, 954, 977, 225, 121, 771, 209, 34, 88, 396, 272, 976, 858, 802, 614, 23, 483,
     381, 58, 243, 912, 569, 153, 580, 415, 9, 687, 622, 71, 492, 65, 600, 879, 54, 151, 943, 533, 855, 945, 859, 949,
     551, 408, 964, 973, 998, 7, 295, 595, 575, 452, 860, 547, 675, 644, 968, 36, 97, 541, 267, 177, 809, 441, 843, 974,
     849, 32, 371, 430, 443, 997, 488, 586, 566, 461, 892, 19, 298, 205, 221, 984, 142, 542, 612, 198, 951, 836, 735,
     561, 429, 409, 752, 35, 741, 380, 164, 760, 262, 837, 770, 546, 812, 695, 598, 79, 891, 69, 651, 477, 568, 91, 329,
     645, 122, 505, 634, 883]]
arr = [random.sample(range(1000), 800)]

startTime = time.perf_counter()
shellSort(arr)
endTime = time.perf_counter()
totalTime = endTime - startTime
# print(f'%.9f' % totalTime)
startTime1 = time.perf_counter()
heapSort(arr)
endTime1 = time.perf_counter()
totalTime1 = endTime1 - startTime1
# print(f'%.9f' % totalTime1)
startTime2 = time.perf_counter()
selectionSort(arr)
endTime2 = time.perf_counter()
totalTime2 = endTime2 - startTime2
# print(f'%.9f' % totalTime2)
startTime3 = time.perf_counter()
insertionSort(arr)
endTime3 = time.perf_counter()
totalTime3 = endTime3 - startTime3
# print(f'%.9f' % totalTime3)
startTime4 = time.perf_counter()
bubbleSort(arr)
endTime4 = time.perf_counter()
totalTime4 = endTime4 - startTime4
# print(f'%.9f' % totalTime4)
startTime5 = time.perf_counter()
quickSort(arr)
endTime5 = time.perf_counter()
totalTime5 = endTime5 - startTime5
# print(f'%.9f' % totalTime5)
table = {"quicksort": f'%.9f' % totalTime5,
         "bubbles": f'%.9f' % totalTime4,
         "inserts": f'%.9f' % totalTime3,
         "selections": f'%.9f' % totalTime2,
         "heapsort": f'%.9f' % totalTime1,
         "shells": f'%.9f' % totalTime}
for key, value in table.items():
    print(key, ":", value)
"""Но на самомо деле результаты рознятся, так как при разных колиствах чисел в массиве результаты несколько иные
При очень больших числа баблсорт на моем ноутбуке крашится, а быстрая сортировка становится не совсем эффективной
Ну и мое железо не супер быстрое)"""

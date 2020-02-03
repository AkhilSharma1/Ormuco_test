def pad_with_zeros(l1, l2):
    '''
    Pads the shorter list with zeros to make it the same length as the longer list.

    Parameters:
    l1 (list) :list of strings
    l2 (list):list of strings

    Returns:
    tuple of padded lists
    '''
    list1_padded, list2_padded = l1, l2
    len_diff = len(l1) - len(l2)
    if len_diff > 0:
        list2_padded = l2 + ['0']*len_diff
    elif len_diff < 0:
        list1_padded = l1 + ['0']*abs(len_diff)

    return list1_padded, list2_padded


def cmp_verson(v1: str, v2: str):
    '''
    Compares two version strings.

    Parameters:
    v1 (str) : version string 1
    v2 (str) : version string 2

    Returns:
    int : 0 if both are equal, -1 if v1 < v2 , 1 if v1 > v2
    '''

    # both strings are equal
    if v1 == v2:
        return 0

    # try converting them to float and then compare them
    try:
        v_float1 = float(v1)
        v_float2 = float(v2)
        return compare_vals(v_float1, v_float2)

    except:
        # print('can"t convert to float . moving on ...')
        pass

    # split the version number strings each into a list of [major_ver,minor_ver,patch_ver]
    v1_split = v1.split('.', 2)
    v2_split = v2.split('.', 2)
    v1_split, v2_split = pad_with_zeros(v1_split, v2_split)

    # store the split values into respective variables
    major_v1, minor_v1, patch_v1 = int(
        v1_split[0]), int(v1_split[1]), v1_split[2]
    major_v2, minor_v2, patch_v2 = int(
        v2_split[0]), int(v2_split[1]), v2_split[2]

    # check if the major version number is equal
    if major_v1 != major_v2:
        return compare_vals(major_v1, major_v2)

    # check if the minor version number is equal
    if minor_v1 != minor_v2:
        return compare_vals(minor_v1, minor_v2)

    # check if patch versions have pre-release identifiers
    if "-" not in patch_v1 and "-" not in patch_v2:
        return compare_vals(int(patch_v1), int(patch_v2))

    # get only the patch version from the string of patch_ver_num+pre_rel_identifiers
    patch_v1_num = int(patch_v1.split('-')[0])
    patch_v2_num = int(patch_v2.split('-')[0])

    if patch_v1_num != patch_v2_num:
        return compare_vals(patch_v1_num, patch_v2_num)
    elif "-" not in patch_v1 and "-" in patch_v2:  # check if only one has pre-release identifiers
        return 1
    elif "-" not in patch_v2 and "-" in patch_v1:  # check if only one has pre-release identifiers
        return -1

    # both have pre-release identifiers
    pre_rel_v1 = patch_v1.split('-')[1]
    pre_rel_v2 = patch_v2.split('-')[1]

    all_pre_ident_v1 = pre_rel_v1.split('.')
    all_pre_ident_v2 = pre_rel_v2.split('.')

    all_pre_ident_v1, all_pre_ident_v2 = pad_with_zeros(
        all_pre_ident_v1, all_pre_ident_v2)

    # for each pre-release identifier, compare digits numerically
    # while compare others lexically in ASCII sort order
    for p1, p2 in zip(all_pre_ident_v1, all_pre_ident_v2):
        # when both are numeric
        if p1.isnumeric() and p2.isnumeric() and int(p1) != int(p2):
            return compare_vals(int(p1), int(p2))
        if p1.isnumeric() and p2.isnumeric() and int(p1) == int(p2):
            continue
        # a numeric pre-release ident is always of a lower priority than a non-numeric one
        if p1.isnumeric() and not p2.isnumeric():
            return -1
        if p2.isnumeric() and not p1.isnumeric():
            return 1

        # both are non-numeric, just compare strings
        if not p1.isnumeric() and not p2.isnumeric():
            if p1 == p2:
                continue
            elif p1 < p2:
                return -1
            else:
                return 1
    return 0


def compare_vals(num1: int, num2: int):
    if(num1 == num2):
        return 0
    return -1 if num1 < num2 else 1


if __name__ == '__main__':

    v1, v2 = "1.0.0-rc", "1.0.0-alpha"

    print(cmp_verson(v1, v2))
